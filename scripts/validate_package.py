"""Read-only structural checks for the distributable R2Team 2.6 package."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

def validate(root):
    root = Path(root).resolve()
    errors = []
    try:
        manifest = json.loads((root / "package.json").read_text(encoding="utf-8"))
        required = manifest["required_files"]
        template_name = manifest["template_root"]
        if not isinstance(required, list) or not all(isinstance(x, str) for x in required):
            raise ValueError("required_files must be a list of paths")
        if not isinstance(template_name, str):
            raise ValueError("template_root must be a path")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f"Invalid package manifest: {exc}"]
    if manifest.get("protocol_version") != "2.6":
        errors.append("Expected protocol_version 2.6")
    if manifest.get("bootstrap") != "R2TEAM_MASTER.md":
        errors.append("Expected bootstrap R2TEAM_MASTER.md")
    if "package_revision" in manifest:
        errors.append("Remove package_revision: protocol_version is the sole release identifier")
    skills = manifest.get("skills", [])
    workspace_skill_path = "skills/r2team-workspace/SKILL.md"
    if "r2team-workspace" not in skills or workspace_skill_path not in required:
        errors.append("Missing packaged workspace skill: r2team-workspace")
    if any(re.search(r"(^|/)(team[_-]?migration|chat[_-]?relocation)(/|\.|$)", name,
                     flags=re.IGNORECASE) for name in required):
        errors.append("Relocation behavior is outside R2Team 2.6")
    template_root = (root / template_name).resolve()
    if not template_root.is_relative_to(root):
        return errors + ["Unsafe manifest path: template_root"]
    seen = set()
    required_texts = {}
    hashes = manifest.get("sha256")
    if hashes is not None and not isinstance(hashes, dict):
        return errors + ["Invalid SHA-256 map"]
    for name in required:
        path = (root / name).resolve()
        if not path.is_relative_to(root) or Path(name).is_absolute():
            errors.append(f"Unsafe manifest path: {name}")
            continue
        if name in seen:
            errors.append(f"Duplicate required file: {name}")
        seen.add(name)
        if not path.is_file():
            errors.append(f"Missing required file: {name}")
            continue
        try:
            required_texts[name] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"Invalid UTF-8 or unreadable required file: {name}")
        if hashes is not None:
            expected = hashes.get(name)
            if expected is None:
                errors.append(f"Missing SHA-256: {name}")
            elif not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
                errors.append(f"Invalid SHA-256: {name}")
            else:
                try:
                    actual = hashlib.sha256(path.read_bytes()).hexdigest()
                    if actual != expected:
                        errors.append(f"SHA-256 mismatch: {name}")
                except OSError:
                    errors.append(f"Unreadable payload: {name}")

    unsafe_patterns = (
        re.compile(r"\b(?:automatic(?:ally)?|auto)\s+(?:force[-\s]*)?"
                   r"(?:delete|remove|clean(?:up)?|terminate|stop|kill|archive|revoke)\w*",
                   re.IGNORECASE),
        re.compile(r"\bforce[-\s]?(?:delete|remove|clean(?:up)?|terminate|stop|kill|archive|revoke)\w*",
                   re.IGNORECASE),
        re.compile(r"\b(?:delete|remove|clean(?:up)?|terminate|stop|kill|archive|revoke)\w*"
                   r"[^.\n]{0,120}\bwithout\s+(?:ownership|approval|authority|preflight)\b",
                   re.IGNORECASE),
        re.compile(r"\b(?:age|merge|receipt|budget|disk pressure|review date|free space)\b"
                   r"[^.\n]{0,100}\b(?:authorizes?|grants?|permits?)\b"
                   r"[^.\n]{0,80}\b(?:delete|remove|cleanup|terminate|kill|archive|revoke)\b",
                   re.IGNORECASE),
    )
    credential_pattern = re.compile(
        r"(?:ghp\x5f[A-Za-z0-9]{20,}|github_pat\x5f[A-Za-z0-9_]{20,}|"
        r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|"
        r"\bsk-[A-Za-z0-9_-]{8,})")
    credential_assignment_pattern = re.compile(
        r"(?im)\b[A-Z][A-Z0-9_]*(?:API_KEY|SECRET|TOKEN|PASSWORD|PRIVATE_KEY)\b"
        r"\s*[:=]\s*([^\r\n#,]+)")
    bearer_pattern = re.compile(
        r"(?im)\bAuthorization\s*:\s*Bearer\s+([^\s,;]+)")
    thread_pattern = re.compile(
        r"\b01[a-f0-9]{6}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b",
        re.IGNORECASE)
    windows_path_pattern = re.compile(r"\b[A-Za-z]:\\[^\r\n`\"']+")
    unix_home_pattern = re.compile(r"/(?:home|Users)/[^/\s<>]+/[^^\s`\"']*")

    for name, text in required_texts.items():
        credential_found = credential_pattern.search(text) is not None
        for pattern in (credential_assignment_pattern, bearer_pattern):
            for match in pattern.finditer(text):
                value = match.group(1).strip().strip("\"'")
                lowered = value.lower()
                placeholder = (
                    not value or
                    lowered in {"null", "none", "not_configured", "redacted"} or
                    (value.startswith("<") and value.endswith(">")) or
                    (value.startswith("${") and value.endswith("}")) or
                    (value.startswith("%") and value.endswith("%"))
                )
                if not placeholder:
                    credential_found = True
                    break
            if credential_found:
                break
        if credential_found:
            errors.append(f"Credential-like material in required file: {name}")
        if thread_pattern.search(text):
            errors.append(f"Actual local thread ID in required file: {name}")
        private_path = False
        for match in windows_path_pattern.finditer(text):
            value = match.group(0)
            if "<" not in value and "${" not in value and "%" not in value:
                private_path = True
                break
        if not private_path:
            private_path = any("<" not in match.group(0)
                               for match in unix_home_pattern.finditer(text))
        if private_path:
            errors.append(f"Populated machine-private path in required file: {name}")
        if name.lower().endswith(".md"):
            for pattern in unsafe_patterns:
                match = pattern.search(text)
                if not match:
                    continue
                line_start = text.rfind("\n", 0, match.start()) + 1
                prefix = text[line_start:match.start()].lower()
                if re.search(r"\b(?:must not|does not|do not|never|no command)\b", prefix):
                    continue
                errors.append(f"Unsafe automatic lifecycle action in required file: {name}")
                break
    for path in root.rglob("*"):
        if path.name == ".codex-local":
            errors.append(f"Local runtime data must not ship: {path.relative_to(root)}")

    texts = {}
    for path in root.rglob("*.md"):
        if not path.resolve().is_relative_to(root):
            errors.append(f"Escaping Markdown path: {path}")
            continue
        try:
            texts[path.resolve()] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"Invalid UTF-8 or unreadable file: {path.relative_to(root)}")
    for path, text in texts.items():
        fence = None
        for line in text.splitlines():
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if marker:
                token = marker.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
                continue
            if fence:
                continue
            for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", line):
                target = match.group(1).strip("<>")
                parts = urlsplit(target)
                if parts.scheme or parts.netloc:
                    continue
                linked = (path.parent / unquote(parts.path)).resolve() if parts.path else path
                if not linked.is_relative_to(root):
                    errors.append(f"Escaping link in {path.name}: {target}")
                    continue
                if path.is_relative_to(template_root) and not linked.is_relative_to(template_root):
                    errors.append(f"Nonportable template link in {path.name}: {target}")
                if not linked.is_file():
                    errors.append(f"Broken link in {path.name}: {target}")
                elif parts.fragment:
                    other = texts.get(linked, "")
                    anchor = unquote(parts.fragment)
                    if f'id="{anchor}"' not in other:
                        errors.append(f"Missing anchor in {path.name}: {target}")
        if fence:
            errors.append(f"Unclosed fence: {path.relative_to(root)}")

    coo_skill = root / "skills" / "r2team-coo" / "SKILL.md"
    if coo_skill.is_file():
        coo_text = texts.get(coo_skill.resolve(), "")
        for marker in (
            "executor-scoped assignment discovery",
            "owner_executor_id",
            "last_seen_default_branch_sha",
            "shared provider actor",
            "handoff_seq",
            "result_to_executor_id",
            "RETURNED_TO_PARENT",
            "ACTION_FOUND_LOCAL",
            "COO_MODE_AMBIGUOUS",
        ):
            if marker not in coo_text:
                errors.append(f"Missing COO assignment-discovery marker: {marker}")
        for marker in (
            "REGISTRATION_READY",
            "PM_ANSWER_REQUIRED",
            "REGISTRATION_BLOCKED",
        ):
            if marker not in coo_text:
                errors.append(f"Missing COO registration-event marker: {marker}")

    team_template = root / "templates" / "TEAM.md"
    if team_template.is_file():
        team_text = texts.get(team_template.resolve(), "")
        for marker in (
            "mode: internal",
            "owner_executor_id",
            "watched_executor_ids",
            "separate_chat_offer",
            "session_start",
            "before_idle",
            "heartbeat_enabled: false",
        ):
            if marker not in team_text:
                errors.append(f"Missing mandatory COO configuration marker: {marker}")
        for marker in (
            "workspace_lifecycle",
            "max_active_per_task",
            "max_mutable_per_executor_task_purpose",
            "project_target_active",
            "project_hard_cap_active",
            "free_space_gib",
            "placement_classes",
            "root_aliases",
            "retention_classes",
            "closure_methods",
            "reconciliation_owner_executor_id",
        ):
            if marker not in team_text:
                errors.append(f"Missing workspace TEAM marker: {marker}")

    task_template = root / "templates" / "TASK-TEMPLATE.md"
    if task_template.is_file():
        task_text = texts.get(task_template.resolve(), "")
        for marker in (
            "handoff_seq",
            "owner_route",
            "previous_owner_executor_id",
            "assigned_by_executor_id",
            "result_to_executor_id",
            "result_to_route",
            "delivery_policy",
            "Authorized next transitions",
        ):
            if marker not in task_text:
                errors.append(f"Missing durable-baton marker: {marker}")
        for marker in (
            "registration_id",
            "tracker_item",
            "onboarding_result_to_executor_id",
            "auto_accept_if",
            "activation_mode",
            "IMMEDIATE_RESERVED",
            "QUEUED_AFTER_REGISTRATION",
            "first_task_id",
            "READY_FOR_ACTIVATION",
        ):
            if marker not in task_text:
                errors.append(f"Missing onboarding-route marker: {marker}")
        for marker in (
            "workspace_policy",
            "workspace_exceptions",
            "workspace_leases",
            "workspace_disposition",
            "closure_owner_executor_id",
            "retention_class",
            "review_date",
            "recovery_ref",
            "close_receipt_ref",
            "candidate_dispositions",
            "artifact_manifests",
            "close_receipts",
        ):
            if marker not in task_text:
                errors.append(f"Missing workspace TASK marker: {marker}")

    protocol = root / "templates" / "CODEX_TEAM_PROTOCOL.md"
    if protocol.is_file():
        protocol_text = texts.get(protocol.resolve(), "")
        for marker in (
            "TASK identity",
            "candidate identity",
            "workspace lease identity",
            "ALLOCATION_BLOCKED",
            "RETAINED_PROTECTED",
            "provider read-back",
            "sanitized manifest",
            "blocks administrative completion",
            "explicit removal authority",
        ):
            if marker not in protocol_text:
                errors.append(f"Missing workspace protocol marker: {marker}")

    local_registry = root / "templates" / "LOCAL_REGISTRY_TEMPLATE.md"
    if local_registry.is_file():
        registry_text = texts.get(local_registry.resolve(), "")
        for marker in (
            "lease_id",
            "physical_path",
            "observed_size_bytes",
            "native_resources",
            "last_observed_at",
        ):
            if marker not in registry_text:
                errors.append(f"Missing local workspace registry marker: {marker}")

    workspace_skill = root / workspace_skill_path
    if workspace_skill.is_file():
        workspace_text = texts.get(workspace_skill.resolve(), "")
        for marker in (
            "name: r2team-workspace",
            "$r2team-workspace status",
            "$r2team-workspace open",
            "$r2team-workspace close",
            "$r2team-workspace doctor",
            "status and doctor are read-only",
            "allocation preflight",
            "evidence and custody preflight",
            "explicit removal authority",
            "RETAINED_PROTECTED",
            "ALLOCATION_BLOCKED",
        ):
            if marker not in workspace_text:
                errors.append(f"Missing workspace-skill marker: {marker}")

    work_skill = root / "skills" / "r2team-work" / "SKILL.md"
    if work_skill.is_file():
        work_text = texts.get(work_skill.resolve(), "")
        if "`r2team-workspace`" not in work_text:
            errors.append("Missing r2team-work workspace boundary: route lifecycle operations to r2team-workspace")

    commands = root / "templates" / "COMMANDS.md"
    if commands.is_file():
        commands_text = texts.get(commands.resolve(), "")
        for marker in (
            "$r2team-workspace status",
            "$r2team-workspace open",
            "$r2team-workspace close",
            "$r2team-workspace doctor",
        ):
            if marker not in commands_text:
                errors.append(f"Missing workspace command marker: {marker}")
        if re.search(r"\$r2team\s+(?:relocate-chat|migrate-team|migrate-chat)\b",
                     commands_text, flags=re.IGNORECASE):
            errors.append("Relocation behavior is outside R2Team 2.6")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    errors = validate(args.package)
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: package structure, hashes, local Markdown links, and lifecycle safety/privacy guards. No runtime/provider/skill execution tested.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
