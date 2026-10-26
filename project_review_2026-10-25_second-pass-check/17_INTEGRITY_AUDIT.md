# 17 · Integrity audit: is the automation itself intact
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `the wiring of the automation, checked by code` (every verb, script, hook, skill, setting, review template, board page, living doc, test run and entry block) · fills from: the hub's menu and dispatcher, the tests, the entry docs, the hooks and skill files, the settings, the review templates and folders, the board, git · 📏 = measured by code · 🧠 = the reviewer's judgement. Only the numbers are this project's; the sections are the same in every project.*

> 🎧 **In one breath:** The standard's wiring holds in this project: every check that applies passes, and the three that skip name things this project does not have. No row gapes. The one gap to close first hides behind a green row: "tests green" passes with no test at all, because nothing is configured to run. Close it by giving the project a suite, and the row will mean what it says. What the audit cannot see is the project's own wiring, which today is one script in a scratchpad and nothing else.

📏 The checks below are the standard's wiring inside this project; the project's own wiring (its hooks, its scripts in its code, the tests) is not checked here and belongs in §4.

**The numbers:** the checks are the audit's rows at 2026-10-25 14:39, the same as the board's `AUDIT.md`; the order of the gaps and what the audit does not see are the reviewer's.

## 1. The checks (📏 at 2026-10-25 14:39; the same rows as the board's `AUDIT.md`, rebuilt after every reply)
| # | Check | Result | Detail |
|---|---|---|---|
| 1 | verbs dispatched (every verb in the menu has a handler) | ✅ | 60 verbs dispatched, 32 in the menu; dispatched, not in the menu: `ask`, `catchup`, `close-version`, `compile`, `context`, `dashboard`, `digest`, `drill` … 14 … |
| 2 | verbs in the entry docs (README or QUICKSTART names every verb) | ⏭️ | the entry docs are not living docs here |
| 3 | verbs tested (a test names every verb) | ✅ | every verb is named in a test |
| 4 | scripts tested (a test names every script) | ✅ | all 58 scripts are named in a test |
| 5 | scripts in the map (the architecture doc names every script) | ✅ | every script is in the architecture doc |
| 6 | scripts under the line (no script over the size line) | ✅ | the biggest is under 1200 lines |
| 7 | hooks wired (every hook command names a verb; the events are set) | ✅ | 3 hooks file(s), every command names a verb, the 5 events are set |
| 8 | hooks explained (the hooks page has words for every verb a hook runs) | ✅ | all 15 hooks are explained on HOOKS.md |
| 9 | enforced by (every rule names the code that holds it, and that code exists) | ✅ | 151 of 193 obligations and 60 of 72 preferences name the code that holds them |
| 10 | weight (no drill run clutters the project root) | ⏭️ | no review folder here |
| 11 | skills wired (every skill names a verb that exists and no person) | ✅ | 12 skill file(s), each names a verb and no person |
| 12 | settings documented (the glossary names every setting) | ✅ | all 9 settings are documented |
| 13 | review templates (every review template is there, in its shape) | ✅ | all 18 review templates are there, each with its legend and its tables, 13 drawn by code |
| 14 | review holes (the newest review has no hole left) | ⏭️ | no review folder yet |
| 15 | review fresh (the newest review is under review_every versions old) | ✅ | no review folder yet, 1 version folder(s) since |
| 16 | board pages (every page refresh writes exists) | ✅ | all 26 pages are there |
| 17 | living docs fresh (no living doc is behind the record) | ✅ | no living doc is behind the record |
| 18 | tests green (the newest measured run passed) | ✅ | 0 tests in v0.1.1 |
| 19 | entry blocks (every entry file carries the installer's block, short and directive) | ✅ | 3 entry file(s) carry the block, short and directive |

📏 19 checks: 16 hold, 0 gap(s), 3 not here. A ❌ row is a gap the model logs as a request; the code fixes nothing. A ⏭️ row names something this project does not have.

## 2. The gaps (📏)
- 🟢 No gap: every check holds.

## 3. Which gaps matter, in what order
1. **No gap in §2.** Every applicable check holds; nothing to order.
2. **Behind the green "tests green" row: the run had no tests.** The damage is a label without a measurement, so a phrasing regression in the outward set would pass every close; the fix is a suite in `test_suites`; the working model does it ([16](16_PRIORITIES.md) row 1).
3. **Behind the green "scripts under the line" row: no `code_dirs`, so no project script is measured.** The damage is that 13 (d) and the hygiene table say "nothing measured" instead of a number; the fix is the export script inside the project and one config line; the working model does it ([16](16_PRIORITIES.md) row 8).
4. **Behind the skipped "review holes" row: this folder was written in the same session as the work.** The damage is a reviewer with the worker's blind spots; the fix is the next review by a different model; the frontier model does it (06 §4 row 9).

## 4. What the audit does not see
| A verb wired and green can still … | The example | The next check to add |
|---|---|---|
| close green with nothing measured | `finish` in v0.1.1: "count not reported", closed partial, the audit's row 18 reads ✅ | tests green only when the newest run had at least one test; otherwise ⏭️ with "no suite configured" |
| run an acceptance list that proves little | three greps: one banned phrase and two files present; both finishes passed | acceptance commands counted per plan, with a floor the config sets |
| gate the edit tool and miss the shell | two `sed` lines and one heredoc in v0.1.1 left no backup and no stamp | a backup-diff row: files changed since the last finish with no backup before them |
| keep the record while the human reads nothing | 0 comments, 0 "tested" lines, 1 request open after the work was built | a row for "human read-back": at least one comment, tested line or close per version |
| hold the standard's wiring while the project's is unmeasured | no `code_dirs`, no `test_suites`, a script in the scratchpad | a row that lists the config lines unset in a project that has files to measure |
