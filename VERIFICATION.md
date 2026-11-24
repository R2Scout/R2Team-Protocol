# R2Team 2.9 distribution verification

Prepared for the resource-lifetime and readable-workspace-name release on 2026-11-24. Source validation is distinct from project adoption, live cleanup, runtime behavior, and independent consuming-agent acceptance.

## Required release checks

Run package validation on a manifest-only copy of package.json plus required_files; local private routing must never enter the package. Run the four suites sequentially:

```text
python scripts/validate_package.py
python -B scripts/test_validate_package.py
python -B scripts/test_workspace_policy.py
python -B scripts/test_relocation_policy.py
python -B scripts/test_resource_lifetime.py
```

The source candidate passed 58 validator tests, 42 workspace tests, 73 relocation tests, and 21 resource-lifetime/directory tests: 194/194. Repeat these checks for the exact versioned release candidate and record its commit/tree in Tasks/TASK-R2TEAM-GIT-WORKTREE-FOLDERS-001.md. Check all six skills with the official skill-creator format validator, English-only Markdown, Python compilation, command-copy equality, payload hashes, and git diff --check.

The resource suite also verifies ordinary Git worktree leaf formation, preserved native IDs, unsafe/missing ID rejection, and refusal to fabricate application/legacy paths. The resource suite covers lifetime/purpose separation, portable names, explicit metadata, malformed/unknown records, owner/resource/event/reference-bound completion receipts, strict booleans, persistent decommission authority, review-only expiry, terminal-policy evidence, and non-bypass of existing allocation and closure gates. Fixtures perform no real filesystem, provider, process, cleanup, or scheduling effects. Format checks do not prove consuming-agent behavior.

## Publication evidence

Integrate the exact reviewed PR head, read back the merge SHA and remote main, then publish an annotated v2.9 tag and non-draft/non-prerelease GitHub Release at the verified accepted commit. Re-read the remote tag object, peeled commit, release fields, and versioned manifest before reporting publication. Keep v2.8 and v2.7 and their historical commits unchanged. A later task-only publication receipt may advance main without changing the tagged payload.

## Limits

NOT_RUN unless separately evidenced: installed user-skill replacement, downstream project adoption, real role-chat migration, independent consuming-agent review, live cleanup/decommission/rename, resource movement, provider revocation, product/runtime/production QA, and automation. PM update text is guidance, not delivery or adoption proof.

Historical v2.7 verification remains recoverable from its exact tag and source history; it is not reported as fresh 2.9 evidence. The existing relocation, queue-routing, evidence, and workspace safety contracts remain in force.
