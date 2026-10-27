# AMIT MALHOTRA — Techno-Functional Engineering Profile & Systems Dossier

**SENIOR AI SYSTEMS ARCHITECT & ENTERPRISE SOLUTIONS LEAD**  
*LLM Runtime Infrastructure · Agent Reliability & Guardrails · Enterprise Data Platforms · Credit Risk & Model Validation*  
Hicksville, NY 11801 | (917) 345-7516 | amit.malhotra1@gmail.com | github.com/amit-malhotra1 | Open to US Full-Time, Contract, and W2/1099

---

## 1. EXECUTIVE OVERVIEW & ARCHITECTURAL PHILOSOPHY

Senior Systems and AI Solutions Architect with 21+ years of production engineering experience (2005–2026) bridging Tier-1 enterprise financial infrastructure, credit-risk modeling, and modern Generative AI runtime systems.

Proven track record across three foundational pillars:
1. **Enterprise Banking & Credit Risk Platforms (Moody's & Major Banks)**: Progressed from senior database engineering to Assistant Director and Lead Systems Consultant at Moody’s Analytics, leading client-facing platform implementations (RiskAnalyst, RiskOrigin) and fully automating the Credit Research Database (CRD). Subsequently delivered strategic advisory across major commercial banks: designed unified Basel II / CCAR Dual Risk Rating (DRR) data warehouses for 30+ regional banks at Synovus; served as Wholesale Probability of Default (PD) SME at PNC Bank; and served as Vice President (CCAR Engagement via Copal Amba/Moody's) directing FR Y-14 regulatory reporting pipelines at Santander Bank.
2. **Conversational Automation & Real-Time Trading Engines (2018 – Present)**: Designed multi-persona conversational bots, voice/chat task automation systems, and high-throughput market data ingestion engines integrating financial exchange APIs.
3. **Production Generative AI Runtime Infrastructure (2022 – Present)**: Architected multi-provider LLM gateways, streaming Server-Sent Events (SSE) tool-calling translation engines, Model Context Protocol (FastMCP) servers, vision-driven desktop automation, local Apple Silicon inference nodes, and autonomous coding-agent execution guardrails validated by 700+ automated tests.

### Core Architectural Principles
- **Determinism Over Hallucination ("Compute, Then Narrate")**: Never delegate mathematical calculations or critical business invariants to an LLM. In both credit risk and AI agent workflows, calculate results in deterministic, verified code, passing the verified outputs to the model solely for structured explanation.
- **Fail-Safe Agent Execution Controls**: Enforce guardrails at the OS and filesystem level via write locks, uncommitted file protections, and mandatory automated test-suite execution before tasks can be marked complete.
- **Protocol & Vendor Independence**: Build modular adapters and proxy layers (FastMCP, streaming SSE accumulators, multi-provider gateways) to decouple enterprise systems from single-vendor rate limits and API shifts.

---

## 2. TECHNICAL STACK & ARCHITECTURAL TOOLKIT

| Domain | Technologies, Protocols & Tooling |
|---|---|
| **AI Runtime & Agent Infrastructure** | Model Context Protocol (FastMCP), Multi-Provider Gateways (Google Vertex AI, AWS Bedrock, OpenRouter, Ollama), Streaming SSE Parsers, Tool-Call Translation, Execution Guardrails, Prompt Caching, Token & Cost Telemetry, Local Model Inference (Apple Silicon, GGUF Quantization). |
| **Computer Vision & GUI Automation** | Vision-Language Models (VLMs), Screen Capture & Action Verification, React Zone Builder, Deterministic State Machine Execution, Intent-to-Outcome Verification, Session Token Budgeting. |
| **Enterprise Software & Languages** | Python (AsyncIO, stdlib, FastMCP, Pytest), Node.js / TypeScript (Express, Streaming SSE), C# / .NET, C/C++, Bash / Shell Scripting. |
| **Databases & Data Engineering** | Microsoft SQL Server (T-SQL, Stored Procedures, Schema Optimization, Indexing), Oracle (PL/SQL), SQLite, PostgreSQL, SSIS ETL Pipelines, Data Warehousing, High-Volume Data Ingestion. |
| **Financial Risk & Regulatory Frameworks** | Basel II / III IRB, CCAR (Comprehensive Capital Analysis & Review), FR Y-14 (A/M/Q), Probability of Default (PD), Loss Given Default (LGD), Exposure at Default (EAD), Risk-Weighted Assets (RWA), Dual Risk Rating (DRR), Financial Spreading. |
| **Systems, DevOps & Governance** | Linux, macOS / Apple Silicon, Docker, Caddy TLS, Automated Test Suites (700+ tests), Process Concurrency, Git Pre-Commit Controls, Enterprise Client Advisory. |

---

## 3. PROFESSIONAL EXPERIENCE & DELIVERED SYSTEMS

### AMTrix Solutions Inc., Hicksville, NY
**Founder & Principal AI Systems Architect** | April 2022 – Present

*Specialized technology engineering practice delivering enterprise LLM runtime infrastructure, agentic execution controls, and automated data platforms.*

#### A. Multi-Provider LLM Gateway Architecture (Claude Code Center)
- **Problem**: Autonomous coding agents suffered from single-vendor API limits, unmonitored token spend, and incompatible tool-calling response formats when routing requests across cloud providers.
- **Engineering Solution**: Developed a self-hosted gateway in Node.js, Express, and SQLite that dynamically routes agent requests across Google Vertex AI (Gemini, Claude rawPredict), AWS Bedrock, OpenRouter, and local Ollama models with zero vendor lock-in.
- **Streaming Tool Translation**: Built a streaming Server-Sent Events (SSE) accumulator that merges fragmented function-call chunks from non-Anthropic models into standard tool-call events for multi-turn agent loops.
- **Cost Controls & Telemetry**: Implemented provider prompt caching, exact-match SQLite response caching, and request-level telemetry tracking token volume, cache hit ratios, and estimated expense.

#### B. Coding-Agent Execution Controls & Reliability Harness (AMTrix Plan)
- **Problem**: Autonomous coding agents frequently overwrite uncommitted files, lose context during long sessions, and mark tasks "done" without verification.
- **Engineering Solution**: Built a Python harness (~23K lines of stdlib Python, 700+ automated unit tests) enforcing OS-level read-only file locks, pre-tool checks safeguarding uncommitted files, and pre-commit verification gates.
- **Automated Verification**: Configured automated test gates requiring passing test runs before tasks can be marked complete by the agent.

#### C. Local Model Inference Environment
- **Problem**: Escalating commercial API costs and privacy requirements prevented running internal code analysis on public endpoints.
- **Engineering Solution**: Configured local LLM inference on a 64GB Apple Silicon workstation using Ollama and GGUF quantized models (including Qwen and Llama architectures), with Open WebUI access and remote connectivity over Tailscale.

#### D. Model Context Protocol (FastMCP) Tooling
- **Problem**: Repetitive file loading and large response payloads caused rapid context exhaustion in multi-step agent workflows.
- **Engineering Solution**: Developed FastMCP servers exposing 10 tools for targeted file retrieval, structured schema compaction, reference-based storage, and recovery from truncated model outputs.

#### E. Vision-LLM Desktop Automation & Control Framework
- **Problem**: Vision and computer-use agents for legacy desktop applications without APIs suffer from non-deterministic behavior, hesitation, and inconsistent actions during long unattended runs.
- **Engineering Solution**: Architected a real-time visual decision agent with a clean three-tier separation: **Perception** (multimodal vision-language model reads the live screen), **Decision** (deterministic priority policy lookup table / JSON state machine), and **Action** (verified mouse/keyboard execution with intent-to-outcome verification).
- **Tooling & Ergonomics**: Built a React coordinate zone builder defining interactive screen regions, swappable strategy cartridges, and per-screenshot session token budgeting (~1.5K tokens/capture) allowing stable 4–5 hour unattended runs.
- **Operational Scale**: Executed 28,600+ audited actions across 270 live runs on a desktop trading interface, enforcing hard risk limits and preventing runaway automated loops.

#### F. Deterministic Data Collection & Analysis
- **Problem**: High-frequency web data collection suffered from daemon contention and duplicated observations.
- **Engineering Solution**: Built a multi-daemon event collection system that ingested 9.8 million observations into SQL for inventory and restock analysis, using process locking and PID verification to prevent duplicate collectors.

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

#### A. Santander Bank — Vice President & Technical Manager, CCAR Stress Testing (via Copal Amba / Moody's, 2015)
- **Mission**: Deliver regulatory risk infrastructure for CCAR stress testing, Risk-Weighted Assets (RWA) calculation, and Federal Reserve regulatory reporting.
- **Architecture & Implementation**:
  - Engineered PL/SQL extraction and transformation engines within Moody's RiskFoundation Oracle data warehouse.
  - Designed source-to-target data mappings for the CCAR data hub and automated Federal Reserve FR Y-14 (A/M/Q) reporting submissions using RiskAuthority and Scenario Analyzer.
  - Presented architectural milestones to executive management committees, securing direct client commendations and expanded follow-on project scope.

#### B. PNC Bank — Subject Matter Expert (SME), Wholesale PD Model Implementation (2014 – 2015)
- **Mission**: Implement and validate wholesale Probability of Default (PD) rating models across commercial banking portfolios.
- **Architecture & Implementation**:
  - Retained as Subject Matter Expert to prototype standalone T-SQL calculation engines across 4 commercial portfolios: Small Business, Financial Institution Insurance, Commercial Real Estate (CRE), and Middle Market.
  - Built the end-to-end model pipeline: raw financial statement extraction → financial spreading ratio calculations → non-linear score transformations → regulatory capital warning overrides → final PD rating outputs.
  - Designed the Model Implementation Accuracy Testing platform in SQL Server, validating calculation integrity across Baseline, Adverse, and Severely Adverse CCAR stress scenarios.
  - Collaborated with strategy and Pega implementation teams to design custom financial spreading algorithms where out-of-the-box spreading was unavailable.

#### C. Synovus Bank — Strategic Consultant & Enterprise Architect (2013 – 2014)
- **Mission**: Establish unified Basel II and CCAR risk-data integration across a consortium of 30+ regional banks.
- **Architecture & Implementation**:
  - Designed the enterprise Dual Risk Rating (DRR) data warehouse, capturing and synchronizing obligor risk ratings and facility ratings.
  - Integrated DRR feeds with core loan accounting systems and shared multi-collateral databases, resolving complex facility allocation across multi-collateral commercial loans.
  - Served as the strategic technical interface bridging executive credit risk committees, data management, and enterprise technology groups.

---

### Moody's Analytics, New York, NY
**Assistant Director / Lead Systems Consultant** | Jul 2007 – Nov 2013

*Progressed from senior systems engineering into Assistant Director and Lead Systems Consultant, combining deep database architecture with client-facing strategic consulting across major commercial banks.*

- **Enterprise Platform Deployments & Strategic Consulting**: Led database configuration, schema design, and technical integration for Moody's flagship RiskAnalyst (RA) and RiskOrigin credit platforms across commercial banking clients; advised client risk officers and architects on financial spreading workflows and model customization.
- **Credit Research Database (CRD) Automation**: Redesigned, rewrote, and fully automated Moody's internal flagship Credit Research Database through advanced T-SQL stored procedures and SSIS ETL pipelines, removing manual processing bottlenecks and accelerating data throughput.
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
