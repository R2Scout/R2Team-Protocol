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
        (self.root / "skills" / "r2team-work").mkdir(parents=True)
        (self.root / "skills" / "r2team-workspace").mkdir(parents=True)
        (self.root / "package.json").write_text(json.dumps({
            "protocol_version": "2.6",
            "bootstrap": "R2TEAM_MASTER.md",
            "skills": ["r2team", "r2team-work", "r2team-coo", "r2team-audit", "r2team-workspace"],
            "required_files": [
                "START.md",
                "templates/Setup.md",
                "templates/CODEX_TEAM_PROTOCOL.md",
                "templates/COMMANDS.md",
                "templates/LOCAL_REGISTRY_TEMPLATE.md",
                "templates/TEAM.md",
                "templates/TASK-TEMPLATE.md",
                "skills/r2team-coo/SKILL.md",
                "skills/r2team-work/SKILL.md",
                "skills/r2team-workspace/SKILL.md"
            ],
            "template_root": "templates"
        }), encoding="utf-8")
        self.put("START.md", "[Start](templates/Setup.md#new)\n")
        self.put("templates/Setup.md", '<a id="new"></a>\n# New\n\nReady.\n')
        self.put("templates/CODEX_TEAM_PROTOCOL.md", """# Protocol
TASK identity
candidate identity
workspace lease identity
ALLOCATION_BLOCKED
RETAINED_PROTECTED
provider read-back
sanitized manifest
Any blocking or nonterminal lease blocks administrative completion
explicit removal authority
""")
        self.put("templates/COMMANDS.md", """# Commands
$r2team-workspace status
$r2team-workspace open
$r2team-workspace close
$r2team-workspace doctor
""")
        self.put("templates/LOCAL_REGISTRY_TEMPLATE.md", """# Local registry
lease_id
physical_path
observed_size_bytes
native_resources
last_observed_at
""")
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
workspace_lifecycle
max_active_per_task
max_mutable_per_executor_task_purpose
project_target_active
project_hard_cap_active
free_space_gib
placement_classes
root_aliases
retention_classes
closure_methods
reconciliation_owner_executor_id
""")
        self.put("templates/TASK-TEMPLATE.md", """# TASK
handoff_seq
owner_route
previous_owner_executor_id
assigned_by_executor_id
result_to_executor_id
result_to_route
delivery_policy
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
workspace_policy
workspace_exceptions
workspace_leases
workspace_disposition
closure_owner_executor_id
retention_class
review_date
recovery_ref
close_receipt_ref
candidate_dispositions
artifact_manifests
close_receipts
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
        self.put("skills/r2team-work/SKILL.md", """---
name: r2team-work
description: Run assigned work without hidden workspace mutation.
---
# Work
Workspace lifecycle operations route to `r2team-workspace`.
""")
        self.put("skills/r2team-workspace/SKILL.md", """---
name: r2team-workspace
description: Inspect and govern R2Team workspace leases with safe preflight and recoverable closure.
---
# Workspace
$r2team-workspace status
$r2team-workspace open
$r2team-workspace close
$r2team-workspace doctor
status and doctor are read-only
allocation preflight
evidence and custody preflight
explicit removal authority
RETAINED_PROTECTED
ALLOCATION_BLOCKED
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
        self.assertTrue(any("Expected protocol_version 2.6" in e for e in validate(self.root)))

    def test_workspace_skill_is_required(self):
        config = json.loads((self.root / "package.json").read_text())
        config["skills"].remove("r2team-workspace")
        config["required_files"].remove("skills/r2team-workspace/SKILL.md")
        self.put("package.json", json.dumps(config))
        self.assertTrue(any("Missing packaged workspace skill" in e
                            for e in validate(self.root)))

    def test_workspace_skill_requires_safe_command_boundaries(self):
        self.put("skills/r2team-workspace/SKILL.md", """---
name: r2team-workspace
description: Close workspaces.
---
# Workspace
$r2team-workspace close
""")
        errors = validate(self.root)
        self.assertTrue(any("Missing workspace-skill marker" in e for e in errors))

    def test_hash_consistent_automatic_force_delete_is_rejected(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        self.put("skills/r2team-workspace/SKILL.md", path.read_text(encoding="utf-8") +
                 "\nDoctor automatically force-deletes every workspace older than one day "
                 "without ownership or approval.\n")
        self.pin_hashes()
        self.assertTrue(any("Unsafe automatic lifecycle action" in e
                            for e in validate(self.root)))

    def test_hash_consistent_private_path_and_thread_id_are_rejected(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        self.put("skills/r2team-workspace/SKILL.md", path.read_text(encoding="utf-8") +
                 "\nObserved path: " + "C:" + "\\Users\\ActualPerson\\private-worktree\n" +
                 "Observed thread: " + "01a15d0b-" +
                 "0ce6-7173-9f51-c721617235ee\n")
        self.pin_hashes()
        errors = validate(self.root)
        self.assertTrue(any("Populated machine-private path" in e for e in errors))
        self.assertTrue(any("Actual local thread ID" in e for e in errors))

    def test_hash_consistent_credential_marker_is_rejected(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        self.put("skills/r2team-workspace/SKILL.md", path.read_text(encoding="utf-8") +
                 "\nTo" + "ken" + ": " + "gh" + "p_" +
                 "abcdefghijklmnopqrstuvwxyz1234567890\n")
        self.pin_hashes()
        self.assertTrue(any("Credential-like material" in e
                            for e in validate(self.root)))

    def test_hash_consistent_api_and_client_secret_assignments_are_rejected(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        payload = ("\n" + "OPENAI_" + "API_KEY" + "=" + "sk-" +
                   "dummy-not-secret\n" + "AZURE_CLIENT_" + "SECRET" +
                   "=" + "dummy-client-secret\n")
        self.put("skills/r2team-workspace/SKILL.md",
                 path.read_text(encoding="utf-8") + payload)
        self.pin_hashes()
        self.assertTrue(any("Credential-like material" in e
                            for e in validate(self.root)))

    def test_hash_consistent_bearer_token_is_rejected(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        payload = "\nAuthorization: " + "Bear" + "er dummy-token-value\n"
        self.put("skills/r2team-workspace/SKILL.md",
                 path.read_text(encoding="utf-8") + payload)
        self.pin_hashes()
        self.assertTrue(any("Credential-like material" in e
                            for e in validate(self.root)))

    def test_hash_consistent_generic_secret_and_token_are_rejected(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        payload = ("\nSERVICE_" + "SECRET" + "=" +
                   "dummy-service-secret\n" + "DEPLOY_" + "TOKEN" +
                   "=" + "dummy-deploy-token\n")
        self.put("skills/r2team-workspace/SKILL.md",
                 path.read_text(encoding="utf-8") + payload)
        self.pin_hashes()
        self.assertTrue(any("Credential-like material" in e
                            for e in validate(self.root)))

    def test_hash_consistent_bare_credential_names_are_rejected(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        payload = ("\n" + "TO" + "KEN=" + "dummy-token\n" +
                   "PASS" + "WORD=" + "dummy-password\n" +
                   "API_" + "KEY=" + "dummy-api-key\n" +
                   "PRIVATE_" + "KEY=" + "dummy-private-key\n")
        self.put("skills/r2team-workspace/SKILL.md",
                 path.read_text(encoding="utf-8") + payload)
        self.pin_hashes()
        self.assertTrue(any("Credential-like material" in e
                            for e in validate(self.root)))

    def test_hash_consistent_cloud_secret_access_key_is_rejected(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        payload = ("\nAWS_" + "SECRET_ACCESS_KEY" + "=" +
                   "dummy-cloud-secret\n")
        self.put("skills/r2team-workspace/SKILL.md",
                 path.read_text(encoding="utf-8") + payload)
        self.pin_hashes()
        self.assertTrue(any("Credential-like material" in e
                            for e in validate(self.root)))

    def test_explicit_credential_placeholders_are_allowed(self):
        path = self.root / "skills/r2team-workspace/SKILL.md"
        payload = ("\n" + "OPENAI_" + "API_KEY" + "=<set-locally>\n" +
                   "AZURE_CLIENT_" + "SECRET" + "=${AZURE_CLIENT_SECRET}\n" +
                   "SERVICE_" + "TOKEN" + "=null\n" +
                   "DEPLOY_" + "TOKEN" + "=not-configured\n")
        self.put("skills/r2team-workspace/SKILL.md",
                 path.read_text(encoding="utf-8") + payload)
        self.pin_hashes()
        self.assertFalse(any("Credential-like material" in e
                             for e in validate(self.root)))

    def test_r2team_work_cannot_hide_workspace_mutation(self):
        self.put("skills/r2team-work/SKILL.md", """---
name: r2team-work
description: Run assigned work.
---
# Work
This command directly allocates and closes workspaces.
""")
        self.assertTrue(any("Missing r2team-work workspace boundary" in e
                            for e in validate(self.root)))

    def test_lifecycle_templates_require_portable_fields(self):
        self.put("templates/TASK-TEMPLATE.md", "# TASK\nowner_executor_id\n")
        errors = validate(self.root)
        self.assertTrue(any("Missing workspace TASK marker" in e for e in errors))

    def test_task_template_requires_append_only_workspace_history(self):
        text = (self.root / "templates/TASK-TEMPLATE.md").read_text(encoding="utf-8")
        self.put("templates/TASK-TEMPLATE.md",
                 text.replace("candidate_dispositions\n", ""))
        self.assertTrue(any("Missing workspace TASK marker: candidate_dispositions" in e
                            for e in validate(self.root)))

    def test_team_chat_relocation_payload_is_rejected(self):
        self.put("templates/COMMANDS.md", "$r2team relocate-chat PM to another thread\n")
        self.assertTrue(any("Relocation behavior is outside R2Team 2.6" in e
                            for e in validate(self.root)))

    def test_coo_must_discover_new_task_ids_by_executor(self):
        self.put("skills/r2team-coo/SKILL.md", "# COO\nOnly inspect known task IDs.\n")
        self.assertTrue(any("Missing COO assignment-discovery marker" in e
                            for e in validate(self.root)))

    def test_task_template_must_define_durable_baton(self):
        self.put("templates/TASK-TEMPLATE.md", "# TASK\nowner_executor_id\n")
        self.assertTrue(any("Missing durable-baton marker" in e
                            for e in validate(self.root)))

    def test_task_template_requires_explicit_return_route_and_delivery_policy(self):
        text = (self.root / "templates/TASK-TEMPLATE.md").read_text(encoding="utf-8")
        self.put("templates/TASK-TEMPLATE.md", text.replace("owner_route\n", "")
                                               .replace("result_to_route\n", "")
                                               .replace("delivery_policy\n", ""))
        errors = validate(self.root)
        self.assertTrue(any("Missing durable-baton marker: owner_route" in e
                            for e in errors))
        self.assertTrue(any("Missing durable-baton marker: result_to_route" in e
                            for e in errors))
        self.assertTrue(any("Missing durable-baton marker: delivery_policy" in e
                            for e in errors))

    def test_team_requires_one_coo_mode_for_each_participant(self):
        self.put("templates/TEAM.md", "# TEAM\nCOO is optional.\n")
        self.assertTrue(any("Missing mandatory COO configuration marker" in e
                            for e in validate(self.root)))

    def test_team_requires_workspace_policy(self):
        text = (self.root / "templates/TEAM.md").read_text(encoding="utf-8")
        self.put("templates/TEAM.md", text.replace("max_active_per_task\n", ""))
        self.assertTrue(any("Missing workspace TEAM marker: max_active_per_task" in e
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
