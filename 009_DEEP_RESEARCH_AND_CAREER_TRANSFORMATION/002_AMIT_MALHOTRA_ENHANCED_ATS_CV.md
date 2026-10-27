# AMIT MALHOTRA
Hicksville, NY 11801 | (917) 345-7516 | amit.malhotra1@gmail.com | github.com/amit-malhotra1 | Open to US Full-Time, Contract, and W2/1099

**SENIOR AI SYSTEMS ARCHITECT & ENTERPRISE SOLUTIONS LEAD**  
*LLM Runtime Infrastructure · Agent Reliability & Guardrails · Enterprise Data Platforms · Credit Risk & Model Validation*

---

## PROFESSIONAL SUMMARY

Senior Systems & AI Solutions Architect with 21+ years of experience spanning enterprise financial platforms, regulatory risk modeling, and production Generative AI runtime infrastructure. Proven track record progressing from core systems engineering to Assistant Director and Lead Systems Consultant at Moody’s Analytics, leading RiskAnalyst (RA) and RiskOrigin enterprise platform implementations across Tier-1 institutions and automating the internal Credit Research Database (CRD). Subsequently delivered high-impact strategic advisory and technical leadership across major commercial banking institutions: architected unified Basel II / CCAR Dual Risk Rating data warehouses for a consortium of 30+ regional banks at Synovus; served as Wholesale Probability of Default (PD) SME at PNC Bank; and served as Vice President (CCAR Engagement via Copal Amba/Moody's) directing FR Y-14 regulatory reporting and RWA stress testing pipelines at Santander Bank.

Over the past eight years, expanded this institutional rigor into advanced AI systems—pioneering conversational AI, multi-persona voice agents, and algorithmic automation, followed by architecting production-grade Generative AI infrastructure at AMTrix Solutions: multi-provider LLM gateways, vision-language model (VLM) desktop automation engines, streaming tool-call translation engines, Model Context Protocol (FastMCP) servers, local Apple Silicon inference environments, and autonomous coding-agent execution guardrails validated by 700+ automated tests. Uniquely bridges enterprise data governance, complex financial calculations, and modern LLM runtime architectures for mission-critical deployments.

---

## CORE TECHNICAL COMPETENCIES

- **AI Runtime & Agent Infrastructure**: Model Context Protocol (FastMCP), Multi-Provider Gateways (Google Vertex AI, AWS Bedrock, OpenRouter, Ollama), Streaming SSE Parsers, Tool-Call Translation, Execution Guardrails & Pre-Tool Hooks, Prompt Caching, Token & Cost Telemetry, Local Model Inference (Apple Silicon, GGUF Quantization), Conversational AI & NLP.
- **Computer Vision & GUI Agent Automation**: Vision-Language Models (VLMs), Screen Capture & Visual Action Verification, Coordinate Mapping (React Zone Builder), Deterministic State-Machine Execution, Session Token Budgeting.
- **Enterprise Software & Languages**: Python (AsyncIO, FastMCP, Pytest), Node.js / TypeScript (Express, Streaming SSE), C# / .NET, C/C++, Bash / Shell Scripting.
- **Data Engineering & Database Architecture**: Microsoft SQL Server (T-SQL, Stored Procedures, Schema Optimization, Indexing), Oracle (PL/SQL), SQLite, PostgreSQL, SSIS ETL Pipelines, Data Warehousing, High-Volume Data Ingestion.
- **Financial Risk & Regulatory Frameworks**: Basel II / III IRB, CCAR (Comprehensive Capital Analysis & Review), FR Y-14 (A/M/Q), Probability of Default (PD), Loss Given Default (LGD), Exposure at Default (EAD), Risk-Weighted Assets (RWA), Dual Risk Rating (DRR).
- **Systems & Practices**: Linux, macOS / Apple Silicon, Docker, Caddy TLS, Automated Test Suites (700+ tests), Process Concurrency, Git Pre-Commit Controls, Enterprise Client Advisory.

---

## PROFESSIONAL EXPERIENCE

### AMTrix Solutions Inc., Hicksville, NY
**Founder & Principal AI Systems Architect** | April 2022 – Present

*Specialized technology engineering practice delivering enterprise LLM runtime infrastructure, agentic execution controls, and automated data platforms.*

- **Multi-Provider LLM Gateway Architecture**: Built a self-hosted, provider-agnostic gateway in Node.js, Express, and SQLite providing a unified, Anthropic-compatible interface across Google Vertex AI (Gemini, Claude rawPredict), AWS Bedrock, OpenRouter, and local Ollama models, reducing reliance on single-provider capacity.
- **Streaming Tool-Call Translation Engine**: Developed a streaming Server-Sent Events (SSE) translation layer that reconstructs fragmented function-call chunks from non-Anthropic models into standard tool-call events for multi-turn agent loops.
- **Cost Engineering & Token Telemetry**: Implemented multi-tiered cost controls including provider prompt caching, exact-match SQLite response caching, and request-level telemetry tracking token usage, cache hits, and estimated expense.
- **Agent Execution Controls (AMTrix Plan)**: Built a Python coding-agent harness with OS-level file protections, pre-tool checks safeguarding uncommitted files, and automated test gates requiring passing test runs before tasks are marked complete; backed by 700+ automated tests.
- **Local Model Inference Workstation**: Deployed local LLM inference on a 64GB Apple Silicon workstation using Ollama and GGUF quantized models (including Qwen and Llama architectures), with Open WebUI access and remote connectivity over Tailscale.
- **Model Context Protocol (FastMCP) Servers**: Built FastMCP servers exposing 10 tools for targeted file retrieval, structured schema compression, reference-based storage, and recovery from truncated model outputs.
- **Vision-LLM Desktop Automation & Control Framework**: Built a multimodal vision-language model (VLM) desktop automation engine for legacy applications without APIs, separating perception (VLM screen reading), decision (deterministic JSON state machine with priority lookup tables), and verified action execution; engineered a React coordinate zone builder and session budgeting (~1.5K tokens/capture) across 28,600+ audited actions over 270 unattended live runs.
- **Deterministic Validation Pipelines**: Separated analytical calculations from LLM-generated explanations, keeping mathematical formulas and risk invariants in deterministic code while using LLMs solely to articulate verified outputs.
- **High-Volume Data Ingestion**: Built a multi-daemon data collection system that ingested and structured 9.8 million observations in SQL for inventory and restock analysis, using process locking and PID verification to prevent duplicate collectors.

---

### AKM USA TRADING INC, Hicksville, NY
**Technology Lead & Systems Architect** | 2018 – Present

*Trading operations and technology firm operating automated market-data ingestion, conversational automation, and execution systems.*

- **Conversational AI & Task Automation**: Designed and deployed natural language conversational interfaces and multi-persona voice/chat task automation bots connecting natural language user requests to backend APIs and trading feeds.
- **Real-Time Market Data Ingestion**: Engineered real-time data ingestion engines, automated signal processors, and order execution interfaces connecting to financial exchange APIs.
- **Data Integration & Notification Pipelines**: Automated data movement between live feeds, execution alerts, and transaction databases using Python and shell automation pipelines.

---

### Malhotra Enterprise Solutions LLC, Hicksville, NY
**Principal Strategic Consultant & Database Architect** | 2013 – 2017

*Enterprise advisory and solutions practice delivering regulatory risk infrastructure, credit model implementations, and strategic data architecture for Tier-1 financial institutions.*

- **Santander Bank — Vice President & Technical Manager, CCAR Stress Testing (via Copal Amba / Moody's, 2015)**:
  - Directed technical implementation for CCAR stress testing, Risk-Weighted Assets (RWA) calculation, and regulatory data reconciliation.
  - Developed high-performance PL/SQL extraction and transformation engines in Moody's RiskFoundation Oracle data warehouse.
  - Authored Federal Reserve FR Y-14 (A/M/Q) regulatory reporting pipelines in RiskAuthority, securing direct commendation and follow-on project scope from executive leadership.
- **PNC Bank — Subject Matter Expert (SME), Wholesale PD Model Implementation (2014 – 2015)**:
  - Subject Matter Expert prototyping standalone T-SQL calculation engines across 4 commercial portfolios: Small Business, FI Insurance, Commercial Real Estate (CRE), and Middle Market.
  - Implemented the complete credit model flow: raw financial inputs → spreading ratios → non-linear score transformations → regulatory capital warning overrides → final Probability of Default (PD) ratings.
  - Architected the Model Implementation Accuracy Testing platform in SQL Server (and ported analytical models to client teams), validating calculation integrity across Baseline, Adverse, and Severely Adverse CCAR scenarios.
  - Partnered with strategy teams on Pega implementation, designing custom financial spreading algorithms to compute creditworthiness ratios where out-of-the-box spreading was unavailable.
- **Synovus Bank — Strategic Consultant & Enterprise Architect (2013 – 2014)**:
  - Retained as strategic data architect to establish unified Basel II and CCAR reporting infrastructure across a consortium of 30+ regional banks.
  - Designed the enterprise Dual Risk Rating (DRR) data warehouse, synchronizing obligor risk ratings and facility ratings with core loan accounting and shared multi-collateral systems.
  - Acted as key strategic liaison bridging executive risk management, credit policy, data management, and enterprise technology teams.

---

### Moody's Analytics, New York, NY
**Assistant Director / Lead Systems Consultant** | Jul 2007 – Nov 2013

*Progressed from senior systems engineering into Assistant Director and Lead Systems Consultant, combining deep database architecture with client-facing strategic consulting across major commercial banks.*

- **Enterprise Platform Deployments & Strategic Consulting**: Led database configuration, schema design, and technical integration for Moody's flagship RiskAnalyst (RA) and RiskOrigin credit platforms across commercial banking clients; advised client risk officers and architects on financial spreading workflows and model customization.
- **Credit Research Database (CRD) Automation**: Redesigned, rewrote, and fully automated Moody's internal flagship Credit Research Database through advanced T-SQL stored procedures and SSIS ETL pipelines, eliminating manual operational bottlenecks and accelerating data throughput.
- **Default Detection Application**: Engineered a client/server default detection platform in C#/.NET and SQL Server; integrated Moody’s proprietary RiskCalc EDF (Expected Default Frequency) models with global financial databases (Compustat, WorldScope).
- **Core Technology Modernization**: Directed database migration from SQL Server 2000 to SQL Server 2008 and developed fault-tolerant backend data services supporting Moodys.com (Sybase and SQL Server).

---

### Intelligent Search Technology, New York, NY
**Software Developer** | Jun 2005 – Jul 2007

- Developed core fuzzy matching algorithms for the NameSearch® search engine in C/C++; built SDK integration libraries for Oracle, SQL Server, and .NET.

---

## EDUCATION

**Syracuse University**, L.C. Smith College of Engineering and Computer Science  
**Bachelor of Science (B.S.) in Computer Science**, Minor in Mathematics, 2005
