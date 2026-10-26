# Source Audit: What I Read to Write the FDE Profile (2026-10-25)

This is pulled from the session log (every tool call I made). Nothing has been changed since your last message.

## The short answer

- **I did NOT read whole files in your project folders.** For each project I ran shell scripts that captured:
  - the **top-level folder listing** and **counts of files by type** (.py, .ts, .md and so on)
  - **git stats**: number of commits, first and last commit date, remote URL (from `git log`, not the code)
  - **dependency lists** from `package.json`, `requirements.txt` and `pyproject.toml`
  - the **first 45 non-blank lines of the README** and the **first 25 lines of CLAUDE.md**, with each line cut at 220 characters
- I then ran **targeted keyword searches (grep) inside the source code and SNAPSHOTS.md** for 5 projects: Claude Code Center, the MCP server, AI Pandit, AGENT_PROTOCOL and Ollama Powerhouse.
- So for most projects I went **beyond the README, but not deep**: README/CLAUDE.md excerpts, plus git history and dependencies. Only the 5 projects above got a look inside the code.
- In this portfolio folder I **read the files I edited in full** (except where noted below).

The exact text I saw is saved here (temporary folder, so copy it if you want to keep it):
`/private/tmp/claude-501/-Users-Amit-Malhotra-Documents-GitHub-AMTRIX-TOOLS-AMIT-RESUME-PORTFOLIO/7498ac15-89be-4e47-8e27-1904c7315ca5/scratchpad/` → `digest.md`, `digest2.md`, `digest3.md`, `digest4.md`

---

## Per project: what I actually looked at

Legend: ✅ = read (excerpt) · 🔍 = keyword search inside code · ⚠️ = thin evidence

| Project | What I read | Depth |
|---|---|---|
| **claude-code-center** | README (first 45 lines), CLAUDE.md (25), `CORE_ARCHITECTURE.md` (40), `config/models.json` (60), package.json deps, git stats; 🔍 grep of `src/*.js` for vertex / rawPredict / google-auth / tools; 🔍 grep of `SNAPSHOTS.md` for vertex / openrouter / subscription; list of `docs/` | **Deepest.** Vertex, SSE accumulator, `.claudesignore`, 32,768-byte cache and "total system loss" came from the src grep + SNAPSHOTS |
| **amtrix-impl-plan-standards** | README (45), CLAUDE.md (25), `amx_impl_plan/README.md` (40), git stats (365 commits, v0.44); grep for "skills build" | Medium |
| **Manoj_Project/0150_MCP_SERVER_DEMO** | README (20), `config.yaml` (50), `docs/mcp_server_pros_cons.md` (30); 🔍 grep of `server.py` for provider / model / tool / def; folder listing + `000_PROJECT_HISTORY` | Medium. The 10 tools, Bedrock + OpenRouter and 60K/8-call anti-truncation came from here |
| **amtrix-ai-pandit** | README (45), git stats; 🔍 grep of `astro_engine/src/*.py` for `def` / `class` / `swe.`; 🔍 grep of `SNAPSHOTS.md` for shadbala / ayanamsa / score; list of `tests/` | Medium |
| **AGENT_PROTOCOL** | package.json, `ANTIGRAVITY_VSCODE_RULEBOOK.md` (20), `AI_agent_protocol/README.md` (lines 1–20 and 30–90), listings of `_ARCHIVE`, `_NEXUS`, `AI_PROTOCOL_TEMPLATE` | Medium. Version history v17.5→v19.5 and `universal_context.py` (1,085 lines) came from the README |
| **ollama-powerhouse-openwebui-docker-v1** | README (45), requirements.txt, git stats; `models.conf` (non-comment lines); 🔍 grep of `docker-compose*.yml` for images / ports / env; keyword count across its .md files (tailscale, searxng, m1 max…) | Medium |
| **frontier-triage-engine** | CLAUDE.md (25), folder listing. No README found | ⚠️ Light |
| **AMTrix-core** | CLAUDE.md (25), `AMTrix_Help.md` (30), first .md in `docs/` (turned out to be a Grok chat backup, 20 lines), listing of `skills/` and `AMtrix_Skill_Viewer`, git stats | Light–medium |
| **AMTRIX-TOOLS** (notify-bus, Patch-TUI, subscription tool, amx-kit) | Folder listings; `AMTRIX-Patch-TUI/README.md` and `amtrix_claude_subscription_tool/README.md` (30 each) | ⚠️ **notify-bus: listing only** (Caddyfile, docker-compose, clients…). I did not open its QUICKSTART.md |
| **BACKUP_VISION_LLM_COMET_TRADER** | `VISION_LLM_FEASIBILITY_ANALYSIS.md` (40), `LLM_SESSION_MANAGEMENT_DEEP_DIVE.md` (25), `local_autotrader/README.md` (40), listing | Light–medium. This is the main source for the Vision Agent section |
| **vision-agents-builder-v1** | Folder listing + file-type counts only. No .md found within 2 levels | ⚠️ **Very thin** |
| **complex-amtrix-engineered-prompts-v1** | `UNIVERSAL_ROUTER_GUIDE.md` (25), `NEXUS_QUICK_REFERENCE.md` (25), `AICEO_FACTORY/README.md` (20), listing of `VISION_LLM_COMET_TRADER/` | Light |
| **amtrix-voicebus** | README (45), package.json deps. Not a git repo, so no commit stats | Light |
| **iphone-inventory-checker-v3** | README (45), CLAUDE.md (25), git stats (62 commits) | Light |
| **iphone-inventory-checker-v2** | README (45), git stats | Light |
| **ai-context-compressor-v1** | README (45), requirements.txt, git stats (25 commits) | Light |
| **amtrix-studio** | README (45), requirements.txt, git stats | Light |
| **PromptForge-The-Prompt-IDE-v1.9.7** | README (45), package.json deps, git stats | Light |
| **amtrix-identity-engine** | README (45), git stats | Light |
| **apple-watch-dashboard** | README (45), package.json deps | Light |
| **Local-ai-code-assistant-v1** | README (45), git stats | Light |
| **custom-alexa-skills** | `SmartBrain/README.md` (15 lines), listing | ⚠️ Thin |
| **multi-agent-assistant-v1** | git stats + listing. README not found where I looked | ⚠️ Thin |
| **ReactTSApp** | package.json deps, git stats | ⚠️ Thin |
| **amtrix_vscode_core** | `MARKDOWN_FILES/temp.md` (15 lines), listing | ⚠️ Thin. The file I picked wasn't a useful one |
| **n8n** | Was in the first scan (README / CLAUDE.md). **Removed from all documents** after you excluded it | — |

## Portfolio folder (AMIT_RESUME_PORTFOLIO)

- **Read in full:** README.md, AGENTS.xml (first 120 lines), PROJECT_NEXUS.xml, `.ai/_VAULT/CONTEXT.xml`, `.ai/_VAULT/ACTIVE_SESSION.md`, LinkedIn_Profile.md, Quick_Reference_Card.md, Resume_BusinessAnalyst_PM.md
- **Partially read:** Resume_Complete_TechnoFunctional.md (first 120 non-blank lines, then lines 1–40), RESUME_PORTFOLIO_MASTER.md (first 40 lines), Interview_Questions.md (first 200 lines), and the first 3–8 lines of the 5 January-snapshot docs (to place the banner)
- **Not read:** STRATEGIC_PITCH/, `.ai/_CORE/USER_PROFILE.md`, the rest of DATA_REFERENCES/

## Where the profile goes beyond the evidence

1. **"40–90% cost reduction"**: copied from the CCC README. I never measured it.
2. **Vision Agent**: based on 3 strategy/README docs. I did not open any trading or vision code.
3. **notify-bus and VoiceBus**: notify-bus from a folder listing, VoiceBus from its README. Their descriptions are general.
4. **"How I Think / Lessons from the Trenches"**: mostly taken from what **you told me** in chat, backed by the friction-log and version-history style found in AGENT_PROTOCOL and AMTrix Plan.
5. **Connected Ecosystem table**: based on folder names showing up in several projects (`AI_PROTOCOL_TEMPLATE` in 10+ repos, `frontier_triage_engine` inside the MCP server). I did not trace the actual sync code.

## Pending change (on hold until you say go)

- Replace "originally built for a partner's IDE workflow" with wording that makes the MCP server clearly **yours**. I'll also stop flagging the IDE work as something to leave out. **Done 2026-10-25.**
- If you want, I can do a **deeper second pass** on the ⚠️ rows (vision-agents-builder, notify-bus, multi-agent-assistant, amtrix_vscode_core, custom-alexa-skills). That means reading their main source files, not just the READMEs.
