# AMIT MALHOTRA

> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 02:30 UTC+4  
> **Status:** Final Approved  

Hicksville, NY 11801 | (917) 345-7516 | amit.malhotra1@gmail.com | github.com/amit-malhotra1 | Open to US Full-Time, Contract, and W2/1099

**STAFF AI SYSTEMS ENGINEER · FORWARD DEPLOYED AI ARCHITECT**  
*Agent Reliability & Governance · Multi-Provider LLM Gateways · High-Throughput Data Systems · Private AI*

---

## PROFESSIONAL SUMMARY

Hardcore Systems and Data Engineer with 21+ years of hands-on experience designing, implementing, and deploying mission-critical software applications, enterprise database platforms, and production Generative AI infrastructure. Proven track record at Moody’s Analytics engineering and automating the internal flagship Credit Research Database (CRD) and financial calculation engines. Since April 2022, architecting modern GenAI and agentic systems under AMTrix Solutions Inc. (C-Corp): multi-provider LLM gateways, autonomous agent reliability harnesses, FastMCP servers, and private on-prem inference nodes. Prior experience includes engineering automated trading execution engines and conversational automation at AKM USA TRADING INC (C-Corp) from 2018 onward, and institutional credit model implementations at Malhotra Enterprise Solutions LLC (2013–2017). Combines deep database and runtime systems engineering with state-of-the-art AI infrastructure.

---

## CORE TECHNICAL COMPETENCIES

- **Generative AI & Agent Infrastructure**: Model Context Protocol (FastMCP), Multi-Provider Gateways (Google Vertex AI, AWS Bedrock, OpenRouter, Ollama), Streaming SSE Accumulators, Tool-Calling Translation, Claude Code Hooks & Tools, Prompt Caching, Token Cost Telemetry, Private On-Prem AI (30B GGUF Models, Apple Silicon, Tailscale), Deterministic Execution Pipelines.
- **Programming Languages**: Python (AsyncIO, stdlib, FastMCP, Pytest), Node.js / TypeScript (Express, Streaming SSE), C# / .NET, C/C++, Bash / Shell Scripting.
- **Database & Data Engineering**: Microsoft SQL Server (T-SQL, Stored Procedures, Schema Redesign, Query Optimization), Oracle (PL/SQL), SQLite, PostgreSQL, SSIS ETL Pipelines, Data Warehousing, Index Optimization, Distributed Caching.
- **Systems & Architecture**: Docker, Linux, macOS/Apple Silicon Hardware Optimization, Caddy TLS, Git Pre-Commit Gates, Automated Test Harnesses, Event-Driven Daemons.

---

## PROFESSIONAL EXPERIENCE

### AMTrix Solutions Inc. (C-Corp), Hicksville, NY
**Founder & Lead AI Systems Engineer** | April 2022 – Present

*Specialized technology solutions and product development firm architecting Generative AI runtime infrastructure, multi-provider LLM gateways, and autonomous agent reliability systems.*

- **Multi-Provider LLM Gateway Architecture (Claude Code Center)**: Engineered a self-hosted, high-throughput proxy (Node.js, Express, SQLite) routing agent traffic across Google Vertex AI (Gemini, Claude rawPredict, Model-as-a-Service third-party models), AWS Bedrock, OpenRouter, and local Ollama without vendor lock-in.
- **Streaming Function-Call Translation Engine**: Developed a streaming Server-Sent Events (SSE) accumulator translating multi-provider function calls into uniform Anthropic tool blocks; implemented dynamic per-model registry flags for reliable tool-calling execution on non-Anthropic models.
- **Cost Engineering & Token Telemetry**: Implemented multi-tiered cost controls including 1-hour prompt-cache injection, keepalive daemons, Vertex explicit context caching, and SQLite exact-match response caching; built real-time HUD telemetry reporting tokens, cache hits, and cost per request.
- **Autonomous Agent Governance Harness (AMTrix Plan)**: Architected a zero-dependency agent safety harness (~23K lines Python stdlib, 700+ tests) enforcing OS-level read-only file locks, pre-tool execution hooks preventing uncommitted data overwrites, and automated test-passing verification gates before tasks are marked complete.
- **Private High-Context Inference Node**: Deployed a private inference workstation on 64GB Apple Silicon running 30B parameter models (Qwen3, Llama 3.1) at 256K context via GGUF quantization, Ollama, and Open WebUI over Tailscale, reducing internal development inference costs to $0.
- **Model Context Protocol (FastMCP) Servers**: Shipped custom multi-model MCP servers (FastMCP, Python) with 10 tools optimizing IDE agent context windows through pass-by-path file loading, schema-bound JSON compression, reference-ID stores, and anti-truncation recovery loops.
- **Deterministic AI Execution Pipelines**: Designed "compute, then narrate" rule engines where deterministic code calculates complex formulas and risk invariants, using the LLM solely to explain verified mathematical results without hallucination risk.
- **Real-Time Data Collection Platform**: Engineered a fault-tolerant multi-daemon event harvesting platform with lock-elected singleton architecture and PID-verified registries; ingested and analyzed 9.8M observations in SQL for availability and restock intelligence.

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

- **PNC Bank Wholesale Model Implementation**: Architected standalone T-SQL calculation engines prototyping financial spreading, ratio calculation, and default probability outputs across 4 commercial portfolios; designed the Model Implementation Accuracy Testing platform in SQL Server.
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

## EDUCATION

**Syracuse University**, L.C. Smith College of Engineering and Computer Science  
**Bachelor of Science (B.S.) in Computer Science**, Minor in Mathematics, 2005
