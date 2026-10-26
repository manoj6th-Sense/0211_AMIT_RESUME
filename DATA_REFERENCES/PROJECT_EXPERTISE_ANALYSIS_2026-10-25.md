# Project Expertise Analysis — Forward Deployed AI Engineer Positioning
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

#### 3.1 AMTrix Core — Agent Skill Library & Context Compiler `[AMTrix-core]` ★
- **Objective:** Solve "LLMs forget instructions after 5–10 turns, hallucinate, and long system prompts collapse" by replacing monolithic prompts with **atomic, composable skills** and a compiled context.
- **Technology:** Python tooling, a Bash hub, native IDE **Mono-Skill** (`/amtrix INIT`, `/amtrix DEBUG`), the **Context Compiler** (`amtrix_context_trail.py`), which merges the latest SPEC + TASK + FRICTION files ("the Triad") with the core prompt into one `LATEST_CONTEXT.md` that any fresh model can pick up. Named agentic workflows (`safe_build` = DNA+RULES+GUARD+FEATURE+TEST+DIFF, `safe_cleanup`, `project_onboard`). 56 commits (Feb–Oct 2026); now governed by AMTrix Plan.
- **What it proves:** You independently arrived at the patterns the industry later standardized: Agent Skills, AGENTS.md, compiled context handoff.
- **Value:** Teams moving between models and tools (Claude ↔ Codex ↔ Gemini) need **portable, model-agnostic context**. This is that layer.

#### 3.2 Nexus Protocol & Brain Sync — Cross-Project Agent Protocol Distribution `[complex-amtrix-engineered-prompts-v1 + AGENT_PROTOCOL]` *(merge into one entry)*
- **Objective:** One versioned agent protocol (`.ai/` v6.0, `.agent` v19.4 "Hardened") that is **propagated automatically to every project**: sync all, deploy to one, update all, deploy to any external path, global symlink.
- **Technology:** XML/Markdown protocol files with an immutable `_CORE/`, a master index (`_MASTER_NEXUS_INDEX.xml`), BRAIN_SYNC launcher scripts, a Python stress-test suite, a Mermaid/SVG visual prompt dashboard, and IDE rulebooks (`.antigravityrules`, `.antigravityignore`).
- **Also inside:** AICEO Factory, a hierarchical persona-alignment framework (CEO → CTO → CFO → … agents trained from one aligned "executive" persona, with onboarding tests, correction logs and promotion criteria). **Reword for the resume** as "hierarchical multi-agent role orchestration with alignment testing"; avoid "CEO clone".
- **Value:** Fleet-wide policy distribution for agents: change the rule once and every repo gets it. Enterprises need exactly this for agent policy rollout.

#### 3.3 AI Context Compressor (Python + Rust) `[ai-context-compressor-v1]`
- **Objective:** Keep the intent of long AI transcripts while cutting tokens, without lossy summarization.
- **Technology:** A 3-phase pipeline: **Time-Travel Dedup** (collapses code blocks that are >80% similar), **Holographic Scan** (strips boilerplate lines that appear in >10% of messages), and **The Codex** (n-gram mining → shortcode dictionary). Rust efficiency engine, a self-learning format-recon mode, and an output format of its own (`.toon`). 25 commits (Jan 2026).
- **Value:** Long-running agents, call-center transcript analysis, chat-history handoff. It compresses by removing redundancy rather than rewriting.

---

### P4 — Multimodal & Vision Agents

#### 4.1 Vision LLM Decision Agent `[complex-amtrix-engineered-prompts-v1/VISION_LLM_COMET_TRADER; backup copy BACKUP_VISION_LLM_COMET_TRADER]` ★ (you said to emphasize this one)
- **Objective:** A vision-language model watches a live chart UI (screenshots), interprets the state and runs a rule-based policy over a **4–5-hour unattended session**.
- **Technology:** About 700 Python files including a local autotrader engine (v11.9 → v12.9 "very stable"), action verifier, click-to-capture, cartridge manager (swappable strategy modules), asset-manifest generator and config audit. Versioned XML system protocols (v3.2 → v3.9.5), and a written **feasibility analysis** and **LLM session-management deep dive** that budgets tokens per screenshot (~1.5K) against the context window over long sessions.
- **Distinctive engineering:** The **priority lookup-table policy**: P0 risk override → P1 movement type (cached at entry) → P2 stop rules → P3 counter-signal (immediate exit, overrides P2) → P4 profit protection. In your words: "the LLM doesn't *think*, it follows a lookup table." Faster, consistent, deterministic, memory-efficient. You split **perception (VLM)** from **decision (deterministic rules)** and **action (verified)**, which is the correct architecture for computer-use agents.
- **Value (Oct 2026):** Computer-use and vision agents are mainstream now, but enterprises hesitate because the agents are nondeterministic. Your pattern of VLM perception → deterministic policy table → action verification → session budgeting is directly reusable for **legacy-UI automation (systems with no API), visual QA, ops-dashboard monitoring and document/screen triage.**
- **Resume framing:** Lead with "real-time visual decision agent". Mention trading as the domain only. **No P&L claims.**

#### 4.2 Vision Agents Builder `[vision-agents-builder-v1]`
- A versioned Bash/YAML scaffolding generator (builder v32 → v42) for vision-agent projects. Fold it into 4.1 as "built a project generator for vision agents". *(Contents not deeply verified.)*

#### 4.3 SmartBrain — Voice Multi-Agent Hub `[custom-alexa-skills/SmartBrain]`
- An Alexa skill running Gemini 2.5 multi-agent routing on Node.js, with session memory (last 4 exchanges) and **portable deployment** (the same code runs on Alexa Hosted, AWS Lambda, GCP Cloud Functions or local Ollama), plus dual-mode secrets (env var → config fallback).
- **Value:** Voice-channel agents with cloud portability. An existing analysis is already in `DATA_REFERENCES/SmartBrain_Analysis.md`.

---

### P5 — Event-Driven Signals & Real-Time Monitoring

#### 5.1 Real-Time Retail Availability Intelligence Platform `[iphone-inventory-checker-v2 → v3]` ★ (most recent, active yesterday)
- **Objective:** Monitor product availability across 30+ retail locations in real time and send actionable alerts within seconds.
- **Technology:** Python backend + web cockpit (port 8200), a **multi-channel alert engine** (Telegram bot with rich HTML and inline action buttons, a self-hosted **ntfy** behind HTTPS with ntfy.sh failover, native macOS notifications), channel toggles that apply without a restart, hot-swappable device profiles, and multiple concurrent checkers on separate ports. Swift components. 62 commits (Dec 2025–Oct 2026). It runs **under the AMTrix Plan governance standard**, so it is your proof that the standard works on a real product.
- **Distinctive engineering:** **Geographic coverage optimization**: 4 anchor ZIP codes cover 30+ stores in 6 states with 9 queries, with no third-party data providers. That is an optimization and set-cover problem solved by hand.
- **Resume framing:** "Real-time availability intelligence & multi-channel alerting platform". Don't mention Apple bypasses or scraping. Leave out the README's "unicorn bypass parser" wording.
- **Value:** The same architecture serves supply-chain stock alerts, price or SLA monitoring, and ops incident paging.

#### 5.2 AMTrix Signal Layer — Agent Event Bus, TTS & Self-Hosted Push `[amtrix-voicebus + AMTRIX-TOOLS/amtrix-notify-bus]` *(merge into one entry)*
- **VoiceBus:** TypeScript. AI agents publish **JSON-Schema-validated events** (ajv). The bus routes them by **security policy** to desktop notifications or TTS, with per-agent voice profiles, `external_delivery: disabled` by default, a file watcher (chokidar), an Express API, a CLI (`doctor`, `publish`, `play`, `stop`) and vitest tests.
- **Notify-Bus:** Docker Compose + Caddy (automatic TLS) self-hosted push server with Linux and macOS clients.
- **Value:** **Human-in-the-loop at a distance.** An agent finishes, fails or needs approval, and the human is paged on their phone with action buttons. Long-running autonomous agents need exactly this channel.

---

### P6 — Platform, Full-Stack & Private AI Infrastructure

| Display name `[repo]` | What it is | Tech | What it proves |
|---|---|---|---|
| **AMTrix Studio — MCP Control Plane** `[amtrix-studio]` | Web control panel to run MCP servers (5 tools: read/write/list/search/autonomous task), multi-provider routing, local vector-memory RAG | Python, Textual/Rich TUI, YAML, HTML/CSS | Early MCP adoption (Dec 2025); agent tool-server operations |
| **Private LLM Stack** `[ollama-powerhouse-openwebui-docker-v1]` | Self-hosted Ollama + Open WebUI + SearxNG (private web-search RAG), dual-machine (Mac + Ubuntu) setup, Watchtower updates, port-conflict self-healing, volume-safe maintenance | Docker Compose, Bash, Python | On-prem / air-gapped AI for privacy-sensitive clients |
| **PromptForge — Prompts-as-Code IDE** `[PromptForge-The-Prompt-IDE-v1.9.7]` | 3-panel IDE; prompts are projects of components with `INSERT` includes, `DYNAMIC_RULE`/`CASE` conditional assembly, live build preview, version control and diff | React, TypeScript, Vite, Google GenAI SDK | Treating prompts as software, where the arc began |
| **AI Companion Toolkit** `[Local-ai-code-assistant-v1 + multi-agent-assistant-v1]` *(merge)* | Portable TUI coding assistant aimed at any repo: user-curated context selection, token/latency metrics per call, **secret redaction in errors (v1.x; regressed in v2.7.3)**, MCP triage "smart mode", git add/commit/push, formal test matrix | Python, OpenRouter, YAML | Built a coding agent before off-the-shelf ones were good, with the security and cost lessons learned |
| **Identity Engine — Design-Token Factory** `[amtrix-identity-engine]` | Brand DNA defined once in YAML → generated CSS (auto light/dark), docs, images, PPT; multi-tenant; real-time "studio tuner" | Python, YAML, CSS, Mermaid | Config-driven code generation; multi-tenant thinking |
| **Computational Ephemeris & Chart Engine** `[amtrix-ai-pandit]` *(optional, see §7)* | Swiss-Ephemeris calculation engine → 8 divisional charts, strength scoring, SVG rendering, LLM-ready XML export, web input terminal, batch mode | Python, SVG templating, XML | Domain-rules engine + structured data for LLM reasoning. 46 commits |

**Excluded from the resume, with reasons:** `apple-watch-dashboard` (small, folds into 5.1), `amtrix_vscode_core` (personal editor config), `AMTX_MPS_*`, `jev-trader-demo`, `outputs`, the boilerplates, the crawler, the spoofing project, and 2019–2022 bots.

---

## 4. What Makes Your Engineering Distinctive (the Interview Story)

These traits recur across **5+ independent projects**. That repetition is what makes them signature traits rather than one-offs:

1. **Determinism over cleverness.** Lookup-table policies (Vision agent), byte-exact hashed payloads and response classification (Triage), `Mode:` first line (Launcher). You make LLM behavior *predictable*.
2. **Never lose work.** Backup before the first edit, versioned sibling files, append-only locked logs, anti-truncation gates, net-deletion alarms. Present in AMTrix Plan, Patch TUI, Claude Code Center, AMTrix Core and the AI Companion Toolkit.
3. **Measured, not claimed.** Tests and timings are recorded by code, never typed by the model; reviews mark each section "📏 measured" or "🧠 judgement". It is a direct answer to hallucinated "done ✅".
4. **Context is a budget.** Path-only MCP loading, compiled context, compression, per-screenshot token budgeting, prompt-cache TTLs. You manage the context window the way a DBA manages memory.
5. **Write once, deploy everywhere.** BRAIN_SYNC, `check_clients.sh`, deploy-to-project scripts. Your standards distribute themselves across repos.
6. **Model-agnostic.** Claude, Gemini, Kimi K2.5, Grok, Llama/Ollama, OpenRouter, Vertex. You choose the model per task, not per habit.
7. **Operator-first UX.** One-command launchers, TUIs, a single health light (`plan_hub.py ok`), catch-up reports. *Resume wording:* "cognitive-load-optimized operator experience". Keep "ADHD-friendly" off the resume; it can be your personal story in interviews if you choose.

**One-sentence pitch:**
> "I build the harness that makes AI agents safe to run: they resume, they can't silently destroy work, they prove what they did, and they cost less, because I've lived the failure modes across 20+ shipped systems and fixed each one in code."

---

## 5. October 2026 Use Cases: Where You Fit in a Company

| Scenario (what a client is struggling with now) | What you deploy | From which project |
|---|---|---|
| **Enterprise rolled out Claude Code/Codex to 300+ devs; spend is up, quality uneven** | AI gateway with prompt-cache injection, per-team routing/budgets, cost HUD; a drop-in governance standard in every repo | Claude Code Center + AMTrix Plan |
| **Regulated firm (bank, insurer, ratings agency) needs AI change audit for model-risk / SOC 2 / AI-governance reviews** | Byte-exact request hashing, append-only attempt logs, secret redaction, human approval gates, measured-evidence records | Frontier Triage + AMTrix Plan (+ your Moody's domain credibility) |
| **Agents lose context in multi-day work; every new session re-explains the project** | Compiled-context handoff, catch-up reports, cross-repo protocol sync, compression of long histories | AMTrix Core + Nexus + Context Compressor |
| **Ops team wants to automate a legacy desktop/web app that has no API** | Computer-use / VLM agent with perception → deterministic policy → verified action, session token budgeting | Vision LLM Decision Agent |
| **Company wants its internal knowledge/tools available to agents through MCP** | Custom MCP servers with path-only loading, pipelines and anti-truncation; an MCP control plane | Kimi MCP Server + AMTrix Studio |
| **Long-running autonomous agents need a human approval path off-desk** | Schema-validated agent event bus → policy routing → phone push with action buttons | Signal Layer (VoiceBus + Notify-Bus) + 5.1 alert engine |
| **Privacy-sensitive client (health, legal, defense) can't send data to cloud LLMs** | On-prem LLM stack with private search RAG, dual-machine setup | Private LLM Stack |
| **Real-time monitoring of inventory/prices/SLAs with instant multi-channel alerts** | Polling/ingestion → geographic/coverage optimization → Telegram/ntfy/desktop alert fan-out | Retail Availability Platform |
| **Brand/design system to propagate across many products** | YAML design tokens → generated CSS/docs/decks | Identity Engine |

**Roles to target:** Forward Deployed Engineer (AI labs and AI-native startups), AI Solutions Architect, Agent Platform / Developer-Productivity Engineer, AI Governance Engineer (financial services), and 1099 "AI agent rollout" consulting.

---

## 6. Claims to Verify Before They Go on the Resume

| Claim | Source | How to verify |
|---|---|---|
| 40–90% cost reduction via cache injection | claude-code-center README | Query `proxy.db` / HUD logs for cache_read vs. input tokens over real sessions |
| AMTrix Plan test count / pass rate | amx_impl_plan tests | `python3 -m unittest discover amx_impl_plan/tests` and use the number `finish` records |
| 30+ stores / 6 states / 9 queries | iPhone v3 GEOGRAPHIC_ROUTING doc | Confirm from config |
| "Production-grade", "Health 100/100", "Golden Master" | various READMEs | Self-labels. Don't put these on a resume; use measured facts instead |
| Commit counts (365 / 97 / 62 / 56 / 46) | git history, measured today | ✅ measured |

---

## 7. Decisions I Need From You

1. ~~Manoj_Project / Kimi MCP Server: client or partner work?~~ **Resolved 2026-10-25:** the user confirmed it is entirely their own work. Described as the Universal MCP Analysis Server; no partner wording.
2. **Vision LLM agent:** OK to mention trading as the domain? (I recommend "real-time visual decision agent; applied to market-chart monitoring", with no performance claims.)
3. **AI Pandit (astrology engine):** include it as "computational ephemeris engine", or leave it out to keep the profile tight? (I lean toward leaving it out.)
4. **Next step:** shall I now read your existing `FINAL_RESUMES/*.md` and produce:
   (a) a new **FDE resume** that merges your 21-year background with these pillars,
   (b) a 1-page **project portfolio** (6 flagship cards),
   (c) a **use-case brief** for 1099 pitches,
   and (d) run the measurements in §6?
