# Team repository and central NRPU integration

## Recommended ownership
Keep WISP_TEAM_C as the shared workspace for Raazia/Maham. A central NRPU organization repository contains team_a/, team_b/, team_c/, frontend/ and shared contracts. Personal repositories can support experiments, but authoritative Team C implementation lives in one repository. Membership uses personal accounts; institutional email is a contact/ownership continuity aid, not a shared password.

## Choose one synchronization method
Preferred once central repo exists: develop Team C work in central `team_c/` feature branches and use WISP_TEAM_C for early experiments. If teams must keep separate repos, use weekly reviewed imports with commit mapping or a maintained git subtree. Do not alternate manual copies and subtree merges. Since the central URL/permissions are not supplied, synchronization is specified but not configured.

## Weekly reviewable integration
1. Freeze a passing Team C commit and record its SHA.
2. Run backend/tests/schema checks and Team B consumer fixture.
3. Compare shared dependencies and contract versions; resolve differences before copying.
4. Create a central feature branch and integrate only Team C package + necessary shared contracts/tooling.
5. Include source SHA, contract changes, tests, limitations and rollback in the PR.
6. Have Team B/A review affected interfaces; merge after checks.
7. Record central SHA and any adaptations in integration ledger.

| Team C SHA | Central SHA | Contract version | Checks | Adaptations | Date |
|---|---|---|---|---|---|
| Pending first integration | Pending central repository | Draft v1 | Not yet run cross-team | None | Pending |

## Agreement items
Team A field names/source boundaries; Team B heat/equipment/power return semantics; currency/timezone; shared UI owner; canonical engine IDs; source/rule activation policy; data snapshot lifecycle; error statuses. Public/private research data visibility must be decided before uploading raw archives into any public repo.

## Git practice
Short feature branches and small PRs reduce conflicts. Peer-review contracts first. Weekly integration is the minimum; share a contract skeleton and fixture immediately rather than waiting for a whole engine. Never force-push main to overwrite another team's work. CodeRabbit may help review code but cannot verify OEM facts, formula validity or scientific applicability.
