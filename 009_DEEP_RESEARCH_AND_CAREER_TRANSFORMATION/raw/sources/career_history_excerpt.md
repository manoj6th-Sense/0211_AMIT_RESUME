# AMIT MALHOTRA — Full Detail Resume
> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 00:00 UTC+4  
> **Status:** Baseline

> **📌 Snapshot: January 2026 (instruction-design era). Kept for history; do not send.**
> Current positioning (Oct 2026): *Forward Deployed AI Engineer*. See `FINAL_RESUMES/AMIT_MALHOTRA_FDE_PROFILE_2026.md` and `DATA_REFERENCES/PROJECT_EXPERTISE_ANALYSIS_2026-10-25.md`.
**For Personal Reference Only — Contains Deep Technical Context**

---

## LINKEDIN HEADER
**AI Systems Architect & Product Leader | Human-Centric AI & Prompt Architecture | Ex-Moody's | 21+ Years in Enterprise Technology & Credit Risk Platforms and Analytics**

---

## CAREER TIMELINE

| Period | Role | Company | Key Focus |
|--------|------|---------|-----------| 
| April 2022–Present | Founder & Lead AI Systems Engineer | AMTrix Solutions Inc. (C-Corp) | Multi-provider LLM gateways, agent governance harness, private AI, FastMCP |
| 2018–Present | Technology Lead & Systems Architect | AKM USA TRADING INC (C-Corp) | Trading operations, real-time data ingestion, conversational automation bots |
| 2013–2017 | Lead Consultant / Database Architect | Malhotra Enterprise Solutions LLC | PNC wholesale PD models, Santander CCAR FR Y-14, Basel II |
| 2015 | Vice President (CCAR Engagement) | Copal Amba (Moody's Analytics) | Santander CCAR RWA & FR Y-14 reporting pipeline |
| 2007–2013 | Assistant Director / Lead Systems Consultant | Moody's Analytics | Flagship Credit Research Database (CRD) rebuild, default detection |
| 2005–2007 | Software Developer | Intelligent Search Technology | NameSearch C/C++ fuzzy matching engine |

---

## DETAILED PROJECT BREAKDOWN

### PNC BANK — Wholesale PD Model Implementation

**What I Actually Did:**
- Implemented PD models for 4 portfolios: Small Business, FI Insurance, CRE, and one more
- Built standalone T-SQL prototypes that ran the entire model flow: raw inputs → ratio calculation → score calculation → PD output
- The prototypes served 3 purposes: Credit Appraisal, Regulatory Capital, and Stress Testing PDs (different use cases, same model)
- Managed third-party data integration — they needed external data for certain ratings
- Designed the database schema for the new Rating Platform — I improved the existing messy structure
- Built the Model Implementation Accuracy Testing platform in SQL Server, then ported to Excel so non-technical people could use it
- The testing platform validated: interim raw ratios → transformations → scores → warning signals/overrides → final PD ratings
- Created Baseline, Adverse, Severely Adverse test cases for CCAR UAT
- Worked with Strategy Testing team on Pega implementation — Pega didn't have out-of-box financial spreading, so we had to custom-build ratio calculation logic

**Technical Details I'd Remember:**
- The prototypes were in T-SQL, not just Excel — real database-backed calculation
- Warning signals and overrides were part of the model logic — not just straight PD calculation
- Financial spreading = breaking down financial statements into ratios for creditworthiness
- SIT = System Integration Testing team, not a person named "Sit"

---

### SANTANDER BANK — CCAR Stress Testing (via CopalAmba/Moody's)

**What I Actually Did:**
- Technical manager for CCAR implementation
- The project was RWA calculation and forecasting + data reconciliation
- Wrote PL/SQL scripts in RiskFoundation (Moody's data warehouse product)
- Designed FR Y-14 (A/M/Q) regulatory reports using RiskAuthority
- Source-to-target mapping for the CCAR data hub
- Got repeat business after presenting to management committee

**Technical Details I'd Remember:**
- RiskFoundation = Moody's Oracle-based data warehouse
- RiskAuthority = Moody's regulatory reporting tool
- FR Y-14 A/M/Q = Fed's CCAR reporting forms (A=Annual, M=Monthly, Q=Quarterly)
- Scenario Analyzer = Moody's stress testing extension to RiskAuthority

---

### MOODY'S ANALYTICS — Credit Research Database (CRD)

**What I Actually Did:**
- Revamped the entire CRD through automation — before, it required manual intervention
- The revamp involved redesigning and rewriting the database
- Result: better data quality, faster processing time, no human touch needed
- Worked with RiskCalc team to add EDF scoring for additional countries (EDF = Expected Default Frequency)
- Migrated from SQL Server 2000 to SQL Server 2008
- Built Default Detection application — client/server app for detecting defaults
- Built SQL wrappers and SSIS packages so RiskCalc could integrate with SQL Server
- Contributed to Moodys.com backend — Sybase and SQL Server work
- Modified stored procedures to update as market/hybrid indicators changed (for compliance department)

**Technical Details I'd Remember:**
- CRD = Credit Research Database, Moody's internal data asset
- EDF = Expected Default Frequency, Moody's proprietary PD metric
- RiskCalc = Moody's model for calculating EDFs
- Hybrid indicators = blend of market-based and fundamental indicators
- WORLDSCOPE and Compustat = external financial data feeds we integrated

---

### SYNOVUS — Basel II/CCAR Integration for 30+ Banks

**What I Actually Did:**
- Synovus was a consortium of 30+ regional banks — they needed unified Basel II and CCAR reporting
- Designed a Dual Risk Rating data warehouse
- Synced DRR information with loan accounting system and shared multi-collateral system
- The synced data fed into financial reporting and CCAR stress testing
- Acted as interface between business, technology, support, and data management

**Technical Details I'd Remember:**
- Dual Risk Rating = both obligor rating and facility rating (Basel II concept)
- Multi-collateral system = loans with multiple pieces of collateral
- The integration was the hard part — 30+ banks with different source systems

---

### INTELLIGENT SEARCH TECHNOLOGY — AI Fuzzy Matching

**What I Actually Did:**
- Redesigned their internal CRM from scratch — new application and database
- Wrote DTS packages (predecessor to SSIS) for data migration
- Developed MS Office add-ins for address validation — the add-ins used fuzzy matching
- NameSearch® was their AI product — fuzzy searching based on artificial intelligence
- Built SDKs and wrappers so NameSearch® could work with Oracle, SQL Server, .NET, PHP
- Created platform-independent address extraction solution in C and C#

**Technical Details I'd Remember:**
- NameSearch® = their flagship AI product, fuzzy logic based
- Fuzzy matching = inexact matching that tolerates typos, variations, abbreviations
- DTS = Data Transformation Services (older SQL Server ETL tool)

---

## AI PORTFOLIO DEEP DIVE (2023–Present)

### 1. AI CEO with Knowledge Base — The Flagship

**What Makes It Special:**
- 133KB production prompt — yes, that large, fully structured
- Motherboard + Cartridge architecture: the Motherboard is the system, the Cartridge is the user identity
- Embedded Knowledge Base with indexed principles: KB-001, KB-002, etc.
- Pre-flight Mandate of Execution: a checklist that runs before every AI response

**Deep Technical Details:**
- Uses `<DATA_VAULT>` tags with CDATA and CSV format for structured data
- "Inefficiency Rage" codified in KB-005 — I hate circular logic, it's in the prompt
- Topology rule: `<NODE connection="-- Label -->">` for labeled flowchart arrows
- Action Footer template with Flow atoms: 🟢🟢✅ and Momentum status
- The whole thing loads like a game cartridge into any LLM

---

### 2. CURSOR AI System Architect v5.3

**What Makes It Special:**
- RPIV = Research → Plan → Implement → Validate cycle
- Verification Mandate: every code output has test steps
- Knowledge Persistence: PROJECT.md, thoughts/ directory, Mistake Journal
- 8 Expert Personas with automatic fallback

**Deep Technical Details:**
- Token thresholds: 60k yellow warning, 70k red (cumulative context)
- HUD format: `📚 Cumulative | 🧠 Operational | 🚀 Momentum | 🫥 Sentiment | 🔄 Phase`
- State-Sync responses: `[A] Applied [B] Blocked [C] Parked [