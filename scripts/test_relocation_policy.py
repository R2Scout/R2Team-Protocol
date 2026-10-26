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
                    activation_receipt=self.activation_receipt(),
                    source_reachable=True,
                    enforceable_revocation=False,
                )
                self.assertEqual("ACTIVATION_IDENTITY_MISMATCH", decision.code)

    def test_activation_rejects_mismatched_cutover_parent(self):
        activation_allowed = self.require("activation_allowed")
        activation = self.activation_receipt()
        activation["cutover_parent"] = "different-fence"

        decision = activation_allowed(
            self.accepted_fence(),
            stop_receipt=self.stop_receipt(),
            activation_receipt=activation,
            source_reachable=True,
            enforceable_revocation=False,
        )

        self.assertEqual("ACTIVATION_CAUSAL_MISMATCH", decision.code)

    def test_partial_team_state_preserves_mixed_executor_custody(self):
        derive_team_state = self.require("derive_team_state")
        records = [
            {
                "executor_id": "dev-a",
                "source_state": "STOPPED",
                "target_state": "ACTIVE",
                "disposition": "RESUMED",
            },
            {
                "executor_id": "qa-a",
                "source_state": "STOPPED",
                "target_state": "INACTIVE",
                "disposition": "BLOCKED",
            },
        ]

        aggregate = derive_team_state(records)

        self.assertEqual("PARTIAL_BLOCKED", aggregate.state)
        self.assertEqual(("dev-a",), aggregate.active_targets)
        self.assertEqual(("qa-a",), aggregate.blocked_executors)

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

    def test_retained_executor_cannot_remain_in_frozen_affected_set(self):
        affected_set_allowed = self.require("affected_set_allowed")

        decision = affected_set_allowed(
            affected_executor_ids=("dev-a", "qa-a"),
            retained_executor_ids=("qa-a",),
            migration_state="FREEZE_PENDING",
        )

        self.assertEqual("RETAINED_SET_CONFLICT", decision.code)

    def test_team_state_is_derived_from_every_executor_record(self):
        derive_team_state = self.require("derive_team_state")
        cases = (
            (
                "COMPLETE",
                [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "ACTIVE", "disposition": "RESUMED"},
                    {"executor_id": "qa-a", "source_state": "STOPPED", "target_state": "ACTIVE", "disposition": "RESUMED"},
                ],
            ),
            (
                "READY_TO_RESUME",
                [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "READY", "disposition": "PENDING"},
                    {"executor_id": "qa-a", "source_state": "STOPPED", "target_state": "READY", "disposition": "PENDING"},
                ],
            ),
            (
                "FROZEN",
                [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "INACTIVE", "disposition": "PENDING"},
                    {"executor_id": "qa-a", "source_state": "STOPPED", "target_state": "INACTIVE", "disposition": "PENDING"},
                ],
            ),
        )

        for expected, records in cases:
            with self.subTest(expected=expected):
                self.assertEqual(expected, derive_team_state(records).state)

    def test_terminal_accounted_executor_can_complete_mixed_team(self):
        derive_team_state = self.require("derive_team_state")
        for disposition in ("BLOCKED", "CANCELLED", "FORWARD_ROLLBACK"):
            with self.subTest(disposition=disposition):
                records = [
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "ACTIVE", "disposition": "RESUMED"},
                    {
                        "executor_id": "qa-a",
                        "source_state": "STOPPED",
                        "target_state": "INACTIVE",
                        "disposition": disposition,
                        "disposition_owner_executor_id": "pm-a",
                        "review_date": "2026-01-02",
                        "next_action": "Retain terminal custody",
                        "disposition_receipt_ref": "receipt-terminal-1",
                    },
                ]
                self.assertEqual("COMPLETE", derive_team_state(records).state)

    def test_incomplete_terminal_disposition_remains_partial(self):
        derive_team_state = self.require("derive_team_state")
        base = {
            "executor_id": "qa-a",
            "source_state": "STOPPED",
            "target_state": "INACTIVE",
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
                    {"executor_id": "dev-a", "source_state": "STOPPED", "target_state": "ACTIVE", "disposition": "RESUMED"},
                    incomplete,
                ]
                self.assertEqual("PARTIAL_BLOCKED", derive_team_state(records).state)

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

    def test_receipt_set_accepts_complete_typed_causal_receipts(self):
        receipt_set_allowed = self.require("receipt_set_allowed")

        self.assertEqual(
            "ALLOW",
            receipt_set_allowed((self.stop_receipt(), self.activation_receipt())).code,
        )

    def test_receipt_set_rejects_orphan_or_wrong_type_activation_parent(self):
        receipt_set_allowed = self.require("receipt_set_allowed")
        orphan = receipt_set_allowed((self.activation_receipt(),))

        wrong_type = self.stop_receipt()
        wrong_type["receipt_type"] = "TARGET_PREFLIGHT"
        wrong_type["target_preflight"] = "PASS"
        wrong_type["target_placement_class"] = "local-standalone"
        wrong_type_result = receipt_set_allowed((wrong_type, self.activation_receipt()))

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
                    receipt_set_allowed((stop, self.activation_receipt())).code,
                )

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
