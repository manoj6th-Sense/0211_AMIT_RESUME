# 08 · Decisions
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `the decisions a review leaves to the human, pre-ticked` · fills from: the open requests, the findings of 01 and 04, the roadmap · 📏 = measured by code · 🧠 = the reviewer's judgement. Only the numbers are this project's; the sections are the same in every project.*

> 🟣 The recommendation is ticked `[x]` on every question: it is the reviewer's prediction of what the human would pick. Change only what you disagree with (move the `x`, or comment on the line on the phone page). If you agree with everything, say **"defaults"**. Nothing is built, deleted or committed before your answer.

**The numbers:** the open requests below are the list at 2026-10-25 14:39; a number inside a question names the file of this folder it comes from.

## The open requests the decisions can draw on (📏)
| Request | Logged | Status | What it means |
|---|---|---|---|
| #1 | 2026-10-25 | open | Re-check the previous model's portfolio work for thoroughness, read every project in full, |

## The questions
**D1 · A real test suite for this documentation project?** (📏 Tests: count not reported; friction: not measured 1)
- [x] **A1** a small shell suite for the outward files, registered in `test_suites`, built by the working model next · [16](16_PRIORITIES.md) row 1
- [ ] **A2** keep the acceptance commands as the only check and set `test_suites` to an empty list · no row

**D2 · What should the GitHub link in the résumé header do?** (📏 the profile shows no public repository today; final report §3)
- [ ] ~~**B1** keep the link and publish repositories~~ · withdrawn v0.1.4: the human refused it, "do not make anything public… don't you dare"
- [ ] ~~**B2** drop the link until a repository is published~~ · withdrawn v0.1.4 for the same reason
- The question is asked again with only two choices, keep the link as it is or drop it; every repository stays private · [16](16_PRIORITIES.md) row 3

**D3 · Re-read the six unreadable project folders?** (📏 6 folders EPERM; the dossier's Verification Note)
- [x] **C1** grant the terminal Files and Folders access, then a session re-reads the six · [16](16_PRIORITIES.md) row 4
- [ ] **C2** keep them as first-pass descriptions, flagged · no row

**D4 · Close your request to re-check the earlier model work for thoroughness?** (📏 Requests: open 1, built in v0.1.1)
- [x] **D1** yes, close it in your words · [16](16_PRIORITIES.md) row 5
- [ ] **D2** not yet; read the exports first and say what to change · [16](16_PRIORITIES.md) row 5

The block, as `ask --json` printed it:

A bare "yes" = A1, B1, C1, D1.

**A · D1 · The Tests light reads nothing here (01 §1: count not reported; friction: not measured). Give this documentation project a real test suite?**
- ★ **A1** Yes: a small shell suite that checks the outward files (banned phrases, no Mermaid in the dossier, LinkedIn limits, exports present), registered in test_suites, built by the working model next [`python3 amx_impl_plan/plan_hub.py new`] — finish then measures something true instead of warning; the acceptance commands already do a third of this
- **A2** No: keep the acceptance commands as the only check and silence the warning with test_suites set to an empty list [`python3 amx_impl_plan/plan_hub.py settings set test_suites []`] — the project is Markdown; the warning is noise

**B · D2 · The résumé header links github.com/amit-malhotra1, which shows no public repository today (final report §3). What should the link do?**
- *(both choices withdrawn v0.1.4: each proposed publishing a repository, and the human refused it: "do not make anything public… don't you dare")*

**C · D3 · Six project folders stayed unreadable (dossier Verification Note). Re-read them?**
- ★ **C1** Yes: grant the terminal app Files and Folders access to Documents/GitHub, then a session re-reads the six and updates the notes and the outward set [`System Settings → Privacy & Security → Files and Folders`] — the six include PromptForge, SmartBrain and AMTrix Studio, which the résumé names
- **C2** No: keep them as first-pass descriptions, flagged as such [`nothing`] — the flagged wording is honest and the résumé does not lean on them

**D · D4 · Your request to re-check the earlier model work for thoroughness (#1) is built and closed in v0.1.1. Close it?**
- ★ **D1** Yes, close #1 as done in my words [`python3 amx_impl_plan/plan_hub.py asks done 1 --said <your words>`] — the Walkthrough v0.1.1 lists what was built and the exports exist
- **D2** Not yet: I will read the exports first and say what to change [`open FINAL_RESUMES/exports/AMIT_MALHOTRA_FDE_RESUME_2026.pdf`] — the résumé is the deliverable; a read-through may change it

**E · Open the deck** (one card per question above).

## Your answers, read back
| Question | The ★ | Your letter | What it set in motion |
|---|---|---|---|
| D1 · the test suite | A1 | A1 ("Yes") | kept: the suite built in v0.1.3; request #3 closed |
| D2 · the GitHub link | B1 | neither: "do not make anything public… don't you dare" | the star withdrawn; requests #10 (never publish) and #12 (a standard request: `ask --read` recorded B1 by mistake); the link question asked again |
| D3 · the six re-reads | C1 | C1 ("Yes") | the human's step: grant Files and Folders access; then request #5 |
| D4 · close request #1 | D1 | D1 ("Yes") | request #1 closed |
