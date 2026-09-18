"""Behavior tests for the package validator; fixtures never contact Git/providers."""
import importlib.util
import hashlib
import json
import shutil
import unittest
import uuid
from pathlib import Path

MODULE = Path(__file__).with_name("validate_package.py")
if MODULE.exists():
    spec = importlib.util.spec_from_file_location("validator", MODULE)
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    validate = validator.validate
else:
    # Missing implementation is an intentional failing assertion, not import noise.
    def validate(root):
        return ["validator not implemented"]

class PackageTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent / ".test-tmp" / f"r2team-240-test-{uuid.uuid4().hex}"
        self.root.mkdir(parents=True)
        self.addCleanup(shutil.rmtree, self.root, True)
        (self.root / "templates").mkdir()
        (self.root / "skills" / "r2team-coo").mkdir(parents=True)
        (self.root / "package.json").write_text(json.dumps({
            "protocol_version": "2.4",
            "bootstrap": "R2TEAM_MASTER.md",
            "required_files": ["START.md", "templates/Setup.md", "templates/TEAM.md", "templates/TASK-TEMPLATE.md", "skills/r2team-coo/SKILL.md"],
            "template_root": "templates"
        }), encoding="utf-8")
        self.put("START.md", "[Start](templates/Setup.md#new)\n")
        self.put("templates/Setup.md", '<a id="new"></a>\n# New\n\nReady.\n')
        self.put("templates/TEAM.md", """# TEAM
coo:
  mode: internal
  owner_executor_id: example-main
  watched_executor_ids: [example-main]
  separate_chat_offer: declined
  triggers:
    session_start: true
    before_idle: true
    heartbeat_enabled: false
""")
        self.put("templates/TASK-TEMPLATE.md", """# TASK
handoff_seq
previous_owner_executor_id
assigned_by_executor_id
result_to_executor_id
Authorized next transitions
registration_id
tracker_item
onboarding_result_to_executor_id
auto_accept_if
activation_mode
IMMEDIATE_RESERVED
QUEUED_AFTER_REGISTRATION
first_task_id
READY_FOR_ACTIVATION
""")
        self.put("skills/r2team-coo/SKILL.md", """# COO
executor-scoped assignment discovery
owner_executor_id
last_seen_default_branch_sha
shared provider actor
handoff_seq
result_to_executor_id
RETURNED_TO_PARENT
ACTION_FOUND_LOCAL
COO_MODE_AMBIGUOUS
REGISTRATION_READY
PM_ANSWER_REQUIRED
REGISTRATION_BLOCKED
""")

    def put(self, name, text):
        (self.root / name).write_text(text, encoding="utf-8")

    def test_valid_package(self):
        self.assertEqual([], validate(self.root))

    def test_missing_required_file_is_rejected(self):
        (self.root / "START.md").unlink()
        self.assertTrue(any("Missing required file: START.md" in e for e in validate(self.root)))

    def test_broken_link_is_rejected(self):
        self.put("START.md", "[Lost](missing.md)\n")
        self.assertTrue(any("Broken link" in e for e in validate(self.root)))

    def test_missing_anchor_is_rejected(self):
        self.put("START.md", "[Start](templates/Setup.md#unknown)\n")
        self.assertTrue(any("Missing anchor" in e for e in validate(self.root)))

    def test_closed_fences_ignore_example_links(self):
        self.put("START.md", "~~~markdown\n[example](not-created.md)\n~~~\n")
        self.assertEqual([], validate(self.root))

    def test_unclosed_fence_is_rejected(self):
        self.put("START.md", "```text\nexample\n")
        self.assertTrue(any("Unclosed fence" in e for e in validate(self.root)))

    def test_external_link_needs_no_network(self):
        self.put("START.md", "[Web](https://example.test/unreachable)\n")
        self.assertEqual([], validate(self.root))

    def test_template_cannot_depend_on_bundle_parent(self):
        self.put("templates/Setup.md", "[Outside](../START.md)\n")
        self.assertTrue(any("Nonportable template link" in e for e in validate(self.root)))

    def test_links_cannot_escape_package(self):
        self.put("START.md", "[Outside](../secret.md)\n")
        self.assertTrue(any("Escaping link" in e for e in validate(self.root)))

    def test_real_local_registry_must_not_ship(self):
        (self.root / ".codex-local").mkdir()
        self.put(".codex-local/THREAD_REGISTRY.md", "private mapping\n")
        self.assertTrue(any("Local runtime data" in e for e in validate(self.root)))

    def test_wrong_version_is_rejected(self):
        config = json.loads((self.root / "package.json").read_text())
        config["protocol_version"] = "2.1"
        self.put("package.json", json.dumps(config))
        self.assertTrue(any("Expected protocol_version 2.4" in e for e in validate(self.root)))

    def test_coo_must_discover_new_task_ids_by_executor(self):
        self.put("skills/r2team-coo/SKILL.md", "# COO\nOnly inspect known task IDs.\n")
        self.assertTrue(any("Missing COO assignment-discovery marker" in e
                            for e in validate(self.root)))

    def test_task_template_must_define_durable_baton(self):
        self.put("templates/TASK-TEMPLATE.md", "# TASK\nowner_executor_id\n")
        self.assertTrue(any("Missing durable-baton marker" in e
                            for e in validate(self.root)))

    def test_team_requires_one_coo_mode_for_each_participant(self):
        self.put("templates/TEAM.md", "# TEAM\nCOO is optional.\n")
        self.assertTrue(any("Missing mandatory COO configuration marker" in e
                            for e in validate(self.root)))

    def test_task_template_requires_closed_onboarding_route(self):
        self.put("templates/TASK-TEMPLATE.md", """# TASK
handoff_seq
previous_owner_executor_id
assigned_by_executor_id
result_to_executor_id
Authorized next transitions
""")
        self.assertTrue(any("Missing onboarding-route marker" in e
                            for e in validate(self.root)))

    def test_onboarding_route_requires_pre_authorized_acceptance(self):
        text = (self.root / "templates/TASK-TEMPLATE.md").read_text(encoding="utf-8")
        self.put("templates/TASK-TEMPLATE.md", text.replace("auto_accept_if\n", ""))
        self.assertTrue(any("Missing onboarding-route marker: auto_accept_if" in e
                            for e in validate(self.root)))

    def test_coo_must_report_registration_events_to_parent(self):
        text = (self.root / "skills/r2team-coo/SKILL.md").read_text(encoding="utf-8")
        self.put("skills/r2team-coo/SKILL.md", text.replace("REGISTRATION_READY\n", ""))
        self.assertTrue(any("Missing COO registration-event marker" in e
                            for e in validate(self.root)))

    def test_separate_package_revision_is_rejected(self):
        config = json.loads((self.root / "package.json").read_text())
        config["package_revision"] = 1
        self.put("package.json", json.dumps(config))
        self.assertTrue(any("protocol_version is the sole release identifier" in e
                            for e in validate(self.root)))

    def test_invalid_utf8_is_rejected(self):
        (self.root / "START.md").write_bytes(b"\xff")
        self.assertTrue(any("Invalid UTF-8" in e for e in validate(self.root)))

    def test_manifest_cannot_escape_root(self):
        self.put("package.json", json.dumps({
            "protocol_version": "2.4", "bootstrap": "R2TEAM_MASTER.md",
            "required_files": ["../outside.md"],
            "template_root": "templates"
        }))
        self.assertTrue(any("Unsafe manifest path" in e for e in validate(self.root)))

    def test_duplicate_required_paths_rejected(self):
        self.put("package.json", json.dumps({
            "protocol_version": "2.4", "bootstrap": "R2TEAM_MASTER.md",
            "required_files": ["START.md", "START.md"],
            "template_root": "templates"
        }))
        self.assertTrue(any("Duplicate required file" in e for e in validate(self.root)))

    def test_wrong_bootstrap_is_rejected(self):
        config = json.loads((self.root / "package.json").read_text())
        config["bootstrap"] = "START.md"
        self.put("package.json", json.dumps(config))
        self.assertTrue(any("Expected bootstrap R2TEAM_MASTER.md" in e
                            for e in validate(self.root)))

    def pin_hashes(self):
        config = json.loads((self.root / "package.json").read_text())
        config["sha256"] = {name: hashlib.sha256((self.root / name).read_bytes()).hexdigest()
                            for name in config["required_files"]}
        self.put("package.json", json.dumps(config))

    def test_pinned_package_passes(self):
        self.pin_hashes()
        self.assertEqual([], validate(self.root))

    def test_modified_payload_is_rejected(self):
        self.pin_hashes()
        self.put("templates/Setup.md", '<a id="new"></a>\nChanged after pinning.\n')
        self.assertTrue(any("SHA-256 mismatch" in e for e in validate(self.root)))

    def test_incomplete_hash_manifest_is_rejected(self):
        self.pin_hashes()
        config = json.loads((self.root / "package.json").read_text())
        del config["sha256"]["START.md"]
        self.put("package.json", json.dumps(config))
        self.assertTrue(any("Missing SHA-256" in e for e in validate(self.root)))

if __name__ == "__main__":
    unittest.main(verbosity=2)
