# Working together

Use one personal GitHub account per person. Raazia owns this Team C repository today. Invite Maham as a collaborator using her verified GitHub username. A central NRPU GitHub organization can own the integration repository, with members signing in using their own accounts. Do not share an NRPU account password.

## Every work item
1. Choose a roadmap task and state its acceptance criteria.
2. Pull main and create `feat/raazia-<task>` or `feat/maham-<task>`.
3. Implement only that task; keep generated outputs and raw research files outside Git.
4. Run lint, relevant tests, and schema drift checks. Run the frontend build for UI changes.
5. Push the branch and open a pull request. Include units, evidence, missing-data behavior and validation.
6. Ask the other person to review. Resolve comments and merge only passing changes.
7. Update MEMORY.md with decisions and open blockers. Do not copy the whole chat.

```bash
git clone https://github.com/Raazia-Imran/WISP_TEAM_C.git
cd WISP_TEAM_C
git switch main
git pull --ff-only
git switch -c feat/raazia-e5-power
# implement and check
git add team_c tests docs
git commit -m "Implement evidence-aware power profile evaluation"
git push -u origin feat/raazia-e5-power
```

Weekly central integration: freeze a tested Team C commit, run shared contract fixtures with Team B/A, and open a central-repository PR for the `team_c/` package plus shared contract updates. Keep root tooling adapted to the central monorepo. Do not paste an entire independent repository over central files. Pick one synchronization policy in docs/INTEGRATION.md and keep a commit mapping.

Branch protection is a follow-up administrator action: require one peer approval, CI/backend and CI/frontend, and block force-push/deletion on main. These settings have not been configured by the starter. GitHub permissions may limit what the connector can change. CODEOWNERS is only enabled after Maham's actual username is known; never add guessed identities.

Official references: https://docs.github.com/en/organizations/managing-membership-in-your-organization/can-i-create-accounts-for-people-in-my-organization and https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
