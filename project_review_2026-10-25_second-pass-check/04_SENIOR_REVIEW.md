# 04 · Senior architect review: what's good, what needs work
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `strengths, problems, hygiene` (what to protect, what to fix ranked by damage, the layers, hygiene scored, the CTO's three) · fills from: git, the tests, the scripts folder · 📏 = measured by code · 🧠 = the reviewer's judgement. Only the numbers are this project's; the sections are the same in every project.*

> 🎧 **In one breath:** The design is a three-layer document pipeline: a notes file of verified facts, an audit of what the earlier pass got wrong, and an outward set rebuilt only from the first two. The idea it carries is the human's own: nothing outward without a measured or read source, and every correction on record. What needs work is proof and persistence: no test suite, no git, and two edits that went around the hook. A CTO would add the small test, initialise git, and make the export a project script before touching any more prose. It is ready to be used as a résumé today; it is not yet ready to be trusted by code.

**The numbers:** the hygiene table's evidence is measured at 2026-10-25 14:39; the grades, the strengths and the problems are the reviewer's, each with the number that shows it.

## 1. 👍 Strong: keep and protect these
| # | Strength | Evidence 📏 | What would break it |
|---|---|---|---|
| K1 | **One source of truth for facts.** Every outward line traces to a dated second-pass block in the notes, with "not read" lines where it does not. | 3 second-pass blocks; 15 audit rows closed | a future edit to the résumé made without a notes line first |
| K2 | **Honest scoping on record.** Six unverified projects are named in the dossier and the kit instead of being written up from memory. | the dossier's Verification Note; the kit §5 | a pass that quietly drops the note without re-reading |
| K3 | **The privacy rules are written down.** Operator profile, trigger words, health and family details, tokens and topic names are listed as never-quote items in the notes. | the notes' privacy lines per section; the kit §4 | a model that reads the outward files but not the notes |
| K4 | **Phrasing rules as a checklist.** "AMTrix" not "AMX", no n8n, no "prompt engineering", softened claims, each with the honest alternative. | kit §4; 1 acceptance grep ("AMX Plan") | the checklist staying prose (W1 turns it into a test) |
| K5 | **The record held the model switch.** Opus to Fable mid-day and a context compaction cost no re-explaining because the plan, Task and notes carried the state. | 2 iterations, 0 revised; the Resume block | a session that edits before `new`, which the hook already refuses |
| K6 | **Exports a recruiter can open.** Two-page PDF, DOCX and a ten-page dossier PDF, rendered from the Markdown, so the Markdown stays the source. | `FINAL_RESUMES/exports/` 5 files | the export script living outside the project (W3) |

## 2. 👎 Needs work, ranked by damage
| # | Problem | The number 📏 | What it costs | Fix | Who |
|---|---|---|---|---|---|
| W1 | **No test suite, so no green close.** The project's own rules (banned phrases, no Mermaid in the dossier, LinkedIn limits, exports present) are checked by the model's eyes. | Tests: count not reported; 0 green of 1 | every finish partial; a phrasing regression unseen | one shell script under `tests/` plus a `test_suites` entry | working · medium |
| W2 | **No git.** The loop ends in "commit locally" and here it cannot; finish skips the backup gate. | Commits: nothing measured; `WARN NO_GIT` | no history of the outward set; a bad edit has only the hook's backups | `git init` with a `.gitignore` for the board and exports' HTML, on the human's yes | human · easy |
| W3 | **The export script lives in the session scratchpad.** It is not in the project, so the next session rebuilds it. | 1 heredoc write to the scratchpad after the hook refused that path as outside the project (corrected v0.1.4: no in-project path was ever tried) | one round per session to re-create it | add `scripts/export_resume.py` inside the project through the edit tool | working · easy |
| W4 | **Two shell edits went around the hook.** `sed` on the notes left no backup and no stamp. | 2 "my slip" friction lines | trust: the record cannot show those two changes | the playbook rule plus W1's test comparing stamps to changes | working · easy |
| W5 | **Six projects second-hand.** The dossier names them honestly, but the résumé still lists PromptForge, SmartBrain and AMTrix Studio from earlier write-ups. | 6 of 21 sections | a recruiter question the human cannot answer from the notes | a permission grant, then a re-read session | human then frontier · hard |
| W6 | **Typed numbers in outward files.** "700+ tests", "27 skills", "~9.8M observations" are typed by the model, not written by code. | the ATS résumé carries several dozen numeric tokens besides the years (corrected v0.1.4: "about a dozen" was an undercount; a grep shows it) | drift when a project changes | W1's test can pin each number to a notes line; beyond that it is a judgement | working · easy |
| W7 | **The reviewer is the worker.** This review was written by the same model that did the work, in the same session. | 1 review folder, 1 model | blind spots stay blind | the next review folder by a different model | frontier · medium |

## 3. Architecture in layers (today)
📏 nothing measured: no code folder found; set code_dirs in amx_plan_config.json

| Layer | Scripts | State |
|---|---|---|
| The human's words | the chat; `asks add`, `approve --said`, `ask --read` | 🟢 |
| The tool's hooks | `.claude/settings.json`: `resume`, `prompt`, `hook`, `stamp`, `stop`, `permission`, `task-completed` | 🟢 |
| The standard's code | `amx_impl_plan/plan_hub.py` and its scripts (never edited here) | 🟢 |
| The project's facts | `DATA_REFERENCES/DEEP_READ_NOTES_2026-10-25.md`, `AUDIT_OF_PRIOR_WORK_2026-10-25.md`, `PROJECT_EXPERTISE_ANALYSIS_2026-10-25.md` | 🟢 |
| The outward set | `FINAL_RESUMES/` (ATS résumé, LinkedIn, kit, dossier), `INTERVIEW_PREP/` | 🟢 |
| The exports | `FINAL_RESUMES/exports/` from a scratchpad script (headless Chrome, python-docx) | 🟡 |
| The project's own checks | none: no `tests/`, no `scripts/` | 🔴 |

**What to look at:** everything below the facts layer depends on it; the exports depend on a script the project does not own; the checks layer is empty, so nothing above it is measured.

## 4. Engineering hygiene, scored (📏 the evidence; 🧠 the grade)
| Item | Evidence 📏 | Grade 🧠 |
|---|---|---|
| Tests | count not reported in 0 s, green (v0.1.1) | 🔴 D · "green" with no test is a label, not a result |
| Script sizes | nothing measured: no code folder found; set code_dirs in amx_plan_config.json | 🟢 A · nothing to size; `code_dirs` could point at `scripts/` once W3 lands |
| Uncommitted work | nothing measured | 🟡 C · no git, so the question cannot be asked |
| Backups beside files | 0 | 🟢 A · the hook's backups stayed in their folder |
| Stale living docs | 0 | 🟢 A · every stamped doc is current |
| Board size | 1.8 MB | 🟢 A · normal for one version |

## 5. If I were your CTO, the next 3 things I'd insist on
1. **Give the project a test it owns (W1).** One shell script that greps the outward files for the banned phrases, counts Mermaid fences in the dossier, checks the LinkedIn lengths and the presence of the exports; register it in `test_suites`. Until then every close is partial and the phrasing rules are prose. Medium, working model, next iteration.
2. **Initialise git (W2).** The record is designed to be committed and the backup gate at finish needs a HEAD; without it the outward set has no history beyond the hook's backups. Easy, the human's yes, five minutes.
3. **Bring the export script inside (W3) and stop editing from the shell (W4).** Both are the same discipline: the project owns its scripts and every change passes the hook. Easy, working model, bundled with W1's iteration or the one after.
