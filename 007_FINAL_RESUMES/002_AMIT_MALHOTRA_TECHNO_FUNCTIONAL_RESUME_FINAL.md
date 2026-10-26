# AMIT MALHOTRA — Techno-Functional Engineering Profile

> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 02:30 UTC+4  
> **Status:** Final Approved  

**Forward Deployed AI Engineer & Lead Systems Architect**  
*Agent Reliability · Multi-Provider LLM Gateways · Private AI Systems · Mission-Critical Data Engineering*  
Hicksville, NY 11801 | (917) 345-7516 | amit.malhotra1@gmail.com | github.com/amit-malhotra1

---

## 1. PROFESSIONAL OVERVIEW

Hardcore Systems and Data Engineer with 21+ years of experience developing, implementing, and deploying mission-critical software applications, enterprise database platforms, and production Generative AI infrastructure. 

A seasoned builder with dual strengths:
1. **Mission-Critical Enterprise Systems (15+ Years)**: Architected, rewritten, and automated flagship database assets at Moody's Analytics, including the Credit Research Database (CRD), wholesale PD model execution platforms in T-SQL (PNC Bank), and CCAR stress testing regulatory reporting pipelines in PL/SQL (Santander Bank).
2. **Cutting-Edge Production AI Engineering (2022 – Present)**: Architected multi-provider LLM gateways, streaming SSE tool-calling translators, autonomous agent reliability harnesses (~23K lines Python stdlib, 700+ tests), and private hardware inference nodes running 30B parameter models at 256K context.

---

## 2. CORE TECHNICAL STACK

| Domain | Technologies & Systems |
|---|---|
| **AI Runtime & Gateways** | Model Context Protocol (FastMCP), Claude Code Hooks & Tools, Multi-Provider Routing (Google Vertex AI, AWS Bedrock, OpenRouter, Ollama), Streaming SSE Translators, Prompt Caching, Token Diet Profiles, Private AI (GGUF 30B Models, Apple Silicon, Tailscale). |
| **Languages & Frameworks** | Python (AsyncIO, stdlib, FastMCP, Pytest), Node.js / TypeScript (Express, Streaming SSE), C# / .NET, C/C++, Bash / Shell Scripting. |
| **Databases & Data Engineering** | Microsoft SQL Server (T-SQL, Stored Procedures, Schema Redesign, Query Optimization), Oracle (PL/SQL), SQLite, PostgreSQL, SSIS ETL Pipelines, Data Warehousing, Index Optimization, Distributed Caching. |
| **Systems & Architecture** | Docker, Linux, macOS/Apple Silicon Hardware Optimization, Caddy TLS, Git Pre-Commit Gates, Automated Test Harnesses, Event-Driven Daemons. |

---

## 3. PROFESSIONAL EXPERIENCE & DELIVERED SYSTEMS

### AMTrix Solutions Inc. (C-Corp), Hicksville, NY
**Founder & Lead AI Systems Engineer** | April 2022 – Present

*Specialized technology solutions and product development firm architecting Generative AI runtime infrastructure, multi-provider LLM gateways, and autonomous agent reliability systems.*

#### A. Multi-Provider LLM Gateway Architecture (Claude Code Center)
- **Problem**: Autonomous coding agents suffered from vendor lock-in, unmonitored token burn, and fragmented tool-calling responses when attempting to route traffic to alternative cloud providers.
- **Engineering Solution**: Developed a self-hosted, high-throughput proxy in Node.js, Express, and SQLite that dynamically routes agent traffic explicitly across Google Vertex AI (Gemini native, Claude rawPredict, Model-as-a-Service third-party models), AWS Bedrock, OpenRouter, and local Ollama without silent fallbacks.
- **Streaming Tool Translation Engine**: Engineered a streaming Server-Sent Events (SSE) accumulator that merges fragmented function-call chunks and reasoning signatures into uniform Anthropic tool blocks, enabling non-Anthropic models to reliably execute agentic tool loops.
- **Cost Controls & Telemetry**: Layered multi-tiered cost controls including 1-hour prompt-cache injection, keepalive daemons, Vertex explicit context caching, and SQLite exact-match response caching; built real-time HUD telemetry reporting tokens, cache hits, and cost per request.

#### B. Autonomous Agent Governance & Reliability Harness (AMTrix Plan)
- **Problem**: Production coding agents frequently corrupt uncommitted files, lose context, drift from task scope, and mark work "done" without verification.
- **Engineering Solution**: Architected a drop-in, zero-dependency governance framework (~23K lines of stdlib Python, 700+ automated unit tests) establishing numbered, read-only session ledgers, OS-level file write locks, and pre-tool execution hooks that prevent uncommitted data overwrites.
- **Measured Verification Gates**: Implemented strict pre-commit gates blocking staged secrets and requiring automated test-suite execution before tasks can be marked complete by the agent.
- **Traceability Rules Ledger**: Engineered an audit ledger mapping ~190 written operating rules to the concrete code modules that enforce each rule.

#### C. Private High-Context Inference Platform
- **Engineering Solution**: Deployed a zero-cloud private inference workstation on 64GB Apple Silicon running 30B parameter models (Qwen3, Llama 3.1) at 256K context using GGUF quantization, Ollama, Open WebUI, and SearxNG private search over Tailscale, reducing internal development inference costs to $0.

#### D. Model Context Protocol (FastMCP) Servers
- **Engineering Solution**: Shipped custom multi-model MCP servers (FastMCP, Python) with 10 tools optimizing IDE agent context windows through pass-by-path file loading, schema-bound JSON compression, reference-ID stores, and anti-truncation recovery loops.

#### E. Real-Time Event-Driven Platform
- **Engineering Solution**: Engineered a fault-tolerant multi-daemon event harvesting platform with lock-elected singleton architecture and PID-verified registries; ingested and analyzed 9.8M observations in SQL for inventory restock prediction.

---

### AKM USA TRADING INC (C-Corp), Hicksville, NY
**Technology Lead & Systems Architect** | 2018 – Present

*Trading operations and technology development firm building automated data ingestion systems, algorithmic interfaces, and conversational workflow solutions.*

- **Pre-GenAI Conversational Automation**: Architected and deployed natural language conversational bots, voice/chat task automation bots, and multi-channel API orchestration pipelines for commercial trading workflows.
- **Algorithmic Execution & Market Data Engines**: Engineered real-time market data ingestion engines, automated signal processors, and order execution interfaces integrating with financial exchange APIs.
- **API Orchestration & Backend Infrastructure**: Developed customized Python and shell automation pipelines connecting disparate trading data feeds, alert systems, and transaction databases.

---

### Malhotra Enterprise Solutions LLC, Hicksville, NY
**Principal Technology Consultant & Database Architect** | 2013 – 2017

*Enterprise technology consulting firm delivering financial database platforms, regulatory stress testing systems, and credit model implementations for major banks.*

- **PNC Bank Wholesale PD Model Implementation**: Architected standalone T-SQL calculation engines prototyping financial spreading, ratio calculation, and default probability outputs across 4 commercial portfolios; designed the Model Implementation Accuracy Testing platform in SQL Server.
- **Santander Bank CCAR Regulatory Reporting Pipeline (via Copal Amba / Moody's, 2015)**: Served as Technical Manager / Vice President for CCAR implementation; developed PL/SQL extraction and transformation engines within Moody’s RiskFoundation Oracle data warehouse to automate Federal Reserve FR Y-14 (A/M/Q) stress testing submissions.
- **Automated Banking Model Testing Platforms**: Architected automated model-accuracy test suites validating interim raw financial ratios, non-linear score transformations, and regulatory capital warning overrides across commercial banking clients.
- **Regulatory Reporting Integration**: Managed Basel II and CCAR reporting data integration across a consortium of 30+ financial institutions, ensuring strict data governance and regulatory compliance.

---

### Moody's Analytics, New York, NY
**Assistant Director / Lead Systems Consultant** | Jul 2007 – Nov 2013

*Core database architect and systems engineer responsible for internal financial databases, regulatory modeling platforms, and client implementation engines.*

- **Credit Research Database (CRD) Automation**: Instrumental in redesigning, rewriting, and automating Moody's internal flagship Credit Research Database; developed high-performance T-SQL stored procedures and SSIS packages, eliminating manual operational bottlenecks and accelerating database processing throughput.
- **Default Detection Application**: Engineered a client/server default detection platform in C#/.NET and SQL Server; integrated Moody’s proprietary RiskCalc EDF (Expected Default Frequency) scoring models with external financial data feeds (Compustat, WorldScope).
- **Enterprise Platform Implementations**: Led database configuration, schema design, and backend integration of Moody's RiskAnalyst and RiskOrigin platforms across Tier-1 financial institutions.
- **Database Modernization**: Led the backend database migration from SQL Server 2000 to SQL Server 2008 and developed backend data services for Moodys.com (Sybase and SQL Server).

---

### Intelligent Search Technology, New York, NY
**Software Developer** | Jun 2005 – Jul 2007

- Developed core algorithms for the NameSearch fuzzy matching search engine in C/C++; built SDK integration libraries for Oracle, SQL Server, and .NET.

---

## 4. EDUCATION

**Syracuse University**, L.C. Smith College of Engineering and Computer Science  
**Bachelor of Science (B.S.) in Computer Science**, Minor in Mathematics, 2005
