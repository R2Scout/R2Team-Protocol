import unittest
import relocation_policy


class RelocationPolicyTests(unittest.TestCase):
    def require(self, name):
        value = getattr(relocation_policy, name, None)
        if value is None:
            self.fail(f"relocation_policy.{name} is missing")
        return value

    @staticmethod
    def accepted_fence():
        from relocation_policy import FenceRecord

        return FenceRecord(
            project_id="project-a",
            executor_id="dev-a",
            epoch=4,
            record_ref="fence-4",
            source_state="STOPPED",
            target_state="READY",
            custody="TARGET_PENDING",
        )

    @staticmethod
    def active_target_fence():
        from relocation_policy import FenceRecord

        return FenceRecord(
            project_id="project-a",
            executor_id="dev-a",
            epoch=5,
            record_ref="fence-5",
            source_state="STOPPED",
            target_state="ACTIVE",
            custody="TARGET_ACTIVE",
        )

    @staticmethod
    def stop_receipt():
        return {
            "receipt_id": "stop-1",
            "receipt_type": "SOURCE_STOP",
            "migration_id": "migration-1",
            "repository_or_project_id": "project-a",
            "executor_id": "dev-a",
            "prior_epoch": 3,
            "new_epoch": 4,
            "causal_parent_ref": "fence-4",
            "accepted_commit_sha": "commit-4",
            "task_checkpoint_refs": ["commit-4"],
            "candidate_refs": ["tree-4"],
            "workspace_disposition_refs": ["workspace-1"],
            "actor_executor_id": "dev-a",
            "actor_provider_class": "local-standalone",
            "observed_outcome": "SOURCE_STOPPED",
            "registry_evidence": "NOT_APPLICABLE",
            "review_date": "2026-01-02",
            "expected_epoch": 4,
            "final_checkpoint": "commit-4",
            "candidate_tree": "tree-4",
            "publishers_in_flight": [],
            "helpers_in_flight": [],
            "workspace_custody": "RETAINED_PROTECTED",
            "native_resource_custody": "NONE",
            "actor_class": "registered-source-executor",
            "stop_mechanism": "COOPERATIVE_ACK",
            "cutover_parent": "fence-4",
            "timestamp": "2026-01-01T00:00:00Z",
        }

    @staticmethod
    def activation_receipt():
        return {
            "receipt_id": "activation-1",
            "receipt_type": "ACTIVATION",
            "migration_id": "migration-1",
            "repository_or_project_id": "project-a",
            "executor_id": "dev-a",
            "prior_epoch": 4,
            "new_epoch": 5,
            "causal_parent_ref": "stop-1",
            "accepted_commit_sha": "commit-5",
            "task_checkpoint_refs": ["commit-4"],
            "candidate_refs": ["tree-4"],
            "workspace_disposition_refs": ["workspace-1"],
            "actor_executor_id": "dev-a-target",
            "actor_provider_class": "local-standalone",
            "registry_evidence": "MAPPING_PRESENT_READ_BACK",
            "review_date": "2026-01-02",
            "causal_stop_receipt": "stop-1",
            "target_preflight_receipt": "preflight-1",
            "cutover_parent": "fence-4",
            "accepted_cutover": "commit-5",
            "target_preflight": "PASS",
            "task_checkpoint": "commit-4",
            "candidate_tree": "tree-4",
            "workspace_custody": "RETAINED_PROTECTED",
            "actor_class": "registered-target-executor",
            "mapping_result": "MAPPING_PRESENT_READ_BACK",
            "observed_outcome": "TARGET_ACTIVE",
            "timestamp": "2026-01-01T00:01:00Z",
        }

    @staticmethod
    def prepare_receipt():
        return {
            "receipt_id": "prepare-1",
            "receipt_type": "PREPARE",
            "migration_id": "migration-1",
            "repository_or_project_id": "project-a",
            "executor_id": None,
            "prior_epoch": 2,
            "new_epoch": 3,
            "causal_parent_ref": "fence-4",
            "accepted_commit_sha": "commit-3",
            "task_checkpoint_refs": ["commit-4"],
            "candidate_refs": ["tree-4"],
            "workspace_disposition_refs": ["workspace-1"],
            "actor_executor_id": "pm-a",
            "actor_provider_class": "local-standalone",
            "observed_outcome": "PREPARED",
            "registry_evidence": "NOT_APPLICABLE",
            "review_date": "2026-01-02",
            "affected_executor_ids": ["dev-a"],
            "timestamp": "2026-01-01T00:00:00Z",
        }

    @staticmethod
    def preflight_receipt():
        return {
            "receipt_id": "preflight-1",
            "receipt_type": "TARGET_PREFLIGHT",
            "migration_id": "migration-1",
            "repository_or_project_id": "project-a",
            "executor_id": "dev-a",
            "prior_epoch": 4,
            "new_epoch": 5,
            "causal_parent_ref": "stop-1",
            "accepted_commit_sha": "commit-5",
            "task_checkpoint_refs": ["commit-4"],
            "candidate_refs": ["tree-4"],
            "workspace_disposition_refs": ["workspace-1"],
            "actor_executor_id": "dev-a-target",
            "actor_provider_class": "local-standalone",
            "observed_outcome": "TARGET_PREFLIGHT_PASS",
            "registry_evidence": "MAPPING_PRESENT_READ_BACK",
            "review_date": "2026-01-02",
            "target_preflight": "PASS",
            "target_placement_class": "local-standalone",
            "timestamp": "2026-01-01T00:00:30Z",
        }

    @staticmethod
    def completion_receipt():
        return {
            "receipt_id": "completion-1",
            "receipt_type": "COMPLETION",
            "migration_id": "migration-1",
            "repository_or_project_id": "project-a",
            "executor_id": None,
            "prior_epoch": 5,
            "new_epoch": 6,
            "causal_parent_ref": "activation-1",
            "accepted_commit_sha": "commit-6",
            "task_checkpoint_refs": ["commit-4"],
            "candidate_refs": ["tree-4"],
            "workspace_disposition_refs": ["workspace-1"],
            "actor_executor_id": "pm-a",
            "actor_provider_class": "local-standalone",
            "observed_outcome": "COMPLETE",
            "registry_evidence": "NOT_APPLICABLE",
            "review_date": "2026-01-02",
            "accounted_executor_ids": ["dev-a"],
            "timestamp": "2026-01-01T00:02:00Z",
        }

    def test_causal_successor_accepts_expected_prior(self):
        try:
            from relocation_policy import FenceRecord, propose_successor
        except ModuleNotFoundError:
            self.fail("relocation_policy model is missing")

        accepted = self.accepted_fence()

        decision = propose_successor(
            accepted,
            expected_prior_epoch=4,
            expected_prior_ref="fence-4",
            new_epoch=5,
            new_record_ref="fence-5",
        )

        self.assertEqual("ALLOW", decision.code)

    def test_successor_rejects_mismatched_causal_parent(self):
        from relocation_policy import propose_successor

        decision = propose_successor(
            self.accepted_fence(),
            expected_prior_epoch=4,
            expected_prior_ref="different-fence-4",
            new_epoch=5,
            new_record_ref="fence-5",
        )

        self.assertEqual("WRITER_CONFLICT", decision.code)

    def test_successor_rejects_stale_or_nonincrementing_epoch(self):
        from relocation_policy import propose_successor

        for expected_prior, new_epoch in ((3, 5), (4, 4), (4, 6)):
            with self.subTest(expected_prior=expected_prior, new_epoch=new_epoch):
                decision = propose_successor(
                    self.accepted_fence(),
                    expected_prior_epoch=expected_prior,
                    expected_prior_ref="fence-4",
                    new_epoch=new_epoch,
                    new_record_ref="fence-next",
                )
                self.assertEqual("WRITER_CONFLICT", decision.code)

    def test_authority_epoch_boundaries_reject_boolean_and_coerced_values(self):
        from relocation_policy import FenceRecord

        propose_successor = self.require("propose_successor")
        materialize_successor = self.require("materialize_successor")
        publication_allowed = self.require("publication_allowed")
        cancellation_allowed = self.require("cancellation_allowed")
        accepted = FenceRecord("project-a", "dev-a", 1, "fence-1", "STOPPED", "READY", "TARGET_PENDING")
        invalid_values = (True, False, "1", 1.0, None, -1)
        for value in invalid_values:
            with self.subTest(api="propose", value=value):
                self.assertNotEqual(
                    "ALLOW",
                    propose_successor(
                        accepted,
                        expected_prior_epoch=value,
                        expected_prior_ref="fence-1",
                        new_epoch=2,
                        new_record_ref="fence-2",
                    ).code,
                )
            with self.subTest(api="materialize", value=value):
                self.assertNotEqual(
                    "ALLOW",
                    materialize_successor(
                        accepted,
                        expected_prior_epoch=value,
                        expected_prior_ref="fence-1",
                        new_epoch=2,
                        new_record_ref="fence-2",
                    )[0].code,
                )
            with self.subTest(api="publication", value=value):
                self.assertNotEqual(
                    "ALLOW",
                    publication_allowed(
                        accepted,
                        claim_project_id="project-a",
                        claim_executor_id="dev-a",
                        claim_epoch=value,
                        claim_record_ref="fence-1",
                        publication_class="PRODUCT",
                        frozen=False,
                        actor_executor_id="dev-a",
                        migration_pm_executor_id="pm-a",
                        path="src/product.py",
                        migration_id="migration-1",
                    ).code,
                )
            with self.subTest(api="cancellation", value=value):
                self.assertEqual(
                    "EPOCH_INVALID",
                    cancellation_allowed(
                        source_state="ACTIVE",
                        target_state="INACTIVE",
                        current_epoch=value,
                        proposed_epoch=2,
                    ).code,
                )

    def test_accepted_fence_epoch_must_be_strict_integer(self):
        from relocation_policy import FenceRecord

        propose_successor = self.require("propose_successor")
        publication_allowed = self.require("publication_allowed")
        accepted = FenceRecord("project-a", "dev-a", True, "fence-1", "STOPPED", "READY", "TARGET_PENDING")
        self.assertNotEqual(
            "ALLOW",
            propose_successor(accepted, expected_prior_epoch=1, expected_prior_ref="fence-1", new_epoch=2, new_record_ref="fence-2").code,
        )
        self.assertNotEqual(
            "ALLOW",
            publication_allowed(
                accepted,
                claim_project_id="project-a",
                claim_executor_id="dev-a",
                claim_epoch=1,
                claim_record_ref="fence-1",
                publication_class="PRODUCT",
                frozen=False,
                actor_executor_id="dev-a",
                migration_pm_executor_id="pm-a",
                path="src/product.py",
                migration_id="migration-1",
            ).code,
        )

    def test_source_stop_receipt_rejects_inflight_helper(self):
        validate_stop_receipt = self.require("validate_stop_receipt")
        receipt = self.stop_receipt()
        receipt["helpers_in_flight"] = ["helper-a"]

        decision = validate_stop_receipt(receipt)

        self.assertEqual("BLOCKED_IN_FLIGHT", decision.code)

    def test_source_stop_receipt_accepts_complete_supported_proof(self):
        validate_stop_receipt = self.require("validate_stop_receipt")

        decision = validate_stop_receipt(self.stop_receipt())

        self.assertEqual("ALLOW", decision.code)

    def test_source_stop_receipt_rejects_missing_fact_or_unknown_mechanism(self):
        validate_stop_receipt = self.require("validate_stop_receipt")
        cases = []
        for field in (
            "receipt_id",
            "receipt_type",
            "migration_id",
            "repository_or_project_id",
            "executor_id",
            "expected_epoch",
            "final_checkpoint",
            "candidate_tree",
            "publishers_in_flight",
            "helpers_in_flight",
            "workspace_custody",
            "native_resource_custody",
            "actor_class",
            "stop_mechanism",
            "cutover_parent",
            "timestamp",
        ):
            missing = self.stop_receipt()
            del missing[field]
            cases.append(missing)
        unknown_mechanism = self.stop_receipt()
        unknown_mechanism["stop_mechanism"] = "NO_PROCESS_OBSERVED"
        cases.append(unknown_mechanism)

        for receipt in cases:
            with self.subTest(receipt=receipt):
                self.assertEqual("STOP_PROOF_INVALID", validate_stop_receipt(receipt).code)

    def test_unreachable_source_without_enforceable_revocation_blocks_activation(self):
        activation_allowed = self.require("activation_allowed")

        decision = activation_allowed(
            self.accepted_fence(),
            stop_receipt=None,
            activation_receipt=None,
            source_reachable=False,
            enforceable_revocation=False,
        )

        self.assertEqual("BLOCKED_SOURCE_UNREACHABLE", decision.code)

    def test_activation_requires_matching_stop_and_cutover_parent(self):
        activation_allowed = self.require("activation_allowed")
        activation = self.activation_receipt()
        activation["causal_stop_receipt"] = "different-stop"

        decision = activation_allowed(
            self.accepted_fence(),
            stop_receipt=self.stop_receipt(),
            preflight_receipt=self.preflight_receipt(),
            activation_receipt=activation,
            source_reachable=True,
            enforceable_revocation=False,
        )

        self.assertEqual("ACTIVATION_CAUSAL_MISMATCH", decision.code)

    def test_activation_accepts_complete_causal_receipts(self):
        activation_allowed = self.require("activation_allowed")

        decision = activation_allowed(
            self.accepted_fence(),
            stop_receipt=self.stop_receipt(),
            preflight_receipt=self.preflight_receipt(),
            activation_receipt=self.activation_receipt(),
            source_reachable=True,
            enforceable_revocation=False,
        )

        self.assertEqual("ALLOW", decision.code)

    def test_activation_rejects_structurally_invalid_stop_receipt(self):
        activation_allowed = self.require("activation_allowed")
        invalid = {
            "receipt_id": "stop-1",
            "expected_epoch": 4,
            "cutover_parent": "fence-4",
        }

        decision = activation_allowed(
            self.accepted_fence(),
            stop_receipt=invalid,
            preflight_receipt=self.preflight_receipt(),
            activation_receipt=self.activation_receipt(),
            source_reachable=True,
            enforceable_revocation=False,
        )

        self.assertEqual("STOP_PROOF_INVALID", decision.code)

    def test_activation_rejects_every_missing_common_or_stop_fact(self):
        activation_allowed = self.require("activation_allowed")
        fields = set(self.stop_receipt())
        for field in sorted(fields):
            with self.subTest(field=field):
                stop = self.stop_receipt()
                del stop[field]
                decision = activation_allowed(
                    self.accepted_fence(),
                    stop_receipt=stop,
                    preflight_receipt=self.preflight_receipt(),
                    activation_receipt=self.activation_receipt(),
                    source_reachable=True,
                    enforceable_revocation=False,
                )
                self.assertNotEqual("ALLOW", decision.code)

    def test_activation_rejects_mismatched_stop_identity_and_custody(self):
        activation_allowed = self.require("activation_allowed")
        mutations = {
            "migration_id": "migration-other",
            "repository_or_project_id": "project-other",
            "executor_id": "qa-a",
            "final_checkpoint": "commit-other",
            "candidate_tree": "tree-other",
            "workspace_custody": "UNKNOWN",
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                stop = self.stop_receipt()
                stop[field] = value
                decision = activation_allowed(
                    self.accepted_fence(),
                    stop_receipt=stop,
                    preflight_receipt=self.preflight_receipt(),
                    activation_receipt=self.activation_receipt(),
                    source_reachable=True,
                    enforceable_revocation=False,
                )
                expected = (
                    "STOP_PROOF_INVALID"
                    if field in {"final_checkpoint", "candidate_tree"}
                    else "ACTIVATION_IDENTITY_MISMATCH"
                )
                self.assertEqual(expected, decision.code)

    def test_activation_rejects_mismatched_cutover_parent(self):
        activation_allowed = self.require("activation_allowed")
        activation = self.activation_receipt()
        activation["cutover_parent"] = "different-fence"

        decision = activation_allowed(
            self.accepted_fence(),
            stop_receipt=self.stop_receipt(),
            preflight_receipt=self.preflight_receipt(),
            activation_receipt=activation,
            source_reachable=True,
            enforceable_revocation=False,
        )

        self.assertEqual("ACTIVATION_CAUSAL_MISMATCH", decision.code)

    def test_activation_rejects_stop_common_parent_unrelated_to_cutover(self):
        activation_allowed = self.require("activation_allowed")
        stop = self.stop_receipt()
        stop["causal_parent_ref"] = "unrelated-record"

        decision = activation_allowed(
            self.accepted_fence(),
            stop_receipt=stop,
            preflight_receipt=self.preflight_receipt(),
            activation_receipt=self.activation_receipt(),
            source_reachable=True,
            enforceable_revocation=False,
        )

        self.assertEqual("STOP_PROOF_INVALID", decision.code)

    def test_stop_expected_epoch_rejects_boolean_and_coerced_values(self):
        activation_allowed = self.require("activation_allowed")
        validate_stop_receipt = self.require("validate_stop_receipt")
        for value in (True, False, "4", 4.0, None, -1):
            with self.subTest(value=value):
                stop = self.stop_receipt()
                stop["expected_epoch"] = value
                self.assertNotEqual("ALLOW", validate_stop_receipt(stop).code)
                self.assertNotEqual(
                    "ALLOW",
                    activation_allowed(
                        self.accepted_fence(),
                        stop_receipt=stop,
                        preflight_receipt=self.preflight_receipt(),
                        activation_receipt=self.activation_receipt(),
                        source_reachable=True,
                        enforceable_revocation=False,
                    ).code,
                )

    def test_partial_team_state_preserves_mixed_executor_custody(self):
        derive_team_state = self.require("derive_team_state")
        records = [
            {
                "executor_id": "dev-a",
                "source_state": "STOPPED",
                "target_state": "ACTIVE",
                "custody": "TARGET_ACTIVE",
                "disposition": "RESUMED",
            },
            {
                "executor_id": "qa-a",
                "source_state": "STOPPED",
                "target_state": "INACTIVE",
                "custody": "SOURCE_STOPPED",
                "disposition": "BLOCKED",
            },
        ]

        aggregate = derive_team_state(
            records,
            affected_executor_ids=("dev-a", "qa-a"),
            migration_mode="team",
        )

        self.assertEqual("INVALID", aggregate.state)

    def test_blocked_and_frozen_states_have_explicit_recovery_routes(self):
        permitted_successors = self.require("permitted_successors")

        cases = {
            "FROZEN": {"READY_TO_RESUME", "CANCELLATION", "FORWARD_ROLLBACK"},
            "PARTIAL_BLOCKED": {"RESUMING", "COMPLETE", "FORWARD_ROLLBACK"},
            "BLOCKED": {"PREPARING", "CANCELLATION", "FORWARD_ROLLBACK"},
        }
        for state, expected in cases.items():
            with self.subTest(state=state):
                actual = set(
                    permitted_successors(
                        state,
                        blocked_from_state="PREPARING" if state == "BLOCKED" else None,
                    )
                )
                self.assertEqual(expected, actual)

    def test_post_stop_cancellation_cannot_silently_revive_source(self):
        cancellation_allowed = self.require("cancellation_allowed")

        decision = cancellation_allowed(
            source_state="STOPPED",
            target_state="READY",
            current_epoch=4,
            proposed_epoch=4,
        )

        self.assertEqual("REACTIVATION_REQUIRED", decision.code)

    def test_forward_rollback_requires_higher_epoch_after_activation(self):
        cancellation_allowed = self.require("cancellation_allowed")

        stale = cancellation_allowed(
            source_state="STOPPED",
            target_state="ACTIVE",
            current_epoch=5,
            proposed_epoch=5,
        )
        forward = cancellation_allowed(
            source_state="STOPPED",
            target_state="ACTIVE",
            current_epoch=5,
            proposed_epoch=6,
        )

        self.assertEqual("FORWARD_ROLLBACK_REQUIRED", stale.code)
        self.assertEqual("FORWARD_ROLLBACK_REQUIRED", forward.code)

    def test_post_stop_epoch_increment_does_not_reactivate_source(self):
        cancellation_allowed = self.require("cancellation_allowed")

        decision = cancellation_allowed(
            source_state="STOPPED",
            target_state="READY",
            current_epoch=4,
            proposed_epoch=5,
        )

        self.assertEqual("REACTIVATION_REQUIRED", decision.code)

    def test_offline_stale_source_cannot_publish_after_target_activation(self):
        publication_allowed = self.require("publication_allowed")

        decision = publication_allowed(
            self.active_target_fence(),
            claim_project_id="project-a",
            claim_executor_id="dev-a",
            claim_epoch=4,
            claim_record_ref="fence-4",
            publication_class="PRODUCT",
            frozen=False,
            actor_executor_id="dev-a",
            migration_pm_executor_id="pm-a",
            path="src/product.py",
            migration_id="migration-1",
        )

        self.assertEqual("WRITER_CONFLICT", decision.code)

    def test_frozen_pm_can_write_only_declared_migration_control_path(self):
        publication_allowed = self.require("publication_allowed")
        common = {
            "claim_project_id": "project-a",
            "claim_executor_id": "dev-a",
            "claim_epoch": 4,
            "claim_record_ref": "fence-4",
            "frozen": True,
            "actor_executor_id": "pm-a",
            "migration_pm_executor_id": "pm-a",
            "migration_id": "migration-1",
        }

        product = publication_allowed(
            self.accepted_fence(),
            publication_class="PRODUCT",
            path="src/product.py",
            **common,
        )
        control = publication_allowed(
            self.accepted_fence(),
            publication_class="MIGRATION_CONTROL",
            path="Team/Migrations/migration-1/MIGRATION.md",
            **common,
        )

        self.assertEqual("FROZEN_PRODUCT_WRITE_BLOCKED", product.code)
        self.assertEqual("ALLOW", control.code)

    def test_frozen_control_write_rejects_wrong_actor_or_path(self):
        publication_allowed = self.require("publication_allowed")
        base = {
            "claim_project_id": "project-a",
            "claim_executor_id": "dev-a",
            "claim_epoch": 4,
            "claim_record_ref": "fence-4",
            "publication_class": "MIGRATION_CONTROL",
            "frozen": True,
            "migration_pm_executor_id": "pm-a",
            "migration_id": "migration-1",
        }

        wrong_actor = publication_allowed(
            self.accepted_fence(),
            actor_executor_id="dev-a",
            path="Team/Migrations/migration-1/MIGRATION.md",
            **base,
        )
        wrong_path = publication_allowed(
            self.accepted_fence(),
            actor_executor_id="pm-a",
            path="Team/Migrations/other/MIGRATION.md",
            **base,
        )
        wrong_migration = publication_allowed(
            self.accepted_fence(),
            actor_executor_id="pm-a",
            path="Team/Migrations/migration-1/MIGRATION.md",
            **{**base, "migration_id": "migration-other"},
        )

        self.assertEqual("FROZEN_CONTROL_FORBIDDEN", wrong_actor.code)
        self.assertEqual("FROZEN_CONTROL_FORBIDDEN", wrong_path.code)
        self.assertEqual("FROZEN_CONTROL_FORBIDDEN", wrong_migration.code)

    def test_frozen_publication_default_denies_task_team_and_unknown_classes(self):
        publication_allowed = self.require("publication_allowed")
        base = {
            "claim_project_id": "project-a",
            "claim_executor_id": "dev-a",
            "claim_epoch": 4,
            "claim_record_ref": "fence-4",
            "frozen": True,
            "actor_executor_id": "dev-a",
            "migration_pm_executor_id": "pm-a",
            "migration_id": "migration-1",
        }
        for publication_class, path in (
            ("TASK", "Tasks/TASK-001.md"),
            ("TEAM", "Team/TEAM.md"),
            ("TSAK", "Tasks/TASK-001.md"),
        ):
            with self.subTest(publication_class=publication_class):
                decision = publication_allowed(
                    self.accepted_fence(),
                    publication_class=publication_class,
                    path=path,
                    **base,
                )
                self.assertNotEqual("ALLOW", decision.code)

    def test_frozen_pm_task_exception_is_exact_field_and_canonical_path_only(self):
        publication_allowed = self.require("publication_allowed")
        base = {
            "claim_project_id": "project-a",
            "claim_executor_id": "dev-a",
            "claim_epoch": 4,
            "claim_record_ref": "fence-4",
            "publication_class": "TASK",
            "frozen": True,
            "actor_executor_id": "pm-a",
            "migration_pm_executor_id": "pm-a",
            "migration_id": "migration-1",
            "governing_task_path": "Tasks/TASK-RELOCATION.md",
            "governing_task_fields": ("status", "evidence"),
        }
        allowed = publication_allowed(
            self.accepted_fence(),
            path="Tasks/TASK-RELOCATION.md",
            claimed_fields=("status",),
            **base,
        )
        wrong_field = publication_allowed(
            self.accepted_fence(),
            path="Tasks/TASK-RELOCATION.md",
            claimed_fields=("owner_executor_id",),
            **base,
        )
        traversal = publication_allowed(
            self.accepted_fence(),
            path="Tasks/../Tasks/TASK-RELOCATION.md",
            claimed_fields=("status",),
            **base,
        )

        self.assertEqual("ALLOW", allowed.code)
        self.assertNotEqual("ALLOW", wrong_field.code)
        self.assertNotEqual("ALLOW", traversal.code)

    def test_frozen_task_exception_rejects_malformed_field_collections(self):
        publication_allowed = self.require("publication_allowed")
        base = {
            "claim_project_id": "project-a",
            "claim_executor_id": "dev-a",
            "claim_epoch": 4,
            "claim_record_ref": "fence-4",
            "publication_class": "TASK",
            "frozen": True,
            "actor_executor_id": "pm-a",
            "migration_pm_executor_id": "pm-a",
            "path": "Tasks/TASK-RELOCATION.md",
            "migration_id": "migration-1",
            "governing_task_path": "Tasks/TASK-RELOCATION.md",
        }
        cases = (
            ("status", ("s",)),
            (("status", ""), ("status",)),
            (("status", 7), ("status",)),
            (("status",), "status"),
            (("status",), ("owner_executor_id",)),
        )
        for governing, claimed in cases:
            with self.subTest(governing=governing, claimed=claimed):
                decision = publication_allowed(
                    self.accepted_fence(),
                    governing_task_fields=governing,
                    claimed_fields=claimed,
                    **base,
                )
                self.assertNotEqual("ALLOW", decision.code)

    def test_registry_remap_rejects_collision_or_wrong_executor(self):
        registry_mapping_allowed = self.require("registry_mapping_allowed")

        collision = registry_mapping_allowed(
            expected_executor_id="dev-a",
            observed_executor_id="dev-a",
            executor_mode="local_standalone",
            mapping_present=True,
            local_authority=True,
            read_back=True,
            collision=True,
        )
        wrong_executor = registry_mapping_allowed(
            expected_executor_id="dev-a",
            observed_executor_id="qa-a",
            executor_mode="local_standalone",
            mapping_present=True,
            local_authority=True,
            read_back=True,
            collision=False,
        )

        self.assertEqual("REGISTRY_CONFLICT", collision.code)
        self.assertEqual("REGISTRY_CONFLICT", wrong_executor.code)

    def test_remote_manual_executor_does_not_require_local_mapping(self):
        registry_mapping_allowed = self.require("registry_mapping_allowed")

        decision = registry_mapping_allowed(
            expected_executor_id="vendor-a",
            observed_executor_id=None,
            executor_mode="remote_manual",
            mapping_present=False,
            local_authority=False,
            read_back=False,
            collision=False,
        )

        self.assertEqual("ALLOW_REMOTE_MANUAL", decision.code)

    def test_local_registry_mapping_requires_authority_and_readback(self):
        registry_mapping_allowed = self.require("registry_mapping_allowed")

        no_authority = registry_mapping_allowed(
            expected_executor_id="dev-a",
            observed_executor_id="dev-a",
            executor_mode="local_standalone",
            mapping_present=True,
            local_authority=False,
            read_back=True,
            collision=False,
        )
        no_readback = registry_mapping_allowed(
            expected_executor_id="dev-a",
            observed_executor_id="dev-a",
            executor_mode="local_standalone",
            mapping_present=True,
            local_authority=True,
            read_back=False,
            collision=False,
        )

        self.assertEqual("REGISTRY_AUTHORITY_REQUIRED", no_authority.code)
        self.assertEqual("REGISTRY_READBACK_REQUIRED", no_readback.code)

    def test_registry_mapping_rejects_untyped_flags_and_identity(self):
        registry_mapping_allowed = self.require("registry_mapping_allowed")
        decision = registry_mapping_allowed(
            expected_executor_id="dev-a",
            observed_executor_id="dev-a",
            executor_mode="local_standalone",
            mapping_present=1,
            local_authority=True,
            read_back=True,
            collision=False,
        )
        bad_identity = registry_mapping_allowed(
            expected_executor_id="   ",
            observed_executor_id="   ",
            executor_mode="local_standalone",
            mapping_present=True,
            local_authority=True,
            read_back=True,
            collision=False,
        )

        self.assertEqual("REGISTRY_INPUT_INVALID", decision.code)
        self.assertEqual("REGISTRY_INPUT_INVALID", bad_identity.code)

    def test_workspace_reuse_rejects_correct_candidate_with_wrong_custody_facts(self):
        workspace_reuse_allowed = self.require("workspace_reuse_allowed")
        expected = {
            "candidate": "commit-4",
            "custody": "TRANSFERRED_TO_NEXT_TASK",
            "host_class": "target-host",
            "native_resources": "NONE",
            "dependencies": "PINNED",
            "contained": True,
            "owner_executor_id": "dev-a",
            "mutability": "mutable",
        }
        observed = dict(expected)
        observed["custody"] = "ACTIVE_SOURCE"

        decision = workspace_reuse_allowed(expected, observed)

        self.assertEqual("WORKSPACE_REUSE_BLOCKED", decision.code)

    def test_workspace_reuse_accepts_all_exact_custody_facts(self):
        workspace_reuse_allowed = self.require("workspace_reuse_allowed")
        facts = {
            "candidate": "commit-4",
            "custody": "TRANSFERRED_TO_NEXT_TASK",
            "host_class": "target-host",
            "native_resources": "NONE",
            "dependencies": "PINNED",
            "contained": True,
            "owner_executor_id": "dev-a",
            "mutability": "mutable",
        }

        self.assertEqual("ALLOW", workspace_reuse_allowed(facts, dict(facts)).code)

    def test_workspace_reuse_rejects_wrong_or_missing_owner_and_mutability(self):
        workspace_reuse_allowed = self.require("workspace_reuse_allowed")
        expected = {
            "candidate": "commit-4",
            "custody": "TRANSFERRED_TO_NEXT_TASK",
            "host_class": "target-host",
            "native_resources": "NONE",
            "dependencies": "PINNED",
            "contained": True,
            "owner_executor_id": "dev-a",
            "mutability": "mutable",
        }
        cases = []
        wrong_owner = dict(expected)
        wrong_owner["owner_executor_id"] = "qa-a"
        cases.append(wrong_owner)
        wrong_mutability = dict(expected)
        wrong_mutability["mutability"] = "immutable"
        cases.append(wrong_mutability)
        missing_mutability = dict(expected)
        del missing_mutability["mutability"]
        cases.append(missing_mutability)

        for observed in cases:
            with self.subTest(observed=observed):
                self.assertEqual(
                    "WORKSPACE_REUSE_BLOCKED",
                    workspace_reuse_allowed(expected, observed).code,
                )

    def test_workspace_reuse_rejects_untyped_expected_facts(self):
        workspace_reuse_allowed = self.require("workspace_reuse_allowed")
        facts = {
            "candidate": "commit-4",
            "custody": "TRANSFERRED_TO_NEXT_TASK",
            "host_class": "target-host",
            "native_resources": "NONE",
            "dependencies": "PINNED",
            "contained": "true",
            "owner_executor_id": None,
            "mutability": "mutable",
        }

        self.assertEqual(
            "WORKSPACE_REUSE_BLOCKED",
            workspace_reuse_allowed(facts, dict(facts)).code,
        )

    def test_retained_executor_cannot_remain_in_frozen_affected_set(self):
        affected_set_allowed = self.require("affected_set_allowed")

        decision = affected_set_allowed(
            affected_executor_ids=("dev-a", "qa-a"),
            retained_executor_ids=("qa-a",),
            migration_state="FREEZE_PENDING",
        )

        self.assertEqual("RETAINED_SET_CONFLICT", decision.code)

    def test_affected_set_rejects_scalars_duplicates_and_untyped_ids(self):
        affected_set_allowed = self.require("affected_set_allowed")
        cases = (
            ("dev-a", ()),
            (("dev-a", "dev-a"), ()),
            (("dev-a", 7), ()),
        )
        for affected, retained in cases:
            with self.subTest(affected=affected):
                self.assertEqual(
                    "AFFECTED_SET_INVALID",
                    affected_set_allowed(
                        affected_executor_ids=affected,
                        retained_executor_ids=retained,
                        migration_state="FREEZE_PENDING",
                    ).code,
                )

    def test_team_state_is_derived_from_every_executor_record(self):
        derive_team_state = self.require("derive_team_state")
        cases = (
            (
                "COMPLETE",
                [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "ACTIVE", "custody": "TARGET_ACTIVE", "disposition": "RESUMED"},
                    {"executor_id": "qa-a", "source_state": "STOPPED", "target_state": "ACTIVE", "custody": "TARGET_ACTIVE", "disposition": "RESUMED"},
                ],
            ),
            (
                "READY_TO_RESUME",
                [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "READY", "custody": "TARGET_PENDING", "disposition": "PENDING"},
                    {"executor_id": "qa-a", "source_state": "STOPPED", "target_state": "READY", "custody": "TARGET_PENDING", "disposition": "PENDING"},
                ],
            ),
            (
                "FROZEN",
                [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "INACTIVE", "custody": "SOURCE_STOPPED", "disposition": "PENDING"},
                    {"executor_id": "qa-a", "source_state": "STOPPED", "target_state": "INACTIVE", "custody": "SOURCE_STOPPED", "disposition": "PENDING"},
                ],
            ),
        )

        for expected, records in cases:
            with self.subTest(expected=expected):
                actual = derive_team_state(
                    records,
                    affected_executor_ids=("dev-a", "qa-a"),
                    migration_mode="team",
                ).state
                self.assertEqual("INVALID" if expected == "COMPLETE" else expected, actual)

    def test_terminal_accounted_executor_can_complete_mixed_team(self):
        derive_team_state = self.require("derive_team_state")
        for disposition in ("BLOCKED", "CANCELLED", "FORWARD_ROLLBACK"):
            with self.subTest(disposition=disposition):
                records = [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "ACTIVE", "custody": "TARGET_ACTIVE", "disposition": "RESUMED"},
                    {
                        "executor_id": "qa-a",
                        "source_state": "STOPPED",
                        "target_state": "INACTIVE",
                        "custody": "SOURCE_STOPPED",
                        "disposition": disposition,
                        "disposition_owner_executor_id": "pm-a",
                        "review_date": "2026-01-02",
                        "next_action": "Retain terminal custody",
                        "disposition_receipt_ref": "receipt-terminal-1",
                    },
                ]
                self.assertEqual(
                    "INVALID",
                    derive_team_state(
                        records,
                        affected_executor_ids=("dev-a", "qa-a"),
                        migration_mode="team",
                    ).state,
                )

    def test_incomplete_terminal_disposition_remains_partial(self):
        derive_team_state = self.require("derive_team_state")
        base = {
            "executor_id": "qa-a",
            "source_state": "STOPPED",
            "target_state": "INACTIVE",
            "custody": "SOURCE_STOPPED",
            "disposition": "CANCELLED",
            "disposition_owner_executor_id": "pm-a",
            "review_date": "2026-01-02",
            "next_action": "Retain terminal custody",
            "disposition_receipt_ref": "receipt-terminal-1",
        }
        for field in ("disposition_owner_executor_id", "review_date", "next_action", "disposition_receipt_ref"):
            with self.subTest(field=field):
                incomplete = dict(base)
                del incomplete[field]
                records = [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "ACTIVE", "custody": "TARGET_ACTIVE", "disposition": "RESUMED"},
                    incomplete,
                ]
                self.assertEqual(
                    "INVALID",
                    derive_team_state(
                        records,
                        affected_executor_ids=("dev-a", "qa-a"),
                        migration_mode="team",
                    ).state,
                )

    def test_activation_rejects_missing_preflight_or_epoch_mismatch(self):
        activation_allowed = self.require("activation_allowed")
        cases = []
        missing_preflight = self.activation_receipt()
        del missing_preflight["target_preflight"]
        cases.append(("TARGET_PREFLIGHT_REQUIRED", missing_preflight))
        wrong_epoch = self.activation_receipt()
        wrong_epoch["new_epoch"] = 6
        cases.append(("ACTIVATION_CAUSAL_MISMATCH", wrong_epoch))

        for expected, receipt in cases:
            with self.subTest(expected=expected):
                decision = activation_allowed(
                    self.accepted_fence(),
                    stop_receipt=self.stop_receipt(),
                    preflight_receipt=self.preflight_receipt(),
                    activation_receipt=receipt,
                    source_reachable=True,
                    enforceable_revocation=False,
                )
                self.assertEqual(expected, decision.code)

    def test_receipt_set_rejects_duplicate_ids(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        first = self.stop_receipt()
        duplicate = self.activation_receipt()
        duplicate["receipt_id"] = first["receipt_id"]

        decision = receipt_set_allowed((first, duplicate))

        self.assertEqual("DUPLICATE_RECEIPT_ID", decision.code)

    def test_receipt_set_rejects_blank_unknown_or_incomplete_receipts(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        cases = []
        blank = self.stop_receipt()
        blank["receipt_id"] = "  "
        cases.append(blank)
        unknown = self.stop_receipt()
        unknown["receipt_type"] = "MAGIC"
        cases.append(unknown)
        missing_common = self.stop_receipt()
        del missing_common["accepted_commit_sha"]
        cases.append(missing_common)
        wrong_parent = self.activation_receipt()
        wrong_parent["causal_parent_ref"] = "different-stop"
        cases.append(wrong_parent)

        for receipt in cases:
            with self.subTest(receipt=receipt):
                self.assertEqual(
                    "RECEIPT_INVALID",
                    receipt_set_allowed((receipt,)).code,
                )

    def test_receipt_set_rejects_missing_type_specific_field(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        prepare = {
            "receipt_id": "prepare-1",
            "receipt_type": "PREPARE",
            "migration_id": "migration-1",
            "repository_or_project_id": "project-a",
            "executor_id": "dev-a",
            "prior_epoch": 3,
            "new_epoch": 4,
            "causal_parent_ref": "fence-3",
            "accepted_commit_sha": "commit-4",
            "task_checkpoint_refs": ["commit-4"],
            "candidate_refs": ["tree-4"],
            "workspace_disposition_refs": [],
            "actor_executor_id": "pm-a",
            "actor_provider_class": "local-standalone",
            "observed_outcome": "PREPARED",
            "registry_evidence": "NOT_APPLICABLE",
            "timestamp": "2026-01-01T00:00:00Z",
            "review_date": "2026-01-02",
        }

        self.assertEqual("RECEIPT_INVALID", receipt_set_allowed((prepare,)).code)

    def test_receipt_set_rejects_empty_set_bad_dates_and_mapping_enum(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        validate_receipt = self.require("validate_receipt")
        self.assertEqual("RECEIPT_INVALID", receipt_set_allowed(()).code)

        bad_timestamp = self.stop_receipt()
        bad_timestamp["timestamp"] = "not-a-timestamp"
        bad_review = self.stop_receipt()
        bad_review["review_date"] = "2026-99-99"
        bad_mapping = self.activation_receipt()
        bad_mapping["mapping_result"] = "MAYBE"
        for receipt in (bad_timestamp, bad_review, bad_mapping):
            with self.subTest(receipt=receipt):
                self.assertEqual("RECEIPT_INVALID", validate_receipt(receipt).code)

    def test_receipt_set_accepts_complete_typed_causal_receipts(self):
        receipt_set_allowed = self.require("receipt_set_allowed")

        self.assertEqual(
            "ALLOW",
            receipt_set_allowed(
                (
                    self.stop_receipt(),
                    self.preflight_receipt(),
                    self.activation_receipt(),
                ),
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )

    def test_receipt_set_rejects_orphan_or_wrong_type_activation_parent(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        orphan = receipt_set_allowed(
            (self.activation_receipt(),),
            accepted_root_ref="fence-4",
            affected_executor_ids=("dev-a",),
            migration_mode="role",
        )

        wrong_type = self.stop_receipt()
        wrong_type["receipt_type"] = "TARGET_PREFLIGHT"
        wrong_type["target_preflight"] = "PASS"
        wrong_type["target_placement_class"] = "local-standalone"
        wrong_type_result = receipt_set_allowed(
            (wrong_type, self.activation_receipt()),
            accepted_root_ref="fence-4",
            affected_executor_ids=("dev-a",),
            migration_mode="role",
        )

        self.assertEqual("RECEIPT_INVALID", orphan.code)
        self.assertEqual("RECEIPT_INVALID", wrong_type_result.code)

    def test_receipt_set_rejects_cross_identity_epoch_or_cutover_edges(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        mutations = {
            "migration_id": "migration-other",
            "repository_or_project_id": "project-other",
            "executor_id": "qa-a",
            "cutover_parent": "fence-other",
            "new_epoch": 3,
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                stop = self.stop_receipt()
                stop[field] = value
                self.assertEqual(
                    "RECEIPT_INVALID",
                    receipt_set_allowed(
                        (stop, self.preflight_receipt(), self.activation_receipt()),
                        accepted_root_ref="fence-4",
                        affected_executor_ids=("dev-a",),
                        migration_mode="role",
                    ).code,
                )

    def test_receipts_reject_malformed_exact_evidence_and_list_elements(self):
        activation_allowed = self.require("activation_allowed")
        receipt_set_allowed = self.require("receipt_set_allowed")
        malformed = ("   ", 7, True, {"bad": "value"}, None)
        for value in malformed:
            for stop_field, activation_field in (
                ("final_checkpoint", "task_checkpoint"),
                ("candidate_tree", "candidate_tree"),
                ("workspace_custody", "workspace_custody"),
                ("cutover_parent", "cutover_parent"),
            ):
                with self.subTest(value=value, field=stop_field):
                    stop = self.stop_receipt()
                    activation = self.activation_receipt()
                    stop[stop_field] = value
                    activation[activation_field] = value
                    self.assertNotEqual(
                        "ALLOW",
                        activation_allowed(
                            self.accepted_fence(),
                            stop_receipt=stop,
                            preflight_receipt=self.preflight_receipt(),
                            activation_receipt=activation,
                            source_reachable=True,
                            enforceable_revocation=False,
                        ).code,
                    )

            with self.subTest(value=value, field="reference-list-element"):
                stop = self.stop_receipt()
                activation = self.activation_receipt()
                for field in ("task_checkpoint_refs", "candidate_refs", "workspace_disposition_refs"):
                    stop[field] = [value]
                    activation[field] = [value]
                self.assertEqual(
                    "RECEIPT_INVALID",
                    receipt_set_allowed((stop, activation)).code,
                )

    def test_receipts_reject_singular_reference_list_mismatch_and_duplicates(self):
        activation_allowed = self.require("activation_allowed")
        validate_receipt = self.require("validate_receipt")
        receipt_set_allowed = self.require("receipt_set_allowed")

        stop = self.stop_receipt()
        stop["task_checkpoint_refs"] = ["different-checkpoint"]
        self.assertNotEqual("ALLOW", validate_receipt(stop).code)
        self.assertNotEqual(
            "ALLOW",
            activation_allowed(
                self.accepted_fence(),
                stop_receipt=stop,
                preflight_receipt=self.preflight_receipt(),
                activation_receipt=self.activation_receipt(),
                source_reachable=True,
                enforceable_revocation=False,
            ).code,
        )

        activation = self.activation_receipt()
        activation["candidate_refs"] = ["different-tree"]
        self.assertNotEqual("ALLOW", validate_receipt(activation).code)

        duplicate_refs = self.stop_receipt()
        duplicate_refs["candidate_refs"] = ["tree-4", "tree-4"]
        self.assertEqual("RECEIPT_INVALID", receipt_set_allowed((duplicate_refs,)).code)

    def test_receipt_epochs_reject_bool_noninteger_and_invalid_ranges(self):
        validate_receipt = self.require("validate_receipt")
        cases = []
        for value in (True, "3", 3.0, None, -1):
            receipt = self.stop_receipt()
            receipt["prior_epoch"] = value
            cases.append(receipt)
        nonincrementing = self.stop_receipt()
        nonincrementing["new_epoch"] = nonincrementing["prior_epoch"]
        cases.append(nonincrementing)

        for receipt in cases:
            with self.subTest(receipt=receipt):
                self.assertEqual("RECEIPT_INVALID", validate_receipt(receipt).code)

        boundary = self.stop_receipt()
        boundary["prior_epoch"] = 0
        boundary["new_epoch"] = 1
        boundary["expected_epoch"] = 1
        self.assertEqual("ALLOW", validate_receipt(boundary).code)

    def test_publication_freeze_state_is_strict_boolean_and_paths_reject_controls(self):
        publication_allowed = self.require("publication_allowed")
        base = {
            "claim_project_id": "project-a",
            "claim_executor_id": "dev-a",
            "claim_epoch": 4,
            "claim_record_ref": "fence-4",
            "actor_executor_id": "pm-a",
            "migration_pm_executor_id": "pm-a",
            "migration_id": "migration-1",
        }
        for frozen in (None, 0, 1, "", "false", [], {}):
            for publication_class, path in (
                ("PRODUCT", "src/product.py"),
                ("TASK", "Tasks/TASK-1.md"),
                ("TEAM", "Team/TEAM.md"),
                ("MIGRATION_CONTROL", "Team/Migrations/migration-1/MIGRATION.md"),
            ):
                with self.subTest(frozen=frozen, publication_class=publication_class):
                    self.assertNotEqual(
                        "ALLOW",
                        publication_allowed(
                            self.accepted_fence(),
                            publication_class=publication_class,
                            frozen=frozen,
                            path=path,
                            **base,
                        ).code,
                    )

        self.assertEqual(
            "ALLOW",
            publication_allowed(
                self.accepted_fence(),
                publication_class="PRODUCT",
                frozen=False,
                path="src/product.py",
                **base,
            ).code,
        )
        for path in (
            "src/product.py\n",
            "src/product.py\r",
            "src/\x00product.py",
            " src/product.py",
            "src/product.py ",
            "src/ product.py",
            "src/./product.py",
            "src//product.py",
            "src\\product.py",
        ):
            with self.subTest(path=repr(path)):
                self.assertEqual(
                    "PUBLICATION_PATH_INVALID",
                    publication_allowed(
                        self.accepted_fence(),
                        publication_class="PRODUCT",
                        frozen=False,
                        path=path,
                        **base,
                    ).code,
                )

    def test_fence_state_custody_matrix_rejects_simultaneous_or_disagreeing_writers(self):
        from relocation_policy import FenceRecord

        publication_allowed = self.require("publication_allowed")
        invalid = (
            ("ACTIVE", "ACTIVE", "TARGET_ACTIVE"),
            ("ACTIVE", "READY", "SOURCE_ACTIVE"),
            ("ACTIVE", "PREFLIGHTED", "TARGET_PENDING"),
            ("STOP_REQUESTED", "ACTIVE", "TARGET_ACTIVE"),
            ("STOPPED", "ACTIVE", "SOURCE_ACTIVE"),
            ("STOPPED", "READY", "TARGET_ACTIVE"),
        )
        for source_state, target_state, custody in invalid:
            with self.subTest(source=source_state, target=target_state, custody=custody):
                fence = FenceRecord(
                    "project-a", "dev-a", 4, "fence-4", source_state, target_state, custody
                )
                decision = publication_allowed(
                    fence,
                    claim_project_id="project-a",
                    claim_executor_id="dev-a",
                    claim_epoch=4,
                    claim_record_ref="fence-4",
                    publication_class="PRODUCT",
                    frozen=False,
                    actor_executor_id="dev-a",
                    migration_pm_executor_id="pm-a",
                    path="src/product.py",
                    migration_id="migration-1",
                )
                self.assertEqual("FENCE_INVALID", decision.code)

        legal = (
            ("ACTIVE", "INACTIVE", "SOURCE_ACTIVE"),
            ("STOP_REQUESTED", "INACTIVE", "SOURCE_STOPPING"),
            ("STOPPED", "INACTIVE", "SOURCE_STOPPED"),
            ("STOPPED", "PREFLIGHTED", "TARGET_PREFLIGHT"),
            ("STOPPED", "READY", "TARGET_PENDING"),
            ("STOPPED", "ACTIVE", "TARGET_ACTIVE"),
        )
        for source_state, target_state, custody in legal:
            with self.subTest(legal=(source_state, target_state, custody)):
                fence = FenceRecord(
                    "project-a", "dev-a", 4, "fence-4", source_state, target_state, custody
                )
                self.assertNotEqual(
                    "FENCE_INVALID",
                    publication_allowed(
                        fence,
                        claim_project_id="project-a",
                        claim_executor_id="dev-a",
                        claim_epoch=4,
                        claim_record_ref="fence-4",
                        publication_class="PRODUCT",
                        frozen=False,
                        actor_executor_id="dev-a",
                        migration_pm_executor_id="pm-a",
                        path="src/product.py",
                        migration_id="migration-1",
                    ).code,
                )

    def test_activation_binds_cutover_commit_registry_and_preflight_receipt(self):
        activation_allowed = self.require("activation_allowed")
        receipt_set_allowed = self.require("receipt_set_allowed")
        for field, value in (
            ("accepted_cutover", "different-commit"),
            ("mapping_result", "MAPPING_ABSENT"),
            ("target_preflight_receipt", "preflight-other"),
        ):
            with self.subTest(field=field):
                activation = self.activation_receipt()
                activation[field] = value
                if field != "target_preflight_receipt":
                    self.assertNotEqual(
                        "ALLOW",
                        activation_allowed(
                            self.accepted_fence(),
                            stop_receipt=self.stop_receipt(),
                            preflight_receipt=self.preflight_receipt(),
                            activation_receipt=activation,
                            source_reachable=True,
                            enforceable_revocation=False,
                        ).code,
                    )
                self.assertEqual(
                    "RECEIPT_INVALID",
                    receipt_set_allowed(
                        (self.stop_receipt(), self.preflight_receipt(), activation),
                        accepted_root_ref="fence-4",
                        affected_executor_ids=("dev-a",),
                        migration_mode="role",
                    ).code,
                )

        for evidence in ("NOT_APPLICABLE", "MAPPING_ABSENT"):
            with self.subTest(remote_manual=evidence):
                preflight = self.preflight_receipt()
                preflight["actor_provider_class"] = "remote-manual"
                preflight["registry_evidence"] = evidence
                activation = self.activation_receipt()
                activation["actor_provider_class"] = "remote-manual"
                activation["registry_evidence"] = evidence
                activation["mapping_result"] = evidence
                self.assertEqual(
                    "ALLOW",
                    receipt_set_allowed(
                        (self.stop_receipt(), preflight, activation),
                        accepted_root_ref="fence-4",
                        affected_executor_ids=("dev-a",),
                        migration_mode="role",
                    ).code,
                )

    def test_remote_manual_registry_absence_rejects_collision_or_observation(self):
        registry_mapping_allowed = self.require("registry_mapping_allowed")
        base = {
            "expected_executor_id": "vendor-a",
            "executor_mode": "remote_manual",
            "mapping_present": False,
            "local_authority": False,
            "read_back": False,
        }
        self.assertEqual(
            "ALLOW_REMOTE_MANUAL",
            registry_mapping_allowed(observed_executor_id=None, collision=False, **base).code,
        )
        self.assertEqual(
            "REGISTRY_CONFLICT",
            registry_mapping_allowed(observed_executor_id=None, collision=True, **base).code,
        )
        self.assertEqual(
            "REGISTRY_CONFLICT",
            registry_mapping_allowed(observed_executor_id="qa-a", collision=False, **base).code,
        )

    def test_all_receipt_types_enforce_typed_semantics_and_causal_context(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        validate_receipt = self.require("validate_receipt")

        malformed_preflight = self.preflight_receipt()
        malformed_preflight["target_preflight"] = "MAYBE"
        self.assertEqual("RECEIPT_INVALID", validate_receipt(malformed_preflight).code)

        partial = self.preflight_receipt()
        partial.update(
            receipt_id="partial-1",
            receipt_type="PARTIAL_DISPOSITION",
            causal_parent_ref="preflight-1",
            prior_epoch=5,
            new_epoch=6,
            observed_outcome="PARTIAL_BLOCKED",
            blocked_from_state="UNKNOWN",
            permitted_successors=["MAGIC"],
        )
        self.assertEqual("RECEIPT_INVALID", validate_receipt(partial).code)

        rollback = self.activation_receipt()
        rollback.update(
            receipt_id="rollback-1",
            receipt_type="FORWARD_ROLLBACK",
            causal_parent_ref="activation-1",
            prior_epoch=5,
            new_epoch=6,
            observed_outcome="FORWARD_ROLLBACK",
            rollback_target_epoch=0,
            causal_activation_receipt="activation-1",
        )
        self.assertEqual("RECEIPT_INVALID", validate_receipt(rollback).code)

        self.assertEqual(
            "RECEIPT_CONTEXT_REQUIRED",
            receipt_set_allowed((self.stop_receipt(), self.activation_receipt())).code,
        )
        self.assertEqual(
            "RECEIPT_INVALID",
            receipt_set_allowed(
                (self.completion_receipt(),),
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )

    def test_receipt_graph_accepts_one_closed_chain_and_rejects_completion_set_drift(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        chain = (
            self.prepare_receipt(),
            self.stop_receipt(),
            self.preflight_receipt(),
            self.activation_receipt(),
            self.completion_receipt(),
        )
        self.assertEqual(
            "ALLOW",
            receipt_set_allowed(
                chain,
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )
        for accounted in ([], ["qa-a"], ["dev-a", "qa-a"], ["dev-a", "dev-a"]):
            with self.subTest(accounted=accounted):
                completion = self.completion_receipt()
                completion["accounted_executor_ids"] = accounted
                self.assertEqual(
                    "RECEIPT_INVALID",
                    receipt_set_allowed(
                        (*chain[:-1], completion),
                        accepted_root_ref="fence-4",
                        affected_executor_ids=("dev-a",),
                        migration_mode="role",
                    ).code,
                )

    def test_receipt_graph_rejects_wrong_parent_for_every_receipt_type(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        prepare = self.prepare_receipt()
        stop = self.stop_receipt()
        preflight = self.preflight_receipt()
        activation = self.activation_receipt()

        freeze = dict(prepare)
        freeze.update(
            receipt_id="freeze-1",
            receipt_type="FREEZE",
            causal_parent_ref="prepare-1",
            prior_epoch=3,
            new_epoch=4,
            observed_outcome="FROZEN",
            affected_executor_ids=["dev-a"],
            stopped_executor_ids=["dev-a"],
            source_stop_receipt_refs=["stop-1"],
        )
        partial = dict(preflight)
        partial.update(
            receipt_id="partial-1",
            receipt_type="PARTIAL_DISPOSITION",
            causal_parent_ref="preflight-1",
            prior_epoch=5,
            new_epoch=6,
            observed_outcome="PARTIAL_BLOCKED",
            blocked_from_state="RESUMING",
            permitted_successors=["RESUMING", "CANCELLATION", "FORWARD_ROLLBACK"],
        )
        cancellation = dict(prepare)
        cancellation.update(
            receipt_id="cancel-1",
            receipt_type="CANCELLATION",
            executor_id="dev-a",
            causal_parent_ref="prepare-1",
            prior_epoch=3,
            new_epoch=4,
            observed_outcome="SOURCE_RETAINED",
            terminal_disposition="SOURCE_RETAINED",
            source_state="ACTIVE",
            target_state="INACTIVE",
        )
        rollback = dict(activation)
        rollback.update(
            receipt_id="rollback-1",
            receipt_type="FORWARD_ROLLBACK",
            causal_parent_ref="activation-1",
            prior_epoch=5,
            new_epoch=6,
            observed_outcome="FORWARD_ROLLBACK",
            rollback_target_epoch=6,
            causal_activation_receipt="activation-1",
        )
        completion = self.completion_receipt()

        cases = (
            (({**prepare, "causal_parent_ref": "wrong-root"},),),
            (({**stop, "causal_parent_ref": "wrong-root", "cutover_parent": "wrong-root"},),),
            ((prepare, stop, {**freeze, "causal_parent_ref": "missing"}),),
            ((stop, {**preflight, "causal_parent_ref": "missing"}),),
            ((stop, preflight, {**activation, "causal_parent_ref": "missing"}),),
            ((stop, preflight, {**partial, "causal_parent_ref": "missing"}),),
            ((prepare, {**cancellation, "causal_parent_ref": "missing"}),),
            ((stop, preflight, activation, {**rollback, "causal_parent_ref": "missing"}),),
            ((stop, preflight, activation, {**completion, "causal_parent_ref": "missing"}),),
        )
        for wrapped in cases:
            receipts = wrapped[0]
            with self.subTest(receipt_types=[item["receipt_type"] for item in receipts]):
                self.assertEqual(
                    "RECEIPT_INVALID",
                    receipt_set_allowed(
                        receipts,
                        accepted_root_ref="fence-4",
                        affected_executor_ids=("dev-a",),
                        migration_mode="role",
                    ).code,
                )

    def test_receipt_graph_accepts_closed_two_executor_chain_and_typed_cancellation(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        validate_receipt = self.require("validate_receipt")

        prepare = self.prepare_receipt()
        prepare["affected_executor_ids"] = ["dev-a", "qa-a"]
        qa_stop = self.stop_receipt()
        qa_stop.update(receipt_id="stop-qa", executor_id="qa-a")
        qa_preflight = self.preflight_receipt()
        qa_preflight.update(
            receipt_id="preflight-qa",
            executor_id="qa-a",
            causal_parent_ref="stop-qa",
            actor_executor_id="qa-a-target",
        )
        qa_activation = self.activation_receipt()
        qa_activation.update(
            receipt_id="activation-qa",
            executor_id="qa-a",
            causal_parent_ref="stop-qa",
            causal_stop_receipt="stop-qa",
            target_preflight_receipt="preflight-qa",
            actor_executor_id="qa-a-target",
        )
        completion = self.completion_receipt()
        completion["accounted_executor_ids"] = ["dev-a", "qa-a"]
        freeze = dict(prepare)
        freeze.update(
            receipt_id="freeze-1",
            receipt_type="FREEZE",
            causal_parent_ref="prepare-1",
            prior_epoch=3,
            new_epoch=4,
            observed_outcome="FROZEN",
            stopped_executor_ids=["dev-a", "qa-a"],
            source_stop_receipt_refs=["stop-1", "stop-qa"],
        )
        chain = (
            prepare,
            self.stop_receipt(),
            qa_stop,
            freeze,
            self.preflight_receipt(),
            qa_preflight,
            self.activation_receipt(),
            qa_activation,
            completion,
        )
        self.assertEqual(
            "ALLOW",
            receipt_set_allowed(
                chain,
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a", "qa-a"),
                migration_mode="team",
            ).code,
        )

        before_stop = dict(prepare)
        before_stop.update(
            receipt_id="cancel-before",
            receipt_type="CANCELLATION",
            executor_id="dev-a",
            causal_parent_ref="prepare-1",
            prior_epoch=3,
            new_epoch=4,
            observed_outcome="SOURCE_RETAINED",
            terminal_disposition="SOURCE_RETAINED",
            source_state="ACTIVE",
            target_state="INACTIVE",
        )
        after_stop = dict(self.stop_receipt())
        after_stop.update(
            receipt_id="cancel-after",
            receipt_type="CANCELLATION",
            causal_parent_ref="stop-1",
            prior_epoch=4,
            new_epoch=5,
            observed_outcome="REACTIVATION_REQUIRED",
            terminal_disposition="REACTIVATION_REQUIRED",
            source_state="STOPPED",
            target_state="READY",
            causal_stop_receipt="stop-1",
        )
        self.assertEqual("ALLOW", validate_receipt(before_stop).code)
        self.assertEqual("ALLOW", validate_receipt(after_stop).code)
        invalid_active_target = dict(after_stop)
        invalid_active_target["target_state"] = "ACTIVE"
        self.assertEqual("RECEIPT_INVALID", validate_receipt(invalid_active_target).code)

    def test_activation_requires_included_same_identity_pass_preflight_in_both_apis(self):
        activation_allowed = self.require("activation_allowed")
        receipt_set_allowed = self.require("receipt_set_allowed")
        stop = self.stop_receipt()
        preflight = self.preflight_receipt()
        activation = self.activation_receipt()

        self.assertEqual(
            "ALLOW",
            activation_allowed(
                self.accepted_fence(),
                stop_receipt=stop,
                preflight_receipt=preflight,
                activation_receipt=activation,
                source_reachable=True,
                enforceable_revocation=False,
            ).code,
        )
        for mutation in ("missing", "wrong-type", "wrong-executor", "blocked"):
            with self.subTest(mutation=mutation):
                candidate = dict(preflight)
                if mutation == "missing":
                    candidate = None
                elif mutation == "wrong-type":
                    candidate["receipt_type"] = "PARTIAL_DISPOSITION"
                elif mutation == "wrong-executor":
                    candidate["executor_id"] = "qa-a"
                else:
                    candidate["target_preflight"] = "BLOCKED"
                    candidate["observed_outcome"] = "TARGET_PREFLIGHT_BLOCKED"
                self.assertNotEqual(
                    "ALLOW",
                    activation_allowed(
                        self.accepted_fence(),
                        stop_receipt=stop,
                        preflight_receipt=candidate,
                        activation_receipt=activation,
                        source_reachable=True,
                        enforceable_revocation=False,
                    ).code,
                )

        blocked_preflight = dict(preflight)
        blocked_preflight["target_preflight"] = "BLOCKED"
        blocked_preflight["observed_outcome"] = "TARGET_PREFLIGHT_BLOCKED"
        blocked_activation = dict(activation)
        blocked_activation["target_preflight"] = "BLOCKED"
        self.assertEqual(
            "RECEIPT_INVALID",
            receipt_set_allowed(
                (self.prepare_receipt(), stop, blocked_preflight, blocked_activation),
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )

    def test_completion_requires_external_root_prepare_and_team_freeze_lineage(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        prepare = self.prepare_receipt()
        stop = self.stop_receipt()
        preflight = self.preflight_receipt()
        activation = self.activation_receipt()
        completion = self.completion_receipt()
        role_chain = (prepare, stop, preflight, activation, completion)

        self.assertEqual(
            "ALLOW",
            receipt_set_allowed(
                role_chain,
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )
        self.assertEqual(
            "RECEIPT_INVALID",
            receipt_set_allowed(
                role_chain[1:],
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )
        self.assertEqual(
            "RECEIPT_INVALID",
            receipt_set_allowed(
                role_chain,
                accepted_root_ref="prepare-1",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )

        qa_stop = dict(stop)
        qa_stop.update(receipt_id="stop-qa", executor_id="qa-a")
        qa_preflight = dict(preflight)
        qa_preflight.update(
            receipt_id="preflight-qa",
            executor_id="qa-a",
            causal_parent_ref="stop-qa",
            actor_executor_id="qa-a-target",
        )
        qa_activation = dict(activation)
        qa_activation.update(
            receipt_id="activation-qa",
            executor_id="qa-a",
            causal_parent_ref="stop-qa",
            causal_stop_receipt="stop-qa",
            target_preflight_receipt="preflight-qa",
            actor_executor_id="qa-a-target",
        )
        prepare_team = dict(prepare)
        prepare_team["affected_executor_ids"] = ["dev-a", "qa-a"]
        completion_team = dict(completion)
        completion_team["accounted_executor_ids"] = ["dev-a", "qa-a"]
        team_without_freeze = (
            prepare_team,
            stop,
            qa_stop,
            preflight,
            qa_preflight,
            activation,
            qa_activation,
            completion_team,
        )
        self.assertEqual(
            "RECEIPT_INVALID",
            receipt_set_allowed(
                team_without_freeze,
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a", "qa-a"),
                migration_mode="team",
            ).code,
        )
        freeze = dict(prepare_team)
        freeze.update(
            receipt_id="freeze-1",
            receipt_type="FREEZE",
            causal_parent_ref="prepare-1",
            prior_epoch=3,
            new_epoch=4,
            observed_outcome="FROZEN",
            stopped_executor_ids=["dev-a", "qa-a"],
            source_stop_receipt_refs=["stop-1", "stop-qa"],
        )
        self.assertEqual(
            "ALLOW",
            receipt_set_allowed(
                (*team_without_freeze[:-1], freeze, completion_team),
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a", "qa-a"),
                migration_mode="team",
            ).code,
        )
        cross_lineage = dict(qa_stop)
        cross_lineage["migration_id"] = "migration-other"
        self.assertEqual(
            "RECEIPT_INVALID",
            receipt_set_allowed(
                (prepare_team, stop, cross_lineage, freeze),
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a", "qa-a"),
                migration_mode="team",
            ).code,
        )

    def test_append_only_graph_allows_later_generations_and_terminal_blocked(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        prepare = self.prepare_receipt()
        stop1 = self.stop_receipt()
        preflight1 = self.preflight_receipt()
        activation1 = self.activation_receipt()
        rollback = dict(activation1)
        rollback.update(
            receipt_id="rollback-1",
            receipt_type="FORWARD_ROLLBACK",
            causal_parent_ref="activation-1",
            prior_epoch=5,
            new_epoch=6,
            observed_outcome="FORWARD_ROLLBACK",
            rollback_target_epoch=6,
            causal_activation_receipt="activation-1",
        )
        stop2 = dict(stop1)
        stop2.update(
            receipt_id="stop-2",
            prior_epoch=6,
            new_epoch=7,
            expected_epoch=7,
            causal_parent_ref="rollback-1",
            cutover_parent="rollback-1",
        )
        preflight2 = dict(preflight1)
        preflight2.update(
            receipt_id="preflight-2",
            prior_epoch=7,
            new_epoch=8,
            causal_parent_ref="stop-2",
        )
        activation2 = dict(activation1)
        activation2.update(
            receipt_id="activation-2",
            prior_epoch=7,
            new_epoch=8,
            causal_parent_ref="stop-2",
            causal_stop_receipt="stop-2",
            target_preflight_receipt="preflight-2",
        )
        completion = self.completion_receipt()
        completion.update(
            prior_epoch=8,
            new_epoch=9,
            causal_parent_ref="activation-2",
        )
        history = (
            prepare,
            stop1,
            preflight1,
            activation1,
            rollback,
            stop2,
            preflight2,
            activation2,
            completion,
        )
        self.assertEqual(
            "ALLOW",
            receipt_set_allowed(
                history,
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )
        duplicate_event = dict(stop2)
        duplicate_event["receipt_id"] = "stop-2-copy"
        self.assertEqual(
            "RECEIPT_INVALID",
            receipt_set_allowed(
                (*history, duplicate_event),
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )

        terminal_blocked = dict(preflight1)
        terminal_blocked.update(
            receipt_id="blocked-1",
            receipt_type="PARTIAL_DISPOSITION",
            causal_parent_ref="preflight-1",
            prior_epoch=5,
            new_epoch=6,
            observed_outcome="TERMINAL_BLOCKED",
            blocked_from_state="RESUMING",
            permitted_successors=["RESUMING", "CANCELLATION", "FORWARD_ROLLBACK"],
            terminal_disposition="BLOCKED",
            disposition_owner_executor_id="pm-a",
            next_action="Retain protected custody",
            disposition_receipt_ref="blocked-1",
        )
        blocked_completion = self.completion_receipt()
        blocked_completion.update(
            prior_epoch=6,
            new_epoch=7,
            causal_parent_ref="blocked-1",
        )
        self.assertEqual(
            "ALLOW",
            receipt_set_allowed(
                (prepare, stop1, preflight1, terminal_blocked, blocked_completion),
                accepted_root_ref="fence-4",
                affected_executor_ids=("dev-a",),
                migration_mode="role",
            ).code,
        )

    def test_team_state_rejects_invalid_records_and_resolves_exact_receipts(self):
        derive_team_state = self.require("derive_team_state")
        invalid_records = (
            [{"executor_id": "dev-a", "source_state": "ACTIVE", "target_state": "ACTIVE", "custody": "TARGET_ACTIVE", "disposition": "RESUMED"}],
            [
                {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "ACTIVE", "custody": "TARGET_ACTIVE", "disposition": "RESUMED"},
                {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "ACTIVE", "custody": "TARGET_ACTIVE", "disposition": "RESUMED"},
            ],
            ["not-a-record"],
        )
        for records in invalid_records:
            with self.subTest(records=records):
                self.assertEqual(
                    "INVALID",
                    derive_team_state(
                        records,
                        affected_executor_ids=("dev-a",),
                        receipts=(),
                        accepted_root_ref="fence-4",
                        migration_mode="role",
                    ).state,
                )

    def test_team_state_accepts_valid_mixed_terminal_receipt_graphs(self):
        derive_team_state = self.require("derive_team_state")
        prepare = self.prepare_receipt()
        prepare["affected_executor_ids"] = ["dev-a", "qa-a"]
        dev_stop = self.stop_receipt()
        qa_stop = self.stop_receipt()
        qa_stop.update(receipt_id="stop-qa", executor_id="qa-a")
        freeze = dict(prepare)
        freeze.update(
            receipt_id="freeze-1",
            receipt_type="FREEZE",
            causal_parent_ref="prepare-1",
            prior_epoch=3,
            new_epoch=4,
            observed_outcome="FROZEN",
            stopped_executor_ids=["dev-a", "qa-a"],
            source_stop_receipt_refs=["stop-1", "stop-qa"],
        )
        dev_preflight = self.preflight_receipt()
        dev_activation = self.activation_receipt()

        for disposition in ("BLOCKED", "CANCELLED", "FORWARD_ROLLBACK"):
            qa_receipts = []
            if disposition in {"BLOCKED", "FORWARD_ROLLBACK"}:
                qa_preflight = self.preflight_receipt()
                qa_preflight.update(
                    receipt_id="preflight-qa",
                    executor_id="qa-a",
                    causal_parent_ref="stop-qa",
                    actor_executor_id="qa-a-target",
                )
                qa_receipts.append(qa_preflight)
            if disposition == "BLOCKED":
                terminal = dict(qa_receipts[-1])
                terminal.update(
                    receipt_id="blocked-qa",
                    receipt_type="PARTIAL_DISPOSITION",
                    causal_parent_ref="preflight-qa",
                    prior_epoch=5,
                    new_epoch=6,
                    observed_outcome="TERMINAL_BLOCKED",
                    blocked_from_state="RESUMING",
                    permitted_successors=["RESUMING", "CANCELLATION", "FORWARD_ROLLBACK"],
                    terminal_disposition="BLOCKED",
                    disposition_owner_executor_id="pm-a",
                    next_action="Retain protected custody",
                    disposition_receipt_ref="blocked-qa",
                )
                qa_record_state = ("STOPPED", "INACTIVE", "SOURCE_STOPPED")
            elif disposition == "CANCELLED":
                terminal = dict(qa_stop)
                terminal.update(
                    receipt_id="cancel-qa",
                    receipt_type="CANCELLATION",
                    causal_parent_ref="stop-qa",
                    prior_epoch=4,
                    new_epoch=5,
                    observed_outcome="REACTIVATION_REQUIRED",
                    terminal_disposition="REACTIVATION_REQUIRED",
                    source_state="STOPPED",
                    target_state="READY",
                    causal_stop_receipt="stop-qa",
                )
                qa_record_state = ("STOPPED", "READY", "TARGET_PENDING")
            else:
                qa_activation = self.activation_receipt()
                qa_activation.update(
                    receipt_id="activation-qa",
                    executor_id="qa-a",
                    causal_parent_ref="stop-qa",
                    causal_stop_receipt="stop-qa",
                    target_preflight_receipt="preflight-qa",
                    actor_executor_id="qa-a-target",
                )
                qa_receipts.append(qa_activation)
                terminal = dict(qa_activation)
                terminal.update(
                    receipt_id="rollback-qa",
                    receipt_type="FORWARD_ROLLBACK",
                    causal_parent_ref="activation-qa",
                    prior_epoch=5,
                    new_epoch=6,
                    observed_outcome="FORWARD_ROLLBACK",
                    rollback_target_epoch=6,
                    causal_activation_receipt="activation-qa",
                )
                qa_record_state = ("STOPPED", "INACTIVE", "SOURCE_STOPPED")
            qa_receipts.append(terminal)
            completion = self.completion_receipt()
            completion.update(
                prior_epoch=terminal["new_epoch"],
                new_epoch=terminal["new_epoch"] + 1,
                causal_parent_ref=terminal["receipt_id"],
                accounted_executor_ids=["dev-a", "qa-a"],
            )
            receipts = (
                prepare,
                dev_stop,
                qa_stop,
                freeze,
                dev_preflight,
                dev_activation,
                *qa_receipts,
                completion,
            )
            records = [
                {
                    "executor_id": "dev-a",
                    "source_state": "STOPPED",
                    "target_state": "ACTIVE",
                    "custody": "TARGET_ACTIVE",
                    "disposition": "RESUMED",
                    "disposition_receipt_ref": "activation-1",
                },
                {
                    "executor_id": "qa-a",
                    "source_state": qa_record_state[0],
                    "target_state": qa_record_state[1],
                    "custody": qa_record_state[2],
                    "disposition": disposition,
                    "disposition_owner_executor_id": "pm-a",
                    "review_date": "2026-01-02",
                    "next_action": "Retain terminal custody",
                    "disposition_receipt_ref": terminal["receipt_id"],
                },
            ]
            with self.subTest(disposition=disposition):
                state = derive_team_state(
                    records,
                    affected_executor_ids=("dev-a", "qa-a"),
                    receipts=receipts,
                    accepted_root_ref="fence-4",
                    migration_mode="team",
                )
                self.assertEqual("COMPLETE", state.state)
                self.assertEqual(("dev-a",), state.active_targets)
                self.assertEqual(("qa-a",) if disposition == "BLOCKED" else (), state.blocked_executors)

    def test_same_next_epoch_branches_are_serialized_by_accepted_parent(self):
        materialize_successor = self.require("materialize_successor")
        accepted = self.accepted_fence()

        first_decision, provider_current = materialize_successor(
            accepted,
            expected_prior_epoch=4,
            expected_prior_ref="fence-4",
            new_epoch=5,
            new_record_ref="fence-5-a",
        )
        second_decision, unchanged = materialize_successor(
            provider_current,
            expected_prior_epoch=4,
            expected_prior_ref="fence-4",
            new_epoch=5,
            new_record_ref="fence-5-b",
        )

        self.assertEqual("ALLOW", first_decision.code)
        self.assertEqual("WRITER_CONFLICT", second_decision.code)
        self.assertEqual("fence-5-a", unchanged.record_ref)


if __name__ == "__main__":
    unittest.main(verbosity=2)
