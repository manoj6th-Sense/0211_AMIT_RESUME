# 14 · Outside the project: what limits the work from beyond the repo, and the plan for it
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `what outside the project limits the work` (the refusals counted by pattern, what the project covers by itself, what does not exist on this side, the boundary) · fills from: the friction logs · 📏 = measured by code · 🧠 = the reviewer's judgement. Only the numbers are this project's; the sections are the same in every project.*

> 🎧 **In one breath:** No guard refusal was logged in this project, so the outside tool's own guards never stopped the work. What limited it came from the operating system: macOS refused six project folders under Documents/GitHub with a permission error, and a third of the facts stayed second-hand. The project covers its own gates through the standard's hooks: edits before approval, writes outside the project, a reply without its board. What only the outside tool gives is the permission dialog itself and the sandbox around the shell. The plan is one dialog by the human, then a re-read session; the folder access stays outside the repo for good, as it should.

**The numbers:** the refusal clusters are the "guard refusal" lines at 2026-10-25 14:39; the tables below are the reviewer's, each row naming its code.

## 1. The facts from this side (📏 the "guard refusal" lines, clustered)
nothing measured

## 2. What the project covers by itself
| Protection | Where it lives | Since |
|---|---|---|
| an edit with no open approved iteration | the PreToolUse hook, `plan_hub.py hook` (`NO_OPEN_ITERATION`) | the install, rules since 0.44.0 |
| a write outside the project root | the PreToolUse hook, `plan_hub.py hook` (`OUTSIDE_PROJECT`) | the install |
| an edit to a recorded file, a backup or the archive | the PreToolUse hook; its names in `hub_gate.py` are `IMMUTABLE_CHANGED`, `BACKUP_PROTECTED` and `ARCHIVE_PROTECTED` (corrected v0.1.4: `RECORDED` does not exist) | the install |
| an edit to the standard's folder | the PreToolUse hook (the system folder rule; corrected v0.1.4: `SYSTEM_DIR` is a path setting, not a refusal code) | the install |
| a commit that stages a secret | the pre-commit gate, `SECRET_STAGED` in `hub_gate.py` | the install; not active here, since there is no git |
| a reply without the board and ⏳ Waiting for you | the Stop hook, `plan_hub.py stop` | the install |
| a finish with a failing acceptance command or a red test | `plan_hub.py finish` (`FINISH_REFUSED`) | the install |
| a review folder with a bad tag | `plan_hub.py review-folder` (`REVIEW_FOLDER_BAD_TAG`) | the install; met once this session |
| a commit with a stale record | the pre-commit gate | not applicable: no git here |

## 3. What does not exist on this side yet
| Only the outside tool gives it today | Could move into the project | How |
|---|---|---|
| the folder permission dialog (macOS Files and Folders) | no | it is the operating system's; the project can only name the six folders it could not read, which the dossier does |
| the sandbox around the shell | no | the tool's; the project's hook gates what it can see and `check` after a shell edit covers the rest |
| a read guard on dot-env files and settings | partly | the playbook's guard refuses the reads today; a project-level list of never-read paths could join the outward test ([16](16_PRIORITIES.md) row 1) |
| a diff of the hook's backups against the files | yes, as a standard request | `check` or `finish` compares each backup with its file and lists a change no backup precedes ([16](16_PRIORITIES.md) row 9) |

🧠 What the outside tool does that nobody asked for: it summarises the conversation when the context fills, and the summary, not the record, is then what the model remembers; this session's summary was right, but the record is what should be trusted when they differ.

## 4. The boundary, and the plan
- **What this project may say about the outside dependency:** "six folders were unreadable from this session" and nothing more; the dossier's Verification Note says it in those words and names no cause the project cannot see.
- **The plan to need it less:** 1. the human grants Files and Folders access once ([08](08_DECISIONS.md) C); 2. a session re-reads the six and writes their second-pass blocks ([16](16_PRIORITIES.md) row 4); 3. the outward set is updated and the Note shrinks; 4. the export script moves inside so no scratchpad write is needed again ([16](16_PRIORITIES.md) row 8).
- **What stays outside for good:** the operating system's permissions, the tool's sandbox and its context summaries, and the source projects' secrets, which this repo lists but never touches.
