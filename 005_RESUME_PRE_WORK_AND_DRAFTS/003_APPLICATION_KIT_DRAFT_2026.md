# Application Kit 2026 — Forward Deployed Engineer
> 🕒 Last changed: v0.1.1 · 26-10-25__14.33.20
> 🗓️ Created: 26-10-25__14.33.20
> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 00:00 UTC+4  
> **Status:** Baseline
<!-- Built 2026-10-25 from DATA_REFERENCES/DEEP_READ_NOTES_2026-10-25.md. Every claim traces to a verified notes line unless marked "not re-verified". -->

Contents: 30-second pitch · cover letter, three variants · four STAR stories · phrasing rules · verification status.

---

## 1. The 30-second pitch

> I'm a Forward Deployed Engineer for AI agents. I spent 15 years at Moody's Analytics and in bank risk consulting proving that credit-risk models were implemented exactly as specified. Since 2025 I've done the same thing for LLM agents, full time: I built my own multi-provider gateway so Claude Code runs on Vertex, Bedrock, OpenRouter or local models with caching and cost telemetry; a governance standard that makes any coding agent back up, stay in scope and prove its work with tests the code runs; MCP servers and an execution harness that never calls a truncated answer complete; and a private 30B-model inference node on Apple Silicon. Twenty-plus shipped tools, all built as small plug-and-play modules. I go into a team's real workflow, find where the AI fails, and ship the fix.

---

## 2. Cover letter template (fill the brackets; pick one variant for paragraph 2)

**Opening (all variants)**

Dear [Hiring Manager / Name],

I'm applying for the [role title] position. I build the infrastructure that makes AI agents dependable, and I deploy it the way a forward-deployed engineer does: inside the customer's workflow, against the customer's actual failures. For 15 years I built credit-risk data platforms and validated model implementations for Moody's Analytics and major banks. Since 2025 I've applied that discipline full time to LLM-agent systems and shipped 20+ tools and platforms, all my own work.

**Variant A — Enterprise AI platform (banks, insurers, large software vendors)**

Your customers are rolling coding agents out to hundreds of developers and need spend, auditability and vendor freedom under control. I've solved each of those on my own stack. Claude Code Center is a self-hosted gateway that routes the Claude Code agent to Google Vertex AI (including third-party Model-as-a-Service models), AWS Bedrock, OpenRouter or local models on the customer's own billing, with prompt caching, tool calling on non-Anthropic models and a per-request cost HUD. AMTrix Plan is a drop-in governance standard: every agent session becomes a numbered, read-only, fingerprinted record; approvals are stored in the human's own words; a pre-commit gate blocks staged secrets; and "done" means the tests the code ran passed. A rules ledger maps about 190 written rules to the code that enforces each one, which is the kind of traceability a model-risk or SOC 2 reviewer asks for. My Frontier Triage Engine hashes every request byte-exactly and refuses to call a partial response complete. I have deployed these to my own projects and written the human-in-the-loop standard a client team can adopt without the code.

**Variant B — AI-native startup FDE (fast-moving product team)**

You need someone who can sit with a customer, understand a messy process quickly, and ship something that works by Friday without breaking what already runs. That is how I build. My retail-availability platform grew from a single scraper into a multi-daemon runtime with lock-elected singletons, a PID-verified instance registry, Apple fulfillment JSON parsing and a multi-channel dispatcher with per-delivery audit and ntfy failover, with new product lines added by YAML profile alone. My MCP server gives IDE agents deep multi-model analysis without context bloat: pass-by-path loading, a reference-ID raw store, drill-down and an anti-truncation loop. My vision-LLM framework lets a multimodal model decide while a deterministic state machine executes, with 28.6K audited actions over 270 runs on a live GUI. Everything is a small, portable module with its own installer, because the next customer will need a different combination.

**Variant C — 1099 / consulting engagement**

You have a specific problem: agents that lose work, cost that is rising, data that cannot leave the building, or a legacy application with no API. I can scope and deliver a fix as a contained engagement. Examples from my own stack: a private AI node on a 64 GB Apple Silicon workstation running 30B models at 256K context with Ollama, Open WebUI and private search; a self-hosted ntfy notification bus behind Caddy TLS with deny-by-default ACLs that any tool can use by setting two environment variables; a deterministic "compute, then narrate" engine with versioned scoring policies and XSD-validated evidence so the LLM never does the math; and a governance layer that installs in one command and updates every project in one more. I work in versioned iterations with an approved plan, a backup before every edit, and a walkthrough you can verify yourself, so you always know what changed and why.

**Closing (all variants)**

My background is 21 years of enterprise technology with a bank-risk foundation, so I build with audit trails by default and I'm comfortable in front of a risk committee as well as in a terminal. I'd welcome a conversation about where your AI deployments are failing and what I would ship first.

Sincerely,
Amit Malhotra
(917) 345-7516 · amit.malhotra1@gmail.com · Hicksville, NY

---

## 3. Four STAR stories

### Story 1 — A data-loss incident became a safety architecture (AMTrix Core → AMTrix Plan)
- **Situation.** In February 2026 an LLM overwrote about 150 lines of my own work. Seventeen days into building a skill library I had 168 files and 74 backups and no protection against a model rewriting a file.
- **Task.** Make loss impossible by construction, not by asking the model to be careful.
- **Action.** The next day I wrote the Side-by-Side Backup Protocol and within three days a backup-first editing CLI (backup, safe-edit, restore, diff, archive-not-delete prune) with a Backup Law in every skill. I commissioned an independent AI review of the tooling that found four tools able to destroy data (for example `rmtree` on deploy, settings wiped on a parse error), fixed all four with atomic writes, timestamped backups, dry-run defaults and move-not-delete, and locked each with a regression test. Later, in AMTrix Plan, this became a PreToolUse hook that backs up before any edit and refuses edits without an open approved iteration.
- **Result.** No data loss since. The pattern now protects three projects through code, and the dated incident write-up is part of the project record.

### Story 2 — Making Claude Code's tool loop run on non-Anthropic models (Claude Code Center)
- **Situation.** I wanted the Claude Code agent on my own Vertex and OpenRouter billing, including Gemini and third-party Vertex models, with no subscription. Tool calls came back as fragmented streaming chunks and the agent's loop broke.
- **Task.** Translate Anthropic-format tool traffic to and from other providers transparently, with explicit routing and no silent fallbacks.
- **Action.** I built a streaming SSE accumulator that merges fragmented function-call fields and reasoning signatures into clean tool blocks, a per-model registry flagging tool support, and explicit provider routing. I debugged a run of production-style failures: a silent cache-off regression, a shell trap that killed a shared daemon, capitalised provider keys causing silent 404s, a missing terminal redirect swallowing input, and stream chunk splitting that garbled output. I then layered cost controls: 1-hour cache injection, a keepalive daemon with measured cost per hour, Vertex explicit context caching and a SQLite exact-match cache.
- **Result.** The agent runs on the provider I choose, on billing I own, with tokens, cache hits and cost visible per request. The same gateway later took IDE extension traffic onto my own Vertex billing.

### Story 3 — Duplicate and lost alerts across processes (retail-availability platform)
- **Situation.** The alerting platform ran several daemons per product profile and several profiles at once. Users saw duplicate alerts and sometimes missed real stock changes.
- **Task.** Find the root cause and make alert state correct across processes without slowing the poll loop.
- **Action.** Root-cause analysis showed independent processes racing on alert state. I built a cross-process file-locked alert-state store with change detection, atomic writes, schema migration, cooldowns and first-run baseline suppression; made the parser and harvester lock-elected singletons with standby takeover; gave each dashboard a PID-verified registry entry; and gated alerts by which dashboards were live, with a registry failure defaulting to "alert" so nothing is silenced by mistake. Every delivery now writes a JSONL audit event with provider, HTTP status and error, and ntfy fails over to a secondary server.
- **Result.** Duplicate and lost alerts stopped. The dispatcher's audit trail made later channel problems a two-minute diagnosis, and SQL over about 9.8M observations turned the telemetry into per-store restock windows.

### Story 4 — A test runaway on a client machine (AMTrix Plan)
- **Situation.** AMTrix Plan's `finish` step runs the project's tests to produce measured evidence. On one installed project the suite ran away and never returned, blocking the close of the iteration.
- **Task.** Make the evidence step safe on any client's machine without weakening it.
- **Action.** I changed the runner to kill the whole process group on timeout rather than the parent alone, and added a hermetic-suite check so a suite that leaks into the real record is detected at every `finish`. A separate bug, where deploy tests wrote empty bundles into the real record because an environment-variable seam did not hold, was fixed by refusing the carry unless the source is the real repo. Both went into the project's own skeptical-buyer review, which lists sixteen known gaps and how each was narrowed.
- **Result.** The suite closes cleanly on every installed project, and a cross-project health check prints one pass/fail per feature per project so a regression on a client shows up the same day.

---

## 4. Phrasing rules (apply to every application)

- Say **AMTrix**, never the shortened form.
- Say **"modular instruction design"** or **"LLM instruction sets"**, not "prompt engineering".
- Say **"vision-driven UI automation"**, not "autonomous trader"; make no profit claim.
- Say **"browser-session automation for reliable availability data"**, not "bypasses bot protection".
- Say **"LLM traffic observability for my own sessions"**, not "capturing a vendor's system prompts".
- Say **"used live with Claude Code; adapters for Codex and Antigravity"** and **"deployed to three of my projects"**, not "battle-tested everywhere".
- Say **"hook-enforced guardrails"**, not "sandbox"; **"offline and mocked test suite"** where live behaviour is unverified.
- Say **"self-hosted ntfy notification bus"**; do not claim high availability (one instance; failover lives in the client).
- "Multi-agent" means planner and executor role prompts, not independent parallel agents.
- Never quote the operator profile, trigger-word lists, health details, family or financial details from any project file.

---

## 5. Verification status (2026-10-25)

Read in full and re-verified this pass: Claude Code Center, the MCP server, Frontier Triage Engine, AMTrix Plan (suite re-run green), AMTrix Core, the retail-availability platform v3, the subscription launcher, notify-bus, Patch TUI, the vision-LLM framework, the prompt library and protocol template, AI Pandit, AMTrix VoiceBus, the identity engine, AI Companion v1 and v2, and the local Ollama model inventory (checked with `ollama list` and `ollama show`).

Described only from earlier project documents, not re-verified this pass because the parent folder was unreadable: Ollama Powerhouse (the launcher and Docker layout), PromptForge, SmartBrain voice agents (custom Alexa skills), AMTrix Studio, AI Context Compressor, vision-agents-builder and claudecodeui. Keep their wording general until re-read.