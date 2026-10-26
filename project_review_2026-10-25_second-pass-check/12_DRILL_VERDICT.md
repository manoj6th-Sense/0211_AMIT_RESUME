# 12 · The replica drill: what it did for you, what it cost, and what to keep
**For:** the human · **By:** Claude Fable 5.1 (for Amit Malhotra) · **Date:** 2026-10-25 · **Record:** iteration v0.1.0 · back to [00_START_HERE](00_START_HERE.md)
*Template for any project: `what the replica drill is for` (what it is, what it measured, what it cost, what it gave, the verdict) · fills from: the drill's score files, the record · 📏 = measured by code · 🧠 = the reviewer's judgement. Only the numbers are this project's; the sections are the same in every project.*

> 🎧 **In one breath:** The drill never ran here and should not: there is no module for a fresh model to rebuild from the record. The measurement that stood in is the acceptance list, three commands run by finish, and it did its job twice. What it proved is narrow: one banned phrase absent, two files present. What it did not prove is everything the human cares about, from phrasing to page count to privacy. Judged the same way as a drill, it scores a pass on three rows and leaves the rest unmeasured, which is exactly what the Tests light says.

📏 This project has no drill target, so the drill never ran here: the one measurement that stands in is its test suite, the tests (no count yet at the last finish). Judge that the same way.

**The numbers:** the runs, the averages and the cost are read from the score files and the plans at 2026-10-25 14:39; the verdict is the reviewer's.

## 1. What it is, plainly
A fresh model rebuilds one module from the record alone, and a score table says, row by row, what it matched (✅) and what it missed (❌). The share is on the board; the goal and the floor are settings.

## 2. What it measured (📏 the score files)
not applicable: no drill target configured (drill_target in amx_plan_config.json)

not applicable: no drill target configured (drill_target in amx_plan_config.json)

📏 Average per module: not applicable: no drill target configured (drill_target in amx_plan_config.json)
📏 Rows missed by every run of the newest module: not applicable: no drill target configured (drill_target in amx_plan_config.json)

## 3. What it cost (📏 the record)
not applicable: no drill target configured (drill_target in amx_plan_config.json)

## 4. What it gave that stays useful
| What the drill forced | Still in the code | Who reads it today |
|---|---|---|
| *(no drill here)* the acceptance list forced the plan to name a check before any edit | the plan's §7 between the acceptance markers; `finish` runs it | `finish`, the human at approval |
| the "not measured" warning forced the gap into the record instead of silence | the friction log, kind "not measured"; the board's Tests cell | the footer, this review, the next model |
| the Verification Note forced the second-hand facts to say so | `FINAL_RESUMES/AMIT_MALHOTRA_FDE_PROFILE_2026.md`, before Appendix A | the recruiter, the human, the next re-read session |

## 5. Did it improve tests or error detection?
**No, not yet.** Directly, the stand-in measurement is three acceptance commands, run at two finishes, both passing; there were no tests before and there are none now, so the count went from nothing to nothing. Indirectly, yes in a small way: the "not measured" line at the first finish is what put the test suite at the top of this review's priorities. (Corrected v0.1.4: an earlier sentence here said the acceptance list caught a banned phrase in a draft; the record shows every acceptance command passed at its first run, so it caught nothing.) The newest iteration with a measured run is v0.1.1, and it reads "count not reported".

## 6. The verdict
| Keep | Change | Stop |
|---|---|---|
| the acceptance list in every plan, with a banned-phrase grep | the three greps become one suite the project owns ([16](16_PRIORITIES.md) row 1) | the "not measured" warning repeating at every close without a row to fix it |
| "never run" for the drill, on purpose | nothing: no module exists to drill | thinking of the drill as a gap here; it is not applicable |

**The one rule:** a finish that measures nothing of the project is a partial close, and the project owes itself a test before the next one.

## 7. What a script can do with this file (normalised)
- §2 and §3 are reads over the score files, the plans and git: `plan_hub.py review-folder` fills them in any project that has run the drill.
- §1 and §7 are generic; §4, §5 and §6 are the reviewer's.
