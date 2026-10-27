# LinkedIn Profile — Amit Malhotra

## HEADLINE

**Senior AI Systems Architect | LLM Infrastructure, Agent Reliability & Computer-Use Automation | Ex-Moody's Assistant Director, Ex-VP Santander, Ex-SME PNC Bank**

---

## ABOUT

Senior Systems and AI Solutions Architect with 21+ years of experience bridging enterprise financial systems, credit-risk modeling, and production Generative AI runtime infrastructure.

🔹 AI RUNTIME & AGENT INFRASTRUCTURE (AMTrix Solutions, 2022–Present):
Architecting production runtime infrastructure for LLMs and autonomous agents:
• Multi-Provider Gateways: Built a self-hosted gateway (Node.js, Express, SQLite) routing traffic across Vertex AI, Bedrock, OpenRouter, and local models.
• Streaming Tool Translation: Engineered an SSE accumulator translating non-Anthropic function calls into standard tool events for agent loops.
• Agent Execution Controls: Built AMTrix Plan, a Python harness with OS-level file locks, pre-tool checks, and automated test gates (700+ tests).
• Vision & Computer-Use Automation: Built a multimodal VLM desktop automation engine with a React zone mapper and state machine (28.6K audited actions).
• Local Inference & FastMCP: Deployed local inference on 64GB Apple Silicon via Ollama; built FastMCP servers with 10 tools optimizing context.

🔹 STRATEGIC BANKING CONSULTANCY & RISK ARCHITECTURE (2013–2022):
Delivered strategic advisory and technical leadership across major commercial banks:
• Santander Bank (2015): VP / Technical Manager for CCAR stress testing via Copal Amba / Moody's; automated Federal Reserve FR Y-14 reporting.
• PNC Bank (2014–2015): Wholesale PD SME prototyping T-SQL calculation engines across 4 commercial portfolios and building the Model Accuracy Testing platform.
• Synovus Bank (2013–2014): Strategic architect designing the Dual Risk Rating (DRR) data warehouse, unifying Basel II/CCAR integration across 30+ regional banks.
• AKM USA Trading: Built conversational AI bots, voice/chat task automation bots, and real-time market data ingestion engines.

🔹 ENTERPRISE PLATFORMS & CREDIT MODELING (Moody's Analytics, 2007–2013):
Progressed from software engineering to Assistant Director / Lead Systems Consultant:
• Led RiskAnalyst (RA) and RiskOrigin database configuration, schema design, and client strategic consulting across commercial banks.
• Fully automated Moody's internal flagship Credit Research Database (CRD) through T-SQL stored procedures and SSIS ETL pipelines.
• Engineered default detection software in C#/.NET and SQL Server integrating RiskCalc EDF models with global financial feeds.

Core Stack: Python (AsyncIO, FastMCP, Pytest), Node.js, SQL Server (T-SQL), Oracle (PL/SQL), C#/.NET, SQLite, PostgreSQL, Docker, Linux, Apple Silicon.

---

## EXPERIENCE

### AMTrix Solutions Inc.
**Founder & Principal AI Systems Architect** | April 2022 – Present | Hicksville, NY

Engineering practice delivering enterprise LLM runtime infrastructure, agentic execution controls, and automated data platforms.
• Built a self-hosted LLM gateway in Node.js, Express, and SQLite providing a common interface across Google Vertex AI, AWS Bedrock, OpenRouter, and local Ollama models.
• Developed a streaming Server-Sent Events (SSE) translation layer that reconstructs fragmented function-call chunks from non-Anthropic models into standard tool-call events for agent loops.
• Implemented multi-tiered cost controls including provider prompt caching, exact-match SQLite response caching, and request-level telemetry tracking token usage, cache hits, and estimated expense.
• Built AMTrix Plan, a Python coding-agent harness with OS-level file protections, pre-tool checks safeguarding uncommitted files, and automated test gates requiring passing test runs before tasks complete; covered by 700+ automated tests.
• Deployed local LLM inference on a 64GB Apple Silicon workstation using Ollama and GGUF quantized models, with Open WebUI access and remote connectivity over Tailscale.
• Built FastMCP servers exposing 10 tools for targeted file retrieval, structured schema compression, reference-based storage, and recovery from truncated model outputs.
• Vision-LLM Desktop Automation & Control: Built a multimodal VLM desktop automation engine for legacy applications without APIs, separating perception (VLM), decision (deterministic state machine), and verified execution across 28.6K audited actions over 270 live runs.
• Implemented deterministic validation pipelines that keep analytical calculations and risk formulas in deterministic code, using LLMs solely to articulate verified outputs.
• Built a multi-daemon data collection system that ingested and structured 9.8 million observations in SQL for inventory and restock analysis, using process locking and PID verification.

---

### AKM USA TRADING INC
**Technology Lead & AI Systems Architect** | 2018 – Present | Hicksville, NY

Trading operations and technology firm operating automated market-data ingestion, conversational automation, and execution systems.
• Designed and deployed natural language conversational interfaces and multi-persona voice/chat task automation bots connecting natural language user requests to backend APIs and trading feeds.
• Engineered real-time data ingestion engines, automated signal processors, and order execution interfaces connecting to financial exchange APIs.
• Automated data movement between live feeds, execution alerts, and transaction databases using Python and shell automation pipelines.

---

### Malhotra Enterprise Solutions LLC
**Principal Strategic Consultant & Database Architect** | 2013 – 2017 | Hicksville, NY

Delivered regulatory risk infrastructure, credit model implementations, and strategic data architecture for Tier-1 commercial banks.
• Santander Bank (Vice President, CCAR Engagement via Copal Amba / Moody's, 2015): Directed technical implementation for CCAR stress testing and RWA forecasting; engineered PL/SQL pipelines in Moody's RiskFoundation Oracle data warehouse and automated Federal Reserve FR Y-14 (A/M/Q) reporting submissions in RiskAuthority.
• PNC Bank (Wholesale PD Model SME, 2014 – 2015): Prototyped standalone T-SQL calculation engines across 4 commercial portfolios; designed the Model Implementation Accuracy Testing platform in SQL Server validating calculations across Baseline, Adverse, and Severely Adverse CCAR scenarios.
• Synovus Bank (Strategic Consultant, 2013 – 2014): Architected the enterprise Dual Risk Rating (DRR) data warehouse, unifying Basel II and CCAR risk-data integration and synchronizing obligor/facility ratings across a consortium of 30+ regional banks.

---

### Moody's Analytics
**Assistant Director / Lead Systems Consultant** | Jul 2007 – Nov 2013 | New York, NY

• Led database configuration, schema design, and technical integration for Moody's flagship RiskAnalyst (RA) and RiskOrigin credit platforms across commercial banking clients, advising client risk officers on financial spreading workflows.
• Redesigned, rewrote, and fully automated Moody's internal Credit Research Database (CRD) through T-SQL stored procedure optimization and SSIS ETL pipelines, removing manual processing bottlenecks.
• Engineered client/server default detection software in C#/.NET and SQL Server; integrated Moody’s proprietary RiskCalc EDF models with external financial data feeds (Compustat, WorldScope).
• Directed database migration from SQL Server 2000 to SQL Server 2008 and developed fault-tolerant backend data services supporting Moodys.com.

---

### Intelligent Search Technology
**Software Developer** | Jun 2005 – Jul 2007 | New York, NY

• Developed core fuzzy matching algorithms for the NameSearch® search engine in C/C++; built SDK integration libraries for Oracle, SQL Server, and .NET.

---

## EDUCATION

**Syracuse University**, L.C. Smith College of Engineering and Computer Science  
**Bachelor of Science (B.S.) in Computer Science**, Minor in Mathematics, 2005

---

## TOP RECRUITER SEARCH SKILLS

### Core Competencies
1. LLM Infrastructure & Runtime Gateways
2. Model Context Protocol (FastMCP)
3. Computer-Use & Vision-Language Model Automation
4. Agent Reliability & Guardrails
5. Tool Calling & Function Calling Translation
6. Credit Risk Modeling (PD, LGD, CCAR, Basel II/III)
7. Python (AsyncIO, FastMCP, Pytest)
8. Node.js & Express
9. Microsoft SQL Server & T-SQL Optimization
10. Oracle PL/SQL & SSIS ETL Architecture
