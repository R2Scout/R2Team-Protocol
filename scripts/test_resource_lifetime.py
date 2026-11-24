"""Offline naming and lifetime gates; these fixtures never create or delete resources."""
import copy
import unittest

import workspace_policy as policy


EVENTS = {
    "persistent": "DECOMMISSION_ACCEPTED",
    "task_scoped": "TASK_RESULT_ACCEPTED",
    "ephemeral": "USE_COMPLETED",
}
TOKENS = {"persistent": "perm", "task_scoped": "task", "ephemeral": "tmp"}


def resource(lifetime="task_scoped", **overrides):
    value = {
        "resource_id": "lease-42",
        "project_slug": "crm.ai",
        "work_ref": "task3244",
        "executor_slug": "dev10",
        "owner_executor_id": "dev10",
        "resource_label": f"crm.ai-task3244-{TOKENS[lifetime]}-dev10",
        "lifetime": lifetime,
        "purpose": "dev",
        "close_condition": {"event": EVENTS[lifetime], "ref": "TASK-3244"},
        "review_date": "2026-12-01",
        "retention_class": "task-result",
        "recovery_ref": "git:refs/heads/task-3244",
    }
    value.update(overrides)
    return value


def proof(value, **overrides):
    result = dict(value["close_condition"], resource_id=value["resource_id"],
                  owner_executor_id=value["owner_executor_id"],
                  satisfied=True, receipt_ref="checkpoint:accepted-result")
    result.update(overrides)
    return result


def close_facts(**overrides):
    value = dict(evidence_exported=True, exclusively_owned=True,
                 target_contained=True, removal_authorized=True)
    value.update(overrides)
    return value


class ResourceLifetimeTests(unittest.TestCase):
    def function(self, name):
        function = getattr(policy, name, None)
        self.assertTrue(callable(function), f"Missing lifetime behavior: {name}")
        return function

    def test_labels_distinguish_lifetime_using_the_accepted_examples(self):
        label = self.function("resource_label")
        for lifetime, token in TOKENS.items():
            with self.subTest(lifetime=lifetime):
                self.assertEqual(f"crm.ai-task3244-{token}-devops", label(
                    "crm.ai", "task3244", "devops", lifetime))
        self.assertEqual("crm.ai-base-perm-devops", label(
            "crm.ai", "base", "devops", "persistent"))

    def test_labels_reject_paths_titles_unknown_lifetimes_and_ambiguous_numbers(self):
        label = self.function("resource_label")
        for args in (("../crm", "task3244", "dev10", "ephemeral"),
                     ("crm.ai", "3244", "dev10", "ephemeral"),
                     ("crm.ai", "task3244", "DevOps Azure Chat", "ephemeral"),
                     ("crm.ai", "task3244", "dev10", "qa"),
                     ("crm.ai", "task3244", "dev10", [])):
            with self.subTest(args=args), self.assertRaises(ValueError):
                label(*args)

    def test_labels_do_not_silently_truncate_long_identifiers(self):
        label = self.function("resource_label")
        with self.assertRaises(ValueError):
            label("c" * 40, "task" + "1" * 40, "d" * 40, "ephemeral")

    def test_complete_records_allow_all_purpose_lifetime_combinations(self):
        errors = self.function("resource_policy_errors")
        for lifetime in EVENTS:
            for purpose in ("dev", "qa", "build", "release", "recovery"):
                with self.subTest(lifetime=lifetime, purpose=purpose):
                    self.assertEqual([], errors(resource(lifetime, purpose=purpose)))

    def test_required_policy_fields_cannot_be_empty_or_inferred_from_a_name(self):
        errors = self.function("resource_policy_errors")
        for field in resource():
            value = resource()
            del value[field]
            with self.subTest(field=field):
                self.assertTrue(errors(value))
        self.assertTrue(errors({"resource_label": "crm.ai-base-perm-devops"}))
        malformed = resource()
        malformed["lifetime"] = []
        for value in (None, [], "perm", malformed):
            with self.subTest(value=value):
                self.assertTrue(errors(value))

    def test_label_and_close_event_must_match_the_explicit_lifetime(self):
        errors = self.function("resource_policy_errors")
        self.assertTrue(errors(resource(resource_label="crm.ai-task3244-tmp-dev10")))
        for lifetime in EVENTS:
            with self.subTest(lifetime=lifetime):
                self.assertTrue(errors(resource(lifetime, close_condition={
                    "event": "ANY_TASK_DONE", "ref": "TASK-3244"})))

    def test_review_date_and_condition_reference_are_required(self):
        errors = self.function("resource_policy_errors")
        self.assertTrue(errors(resource(review_date="2026-02-30")))
        self.assertTrue(errors(resource(close_condition={
            "event": "TASK_RESULT_ACCEPTED", "ref": ""})))

    def test_allocation_requires_classification_and_preserves_existing_budget_gates(self):
        allocate = self.function("resource_allocation_decision")
        facts = dict(active_task=1, project_active=20, free_gib=100)
        self.assertEqual("ALLOCATION_BLOCKED", allocate({}, **facts))
        self.assertEqual("ALLOW_NORMAL", allocate(resource(), **facts))
        self.assertEqual("ALLOCATION_BLOCKED", allocate(
            resource(), active_task=1, project_active=150, free_gib=100))
        self.assertEqual("REUSE_EXISTING", allocate(
            resource(), compatible_lease=True, **facts))

    def test_unclassified_legacy_resources_remain_protected(self):
        close = self.function("resource_closure_decision")
        self.assertEqual("RESOURCE_POLICY_BLOCKED", close(
            {}, condition_evidence=None, **close_facts()))

    def test_task_scoped_and_ephemeral_resources_need_their_bound_completion_receipt(self):
        close = self.function("resource_closure_decision")
        for lifetime in ("task_scoped", "ephemeral"):
            value = resource(lifetime)
            with self.subTest(lifetime=lifetime):
                self.assertEqual("RETAINED_PROTECTED", close(
                    value, condition_evidence=None, **close_facts()))
                self.assertEqual("CLOSED", close(
                    value, condition_evidence=proof(value), **close_facts()))

    def test_wrong_resource_owner_event_reference_or_boolean_cannot_prove_completion(self):
        close = self.function("resource_closure_decision")
        value = resource("ephemeral")
        for field, wrong in (("resource_id", "lease-other"),
                             ("owner_executor_id", "qa-other"),
                             ("event", "TASK_RESULT_ACCEPTED"),
                             ("ref", "TASK-OTHER"), ("satisfied", "true"),
                             ("satisfied", 1), ("receipt_ref", "")):
            with self.subTest(field=field):
                self.assertEqual("RETAINED_PROTECTED", close(
                    value, condition_evidence=proof(value, **{field: wrong}),
                    **close_facts()))

    def test_persistent_requires_decommission_authority_even_with_a_completion_receipt(self):
        close = self.function("resource_closure_decision")
        value = resource("persistent")
        for authority in (False, "true", 1):
            with self.subTest(authority=authority):
                self.assertEqual("RETAINED_PROTECTED", close(
                    value, condition_evidence=proof(value),
                    decommission_authorized=authority, **close_facts()))
        self.assertEqual("CLOSED", close(value, condition_evidence=proof(value),
                         decommission_authorized=True, **close_facts()))

    def test_lifetime_completion_never_bypasses_evidence_authority_or_dependencies(self):
        close = self.function("resource_closure_decision")
        value = resource("ephemeral")
        for facts, expected in (({"dirty_or_unknown": True}, "RETAINED_PROTECTED"),
                                ({"evidence_exported": False}, "RETAINED_PROTECTED"),
                                ({"live_process": True}, "BLOCKED_DEPENDENCY"),
                                ({"dependent_lease": True}, "BLOCKED_DEPENDENCY"),
                                ({"removal_authorized": False}, "BLOCKED_AUTHORITY"),
                                ({"retained_recovery_input": True}, "RETAINED_PROTECTED"),
                                ({"custody": "codex-managed"}, "APPLICATION_ARCHIVE_REQUIRED")):
            with self.subTest(facts=facts):
                self.assertEqual(expected, close(value, condition_evidence=proof(value),
                                                 **close_facts(**facts)))

    def test_review_due_never_converts_a_resource_or_deletes_it(self):
        review = self.function("resource_review_decision")
        value = resource("persistent", review_date="2026-11-22")
        before = copy.deepcopy(value)
        self.assertEqual("REVIEW_DUE", review(value, today="2026-11-22"))
        self.assertEqual(before, value)
        self.assertEqual("REVIEW_SCHEDULED", review(resource(), today="2026-11-22"))
        self.assertEqual("RESOURCE_POLICY_BLOCKED", review({}, today="2026-11-22"))
        self.assertEqual("RESOURCE_POLICY_BLOCKED", review(value, today="bad-date"))

    def test_closure_rejects_untyped_authority_and_unknown_custody(self):
        close = self.function("resource_closure_decision")
        value = resource("ephemeral")
        for facts in ({"removal_authorized": "false"},
                      {"evidence_exported": 1}, {"live_process": "false"},
                      {"custody": "unknown"}):
            with self.subTest(facts=facts):
                self.assertEqual("RESOURCE_POLICY_BLOCKED", close(
                    value, condition_evidence=proof(value), **close_facts(**facts)))

    def test_administrative_completion_requires_policy_and_terminal_custody_together(self):
        complete = self.function("resource_completion_decision")
        anchor = resource("persistent", state="RETAINED_PROTECTED",
                          closure_owner_executor_id="dev10",
                          close_receipt_ref="receipt:standing-anchor-retained")
        self.assertEqual("ADMIN_COMPLETION_ALLOWED", complete([anchor]))
        missing = copy.deepcopy(anchor)
        del missing["lifetime"]
        self.assertEqual("ADMIN_COMPLETION_BLOCKED", complete([missing]))
        self.assertEqual("ADMIN_COMPLETION_BLOCKED", complete([
            resource(state="ACTIVE")]))
        self.assertEqual("ADMIN_COMPLETION_BLOCKED", complete(None))

    def test_git_worktree_directory_includes_native_id_and_readable_label(self):
        name = self.function("git_worktree_directory_name")
        self.assertEqual("ws0044-crm.ai-task3244-tmp-qa2", name(
            "ws0044", "crm.ai", "task3244", "qa2", "ephemeral"))
        self.assertEqual("ws0042-crm.ai-base-perm-devops", name(
            "ws0042", "crm.ai", "base", "devops", "persistent"))

    def test_git_worktree_directory_preserves_an_existing_numeric_id(self):
        name = self.function("git_worktree_directory_name")
        self.assertEqual("0043-crm.ai-task3244-task-dev10", name(
            "0043", "crm.ai", "task3244", "dev10", "task_scoped"))
        self.assertEqual("slot_0043-crm.ai-task3244-task-dev10", name(
            "slot_0043", "crm.ai", "task3244", "dev10", "task_scoped"))

    def test_git_worktree_directory_cannot_escape_its_parent_or_guess_a_missing_id(self):
        name = self.function("git_worktree_directory_name")
        for native_id in (None, "", "../ws0044", "ws/0044", "ws\\0044",
                          "C:ws0044", "ws0044 ", "ws0044.", "x" * 65):
            with self.subTest(native_id=native_id), self.assertRaises(ValueError):
                name(native_id, "crm.ai", "task3244", "qa2", "ephemeral")

    def test_git_worktree_directory_does_not_fabricate_application_or_legacy_paths(self):
        name = self.function("git_worktree_directory_name")
        for custody in ("codex-managed", "legacy-retained", "UNKNOWN", None):
            with self.subTest(custody=custody), self.assertRaises(ValueError):
                name("ws0044", "crm.ai", "task3244", "qa2", "ephemeral",
                     custody=custody)
        self.assertEqual("ws0044-crm.ai-task3244-tmp-qa2", name(
            "ws0044", "crm.ai", "task3244", "qa2", "ephemeral",
            custody="external-authorized"))

    def test_git_worktree_directory_keeps_resource_label_validation(self):
        name = self.function("git_worktree_directory_name")
        for args in (("../crm", "task3244", "qa2", "ephemeral"),
                     ("crm.ai", "3244", "qa2", "ephemeral"),
                     ("crm.ai", "task3244", "QA Chat", "ephemeral"),
                     ("crm.ai", "task3244", "qa2", "qa")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                name("ws0044", *args)


if __name__ == "__main__":
    unittest.main(verbosity=2)
