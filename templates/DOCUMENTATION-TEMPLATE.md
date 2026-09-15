# Documentation map template

During setup, merge into the existing README/docs index; create another file only when needed. Do not maintain competing maps.

## Project

Purpose, users, boundaries, overall system and current stage.

## Where to look

- Protocol/TEAM and role contracts:
- Current OpenSpec specifications:
- Active changes and TASKs:
- Architecture and significant ADRs:
- UX/research, if present:
- Run/build/test commands:
- Operations/deployment/rollback:
- Access-request procedure, without secrets:

## Specification coverage

| Capability | Current knowledge source | Spec/change | Evidence | Coverage/gap | Next priority |
| --- | --- | --- | --- | --- | --- |
| Actual capability | Verified document/code/ref | Reference or absent | Check or NOT_RUN | Covered / Partial / Unknown | Next slice |

One completed OpenSpec change does not document an entire MVP. Observed behavior is not automatically the intended requirement. Update specs, design, tests and documentation together for the affected area.

## Maintenance

The executor updates affected documentation in the same PR. PM checks coverage of the accepted scope. Record significant architectural decisions as ADRs when needed. Requirements/scenarios do not replace user instructions or an operational runbook.
