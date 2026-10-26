# 15 · Automation candidates: what in this folder is a script, and what should become one
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `what code fills and what the reviewer writes` (the seventeen files' split, regenerated from the templates; what this review suggests to automate next; the normalisation checklist) · fills from: the templates themselves · 📏 = measured by code · 🧠 = the reviewer's judgement. The sections are the same in every project.*

> 🎧 **In one breath:** One thing became a script in this project's work: the export of the résumé and the dossier to PDF, DOCX and HTML, and it lives in the wrong place, the session scratchpad. Nothing else is code: the phrasing rules, the page count, the LinkedIn limits and the privacy words are all checked by reading. The next script is the outward test, one shell file that turns those readings into a count finish can record. After it, the export script moves inside and runs from the same test. The banned-phrase list becomes a file the test reads, so the rule and the check are one thing.

📏 This file is about what to automate in this project's own work (its builds, its deploys, its tests in its code); the table in §1 is about the review templates themselves, the same in every project.

**The numbers:** the split table is regenerated from the templates at 2026-10-25 14:39; the candidates are the reviewer's, each with its exit test.

## 1. The seventeen files: what code fills, what the reviewer writes (📏 regenerated from the templates)
| File | Role | 📏 a script fills | 🧠 the reviewer writes | Inputs |
|---|---|---|---|---|
| 00 START_HERE | the five-minute verdict | since_last_review, board, files_table, earlier_reviews | 4 hole(s) | the previous review, the board, git |
| 01 DIAGNOSTICS | where it stands, measured | state_table, light, light_reasons, previous_findings | 5 hole(s) | git, the tests, the record, the board |
| 02 GOAL_SCORECARD | the goal and the distance | slip_catalog, slip_pie, p2, obligations | 6 hole(s) | the friction logs, the rules ledger |
| 03 STRUCTURED_THINKING | prompt rules vs code | about_03, p2_table, p2 | 7 hole(s) | the roadmap's P2 table |
| 04 SENIOR_REVIEW | strengths, problems, hygiene | scripts_summary, hygiene_table | 6 hole(s) | git, the tests, the scripts folder |
| 05 COMPANY_AND_MARKET | roles and the market | nothing | 6 hole(s) | none (a web scan by the reviewer) |
| 06 ROADMAP_CHECK | each phase's status | roadmap_status, exit_tests | 5 hole(s) | the roadmap doc, the board, the record |
| 07 OPERATING_MODEL | how the human runs it | about_07, settings_table, lights_table, numbers_table | 7 hole(s) | the settings, the board |
| 08 DECISIONS | questions pre-ticked | open_requests | 2 hole(s) | the open requests |
| 09 TOOLS_YOU_CANNOT_MISS | every verb for the human | about_09, project_tools, verb_table | 4 hole(s) | the hub's menu |
| 10 YOUR_NOTES_ANALYZED | requests, friction, dots grouped | requests_summary, friction_summary, intake_summary, feedback_lines, clients_pains, open_requests | 6 hole(s) | the requests, the friction logs, the intake |
| 11 STRUGGLES_OF_THE_WORKING_MODEL | the model's slips and their fixes | about_11, struggle_numbers, struggle_pie, struggle_clusters | 5 hole(s) | the friction logs |
| 12 DRILL_VERDICT | what the replica drill is for | about_12, drill_runs, drill_chart, drill_modules, drill_missed, drill_cost | 4 hole(s) | the drill's score files, the record |
| 13 VISUAL_STRUCTURE | the pictures | picture_a, picture_b, picture_c, module_tree, module_tree_mermaid, evolution, evolution_mermaid, picture_f | 7 hole(s) | the scripts folder, the evolution doc |
| 14 EXTERNAL_DEPENDENCIES | what outside the project limits the work | refusal_clusters | 4 hole(s) | the friction logs |
| 15 AUTOMATION_CANDIDATES | what code fills and what the reviewer writes | about_15, automation_table, automation_count | 2 hole(s) | the templates themselves |
| 16 PRIORITIES | every suggestion as a work list | carried_rows | 2 hole(s) | the previous review, the requests |
| 17 INTEGRITY_AUDIT | is the automation itself intact | about_17, audit_table, audit_count, audit_gaps | 3 hole(s) | the audit's rows (the board's AUDIT.md) |

📏 of 18 files, 17 have at least one section code fills; 1 are judgement only. Every file keeps its sections even when a section is empty: it then says "nothing measured" or keeps its hole.

## 2. What this review suggests to automate next
| Candidate | Inputs | What it does | Outputs | When it runs | Exit test |
|---|---|---|---|---|---|
| **The outward test** ([16](16_PRIORITIES.md) row 1) | `FINAL_RESUMES/*.md`, `INTERVIEW_PREP/*.md`, a banned-phrase file | greps the outward files for the banned phrases, counts Mermaid fences in the dossier, checks the LinkedIn headline and About lengths, checks the exports exist | pass or fail per check, a count | `plan_hub.py test` and `finish`; registered in `test_suites` | `python3 amx_impl_plan/plan_hub.py test` prints a count and green |
| **The export script inside the project** ([16](16_PRIORITIES.md) row 8) | the ATS résumé and the dossier Markdown | renders PDF, DOCX and HTML with headless Chrome and python-docx; checks the résumé PDF is two pages | `FINAL_RESUMES/exports/` | by hand after an outward change; later a PostToolUse hook on `FINAL_RESUMES/` | the exports' stamps newer than the Markdown's; the PDF page count printed |
| **The banned-phrase list as a file** ([16](16_PRIORITIES.md) row 1, part) | the kit §4 phrasing rules | one line per phrase with its honest alternative, read by the test and by the model | `tests/banned_phrases.txt` | read at every test run | the test fails when a listed phrase appears in an outward file |
| **The LinkedIn length check** ([16](16_PRIORITIES.md) row 1, part) | `FINAL_RESUMES/LinkedIn_Profile.md` | counts the headline and About characters against the platform's limits | two numbers and a pass or fail | the outward test | the test prints both counts under the limits |
| **The privacy grep** ([16](16_PRIORITIES.md) row 1, part) | the outward files; a never-quote list kept outside the outward set | greps for the token pattern, the topic names and the operator-profile words; the list itself is never printed | pass or fail, no quoted matches | the outward test | a seeded test file with one listed word fails the check |
| **The backup-diff check** ([16](16_PRIORITIES.md) row 9; a standard request, outside this repo) | the hook's backup folder, the project files | lists a changed file that no backup precedes | a warning line at `check` | `check` and `finish` | a `sed` edit of a project file shows up as a warning |

## 3. The normalisation checklist (every script must pass it, as a test)
1. **No project name.** The output never contains the repo's folder name; the project is the config's `goal` or nothing.
2. **No person's name.** The human is the `operator` setting; the model is the plan's Author line.
3. **No path outside the config's dirs.** Every path is built from the config (the record dir, the board dir, the system dir).
4. **Every number from a command.** A number in a 📏 section is computed at write time; a 🧠 section may hold none.
5. **Every section present, even empty.** An empty measured section reads "nothing measured"; an empty judgement hole stays as its marker.
6. **The legend line is the first italic line** of every file, and every judged section has its table header in the template (v0.41.2): the reviewer fills rows, never invents columns.
7. **Dated folder, numbered files, 00 first.** The folder's date comes from the clock, the tag from the argument.
8. **Every picture twice** (v0.41.2): a text drawing for the phone, a Mermaid one with the standard's init line for the page.
