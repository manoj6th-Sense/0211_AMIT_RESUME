# 05 · Compared with a 20-person company and with what's out there
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `roles and the market` (a company role by role, what a company has that no tool gives, the market with dated sources, what to borrow) · fills from: nothing measured; the reviewer's web scan, every source dated · 📏 = measured by code · 🧠 = the reviewer's judgement. This file is judgement only; its sections are the same in every project.*

> 🎧 **In one breath:** Against a twenty-person company this project has a product owner, a release manager and a librarian by code, a tech lead and a tech writer in the model, and no QA, no security role and no second reviewer. Against the tools of the month it sits in a crowded lane: GitHub's Spec Kit, Claude Code hooks, Codex's AGENTS.md policies and Cursor rules all put a plan or a rule file in front of the model. None of them records the human's yes in the human's words, locks the record at a measured close, or counts whether the model's default matched the human's pick. That is the niche, and it holds here because the standard is installed, not because the portfolio did anything itself. What the portfolio should borrow is small: a test the project owns, the way every one of those tools assumes one.

**The numbers:** none are measured here; a count in this file names the source it came from and its date.

## 1. A 20-person software company, role by role
| Role | What it does in a company | Who or what does it here | Score 🧠 | Gap |
|---|---|---|---|---|
| Product owner | decides what is built and in what order | the human, by words; `asks add` and `approve --said` keep them | ✅ | none: one request, one yes, both on record |
| Tech lead | shapes the work, names the risks | the model, in the plan's §2, §8 and §9 | 🟢 | the plan is read by nobody but the human; a second model never checks it ([04](04_SENIOR_REVIEW.md) W7) |
| Reviewer of every change | reads each diff before it lands | the hook's backup and the stamp; no reader | 🟡 | a diff is kept, never reviewed; the human's read-through of the exports is the only review ([08](08_DECISIONS.md) D) |
| QA | runs the tests, refuses a red build | `finish` runs three acceptance greps; no suite | 🔴 | no `tests/` ([16](16_PRIORITIES.md) row 1) |
| Release manager | cuts a version, writes the notes | `finish`, `bump`, the Walkthrough, the EVOLUTION line | ✅ | no git, so a release has no commit ([04](04_SENIOR_REVIEW.md) W2) |
| Librarian | keeps the source of truth findable | the notes file, the audit file, the board's file index | ✅ | none; the notes are the single source and say so |
| Scrum master | keeps the loop moving, logs the blockers | the state line, the footer, the friction log | ✅ | none; friction has every refusal and both slips |
| Support | answers "where is it, how do I open it" | the Walkthrough's Try it yourself; the listen-along page | 🟢 | the export script is outside the project ([04](04_SENIOR_REVIEW.md) W3) |
| Security | keeps secrets out of the outward set | the model's reading, the notes' never-quote lines | 🟡 | no grep for the token, the topic names or the profile words ([15](15_AUTOMATION_CANDIDATES.md) row 3) |
| Tech writer | writes what a stranger reads | the model: the résumé, the kit, the dossier | 🟢 | typed numbers unchecked ([04](04_SENIOR_REVIEW.md) W6) |
| Internal auditor | checks the process itself | `audit` (19 rows), this folder | 🟢 | the reviewer is the worker ([04](04_SENIOR_REVIEW.md) W7) |
| Analytics | counts what happened | the board's cells, `learned`, the friction pie | ✅ | none the project needs |

Score (🧠): ✅ 5 · 🟢 4 · 🟡 2 · 🔴 1 of 12

## 2. What a company has that no tool gives you
- **A second pair of eyes that did not write the text.** A company has a reviewer who was not the author; here the closest thing is the audit file, where this model listed the earlier model's defects, and the human's read-through of the exports.
- **A recruiter in the room.** A company tests its pitch on the people who hire; here the closest thing is the kit's phrasing rules and the two-page check by pypdf, neither of which is a reader's reaction.
- **Access that is already granted.** A company's engineer can open every repository; here six folders refused to open and the gap went into a note instead of a ticket someone else resolves.
- **A security owner.** A company has one person who rotates a leaked token the day it is found; here the final report lists the leaks and waits for the human's hands.

## 3. The market (scan dated; newest source named)
*Scan of 2026-10-25, four searches; the newest dated source is September 2026.*

| Tool or standard | What it is | The yes as code | Tests measured by the tool | A locked record | A scheduled review | The phone | Overlap with this project |
|---|---|---|---|---|---|---|---|
| **This project** (AMTrix Plan installed, rules since 0.44.0) | a plan-approve-build-finish loop with hooks, a record and a board | ✅ `approve --said` | ✅ `finish` runs the suites and the acceptance list (no suite here yet) | ✅ locked at finish | ✅ `review_every` 3 versions | ✅ the comment page over Tailscale | the subject of this review |
| **GitHub Spec Kit** (announced 2025-09-02; v1.0.6, September 2026) | spec-driven development: Specify, Plan, Tasks, Implement as slash commands and templates | ❌ the human edits the spec; no recorded yes | ❌ tasks say "write tests"; nothing measures them | partly: the spec and plan are files in git | ❌ | ❌ | the same four stages as the plan's sections; no gate between them |
| **Claude Code hooks** (official reference, 2026) | shell commands on PreToolUse, PostToolUse, Stop, SessionStart, PermissionRequest and more | partly: a PreToolUse hook can refuse, but what it checks is the project's own code | ❌ | ❌ | ❌ | ❌ | this project's hooks are built on exactly these events |
| **OpenAI Codex AGENTS.md and `requirements.toml`** (managed policies, 2026) | a rules file per repository plus admin-managed policies the agent cannot override | partly: the policy is code, but it is a ceiling, not a per-step yes | ❌ | ❌ | ❌ | ❌ | the CLAUDE.md role; the policy file is the nearest thing to "edits refused before approval" |
| **Cursor rules** (`.cursor/rules`, 2025 to 2026) | project and user rules injected into the model's context | ❌ | ❌ | ❌ | ❌ | ❌ | the prose half of this project's discipline, with nothing holding it |
| **Spec-driven alternatives** (Kiro, OpenSpec, BMAD-METHOD, Task Master, Tessl, SpecStory; 2025 to 2026) | spec and task files that drive agents, some with their own CLIs | ❌ (Kiro: a task checkbox) | ❌ | partly: files in git | ❌ | ❌ | the task list; none records who said yes to what |

The read (🧠):
1. Every tool of the month puts a document in front of the model; none of them measures the close. "Implement" in Spec Kit ends when the model says it ended.
2. The rule files are read inconsistently: an arXiv study, cited second-hand in one blog during the scan, found agents opened the policy file in about 3.5 % of episodes (corrected v0.1.4: the blog was not identified in the scan's notes, so the figure is unverified and not tied to any source below). A hook that refuses is the only thing that does not depend on the model reading.
3. Codex's managed policies are the closest to a gate, but they are an administrator's ceiling, not the human's per-iteration yes in the human's words.
4. The niche is the recorded yes, the measured finish and the counted pick. For this portfolio the niche costs nothing extra; what it lacks is the one thing all the others assume: a test to run.

## 4. What to borrow this month
| From | What | Where it lands | Size |
|---|---|---|---|
| Spec Kit's Tasks stage | a task list where every outward file names the notes line it was built from, so a re-read can tick each one | a "Sources" footer per section of the kit and the dossier; checked by the test of [16](16_PRIORITIES.md) row 1 | medium |
| Codex managed policies | a policy that cannot be edited by the model: the banned-phrase list as a file the test reads, outside the outward set | `tests/banned_phrases.txt` read by `tests/check_outward.sh` | easy |
| Claude Code hooks reference | a PostToolUse hook that runs the outward-file check on every edit to `FINAL_RESUMES/`, not only at finish | a line in `.claude/settings.json` after the test exists (the human's yes; the settings file is guarded) | easy |

## Sources
- **Spec Kit:** official reference [github.github.com/spec-kit](https://github.github.com/spec-kit/) (2026); third-party: [Visual Studio Magazine, "GitHub Spec Kit"](https://visualstudiomagazine.com/) (2025-09-03 and 2026-05-12), [ssojet.com](https://ssojet.com/) (2026), [smartscope.blog](https://smartscope.blog/) (2026), [morphllm.com](https://morphllm.com/) (2026).
- *Corrected v0.1.4: every link in this list is the site's root, not the article read; the article addresses were not kept from the scan, so each line names where to look, not the page.*
- **Spec-driven alternatives (Kiro, OpenSpec, BMAD-METHOD, Task Master, Tessl, SpecStory):** third-party: [intuitionlabs.ai](https://intuitionlabs.ai/) (2026); [getmaxim.ai](https://getmaxim.ai/) (2026); [radar.firstaimovers.com](https://radar.firstaimovers.com/) (2026).
- **Claude Code hooks:** official reference [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) (2026).
- **OpenAI Codex AGENTS.md and managed policies:** third-party: [codex.danielvaughan.com](https://codex.danielvaughan.com/) (2026-08-06); the official Codex documentation was not fetched in this scan.
- **Cursor rules:** general knowledge of the `.cursor/rules` format (2025 to 2026); no source fetched in this scan, so the row carries no version.
