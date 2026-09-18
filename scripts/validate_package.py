"""Read-only structural checks for the distributable R2Team 2.4 package."""
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
    if manifest.get("protocol_version") != "2.4":
        errors.append("Expected protocol_version 2.4")
    if manifest.get("bootstrap") != "R2TEAM_MASTER.md":
        errors.append("Expected bootstrap R2TEAM_MASTER.md")
    if "package_revision" in manifest:
        errors.append("Remove package_revision: protocol_version is the sole release identifier")
    template_root = (root / template_name).resolve()
    if not template_root.is_relative_to(root):
        return errors + ["Unsafe manifest path: template_root"]
    seen = set()
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
        elif hashes is not None:
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

    task_template = root / "templates" / "TASK-TEMPLATE.md"
    if task_template.is_file():
        task_text = texts.get(task_template.resolve(), "")
        for marker in (
            "handoff_seq",
            "previous_owner_executor_id",
            "assigned_by_executor_id",
            "result_to_executor_id",
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
    print("PASS: package structure and local Markdown links. No runtime/provider/skill execution tested.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
