# Implementation Plan: Project Reorganization & Document Standardization

**Document Version:** v1.0  
**Last Modified:** 2026-10-26 23:58 UTC+4  
**Status:** In Review  
**Skills Applied:** `002_ORGANIZE_FOLDER`, `003_ORGANIZE_PROJECT`, `document_versioning.md`

---

## 1. Executive Summary

This plan restructures `0211_AMIT_RESUME` (`amit-malhotra1/resume-project`) into a fully standardized, numbered, and timestamped taxonomy adhering to:
1. **Folder Standards**: 3-digit zero-padded prefixes (`000_`, `001_`, `002_`...) with `UPPER_SNAKE_CASE` naming.
2. **File Standards**: Sequential 3-digit prefixes (`001_`, `002_`...) within folders, clean lowercase extensions, and elimination of spaces or unescaped characters.
3. **Mandatory Project History**: Formal integration of `000_PROJECT_HISTORY/` (Plans, Walkthroughs, Tasks, Sessions, Recaps/Audits).
4. **Document Versioning & Timestamping**: Standardized YAML/Markdown metadata headers and revision blocks across all documents.
5. **Git History & Tooling Compatibility**: Git moves (`git mv`) to preserve commit blame, along with updates to `.gitignore`, export scripts, and test suites.

---

## 2. Target Directory Hierarchy

```
0211_AMIT_RESUME/
├── 000_PROJECT_HISTORY/
│   ├── 001_IMPLEMENTATION_PLANS/
│   │   └── 001_PROJECT_REORGANIZATION_PLAN.md
│   ├── 002_WALKTHROUGHS/
│   ├── 003_TASKS_AND_CHECKPOINTS/
│   ├── 004_SESSIONS/
│   └── 005_RECAPS_AND_AUDITS/
│
├── 001_FINAL_RESUMES/
│   ├── 001_AMIT_MALHOTRA_FDE_PROFILE_2026.md
│   ├── 002_AMIT_MALHOTRA_FDE_RESUME_2026_ATS.md
│   ├── 003_APPLICATION_KIT_2026.md
│   ├── 004_LINKEDIN_PROFILE.md
│   ├── 005_RESUME_BUSINESS_ANALYST_PM.md
│   ├── 006_RESUME_COMPLETE_TECHNO_FUNCTIONAL.md
│   └── 007_EXPORTS/
│       ├── 001_AMIT_MALHOTRA_FDE_PROFILE_2026.html
│       ├── 002_AMIT_MALHOTRA_FDE_PROFILE_2026.pdf
│       ├── 003_AMIT_MALHOTRA_FDE_RESUME_2026.docx
│       ├── 004_AMIT_MALHOTRA_FDE_RESUME_2026.html
│       └── 005_AMIT_MALHOTRA_FDE_RESUME_2026.pdf
│
├── 002_STRATEGIC_PITCH/
│   ├── 001_AMTRIX_STRATEGIC_PITCH.md
│   ├── 002_THE_EXECUTION_MANDATE.md
│   └── 003_VALUE_PROPOSITION_PITCH_DECK.md
│
├── 003_INTERVIEW_PREP/
│   ├── 001_COMPETITIVE_EDGE_ANALYSIS.md
│   ├── 002_HONEST_ASSESSMENT_SUMMARY.md
│   ├── 003_INTERVIEW_QUESTIONS.md
│   ├── 004_PORTFOLIO_ANALYSIS_AND_GAP_STRATEGY.md
│   ├── 005_QUICK_REFERENCE_CARD.md
│   └── 006_RESUME_FULL_DETAIL_PERSONAL.md
│
├── 004_DATA_REFERENCES/
│   ├── 001_AUDIT_OF_PRIOR_WORK_2026-10-25.md
│   ├── 002_DEEP_READ_NOTES_2026-10-25.md
│   ├── 003_OLLAMA_POWERHOUSE_ANALYSIS.md
│   ├── 004_PROJECT_EXPERTISE_ANALYSIS_2026-10-25.md
│   ├── 005_PROMPTFORGE_ANALYSIS.md
│   ├── 006_SMARTBRAIN_ANALYSIS.md
│   ├── 007_SOURCE_AUDIT_2026-10-25.md
│   └── 008_OLD_RESUMES/
│       ├── 001_AMIT_MALHOTRA_AA.docx
│       ├── 002_AMIT_MALHOTRA_LATEST.docx
│       ├── 003_AMIT_MALHOTRA_LATEST_TL.docx
│       └── 004_PDF_FULL_SIZE_AMIT_MALHOTRA.pdf
│
├── 005_SCRIPTS/
│   ├── 001_export_resume.py
│   └── 002_preview_share.sh
│
├── 006_TESTS/
│   ├── 001_banned_phrases.txt
│   └── 002_check_outward.sh
│
├── .gitignore
├── README.md
└── PROJECT_INDEX.md
```

---

## 3. Comprehensive Migration Map

| Current Path | Proposed Path | Action Type |
|---|---|---|
| *(New Directory)* | `000_PROJECT_HISTORY/` | Create standard history structure |
| `FINAL_RESUMES/` | `001_FINAL_RESUMES/` | `git mv` folder & rename files |
| `FINAL_RESUMES/AMIT_MALHOTRA_FDE_PROFILE_2026.md` | `001_FINAL_RESUMES/001_AMIT_MALHOTRA_FDE_PROFILE_2026.md` | `git mv` & add timestamp header |
| `FINAL_RESUMES/AMIT_MALHOTRA_FDE_RESUME_2026_ATS.md` | `001_FINAL_RESUMES/002_AMIT_MALHOTRA_FDE_RESUME_2026_ATS.md` | `git mv` & add timestamp header |
| `FINAL_RESUMES/APPLICATION_KIT_2026.md` | `001_FINAL_RESUMES/003_APPLICATION_KIT_2026.md` | `git mv` & add timestamp header |
| `FINAL_RESUMES/LinkedIn_Profile.md` | `001_FINAL_RESUMES/004_LINKEDIN_PROFILE.md` | `git mv` & add timestamp header |
| `FINAL_RESUMES/Resume_BusinessAnalyst_PM.md` | `001_FINAL_RESUMES/005_RESUME_BUSINESS_ANALYST_PM.md` | `git mv` & add timestamp header |
| `FINAL_RESUMES/Resume_Complete_TechnoFunctional.md` | `001_FINAL_RESUMES/006_RESUME_COMPLETE_TECHNO_FUNCTIONAL.md` | `git mv` & add timestamp header |
| `FINAL_RESUMES/exports/` | `001_FINAL_RESUMES/007_EXPORTS/` | `git mv` & rename export binaries |
| `STRATEGIC_PITCH/` | `002_STRATEGIC_PITCH/` | `git mv` folder & rename files |
| `STRATEGIC_PITCH/AMTRIX_STRATEGIC_PITCH.md` | `002_STRATEGIC_PITCH/001_AMTRIX_STRATEGIC_PITCH.md` | `git mv` & add timestamp header |
| `STRATEGIC_PITCH/THE_EXECUTION_MANDATE.md` | `002_STRATEGIC_PITCH/002_THE_EXECUTION_MANDATE.md` | `git mv` & add timestamp header |
| `STRATEGIC_PITCH/VALUE_PROPOSITION_PITCH_DECK.md` | `002_STRATEGIC_PITCH/003_VALUE_PROPOSITION_PITCH_DECK.md` | `git mv` & add timestamp header |
| `INTERVIEW_PREP/` | `003_INTERVIEW_PREP/` | `git mv` folder & rename files |
| `INTERVIEW_PREP/Competitive_Edge_Analysis.md` | `003_INTERVIEW_PREP/001_COMPETITIVE_EDGE_ANALYSIS.md` | `git mv` & add timestamp header |
| `INTERVIEW_PREP/Honest_Assessment_Summary.md` | `003_INTERVIEW_PREP/002_HONEST_ASSESSMENT_SUMMARY.md` | `git mv` & add timestamp header |
| `INTERVIEW_PREP/Interview_Questions.md` | `003_INTERVIEW_PREP/003_INTERVIEW_QUESTIONS.md` | `git mv` & add timestamp header |
| `INTERVIEW_PREP/Portfolio_Analysis_and_Gap_Strategy.md` | `003_INTERVIEW_PREP/004_PORTFOLIO_ANALYSIS_AND_GAP_STRATEGY.md` | `git mv` & add timestamp header |
| `INTERVIEW_PREP/Quick_Reference_Card.md` | `003_INTERVIEW_PREP/005_QUICK_REFERENCE_CARD.md` | `git mv` & add timestamp header |
| `INTERVIEW_PREP/Resume_FullDetail_PERSONAL.md` | `003_INTERVIEW_PREP/006_RESUME_FULL_DETAIL_PERSONAL.md` | `git mv` & add timestamp header |
| `DATA_REFERENCES/` | `004_DATA_REFERENCES/` | `git mv` folder & rename files |
| `DATA_REFERENCES/AUDIT_OF_PRIOR_WORK_2026-10-25.md` | `004_DATA_REFERENCES/001_AUDIT_OF_PRIOR_WORK_2026-10-25.md` | `git mv` & add timestamp header |
| `DATA_REFERENCES/DEEP_READ_NOTES_2026-10-25.md` | `004_DATA_REFERENCES/002_DEEP_READ_NOTES_2026-10-25.md` | `git mv` & add timestamp header |
| `DATA_REFERENCES/Ollama_Powerhouse_Analysis.md` | `004_DATA_REFERENCES/003_OLLAMA_POWERHOUSE_ANALYSIS.md` | `git mv` & add timestamp header |
| `DATA_REFERENCES/PROJECT_EXPERTISE_ANALYSIS_2026-10-25.md` | `004_DATA_REFERENCES/004_PROJECT_EXPERTISE_ANALYSIS_2026-10-25.md` | `git mv` & add timestamp header |
| `DATA_REFERENCES/PromptForge_Analysis.md` | `004_DATA_REFERENCES/005_PROMPTFORGE_ANALYSIS.md` | `git mv` & add timestamp header |
| `DATA_REFERENCES/SmartBrain_Analysis.md` | `004_DATA_REFERENCES/006_SMARTBRAIN_ANALYSIS.md` | `git mv` & add timestamp header |
| `DATA_REFERENCES/SOURCE_AUDIT_2026-10-25.md` | `004_DATA_REFERENCES/007_SOURCE_AUDIT_2026-10-25.md` | `git mv` & add timestamp header |
| `DATA_REFERENCES/OLD_RESUMES/` | `004_DATA_REFERENCES/008_OLD_RESUMES/` | `git mv` folder & rename files |
| `scripts/` | `005_SCRIPTS/` | `git mv` & update internal paths |
| `scripts/export_resume.py` | `005_SCRIPTS/001_export_resume.py` | `git mv` & update defaults |
| `scripts/preview_share.sh` | `005_SCRIPTS/002_preview_share.sh` | `git mv` & update regex whitelist |
| `tests/` | `006_TESTS/` | `git mv` & update test targets |
| `tests/banned_phrases.txt` | `006_TESTS/001_banned_phrases.txt` | `git mv` |
| `tests/check_outward.sh` | `006_TESTS/002_check_outward.sh` | `git mv` & update paths to 001_/003_ |

---

## 4. Document Versioning & Header Metadata Standard

Every markdown document in `001_FINAL_RESUMES`, `002_STRATEGIC_PITCH`, `003_INTERVIEW_PREP`, and `004_DATA_REFERENCES` will receive a standardized metadata block at line 2:

```markdown
> **Document Version:** v1.0  
> **Last Modified:** 2026-10-26 23:55 UTC+4  
> **Status:** [Baseline | Approved]  
```

---

## 5. Tooling, CI & Integrity Verification

1. **`.gitignore` Update**: Update root allow-list:
   ```gitignore
   !/000_PROJECT_HISTORY/
   !/001_FINAL_RESUMES/
   !/002_STRATEGIC_PITCH/
   !/003_INTERVIEW_PREP/
   !/004_DATA_REFERENCES/
   !/005_SCRIPTS/
   !/006_TESTS/
   ```
2. **`check_outward.sh` Update**:
   Update target definitions:
   ```bash
   OUTWARD="001_FINAL_RESUMES/*.md 003_INTERVIEW_PREP/*.md"
   DOSSIER="001_FINAL_RESUMES/001_AMIT_MALHOTRA_FDE_PROFILE_2026.md"
   RESUME="001_FINAL_RESUMES/002_AMIT_MALHOTRA_FDE_RESUME_2026_ATS.md"
   LINKEDIN="001_FINAL_RESUMES/004_LINKEDIN_PROFILE.md"
   EXPORTS="001_FINAL_RESUMES/007_EXPORTS"
   BANNED="006_TESTS/001_banned_phrases.txt"
   ```
3. **Execution Verification**:
   Execute the test suite `bash 006_TESTS/002_check_outward.sh` to ensure 100% of checks pass cleanly after migration.
