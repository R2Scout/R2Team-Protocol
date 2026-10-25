"""Deterministic R2Team 2.6 workspace lifecycle behavior tests."""
import unittest

from workspace_policy import (
    allocation_decision,
    closure_decision,
    completion_decision,
    evidence_decision,
    result_record,
    transfer_decision,
)


def valid_exception(**overrides):
    value = {
        "task_id": "TASK-42",
        "reason": "changed exact base requires a disjoint compatibility lane",
        "lease_id": "lease-review-2",
        "owner": "qa-main",
        "purpose": "qa",
        "capacity_evidence": "destination 80 GiB free",
        "review_date": "2026-11-01",
        "changed_base": True,
        "custody_known": True,
        "disjoint_lane": True,
        "candidate_preserved": True,
        "recovery_rule": "retain protected candidate and return to the recorded owner",
    }
    value.update(overrides)
    return value


class WorkspacePolicyTests(unittest.TestCase):
    def test_task_revision_reuses_compatible_author_lease(self):
        self.assertEqual("REUSE_EXISTING", allocation_decision(
            active_task=1, project_active=20, free_gib=100, compatible_lease=True))

    def test_fourth_task_workspace_is_blocked(self):
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=3, project_active=20, free_gib=100))

    def test_project_hard_cap_blocks_without_cleanup(self):
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=1, project_active=150, free_gib=100))

    def test_reuse_only_capacity_blocks_new_placement(self):
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=1, project_active=20, free_gib=35))

    def test_owner_approved_recovery_allocation_is_bounded(self):
        self.assertEqual("ALLOW_RECOVERY", allocation_decision(
            active_task=1, project_active=20, free_gib=20,
            recovery=True, exception=valid_exception(), today="2026-10-25"))

    def test_recovery_band_rejects_ordinary_allocation(self):
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=1, project_active=20, free_gib=20))

    def test_below_floor_blocks_even_recovery(self):
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=1, project_active=20, free_gib=10,
            recovery=True, exception=valid_exception(), today="2026-10-25"))

    def test_fourth_workspace_with_complete_exception_is_allowed(self):
        self.assertEqual("ALLOW_EXCEPTION", allocation_decision(
            active_task=3, project_active=20, free_gib=80,
            exception=valid_exception(), today="2026-10-25"))

    def test_exception_missing_required_field_is_blocked(self):
        for field in (
                "task_id", "reason", "lease_id", "owner", "purpose",
                "capacity_evidence", "review_date", "changed_base",
                "custody_known", "disjoint_lane", "candidate_preserved",
                "recovery_rule"):
            with self.subTest(field=field):
                self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
                    active_task=3, project_active=20, free_gib=80,
                    exception=valid_exception(**{field: ""}),
                    today="2026-10-25"))

    def test_expired_exception_is_blocked(self):
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=3, project_active=20, free_gib=80,
            exception=valid_exception(review_date="2026-10-24"),
            today="2026-10-25"))

    def test_exception_requires_changed_base_known_custody_disjoint_lane_and_preserved_candidate(self):
        for field in ("changed_base", "custody_known", "disjoint_lane",
                      "candidate_preserved"):
            with self.subTest(field=field):
                self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
                    active_task=3, project_active=20, free_gib=80,
                    exception=valid_exception(**{field: False}),
                    today="2026-10-25"))

    def test_exception_never_bypasses_hard_cap_disk_floor_or_single_writer(self):
        exception = valid_exception()
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=3, project_active=150, free_gib=80,
            exception=exception, today="2026-10-25"))
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=3, project_active=20, free_gib=10,
            exception=exception, today="2026-10-25"))
        self.assertEqual("ALLOCATION_BLOCKED", allocation_decision(
            active_task=3, project_active=20, free_gib=80,
            active_mutable_for_purpose=1,
            exception=exception, today="2026-10-25"))

    def test_verdict_and_workspace_disposition_remain_separate(self):
        self.assertEqual(
            {"verdict": "PASS", "workspace_disposition": "BLOCKED_DIRTY"},
            result_record("PASS", "BLOCKED_DIRTY"),
        )

    def test_dirty_or_unknown_material_is_retained(self):
        self.assertEqual("RETAINED_PROTECTED", closure_decision(
            evidence_exported=True, exclusively_owned=True,
            target_contained=True, removal_authorized=True,
            dirty_or_unknown=True))

    def test_codex_managed_custody_requires_application_archive(self):
        self.assertEqual("APPLICATION_ARCHIVE_REQUIRED", closure_decision(
            evidence_exported=True, exclusively_owned=True,
            target_contained=True, removal_authorized=True,
            custody="codex-managed"))

    def test_all_removal_gates_allow_closed(self):
        self.assertEqual("CLOSED", closure_decision(
            evidence_exported=True, exclusively_owned=True,
            target_contained=True, removal_authorized=True))

    def test_live_process_or_dependent_lease_blocks_close(self):
        self.assertEqual("BLOCKED_DEPENDENCY", closure_decision(
            evidence_exported=True, exclusively_owned=True,
            target_contained=True, removal_authorized=True,
            live_process=True))

    def test_shared_cache_or_retained_input_is_protected(self):
        self.assertEqual("RETAINED_PROTECTED", closure_decision(
            evidence_exported=True, exclusively_owned=True,
            target_contained=True, removal_authorized=True,
            shared_immutable_cache=True))

    def test_missing_removal_authority_blocks_close(self):
        self.assertEqual("BLOCKED_AUTHORITY", closure_decision(
            evidence_exported=True, exclusively_owned=True,
            target_contained=True, removal_authorized=False))

    def test_transfer_preserves_candidate_and_single_writer(self):
        self.assertEqual({
            "disposition": "TRANSFERRED_TO_NEXT_TASK",
            "head": "a" * 40,
            "tree": "b" * 40,
            "next_owner": "qa-main",
        }, transfer_decision("a" * 40, "b" * 40, "qa-main", active_writers=1))

    def test_transfer_rejects_multiple_active_writers(self):
        self.assertEqual("BLOCKED_DEPENDENCY",
                         transfer_decision("a" * 40, "b" * 40, "qa-main",
                                           active_writers=2))

    def test_administrative_completion_rejects_active_lease(self):
        self.assertEqual("ADMIN_COMPLETION_BLOCKED",
                         completion_decision(["CLOSED", "ACTIVE"]))

    def test_every_terminal_custody_state_allows_administrative_completion(self):
        for state in ("CLOSED", "RETAINED_PROTECTED",
                      "TRANSFERRED_TO_NEXT_TASK"):
            with self.subTest(state=state):
                self.assertEqual("ADMIN_COMPLETION_ALLOWED",
                                 completion_decision([state]))

    def test_every_nonterminal_or_blocking_state_rejects_administrative_completion(self):
        for state in ("REQUESTED", "ACTIVE", "CLOSE_PENDING",
                      "BLOCKED_DIRTY", "BLOCKED_DEPENDENCY",
                      "BLOCKED_AUTHORITY", "UNKNOWN"):
            with self.subTest(state=state):
                self.assertEqual("ADMIN_COMPLETION_BLOCKED",
                                 completion_decision([state]))

    def test_only_terminal_custody_mix_allows_administrative_completion(self):
        self.assertEqual("ADMIN_COMPLETION_ALLOWED",
                         completion_decision(["CLOSED", "RETAINED_PROTECTED",
                                              "TRANSFERRED_TO_NEXT_TASK"]))

    def test_git_or_hash_bound_manifest_is_durable_evidence(self):
        self.assertEqual("EVIDENCE_DURABLE", evidence_decision("git"))
        self.assertEqual("EVIDENCE_DURABLE", evidence_decision(
            "manifest", content_hash="c" * 64, recovery_location="vault:item",
            owner="qa-main", retention_class="release", access_boundary="team"))

    def test_chat_only_evidence_is_rejected(self):
        self.assertEqual("EVIDENCE_BLOCKED", evidence_decision("chat"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
