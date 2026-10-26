# Application Kit — Amit Malhotra

> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 02:35 UTC+4  
> **Status:** Final Approved  

**Contents:** 30-Second Elevator Pitch · 3 Tailored Cover Letter Variants · 4 Detailed STAR Stories · Strategic Phrasing Rules

---

## 1. THE 30-SECOND ELEVATOR PITCH

> "I am a Staff AI Systems Engineer and Forward Deployed Architect with 21+ years of systems and data engineering experience. I spent 6 years at Moody's Analytics rewriting and automating their flagship Credit Research Database (CRD), followed by enterprise credit risk consulting across Tier-1 banks (PNC, Santander). From 2018 onward at AKM USA TRADING INC (C-Corp), I engineered real-time data ingestion pipelines, automated trading signal execution interfaces, and conversational task automation bots. Since April 2022, under AMTrix Solutions Inc. (C-Corp), I have architected production-grade Generative AI runtime infrastructure: self-hosted multi-provider LLM gateways that run agentic workflows across Google Vertex AI, AWS Bedrock, and local models with prompt caching and cost telemetry; zero-dependency agent governance harnesses (~23K lines Python stdlib, 700+ tests) with OS-level file locks and verification gates; FastMCP servers; and private on-prem 30B inference nodes on Apple Silicon. I combine institutional database rigor with hands-on AI systems engineering to ensure AI agents run reliably in production."

---

## 2. COVER LETTER TEMPLATES

### Master Opening (All Variants)

Dear [Hiring Manager / Team Lead],

I am writing to express my strong interest in the [Role Title] position. I am a hardcore systems and data engineer with 21+ years of experience designing, implementing, and deploying mission-critical software, enterprise database platforms, and production Generative AI infrastructure. 

Throughout my career—from automating Moody's Analytics' flagship Credit Research Database (CRD) and engineering wholesale PD model execution platforms for PNC Bank, to deploying real-time market data ingestion and trading automation at AKM USA TRADING INC (C-Corp) (2018–Present)—I have focused on building resilient systems where mathematical precision, low latency, and runtime reliability are paramount. Since April 2022, at AMTrix Solutions Inc. (C-Corp), I have applied this engineering discipline to Generative AI runtime systems and autonomous agent reliability.

---

### Variant A — Enterprise AI Platform (Banks, FinTech, & Large Software Systems)

Your organization is deploying coding agents and LLM applications across distributed teams and requires robust cost engineering, granular auditability, and independence from cloud vendor lock-in. I have engineered production solutions addressing each of these challenges:

- **Multi-Provider LLM Gateway Architecture**: Engineered Claude Code Center, a self-hosted high-throughput proxy (Node.js, Express, SQLite) routing agent traffic across Google Vertex AI (Gemini, Claude rawPredict, Model-as-a-Service third-party models), AWS Bedrock, OpenRouter, and local Ollama.
- **Streaming Tool Translation**: Developed a streaming Server-Sent Events (SSE) accumulator translating fragmented function-call chunks into uniform Anthropic tool blocks, allowing non-Anthropic models to reliably execute agentic tool loops.
- **Cost Engineering & Telemetry**: Implemented multi-tiered cost controls including 1-hour prompt-cache injection, Vertex explicit context caching, and SQLite exact-match caching, coupled with real-time HUD telemetry tracking token spend and cache hit ratios.
- **Agent Governance & Safety Harness (AMTrix Plan)**: Architected a zero-dependency governance framework (~23K lines Python stdlib, 700+ unit tests) enforcing OS-level read-only file locks, pre-tool hooks preventing uncommitted data loss, and automated test-passing verification gates before tasks are marked complete. An audit ledger maps ~190 operating rules directly to enforcing code modules for compliance and SOC 2 / Model Risk reviews.

---

### Variant B — AI-Native Fast-Moving Product Teams (Forward Deployed Engineer)

You need an engineer who can embed within customer workflows, diagnose complex integration and runtime failures rapidly, and ship production-ready fixes without destabilizing existing infrastructure:

- **High-Throughput Event Daemons**: Engineered a fault-tolerant multi-daemon event harvesting platform featuring a lock-elected singleton architecture and PID-verified registries, ingesting and analyzing 9.8M observations in SQL for inventory and restock prediction.
- **Model Context Protocol (FastMCP) Servers**: Shipped custom multi-model MCP servers (FastMCP, Python) with 10 tools optimizing IDE agent context windows through pass-by-path file loading, schema-bound JSON compression, and automated anti-truncation recovery loops.
- **Deterministic AI Execution Pipelines**: Designed "compute, then narrate" rule engines where deterministic code calculates complex formulas and risk invariants, using the LLM solely to explain verified mathematical results without hallucination risk.
- **Modular Architecture**: Built modular, plug-and-play components with dedicated test harnesses, ensuring seamless deployment and integration across heterogeneous environments.

---

### Variant C — 1099 / High-Impact Advisory & Systems Consulting

If your team faces pressing operational hurdles—such as agents overwriting code, escalating LLM inference costs, sensitive data that cannot leave internal networks, or legacy systems requiring automated interfaces—I can scope and deliver contained, measurable solutions:

- **Private On-Prem AI Nodes**: Deployed private inference workstations on 64GB Apple Silicon running 30B parameter models (Qwen3, Llama 3.1) at 256K context via GGUF quantization, Ollama, Open WebUI, and SearxNG private search over Tailscale, reducing development inference costs to $0.
- **Secure Event & Notification Bus**: Architected self-hosted notification buses behind Caddy TLS with deny-by-default access control lists and automated failover.
- **Disciplined Execution Protocol**: Every engagement proceeds through documented, approved plans, pre-edit backups, and verified test-suite execution.

---

### Master Closing (All Variants)

With a foundation built on 21+ years of mission-critical systems engineering, I approach modern AI agent development with institutional rigor, comprehensive test automation, and complete auditability. I would welcome the opportunity to discuss how my systems background and AI runtime architectures can accelerate your team's initiatives.

Sincerely,  
**Amit Malhotra**  
Hicksville, NY 11801 | (917) 345-7516 | amit.malhotra1@gmail.com | github.com/amit-malhotra1

---

## 3. FOUR DETAILED STAR STORIES

### Story 1: Preventing Uncommitted Code Corruption (AMTrix Plan Governance Harness)
- **Situation**: During intensive agentic development sessions, autonomous coding agents would periodically overwrite uncommitted files, hallucinate task completion, or mark tasks "done" while unit tests were failing.
- **Task**: Eliminate agent-induced data loss and task drift by construction through code enforcement rather than relying on LLM prompt instructions.
- **Action**: Architected AMTrix Plan, a zero-dependency agent safety harness (~23K lines Python stdlib, 700+ unit tests). Implemented:
  1. A `PreToolUse` hook that verifies the active iteration status and creates timestamped file backups before any write/edit tool is permitted to execute.
  2. OS-level read-only file locks on completed artifacts and ledger entries.
  3. Strict pre-commit gates blocking staged secrets and requiring automated test execution to pass before an iteration can be finalized.
- **Result**: Completely eliminated accidental code overwrites across all production repositories. Established full audit traceability mapping ~190 operating rules to concrete code implementations.

---

### Story 2: Cross-Provider Function Calling for Coding Agents (Claude Code Center)
- **Situation**: Coding agents such as Claude Code were tied to a single proprietary provider subscription, causing vulnerability to vendor rate limits and preventing access to specialized third-party or open-weights models.
- **Task**: Translate multi-provider streaming responses transparently so Claude Code could run across Google Vertex AI (including third-party MaaS models), AWS Bedrock, OpenRouter, and local Ollama without loop disruption.
- **Action**: Developed a self-hosted high-throughput proxy in Node.js, Express, and SQLite. Engineered a streaming Server-Sent Events (SSE) accumulator that reconstitutes fragmented function-call arguments and reasoning signatures into uniform Anthropic tool blocks. Layered dynamic per-model registry flags, 1-hour prompt-cache injection, and exact-match SQLite caching with real-time HUD cost telemetry.
- **Result**: Enabled zero-vendor-lock-in execution of autonomous coding loops across multiple cloud providers and local private inference nodes on owned billing, delivering substantial cost efficiency.

---

### Story 3: Rebuilding Moody's Flagship Credit Research Database (CRD Automation)
- **Situation**: Moody's Analytics' internal flagship Credit Research Database (CRD) suffered from manual operational bottlenecks, lengthy processing windows, and escalating data volume challenges across global financial datasets.
- **Task**: Re-architect and automate the database platform to eliminate manual interventions, optimize query execution, and ensure data integrity for downstream default scoring engines (RiskCalc).
- **Action**: Redesigned database schemas, authored high-performance T-SQL stored procedures, and designed automated SSIS ETL pipelines. Engineered a client/server default detection platform in C#/.NET and SQL Server, integrating RiskCalc Expected Default Frequency (EDF) scoring models with external financial data feeds (Compustat, WorldScope).
- **Result**: Fully automated the CRD data pipeline, eliminating manual operational bottlenecks, accelerating processing throughput by multiples, and ensuring flawless data feed reliability for Tier-1 banking clients.

---

### Story 4: Standalone T-SQL PD Calculation Engines for PNC Bank Wholesale Portfolios
- **Situation**: PNC Bank required wholesale Probability of Default (PD) model implementations across 4 commercial portfolios (Small Business, FI Insurance, Commercial Real Estate, and Middle Market) across 3 distinct use cases: Credit Appraisal, Regulatory Capital, and Stress Testing.
- **Task**: Architect and validate standalone prototype calculation engines that executed the entire credit modeling pipeline—from raw financial statement spreading to ratio calculations, non-linear score transformations, warning overrides, and final PD outputs.
- **Action**: Authored standalone T-SQL prototype calculation engines replicating complete credit risk model specifications. Designed and deployed the Model Implementation Accuracy Testing platform in SQL Server, validating intermediate ratios, warning overrides, and regulatory capital rules under Baseline, Adverse, and Severely Adverse CCAR stress scenarios.
- **Result**: Delivered 100% mathematical accuracy across all 4 commercial portfolios, providing the definitive benchmark for the bank's production Rating Platform and regulatory compliance audits.

---

## 4. STRATEGIC PHRASING & TERMINOLOGY STANDARDS

| Standardized Term | Deprecated / Avoided Term | Rationale |
|---|---|---|
| **AMTrix Plan** | AMX | Brand clarity and consistency |
| **Generative AI Runtime Infrastructure** | Prompt Engineering | Emphasizes systems engineering, proxy architecture, and governance |
| **Vision-Driven UI Automation** | Autonomous Trader / Bot | Focuses on computer vision and deterministic state execution |
| **Automated Availability & Harvesting Daemons** | Bot Protection Bypassing | Highlights distributed data ingestion and singleton architectures |
| **Multi-Provider LLM Gateway** | Reverse Proxy Wrapper | Highlights dynamic model routing, SSE translation, and prompt caching |
| **Hook-Enforced Guardrails & Gates** | AI Sandbox | Accurate systems terminology; hooks enforce concrete preconditions |
| **Deterministic Pipelines ("Compute, Then Narrate")** | Prompt Chains | Emphasizes mathematical verification before LLM summarization |
