# 09 · The tools you cannot miss: what you say → what happens
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `every verb for the human` (the verbs from the hub's menu; which the human types, which the model runs; five words that are enough) · fills from: the hub's menu · 📏 = measured by code · 🧠 = the reviewer's judgement. Only the list is this project's; the sections are the same in every project.*

> 🎧 **In one breath:** This project has no commands of its own yet, so the five tools are the hub's. The map, `amx`, shows where the record stands and what to type. A letter on a card, or "defaults", answers every question the model builds. Your own words, logged by `asks add` and `approve --said`, are the only record of what you wanted and what you allowed. `check` is the word for "is anything wrong", and once a `tests/` folder exists, `test` is the word for "prove it".

📏 This file is about the tools of this project first: its own commands are in the table right below; the hub's verbs under them are the standard's, the same in every project.

📏 none found: this project has no npm script, make target, shell script at its root or test suite the file index knows

**The numbers:** the verb list is the hub's menu at 2026-10-25 14:39; the right column, the hooks table and the five words are the reviewer's.

**Legend:** **you** = you type or say it · model = the model runs it for you · the hook = it runs by itself.

## 1. Every verb (📏 the hub's menu; 🧠 the right column)
| Verb | What you say → what happens 🧠 |
|---|---|
| `plan_hub.py amx` | **you** type `amx_plan` → the map: where the record stands, what you can say, what runs by itself |
| `plan_hub.py resume` | the hook, at session start → the Resume block the model states to you in five lines |
| `plan_hub.py new` | model, when you say what you want → the next iteration's four files, the plan skeleton |
| `plan_hub.py approve` | model, after **you** say yes → your words recorded; edits allowed from here |
| `plan_hub.py tested` | model, after **you** say "I tested it" → your words recorded as the manual test |
| `plan_hub.py finish` | model, or **you** type `finish` → the suites and acceptance commands run, the record locks, the board rebuilds |
| `plan_hub.py next` | model, when a seen plan must change → the revision opens as the next iteration; the seen one stays |
| `plan_hub.py comments` | model, after **you** comment on the page → your threads read and answered |
| `plan_hub.py review` | model → a Markdown file shown to you as cards to comment on (corrected v0.1.4: it is not a diff review) |
| `plan_hub.py serve` | the model once → the comment page on your phone, over Tailscale |
| `plan_hub.py link` | model, in every reply → a tappable link for each file named |
| `plan_hub.py asks` | **you** type `requests` → your requests by their words; the model adds, opens, closes them |
| `plan_hub.py answers` | model → your letters from the page, read back into the record |
| `plan_hub.py intake` | model, when **you** say something new → the dot: your words, the reading, the default |
| `plan_hub.py restate` | model → the diagnostics page and its link, when you ask "where are we" |
| `plan_hub.py learned` | the refresh → the make-or-break lines on the board |
| `plan_hub.py compare` | model → two iterations side by side |
| `plan_hub.py check` | model, or **you** type `audit` → the gate: holes, stale docs, mismatches, warnings |
| `plan_hub.py selftest` | model → the standard's own tests, when the hub itself seems wrong |
| `plan_hub.py refresh` | the hooks → every board page rebuilt |
| `plan_hub.py bump` | model, on **your** yes → the version closes with its docs current; the next opens |
| `plan_hub.py ok` | the hook → the one light and its reasons |
| `plan_hub.py brief` | model → the listen-along brief after a finish |
| `plan_hub.py friction` | model, or **you** say what hurt → one line in the log with its kind |
| `plan_hub.py card` | model → one iteration as a card for the page |
| `plan_hub.py launch` | **you** → start Claude Code in this project with a preset from the launch page (corrected v0.1.4: it does not start the page) |
| `plan_hub.py review-folder` | model, when **you** type `reviewer` → this folder, the measured sections by code |
| `plan_hub.py module` | model → one module's digest for a drill (not used here: no code) |
| `plan_hub.py diagrams` | the refresh → the pictures of 13 |
| `plan_hub.py audit` | **you** type `audit` → the 19 wiring checks of 17 |
| `plan_hub.py archive` | model, on **your** yes → old board files moved to the archive |
| `plan_hub.py backups` | model → the hook's backups listed; a diff of one against the file |

## 2. What runs by itself
| When | What runs | What you see |
|---|---|---|
| A session opens | SessionStart → `resume` | the Resume block, stated to you in five lines |
| A message is sent | UserPromptSubmit → `prompt` | the state line: iteration, phase, one next step, open comments, requests logged since your message |
| An edit is about to happen | PreToolUse → `hook` | nothing when allowed (a backup is taken); a refusal line when no iteration is open or the path is outside the project |
| A shell line is about to run | no hook (corrected v0.1.4: the edit hook fires only on Edit, Write, MultiEdit and NotebookEdit) | nothing; only the permission hook answers if a dialog appears, so a `sed` on a project file is never gated, which is why the rule says never |
| A reply ends | Stop → `stop` | nothing when the board and ⏳ Waiting for you are there; the reply comes back once when they are not |
| A task is marked done | TaskCompleted → `task-completed` | the task stays open until `finish` has closed the iteration (corrected v0.1.4) |
| A permission under a standing yes | PermissionRequest → `permission` | the call allowed by code under your standing yes; refused and logged outside it |
| An edit landed | PostToolUse → `stamp` | the `🕒 Last changed` line at the top of the file |
| A commit | pre-commit (git) | not here: no git in this project |
| Other agents | the Codex and Antigravity adapters in the standard | the same verbs from another tool; not used in this project today |

## 3. Five words that are enough
| Word | What it does |
|---|---|
| **amx_plan** | the map: where the record is and what you can type next |
| **a letter, or "yes"** | answers a card; a bare yes takes every ★ |
| **your own words** | "do this", "that is wrong", "done": logged as a request, a friction line or a close, never paraphrased |
| **audit** | is anything wrong with the wiring or the record; the 19 checks and the gate |
| **finish** | close the open step: code measures, locks, shows the board (here, with no git, it also stands in for commit) |
