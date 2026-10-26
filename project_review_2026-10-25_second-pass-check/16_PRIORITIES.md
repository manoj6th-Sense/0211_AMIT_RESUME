# 16 · The priorities: every suggestion of this review, who does it, in what order
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `the review's suggestions as a work list` · fills from: the previous review's open rows, the requests · 📏 = measured by code · 🧠 = the reviewer's judgement. Only the numbers are this project's; the sections are the same in every project. `plan_hub.py review-jobs <folder>` turns each row without a request number into a request (its note carries the priority, the size and who does it) and writes the number back. Comment on any row before it runs; move a priority by editing the cell.*

> 🎧 **In one breath:** Nine suggestions, none carried, since this is the first review. Six are easy, one is medium and two are hard. The working model takes the test suite, the config lines and the export script; the human takes the GitHub decision, the folder access, the close of the one request and the token rotation; the frontier model takes the six re-reads and the standard's backup-diff check. None of them is a change to the résumé's content: the words wait for the re-reads and the human's read-through. The first row is the one that changes what every later finish means.

**The numbers:** the carried rows and the Request column are code's at 2026-10-25 14:39; the new rows, their priorities and sizes are the reviewer's, the human edits them.

**Legend:** Priority P1 = this week · P2 = this version · P3 = when its turn comes. Size: easy = one function and its test; medium = one script; hard = several scripts or a design. Who: **working** = the working model, on its own · **frontier** = the frontier model, one per session · **human** = only the human can.

## 1. The table (the verb reads this: keep the columns)
| # | Suggestion | From | Priority | Size | Who | Request | How |
|---|---|---|---|---|---|---|---|
| | *(no row carried from the previous review)* | | | | | #2 | |
| 1 | Give the project a test suite it owns: one shell script that checks the outward files (banned phrases, no Mermaid in the dossier, LinkedIn lengths, exports present, privacy words), registered in `test_suites`. | 01 G1, 02 §4 Proof, 04 W1, 12 §6 | P1 | medium | working | #3 | `tests/check_outward.sh` and `tests/banned_phrases.txt`; exit: `python3 amx_impl_plan/plan_hub.py test` prints a count and green |
| 2 | Set a `goal` and a `project_name` line in the config so 02 §1 and the review's front page read them by code. | 02 §1, 02 §4 Planning | P2 | easy | working | #4 | `amx_plan_config.json`; exit: 02 §1 of the next review shows the goal as 📏 |
| 3 | Decide whether the GitHub link in the résumé header stays or goes; every repository stays private (corrected v0.1.4: the human, "do not make anything public"). | 08 D2, 02 §2 Stage 3 | P1 | easy | human | | a letter on [08](08_DECISIONS.md); exit: the header line matches the decision in the ATS résumé and LinkedIn |
| 4 | Grant the terminal Files and Folders access to Documents/GitHub, then re-read the six unreadable projects in full and update the notes and the outward set. | 01 G2, 04 W5, 06 §3, 08 D3, 14 §4 | P2 | hard | human, then frontier | #5 | System Settings, then a session; exit: 6 new second-pass blocks in the notes, the Verification Note gone |
| 5 | Close the request to re-check the earlier model work, in the human's words, or say what to change after reading the exports. | 01 G5, 08 D4 | P1 | easy | human | | `asks done 1 --said`; exit: Requests: open 0 |
| 6 | Turn the final report's §5 doc edits into requests in each source project (AMTrix Plan glossary, AMTrix Core paths, iPhone v3 README, identity engine template). | the final report §5; 06 §5 | P3 | easy | human, then working | #6 | `asks add` in each source project; exit: one request per project, none in this repo |
| 7 | Rotate the Telegram token and untrack the key files named in the final report §4, as private hygiene; no repository goes public (corrected v0.1.4). | the final report §4; 05 §2; 08 D2 | P1 | easy | human (outside this repo) | #7 | the source projects; exit: the report's §4 rows ticked |
| 8 | Move the export script inside the project as `scripts/export_resume.py`, written through the edit tool, and point `code_dirs` at `scripts/`. | 04 W3, 10 §2, 13 (c) and (d), 15 §2 | P2 | easy | working | #8 | `scripts/export_resume.py`, `amx_plan_config.json`; exit: the exports rebuild from inside the project and 13 (d) measures one file |
| 9 | Ask the standard's source project for a backup-diff check at `check` or `finish` that lists a changed file no backup precedes. | 04 W4, 10 §2, 11 §2, 14 §3 | P3 | hard | frontier (a standard request) | #9 | `asks add` with the words of 11 §2; exit: a `sed` edit shows as a warning in the standard's next version |

## 2. How the working model goes through this
1. `plan_hub.py review-jobs <this folder>` once, when the human says so: every row without a number becomes a request; the number lands in the table.
2. "Next up" on the board sorts them: P1 first, then easy before medium before hard, then the older first. A hard row waits for the frontier model.
3. Three easy rows of one code area go into one iteration; a medium row is one iteration; a hard row goes alone.
4. A plan names its rows on its `**Requests:**` line; a green `finish` ticks them.

## 3. What a script can do with this file (normalised)
- The table's columns are fixed; `review-jobs` reads any `NN_PRIORITIES.md` in any review folder. The 📏 part is the carried rows and the Request column; the 🧠 part is the new rows, the priorities and the sizes, which the reviewer writes and the human edits.
