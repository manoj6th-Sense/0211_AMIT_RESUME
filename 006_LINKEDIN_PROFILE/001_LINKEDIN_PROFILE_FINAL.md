# LinkedIn Profile — Amit Malhotra

> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 02:30 UTC+4  
> **Status:** Final Approved  

---

## HEADLINE

**Staff AI Systems Engineer & Solutions Architect | Agent Reliability, LLM Gateways & Private AI | Ex-Moody's Lead Systems Engineer (Credit Research Database) | Python · Node.js · T-SQL**

---

## ABOUT

I am a hardcore systems and data engineer with 21+ years of experience designing, building, and automating mission-critical software, enterprise databases, and production Generative AI infrastructure.

Throughout my career, I have specialized in building robust software architectures for complex, high-stakes environments where data integrity and runtime reliability are non-negotiable:

🔹 PRODUCTION GENERATIVE AI & AGENT INFRASTRUCTURE (April 2022 – Present):
At AMTrix Solutions Inc. (C-Corp), I architect production-grade runtime infrastructure and software solutions for AI agents and LLMs:
• Multi-Provider LLM Gateways: Built high-throughput proxy architectures routing agent traffic across Google Vertex AI, AWS Bedrock, OpenRouter, and local models with prompt caching and real-time cost telemetry.
• Streaming Tool Calling: Engineered streaming SSE function-call accumulators translating non-Anthropic model responses into uniform tool blocks for agentic loops.
• Agent Governance & Safety: Architected zero-dependency agent safety harnesses (23K lines Python stdlib, 700+ tests) with OS-level file write locks, pre-tool hooks preventing uncommitted data loss, and automated test-passing verification gates.
• Private On-Prem AI: Deployed private inference workstations on 64GB Apple Silicon running 30B parameter models at 256K context via GGUF quantization.

🔹 ENTERPRISE SOFTWARE & CONVERSATIONAL AUTOMATION (2013 – Present):
At AKM USA TRADING INC (C-Corp) (2018 – Present) and Malhotra Enterprise Solutions LLC (2013 – 2017), I engineered real-time data ingestion pipelines, automated trading signal execution interfaces, conversational chatbots, and enterprise financial platforms—including standalone T-SQL wholesale PD model calculation engines for PNC Bank and CCAR regulatory reporting pipelines (FR Y-14) for Santander Bank.

🔹 MISSION-CRITICAL DATABASE PLATFORMS (Moody's Analytics, 2007 – 2013):
At Moody's Analytics, I was instrumental in redesigning, rewriting, and fully automating the internal flagship Credit Research Database (CRD). I authored complex T-SQL stored procedures, designed SSIS ETL pipelines, eliminated manual operational bottlenecks, and developed client/server default detection software in C#/.NET and SQL Server.

Technical Toolkit: Python (AsyncIO, FastMCP, Pytest), Node.js / TypeScript, C#/.NET, C/C++, SQL Server (T-SQL, Schema Redesign), Oracle (PL/SQL), SQLite, PostgreSQL, Docker, Linux.

---

## EXPERIENCE

### AMTrix Solutions Inc. (C-Corp)
**Founder & Lead AI Systems Engineer** | April 2022 – Present | Hicksville, NY

Architecting modern Generative AI runtime infrastructure, multi-provider LLM gateways, and autonomous agent reliability systems.
• Engineered Claude Code Center, a self-hosted multi-provider LLM gateway (Node.js, Express, SQLite) routing agent traffic across Google Vertex AI, AWS Bedrock, OpenRouter, and local Ollama without vendor lock-in.
• Built a streaming Server-Sent Events (SSE) accumulator translating multi-provider function calls into uniform Anthropic tool blocks, enabling non-Anthropic models to reliably execute agentic tool loops.
• Implemented multi-tiered cost controls including 1-hour prompt-cache injection, Vertex explicit context caching, and SQLite exact-match response caching.
• Designed AMTrix Plan, an autonomous agent governance harness (~23K lines Python stdlib, 700+ tests) enforcing OS-level read-only file locks, pre-tool execution hooks, and automated test-passing verification gates.
• Deployed a private inference workstation on 64GB Apple Silicon running 30B parameter models at 256K context via GGUF quantization and Ollama over Tailscale.
• Shipped custom multi-model FastMCP servers with 10 tools optimizing context windows through pass-by-path loading, schema-bound JSON compression, and anti-truncation recovery loops.

---

### AKM USA TRADING INC (C-Corp)
**Technology Lead & Systems Architect** | 2018 – Present | Hicksville, NY

Automated data ingestion systems, algorithmic trading interfaces, and conversational workflow solutions.
• Architected natural language conversational bots, voice/chat task automation bots, and multi-channel API orchestration pipelines for commercial trading operations.
• Engineered real-time market data ingestion engines, automated signal processors, and order execution interfaces integrating with financial exchange APIs.
• Developed customized Python and shell automation pipelines connecting trading feeds, alert systems, and transaction databases.

---

### Malhotra Enterprise Solutions LLC
**Principal Technology Consultant & Database Architect** | 2013 – 2017 | Hicksville, NY

Delivered financial database platforms, regulatory stress testing systems, and credit model implementations for major banks.
• PNC Bank: Architected standalone T-SQL calculation engines prototyping financial spreading, ratio calculation, and default probability outputs across 4 commercial portfolios; designed the Model Implementation Accuracy Testing platform in SQL Server.
• Santander Bank (via Copal Amba / Moody's, 2015): Technical Manager / Vice President for CCAR implementation; developed PL/SQL extraction and transformation engines within Moody’s RiskFoundation Oracle data warehouse to automate Federal Reserve FR Y-14 stress testing submissions.
• Architected automated model-accuracy test suites validating interim raw financial ratios, non-linear score transformations, and regulatory capital warning overrides.

---

### Moody's Analytics
**Assistant Director / Lead Systems Consultant** | Jul 2007 – Nov 2013 | New York, NY

• Credit Research Database (CRD): Instrumental in redesigning, rewriting, and automating Moody's internal flagship Credit Research Database; developed high-performance T-SQL stored procedures and SSIS packages, eliminating manual operational bottlenecks and accelerating database processing throughput.
• Default Detection Application: Engineered a client/server default detection platform in C#/.NET and SQL Server; integrated Moody’s proprietary RiskCalc EDF scoring models with external financial data feeds (Compustat, WorldScope).
• Led database configuration, schema design, and backend integration of Moody's RiskAnalyst and RiskOrigin platforms across Tier-1 financial institutions.
• Led backend database migration from SQL Server 2000 to SQL Server 2008 and developed backend data services for Moodys.com.

---

### Intelligent Search Technology
**Software Developer** | Jun 2005 – Jul 2007 | New York, NY

• Developed core algorithms for the NameSearch fuzzy matching search engine in C/C++; built SDK integration libraries for Oracle, SQL Server, and .NET.

---

## EDUCATION

**Syracuse University**, L.C. Smith College of Engineering and Computer Science  
**Bachelor of Science (B.S.) in Computer Science**, Minor in Mathematics, 2005
