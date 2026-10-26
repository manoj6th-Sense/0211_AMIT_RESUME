# AMIT MALHOTRA
> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 00:00 UTC+4  
> **Status:** Baseline
**Hicksville, NY 11801 | (917) 345-7516 | amit.malhotra1@gmail.com | github.com/amit-malhotra1**

**Forward Deployed AI Engineer — Agent Reliability · LLM Gateways · Private AI · Context Engineering**

---

## PROFESSIONAL SUMMARY

AI engineer with **21+ years in enterprise technology**: 15 years in credit-risk data platforms and model validation (Moody's Analytics, Fortune 500 banks), and, since 2025, **full-time building AI-agent infrastructure** (20+ shipped tools and platforms). I built:

- A vendor-independent LLM gateway that runs the Claude Code agent on Google Vertex AI (including third-party models), AWS Bedrock, OpenRouter or local models.
- A drop-in governance standard that makes AI coding agents resume, back up, stay in scope and prove their work.
- MCP servers, a private AI platform on Apple Silicon, and deterministic "compute, then narrate" engines.

I get into the details of a complex process, break it into **lightweight, portable, plug-and-play modules**, and rebuild it so it is simple to use. Every failure becomes a rule enforced by code.

---

## TECHNICAL SKILLS

**AI & Agents:** Claude Code (hooks, skills, commands), Codex, Gemini CLI, Model Context Protocol, multi-agent orchestration, vision-language models, prompt caching, context engineering, RAG, agent test harnesses
**Model Platforms:** Anthropic API, Google Vertex AI (incl. Model-as-a-Service), AWS Bedrock (Converse), OpenRouter (BYOK)
**Private AI:** Ollama, Open WebUI, SearxNG, GGUF quantized models (Qwen3, Llama, LLaVA), Apple Silicon inference, Tailscale
**Languages:** Python, TypeScript / Node.js, Bash, SQL (T-SQL, PL/SQL), Rust, Swift, C# / .NET
**Data & Back End:** Express, SQLite, PostgreSQL (Drizzle), SQL Server, Oracle, Sybase, SSIS, data-warehouse design, JSON / XML schema
**Infrastructure & UI:** Docker Compose, Caddy, ntfy, Telegram Bot API, GCP OAuth2, git hooks, React, Vite, Mermaid, SVG, terminal UIs
**Risk Domain:** Basel II/III IRB, CCAR, FR Y-14, PD/LGD/EAD, RWA, model implementation testing

---

## PROFESSIONAL EXPERIENCE

### AMTrix SOLUTIONS INC. — Founder & AI Systems Engineer
**April 2022 – Present**

Design and build AI-agent infrastructure and consult on AI integration for mid-market and small-business clients.

- **Claude Code Center: LLM gateway** (Node.js, Express, SQLite; 97 commits)
  - Proxy that runs the Claude Code agent against Vertex AI: Claude via `rawPredict` with verified 1-hour caching, Gemini natively, and third-party Kimi K2 / DeepSeek through Vertex MaaS. Also routes to Bedrock, OpenRouter BYOK and a $0 local tier.
  - Built an SSE accumulator that rebuilds streamed tool calls, so the agent's tool loop works on non-Anthropic models.
  - Prompt-cache injection, Vertex `cachedContents`, a SQLite response cache, and a per-request cost HUD.
- **AMTrix Plan: agent governance standard** (Python, Claude Code / Codex / Gemini hooks; 365 commits in 22 days)
  - A drop-in folder that gives any repository automatic session resume, backup before edit, versioned plan records and human approval gates.
  - Test results recorded by code, a reviewer-model audit, pre-commit secret scanning, and one-command updates of every installed project.
- **Private AI platform** (Ollama, Open WebUI, Docker, Tailscale)
  - 30B mixture-of-experts models (Qwen3-Coder, Qwen3 Thinking) as quantized GGUF with 128K–192K context on a 64 GB Apple Silicon workstation.
  - My own Open WebUI assistant combining local models and cloud APIs, with SearxNG private search, a dual-machine setup and self-healing operations.
- **Universal MCP analysis server** (Python, MCP, Bedrock, OpenRouter)
  - 10 tools for IDE agents, model-agnostic. Pass-by-path loading keeps code out of the agent's context.
  - Automatic continuation of truncated output (up to ~60K tokens), raw-output storage with drill-down, and a fallback client built only on the standard library.
- **Frontier Triage Engine**
  - Byte-exact SHA-256-hashed model requests, with responses classed COMPLETE / PARTIAL / FAILED / UNKNOWN.
  - File-locked append-only audit trail with secret redaction, and a human cost gate before every paid call.
- **Vision LLM decision agent** (Python; perception / decision / action modules)
  - VLM screen perception feeding a deterministic P0–P4 priority policy, with verified actions.
  - Token budgeting for 4–5-hour unattended sessions.
- **Computational ephemeris & multi-factor scoring engine**
  - Swiss Ephemeris astronomy, coordinate transforms, modular-arithmetic projections and weighted scoring matrices.
  - Strict schema-validated evidence for LLM interpretation; 9 regression and invariant test suites.
- **Context-engineering stack**
  - Agent Protocol (on-disk memory vault, multi-provider router, payload capture), AMTrix Core (atomic skills, composed workflows, Context Compiler) and an AI Context Compressor (Python + Rust).
- **Real-time systems**
  - Availability intelligence platform covering 30+ locations from 4 anchors, with Telegram / ntfy / desktop alerting.
  - Agent event bus with JSON-Schema validation and text-to-speech (TypeScript).
- **Earlier builds:** PromptForge (version-controlled IDE for LLM instruction sets, React/TS), SmartBrain multi-agent voice assistant (Alexa, Gemini), AMTrix Studio MCP control plane, Mermaid dashboard generator, Identity Engine brand-kit generator and drop-in theming layer.

### AKM USA TRADING INC. — Principal / Technology Lead
**2017 – April 2022**
- Ran trading operations with periodic technology projects: conversational chatbots, voice/chat automation, mobile integration, API orchestration.
- Developed a Credit Booster application drawing on credit-risk expertise.

### MALHOTRA ENTERPRISE SOLUTIONS LLC — Lead Consultant
**November 2013 – 2017**
- **Major Regional Bank:** implemented wholesale PD models (Small Business, FI Insurance, CRE) on a new risk-rating platform. Built a modular SQL Server model-implementation accuracy-testing platform and CCAR stress scenarios. Led SIT defect and root-cause analysis.
- **Regional Banking Consortium (30+ banks):** delivered Basel II/CCAR reporting integration and designed a Dual Risk Rating data warehouse integrated with loan accounting.
- **Financial Consulting Firm:** managed AML software development (Agile).

### COPAL AMBA (A MOODY'S ANALYTICS COMPANY) — Vice President
**May 2015 – November 2015**
- Managed RWA calculation and forecasting architecture for CCAR at a major international bank.
- Designed FR Y-14 (A/M/Q) reports in Moody's RiskAuthority. Won repeat business after the executive presentation.

### MOODY'S ANALYTICS — Assistant Director / Lead Consultant
**July 2007 – November 2013**
- Led RiskAnalyst / RiskOrigin implementations for Fortune 500 financial institutions.
- Built a modular BI platform for Basel II/CCAR model validation.
- Fully automated the Credit Research Database pipeline, led the SQL Server 2000 → 2008 migration, built RiskCalc (EDF/PD) scoring integrations, and helped extend EDF scoring to additional countries.

### INTELLIGENT SEARCH TECHNOLOGY — Software Developer
**June 2005 – July 2007**
- Built fuzzy matching on the NameSearch® engine and platform-independent address extraction (C/C#), plus SDKs for Oracle, SQL Server, .NET and PHP.

---

## EDUCATION

**Syracuse University**, L.C. Smith College of Engineering and Computer Science
B.S. Computer Science, Minor in Mathematics, 2005

---

## HOW I WORK

| Principle | In practice |
|---|---|
| **Understand deeply, then simplify** | Map the whole process, break it into small testable pieces, give the user one simple surface |
| **Lego architecture** | Lightweight, portable, plug-and-play modules reused across every active project |
| **Determinism over cleverness** | Lookup policies, hashed requests, "compute, then narrate" |
| **Measured, not claimed** | Results recorded by code, never typed by a model |
| **Failures become code** | Friction logs turn into rules enforced by hooks and tests |
| **Visual-first** | Mermaid architecture diagrams and visual dashboards for fast learning and clear handoff |

*A detailed project profile is available on request (AMIT_MALHOTRA_FDE_PROFILE_2026).*