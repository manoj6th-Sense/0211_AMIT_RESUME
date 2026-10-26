# Deep Read Notes: Full Project Pass (2026-10-25)
> 🕒 Last changed: v0.1.1 · 26-10-25__14.18.58
> 🗓️ Created: 26-10-25__14.18.58

How this pass works:
- **Docs current** (updated alongside the latest code): read all current docs, then spot-check the code against them.
- **Docs stale** (older than the code): read the **current source files** in full.
- **Skipped:** versioned copies (`file_v2.4.5.js` and similar), backup folders, caches, generated plan records, `node_modules`.
- Each project has its own section with the exact files read, so you can audit it.

---
## 1. claude-code-center (Claude Code Center / AMTrix Gateway): v2.4.9.6, 97 commits, last commit 2026-10-02

**Docs vs code:** README/CLAUDE.md are dated 2026-05-22 (v2.4.7.2). The code is from Oct 2026, so **I read the code**. SNAPSHOTS.md (the change log, current through Oct 2) was read in full.

**Read in full:** `src/proxy_server.js` (3,151 lines); `src/proxy/` routing.js, cache.js, db.js, vertex_cache.js, hud.js, utils.js, antigravity/translator.js, patch_ide.sh; `src/` launcher.sh, tui_hub.sh, tui_builder.sh, tui_vertex_models.sh, keep_cache_alive.sh, cache_tools_tui.sh, help.sh; `config/models.json` (all 7 groups), `routing.json`, `model_profiles.json` (schema, cache rules, all 35 profiles summarized); SNAPSHOTS.md; README.md; CLAUDE.md (design patterns and decisions sections). **Ran** the offline unit tests (`scripts/tests/v2.4/test_proxy_modules.js`). **Not read:** `config/profiles.env` and the credential JSON (they hold keys), the versioned `_v2.x` copies, the 27 test files beyond the list above, and `docs/`.

### What it actually is
- **Two halves.** A Bash TUI and launcher sit in front of the Claude Code CLI. A Node/Express gateway ("AMTRIX Gateway", :8080) speaks the Anthropic Messages API and translates it to each provider.
- **TUI hub** (`tui_hub.sh`): builds its model menu from `models.json` via jq, with ~45 models in 7 groups: Anthropic, OpenAI native, Vertex Gemini native, Vertex MaaS third-party (DeepSeek, GLM, Kimi, Qwen, Grok), OpenRouter-only, local Ollama (Qwen 3 30B variants, Llama, LLaVA), and Bedrock. It also opens the Builder, Cache Tools, Help, a Vertex menu and a proxy launcher (osascript).
- **6-step Advanced Builder** (`tui_builder.sh`): Transport → Route policy → Model → Output → Permissions → Directory/flags. It writes `~/.claude-control-center/launch.env` and hands off to `launcher.sh --config`.
- **Per-model auto-flags** (`model_profiles.json` v2.4.9, Oct 2): about 35 profiles. Each emits Claude Code flags and settings: `--tools` allowlist (6 tools), `--strict-mcp-config` with empty MCP (disables MCP), `--no-chrome`, `--exclude-dynamic-system-prompt-sections`, plus env (`CLAUDE_CODE_AUTO_COMPACT_WINDOW`, `BASH_MAX_OUTPUT_LENGTH`, `CLAUDE_CODE_MAX_OUTPUT_TOKENS`, …). This is **token-diet tuning per model**, and the Oct 2 commits say so directly ("save tokens especially for Anthropic models"; "fixed GPT running all tools from claude code").
- **Vertex dedicated menu** (`tui_vertex_models.sh`): Google first-party models plus third-party MaaS. You choose Direct Vertex (service account → regional or global `aiplatform` endpoint) or OpenRouter BYOK (OpenRouter bills against your GCP account).
- **Cache keepalive**: the proxy hashes each conversation into a session key and stores a "warm bundle" on disk. `keep_cache_alive.sh` is a PID-tracked daemon that pings `/internal/keepalive/:key` with `max_tokens:1` every N minutes and logs cache_read and cache_creation tokens. The TUI lets you pick a session from `/debug/warm-bundles`. SNAPSHOTS gives the measured cost per hour: 2-min interval $0.30/hr, 6-min $0.10/hr, 45-min $0.013/hr.
- **Gateway internals**: see the earlier summary, now confirmed:
  - explicit per-provider routing by URL path (no model-string guessing)
  - Vertex native Gemini with schema cleaning, thought-signature registry and a streaming function-call accumulator
  - Claude on Vertex via rawPredict
  - Vertex MaaS via openapi chat/completions
  - Vertex explicit `cachedContents` when the stable prefix is ≥32,768 bytes
  - OpenRouter per-block `cache_control` with a 1h TTL and lowercase provider pins (`google-vertex`, `amazon-bedrock`), `allow_fallbacks:false`
  - 501 "PROXY BLOCKED" instead of silent fallback
  - an SQLite exact-match response cache (24h, with timestamps stripped from the key)
  - an HTML HUD with spend, cache and session views and payload-diff debug endpoints
- **Antigravity "Brain Swap"** (this is **your IDE work**): `patch_ide.sh` scans the VS Code, Cursor and Antigravity extension folders for the hardcoded `generativelanguage.googleapis.com` endpoint, backs up each file, and rewrites it to point at the local proxy. `translator.js` catches `/v1beta/models/*:generateContent` and reroutes it to Vertex BYOK with explicit context caching. There is also an unpatch script.

### Engineering story the change log proves (dates from SNAPSHOTS.md)
- **Mar 21, 2026, v1.0:** Claude Code CLI router to OpenRouter and Ollama. Keys moved out of git into env-var expansion. A `.claudesignore` policy fixed "a directory sweep costing ~23,000 tokens on simple prompts".
- **Mar 24, v1.1.11:** root-caused a lifecycle bug. Each launcher's `trap EXIT` killed the shared proxy. Fixed with a detached `nohup` daemon plus a PID file.
- **Mar 24, v1.1.13:** found that cache injection had been **silently off since v1.1.8** because of a wrong comment ("the proxy was providing zero cache benefit") and restored it.
- **Apr 5, v2.3.2:** "90% discount confirmed even after 55 minutes" with per-block caching and the Anthropic provider lock (`docs/CACHE_Research_by_GPT_5.4.md`). Your own live test.
- **Apr 13, v2.3.8:** keepalive interval bug (a `read` missing `</dev/tty`) found and fixed. A multi-instance colour-coded HUD was added.
- **May 9–14, v2.3.9:** Vertex BYOK. A Gemini 3 thought_signature 400 workaround ("text-collapse"). Anthropic-on-Vertex rawPredict. URL-path provider routing to avoid Claude Code's API-key prompt. A stream-buffer fix for DeepSeek "garbled output". **Your own finding:** Vertex MaaS needs OpenAI-format tools, so tool-using Claude Code sessions on MaaS models should go through OpenRouter BYOK, and Vertex Direct is for chat-style integrations.
- **May 15, v2.4.0:** monolith split into `src/proxy/` modules, `models.json` registry ("76/76 unit tests pass").
- **May 17, v2.4.6:** "recovered from total system loss". Fixed silent 404s caused by capitalised OpenRouter provider names.
- **May 18, v2.4.7:** Antigravity sandbox caching, JSON config decoupling, SSE tool accumulator, Kimi/DeepSeek on Vertex MaaS.
- **Aug 7–13, v2.4.8.x:** universal registry, launcher mitigation for Claude Code's unknown-model context-window enforcement, strict Anthropic SSE for Ollama and MaaS streams, SQLite exact-match cache with timestamp stripping.
- **Oct 1–2, v2.4.9.x:** model catalog refresh, per-model token-saving flag profiles, GPT tool-overuse fix.

### Verified vs. claimed (for resume accuracy)
| Claim in current docs/profile | What the code/logs show |
|---|---|
| "90% cache discount" | ✅ Your own log entry for **Anthropic models via OpenRouter with per-block cache_control plus Anthropic lock** (Apr 5). Not a blended number across all providers. |
| "40–90% cost reduction" | ⚠️ Not measured anywhere I found. Use "up to 90% on cached input tokens (Anthropic 1h TTL, verified live)". |
| README "Prompt Caching Match Rate 99.7%", "Score 100/100" | ⚠️ Self-reported in the docs. No source data found. Leave off the resume. |
| HUD "saved by cache" | ⚠️ `hud.js` reads `cache_write`/`cache_read`, but the price table uses `cachewrite`/`cacheread`, so savings compute as 0. Don't quote HUD savings until this is fixed. |
| Vertex third-party models **with tools** | ⚠️ Partly. Native Gemini on Vertex passes tools (functionDeclarations plus accumulator). The MaaS path (Kimi, DeepSeek, …) translates only text back, and tool_calls are dropped. Your May 14 log already says tools on MaaS go via OpenRouter BYOK. Claude-on-Vertex rawPredict sends no tools. |
| Bedrock | ⚠️ In the registry, but no native handler. It reaches Bedrock only through OpenRouter `provider.order: amazon-bedrock`. |
| "Auto-falls back to OpenRouter BYOK if quota exceeded" (Vertex menu text) | ⚠️ `TARGET_FALLBACK` is exported but nothing reads it, and `routing.json` fallbacks aren't referenced. The proxy deliberately returns 501 instead. The "no silent fallbacks" design is the accurate story. |
| "76/76 unit tests pass" (May) | ⚠️ **Re-run today: 54 passed, 22 failed.** The failures are routing-inference and model-normalisation tests that predate the deliberate "no string guessing" change. The tests weren't updated. `npm test` also points to `scripts/run_all_tests.sh`, which moved to `scripts/utils/`. |

### Resume-ready takeaways
- Built and run **your own multi-provider LLM gateway**: Anthropic API in; OpenRouter, Vertex (Gemini native, Claude rawPredict, MaaS), OpenAI, Gemini API and Ollama out. Explicit routing, no silent fallbacks.
- **Cost engineering with evidence:** per-block 1h cache injection, a keepalive daemon with measured $/hr, Vertex explicit context caching, an exact-match SQLite cache, and per-model CLI token-diet profiles.
- **Debugging stories you can tell in interviews:** silent cache-off regression, a trap-kills-shared-daemon bug, capitalised provider keys causing silent 404s, a missing `</dev/tty` swallowing input, and stream chunk splitting garbling output.
- **IDE integration (yours):** extension endpoint patcher plus a translator that moved IDE Gemini traffic onto your own Vertex billing with caching.

---
## 2. MCP server ("amit-MCP", folder `Manoj_Project/0150_MCP_SERVER_DEMO`): code Sep 29, 2026; logs Jun 28 to Oct 25

**Docs vs code:** the README and setup guides are from June, but the code was rewritten Sep 29, so **I read the code**. `docs/Amit-MCP-md-files/01–05` (Sep 28) and `SESSION_HANDOFF_FRONTIER_TRIAGE.md` (Sep 30) were read as current.

**Read in full:** `server.py` (528), `utils/model_client.py` (416), `utils/anti_truncation.py` (151), `pipelines/deep_analysis.py`, `deep_research.py` (264), `checkpoint.py` (310), and `config.yaml` (models and pipelines; no secrets in it). **Read the main logic of:** drill_down, continue_partial, recap, wrap, `utils/formatter.py`, `storage.py`. **Skimmed headers and function lists of:** `ast_indexer.py`, `audit_tracer.py`, `universal_tui.py`, `Amit-MCP-Demo/run_demo.py`. Also read SESSION_HANDOFF (full), the 05 architecture doc (headings), `000_FRONTIER_AUDITS` (the audit outputs and the ledger), and **logs/server.log\*** for usage counts. The vendored `frontier_triage_engine/` copy is covered in its own section.

### What it actually is
- **FastMCP stdio server with 11 tools:**
  - `project_ast_index`: deterministic, no LLM, $0
  - analysis: `deep_analysis`, `quick_summary`, `code_review`
  - follow-up: `drill_down`, `mcp_continue`
  - `deep_research`
  - session lifecycle: `session_checkpoint`, `session_recap`, `session_wrap`
  - a backward-compatible `kimi_pipeline` router over all of them
- **Built for the Antigravity IDE and Claude Code.** Every tool takes `provider_override` and `model_override`.
- **Model layer:** one `.chat()` interface over **AWS Bedrock** (boto3 `converse`, the default: Kimi K2.5, Claude Sonnet 4.6, DeepSeek R1, Nova) and **OpenRouter** (urllib only, no SDK). About 40 aliases resolve to a client, model and provider preferences, including OpenRouter `~…-latest` floating slugs and BYOK pins (`order: ["Amazon Bedrock"]` / `["Google Vertex"]`, `require_parameters`). Legacy slugs are rewritten automatically.
- **Context-window protection pattern (the core design idea):**
  1. The heavy model output is saved to disk under a `raw_reference_id` with a 7-day TTL.
  2. A second low-temperature call compresses it into a fixed JSON schema (summary ≤10 sentences, ≤8 findings, ≤10 actions, ≤5 warnings, ≤5 decisions), parsed with a regex fallback.
  3. The IDE gets only the compact JSON, and `drill_down` and `continue` work from the stored reference ID.
- **Anti-truncation loop:** if `finish_reason` is `length` or `max_tokens`, the loop re-prompts with the last 30 words and "do NOT repeat", for up to 8 calls or 60K output tokens, then reports `complete`/`partial` with the stop reason. **The logs show it firing for real** (a 3-iteration continuation).
- **Session audit trail:** `checkpoint` writes `000_PROJECT_HISTORY/002_SESSIONS/<date>/<id>/` with ARTIFACTS, CHECKPOINTS, LLM_FILES and MCP_LOGS folders, rendered chat history, an MCP call log (args and outputs), token metrics, and `index.json`. `wrap` runs checkpoint → status wrapped → model recap.
- **`deep_research`:** a 5-phase chain (plan → facts → reasoning matrix → exec memo → skeptical self-audit) with a raw/processed/insight folder layout and per-phase token metrics.

### Usage evidence (from logs)
- **63 tool invocations** and **28 successful Bedrock Kimi K2.5 calls** between Jun 28 and Oct 25, 2026. This is a working tool you used, not a mock-up.
- `000_FRONTIER_AUDITS/audit_ledger.json`: you ran a **worker-model audit plus a frontier-model review of your own server** (2 paid calls, **$0.097 total**). The audit found real issues:
  - the `kimi_pipeline` router silently drops params (`output_format`, `max_output_tokens_hint`, session fields)
  - `model_client` mutates `os.environ` from `mcp_config.json`
  - hardcoded caps
  - config re-read on every call

  **That audit led directly to the Frontier Triage Engine** (truthful 4-state classification, approval gates, durable audit vault). This is a strong "I audit my own tools and act on the findings" story.

### Verified vs. claimed
| Claim | Reality |
|---|---|
| "10 tools" (current profile) | 11 registered (10 discrete + router). Either number is fine if you say "10 tools plus a unified router". |
| "Bedrock primary, OpenRouter fallback" (docstring) | ⚠️ No automatic failover. The provider is chosen by config, alias or override. Say "Bedrock or OpenRouter, selectable per call". |
| "60K / 8-call anti-truncation" | ✅ Exact constants. Hardcoded, not read from config. |
| `deep_research` = "research" | ⚠️ **No web retrieval.** All 5 phases are model-only, so the "facts" come from the model's own knowledge and the Phase 5 audit is a self-check. Describe it as a "structured multi-phase analysis chain", not grounded research. |
| `docs/Amit-MCP-md-files/05_mcp_server_architecture.md` | ⚠️ Describes a different directory layout (`02_ORGANS/08_orchestrator/...`, `KimiRoutedClient`, Mistral/Sarvam mappings) that **this repo's code doesn't contain**. Don't cite it for this project. |

### ⚠️ Something you should know before showing this repo
You told me this work is yours, and the profile wording will say so. But the code still contains strings that tie it to another name and repo. Anyone who opens it will see:
- the folder name `Manoj_Project/`
- `C:\Users\Manoj\.gemini\antigravity\mcp_config.json` in the `model_client.py` docstring
- `HTTP-Referer: https://github.com/manoj6th-Sense/ManuNexusAI`
- "ManuNexusAI root" path logic and `03_MONITOR/02_MONITORING/db_utils`

If you plan to share the repo or demo it, consider renaming those before you link it. **I haven't changed anything.** This is only a heads-up.

### Resume-ready takeaways
- Designed and shipped a **multi-model MCP server** (FastMCP; Bedrock and OpenRouter) that keeps IDE context small: a reference-ID raw store, schema-bound JSON compression, and drill-down/continue tools that pull detail on demand.
- **Reliability engineering for LLM output:** an anti-truncation continuation loop with explicit partial/complete reporting, and a session checkpoint/recap/wrap audit trail.
- **Cost-aware self-audit:** you used a cheap worker model plus a frontier reviewer ($0.10) to audit your own server, then turned the findings into a stricter engine.

---
## 3. frontier-triage-engine (v2.0.0, Sep 30 to Oct 4, 2026; not a git repo)

**Copies:** 4 exist (root `frontier-triage-engine/`, `AMTRIX-TOOLS/frontier-triage-engine/`, inside the MCP server, and `.agents/skills/` there). **Canonical = root `frontier-triage-engine/`**, which has the newest files (CLAUDE.md Oct 4, `dispatch.py`/`universal_tui.py` Oct 1). Its CLAUDE.md says it "moved out of amtrix-impl-plan-standards on 2026-10-04".

**Docs vs code:** in sync (both Sep 30 to Oct 1). **Read in full:** CLAUDE.md, SKILL.md, `references/01_PROBLEM_DIAGNOSIS…`, `scripts/dispatch.py`, the request/send half of `model_client.py`, and `audit_tracer.py`'s FileLock and atomic writes. **Function lists only:** the rest of `audit_tracer.py`, `ast_indexer.py` (761 lines), and the MCP-copy SESSION_HANDOFF (which describes P1/P2 in detail). **Ran** the offline tests: **21 tests, all OK** (0.12 s). **Not opened:** references 02–06 and `universal_tui.py`.

### What it actually is
- **Origin:** a **standard-library-only "truthful execution" engine** you built after auditing your own MCP server. It is packaged as a portable Agent Skill (SKILL.md, scripts/, references/, tests/).
- **Request integrity:** `build_request` serialises canonical JSON once (`sort_keys`, compact separators) and computes **SHA-256**. The pre-flight card shows exactly those bytes, and `send()` transmits those same bytes. What you approve is what gets sent.
- **Typed failure model:**
  - **NotSent** (connection failed before transmit)
  - **OutcomeUnknown** (timeout after dispatch, so it may have been billed, and there is **no auto-retry**)
  - **HTTPError**
  - **MalformedResponse**
- **Pure `classify()`:**
  - **PARTIAL:** `length`/`max_tokens`. Stamped with a "TRUNCATED, downstream halted" banner.
  - **COMPLETE:** stop/end_turn with non-empty content.
  - **FAILED:** errors inside HTTP 200, refusal, content_filter, reasoning-only with null content ("ghost deliverable"), or any unrecognised finish reason. Never assumed complete.
  - **UNKNOWN:** timeout.
- **Two-stage worker → frontier reviewer.** Each stage needs its own human approval, and Stage B is blocked unless Stage A is COMPLETE.
- **Cost estimates:** only for known model presets, labelled "hardcoded preset, unverified". Unknown models get **no estimate** rather than a misleading one. The ledger records **provider-reported** spend.
- **Audit vault:**
  - monotonic attempt IDs under an `O_CREAT|O_EXCL` lockfile (the PID is written in, and stale-lock info is reported)
  - atomic `tmp → fsync → os.replace` writes
  - recursive secret redaction (`authorization`, `api_key`, `sk-or-`, `sk-ant-`, `ghp_`, …)
  - per-attempt folders holding request, state, response and deliverable
- **AST context engine:**
  - Python AST with full 5-part signatures; non-Python files labelled honestly as `ast: None`
  - pruning, symlink-escape guard, 256 KB cap, binary detection
  - hard-blocks `.env`, `*.pem`, `*.key` and `id_rsa`
  - SHA-based staleness checks and a dependency graph
  - bounded packaging with explicit `[OMITTED]` markers (**no silent `text[:N]` slicing**)
  - portable relative links
- **`deploy_to_project.py`:** one-command install into any repo. It then runs the offline tests in the target, and that is itself tested.

### Verified vs. claimed
| Claim | Reality |
|---|---|
| "19/19 acceptance tests" (handoff) | ✅ Today: **21 pass** (P1 + P2 + deploy tests). `acceptance_tests.csv` has 30 rows (29 specs), and SKILL.md says 31. Say "21 automated offline tests". |
| "Zero-pip" | ✅ Only urllib, json, hashlib, os and unittest imports in the core modules. |
| AST "universal" | ⚠️ The AST parsing is **Python-only**. Other languages are indexed as files without symbols, and the tool says so honestly. |

### Resume-ready takeaways
- Built a **dependency-free LLM execution harness** with byte-exact pre-flight hashing, a 4-state truthful outcome classifier, human approval gates between stages, and a crash-safe audit ledger.
- **A real FDE talking point:** "I don't let a pipeline report success on a truncated or reasoning-only response. PARTIAL halts downstream so the next model can't hallucinate across the gap."
- Packaged as a **plug-and-play skill** with a one-command deployer that self-verifies in the target repo (your Lego-piece principle in practice).

---

## 4. amtrix-impl-plan-standards (AMTrix Plan, folder `amx_impl_plan/`): v0.44.7, 365 commits, last commit 2026-10-22; docs current (v0.43.6, Oct 20)

**Read in full:** `amx_impl_plan/README.md`, `docs/HOW_IT_WORKS.md`, `docs/EVOLUTION.md` (timeline Aug → v0.43, features, limits, version log v0.13–v0.43), `docs/HONEST_REVIEW.md` (all 11 sections), `docs/ROADMAP.md` (P0–P6 and the per-version log to v0.42), the opening of `docs/VERIFY.md` (levels 0–3 and the quick checks).
**Code spot-checked:** script sizes (all 59), `hub_record.py` (approve/tested `--said`), `hub_finish.py` (process-group kill, FINISH_OK/PARTIAL), the enforcement codes in `hub_gate`/`hub_record`/`hub_finish`/`plan_hub`/`clients`.
**Run today (read-only per VERIFY.md; git status the same before and after):** `ok`, `audit`, `selftest --quick`.
**Not read in the first pass (closed by the second pass below):** ARCHITECTURE, HOW_CHECKS_WORK, WORKER_PLAYBOOK, RULES_LEDGER, rules.md, operator.md, FAQ, FEEDBACK_LOOP, FOOTER_DESIGN, PICTURES, GLOSSARY, HUMAN_IN_THE_LOOP_STANDARD. `docs/plan/` records: sampled only. Full suite: re-run in the second pass.

### What it is (from the docs, confirmed in code where marked ✓)
- **A drop-in "operating system" for AI-assisted development.** Copy one folder into any repo and install from a menu. The folder itself is never written to. It makes a model's work **visible, resumable, reviewable and hard to fake**, while the human stays the reviewer rather than the memory.
- **Origin:** an Aug 2026 doc-os skill, blended with the frontier triage engine on Oct 1 and unified as v0.1.0 on Oct 3. 44 minor versions in about 3 weeks. Every version log line is written by code.
- **The record:** `docs/plan/vX.Y.Z/` holds 4 files per iteration (6 until v0.33.6) plus 2 append-only logs per version, with lockstep numbering. Records are fingerprinted and made read-only at the OS level.
- **Approval by code ✓:** `approve --said "<human's words>" --do "<step>"` is the only way an approval enters the record, and `tested --said` the only way a human test does.
- **"Done" is measured ✓:**
  - `finish` runs the project's own tests (Python, `package.json` scripts, Makefile `test`) and the approved acceptance commands.
  - It refuses a red suite (`FINISH_REFUSED_RED`) and prints `FINISH_PARTIAL` when no tests are configured.
  - `approve` refuses acceptance commands that can't fail (`APPROVE_WEAK_ACCEPTANCE`).
- **Four enforcement layers:**
  1. OS read-only records.
  2. A git pre-commit gate that blocks rewrites and **`SECRET_STAGED`** ✓ (common key shapes only).
  3. Tool hooks: backup before edit; `NO_OPEN_ITERATION` ✓; `OUTSIDE_PROJECT` ✓; a per-message state line.
  4. Written rules, with a **rules ledger whose code-held share is itself measured**.
- **Human-facing features:**
  - visible dated backups next to each file (`name_vX.Y.Z_YY-MM-DD__HH.MM.SS.ext`, read only as diffs, so zero tokens)
  - in-file comment threads
  - `FILE_INDEX.md` with notes and STALE flags
  - a zero-model-call AST `CODE_MAP.md`
  - a Resume block at every session start
  - a board ending every reply
  - a phone comment page (`serve` + Tailscale, with the Mac's voice reading aloud)
- **Self-measurement:**
  - friction logs written by code
  - `WHAT_WE_LEARNED.md`
  - a replica drill (can a fresh model rebuild a module from the record?)
  - a reviewer folder written by code
  - `audit` (every verb dispatched, documented and tested)
- **Feedback loop:** each client project writes a privacy-tested bundle at every `finish`; the source ingests them into requests and ships shared rules back. Built end to end, but every bundle so far was empty or came from this repo.
- **Portability:** standard-library Python, no network. Hooks for Claude Code, Codex and Antigravity. Install/update/repair/undo/remove with a preview, `update-all`, `check_clients.sh`, and a module contract (`module new`, the Lego piece).

### Verified vs. claimed
| Claim | Reality (measured 2026-10-25 unless noted) |
|---|---|
| Size | ✅ scripts **23,440 lines / 59 files**, none over 1,200 lines (the limit is enforced by a test; largest is `hub_finish.py` at 1,047). **46 test files, 745 test functions.** |
| Test count | ✅ The `audit` output reads "**737 tests in v0.44.7**", green, measured by `finish`. `selftest --quick`: **67 OK in 10.1 s**. `audit`: **AUDIT_OK, 19 checks hold**. |
| Zero dependencies | ✅ stdlib only (consistent with the triage engine; no pip). |
| Deployed to projects | ✅ `~/.amx_plan/deployments.json` lists **5**, all at standard 0.44.0 (Oct 22). 2 are DEMO/TEST (excluded), so the **real ones are AMTrix-core, iphone-inventory-checker-v3 and claudecodeui**. |
| Hooks in Claude Code, Codex, Antigravity | ⚠️ **Claude Code live** (since 2026-10-06). Codex and Antigravity are **built and payload-tested, never seen running live** (the doc says so itself). Say "Claude Code, with Codex/Antigravity adapters". |
| "Hard to fake" | ⚠️ Structure and measured numbers are guaranteed; the **words are still model-written** (HONEST_REVIEW gap 6). Shell edits bypass the tool hooks (narrowed by git-based backups). Hooks fail open by design. |
| Proven on a real project | ⚠️ The doc's own verdict (Oct 19): "**young, unproven on a real second project**". The ten real sessions on AMTrix-core (#306) hadn't started as of Oct 19. It is deployed into 3 real projects, and AMTrix-core's reviewer has run on it (v0.42–v0.43 fixes came from there). |
| Replica drill | ⚠️ A fresh model rebuilds an untuned module at **60–72 % strict / ~80 % lenient** (88 % on a tuned one). The goal is 80 lenient; tuning was stopped on purpose (D2). |
| Today's `ok` light | 🔴, only because of 2 uncommitted files and a last commit 64 h ago. This is an honest signal, not a failure. |

### Resume-ready takeaways
- **Designed and built "AMTrix Plan", a portable, zero-dependency governance layer for AI coding agents** (23K lines of stdlib Python, 737 automated tests). Drop it into any repo and every AI session becomes a numbered, read-only, fingerprinted record. Approvals are recorded only in the human's own words, by code, and "done" means the project's tests and the approved acceptance commands passed, measured rather than claimed.
- **Enforcement in depth:** OS read-only records, a git pre-commit gate (including staged-secret detection), editor hooks (pre-edit backups, no edits without an open iteration, no writes outside the repo), and a rules ledger that measures how much of the rulebook code actually holds.
- **An FDE talking point (honest engineering):** the project ships its own skeptical-buyer review listing 16 known gaps and how each was narrowed. Example: a test runaway on a client machine was fixed by killing the whole process group on timeout ✓ and adding a hermetic-suite check.
- **Human-in-the-loop UX:**
  - visible dated backups that cost zero tokens
  - in-file comment threads answered in place
  - a phone review page over Tailscale with voice read-aloud
  - an AST code map built with zero model calls
  - a resume block so no one re-explains the project
- **Productised:** a menu installer with preview/undo, update-all across client projects, a privacy-tested feedback loop from clients, and a module contract for plug-and-play pieces (the Lego principle).
- **Wording caveats:** say "used live with Claude Code; adapters for Codex and Antigravity". Don't claim "battle-tested on many projects"; say "deployed to 3 of my projects". Don't put a % on the replica drill.

### Second pass (2026-10-25, Fable 5.1): the 11 docs the first pass skipped, plus HUMAN_IN_THE_LOOP_STANDARD.md
**Read in full:** `docs/ARCHITECTURE.md` (220 lines: module map of ~45 scripts with reads/writes, generated-files table, verb table), `HOW_CHECKS_WORK.md` (261), `WORKER_PLAYBOOK.md` (225), `RULES_LEDGER.md` (205), `rules.md` (78), `operator.md` (184), `FAQ.md` (254), `FEEDBACK_LOOP.md` (205), `FOOTER_DESIGN.md` (99), `PICTURES.md` (144), `GLOSSARY.md` (149), `HUMAN_IN_THE_LOOP_STANDARD.md` (373). The §4 claims above all hold; nothing contradicts them. **Full suite:** see the line at the end of this block.

**New, résumé-relevant facts (all from the docs; marked ✓ where the code or a run confirmed it earlier):**
- **Seven Claude Code hook points are wired** (ARCHITECTURE §2, PICTURES §3): SessionStart → `resume`; UserPromptSubmit → `prompt` (state line, core rules every 6th message, slim form between); PreToolUse → `hook` (backup, then allow or refuse); PostToolUse → `stamp`; Stop → `stop` (board rebuild; sends a reply back once if it lacks its ending, `REPLY_ENDING`/`REPLY_CHOICES`/`REPLY_STEPS`); **PermissionRequest → `permission`** (a "standing yes" of N turns, recorded in the human's words, auto-answers the tool's permission dialog for the loop's own calls inside an approved iteration; pushes, installs, deletes still ask); TaskCompleted → `task-completed` (a task stays open until `finish` closed the iteration). This is the most concrete "agent governance" story in the portfolio.
- **Layered defence against "green but wrong"** (HOW_CHECKS_WORK §4): acceptance commands approved before any code; a Try-it-yourself sheet per Walkthrough; black-box install tests on a throwaway project; the replica drill; a second-model review; friction logging. The doc states plainly that none of this proves logic right; it leaves a trail of who checked what.
- **Multi-language, honestly scoped** (HOW_CHECKS_WORK §6): any test command works via exit code (`npm test`, `go test`, `cargo test`, `pytest`); install auto-detects Python tests, `package.json` `test`/`test:*`/`typecheck`/`lint` and Makefile `test`; the AST code map is Python-only, and `FILE_INDEX.md` opens with a `BLIND n of m code files` coverage line for everything else.
- **One-script client check** (§10b): `check_clients.sh` prints one ✅/❌ per feature per deployed project; every new feature must add its own line (a test enforces the list). The client's own reviewer found two measurement bugs on AMTrix-core (backups and version copies counted as code) that became fixes shipped to every project.
- **Test map** (§11): `TEST_MAP.md` lists every code file and public function no test names, most-untested first, with the next one to cover.
- **A KPI on the model's judgement** (FOOTER_DESIGN §4): "Recommendations matched" counts how often the human's pick equals the model's ★ default, goal 90 %, recorded by `ask --read`; the board is built from a one-page executive-status-report pattern (decisions first, one light per dimension with a written trigger, numbers not adjectives, same template every time), with the four sources cited.
- **Rules ledger** (RULES_LEDGER): ~190 obligations, each with the exact phrase code checks is still in `rules.md`, the version it entered, and an **"Enforced by"** column (a verb, a hook word, a script, or "the worker"); `audit` refuses a name that does not exist. `operator.md` has the same table for ~75 dated operator preferences.
- **Worker playbook** (WORKER_PLAYBOOK §6, §9): ~100 gotcha rows, each symptom → cause → fix, many ending "by code since vX.Y.Z" (the slip became a refusal). A live model switch mid-session (Opus 5.5 → Fable 5.1, Oct 8) is recorded as costing nothing because the Resume block, board, playbook and state line carried the state. Good interview material for "how do you make an agent workflow model-agnostic".
- **Feedback loop** (FEEDBACK_LOOP §15): built in three slices; the deploy tests once wrote empty bundles into the real record (the registry's env-var seam did not hold), fixed by refusing the carry unless the source is the real repo and by a hermetic-suite check (`SUITE_LEAKED`) at every `finish`. A good "what went wrong and what you changed" story.
- **HUMAN_IN_THE_LOOP_STANDARD.md** is a portable, nameless v2.0.0 standard (14 principles with do/don't/check, a backup standard and living-doc stamp to adopt as written, a record standard, install/upgrade "careful mode" with `UPGRADE_PARTIAL` notes, an anti-pattern table with the fix for each, an adoption checklist). It is the kind of document a client team can adopt without the code. Strong FDE artefact.
- **FAQ is unusually honest:** a table of which board files the model actually reads ("almost certainly no" for the dynamic ignore files); "Codex and Antigravity … not yet seen running in the real app"; the replica drill "was not worth what it took" (29 of 49 iterations); "No network calls, no keys."

**Doc defects seen (for the proposed-edits list, not the résumé):** GLOSSARY "Iteration … Six files at the same N" is stale (four since v0.33.6; rules.md and ARCHITECTURE say four). FAQ contradicts itself on the page key ("A restart makes a new key" under *comment page* vs. "keeps its key across restarts" since v0.26.8 under *Problems*). FOOTER_DESIGN §4 "Lights and their triggers" still says "trust 🟡 over 2 changes in 7 days" while the settings default is 20 per 2 days. `operator.md` quotes the operator's profanity verbatim and names a personal health detail; never quote either anywhere outward.

**Résumé additions from this pass:** (1) "wired all seven Claude Code hook events, including a PermissionRequest handler that auto-approves only the loop's own calls under a time-boxed standing approval"; (2) "a ledger that maps ~190 written rules to the code that enforces each one, audited on every refresh"; (3) "a one-command cross-project health check across deployed installs"; (4) "a portable human-in-the-loop standard document adoptable without the code".

**Full suite re-run (scratch copy, `discover -s tests -t tests`, HUB_NO_SERVE=1):** `Ran 737 tests in 481.527s — OK (skipped=2)`, exit 0, measured 2026-10-25 on a scratch copy of v0.44.7 (`amxplan_suite.log`). This matches the first pass count of 737, so the backup `_v0.x` test copies did not inflate it.

---

## 5. AMTrix-core (skill library + skill compiler): v3.2.7 library, v0.2.x record, 56 commits (Feb 8 → Oct 22, 2026)

**Freshness:**
- Library docs and builders are mostly from May 2026 and match the code of that date.
- The code touched since then: the Oct 4 M1 safety fixes, plus tests.
- Every commit since Oct 15 is an AMTrix Plan update or a review.
- So the Oct 2026 reviews are the freshest description; I verified their code claims myself.

**Read in full:**
- `docs/README.md` (Oct 18)
- `docs/DIAGNOSTICS_2026-10-03_safety.md`
- the 3 Opus 5.5 reviews (Oct 3: core, extended code analysis, per-skill grades)
- the Fable 5.1 review README + `01_current_state` (Oct 10)
- the Oct 19 AMTrix Plan review's `00_START_HERE` and `04_SENIOR_REVIEW`
- code: `patch_ide_settings.py`, `generate_mac_text_replacements.py`, `deploy_mono_skill.py`, `amtrix_core_hub.sh`, `deploy/deploy_amtrix.sh`, `test/test_amtrix_core.py`, `BCBS/tools/rebuild_bcbs_artifacts.py` (first 60 lines)
- the first 80 lines of `LATEST_CONTEXT.md` (the system prompt)
- the head of `wisdom/WISDOM_NEXUS.xml`

**Structure-checked only:**
- `PROTOCOL_CORE.xml`: 29 protocols with Var/LOGIC/GATE/WISDOM_REF tags
- `amtrix_safety.py`: function list
- skill viewer: file list and cartridge count
- the BCBS JSON shape

**Run:** `test/test_amtrix_core.py` on an **isolated copy** in scratchpad with HOME redirected. **10 tests OK in 1.06 s.**

**Not read in the first pass (mostly closed by the second pass below; still unread: `docs/references/` research notes, the visual dictionary, `app.js` lines 552–1,275, sets ONBOARD/REVIEW/DEPLOY, scenarios 05/06, the rest of the Oct 18/19 review folders):**
- `docs/references/` (14K lines: research notes and a session log)
- `prompts/INITIAL_STARTUP_PROMPT.md` (generated)
- the visual dictionary
- the 30 skill files one by one (graded individually in the Opus review; I didn't re-grade)
- `app.js` body
- `thoughts/`
- other files of the Oct 18/19 review folders

### What it is
- **A skill library plus compiler.** The source is about 24 hand-written Markdown skills (DEBUG, REFACTOR, TESTER_QA_DEBUGGER, BRAINSTORM, AUDIO/Listen, GUARD, DNA…), 8 sets (chained workflows: FEATURE, HOTFIX, CLEANUP, ONBOARD, REVIEW, DEPLOY, STARTUP) and 10 scenarios (human walkthroughs, including "when NOT to use AMTrix").
- **One source, many targets.** Builders generate:
  - an `INDEX.md` routing table
  - a one-paste startup prompt (`;;init`)
  - **macOS/iPhone text replacements** (`.plist`; iCloud syncs it to the phone)
  - VS Code/Cursor/Antigravity snippets
  - an XML protocol form (29 protocols)
  - an **Antigravity mono-skill**: a `/amtrix` router `SKILL.md` plus `modules/` and `scripts/`, live with 33 modules in `~/.gemini/config/skills/amtrix`
- **Capability-based instructions:** the system prompt tells the model to reason in `can_read_files / can_run_shell / can_only_chat…`, not in product brands. This is the portability idea in instruction form.
- **Skill viewer:** a static HTML/JS GUI (90 KB `app.js`, no server) that draws **"cartridges"** (`llm-control-deck-cartridge/v1` JSON, ~23 workflow loops) as clickable flowcharts.
  - Each node is an action with a ready prompt and `{{variables}}`.
  - It works in any chatbot.
  - The "HNTL" envelope carries step/predecessor/cross-cartridge safety for chats with no memory.
  - The Antigravity IDE cartridge v4 is the origin of the "LLM Board", the ancestor of AMTrix Plan.
- **Wisdom Nexus:** an XML knowledge base of the operator's mental models, with an AI-vs-human decision weight per concept (e.g. `weightAI=50 weightPresident=50`), plus 13 project NEXUS files.
- **BCBS 239 side project** (git-ignored, Feb 2026): a 64-term / 63-relation risk-data-governance taxonomy compiled by Python into Mermaid mindmaps and XML (4 pillars: Data Aggregation, Governance & Infrastructure, Risk Reporting, Supervisory Review). This is **banking-regulation domain modelling**, relevant to the BA background.
- **Neon Glass Mermaid compiler** (`neonify.js`, ~500 lines): restyles plain Mermaid by shape and keyword rules.

### Verified vs. claimed
| Claim | Reality |
|---|---|
| Mac text replacements "work everywhere" | ✅ The generator measures **chars, UTF-8 bytes and UTF-16 units against an 1,800 limit**, splits on paragraphs, then lines, and adds a "binder" entry. Since M1 it writes atomically with a timestamped backup and an **added/removed/changed report** (tested). ⚠️ Apple can't chain entries, so a big skill becomes `;;x_1…;;x_n` that you type one by one. |
| M1 safety fixes | ✅ Verified in code and tests:<br>• the IDE patcher no longer wipes JSONC settings (it skips and writes nothing)<br>• the mono-skill deployer builds in a temp folder and **moves** old folders to backups instead of `rmtree`<br>• prune defaults to dry run and archives instead of deleting<br>• the plist gets a backup and a report<br>Each fix has a test. |
| Tests | ✅ **10 pass** (re-run today). ⚠️ They cover only the 4 M1 tools. The index, snippets, payload, XML and deploy builders have no tests. |
| Deploys to Claude Code | ⚠️ `deploy_amtrix.sh` copies `.md` files into `~/.claude/skills/amtrix` with **no `SKILL.md`, so Claude Code doesn't load them**. The Cursor target is probably not read either. Only the **Antigravity mono-skill is truly live**. The deployers also ship `_bk`/`_v` copies (Oct 19 review W2). |
| Portable | ⚠️ 5 tools hard-code `/Users/Amit_Malhotra/...`. |
| On GitHub | ⚠️ `github.com/amit-malhotra1/AMTrix-core`: **38 local commits unpushed; the remote was last updated 2026-05-27.** BCBS and ~500 history files are git-ignored and exist only on this Mac. (Public or private: not checked.) |
| Skill quality | Independent Opus 5.5 review grade: **A or B on 18 of 24 skills**. DEBUG (3 hypotheses, file + function + mechanism, gate, minimal patch), TESTER_QA ("green checks are hypotheses until physically proven") and Scenario 10 were rated "gold". |

### Resume-ready takeaways
- **Built a "write once, deploy everywhere" skill compiler for LLM instruction sets:**
  - The source is Markdown modules.
  - Python builders generate an Antigravity router skill, editor snippets, a one-paste startup prompt, an XML protocol form, and system-wide **macOS/iPhone text replacements** with multi-metric size checks.
  - This is the Lego principle in practice: small modules that plug into any chat, IDE or phone.
- **Model-agnostic workflow GUI:** a serverless "cartridge" viewer that turns multi-step AI workflows into clickable flowcharts with human gates. It works with any chatbot.
- **Engineering hygiene story (FDE-relevant):**
  - Commissioned an independent AI review that found 4 tools able to destroy data (e.g. wiping IDE settings on a JSONC parse error, `rmtree` on deploy).
  - Fixed all four with atomic writes, timestamped backups, dry-run defaults and move-not-delete.
  - Locked each fix with a regression test.
- **Domain:** modelled the **BCBS 239** risk-data aggregation principles as a 64-node taxonomy and generated visual mindmaps (banking regulation to structured knowledge).
- **Wording caveats:**
  - Don't say "deployed to Claude Code" (it isn't loaded there). Say "Antigravity, editors and Mac/iPhone".
  - Say "24 skills, 8 workflow sets, 10 scenarios".
  - Push the 38 commits before pointing an employer at the GitHub repo.

### Second pass (2026-10-25, Fable 5.1): the skill files, sets, tools, viewer, startup prompt and thoughts the first pass skipped
**Read in full:** all 27 live skill `.md` files in `shortcuts/skills/` (v3.2.7, dated 2026-05-27; the `_bk`/`_v` copies skipped) plus the first 120 lines of `_TEMPLATE_STANDARD.md` v4.1; sets STARTUP, FEATURE, HOTFIX and most of CLEANUP (ONBOARD, REVIEW, DEPLOY and scenarios 05/06 remain unread); `shortcuts/tools/` `amtrix_safety.py` (588 lines), `amtrix_v3.1.0.py` (738), `generate_index.py` (409), `md_to_xml.py` (313), `neonify.js` (503), tools README; `AMtrix_Skill_Viewer/app.js` lines 1–551 of 1,275 (the whole default HNTL cartridge); `prompts/INITIAL_STARTUP_PROMPT.md` (1,015 lines, generated 2026-05-25); `thoughts/` brainstorm_20260217_state_of_amtrix, brainstorm_20260208_amnesia_analysis, brainstorm_20260217_visual_navigation, AMTrix_Changes_Report_v3.2.6.6; `docs/references/AMTRIX_PROTOCOL_STANDARD_v3.0.md`. **Git re-measured:** 56 commits, all authored by Amit Malhotra (`git log --format=%an | sort | uniq -c`); branch `master` is **ahead of `origin/master` by 38** (`git branch -vv`), remote last updated 2026-05-27; 12 uncommitted paths; `api.github.com/repos/amit-malhotra1/AMTrix-core` returns 404, so the repo is private or renamed. The §5 claims above hold.

**New, résumé-relevant facts:**
- **Every skill is a routed module.** Each file opens with YAML metadata: name, description, triggers (`;;debug`, `!debug`), `requires`, `required_supporting_skills`, `variables`, `next: "!AMTrix"`, `gate`, version, status, `set_tags`, chat/terminal/IDE fit, `compatibility_mode`, `minimum_capabilities`, `fallback_mode`, `proof_required`. `generate_index.py` scans that metadata and writes `INDEX.md` with a chat/terminal/IDE column per skill, a QUICK TRIGGER MAP, a MISSING-ONLY CONTRACT (load only what the session lacks) and a RECOMMENDATION ENGINE footer; `md_to_xml.py` compiles the same YAML into `<Protocols version="3.2.5">` XML with LOGIC/DECISION/LOOP/ABORT/CONFIRM steps and KernelRules. This is the concrete "modular instruction design" artefact: metadata-driven routing, not prose.
- **Capability-aware degradation is designed in.** `amtr-lite` is a chat-only degraded mode with a capability map and the same MISSING-ONLY contract; DNA auto-detects `ENV_MODE` (ide/terminal/chat); every skill declares `fallback_mode` and `minimum_capabilities`. The startup prompt's rule 1 is "capabilities over brands".
- **Safety is structural, not advisory.** DNA's 8 unbreakable rules (Backup Law `_filename_YYYYMMDD_HHMMSS_bk.ext`, Prove It, One Goal, Hub Return, Milestone Law `;;plan`, Load INDEX, 200-word Session Log, Choice Menu A/B/C); GUARD's pre-flight checklist with risk levels, three backup types (side_by_side / local_shadow / git) and a red-flag auto-STOP at >40 % of a file or 5+ files; RULES' 150-line file cap, SRP/DI, four-layer layout and a ban on `// ... existing code ...` placeholders. `amtrix_safety.py` v3.2.5 makes the Backup Law a CLI (`backup`, `safe-edit`, `restore`, `write`, `diff`, `prune`, `status`, `neonify`) with a 5-second debounce and prune-to-`.safety/archive/` dry-run by default. The Feb 8 "amnesia analysis" note explains why the CLI exists: the model kept forgetting the rule because backup and edit were separate tool calls, so the fix was to fuse them into one `safe_edit`.
- **A documented origin story with a crisis.** `brainstorm_20260217_state_of_amtrix.md`: 168 files and 74 backups 17 days after the first protocol XML; Feb 6 2026 "DATA LOSS CRISIS" (an LLM overwrote ~150 lines) → the Side-by-Side Backup Protocol the next day; Feb 7 Neon Glass; Feb 9 `amtrix_safety.py` pushed to GitHub. Honest, dated, and good interview material for "a time an AI tool hurt you and what you changed".
- **Debug and QA skills are the strongest.** DEBUG forces a 3-hypothesis table (file + function + mechanism), a diagnosis gate, then a minimal before/after patch. TESTER_QA_DEBUGGER adopts a "Skeptical Auditor" persona, requires proof artefacts (`http_payload`, `sqlite_row`, `sse_log`) and drives `src/tui_hub_QA_Debugger.sh --all/--model/--keys/--caching/--tools` from Claude Code Center (§1), so the two projects are wired together. REFACTOR builds a dependency graph and extracts leaf-first with GO/STOP/SKIP. PLAN produces the four pillar docs under `docs/implementation_plans/v{VERSION}/` that AMTrix Plan (§4) later automated.
- **Sets are compositions, not copies.** STARTUP inlines DNA+RULES+GUARD and ends with a Mermaid sequence diagram and a confirmation banner; FEATURE chains RULES+DNA+GUARD+IDE+TEST+DIFF with dual-mode links (`../../../AMTrix-core/shortcuts/skills/*.md` for IDEs, `;;` shortcuts for chat); HOTFIX aborts past 20 changed lines. Named set tags: project_onboard, safe_build, safe_cleanup, safe_debug, ship_gate.
- **The HNTL cartridge is the ancestor of AMTrix Plan, in detail.** The viewer's default cartridge `hntl.antigravity-ide` v2.0.0 has setup/draft/ag_review/comments/approve/implement/verify/archive/memory/refresh actions that scaffold `.llm_board/` (ACTIVE_PLAN, TASKS, WALKTHROUGH, FILE_INDEX, BOARD_RULES, AVAILABLE_ACTIONS) and four helper scripts (`refresh_board.py`, `generate_file_index.py`, `sync_dynamic_ignore.py`, `archive_board_state.py`); a WHITELIST_START/END block generates `.antigravityignore` and `.claudeignore` dynamically. Every §4 concept (board, review gate, approve, verify, archive) is already here in prompt form, dated Jan–Feb 2026.
- **AUDIO v4.1 "Listen Mode"** is a standalone TTS brief skill with FLASH/BRIEF/LESSON/BUILD/DIAGNOSTIC profiles and setup notes for Perplexity, Grok and iPhone. PROJECT_MAPPER generates MANIFEST/SYSTEM_ARCHITECTURE/ROADMAP/QuickStart with strict relative links and Neon Glass Mermaid. MERMAID/`neonify.js` classifies flowchart nodes by shape and keyword, frames subgraphs, uses an 8 %-opacity glass palette for sequence diagrams, is idempotent via a `%% NEON GLOBAL INIT %%` marker, and takes `--no-fill/--no-dash/--no-rounding/--no-frame`.
- **The startup prompt is a 17-rule operating contract**: capabilities over brands, hub return, reuse before asking, an ask limit of 2, MISSING-ONLY, preserve skill essence, proof over vibes, test each step, "nectar extraction", operator-friendly output, cache-aware, Backup Law + GitHub hygiene, a 4-level Documentation Versioning & Timestamp Law (`v3.2.6.5`), Planning Law, Universal Mapper (`PROJECT_STRUCTURE.md` via `tools/amtrix_clean_mapper.py`), then the embedded INDEX, DNA, RULES and GUARD.

**Doc defects seen (for the proposed-edits list, not the résumé):** `amtrix_safety.py` `neonify` resolves `PROJECT_ROOT` to the repo root and looks for `tools/neonify.js` there, but the file lives at `shortcuts/tools/neonify.js`, so the command fails as shipped (verified: `ls tools/neonify.js` → no such file). DNA's YAML description says "the 7 unbreakable rules" while the body heading says "THE 8 UNBREAKABLE RULES". The HNTL envelope header says CARTRIDGE VERSION 2.0.0 but its own safety check tests for "version 1.0.0". The cartridge's `generate_file_index.py` hard-codes the repo name `local_autotrader` and `archive_board_state.py` defaults to version `v12.9.3.7` (both copied from the trader, §10). `amtrix_safety.py` prints "kipped backup" (typo). `generate_index.py` `is_protocol_file` is a stub that returns True. TESTER_QA_DEBUGGER lists its author as Antigravity.

**Privacy note (keep applying):** DNA, STARTUP, HELP and amtr-lite contain an operator profile with a neurodiversity detail and a trigger-word list that includes profanity. Outward material says "mood-aware hub routing" and "operator profile" and quotes neither.

**Résumé additions from this pass:** (1) "designed a metadata-routed instruction-set library: 27 skills and 7 workflow sets with YAML capability/fallback/proof fields, an auto-generated routing index and a Markdown→XML protocol compiler"; (2) "turned a documented data-loss incident into a backup-first editing CLI with debounce, restore, diff and archive-not-delete prune, then into tested deployers"; (3) "wired a QA skill to a live proxy diagnostics script so the model must produce HTTP payloads, SQLite rows or SSE logs as proof"; (4) "the plan→review→approve→implement→verify board that became AMTrix Plan began as a chat-only cartridge in this repo".

---

## 6. iphone-inventory-checker-v3 (app v3.9.9.9, AMTrix Plan record v0.3.7): 62 commits, active Oct 22 → Oct 25, 2026

**Read in full:**
- `README.md` (Oct 24)
- `docs/analysis/INVENTORY_LANDING_TIMES.md` (Oct 23)
- `docs/Enhancments_by_Opus.md` (first 80 lines: the Oct 22 root-cause analysis)
- `docs/architecture/GEOGRAPHIC_ROUTING_ARCHITECTURE.md` (first 60)

**Code read:**
- `inventory_checker.py`: header, `fetch_latest`, `_fetch_once`
- `mac_safari_sync.py`: SKU lists, fulfillment URL, AppleScript runner, `fetch_cycle` steps 1–2
- `alerts.py`: the whole `AlertStateStore`
- `db.py`: schema, restock patterns, tax/savings
- `tools/refuse_db_commit.sh`
- function maps of all 10 main modules

**Measured (read-only):**
- the SQLite DB, opened `mode=ro`
- git tracking/push state

**Run:** the unit suite on a **scratch copy** (no DB, no `.env`, HOME redirected) with the project's venv. **51 tests OK in 1.08 s.**

**Not read in the first pass (closed by the second pass below, except the `web/index.html` body line by line, `notify.py` lines 586–753 and 796–1,026, and the two network test scripts):**
- `web/index.html` (4,181 lines; UI)
- `web/server.py` POST handlers (lines 341–905)
- `notify.py` channel bodies
- `start.sh` (709)
- `raw_apple_parser.py` body
- the 11 YAML profiles beyond the README's schema
- `SYSTEM_STATE_HANDOVER.md` / `FILE_INDEX.md` (Sep 28, older than the multi-port rewrite)
- `tests/test_live_verification.py` and `test_notification_dump.py` (script-style; they hit the network, so not run)

### What it is
- **A real-time retail-availability intelligence system** for Apple Stores across NY/NJ/CT/PA/DE/NH, with multi-channel push alerts and a web "cockpit". It is a solo-built production tool that has been running continuously since mid-September.
- **Two data sources, merged:**
  1. A third-party JSON/HTML feed (`iphonechecker.herokuapp.com`), with retries, freshness targets, 429/403/503 detection, and a stop on HTTP 400 for a phone the feed doesn't carry.
  2. **Apple's own fulfillment endpoint via a real Safari session.** AppleScript primes cookies on the buy page, reloads all fulfillment tabs at once, waits for the backend to settle, then harvests and merges the JSON. Per the doc, direct HTTP to that endpoint is blocked by Akamai.
- **"4-shot anchor" geo design:** Apple's 50-mile radius means 4 anchor ZIPs cover 30+ stores in 6 states with ~9 browser tabs.
- **Alerting:**
  - Telegram bot (inline checkout buttons), self-hosted ntfy over a Cloudflare tunnel with public ntfy.sh failover (250/day limit handled), Discord, a webhook, and macOS desktop notifications (copies the ZIP to the clipboard).
  - Per-channel toggles hot-reload from the UI.
- **Alert-state engine (`AlertStateStore`):**
  - cross-process `fcntl` lock around reload → compare → save; it detects another writer by mtime+size and reloads first
  - atomic tmp→replace writes
  - schema migration (5-part to 4-part keys, merged)
  - baseline-suppression on a profile's first run (no alert storm)
  - per-variant cooldown (900 s default)
  - SOLD_OUT alerts only when the user was alerted for that variant before
- **Multi-profile / multi-port (Oct 22–24):**
  - one YAML profile per phone, each on its own port with its own alert targets
  - a run registry with PID-liveness checks
  - a **singleton Safari harvester** serving every running dashboard, picking up a new one within 10 s
  - "Add a phone" needs config only, no code
- **Data layer:**
  - SQLite `observations` / `latest_state` / `transitions`
  - a 35-store **sales-tax reference** (savings vs NYC 8.875%, tax-free DE/NH)
  - restock-pattern SQL by hour and weekday
- **Analysis deliverable:** "When does Pro Max stock land?":
  - 370 landings / 224 drops over 5 weeks, defined as a variant back in stock after ≥4 h out (anti-flicker)
  - three ET windows; per-store median time-in-stock (Manhasset 40 min, Smith Haven 120 min)
  - weekday effects; regional multi-store pushes

### Verified vs. claimed
| Claim | Reality (2026-10-25) |
|---|---|
| Scale | ✅ DB: **9.82 M observations, 59,771 stock transitions, 57 stores, 9 models, 35 tax-reference stores, 3.2 GB**, Sep 13 → Oct 25. Sources: feed 7.23 M, raw parser 1.32 M, Safari harvester 1.28 M. Alert log: 17,681 events. |
| Tests | ✅ **51 unit tests pass** (unittest; 128 `test_` functions across 23 files, the rest in 2 network/script files). Commit history shows a test per change (v0.1.3 → v0.3.6). |
| "Zero simulation" / "100% reliable" | ⚠️ Marketing wording. The README says itself that a time is "when the checker saw it (±5 min)", with gaps on 10/04, 10/12 and 10/14. Say "continuously polled". |
| Multi-port works | ✅ It was redesigned after the Oct 22 root-cause analysis, which found: 4 processes per instance with only one honouring `--config`, a second instance `kill -9`ing the first's server, and stale-state clobbering with no file lock. Fixed via the run registry, profile-scoped alert files, the singleton harvester and the locked state store (seen in code). |
| Mixed date formats | ⚠️ `observations.observed_at` holds both `09/13/2026, 02:54 PM` and ISO strings (the min() shows it). Minor data-quality point. Don't fix (out of scope). |
| On GitHub | ⚠️ `origin/main` is still only the **initial commit (2025-12-14)**. **61 local commits unpushed**, and the push is blocked (see heads-up). |

### ⚠️ Heads-up for the user (security; nothing changed by me)
- **Plaintext secrets in tracked files:**
  - `README.md` lines ~124–138 show a **Telegram bot token and chat ID**.
  - `.env` and `shared/alert_targets.json` (Telegram token, **Discord webhook**) are **tracked in git**.
- **Not on GitHub:** the token commit `3de82a0` (Sep 16) is **not** on the remote.
- **Still at risk:** any future push of the local history would publish them. The DB (2.7–3.2 GB, plus WAL/SHM) and the logs are also still tracked. `refuse_db_commit.sh` blocks only *new* DB commits.
- **The plan already exists:** the Oct 22 analysis's "Step 0" (untrack, `.gitignore`, rewrite only the unpushed commits, keep `backup/pre-rewrite`) was **not applied yet**.
- **Recommendation:** rotate the Telegram token and the Discord webhook (they're in README text), then do Step 0 before any push. Also remove the token from the README itself.

### Resume-ready takeaways
- **Built and operate a real-time retail-availability intelligence system:**
  - 9.8 M observations and ~60 K stock transitions over 6 weeks across 57 stores in 6 states
  - multi-source ingestion: an external feed plus browser-session automation of Apple's fulfillment API
  - a geo-anchored polling design (4 ZIPs → 30+ stores)
  - multi-channel push (Telegram, self-hosted ntfy with failover, Discord, desktop)
- **Concurrency correctness:**
  - a cross-process file-locked alert-state store with change detection, atomic writes, schema migration, cooldowns and first-run baseline suppression
  - from a root-cause analysis that found duplicate and lost alerts across processes
- **Turned telemetry into a decision:** SQL analysis of restock "landings" (anti-flicker definition, per-store median time-in-stock, time windows). This is the kind of ops-analytics an FDE delivers to a client.
- **Config-driven extensibility:** add a new product line by YAML profile only; each profile runs on its own port; one shared harvester.
- **Wording caveats:**
  - Avoid "bypasses Akamai / bot protection" on a resume. Say "browser-session automation for reliable availability data".
  - Drop "100% reliable / zero-simulation".
  - Don't link the GitHub repo until Step 0 and token rotation are done (it shows only the initial commit anyway).

### Second pass (2026-10-25, Fable 5.1): the server, launcher, parser, dispatcher, CLI, profiles, guides and the macOS app the first pass skipped
**Read in full:** `web/server.py` lines 341–958 (every POST handler and the `__main__` block), `start.sh` (709 lines), `cli/run_registry.py` (117), `cli/store_profiles.py` (147), `cli/raw_apple_parser.py` (463), `cli/main.py` (371), `cli/notify.py` `NotificationDispatcher.dispatch`, `_send_ntfy` and `dispatch_batched_store_alerts` (lines 371–585, 754–795) plus the function map of the whole 1,026-line file, the rest of `docs/Enhancments_by_Opus.md` (lines 80–171), `shared/profiles/config.iphone17_pro.yaml` (one of 12 profile files, read with a redaction filter), `docs/guides/CONFIG_ARCHITECTURE_AND_PROFILES.md`, `NOTIFICATION_SETUP_GUIDE.md` and `GITHUB_SETUP.md` (read through a redaction filter; see heads-up), the first 60 lines of `SYSTEM_STATE_HANDOVER.md`, `app/README.md` and `app/Package.swift`. `web/index.html` (4,181 lines) was read structurally: 101 element ids, 67 functions, 10 fetch targets, section headings. **Git re-measured:** 62 commits, all authored by Amit Malhotra; `main` is **ahead of `origin/main` by 61**; last commit 2026-10-25 10:24. The §6 claims above hold; the Oct 22 analysis's phases B–E are implemented in the code (A, the repo-hygiene step, is not).

**New, résumé-relevant facts:**
- **Process topology is explicit and guarded.** One launch (`start.sh run_app`) starts four daemons per profile: the feed watcher (`cli.main watch`), the Apple-JSON parser, the HTTP dashboard and, on macOS, the Safari harvester; their PIDs go to `shared/run/pids_<profile>`. The parser and harvester are **singletons across all profiles**: `acquire_singleton` takes an exclusive `fcntl.flock`; a second copy blocks in standby and takes over when the owner exits. Each dashboard registers `shared/run/instance_<profile>.json` with a PID that `live_instances()` checks before trusting the file. The port guard asks `/api/instance` who holds the port and **refuses to kill an instance of a different profile**; it only replaces the same profile after a y/n prompt, escalating `kill` → `kill -9` after 5 s. This is the direct fix for the Oct 22 finding "a second instance `kill -9`'d the first's server".
- **Alerting follows the running dashboards.** `alerting_models()` reads the live registry and holds back transitions for phones with no open dashboard, while the DB and alert state still record every model; a registry failure returns `None` so alerts are never silenced by mistake. Alerts are gated by a store whitelist that is the union of every port's `enabled_stores`.
- **Apple fulfillment JSON is parsed, not scraped.** `parse_raw_apple_json` walks `body.content.pickupMessage.stores[].partsAvailability[part].pickupDisplay == "available"`, parses `storePickupProductTitle` ("iPhone 17e 256GB Soft Pink") into model/size/colour after normalising non-breaking spaces, maps display names to codes via the profiles' `model_metadata` first and a 15-entry fallback table second, and composes a direct checkout URL `buy-iphone/<slug>/<inches>-inch-display-<size>-<colour>-unlocked`. Store names are canonicalised ("Apple SoNo Collection" / "The SoNo Collection" → "SoNo Collection") before merging into every `latest_*.json`.
- **The dispatcher is multi-channel with an audit trail.** Every delivery appends a JSONL event (timestamp, event key, provider, outcome, HTTP status, error) to `shared/alert_events.jsonl`. ntfy posts to the server root with the topic in the JSON body (the JSON publish API), uses a crown/zap tag scheme so Pro Max and Pro are visually distinct, attaches the maximum three action buttons (Chrome, Safari, DuckDuckGo), defaults `click` off to avoid hijacking the card, and **fails over to a secondary ntfy URL with a Bearer token**. The Chrome link is `googlechromes://…` on purpose: the guide explains that plain `https://apple.com` links trigger iOS Universal Links into the Apple Store app, which drops the configured cart. In-stock events are sent individually (`skip_batchable`) and then as a "top 5" batch of per-platform structured cards spaced 1.5 s apart. Desktop alerts copy the ZIP to the clipboard.
- **The dashboard API is small and complete.** GET side (first pass) plus POST: `/api/dump` accepts a single object, an array or a concatenated multi-object stream, decodes with `raw_decode`, and **cumulatively merges `partsAvailability` by store** unless `?clean=true`; `/api/alerts/targets` separates per-port targeting keys (written atomically to `shared/alerts/<profile>.json`) from shared channel settings (written to `alert_targets.json`, `.env` and this instance's own YAML only, with a two-zone banner); `/api/config` saves the in-browser YAML editor after `yaml.safe_load` must return a mapping; `/api/alerts/reevaluate` reloads `cli.alerts`, re-parses the last Apple payload or falls back to the newest DB batch, and re-runs `compare()` with baseline suppression off; `/api/alerts/test` sends a sample built from this port's own first model/colour/size to telegram, discord, primary or secondary ntfy. Every response disables caching and sets CORS `*`.
- **The front end is one 4,181-line file with 67 functions**: alert-target matrix (sizes, stores, custom variants per model), store-priority cycling with presets, cooldown presets, telemetry modal, "Manual JSON Super Dump" panel, Active Configuration Editor, Upstream Feed Diagnostics, Mobile Alert Engine Health, history with size/colour chips, Safari-log polling, fast-buy and copy-ZIP toast. No framework, no build step.
- **The CLI (`click`) has nine commands**: `once`, `watch`, `sync`, `export`, `verify-links` (prints every composed checkout URL), `audit-fulfillment` (live HTTP status, latency, ZIP, store-by-store slot table), `debug-feed`, `alerts-status`, `alerts-test --provider`. Global options override colours, sizes, `Color:Size` variants, models and ZIP rotation.
- **Profiles are the extension point.** 12 YAML files under `shared/profiles/` (16, 16 base, 16 Pro, 17, 17 base, 17 Pro, 17e, 18 base, 18 Pro, 18 template, Duo, minimal), each with its own port (the Oct 22 plan assigns 8200/8201/8204/8210/8211/8220/8221/8299), 4 anchor ZIPs, a **35-store registry** with Apple store numbers (R139, R068…) and region tags including `tax_free`, colour/size slug maps, `model_sizes`, and artifact paths; channel secrets are referenced by env-var name (`url_env: NTFY_URL`), never inline. `start.sh` has a 3-prompt "new product profile" wizard that clones the 18 template and rewrites models/metadata/artifacts, a snapshot-to-profile action and timestamped `_config_v3.0_<ts>_bk.yaml` backups before every hot-swap; hot-swap is refused while a default-config dashboard is running.
- **A native macOS app exists** (`app/`, Swift Package, SwiftUI, macOS 13+, 561 lines in four files) that watches `shared/latest.json`, offers a refresh picker from 5 s to 5 min and colour/storage filters. Its README still says v2 and "seven stores", so it predates the 35-store rewrite; it is a thin viewer, not the product.
- **Tests:** 23 `tests/` entries, 13 live files after removing the `_v0.x` copies (17e profile, alert model identity, alert profile label, alerts-and-config flow, harvester smoke, heroku-off, live verification, log links, notification dump, parser alert scope, parser names from profiles, refuse-db-commit, test-alert sample) plus `sample_apple_dump.json` as a fixture. First-pass result stands: 51 unit tests OK on a scratch copy.

**Doc defects seen (for the proposed-edits list, not the résumé):** `CONFIG_ARCHITECTURE_AND_PROFILES.md` describes the "Dual-Write Engine" writing to `config.yaml` **and** the active profile; the code now writes only the instance's own config (server.py comment "never another profile's"). The same guide and `start.sh`'s menu say "28 Apple Retail Stores" / "28 confirmed store ZIPs" while every profile carries 35. `SYSTEM_STATE_HANDOVER.md` is titled "v4.0 / v4.1", names `web/index_v4.0.html` and says "WebSocket/polling"; the app is v3.9.9.9, has one `index.html`, and polls over plain HTTP. `cli/main.py`, `store_profiles.py` and `app/README.md` still say "v2". `NOTIFICATION_SETUP_GUIDE.md` claims "Production Ready" and "zero missed stock alerts"; keep "continuously polled" wording outward.

**⚠️ Additional heads-up (security; nothing changed by me):** (1) `docs/guides/NOTIFICATION_SETUP_GUIDE.md` repeats the Telegram bot token in **four** code blocks (`.env`, `~/.zshrc`, `~/.bashrc`, `docker run`) and prints the chat ID, on top of the README occurrence noted above; it is tracked. (2) `/api/alerts/targets` is the mechanism that wrote those secrets into `.env` and `shared/alert_targets.json` in the first place: the UI posts the token and the server persists it to disk. (3) `web/server.py` binds `0.0.0.0` by default (log line: "Tailscale & Localhost enabled") and answers every request with `Access-Control-Allow-Origin: *`; `/api/config` writes whatever repo-relative filename the client names after a `replace("../", "")` that a `....//` sequence defeats, so any LAN/Tailscale peer or any web page the operator has open can rewrite files under the repo. Suggest `SERVER_HOST=127.0.0.1` (the env var already exists), an allow-list of writable config paths, and dropping the wildcard CORS. (4) The ntfy topic names in the guides and code act as shared secrets on public `ntfy.sh` (anyone who knows one can publish or subscribe); do not quote them in outward material.

**Résumé additions from this pass:** (1) "designed the multi-process runtime: four daemons per product profile, lock-elected singleton harvester with standby takeover, a PID-verified instance registry, and a port guard that never kills another profile's server"; (2) "parsed Apple's fulfillment JSON into model/size/colour/store events with canonical store names and composed direct checkout URLs, gated by which dashboards are live"; (3) "multi-channel dispatcher with per-delivery JSONL audit (provider, HTTP status, error), ntfy primary→secondary failover, three-action cards and Chrome deep links chosen to defeat iOS Universal-Link hijacking"; (4) "a nine-command operations CLI (live fulfillment audit with latency and HTTP status, link verification, provider tests) alongside a 67-function single-file web cockpit"; (5) "added a new phone line by YAML profile only: 12 profiles, unique ports, 35-store registry with Apple store numbers, template-driven profile wizard".

---

## 7. amtrix_claude_subscription_tool (AMTrix Subscription Tool): v0.0.6, 19 commits, last commit 2026-10-11

**Read in full:** README (v0.0.5), `docs/PROGRESS_2026-10-11.md`, CLAUDE.md, `src/scope_guard.cjs` (127), `src/remote_mode.cjs` (166), `src/remote_policy.json`, `src/amtrix_close.cjs` (161), `src/tui_subscription.sh` (438), `src/skills/diagnose/SKILL.md`, `workbench/amx_kit/README.md` (opening).
**Not read:** `prepare_skill.cjs`, `auto_backup.cjs`, `amx.cjs`, the 10 slash-command `.md` files (names only), test bodies (results only), `docs/v0.0.x/` records, HOOKS_EXPLAINED, BEST_PRACTICES_REMOTE_AND_MAX. `.state/` deliberately never read (private login).
**Size:** 7,346 lines across `src/*.cjs|sh`, `tests/`, `workbench/amx_kit/*.cjs`, `src/commands/*.md`.

### What it is
A standalone launcher (bash TUI + Node hooks) that starts Claude Code on a **Max subscription** with pinned cost and safety settings, plus a one-file skill review workbench. It sits next to Claude Code Center (the API/OpenRouter lane) and is deliberately separate from it.
- **Billing/route pinning** (`tui_subscription.sh`):
  - `clean_env` unsets every `ANTHROPIC_*`, `CCC_*`, `CLAUDE_CODE_USE_*` and caching override, then forces `api.anthropic.com`, a 1-hour cache TTL, an Opus subagent model and no model fallback.
  - `check_auth` refuses to launch unless `claude auth status` reports `claude.ai` + a Max subscription.
  - It refuses an existing config that carries an API key, auth token, proxy URL or `apiKeyHelper`.
  - Project `.claude/settings*.json` are loaded **only if** they can't reroute billing, model or cache (jq gate). Otherwise the launcher falls back to user settings and says why.
  - Three config lanes (menu C): the tool's private `.state`, `~/.claude-max`, or `~/.claude`. The code never writes settings into the last two.
  - The launch can be copied as one portable string (node-built `$'…'` quoting, because bash 3.2 `printf %q` mangles some characters).
- **Scope guard** (`scope_guard.cjs`, PreToolUse hook):
  - Path containment with realpath; denies symlinks, `.state` and credential filenames.
  - A verified SHA-256 pre-change backup beside every edited file (one per file per session).
  - Profile-based write rights across 9 profiles (work, architecture, implementation, verification, discussion, resume, resume_replay, skill_review, skill_update).
  - A guard-integrity regex: no shell command may rewrite the guard, its policy or the private state, even if the human approves.
- **amx-auto-mode** (`remote_mode.cjs` + `remote_policy.json`):
  - A shell-command classifier for phone/remote sessions that returns allow / ask / block.
  - It splits commands at `&& || ; |` outside quotes, detects out-of-project paths, `>`/`>>` redirect targets, `$(…)`/backticks and `sed -i`.
  - 12 always-blocked classes (push, `rm -r`, `reset --hard`, installs, sudo, chmod, keys/.env, hook rewrites, system-level).
  - It's switched **only by the human's typed message**, read by a UserPromptSubmit hook. The model can't change it, because the guard denies `.state`.
  - Every decision is logged to a markdown table.
- **`/wrapup` close engine** (`amtrix_close.cjs`):
  - Stamps changed living docs, runs the tests and writes a measured `Evidence_vX.Y.Z.md`.
  - Writes honest stubs for missing record types ("lockstep" with the previous version folder).
  - In a project that has AMTrix Plan, it hands over to `plan_hub.py finish`, so only one engine runs.
- **Skill workbench (menu 10/11):** an immutable snapshot, an editable candidate and a SHA-256 manifest. The live source is never given to the model. Files over 1 MiB, symlinks and credential files are rejected.
- **Packaged methods:** 10 slash commands (discuss/research/makeplan/implement/verify/catchup/wrapup/comments/amx/amx_claude) and a `/diagnose` skill (3 ranked hypotheses with file + function + mechanism, a human gate, the smallest patch, revert-before-retry, stop after 2 failed patches).
- **amx-kit** (`workbench/amx_kit/`): the same auto-mode + backup idea, rebuilt as a 2-file, dependency-free hook to drop into any project (the Lego-piece direction).

### Verified vs claimed
| Claim | Status |
|---|---|
| 162/162 offline + mocked checks (PROGRESS Oct 11) | ✅ **Measured today: 162/162**, exit 0, on an isolated copy (no `.state`, HOME redirected). The JSON still says `live_subscription_verified: false` (correct; no live login in tests). |
| amx-kit 31/31 | ✅ **Measured today: 31/31** on the same copy. |
| `bash -n` on both shell scripts "never measured" | ✅ **Measured today:** `SHELL_SYNTAX_OK` for `tui_subscription.sh` and `run.sh`. |
| "Live-verified Oct 4: slash commands, /diagnose, scope guard block" | Stated in the README/PROGRESS; I didn't re-run it (it needs a live Max session). |
| amx-auto-mode on a phone session, menu C `max`, menu R off | ❌ **Still pending a live check**, per the project's own runbook (Step 5). |
| Guard "cannot be bypassed" | The project itself says it's **not an OS sandbox**: it doesn't parse every shell side effect, and managed policy can disable hooks. Its wording is honest; keep it that way on the resume. |
| VALIDATION.json | Still reports v0.0.5 (85 checks); the newer 162 figure lives only in PROGRESS/Evidence. Minor staleness. |

### Heads-ups (written here only; nothing changed)
- **The amx-kit was never moved.** `AMTRIX-TOOLS/amx-kit/` exists but is **empty** (created Oct 12 00:45). The only copy is `workbench/amx_kit/`, and its 3 files have **uncommitted** changes. PROGRESS says the workbench copy "gets removed once he confirms the copy", so **don't delete it**: it's the only copy.
- 5 files are uncommitted (CLAUDE.md, PROGRESS_2026-10-11.md and the 3 kit files).
- The project notes say Amit "doesn't care about this subscription tool long-term". Its value for the resume is the **patterns**, not the product.

### Resume-ready takeaways
- **Cost-governed agent launcher:**
  - pins the billing route, model, subagent model and the 1-hour prompt cache
  - strips inherited API/proxy env vars
  - checks the account tier before launch
  - rejects project configs that could silently reroute billing
- This is the "know where every token is billed" discipline that pairs with Claude Code Center's API lane. **Story: two lanes, subscription and own-proxy, with no cross-contamination.**
- **Agent guardrails as code, not prompts:**
  - PreToolUse/UserPromptSubmit hooks with path containment and verified SHA-256 backups before every edit
  - a quote-aware shell classifier (allow/ask/block)
  - a human-only toggle the model can't reach
  - an audit log of every decision
  - 162 automated checks
- **Evidence-first session close:** a test-measured evidence file plus lockstep record stubs, handing over to AMTrix Plan when it's present. This shows the same "measured, not typed" principle across tools.
- **Packaged debugging method** (`/diagnose`): hypothesis-ranked root-cause analysis with a human gate and a loop-breaker. These are modular LLM instruction sets, not one-off prompts.
- **Lego-piece evolution:** the guard was refactored into a 2-file, dependency-free, drop-in kit (amx-kit) that any project can use without the launcher.
- **Wording caveats:**
  - Say "hook-enforced guardrails", not "sandbox".
  - Say "offline + mocked test suite (162 checks)"; live remote/phone behavior is still unverified.
  - Present amx-kit as "built and tested (31 checks), not yet deployed".

---

## 8. amtrix-notify-bus + amtrix-notify-bus-linux (self-hosted ntfy): Aug 26 → Sep 19, 2026; not git repos

**Read in full:** every file in both projects. That's QUICKSTART, docker-compose, `config/server.yml`, Caddyfile, `bootstrap.sh`, `notify_control.sh` (Linux only), `notify.sh`, `health.sh`, `publish-test.sh`, `clients/notify.py` and the example. Secret values were redacted while reading.
**Not read:** `.env`, `data/config/ntfy-amit.env` (credential file), `backups/*.tar.gz` (ntfy state), the bundled `.zip`.
**Size:** ~300 lines each. This is infrastructure-as-config, not an app.

### What it is
A Docker Compose ntfy push-notification server that any script, cron job or app can publish to over HTTP. It runs on an Apple Silicon Mac or Ubuntu, and is deliberately independent of the iPhone checker (which uses it as one channel, with failover).
- **Mac variant:** binds `127.0.0.1` only (local first).
- **Linux variant (the deployed one):**
  - public HTTPS through a Caddy reverse proxy (`--profile public`) on an `amtrixsolutions.com` subdomain
  - `behind-proxy`
  - an APNs upstream via ntfy.sh for instant iPhone wake-up
  - login enabled, signup disabled, `auth-default-access: deny-all`
- **Security model:**
  - per-identity users (admin / publisher / mobile)
  - topic ACLs (publisher = write-only, phone = read-only)
  - a random 36-hex topic name
  - Bearer-token publishing
  - the QUICKSTART says not to go public until ACLs and HTTPS work
- **`bootstrap.sh`:**
  - detects or provisions the container runtime when asked (`--install-runtime`): Colima + Docker CLI on macOS (no Docker Desktop), docker.io + compose plugin on Ubuntu
  - rewrites `base-url` from `.env`
- **`notify_control.sh` (Linux):**
  - **desired-state drift repair** (`ensure`): re-enforces deny-all, login on and signup off, restarts, polls `/v1/health` up to 30 s, and restores the user ACL
  - interactive password rotation (never echoed; secret file `chmod 600`)
  - `status`
- **Ops hygiene:** state backups (7 tarballs, Aug 26 → Sep 19); `publish-test.sh` sends a message explicitly labelled "TEST DELIVERY — NOT INVENTORY".
- **Integration contract:** publish only from a verified `false/unknown → true` transition, never from a poll loop. This is the same edge-triggered rule the iPhone checker's `AlertStateStore` enforces.

### Verified vs claimed
| Claim | Status |
|---|---|
| "Bootstrap starts ntfy only on loopback" (QUICKSTART, shared by both) | ✅ Mac variant. ⚠️ The Linux compose binds **all interfaces** on 2586 (mitigated by deny-all + login, and fronted by Caddy). The QUICKSTART text wasn't updated for the Linux variant. |
| Multi-arch (arm64) | Plausible (upstream image); not tested here. |
| Live server | Not probed (no network calls made). The config and the iPhone checker's channel config show it was in use. |
| `notify_control.sh` usage comment | Says `ntfy-control.sh`, but the file is `notify_control.sh`. `ROOT` is hard-coded to `$HOME/amtrix-notify-bus-linux` (the server path). Cosmetic. |

### Resume-ready takeaways
- **Self-hosted, secure notification infrastructure:**
  - a Dockerized ntfy server behind a Caddy TLS reverse proxy on his own domain
  - deny-by-default ACLs, least-privilege publisher/subscriber identities, token auth
  - an APNs upstream for instant mobile push
  - one HTTP contract (shell + Python client) reused across his tools
  - This is a Lego piece: any project gets push alerts by setting two env vars.
- **Ops automation:** an idempotent desired-state "ensure" script (config drift repair, health-gated restart, ACL restore), secret rotation without echo, state backups, and cross-platform runtime bootstrap (Colima on Apple Silicon, apt on Ubuntu).
- **Wording:** "self-hosted ntfy notification bus (Docker, Caddy/TLS, ACLs)". Don't claim HA. It has one instance; failover lives in the client (iPhone checker), not the server.

---

## 9. AMTRIX-Patch-TUI (safe versioned patch utility): Aug 7 → Aug 11, 2026; not a git repo

**Read in full:** both sources (`src/amtrix_patch_tui.js` 3.6 KB and `src/amtrix_patch_tui_vbk.js` 4.6 KB, minified one-liners, read after reformatting), both `.command` launchers, `patches/README.md`, the template manifest and the routing manifest.
**README:** I read the section headings and the SHA/STOP lines; it's 412 lines, older (Aug 11) and matches the code apart from the gap below.
**Not read:** the other 5 v2.4.8 manifests (same shape, all targeting claude-code-center config; `profiles.env` is a target name only, so no secret values are in them).

### What it is
A zero-dependency Node TUI that applies **declarative JSON patch manifests** to a config or code file **without ever overwriting the original**. It writes a sibling `name_vX.Y.Z.ext` and refuses if that file already exists.
- **4 ops:** `replace_literal`, `regex_replace`, `insert_after` and `insert_before` (anchor-based).
- **Exact-count gate:** every edit declares `expected` matches (default 1). If the count is wrong, it's STOP and nothing gets written.
- **Workflow:** Load+validate → Plan (before/after SHA-256 + READY/STOP per edit) → unified diff (`diff -u` via a temp file) → create the versioned file.
- **Used for:** the claude-code-center v2.4.8 release, as 6 ordered manifests (proxy_server, models, model_profiles, profiles.env, routing, README).
- **Ancestry:** this is the "visible versioned backup, never overwrite, exact-match edits" law that later shows up in AMTrix Plan's backups and the subscription tool's scope guard.

### Verified vs claimed (smoke test on a scratch file today)
| Claim | Status |
|---|---|
| Plan shows before/after SHA-256 and READY per edit; output is versioned and the original is untouched | ✅ **Measured:** `● READY v (1/1)`, `t_v1.0.1.json` created, original unchanged. |
| "If a source SHA-256 lock is set, the target must match" (README §Validation) | ⚠️ **Only in `amtrix_patch_tui_vbk.js`** (measured: `PATCH STOPPED: SHA-256 source lock mismatch.`). The **default launcher** `amtrix_patch_tui.command` runs `amtrix_patch_tui.js`, which **ignores `source_sha256`**: with a wrong lock it still produced the file. The `_bk.command` launcher runs the same file plus `"$@"`, so it doesn't reach the vbk build either. |
| READY/STOP table lists every STOP | Partly: in both builds the first mismatching edit throws during load, so you see one STOP message, not a full table. It's still fail-closed. |
| Tests | None in the project. |

### Resume-ready takeaways
- **Built a fail-closed, declarative change-management tool for config releases:**
  - JSON manifests with exact-match counts
  - SHA-256 before/after fingerprints (plus an optional source lock)
  - a unified diff preview
  - versioned outputs that never overwrite the source
- He used it to ship a multi-file gateway release (claude-code-center v2.4.8).
- **Story value:** this is the early "safe change" primitive that later grew into AMTrix Plan's evidence and backup laws. It's good for showing an engineering *philosophy*, not as a headline product.
- **Wording:** claim "SHA-256 fingerprinted plans" safely. Claim "source-lock enforcement" only after pointing the launcher at the vbk build (not done; no edits made).

---

## 10. Vision LLM Comet Trader / AMTrix Vision OS (`complex-amtrix-engineered-prompts-v1/VISION_LLM_COMET_TRADER/local_autotrader`): v13.8.4–v13.8.5, 39 commits, Jan 15 → Aug 7, 2026

**Canonical copy:** this folder (latest commit `bb343c4`, Aug 3; docs to Aug 3 22:15; files to Aug 7).
- `BACKUP_VISION_LLM_COMET_TRADER/` is older (last file Mar 17) and holds 30+ `local_autotrader_v9.x–v12.9` snapshot folders plus the early protocol XMLs (VISION_LLM_PROTOCOL v3.2–v3.9.5, AGENTS v3.5–v4.0). It's history, not a separate project.
**Read in full:**
- docs: README, PROJECT_STATE, CLAUDE.md, `docs/v13.8.0/Walkthrough.md` (all 5 iterations v13.8.1–.5), `docs/v12.9.8/BENCHMARK_AND_CREDIBILITY`, the opening of `VISION_CRUCIBLE_BUILD_SPEC`
- code: `core/run_trader.py` (1,042), `engines/routine_engine.py` (980), `engines/vision_engine.py` (590), `core/config_contract.py`, `modules/risk_mitigator.py`, `modules/action_verifier.py`, and the routing core of `utils/api_loader.py` (`generate_llm_content`, `get_model_routing`)
**Structure only (signatures):** `visualizer/src` (RoutineBuilder.jsx 1,696, VisionCrucible.jsx 1,426, App.jsx 1,404, SpatialCanvas.jsx 820), `proxy/` (the early copy of the Claude Code Center gateway; see §1).
**Not read:** `hands_library.py`, `coord_utils.py`, `notification_zone.py`, `intent_logger.py`, `setup_wizard.py`, the `tools/*` advisors, the 37 routine JSONs, the older `docs/v9–v13.7`. Secrets were not opened (see heads-up).
**Size:** ~14 K lines of Python (engines/core/modules/utils, including in-tree backups), ~5.9 K lines of current React, a 2.9 K-line proxy.

### What it is
A **vision-driven desktop automation framework** (macOS). It sees the screen, decides with a multimodal LLM and acts with PyAutoGUI. The first target is TradingView futures (NQ/MNQ/ES), but the design is app-agnostic.
- **Cartridge architecture** (`Apps/<name>/`): config, asset manifest, system prompt, strategy text, reference images, routines and logs per app. Swapping the cartridge swaps the target app.
- **Hybrid "Hands vs Brain" split** (the main design idea):
  - A deterministic JSON **routine engine** does the fast micro-actions: about 30 ops (CLICK, DRAG, WAIT_IMAGE, SCENE_CHECK, VERIFY, OCR, LOOP/WHILE/IF/SWITCH, CALL, SECTION, APP_CONTROL, LLM_EVAL, LLM_DECIDE…).
  - **FREP2 branching** is required on every step: `on_success`/`on_fail` = CONTINUE / ABORT / BREAK / HALT / `>goto` / `@call` / inline op.
  - Critical sections with remediation and retry.
  - A black-box **failure snapshot** (capped at N).
  - Conditions go through a **sandboxed eval** (200-char cap, character whitelist, no builtins, 6 safe functions).
  - The LLM is consulted at low frequency to judge strategy state and fill variables.
- **Trading loop** (`run_trader.py`), per cycle:
  1. reset the chart axes
  2. vitality check (buy/sell buttons visible)
  3. deterministic pixel scan of price/stop lines
  4. a **"Position Reality"** check (a stop above price = SHORT, below = LONG) compared with the last action, flagging "EXTERNAL FLIP"
  5. an **eyes-first visibility map** sent to the LLM as context
  6. a **deterministic risk rule that bypasses the LLM** (2 order boxes = orphaned, 4+ = ghost orders, either way FLATTEN immediately)
  7. LLM decision as JSON
  8. execute
  9. **intent → outcome verification** (log intent, screenshot the notification zone, LLM-read the notification, then keyword-match for BUY/SELL bracket legs and count ≥3 for FLATTEN; a mismatch skips the cooldown and re-scans)
  - **Trailing-stop safety:** direction-aware (only the correct stop type), a 600 px distance filter, and "destination crosses price → abort". It refuses to act when position reality is unknown.
- **Multi-provider LLM router** (`api_loader.generate_llm_content`):
  - ordered primary + fallbacks from config aliases
  - routes by prefix to Ollama / LM Studio (local), Vertex native, AI Studio or OpenRouter
  - an optional local proxy (the Claude Code Center gateway) with automatic fall-back to native routing
  - This is where the gateway/BYOK work began (`proxy/LLM_BluePrint_Enhancment_VERTEX_BYOK.md`, plus `tests/test_*_vertex*.js`).
- **Config contract migration (v13.8.x):**
  - an `AssetSpec` dataclass with alias lists (`FIELD_IMG_TO_MATCH = ["img_to_match","files","file"]`)
  - a repo scanner (`config_contract_audit.py`) with a measured baseline of 207 raw reads → 0 in migrated files
  - 80 shared constants
  - The written root-cause analyses are good: BUG-006 "only Northstar matches" (vision_engine read legacy keys), BUG-008, and a left/right default inconsistency.
- **React visualizer:**
  - a schema-driven **routine builder** ("AST compiler": drag-in templates auto-wrapped in `SECTION` with ID-namespaced placeholders and variables)
  - SpatialCanvas, for drawing search zones over Retina screenshots
  - **Vision Crucible**: a seeded-PRNG 3×3 visual-recognition stress-test game with honest geometry scoring (native image size kept, fuzzed scale, reroll on `ASSET_TOO_LARGE_FOR_CELL`)

### Verified vs claimed
| Claim | Status |
|---|---|
| Real use | ✅ **Measured:** 270 audited runs, **28,668 JSONL audit entries** (Jan 15 → Aug 3, 2026), 37 routines, 36 reusable templates, 31 verification screenshots. The TradingView cartridge is the only real one (the others are TEST/backup). |
| "Zero-latency RAM cache; flushed on CLICK/DRAG" (CLAUDE.md) | ❌ `clear_cache()` is a **no-op** and `cached_frame` is never used; every find re-captures the screen. |
| "Post-action verification" in VisionEngine | ⚠️ It only checks that the **cursor** sits where it clicked. The real outcome check is the notification-reading step in `run_trader.py`, which is LLM-read plus keyword match. |
| RiskMitigator / ActionVerifier (severity ladder, 3-mismatch session halt, price-delta tolerance) | ⚠️ Well-designed modules, but **not imported** by the live loop (only by each other). The live loop uses its own inline deterministic risk rule and keyword verification instead. |
| OCR op | ❌ Calls `vision.read_text`, which doesn't exist in VisionEngine, so it fails at runtime (caught and routed to `on_fail`). |
| `LLM_DECIDE` | Copies every key the LLM returns into routine variables, so the LLM can overwrite any variable. That's a design caveat for "LLM only fills forms". |
| "Immune to underlying code changes" / "9.5/10 credibility" (BENCHMARK doc) | Self-assessment written by an LLM, not measured. It's immune to DOM changes but sensitive to **visual** changes (template matching plus calibration; the project's own BUG-006/007 show it). Don't quote it. |
| Tests | Measured on a scrubbed copy (no `api_config.json`, no credentials): `tests/test_api_loader.py` **1/3 pass**. The 2 failures need the private `api_config.json`, which wasn't copied on purpose; the mocked Vertex-routing test passes. `tests/test_menu_components.py` **2/2 PASS**. Not run: `tools/component_test.py` (moves and clicks the real mouse), the `tests/test_*.js` (live Vertex/OpenRouter calls, billable), `VisionCrucible.test.jsx` (3 vitest checks, node_modules not copied). |

### 🔐 Security heads-up (written here only; nothing changed)
- `config/OR_Vertex_BYOK_Credential.json` is **tracked in git**. Its keys are a **Google Cloud service-account JSON, including `private_key`**; I read the key names only, never the values. `config/profiles.env` (38 vars) is also tracked.
- Both were committed in `5294f05` (Jul 29), and that commit **is on `origin/main`** (`github.com/amit-malhotra1/vision-llm-amtrix-agents`).
- An unauthenticated GitHub API request returns **404**, so the repo is private (or renamed). It isn't publicly exposed, but the key now lives in GitHub history.
- **Recommend:**
  - rotate or disable that service-account key in GCP
  - remove both files from tracking and add them to `.gitignore` (`api_config*.json` is already ignored)
  - consider a history rewrite before ever making the repo public
- Local is 3 commits ahead of origin.

### Resume-ready takeaways
- **Built a vision-LLM desktop automation framework (vision-RPA)** that operates any GUI without APIs or DOM access:
  - a multimodal LLM perceives and decides
  - a deterministic JSON state machine executes
  - a pluggable "cartridge" per target app
  - 28.6 K audited actions across 270 runs on a live trading UI
- **Safety architecture for LLM-in-the-loop actions:**
  - deterministic eyes-first pre-scan
  - LLM-bypassing hard risk rules (orphan/ghost-order flatten)
  - a position-reality cross-check against model memory
  - intent → outcome verification from on-screen notifications
  - direction-aware guard rails on every drag
  - failure black-box snapshots
  - This is "the LLM fills forms, the engine executes", which is exactly the FDE talking point for high-stakes automation.
- **Built a routine DSL + visual builder:**
  - ~30 ops with mandatory success/fail branching (goto/call/inline)
  - a sandboxed expression evaluator
  - encapsulated drag-in templates with auto-namespaced variables
  - a React builder with a Retina-accurate zone-drawing canvas and a seeded visual-recognition benchmark (Vision Crucible)
- **Multi-provider LLM routing with ordered fallbacks** (Gemini/Vertex native, OpenRouter, local Ollama/LM Studio, optional own proxy). This is the **origin of the Claude Code Center gateway** and the Vertex BYOK work.
- **Engineering discipline:** a schema contract and alias layer that removed 207 raw config reads, with a scanner as the exit gate and root-cause write-ups. Versioned Task/Walkthrough/Diagnostics/Audit records per iteration (the pattern AMTrix Plan later formalized).
- **Wording caveats:**
  - Say "vision-driven UI automation", not "autonomous trader". Don't imply profitability (no P&L evidence anywhere).
  - Don't claim the RAM cache, the RiskMitigator severity ladder or OCR as live features.
  - Avoid "immune to UI changes".
  - Mention that it runs on a demo/paper account only if he confirms that. Not verified.

---

## 11a. Prompt Mermaid Dashboard (`complex-amtrix-engineered-prompts-v1/PROMPT_MERMAID_DASHBOARD`): v16.9.95 (Nov 12, 2025 → Feb 19, 2026), plus the Antigravity Hub / Universal Context Router v15 (Jan 21–22, 2026) in the same folder

**Git:** 6 commits, last `8810d1b` on 2026-01-10. Remote `github.com/amit-malhotra1/prompt-mermaid-dashbaord` (sic) returns 404 to an anonymous request, so it's private. **None of the v16.9.x folders or `.agent/` is committed** (59 uncommitted or untracked paths). The docs (README/GUIDE/CHANGELOG) describe v16.9.9 (Jan 20); the code is v16.9.95 (Feb 18–19).

**Read in full (code):**
- `v16.9.95/js/app.js` (1,716), `js/xml_sanitizer.js` (297), `js/neonify.js` (503), `brand_loader.js` (734), `config/bios.js`, `css/engine.py`, `css/brands/amtrix_2026.yaml`, the `index.html` structure
- `.agent/services/proxy_server.js`, `.agent/services/start_mcp_proxy.sh`, `.agent/interfaces/antigravity_hub.sh` (v15, 386 lines), `.agent/deploy.sh`, `.agent/skills/router/SKILL.md`, `.agent/docs/ARCHITECTURE.md`, `.agent/docs/PENDING_FIXES_AND_UNIT_TESTS.md`
- `universal_context_v14_THE_BEST.py` in full, plus the diff to `.agent/core/universal_context.py` (v15)

**Read (docs):** README/GUIDE/CHANGELOG v16.9.9, ECOSYSTEM_MAP, STRESS_TEST suite.
**Not read:** `css/styles.css` / `adaptive_brand.css` (presentation only), `Deep_Research_on_mermaid_syntax.md` (a 46 KB research note), the ~9 older v16.x snapshot folders and `old_versions/`, Executive_summary / business_strategy (Nov 2025).

### What it is
**1. Prompt-to-diagram workbench** (single-page, offline-capable via `file://`; Mermaid, CodeMirror and marked from CDNs):
- **XML → Mermaid compiler:**
  - recursive `generateMermaidFromXml` turns any XML prompt or protocol into a flowchart
  - auto-detects state / block / mindmap / sequence modes from the root tag
  - sibling auto-indexing (`STEP_1`, `STEP_2`) so filter IDs stay stable
  - a per-node **filter tree** to toggle the visibility, shape (14 Mermaid shapes), colour and connector type of any branch; children are disabled with their parent
- **"BIOS" config:** `config/bios.js` maps tag → shape/colour/label, plus the connection and diagram-type lists. Users can add a tag without touching code.
- **Hybrid rendering trick:**
  - Embedded `<svg>` nodes and long-text "smart cards" are base64-encoded into an `svgLookup`.
  - Mermaid lays out a dot-padded text **scaffold** sized to the asset (tunable char-width/line-height with a ratio lock).
  - The placeholder is swapped for the real image after render.
  - This puts arbitrary SVG/Markdown *inside* Mermaid nodes, which Mermaid can't do natively.
- **Smart Import ("Parlor"):** cleans raw LLM chat output.
  - extracts fenced blocks
  - strips the preamble
  - converts JSON to XML
  - escapes stray `&`, `<`, `>`
  - repairs `<STEP>…<STEP>` missing slashes
  - enforces unique `name` attributes
  - reports each fix with its line number
- **Asset templates:** `{{icon_db}}`, `{{ai_pandit}}` (an AI Pandit chart SVG) expand from `js/assets.js`.
- Exports SVG/PNG/code; LocalStorage persistence; `#content=` base64 share links; a crude Python/Rust → classDiagram "transpiler"; resizable panes; a neon theme toggle.
- **Brand layer:** `brand_loader.js` (a drop-in "Studio Tuner": 3 identity presets, per-component radius/blur/border/opacity, a VFX matrix, export as JSON) and `css/engine.py` (YAML brand file → templated CSS kit). This is the seed of the later **amtrix-identity-engine** / amtrix-studio.

**2. Antigravity Hub v15 / Universal Context Router** (`.agent/`, deployed to `~/.antigravity` by `deploy.sh`):
- **`universal_context.py`**, a CLI or JSON-request context packer:
  - file tree (depth ≤3, ≤20 files per dir, refuses to run from `~`)
  - `~/.antigravity/memory.md` + `rules.md`
  - `git diff HEAD` (10 K cap)
  - target files under a **token budget** (`--limit`, ~4 chars/token, with truncation markers)
  - session history (`--session`, last 20 turns)
  - routing to the **local :8080 proxy** (gemini/openrouter/anthropic/local) or **direct** (Gemini, OpenAI, Anthropic, OpenRouter with `include_reasoning`, Ollama)
  - a TCP health check before sending, normalized token usage, and latency / tok-per-second metrics
- **`proxy_server.js`:** an Express "Super Proxy" with one `/ask` schema `{target, message, context, history, modelOverride}` and 4 provider adapters.
- **`antigravity_hub.sh`:** a TUI to start, stop and configure the proxy (masked key display, Ollama status) and run a multi-turn chat wizard. Context gathering is **off by default ("Safety Mode")** unless a router model is set.
- **Router skill (`SKILL.md`):** IDE agent instructions to write a `_context_request.json` and shell out to the core, so a cheap model picks the files and a strong model answers (the "Fast brain / Slow brain" design in ARCHITECTURE.md).
- **Lineage:** this is the **direct ancestor of the Vision trader's `proxy/` and the Claude Code Center gateway** (§1, §10). Same idea (own the proxy, route by target), at an earlier stage.

### Verified vs claimed
| Claim | Status |
|---|---|
| Hybrid view renders SVG + Mermaid in the centre and a tree on the right (CHANGELOG "✅ tested") | ⚠️ The tree and the SVG blocks render, but `renderHybridVisualization` ends with `mermaid.init(undefined, mermaidNodes)` and **`mermaidNodes` is never defined** (grep). It throws a ReferenceError, so fenced Mermaid blocks in hybrid input are left as raw text in v16.9.95. It probably regressed after the v16.9.9 test. |
| Sanitizer "mind reading": "Check if database is online" auto-gets a DECISION/DB shape (GUIDE) | ❌ `guessShape()` exists but is **never called**. Shapes come only from exact tag names in BIOS. The `HEURISTICS` map is flattened into the tag map as strings, so it has no effect. |
| `neonify.js` "Neon Glass" transformer (CLI) | ❌ **Measured:** `node js/neonify.js` throws `TypeError … is not a function` on any input. Missing commas in `buildInitBlock()` turn adjacent template literals into tagged-template calls. index.html also loads it as a browser script, where `module.exports` is undefined. The live neon toggle uses a separate inline implementation in app.js, which works by inspection. |
| `css/engine.py` brand kit generator | ✅ **Measured** on a scratch copy: it rendered `adaptive_brand.css` for "AMTrix Solutions Inc." 2 placeholders were left unfilled (`typography.font_primary/secondary` vs the YAML's `headings/body`). |
| "OPEN CANVAS ↗" studio link | ❌ `studio.html` doesn't exist in v16.9.95. |
| v15 stress test "results" / "report" (7 docs) | ❌ All 7 files have the **same MD5** as the test *plan*, so no results were recorded. The real outcome is `PENDING_FIXES_AND_UNIT_TESTS.md`, which lists 5 failures found (untracked files invisible, **binary file crashes the reader**, the model refuses context, no proxy singleton lock, flaky TUI PID tracking). In the v15 code, the binary crash and the singleton lock are still unfixed. |
| Router targets groq / mistral / deepseek / lmstudio | ❌ They have adapter branches but no `SERVER_MAP` entries, so they're rejected as "Unknown target". |
| Status: "Production Ready" (README) | Self-label. No automated tests exist for either the dashboard or the router (`package.json` test = the npm default stub). |

### ⚠️ Caveats worth knowing (not resume material)
- **The proxy listens on `0.0.0.0:8080`** (`.agent/services/proxy_server.js`) with `cors()` open and **no auth**. Anyone on the same network can spend the Gemini/OpenRouter/Anthropic keys. The hub's own heredoc copy uses Express's default bind, which is also all interfaces.
- Hub option 6, "Kill Server", runs **`killall node`**, killing every Node process on the machine, not just the proxy.
- The hub **overwrites** `~/.antigravity/proxy_server.js` with its embedded copy each time it starts, so `deploy.sh`'s copy is silently replaced.
- `.agent/.env` (7 key names, values not read) is **git-ignored** (`*.env`), and not tracked. ✅
- The dashboard uses Mermaid `securityLevel: 'loose'` plus `innerHTML` of user content, and auto-renders on load from `#content=` share links. Treat share links from others as untrusted (XSS).

### Resume-ready takeaways
- **Built a prompt-visualization IDE** that compiles structured XML/LLM protocols into interactive Mermaid diagrams:
  - per-branch filters (visibility/shape/colour/connector)
  - config-driven tag-to-shape mapping
  - an "LLM output cleaner" that extracts, repairs and validates messy model output with line-numbered fix reports
  - a **scaffold-and-swap technique** that embeds SVG graphics and Markdown cards inside Mermaid nodes
- **Built an early own-the-proxy LLM gateway + context router (Jan 2026):**
  - one JSON schema across Gemini / OpenRouter / Anthropic / Ollama
  - a CLI context packer with a token budget, git-diff awareness, persistent memory/rules and session history
  - per-call latency, token and tok/s metrics
  - an IDE "router skill" so a cheap model gathers context and a strong model answers
  - This is the first iteration of the gateway that became Claude Code Center.
- **Wrote a failure-driven test plan** (stress suite → 5 identified failures → unit-test acceptance criteria). It's honest evidence of a test-first habit, but there are no recorded passing results.
- **Wording caveats:**
  - Don't call it "production ready" or "MCP" (the proxy is plain HTTP, not the Model Context Protocol, despite the "MCP Proxy" name).
  - Don't claim the heuristic shape inference or the neonify CLI.
  - If shown live, fix `mermaidNodes` first; it's a one-line bug.

---

## 11b. Prompt library + AI_PROTOCOL_TEMPLATE (rest of `complex-amtrix-engineered-prompts-v1`): Nov 10, 2025 → Jan 23, 2026 (one file from Mar 28, 2026)

**Git:** only `AI_PROTOCOL_TEMPLATE` is a repo: 63 commits (2026-01-08 → 01-19), last `c0a93b7`. Origin `ai-protocol-template` returns 404 to an anonymous request, so it's private. 0 ahead / 0 behind, 22 paths uncommitted. Every other folder is plain files with no git.

**Read in full (code):**
- `AI_PROTOCOL_TEMPLATE/.ai/manage.py` (1,340 lines)
- `AI_PROTOCOL_TEMPLATE/BRAIN_SYNC.command` (780 lines). The root `BRAIN_SYNC.command` differs only by adding `AICEO_FACTORY` to `TRACKED_PROJECTS`.
- `START_MCP_PROXY/start_mcp_proxy.sh` (Jan 23; embedded Node server). `.env` key names only, values not read.

**Read in full (prompts/docs):**
- `Distillation_Protocol.xml` v3.5 and its README
- AICEO_FACTORY: README, QUICK_BOOK, CONFIDENCE_CALIBRATION, SHIPPING_PRIORITIES, LLM_COGNITION_GUIDE, WEIGHTED_AUTHORITY_MATRIX, `personas/CEO_CLONE/PERSONA.xml`
- AMTRIX_SYSTEMS: README (17 KB), the start of INTEGRATION_GUIDE, `Proto_Default.xml`
- CURSOR_AI_SYSTEM_ARCHITECT: v5.3 README, plus the boot, "Amit Protocol", RPIV, verification, persona matrix, scope-snapping and token-guard sections of the main prompt
- READMEs of DUAL_PROMPT, UNIVERSAL Nexus Architect and WISDOM_NEXUS
- `PROMPT_IP_PROTECTED_ANALYSIS.md`, `ANTIGRAVITY_VSCODE_RULEBOOK.md`, `UNIVERSAL_ROUTER_GUIDE.md`
- `docs/CONTEXT_COMPRESSION_BENCHMARK.md`, `docs/LLM_ONBOARDING_TEST.md`

**Read by structure only (tag/heading outlines plus targeted sections):**
- `AMTRIX_AI_CEO_PROMPT_WITH_KBASE.md` (100 KB). I read the intro, TECH-STACK/AI-ARMY/CORP-PHIL and the modularity sections 2–6.
- `AMTRIX_AI_CEO_NXS.xml`, `ENTERPRISE_BRAIN_MAP.xml` (vision and group list)
- both `UNIVERSAL_NEXUS_*MOTHERBOARD*` XMLs (outlined and diffed)
- `WISDOM_NEXUS_PROMPT_NXS.xml` (IDs counted, lexicon sampled)
- `Dual_Prompt…md` (outline)

**Not read:**
- `OLD_VERSIONS/` (most are byte-identical copies by size)
- the `Comparative_Analysis.md` files (marketing output of the IP-protected prompt, so not evidence)
- `AI_CEO_PERSONA_ARCHITECTURE.xml`, `CORE_PHILOSOPHY.md`, `SHORTCUT_PROTOCOLS.md`, `Research_Files/`
- `6 LAWS_OF_UNIVERSE…md` (Mar 28; personal)
- `node_modules/`, the zip snapshot

### What it is
**1. AI_PROTOCOL_TEMPLATE v4.0 "Telemetry Edition", the direct ancestor of AMTrix Plan:**
- a portable `.ai/` folder dropped into any project:
  - `_CORE/` (immutable rules, profile, wisdom)
  - `_VAULT/` (living session log, CONTEXT.xml, friction log)
  - `AGENTS.xml` bootloader at the project root
- `manage.py`:
  - commands: `init`, `brief`, `log`, `wrapup`, `sync`, `check`, `test`
  - CONTEXT.xml auto-scan
  - friction log with a "3x → promote" hint
  - keyword-triggered auto-wisdom capture
  - 5-hour stale-session auto-wrap
  - test-framework and tool discovery
- **BRAIN_SYNC.command** (macOS menu): a fleet updater for the `.ai/` folder.
  - **Smart deploy** backs up the data files, copies the framework, restores the data, removes v3.4 legacy templates, drops in AGENTS.xml and re-runs `init`.
  - Other options:
    - external-path deploy
    - "update all" across 11 tracked projects
    - a `~/.ai-master` symlink
    - a Monday 9 AM launchd reminder
  - This is the same "one source, many installs" idea that AMTrix Plan formalised with checksums and audits.

**2. Modular instruction library** (all paste-into-any-LLM artifacts, versioned by hand):

| Artifact | Version | Core design |
|---|---|---|
| **AMTRIX_SYSTEMS "NEXUS DNA"** | v2.2.0 (Dec 2025 → Jan 2026) | 4-layer instruction stack: **Kernel** (safety/format laws) → **DNA** (user profile) → **Proto** (stateless skill) → **Vault** (data). Explicit precedence Kernel > DNA > Proto > Vault, plus a `<SYSTEM_BOOT>` "integration glue" block. Prefix/version file naming convention. |
| **Dual Prompt w/ User Profile OS** | v3.5 | Separates *who* (portable profile = "OS") from *what* (task = "app"). 5 parts; D/R/L modes; an emotional-state HUD with weighted recency scoring. |
| **AI CEO + Knowledge Base** | v1.7.7 MD (100 KB) / NXS v2.0.1 XML | "Motherboard + Cartridge":<br>• an ID-addressable knowledge base (`[TECH-STACK-001]`, `[CORP-PHIL-001-P06]`) with a schema/concordance doc<br>• per-persona **RBAC-style context scoping** (`PERM-DEV-001` sees only listed KB sections)<br>• an SOP to clone a new agent by swapping only the app layer, or a new user by swapping only the profile and KB |
| **CURSOR_AI_SYSTEM_ARCHITECT** | v5.3 | Coding co-pilot prompt:<br>• **RPIV** cycle (Research → Plan → Implement → Validate) with a verification mandate on every code output<br>• PROJECT.md mistake journal (`!learn`)<br>• 4-level **scope-snapping** output formats (micro-patch → full file) with an "anti-lazy" no-`// ...existing code...` rule<br>• token guard thresholds at 60k/70k<br>• manifest-driven multi-part delivery with a recovery block<br>• persona matrix for 8 stacks |
| **UNIVERSAL Nexus Architect / Motherboard-Cartridge Architect** | v1.6 → v2.0 (file dated Jan 20) | Prompt that *builds prompts*: XML structure + ID attributes + Markdown content; `<STARTUP_PROTOCOL>` config; a trigger-based `<PROTOCOL_LIBRARY>` "event loop"; an embedded KB of practices; a `<CASE_BANK>` of past failures used as negative constraints. The newest copy adds 3 rules: Polyglot Mandate, Atomic 6-year-old, **Calculator Ban**. |
| **Distillation Protocol** | v3.0 → v3.5 (Nov 2025) | 3-phase SOP: cheap long-context model consolidates → strong model distils into 9 products (exec brief, reusable components, principles, failure log, LLM-interaction log, tags, "cognitive distillate", KB integration audit with dropped-thread/legacy-alert flags, visual strategy) → final package. |
| **WISDOM_NEXUS_PROMPT** | NXS v9.7.1 | Book-sourced principle lexicon plus parable archive with stable IDs (`WSDM-AGY-001`), and append-only update blocks. Personal-development content. |
| **AICEO_FACTORY** | v4.0.2 (Jan 19–20, 2026) | Design docs for a "CEO clone" persona hierarchy (L0 intern → L4) trained from logged human corrections, plus a **Weighted Authority Matrix** (per-topic human-vs-AI stake, intervention triggers, a respectful-pushback template, a disagreement-log schema). |
| **IP-Protected Competitive Analysis** | v1.0 | Prompt that writes outcome-only marketing copy without revealing implementation ("replication barrier" test). The `Comparative_Analysis.md` files across the library are its output. |
| **ANTIGRAVITY rulebook / UNIVERSAL_ROUTER_GUIDE** | Jan 21, 2026 | Ops notes: index vs context window (`@file` tagging), ignore/rules files, the cost-mode workflow; plus the router/proxy cheat-sheet. |

**3. START_MCP_PROXY "Super Proxy v3"** (Jan 21–23, 2026; a sibling of the hub proxy in 11a):
- an interactive bash menu to set keys and default models per provider
- an embedded Express server with one `POST /ask {target, model, message, context}`, routing to:
  - Gemini (SDK)
  - OpenRouter (chat/completions)
  - Anthropic (Messages API)
  - local Ollama (`/api/generate`)
- normalised `{reply|…, provider, model_used}` responses

### Verified vs claimed

| Claim / assumption | Finding |
|---|---|
| "47:1 compression (143k → 3k tokens), near-zero loss" | **Self-reported.** The benchmark table has "~" token estimates. The "fidelity test" is 8 recall questions the next LLM answers about the prior session (needle-in-haystack style). No tokenizer counts and no independent scoring are recorded. Treat it as a design target or anecdote, not a measurement. CONFIDENCE_CALIBRATION also cites it as evidence ("no one else has this"), so keep that phrasing off the resume. |
| "WISDOM_NEXUS (111+ principles)" | `WISDOM_NEXUS_PROMPT_NXS.xml` has **65 unique lexicon principle IDs + 39 archive/parable IDs = 104** (README: "111 principles, 30+ parables"). The `.ai/_CORE/WISDOM_NEXUS.xml` used by the protocol has **64** named entries. Neither reaches 111. |
| CEO clone "correction logs → alignment" | **Design only.** `PERSONA.xml` shows `current_alignment 0%`, `corrections_logged 0`. `scripts/` is empty. There's no `DISAGREEMENT_LOG.md` in `_VAULT`. |
| NEXUS layers "assemble" into deploy builds | Manual copy-paste. `assemble.sh` is listed under "Planned Q1 2026" and doesn't exist. The layer files `Proto_Default`/`Vault`/`DNA_Default` are ~1–1.5 KB stubs. The real built artifact is `99_DEPLOY_BUILDS/AI_CEO_OS_CARTRIDGE.xml` (24 KB). |
| BRAIN_SYNC help: smart deploy "PRESERVES … USER_PROFILE.md" | **Not true in code.** `USER_PROFILE.md` is not in `DATA_FILES`, so `cp -r source/* target/` overwrites it. "Update All" also overwrites `_CORE/WISDOM_NEXUS.xml`, which smart deploy *does* preserve. The behaviour is inconsistent between the two paths. |
| BRAIN_SYNC smart-deploy safety | Backups go to fixed paths `/tmp/_VAULT/SESSION_LOG.md.backup` etc. (not `mktemp`), and there's no check that the copy succeeded before restore. A failed or concurrent run can lose or mix data. New installs copy root `AGENTS.xml`, while updates copy `templates/AGENTS.template.xml`, despite the "SSOT" comment. |
| `sync` builds `_MASTER_NEXUS_INDEX.xml` | It prints and writes `.sync_state.json` only (as found earlier). The root `_MASTER_NEXUS_INDEX.xml` is dated **Jan 10**, while syncs ran through Jan 19–20. |
| `wrapup` | Crashes with `EOFError` at the wisdom y/n prompt when there's no stdin (scratch run). It works with `n` piped in. |
| "MCP proxy" | **Not MCP.** It's a plain HTTP `/ask` gateway. Only the Gemini path forwards `history`; OpenRouter and Anthropic are single-turn (system + one user message). No streaming and no tool calls. Defaults disagree: the config prompt uses `anthropic/claude-3.7-sonnet`, the launcher uses `anthropic/claude-4.5-opus`, and the router guide's alias uses `anthropic/claude-opus-4.5`. Verify the slugs before demoing. `package.json` omits `@google/generative-ai`/`axios`/`cors`; `check_deps` installs them `--no-save`, but they're present in `node_modules`. |
| Readme drift | The Distillation README points to `Distillation Protocol v3.5.xml`; the live file is `Distillation_Protocol.xml`. The Universal Nexus README describes v1.8.3; the live file is the v2.0 Motherboard-Cartridge. The Dual Prompt main file contains two concatenated versions (PART 1 appears at lines 1 and 318). |

### Security / privacy heads-ups
- **Super Proxy:**
  - `app.listen(8080)` has no host, so it binds all interfaces, with `cors()` open, **no auth** and a 50 MB body limit.
  - Anyone on the LAN can spend the Gemini, OpenRouter and Anthropic keys.
  - The script writes keys to a plaintext `.env` in the folder. The folder isn't git, so it isn't pushed.
  - Same finding as the 11a hub proxy.
- **Personal content:**
  - The AI CEO KB, Dual Prompt, Cursor "Amit Protocol" BIOS, AICEO_FACTORY docs and AMTRIX_SYSTEMS DNA contain personal health, family, financial and emotional details.
  - **Don't publish these folders or quote them in portfolio material.** Share only the architecture (layering, precedence, ID scheme, RBAC scoping, SOPs).
- The `nuke` alias in the rulebook does `rm -rf .antigravity .cursor .brain .cursor_brain` in the current directory. It's harmless in a project folder but worth a note if shared.

### Resume-ready takeaways ("modular instruction design", not "prompt engineering")
- **Designed a layered, portable LLM instruction architecture (2025–26):**
  - Kernel/safety → user profile → stateless skill → data vault, with explicit precedence rules and a boot/integration block
  - an ID-addressable knowledge base with RBAC-style per-agent context scoping
  - an SOP to spin up a new agent or user by swapping one layer
  - These are the Lego-piece principles later carried into AMTrix-core's skill compiler and AMTrix Plan.
- **Wrote a coding-agent operating protocol** (RPIV + verification on every change, scope-sized patch formats, no-elision rule, token-budget guard, mistake journal). It predates and parallels what Claude Code-style workflows later standardised.
- **Built a conversation-distillation pipeline** (3 phases, 9 outputs including failure logs, dropped-thread audit and KB reconciliation). It's the seed of the later context-compression and brief tooling.
- **Codified deterministic-offload rules for LLM systems** ("Calculator Ban": numbers come from code, the model echoes them; "Polyglot" format law: XML for reference, JSON for branching, numbered steps for commands). These tie directly to AI Pandit's math-and-determinism emphasis.
- **Shipped a portable project-memory protocol + fleet updater** (AI_PROTOCOL_TEMPLATE v4.0, 63 commits; BRAIN_SYNC smart deploy across 11 projects). This is the precursor to AMTrix Plan.
- **Human-in-the-loop governance design** (the Weighted Authority Matrix: per-topic decision stakes, intervention triggers, a disagreement log as training data). Present it as a framework, not a trained system.
- **Wording caveats:**
  - Drop "47:1" or label it "self-measured, ~47:1 on one session".
  - Use "~100 curated principles", not 111.
  - Don't claim CEO-clone alignment results, an automated assembler, or "MCP".
  - Don't put "$2.1B empire" or "AI army" language in client-facing material.

---

## 12. apple-watch-dashboard ("Apple Product Picker"): all files dated Aug 26, 2026; not a git repo

**Read in full:** every file (`server.js`, `public/app.js`, `index.html`, `style.css` by size, `catalog.json`, `data.json`, `README-FIRST.txt`, `package.json`). It's 8 files, about 15 KB, with minified one-line JS.

### What it is
- **Not an Apple Watch app.** "Watch" means a saved *watch-list entry*. It's a localhost (127.0.0.1:9595) picker for iPhone configurations:
  - catalog dropdowns from an editable `catalog.json` (iPhone 16 → 17 Pro Max, plus iPhone 18 placeholders)
  - saved watches
  - a "copy configuration" helper and a deep link to Apple's buy page
- **Webhook-driven, not a poller.** Each watch gets a random `base64url` token, and `POST /api/webhooks/<token>` with `{status, message, stores}` records an event.
  - Status is clamped to available/unavailable/changed/unknown.
  - Text is capped at 600 characters.
  - Up to 300 events are kept.
  - On a *change* it fires an optional ntfy POST (5 s timeout) plus browser Notifications.
- The README says outright that it doesn't poll Apple and can't pre-click checkout options. That's an honest scoping note. It's the "front end" companion to iphone-inventory-checker-v3 and notify-bus.

### Verified (smoke test on a scratch copy with empty data)
- The catalog served 10 models.
- Create a watch → webhook with a valid token returns `ok` plus the event; an unknown token gives `Unknown webhook`; bad JSON gives `Invalid JSON`.
- `/../server.js` returns `Not found` (the path-normalise guard works).
- It binds **127.0.0.1 only**, and the UI HTML-escapes all user fields. ✅
- **Gaps:**
  - no tests
  - no request-body size limit
  - `README-FIRST` says to start from `~/Documents/GitHub/apple-picker-restored` (wrong folder name)
  - `data.json` holds one live webhook token (local-only, low risk)

### Resume-ready takeaways
- Small, zero-dependency Node service showing a **tokenised per-entity webhook ingestion → state-change detection → push-notification fan-out** pattern (ntfy + browser), with input clamping and localhost-only binding.
- Worth one line under the iPhone inventory/notify-bus story. It isn't a headline project.

---

## 13. amtrix-ai-pandit (AI Pandit, v2.9.3)

**Repo:** private (`amit-malhotra1/amtrix-ai-pandit`), 46 commits (2025-12-17 → 2026-08-20), last `72e0109`, in sync with origin; 152 uncommitted paths.

### Read in full / Not read
- **Read:** `astro_engine/src/engine.py` (1,814 lines: chart, dasha, transit, yoga, finance/career/relationship/health/happiness analysers), `shadbala.py`, `event_validator.py` (rule table + validator), `scoring_policies.json`, `config/event_validation_policy.yaml`, `run.sh`, `web_ui/ui_server.py`, the key parts of `generate_guru_xml.py` (header, provenance, XSD validation), all 9 test files, and the v2.9.3 FEATURES / IMPLEMENTED_PHASE_1/2 / diagnostics docs.
- **Not read:** `blueprint.md` (24 KB), the GPT-5.6 feedback docs, `LLM_GURU_PROMPT.md` / `system_prompt.md`, the `old versions/` folders, and the `renderer.py` SVG internals. I didn't open `data_input/User_Profiles.json` or `outputs/` because they hold personal birth data.

### What it is
A deterministic Vedic-astrology computation engine. It turns birth data into structured, evidence-traced XML that an LLM then narrates. Pipeline: web form or CLI → `run.sh` (active-run contract: checks inputs and prompt, records the prompt's SHA-256) → `main.py` (charts) → `merge_chart.py` → `generate_guru_xml.py` (XSD-validated output) → LLM prompt.

### Verified vs claimed
- **Verified (ran it):** the test suite passes, **30/30 in 0.37 s** (on a scratch copy with the existing venv).
- **Verified (code):**
  - Swiss Ephemeris sidereal maths: Lahiri/KP/Raman ayanamsa map, True Node, whole-sign houses.
  - Divisional charts D1/2/3/4/7/9/10/11/60.
  - Vimshottari MD/AD/PD periods.
  - Double-transit detection that emits structured activations (`rule_id` such as `DT_ASC_H11`, status, contributions).
  - Declarative, versioned `scoring_policies.json` (support/stress points, thresholds).
  - Evidence records (`rule_id`, points, text, threshold_id/min/max, ruleset version).
  - Event validator with rule IDs, versions, meaning templates and MATCHED/PARTIAL policy status.
  - XSD schema check through `xmlschema`.
- **Bugs confirmed by running:**
  1. **Natal speed is always 0.0.** `calculate_charts` calls `swe.calc_ut(..., FLG_SWIEPH)` without `FLG_SPEED`. A 1990 test chart returned 0.0 for all 8 bodies. As a result, retrograde modifiers in `calculate_net_impact` never fire, and Shadbala Chesta treats every planet as near-stationary. Transits do pass `FLG_SPEED`, so they're correct.
  2. **Dhana-yoga double counting.** The L1×L2 loop runs both ways, so 3 conjunct wealth lords give 6 yogas instead of 3 ("A and B" plus "B and A"). That inflates `natal_score = count × 20`.
  3. **The "exchange signs" (parivartana) branch can never run.** Its condition reduces to `h1 == h2`, which the branch above it already catches.
- **Confirmed by reading the code:**
  - **Not deterministic over time.** `calculate_vimsottari`, `calculate_transits` and the XML `generated`/`as_of` stamps all use `datetime.now()`, and there's no clock injection. Running the same input on a different day gives different output.
  - The planned STATIONARY motion state isn't implemented.
  - The "Mahapurusha" and "Gandanta" modifiers are dead code: the yogas are named "☆ Ruchaka" etc., and nothing produces Gandanta. Vipreet yogas are computed and then thrown away (`pass`).
  - Several yogas are conjunction-only simplifications, as the code comments admit.
  - Shadbala is a heuristic, not classical virupa Shadbala: day/night is decided by clock hour 6–18, and there's an enemy→10 fallback.
  - Natal ratings are still hardcoded (finance count×20; career H10 Shadbala ≥130/≥100). So "fully decoupled policy" is only partly true. If the policy file fails to load, the code silently falls back to empty rules.
  - In the event validator, `loss_parent` and `loss_mother` have identical conditions, and the `relationship_saturn_moon` rule ID is used twice.
  - `xmlschema` isn't in `requirements.txt`. The generator only warns and skips XSD validation when it's missing (it is present in the current venv).
- **Fine:** the nakshatra/pada boundary constants (13.3333333333) gave correct results at the edges I tested.
- **Docs are stale:** the README is v2.2.1 (Dec 2025, "PRODUCTION READY", old `AI_Pandit_Deploy_v2.1` path), while the code is v2.9.3. `IMPLEMENTED_PHASE_1.md` actually contains the Phase 2 plan.
- **Security/privacy:**
  - `ui_server.py` binds **all interfaces on port 8000** (`TCPServer(("", 8000))`) with no auth.
  - `GET /get_users` returns every stored birth profile.
  - `POST /generate` runs `run.sh`. It uses list-form `subprocess`, so there's no shell injection.
  - `User_Profiles.json` and 141 `outputs/` files are tracked in the (private) git repo.

### Resume-ready takeaways
- "Built a **deterministic, evidence-traced rules engine** on Swiss Ephemeris. Versioned declarative scoring policies, rule-ID provenance on every score, XSD-validated XML handed to the LLM. The LLM only narrates computed numbers; it never does the maths (the 'Calculator Ban' pattern)."
- "Run contract: input checks + prompt SHA-256 recorded per run; 30 pytest invariants/regressions (schema validity, evidence consistency, timeline/transit agreement)."
- Frame it as **math, determinism and auditability**, not astrology (per user rule).
- **Avoid:** "fully deterministic" (it depends on the run date), "full Shadbala", "production ready", and "fully decoupled hardcoded logic".
- **Safe wording:** "reproducible for a given as-of date" (only after the clock is injected), or "deterministic computation layer".

---

## 14. amtrix-voicebus (AMTrix VoiceBus v0.0.1)

**Repo:** **not a git repo** (local only). Files dated Aug 11–17, 2026. About 1.2k lines of TypeScript in `src/`, plus a vanilla web UI, a JSON Schema, Nunjucks templates and 3 vitest files.

### Read in full / Not read
- **Read:** every file in `src/` (cli, server, store, schema, policy, routing, render, config, types, both macOS adapters), `schemas/voice-event.v1.json`, both templates, `shell/talk.zsh`, `scripts/install-local.sh`, the event-rendering and API-call parts of `public/app.js`, README, `package.json`, `config/voicebus.json`, `skills/amtrx-voicebus/SKILL.md`, `docs/VOICEBUS_INTEGRATION_APPROACHES.md`, and the master plan `AMTRX_VoiceBus_Implementation_Plan_UPDATED.md` (latest, Aug 17).
- **Skimmed:** `scripts/comment-sync.ts` (grep only).
- **Not read:** the older plan versions v0.0.1–v0.0.5 (they're superseded), the comment-engine plans and SKILL.md, MACOS_SIRI_QUIRKS / VOICE_CUSTOMIZATION, the demo scripts, and `.comments/` (a 200 KB manifest).

### What it is
A local event bus for AI agents. Agents publish a **canonical `voice-event.v1` JSON event**, and VoiceBus then:
- validates it with AJV;
- writes **write-once** artifacts to `~/.amtrx/voicebus/`: event JSON, a Markdown brief and speech text, plus `latest.*` copies and a JSONL log;
- routes it through a deny-by-default channel policy (local `say`/`osascript` allowed, email/WhatsApp/web disabled; a per-event override can't enable external channels in Phase 0);
- speaks it with per-actor voice profiles (with a workaround for the macOS Siri `-v` quirk);
- pushes it live to a dashboard over SSE (chokidar file watch → Express `/api/stream`).

It also has human-in-the-loop "CEO decision" event kinds. The code notes that the templates were carried over from a Python version, so this is a Python→TypeScript port.

### Verified vs claimed
- **Verified (ran it in a scratch copy, HOME redirected):** **34/35 tests pass.**
  - The one failure is fixture drift: `render.test.ts` expects `VB-20260805-0001`, but `tests/fixtures/demo.json` now has `…0002`.
- **Verified (code):**
  - Strict schema (`additionalProperties:false`, event-ID pattern `VB-YYYYMMDD-NNNN`, kind enum).
  - Immutable store (`EventExistsError`) and a `migrate` upcaster.
  - Deterministic adapter ordering (notify before TTS).
  - Adapters use `execFileSync` with no shell (osascript string escaped).
  - `doctor` health checks.
  - Graceful no-op on non-macOS platforms.
- **SECURITY: confirmed by running it.**
  - `POST /api/open-local` does `execSync(\`open "${path}"\`)`, so a path containing `"; cmd; "` runs a shell command. I verified this harmlessly: it created a marker file in scratch, which I then deleted.
  - The server uses `cors()` (`Access-Control-Allow-Origin: *`) and `app.listen(port)` binds **all interfaces** (`*:4791` seen in lsof). So any website, or anyone on the LAN, can run commands on the Mac while `voicebus serve` is running.
  - The dashboard also puts event fields into the page with `innerHTML` and renders briefs with `marked.parse` unsanitised, which is a stored-XSS path into that same endpoint.
  - The master plan says VoiceBus "never executes arbitrary shell commands", and Bearer auth is listed as *pending*. The plan is honest about the missing auth, but the injection contradicts its claim.
- **Doc-vs-code contradictions (verified):**
  - `--requires-review` is documented in SKILL.md, the integration guide and the plan, but the CLI fails with `error: unknown option '--requires-review'`.
  - **`POST /api/events` (REST "Approach 4") doesn't exist** in `server.ts`. The only POST routes are play/stop/open-local. The example payload also uses `kind: "test_complete"`, which isn't in the schema enum.
  - `talk --file <md>` is documented as reading a Markdown document aloud. It actually calls `voicebus play <path>`, which fails with `Event not found: README.md`.
  - SKILL.md Test 5.3 is titled "Publish Live Event via cURL" but calls `/api/open-local`.
  - The comment-sync bridge is documented as "triggers VoiceBus to notify". `comment-sync.ts` only rewrites `.comments` JSON and the manifest; it never calls VoiceBus.
  - `--no-speak` is read as `opts.noSpeak`, but commander sets `opts.speak=false`, so the flag has no effect. Verified with commander. It's harmless while `autoplay` is "notify".
  - The README says "zero-dependency" and "npm link links the CLI globally". It actually has 9 runtime dependencies, and `package.json` has no `bin` field, so `voicebus` only exists after `bun build --compile`. `talk.zsh` and install-local assume it's on PATH.
- **Smaller issues:**
  - `pkill -f "say"` kills any process whose command line contains "say".
  - The server hardcodes `~/.amtrx/voicebus` and ignores `config.store_dir`.
  - `migrate` spreads `...raw` after its defaults, so an old `schema_version` value overrides "voice-event.v1".
  - In `loadConfig`, `JSON.parse` sits outside the try, so bad JSON crashes it.
  - `/api/briefs/:id.md` and `/api/play/:id` don't validate the ID.

### Resume-ready takeaways
- "Designed **AMTrix VoiceBus**, a local agent-to-human communications and audit bus: canonical versioned event contract (JSON Schema/AJV), write-once artifact store (JSON + Markdown brief + speech text + JSONL log), deny-by-default channel policy, per-actor voice profiles, and a live SSE dashboard. Gives AI coding agents (Claude Code, Antigravity) a standard way to announce milestones and request human 'CEO' decisions."
- FDE angle: **human-in-the-loop gating plus an audit trail for agent output**, with provider-neutral adapters. It's a strong talking point for "how do you keep humans in control of agents".
- **Avoid until fixed:** "REST gateway", "secure", "zero-dependency", and the 4-approaches matrix (approaches 2 and 4 aren't implemented). Before demoing the server, the open-local injection needs fixing (`execFile('open', [path])`, bind 127.0.0.1, restrict CORS).

---

## 15. amtrix_vscode_core (editor workspace design system)

**Repo:** **not a git repo**. 16 files, dated Aug 6–7, 2026. **There's no executable code.** It's an editor configuration kit: `settings.json` (245 lines), `keybindings.json`, a Markdown Preview Enhanced `style.less` (435 lines) and `config.js`, a 669-line blueprint doc, and sample Markdown pages.

### Read in full / Not read
- **Read:** `docs/INITIAL_PLAN_AND_PROGRESS.md` (all of the prose plus the HTML component templates; I skimmed past the CSS rule bodies), the key `settings.json` entries (secrets grep redacted, key names only), the MPE `config.js`, and `MARKDOWN_FILES/devlopment_log.md`.
- **Not read:** the `temp*.md` scratch notes, `CData_Script_in_.md`, `HUMAN_AUTO.md`, and `Main_Syles_for.md`.

### What it is
A portable "**script-free design system**" for VS Code/Antigravity:
- One global stylesheet plus HTML class/`data-*` attribute conventions, so an LLM can write Markdown that renders as dashboards, **multi-agent conversation cards** (human / LLM-primary / LLM-critic roles, labelled through CSS `attr()`), collapsible agent logs, alert panels, status badges and a sticky HUD bar. All of it works without JavaScript.
- An accessibility/TTS pipeline: `editor.accessibilitySupport: on` so macOS speech can track the cursor, a VoiceFlow Reader + Siri voice alias, and two-way preview scroll sync.
- The Commentary extension pointed at **`http://localhost:8080/api/v1/messages`** (his own local proxy) with model `anthropic/claude-haiku-4.5`. That's concrete evidence for the "owned proxy, no subscriptions" story.

### Verified vs claimed
- **Contradiction:** the doc's headline is "Script-Free… (enableScriptExecution: false)", but both the doc's own settings block and `PREFRENCES/settings.json` line 234 set `"markdown-preview-enhanced.enableScriptExecution": true`.
- The doc has repeated "Use code with caution." lines. That's pasted LLM chat output, so the doc needs a cleanup pass before anyone else sees it.
- The sample "Security Validation: Verified Secure" and "Engine Operational Baseline" text is placeholder copy, not a test result.
- `devlopment_log.md` uses the team-thread components to draft the VoiceBus flow (human command → canonical event → immutable record → human review). That links this kit to VoiceBus (§14).
- `CodeGPT.apiKey: "Ollama"` is a placeholder, not a secret.

### Resume-ready takeaways
- At most one line, as a supporting skill: "Built a **script-free Markdown design system** (CSS tokens + HTML/`data-*` component contracts) that LLM agents write to, so agent output renders as dashboards and human/LLM-primary/LLM-critic review threads with no JavaScript."
- It supports two stories: the "LLM output contracts" story (same idea as the AMTrix Plan and Mermaid dashboard) and the local-proxy story (Commentary → localhost:8080).
- Don't list it as a project.

---

## 16. AGENT_PROTOCOL (folder) → `AI_agent_protocol` repo ("AMTRIX GOD MODE" v19.0 → v20.0)

**Repo:** only `AI_agent_protocol/` is a git repo: `amit-malhotra1/ai_agent_protocol`, private (anonymous API returns 404). 12 commits, 2026-02-13 → **2026-03-23** (last `2d6ca42`, "v20.0 Protocol-Driven Platform Edition"). 1 uncommitted path.

The rest of the folder (2,279 files in all) is mostly **copies and predecessors**:
- `AI_PROTOCOL_TEMPLATE/` and `START_MCP_PROXY/` are near-identical to the `complex-amtrix-engineered-prompts-v1` copies reviewed in §11b (11 and 1 differing files).
- `BRAIN_SYNC_v4.0.0.command` is byte-identical.
- `ai-context-compressor-v1/` is a copy of the standalone repo (11 diffs); it gets its own section later.
- Root `.agent/` (v15.5) and `AGENT_ANT_VSCODE/` are older versions.
- `_AICEO_VISUAL_ENGINE/` holds doc-formatting standards (overlaps §11a).
- `_NEXUS/` and `NEXUS_STATE_SNAPSHOT_v4.0.0/` are `.ai` registries and snapshots.
- Not re-read: `_ARCHIVE/`.

### Read in full / Not read
- **Read (code):**
  - `.agent/runtime/core/universal_context.py` (1,126 lines), `api_client.py`, `antigravity_interceptor.py`
  - `runtime/tools/ide_interceptor.py` (403), `start_mitm.sh`
  - the listen/CORS/handler sections of all 3 Node proxies
  - all of `deploy/` (orchestrator + 4 libs + 4 targets) and one `skill.deploy.json`
  - the key-entry and target-menu parts of `hub/AMTRIX_GOD_MODE.command`
  - the compressor function outline
  - the `proj-snapshot` SKILL.md header
- **Read (docs):**
  - `README.md`
  - `HARDENING_AUDIT_LOG.md` (all 5 runs)
  - `IMPLEMENTATION_PLAN_v20.md` (context, gap table, phase/task outline)
  - `BRAINSTORM_v2.md` (decisions, constraints, architecture, "edge" rationale, open questions)
- **Not read:**
  - `hub/antigravity_hub.sh` (469 lines)
  - the `SYSTEM_ARCHITECTURE*` and `CHANGELOG_v19.5` bodies
  - the research/knowledge docs (Research_Claude_Code 2,158 lines, Intercept_antigravity 1,821, Real_MITM 812, REFERENCE_MCP_THINKING 883). I only scanned them for key patterns, and the matches were placeholders (`sk-ant-YOUR…`).
  - the older test suites
  - `.ai/` (that's the §11b system, v6.0 here)
- I didn't open `.env*` or the `.debug`/`mitm_output` capture bodies.

### What it is
The **Agent Protocol journey**, the step before owning the proxy (§1 claude-code-center):
1. **`universal_context.py`, a CLI "context packer + router".**
   - It builds an XML `<VIRTUAL_CONTEXT>`: file tree (depth ≤3, suppressed when run from home), `git diff HEAD` (10k-char cap), `~/.antigravity` memory/rules, and up to N files under a token budget with truncation markers.
   - It routes to **13+ targets** through provider adapters: Gemini direct, OpenAI-compatible (OpenRouter/OpenAI/Groq/Mistral/DeepSeek/LM Studio), Anthropic (with a **prompt-caching client**: `cache_control: ephemeral` and a printed cache-savings %), **AWS Bedrock** (boto3), Ollama, a local `/ask` proxy, and echo.
   - Config-driven model aliases sit in `models.json` (global, with a project overlay). There's session memory, an **auto-router heuristic** (prompt >500 chars or keywords → "strong" OpenRouter Opus, otherwise Gemini; "System One / System Two"), a keyword safety stop, and full **transparency dumps** (payload JSON + reproducible cURL + readable context).
2. **`ide_interceptor.py`, a mitmproxy addon.**
   - It captures the IDE's own LLM traffic (Antigravity/Gemini, Claude Code/Anthropic, OpenAI, OpenRouter) with source detection and token estimates.
   - It writes readable Markdown reports (system prompt, tool list, conversation) and timestamped vault archives.
   - Modes are passthrough or capture.
   - Purpose (BRAINSTORM_v2): study how premium harnesses build context, then route 80% of traffic to cheap models. It records the actual budget: $100 OpenRouter credit, Claude Code $20/mo planned, and an estimated "$35/mo vs $200/mo".
3. **v20 Deploy Engine.**
   - **Per-skill manifests** (`skill.deploy.json`: targets, scope, update strategy, conflict policy) fan out one skill source to **Antigravity, Claude Code and Cursor (stub)**, plus a runtime target (`~/.antigravity`).
   - It keeps a **SHA-256 lock manifest** and classifies each file NEW/SAME/UPDATED/**CONFLICT**, with policies (preserve-local / overwrite / interactive prompt), `--dry-run`, status and tee'd logs.
   - The hub is a TUI menu (provider picker, key/model setup with masked display, MITM launcher, capture viewer).
4. **Skills:** router, extractor (use captured context), compressor (dictionary encoder + decompressor), and `proj-snapshot` (git-commit snapshots + SNAPSHOTS.md + panic-branch restore).

### Verified vs claimed
- **Ran (scratch copy, HOME redirected, no keys, captures/.env excluded):** `v20_platform_suite.py` gives **62/63 PASS**. The one failure is P7.3 (the Gemini cURL masking regression), which needs a `.debug` dump I excluded.
  - The repo's own log shows the progression 55/63 → 62/63 → 62/63. P4.2 ("deploy writes a log") was the remaining failure in the real tree.
  - The suite makes a few **unauthenticated** provider calls (they return 401), so nothing was billed.
- **Audit log oddity:** v19.4 check C2.1 says "Expected Model ID: anthropic/claude-opus-4.5 | Observed: None | ✅ PASS". A pass recorded on a None observation means that assertion is weak.
- **Bugs confirmed by running:**
  - **JSON mode with the default target crashes.** `{"prompt":"Hello",…}` without `target` → `❌ EXECUTION FAILED: 'NoneType' object has no attribute 'status_code'`. The auto-router only runs in CLI mode, and `SERVER_MAP["auto"]` has no adapter branch.
- **Bugs and gaps (code + filesystem):**
  - **API keys get written in plaintext to debug files.**
    - `dump_curl_debug()` in `universal_context.py` masks the Gemini URL key but writes the OpenAI-compatible `Authorization: Bearer <key>` header unmasked.
    - `AntigravityInterceptor._save_curl_command` only masks keys present in `os.environ`. Keys loaded from `~/.antigravity/.env` aren't masked.
    - `ide_interceptor.save_capture` / `_save_to_vault` store **raw request headers** (auth headers included).
    - Result: **13 local files contain raw-looking keys** (`.agent/.debug/_LAST_CURL_OPENROUTER.sh`, `tests/mitm_output*/…`). All 13 are **gitignored, and git history has none** (checked with `git log -G`). The tracked `runtime/.debug` dumps have empty key values.
    - There's a privacy side too: tracked `runtime/vault/captures/antigravity/*context*.md` (19) holds captured prompt context.
  - `CachedAPIClient` reads `ANTHROPIC_API_KEY` only from `os.environ` (it ignores the `.env` loader). It's **forced on whenever the model is `claude-opus-4.5`** and always uses alias "amtrix", so the user's model choice is ignored on that path.
  - **Unimplemented features documented as present:**
    - The interceptor's `redirect_ollama` / `redirect_openrouter` modes are `pass` stubs. The docstring says "Redirect to local Ollama / OpenRouter".
    - `--compress` only prints a hook message.
    - The Cursor deploy target is a stub (honestly labelled).
    - Plan Phase 4 (project recipes) isn't built (`project_recipes/` is absent).
  - **`deploy.sh rollback` can never succeed:** it restores from `~/.antigravity/.deploy_backup`, but nothing creates that directory (it's referenced only once).
  - Runtime core files deploy with the `overwrite` policy, so local edits to the deployed core are silently replaced.
  - `mcp_proxy/proxy_server.js` binds **0.0.0.0:8080** with `cors()` and no auth. It's the same exposure already flagged for the hub/Super Proxy. In this version all handlers do forward history.
  - Safety is a keyword denylist ("RM -RF", "DELETE ALL"). The auto-context fallback sends the 5 most recently modified non-dot files in cwd to the LLM, so a non-dot secrets file (`profiles.env`, `*Credential.json`) could be sent.
  - The hub reads API keys with a plain `read -r`, so they're visible while typed.
- **Doc drift:**
  - README says `.agent` v19.4 and points to `.agent/core/`, `.agent/tools/`, `.agent/interfaces/`, `.agent/models.json`. v20 moved all of these under `runtime/` and `hub/`, and the old paths no longer exist.
  - README says the v19.4 suite has "0 dependencies", but it needs `requests` and network access.
  - Its roadmap Phases 0–5 (Claude Code recon, replay.py, CLI router, dashboard, productization) are all unchecked.
  - BRAINSTORM_v2's "Legal" open question (whether selling a tool that captures Claude Code's system prompts is allowed under the TOS) is unresolved.

### Resume-ready takeaways
- **Journey line (the user wants this emphasized):** "Iterated from a CLI context-packer/router (v14–v19: 13+ provider adapters, Anthropic prompt caching, Bedrock, Ollama, config-driven model aliases, heuristic cost routing) through a mitmproxy **LLM-traffic observability layer** (captured and studied how IDE agent harnesses assemble system prompts, tools and context) to **owning the gateway**: a self-hosted proxy on OpenRouter/Vertex with no vendor subscriptions (→ Claude Code Center §1)."
- "Built a **manifest-driven skill deploy engine**: one skill source fans out to Antigravity, Claude Code and Cursor targets, with SHA-256 lockfile drift detection, NEW/UPDATED/CONFLICT classification, per-skill conflict policies, dry-run, and a 63-check platform verification suite."
- FDE angle: **multi-provider integration, cost-aware routing, observability/transparency, and safe config deployment across developer tools.**
- **Wording cautions:**
  - Say "LLM traffic observability / transparency proxy for my own sessions", not "capturing Claude Code's system prompts", because of the TOS question.
  - Avoid "hardened" and "100% green audit" (the audit has a None-observation PASS and one real FAIL).
  - Avoid "rollback" and "redirect modes", which don't work yet.
  - Before showing anyone this repo, fix the Bearer-header masking and the raw-header vault capture.

---

## 17. multi-agent-assistant-v1 ("AI Companion" TUI, v2.7.3)

**Repo:** `amit-malhotra1/multi-agent-assistant-v1`, private (404). There's **1 commit** (2025-11-16, "Initial commit"). After that, 18 tracked files were modified locally and never committed (+1,002/−610 lines), and 3 `* copy.py` files were deleted. The working tree is the v2.7.3 code (Nov 17, 2025).
- `src/*.py` equals the `*_v2.7.3.py` snapshots.
- Around 30 versioned snapshot files (`*_v2.5` … `*_v2.7.3`) are gitignored by the `*_v*.*` pattern.
- The chronicle covers 2025-11-14 → 2025-12-15.

### Read in full / Not read
- **Read in full:**
  - `src/model_router.py` (209), `app_actions.py` (192), `gatekeeper.py` (107), `tui_screens.py` (118)
  - `config.yaml` (125), `consumer.yaml`, `install.sh`, `ai-session.sh`, `requirements.txt`, `.ai_ignore`, `.gitignore`
  - all 10 `briefing_documents/*.md`
  - `todo_project/AI_CEO.md` and the head of `todo.py` (the sample target app)
  - `.antigravity/knowledge/*.md`
- **Summarised, not read line by line:** `.ai_chronicle.md` (965 lines, 120 timestamped goals, mostly test inputs).
- **Not read:**
  - the ~30 older snapshot versions (v2.3–v2.7.1; superseded)
  - `AI_PROTOCOL_TEMPLATE/` (an older 203-line `manage.py` predecessor of the §11b system)
  - `.env` (key names only: AI_PROVIDER, ANTHROPIC/OLLAMA/OPENAI/OPENROUTER_API_KEY; not tracked in git, no history)

### What it is
A **Textual TUI coding companion**. It's the earliest ancestor of the router/context-packer line (→ §16 AGENT_PROTOCOL → §1 Claude Code Center).
- **Context engine:**
  - It builds a briefing prompt: system prompt `AI_CEO.md`, plus a "project brain" index (specs = What, manifest = Why, standards = Rules, philosophy = How), plus **hierarchical `AI_CEO.md` files collected from every folder**, the goal, and either the user-selected files (an editable file-list modal filtered by `.ai_ignore` + universal ignores) or the `git diff` ("Refine").
  - `target_project_root` makes it portable to any project.
- **Three routing modes (`mcp_mode`):**
  - `direct`: one call.
  - `triage`: a cheap/local model (default Ollama `qwen3:30b`) picks the provider from the goal alone. It checks the chosen provider has a key, and falls back to the default if not.
  - `planner`: the planner LLM returns a JSON plan (agent, mission brief, minimal context files/rules, depends_on). Each step runs on the execution provider with **stateful in-memory file versions carried between steps**, and everything is merged into one final patch with aggregate latency/tokens.
- **Providers:** OpenRouter, OpenAI, Anthropic, Gemini, Ollama, plus a **Clipboard mode** (no API, copy/paste with any chat UI). There's also an `ai_enabled` master kill switch.
- **Multi-key rotation:** a list of env-var names per provider, rotating every N requests.
- **Safety and audit:**
  - patches use a strict `FILE: path <<'EOF' … EOF` protocol
  - they're applied from the clipboard only after a y/N confirm
  - an automatic `.ai_backups/` copy is taken first
  - every overwrite is appended to `audit_log.md`, and every goal to `.ai_chronicle.md`
- **Git:** a git pre-flight degrades refine/push when git is missing. Push runs `git add . && commit && push`.
- **Metrics:** a header per response (provider/key/model) and stats (latency, total incl. triage, tokens in/out, tok/s).
- The docs set out the "Human-AI Centric System" philosophy: Principle of Proportionality, ask for clarification on vague goals, auditable everything, and a **"Lego piece" modular architecture**. That phrase appears in specs.md as early as Nov 2025.

### Verified vs claimed
- **Ran (scratch copy, `.env` excluded, own venv, no network to providers):**
  - The TUI mounts headless (Textual `run_test`).
  - **Planner orchestration works with mocked LLMs:** planner call → 2 execution calls. Step 2 saw step 1's in-memory file state, the final merged patch held the step-2 version, and total_latency was aggregated.
  - Real usage in the chronicle: gemini-2.5-flash 37, deepseek-chat-v3.1 27, gemini-2.5-pro 10, qwen3:30b 4, Clipboard 80.
- **Bugs confirmed by running:**
  1. **The Gemini API key leaks into error text.** The key sits in the URL query (`?key=`), and the HTTPError branch of `_send_request` re-raises `requests`' message ("…for url: …?key=<KEY>") **without redaction**. Only the generic-exception branch redacts. The probe used a fake key against a local 400 server, and the key appeared in the returned text that the TUI logs. That contradicts specs v1.6.2, "redacts secret keys from any error messages".
  2. **Patch path traversal.** `FILE: ../x.txt` was written **outside `target_project_root`**, because the target is `root / header` with no containment check. A human y/N gate exists, but a malicious or hallucinated path is still honoured.
  3. **`triage_model` is never read from config.** It's nested under `models:` in YAML, but the code reads it at top level, so the hardcoded default `ollama/qwen3:30b` always wins. The YAML value `ollama/qwen:30b` also has a typo.
  4. **The planner prompt file isn't in git, and its path has the wrong case.** The code opens `MCP_Planner_Prompt.md` but the file is `mcp_planner_prompt.md`. It works only on macOS's case-insensitive filesystem, it's untracked, and a fresh clone in planner mode fails.
  5. **The planner prompt's example JSON is invalid** (`"depends_on":,`).
- **Code-read gaps:**
  - `depends_on` and "parallelizable" are ignored; steps run strictly in sequence.
  - The "Cmd? (optional)" input is collected and passed as `main_command`, but **never used**.
  - Config keys `max_autonomous_missions`, `max_spec_versions_to_load`, `github_integration`, the `tui_options.rich_log_*` options and `consumer.yaml` (the "BYOK consumer" mode) are **not referenced by any code**.
  - `APP_VERSION = "2.7.1"` while the files say v2.7.3. Anthropic model id `claude-3.5-sonnet-20240620` is malformed. Config maps Anthropic to `CLAUDE_API_KEY` and Gemini to `GEMINI_API_KEY_1/2`, which aren't in the local `.env`, so only OpenRouter/Ollama/clipboard work as configured.
  - There are no request timeouts.
  - The specs roadmap has duplicates and contradictions: "Workspace Root" is listed as done in 2.5.0 and also unchecked 3 times; the "Double Confirmation" safety latch, `undo`, chatbot mode and the model switcher are not built.
  - `.antigravity/knowledge/projectbrief.md` / `techContext.md` (dated 2026-06-28) were generated by an analyzer with **"Analyzed Files: None"** ("Inferred from Kimi K2.5"). They describe asyncio/FastAPI/PostgreSQL agents that **don't exist**. **Don't use them as a source.** This is also a data point against whatever tool generated them.

### Resume-ready takeaways
- "**Built an AI coding-companion TUI (Python/Textual)** with a hierarchical context engine (per-folder `AI_CEO.md` rules + 'project brain' briefing docs + selectable files or git-diff) and **three orchestration modes**: direct, **LLM triage routing** (a local Ollama model picks the provider), and a **planner→executor multi-agent pipeline** carrying in-memory file state across steps into one reviewed patch."
- "Provider-agnostic across OpenRouter, OpenAI, Anthropic, Gemini and local Ollama, plus a zero-API clipboard mode. Multi-key rotation, per-call latency/token/throughput telemetry, human-confirmed patch application with automatic backups and an append-only audit trail."
- Timeline value: dated **Nov 2025** evidence of the "Lego piece" modular philosophy and of triage-based cost routing, before AGENT_PROTOCOL (Feb–Mar 2026) and Claude Code Center.
- **Wording cautions:**
  - It's single-process and sequential. Don't say "parallel agents", "asyncio" or "FastAPI".
  - Don't claim "secret redaction" (Gemini leak), "autonomous missions", "undo" or "GitHub integration".
  - "Multi-agent" is fair only as **planner + executor role prompts**, not independent agents.

---

## 18. iphone-inventory-checker-v2 (Oct 2025 ancestor of §6 v3)

**Repo:** `amit-malhotra1/iphone-inventory-checker-v2`, private (404). **11 commits, 2025-10-07 → 2025-11-04**, 24 tracked files.
- Uncommitted: a Dec 14 2025 dashboard rebrand in `web/index.html` ("AMTrix Solutions Inc. – 2026 AI Era Edition", "Deep Void" glass styling) and untracked AMTrix brand-guideline docs in `shared/`.
- **No secrets found** (token-shape scan of the source; the Telegram token noted earlier is in v3, not here).
- v3 (§6) is a superset. The Swift app files are byte-identical in v3. All the Python, web and shell files differ: v3 is 1.4–7× larger.

### Read in full / Not read
- **Read in full:**
  - `cli/inventory_checker.py` (737), `cli/main.py` (213), `notify.py` (55), `store_profiles.py` (73), `__main__.py`
  - `shared/config.yaml` (112)
  - `start.sh` (139, including the folded long lines), `Makefile` (68)
  - `README.md` (150), `cli/README.md`, `web/README.md`
  - `.internal/system-prompt.md` (36)
  - the whole `<script>` of `web/index.html` (lines 72–607)
- **Structure only:** the Swift app (`Package.swift`, plus type/function maps of the 3 sources, 551 lines). The README marks it "DEPRECATED, do not use", but a release build exists in `.swiftpm` (Oct 7 2025).
- **Not read:** the `web/index.html` CSS/markup (lines 1–71), `style.css`, the `.bak` copies, `startOld.sh`, `fetch.log` (90k lines), and the saved HTML snapshots (I only parsed them in the probe).

### What it is
- **Python CLI (click):** `once` / `watch N` / `export`.
  - It scrapes a third-party aggregator (`iphonechecker.herokuapp.com/q/<zip>/<model>/unlocked`).
  - It follows "refresh" links up to 5×, extracts the embedded Next.js `{"props":…pageProps}` JSON, and falls back to BeautifulSoup table/badge parsing.
  - It maps part numbers to color and size and normalises names.
- **Freshness engine:**
  - It reads the page timestamp (`<small>` label, ISO in the page, or `pageProps.ts`).
  - Thresholds: target <30 s, warn ≤180 s, force-retry >600 s, and sub-2 s "too real-time" rejection.
  - It does ZIP rotation with randomized 1.5–3.5 s jitter, capped at `max_attempts`.
  - Per-model log tagging (`[iPhone 17 Pro Max] Attempt …`).
- **Outputs:**
  - `latest.json` (models → stores → color×size availability, store sync timestamps, warnings, age)
  - `latest.md` (NY vs CT/NJ tables)
  - raw HTML snapshots per model
  - **generated Apple buy-links** for every color/size from config slugs
- **Alerts:** a target-variant list fires desktop notifications (macOS `pync`). Email and SMS are explicit TODO stubs.
- **Dashboard:**
  - A static HTML/JS page with no backend (the stdlib `http.server`). It polls `latest.json`.
  - Model picker; color/storage/region card filters with select-all; per-store tables with ✓ buy-links.
  - A **client-side availability history**: it detects false→true transitions, dedupes by key, caps at 500 entries and persists in localStorage.
- **`start.sh` launcher:**
  - an interactive menu
  - venv creation and dependency checks (`--force-install`)
  - port-conflict detection: shows the process, offers to kill it, or picks a free port
  - starts watcher + web server with trap-based cleanup on Ctrl+C
  - opens the browser
  - **creates macOS `.command` / Ubuntu `.desktop` shortcuts**
- **SwiftUI macOS 13 companion app:** a Combine timer polls the same JSON, with filters and buy-links.
- **`.internal/system-prompt.md`:** an LLM handover/"inherit and continue" system prompt for the repo (mission, components, invariants, testing discipline, milestone changelog). It's early evidence of his **agent-handover documentation** practice (Oct 2025). It mentions a "Tahir milestone" (a name, recorded neutrally).

### Verified vs claimed
- **Ran (scratch copy, the project's own `.venv` interpreter, no network):**
  - `--help` works.
  - **The offline parser test on the saved Dec 14 2025 snapshots works:** pageProps extracted, 12 stores parsed per model, 144 (Pro Max) and 108 (Pro) color×size cells. Every one was "available", and the raw `pickupDisplay` values are all `available`, so the parser is correct and stock was simply plentiful by December.
- **Confirmed by running:**
  - **The README usage fails.**
    - `cli/README.md` shows `once --model … --colors … --sizes …`.
    - Real: these are *group* options (`--color/--size/--model`, singular and repeated) that must come **before** the subcommand.
    - `once --model i17Pro` → "No such option: --model". `--colors` → "Did you mean --color?".
  - **"Never accepts >10 min" is false.**
    - The CLI README says that; the root README says "keeps refreshing until … no more than 3 minutes old".
    - The probe fed a 1-hour-old (and 6-year-old) timestamp: after `max_attempts` (6) the code **accepts it with a warning** ("Accepted stale data after exhausting attempts").
- **Code-read gaps:**
  - Notifications re-fire **every cycle** while a target variant stays in stock (no dedupe server-side; the history dedupe is only in the browser).
  - `fetched_age_seconds = age or -1` turns a genuine 0 s age into "unknown".
  - The code default `max_attempts` is 25 vs 6 in config (config wins).
  - The uncommitted dashboard rebrand **removed the history filters**: `renderHistoryFilters` and `ensureHistorySelections` are now placeholders. That's a regression against the system prompt's "history filters mirror the main filters" invariant and commit `67584b8` "restore history panel".
  - Store names and timestamps from the third-party feed go into `innerHTML` unescaped (only filter labels use `escapeHtml`).
  - `python -m http.server` binds all interfaces by default, so the dashboard and JSON are LAN-visible. Low impact (public stock data).

### Resume-ready takeaways
- Use it as **the origin point** of the iPhone line (Oct 2025) → v3 (Oct 2026, 62 commits, SQLite, Safari automation, multi-channel alerts via notify-bus). Don't list v2 as a separate headline project; it overlaps v3.
- If you need a single line: "**Built a real-time retail-inventory monitor**: a scraper with freshness SLAs (timestamp-aged data, ZIP rotation with jittered retries), structured JSON/Markdown artifacts with generated deep-links, a filterable dashboard with transition history, a macOS SwiftUI companion, and a one-command cross-platform launcher (venv bootstrap, port-conflict handling, desktop shortcuts)."
- Evidence of **"LLM handover system prompts"** (Oct 2025), predating the AI_PROTOCOL/AGENTS work.
- **Wording cautions:** don't say "guaranteed fresh / never stale data" or "email/SMS alerts" for v2. Say "polls an aggregator", not "polls Apple".

---

## 19. Local-ai-code-assistant-v1 ("AI Companion Toolkit" v1.3 → v1.6.x; predecessor of §17)

**Repo:** `amit-malhotra1/Local-ai-code-assistant-v1`, private (404). **12 commits, 2025-11-08 → 2025-11-14** (v1.3.1 baseline → "v1.6.9 Stable").
- `.env` holds key names only (GEMINI_API_KEY_1/2, ANTHROPIC, OPENAI, OPENROUTER, OLLAMA, AI_PROVIDER). It's untracked and was never in history.
- Uncommitted: a typo fix in specs, a `boilerplate_project` README, and `manuals_drafts/app_actions copy.py`.
- Untracked: an older `AI_PROTOCOL_TEMPLATE/` (Dec 2025) and `.antigravity/knowledge` (the same "Analyzed Files: None" generated brief as §17; don't use it).
- `boilerplate_project/` (excluded by the user's rule) and `manuals_drafts/` (~20 versioned snapshots of api_client/app_actions) are scaffolding.

### Read in full / Not read
- **Read in full:**
  - `src/api_client.py` (215), `app_actions.py` (239), `gatekeeper.py` (157)
  - `config.yaml` (comments stripped)
  - `briefing_documents/system_prompt.md` (49)
  - `README.md` (263: four stacked version READMEs, v1.6.3 / v1.6.0 / v1.4.3 / v1.3.0)
  - the specs head and its diff
- **Diffed against §17:** objective/manifest/philosophy/standards are identical except for trailing separators.
- **Mapped:** `tui_screens.py` (116; classes/inputs only).
- **Not read:** the `manuals_drafts/*` snapshots, `.ai_chronicle.md` body (28 entries: Clipboard 53 model tags, deepseek 9, gemini-2.5-pro 7), `project_architecture.md` (the same Mermaid as §17).

### What it is (and what's different from §17)
- The same TUI concept, one generation earlier:
  - s/r/a/e/p/h/q bindings
  - `target_project_root` portability ("super folder": tool + target side by side)
  - EOF full-file patch protocol with backup and audit log
  - line-numbered file context (`12:def foo():`) for precise LLM references
  - multi-key rotation (`itertools.cycle` every N requests)
  - per-call latency/tokens/tok-s
  - Clipboard mode and an `ai_enabled` kill switch
  - git pre-flight
- **Things only in v1:**
  1. **Command-in-the-loop "Execution Report".** The "Cmd?" field is **actually executed** (`subprocess.run(cmd, shell=True)`), and its exit code + stdout/stderr go into the prompt. That's an early test-output-feedback loop. In §17 v2.7.3 the field is still shown but no longer used.
  2. `max_spec_versions_to_load` **works here**: it trims specs.md to the newest N `---` sections, a token budget for the project history. In v2.7.3 it's dead config.
  3. Triage has a key-presence check *before* the triage call, and a **3-way goal classification** prompt (code_generation / simple_refactor / general_question → provider).
  4. TUI theme engine (dracula/monokai) and the `rich_log_*` options are wired here; v2.7.3 dropped them.
  5. **`system_prompt.md` "Adaptive Patching Strategy":** present changes at Level 1 snippet / Level 2 function / Level 3 multi-function for human review, but **always** emit the full-file EOF block for machine application. Plus rules such as "don't modify the tool unless asked", "respect test goals", "no comment churn". Early **modular instruction design** (Nov 2025) with the "Lego pieces" framing in the system prompt itself.
- Chronology from the README: v1.4.3 applied patches as a `TEMP_CHANGE.diff` **opened in VS Code for visual review**. v1.6 replaced the brittle `patch`/diff with the EOF full-file overwrite, which the README frames as "100% reliability".

### Verified vs claimed
- **Ran (scratch copy, `.env` excluded, the §17 scratch venv, local mock server only):**
  - The TUI mounts headless (Textual `run_test`, help rendered).
  - **Key redaction works in v1:** a Gemini 400 error showed `…?key=[...3456]`, masked to the last 4. So the **§17 v2.7.3 leak is a regression**: the HTTPError branch was rewritten without redaction. Spec v1.6.2's "redacts secret keys" was true for v1.6.x.
- **Bug confirmed by running:**
  - **Ignore files are only half honoured.** The scanner reads only **directory** patterns (lines ending in `/`) from `.gitignore` / `.ai_ignore`.
  - In a scratch target whose `.gitignore` listed `secrets.log` and `*.pem`, the pre-selected file list included **`secrets.log`, `key.pem` and `.env.local`**. Only `build/` was excluded.
  - Those files go to the LLM unless the user deletes the lines in the review modal.
  - The README test A-02 and specs "Hardened Context Engine… respects .ai_ignore" overstate this.
  - The commit title "**Git-Powered** File Scanner" is a misnomer: no `git ls-files` / `check-ignore` appears in any commit. It means "reads .gitignore directory entries".
- **Code-read gaps:**
  - The `.ai_backups/` path is relative to the tool cwd, not the target, so different targets can collide.
  - Same patch path-traversal pattern as §17 (`root / header`, no containment), behind a y/N confirm.
  - `SmartRouter()` is instantiated at import (needs `config.yaml` in cwd).
  - No request timeouts.
  - "Cmd?" runs `shell=True` on every Start/Refine, even with the default `echo No command`. It's user-typed, so it's a feature, but say "executes a user-specified command" honestly.
  - Same malformed Anthropic model id as §17. The triage default is `gemini-1.5-flash` (dated).

### Resume-ready takeaways
- Fold this together with §17 as **one project, "AI Companion" (Nov–Dec 2025, v1.3 → v2.7.3)**. Don't list them separately.
  - The story arc: **diff-patch → EOF full-file protocol → triage routing → planner/executor**, all inside 6 weeks.
  - It shows rapid iteration and versioned release discipline (12 commits with semver release notes, stacked README changelogs, an explicit test-case table A-01…E-01).
- Additional bullet material:
  - "Closed the loop between execution and the LLM: the assistant runs a user-specified command and feeds exit code and output back into the prompt."
  - "Designed an adaptive patch-presentation protocol: human-reviewable granular views, machine-applicable full-file blocks."
- **Wording cautions:**
  - Don't claim "git-powered scanner" or "respects .gitignore" in full.
  - Claim "secret redaction" only for v1.x (it regressed in v2.7.3).

---

## 20. ReactTSApp (Sep 2025): Replit-generated starter, not resume material

**Repo:** `amit-malhotra1/ReactTSApp`, private (404). **5 commits, all on 2025-09-09.**
- **4 of the 5 commits are authored by the GitHub identity `nitinkak22`**: "Initial commit", the Replit Agent scaffold ("Introduce a comprehensive React + TypeScript application setup…"), and two one-line edits. Only the final commit `02b8cb5` is `amit-malhotra1`.
- The user says all projects are theirs. That could be a second account of theirs or a Replit workspace identity. I'm recording it as a fact, not a judgment. **If a reviewer ever opens this repo, the commit history won't show the user as the author of the scaffold.**
- Uncommitted: an App.tsx fix. Untracked: a VS Code Docker-extension `Dockerfile` / `.dockerignore` / `.vscode` tasks and the generated `.antigravity` brief.

### Read in full / Not read
- **Read in full:**
  - `replit.md`, `.replit`, `package.json` scripts and dependency counts (63 deps / 22 dev)
  - `server/index.ts`, `routes.ts`, `storage.ts`, `shared/schema.ts`
  - `Dockerfile`, `.dockerignore`, `.vscode/launch.json`, `.vscode/tasks.json`
  - the `App.tsx` diff and blame
- **Skimmed:** the 9 custom landing components and pages (732 lines, text and handlers only).
- **Not read:** the 48 generated `components/ui/*` shadcn files, `server/vite.ts`, `package-lock.json`.
- **Not run:** there's no `node_modules`, and installing 85 packages to build a template adds nothing.

### What it is
- The **Replit Agent full-stack starter**: React 18 + Vite + Wouter + TanStack Query + shadcn/Radix + Tailwind on the front end, and Express + Drizzle (Postgres/Neon) + Zod + an in-memory `MemStorage` on the back end.
- **`registerRoutes` has no routes.** The UI is a static marketing page *about* React+TS (features grid, project structure, quick-start terminal, "Lighthouse Score" stats).
- **Defects:**
  - The committed HEAD has `<Route component={Not-Found} />`, introduced by `02b8cb5`. That's an undefined `Not` and a TS/runtime error. It's fixed only in the uncommitted working tree.
  - The untracked Dockerfile is the generic VS Code template: `EXPOSE 3000` while the app listens on 5000; `npm install --production` drops vite/esbuild; `npm start` needs `dist/` from a build that never runs. **The image wouldn't start.**

### Resume-ready takeaways
- **Leave it off the resume.** It's a generated scaffold with no custom logic, and the authorship mix is a risk.
- At most it shows familiarity with the Replit Agent / Vite + Express + Drizzle stack, which is already better evidenced elsewhere (AMTrix Plan, claudecodeui). **Treat it as excluded**, like TEST/DEMO/boilerplate.

---

## 21. amtrix-identity-engine (Dec 2025 → Jan 2026): YAML-driven brand-kit generator + drop-in "Studio Tuner" loader

**Repo:** `amit-malhotra1/amtrix-identity-engine`, private (404). **13 commits, all by Amit Malhotra:** initial on 2025-12-14, then 12 on 2026-01-19 (Studio Tuner v3.2 → v3.3 "VFX Matrix", cache busting, config export, AVG-2026 post-mortem, docs v3).
- Untracked: `showcase.py`, `ARCHITECTURE_AND_HISTORY.md`, `_AICEO_VISUAL_ENGINE/`, the brands/core/.ai READMEs, `backup_Obsidian/`, `.antigravity/`, `.vscode/`. Modified: README, `HOW_THE_MAGIC_WORKS.md`, the `.ai` vault.
- `output/` is gitignored. Only 4 Obsidian files are force-tracked: `brand_loader.js`, `adaptive_brand.css`, `STUDIO_TUNER_GUIDE.md` and `AVG_2026_DESIGN_SYSTEM.md`.

### Read in full / Not read
- **Read in full:**
  - Docs: README, `HOW_THE_MAGIC_WORKS.md`, `ARCHITECTURE_AND_HISTORY.md`, `STUDIO_TUNER_GUIDE.md`, `AVG_2026_DESIGN_SYSTEM.md`, `GITHUB_SETUP.md` (from the scratch copy)
  - Code and config: `engine.py` (and its diff to `engine_v2.2.py`: header only), `showcase.py`, `core/templates/brand_loader.js` (448 lines), `output/AMTrix_Obsidian/brand_loader.js` (718 lines), `studio.html`, all 4 `brands/*.yaml`
- **Partly read:**
  - `AMTrix_Branding_20261901/AMTrix_Summary_Overview.md` (first 80 of 426 lines)
  - `AGENTS.xml` header: the same AI Protocol v4.0 as §11b
  - `_AICEO_VISUAL_ENGINE/README.md` head: the doc-standards kit from §11a/§16
- **Checked by grep only:** both `adaptive_brand.css` files, for the classes the loader toggles.
- **Not read:**
  - the other 8 branding-research files (~5.4k lines, one commit)
  - `amtrix-brand.css` (42 KB; nothing loads it)
  - `demo/slide_deck/word_bridge.html`, the `.md` templates, `TWEAK_GUIDE`, the backups, the Mermaid prompt HTML
  - `.antigravity/knowledge/*`: **access to `~/Documents/GitHub` was revoked (EPERM) partway through this section**, so anything not already in the scratch copy is unread.

### What it is
- **`engine.py`** (111 lines): reads a brand YAML (`meta/colors/typography/theme/...`) and renders every file in `core/templates/` into `output/<meta.name>/`.
  - It uses a hand-rolled `{{section.key}}` substitution plus a minimal `{% if a.b == 'x' %}…{% else %}…{% endif %}` evaluator (no nesting).
  - `brand.css` uses this for real adaptive light/dark (`@media (prefers-color-scheme)` in `Universal_Default`) and for Glassmorphism-only blocks.
- **`brand_loader.js`** ("Secret Agent"): one `<script>` tag that injects Google Fonts + `adaptive_brand.css` and a floating ⚡ **Studio Tuner** panel. The panel has:
  - presets: Obsidian / Titanium / Ghost
  - per-component radius/blur/border/opacity sliders (Global/Panels/Cards/Btn/Inputs, plus "Link All")
  - a palette and an RGB-cycle
  - in v3.3: neon Solid/Pulse with a speed slider, ambient glow, a **VFX Matrix** (Float/Sway/Neon × Panel/Card/Btn/Input + Liquid), 6 quick OLED themes, Reset, and **JSON config export**
  - mouse-tilt 3D on cards
  - state kept in `localStorage['AMTrix_Config_v3']`
- **`showcase.py`**: a curses TUI plus a `--HEADLESS` mode. It scans `output/`, builds a glass `dashboard.html` index, copies the Obsidian loader and CSS in, and snapshots a kit to `<name>_vYYYYMMDD_HHMM`.
- **`AVG_2026_DESIGN_SYSTEM.md`** is an honest post-mortem of a "7-hour fix-break loop". It covers opacity vs RGBA darkness, CSS animations caching variable values (fixed with the reflow trick `forceAnimationRestart()`), and the OLED low-opacity formula.

### Verified by running (scratch copy, headless Chrome, fresh profile; no network beyond the fonts URL)
- **Engine works on all 4 YAMLs** (exit 0, 4 kits). Unrendered placeholders remain wherever a YAML lacks a key the template uses:
  - `{{typography.font_primary/secondary}}`, `{{colors.glass_border}}`, `{{colors.text_high/med}}`, `{{ppt.*}}`
  - affected: 14 files across Light / Solutions Inc. / Universal_Default / Obsidian
- **Regenerating overwrites the real v3.3 work.** `brands/amtrix_next_gen.yaml` has `meta.name: "AMTrix Obsidian"`, so running the engine on it writes into `output/AMTrix_Obsidian/`. Both files get replaced with the **older template** versions, which lack the VFX Matrix, quick themes, neon and ambient:
  - `brand_loader.js`: 36,418 → 22,903 bytes
  - `adaptive_brand.css`: 17,626 → 11,552 bytes
  - The v3.3 features were hand-edited in `output/` and **never back-ported to `core/templates/`**.
- **Template loader (`core/templates`):**
  - `init()` throws `ReferenceError: startLoops is not defined`.
  - Palette swatches throw `ReferenceError: state is not defined`: the inline `onclick` can't see the IIFE-scoped `state`, so color never changes.
  - The "Panels" target throws `TypeError … reading 'radius'`: `updateUI`'s map has no `panel` key.
  - Slider changes are never saved.
- **v3.3 loader (`output/AMTrix_Obsidian`):** init, palette, quick themes and VFX class toggles work, but:
  - The "Panels" target still throws the same TypeError.
  - VFX buttons keep showing "OFF" after toggling: `toggleVFX` calls `window.updateUI`, which is never exported.
  - **Slider edits aren't persisted** (the saved cardRadius stayed 16 after setting it to 50).
  - **Neon mode, ambient and speed are saved but not restored on reload.** The saved values were `neonMode=solid, ambient=false, speed=6`; after reload the classes were absent and `--neon-speed` was unset. `fx*` flags are restored.
  - The Google Fonts URL in the committed loader still contains the literal `{{typography.font_primary}}`. Outfit/Inter never load from it, and `showcase.py` copies this file into `output/` while calling it the "processed loader".
- **`showcase.py --HEADLESS`:**
  - Generates the dashboard with 7 cards and copies the loader and CSS.
  - It crashes at import if `.ai/` is missing (`logging` FileHandler). That's fine in this repo, but it isn't portable.
  - Project names go into the HTML unescaped (local-only).

### Verified vs claimed
- **"Glass Polish: scans for `<nav>`, `.card` and stamps `.amtrix-glass`"** (HOW_THE_MAGIC_WORKS step C): **no loader does this**, and no CSS defines `.amtrix-glass`. The class appears only in an old `AMTrix_Next_Gen` output and the dashboard markup.
- **"Inject Outfit/Inter fonts"**: broken in the committed loader (placeholders, see above).
- **README "Seamless Blend… `@media (prefers-color-scheme)`"**: true for `brand.css` via `default_adaptive.yaml`, but **not** for `adaptive_brand.css` (no media query).
- **README:**
  - "Engine v2.3"; the file header says v3.0.
  - "Paste `IMAGE_GUIDELINES.md`"; the actual outputs are `image.md` / `doc.md`.
- **Broken doc links:**
  - `ARCHITECTURE_AND_HISTORY.md` points to `_AICEO_TOOLKIT/`, which **doesn't exist** (it's `_AICEO_VISUAL_ENGINE/`).
  - `HOW_THE_MAGIC_WORKS` links `./demo_override.html` at the root; it lives in `core/templates/`.
- **STUDIO_TUNER_GUIDE:**
  - "All settings are saved to localStorage": partly false (sliders; neon/ambient/speed not restored).
  - "5 curated themes": the code has 6 (+ Golden Outline).
- **`AMTrix_Branding_20261901/`** is AI-generated guideline output ("Congratulations! You now have four comprehensive brand guideline documents…"). It specifies a **Deep Teal palette that v3.0 explicitly "killed"**, and claims WCAG AAA without evidence. Treat it as research input, not the shipped system.
- "Multi-Tenant: unlimited brands via YAML" is true in mechanism. "React/Vue/Angular works natively" is plausible (plain DOM injection) but untested.

### Resume-ready takeaways
- **Worth one line, best inside a "design systems / developer experience" cluster with the Mermaid dashboard (§11a) and the vscode_core Markdown design system (§15),** not as a headline FDE project.
- The honest pitch: "Built a **config-driven brand-kit generator** (YAML → CSS/HTML/doc/PPT/image guideline templates, with conditional light/dark/adaptive blocks). Also built a **single-script drop-in theming layer** with a live tuner (presets, per-component physics, VFX matrix, JSON export) that restyles any existing HTML page without touching its markup."
- It strongly supports the **Lego-piece / plug-and-play** theme: one `<script>` tag, no build step, portable kits.
- The **AVG-2026 post-mortem** is a good interview story: a 7-hour fix-break loop → root cause (CSS animations snapshot custom-property values) → a documented fix and "rules for future LLMs". It shows debugging discipline and writing for AI successors.
- **Wording cautions:**
  - Don't claim "auto-glass class stamping", "fonts injected automatically", or "all settings persist".
  - Before a demo: back-port the v3.3 loader/CSS into `core/templates/`, fix the `panel` map / `window.updateUI` / restore-on-load bugs, and add `typography.font_*` to all YAMLs. Otherwise the documented Quick Start silently downgrades the showcase.

---
