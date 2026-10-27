# Project Expertise Analysis — Forward Deployed AI Engineer Positioning
> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 00:00 UTC+4  
> **Status:** Baseline
**Prepared:** 2026-10-25 · **Scope:** 24 projects in `~/Documents/GitHub` (excluded: anything named TEST / DEMO / outputs / spoofing / boilerplate / crawler, `jev-trader-demo`, pre-2023 bots, `open-webui`/`cors-anywhere` clones)
**Basis:** READMEs, CLAUDE.md files, dependency manifests, git history. These are documented claims. The metrics flagged in §6 have to be measured before they go on a resume.

---

## 1. The Short Version: Who These Projects Show You Are

Across 14 months the projects follow one line of work: **making LLMs reliable enough to put in production.** You started with prompts (PromptForge, Sep 2025). You quickly saw that prompts alone don't scale. From there you built, in order:

1. **Private infrastructure**: self-hosted models, Docker, local RAG.
2. **Context engineering**: compression, cross-project memory sync, context compilers.
3. **An LLM gateway**: routing, prompt-cache injection, cost telemetry across 5 providers.
4. **Agent governance**: hooks, backups before every edit, plan-before-edit, measured evidence, audit trails, human approval gates.

That is the work a **Forward Deployed Engineer** does in 2026. They go into a company that has bought Claude/Codex/Gemini seats, find out why agents hallucinate, lose work, overspend or stall, and build the harness that fixes it. Your repos are that harness, built for yourself first.

**Recommended headline:**
> **Forward Deployed AI Engineer — Agent Reliability, LLM Gateways & Context Engineering**
> 21+ years of enterprise data/technology (ex-Moody's) + since 2025 full-time building AI-agent infrastructure.

---

## 2. Six Expertise Pillars (Non-Overlapping)

Each project belongs to exactly **one** pillar, so the resume never says the same thing twice.

| # | Pillar | Flagship (lead with) | Supporting |
|---|---|---|---|
| P1 | **Agent Governance & Human-in-the-Loop** | AMTrix Plan Standard (`amtrix-impl-plan-standards`) | Frontier Triage Engine, Patch TUI, Subscription Tool |
| P2 | **LLM Gateway, Routing & Cost Engineering** | Claude Code Center | Universal Router / MCP Proxy, Kimi K2.5 MCP Server |
| P3 | **Context Engineering & Agent Memory** | AMTrix Core + Nexus Protocol | AI Context Compressor (Python+Rust), AGENT_PROTOCOL |
| P4 | **Multimodal & Vision Agents** | Vision LLM Decision Agent | Vision Agents Builder, SmartBrain (Alexa), VoiceBus TTS |
| P5 | **Event-Driven Signals & Real-Time Monitoring** | Retail Availability Intelligence (iPhone v3) | VoiceBus event bus, Notify-Bus (self-hosted push) |
| P6 | **Platform, Full-Stack & Private AI Infra** | AMTrix Studio (MCP control plane) | Ollama Powerhouse, PromptForge, Identity Engine, ReactTSApp, AI Companion Toolkit |

---

## 3. Project-by-Project Analysis

Format per project: **Objective → Technology → What it proves → Value to a company.** Display names are written for the resume; the repo name is in brackets.

### P1 — Agent Governance & Human-in-the-Loop *(newest and strongest work: Sep–Oct 2026)*

#### 1.1 AMTrix Plan — Drop-in Governance Standard for AI Coding Agents `[amtrix-impl-plan-standards]` ★ FLAGSHIP
- **Objective:** A single folder you drop into any repo. From then on every AI model there (Claude Code, Codex, Gemini) resumes where the last session stopped, records each session the same way, backs up before editing, and proves its work with measured tests.
- **Technology:** Python (stdlib, unittest), Claude Code / Codex / Gemini **hooks** (`.claude/settings.json`, `.codex/hooks.json`), slash-command skills, git pre-commit secret scanning, append-only versioned logs, generated dashboards (CODE_MAP, FILE_INDEX, TEST_MAP), a reviewer-model review cycle, cross-repo deployment (`check_clients.sh`), an installer with a help system.
- **Scale:** **365 commits in 22 days** (Oct 1–22, 2026), versions v0.1 → v0.44, already deployed in AMTrix-core and iPhone v3.
- **What it proves:** Systems thinking about **agent failure modes**: amnesia between sessions, silent overwrites, unverifiable "done" claims, scope creep. You treat the AI agent as an untrusted junior engineer and build the process around it in code, not in prompts. The idea that "the count and time are measured by `finish`, never typed" is a strong anti-hallucination principle.
- **Value:** Enterprises rolling out coding agents to hundreds of developers need **auditability, reproducibility and rollback**. This is a working reference implementation of an "agent SDLC": plan → approve → backup → edit → measured test → append-only record → handoff. It maps directly onto SOC 2 change management, model-risk audit trails and the AI-governance programs companies are building in 2026.

#### 1.2 Frontier Triage Engine — Audited, Cost-Gated Model Dispatch `[frontier-triage-engine]`
- **Objective:** Every paid frontier-model call is reproducible, classified, audited and approved by a human before it is sent.
- **Technology:** Python, OpenRouter. The payload is serialized **once** and its **SHA-256** is recorded, and the exact same bytes are transmitted. Responses are classified as `COMPLETE | PARTIAL | FAILED | UNKNOWN` (`finish_reason=length` → PARTIAL, timeout → UNKNOWN). The audit tracer uses monotonic attempt IDs under a FileLock, atomic fsync writes and recursive secret redaction. A zero-token **AST indexer** handles code context, there is a pre-flight cost card with a y/N gate, a fully offline test suite, and a deploy-to-project script.
- **What it proves:** Reliability-engineering habits from regulated industries: idempotency, byte-level reproducibility, explicit handling of truncated or partial LLM output, which most teams silently ignore.
- **Value:** Model-risk management (banks, insurers, ratings agencies) needs "what exactly did we send, what came back, who approved the spend." This is that, in about 16 Python modules.

#### 1.3 Patch TUI — Manifest-Based Surgical Patching `[AMTRIX-TOOLS/AMTRIX-Patch-TUI]`
- **Objective:** Apply only the exact edits an LLM proposes, declared in a JSON manifest. Never rewrite whole files.
- **Technology:** Validates the manifest, shows the plan with hashes and a unified diff, then writes a **versioned sibling file** (`proxy_server.js → proxy_server_v2.4.8.js`). The original is never touched.
- **Value:** Fixes the #1 complaint about AI code edits: silent truncation and collateral damage.

#### 1.4 Mode-Scoped Agent Launcher `[AMTRIX-TOOLS/amtrix_claude_subscription_tool]`
- **Objective:** A launcher for Claude Max/Opus sessions with explicit operating modes: `/discuss`, `/research`, `/makeplan`, `/implement`, `/verify`, `/catchup`, `/wrapup`, `/diagnose`.
- **Technology:** Claude Code hooks, a **scope guard** that blocks edits outside the allowed paths (live-verified 2026-10-04), a 3-hypothesis debugger (ranks causes by file + function + mechanism, stops for approval, then makes the smallest fix and runs the tests), and an evidence-stamping wrap-up script (Node `.cjs`).
- **Value:** A deployable pattern for **bounded autonomy**: agents that know which mode they are in and cannot drift out of it.

---

### P2 — LLM Gateway, Routing & Cost Engineering

#### 2.1 Claude Code Center — LLM Gateway & Prompt-Cache Router `[claude-code-center]` ★ FLAGSHIP
- **Objective:** A local gateway in front of the Claude Code CLI (and other Anthropic clients) that routes across providers, injects prompt caching and makes token spend visible.
- **Technology:** Node/Express proxy with modular handlers (routing, cache, db, hud), **schema translation** between the Anthropic, OpenRouter, Google Vertex (service-account BYOK) and Ollama formats, **Anthropic prompt-cache injection with 1-hour TTL**, a **SQLite exact-match response cache**, warm-bundle session continuity, a multi-terminal **cost/telemetry HUD**, JSON work profiles (Quick Fix / Deep Work / Clean Slate), a Bash TUI and launcher. 14+ models. 97 commits (Mar–Oct 2026).
- **What it proves:** You understand LLM economics at the protocol level: cache breakpoints, TTLs, payload shapes, provider differences. Most engineers only use an SDK.
- **Value:** Every company with large Claude/agent bills needs an **AI gateway**: central routing, caching, per-team cost attribution, provider failover. README claims a **40–90% cost reduction** (⚠ measure from `proxy.db` before citing, see §6).
- ⚠ **Leave off the resume:** the IDE-binary patching / auth-override layer (`antigravity/patch_ide.sh`). It can read as ToS circumvention. Describe it only as "IDE traffic routing through a local gateway", if at all.

#### 2.2 Universal Router & MCP Proxy `[complex-amtrix-engineered-prompts-v1/START_MCP_PROXY, UNIVERSAL_ROUTER_GUIDE]`
- One `context` command routes any prompt to Gemini, local Llama, OpenRouter or Anthropic, through a central logging proxy or directly. Global config with per-project overlays (`.agent/models.json`).
- **Value:** Provider-agnostic AI access with central logging. This is the seed of 2.1, so present it as part of 2.1's story, not as a separate bullet.

#### 2.3 Universal MCP Analysis Server — Multi-Pipeline Analysis Server `[Manoj_Project/0150_MCP_SERVER_DEMO]` *(my own build; the folder name is historical)*
- **Objective:** Expose Kimi K2.5 to an IDE agent through **MCP**, with 5 pipelines: deep_analysis, quick_summary, code_review, drill_down, continue.
- **Key design:** The IDE passes **file paths only** and the server loads the contents, so the main agent's context never bloats. It also has anti-truncation with a `continue` pipeline, structured JSON output, and the Frontier Triage Engine embedded.
- **Value:** This is literally forward-deployed work: building a custom MCP server for someone else's stack. **Your strongest FDE proof, if you are allowed to cite it** (see §7, Q1).

---

### P3 — Context Engineering & Agent Memory

#### 3.1 AMTrix Core — Agent Skill Library & Con