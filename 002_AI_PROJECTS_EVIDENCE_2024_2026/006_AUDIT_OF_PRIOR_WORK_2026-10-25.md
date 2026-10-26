# Audit of prior work — 2026-10-25 (Fable 5.1 pass)
> 🕒 Last changed: v0.1.1 · 26-10-25__14.33.21
> 🗓️ Created: 26-10-25__14.33.21
> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 00:00 UTC+4  
> **Status:** Baseline

Scope: what the previous model produced in this session (deep-read notes §1–21, the FDE profile, resumes, LinkedIn, interview prep, PROJECT_NEXUS). Goal: find shortcomings, then fill them and produce résumé / LinkedIn / job-application content that survives a fact check.

---

## 0. Blocker: the re-grant did not cover `~/Documents/GitHub`

Tested after your re-grant. Only these paths are readable:

| Readable | Blocked (EPERM) |
|---|---|
| `AMTRIX-TOOLS/` (this portfolio) | `claude-code-center`, `AGENT_PROTOCOL`, `multi-agent-assistant-v1`, `amtrix-ai-pandit`, `notify-bus-linux` |
| `amtrix-identity-engine/` | **All 6 unread projects:** `ai-context-compressor-v1`, `custom-alexa-skills`, `ollama-powerhouse-openwebui-docker-v1`, `amtrix-studio`, `PromptForge-The-Prompt-IDE-v1.9.7`, `vision-agents-builder-v1` (and `claudecodeui`) |
| `amtrix-voicebus/`, `iphone-inventory-checker-v3/` | listing `~/Documents/GitHub` itself |

The grant seems to have applied per-folder. Please grant the parent folder `/Users/Amit_Malhotra/Documents/GitHub` (or each project folder). Until then I can only work on portfolio files and the three readable projects.

---

## 1. Deep-read coverage (DEEP_READ_NOTES_2026-10-25.md, 21 sections)

**Solid (code read in full, claims tested by running):** §1 claude-code-center (proxy_server.js 3,151 lines + all `src/proxy`), §2 MCP server, §3 frontier-triage, §7 subscription tool, §8 notify-bus (every file), §9 Patch-TUI, §12 apple-watch, §13 pandit, §14 VoiceBus, §16 AGENT_PROTOCOL, §17 AI Companion v2, §18 iPhone v2, §19 AI Companion v1, §20 ReactTSApp, §21 identity engine (finished today, headless-Chrome probes).

**Partial — needs a second pass under your "entire project, no shortcuts" rule:**

| § | Project | What was skipped |
|---|---|---|
| 4 | AMTrix Plan | 11 docs not read (ARCHITECTURE, HOW_CHECKS_WORK, WORKER_PLAYBOOK, RULES_LEDGER, rules.md, operator.md, FAQ, FEEDBACK_LOOP, FOOTER_DESIGN, PICTURES, GLOSSARY); test suite count not measured (the notes say "use the number `finish` records") |
| 5 | AMTrix-core | `rebuild_bcbs_artifacts.py` first 60 lines; `LATEST_CONTEXT.md` first 80 lines; a "Not read" list exists |
| 6 | iPhone v3 | `Enhancments_by_Opus.md` first 80 lines only; live tests not run (network); notes predate the "entire project" demand |
| 10 | Vision trader | 5 modules + `tools/*` + 37 routine JSONs unread; tests 1/3 on a scrubbed copy; "~700 Python modules" not re-counted |
| 11b | Prompt library | 100 KB AI-CEO prompt read in parts (intro + sections 2–6) |
| 15 | vscode_core | 4 scratch notes unread (low value) |

**Not read at all (6 projects), yet already described in the résumé:** the Private AI Platform flagship (#3), PromptForge, SmartBrain Voice Agents, AMTrix Studio, Context Compressor and Vision Agents Builder rows rest on three *earlier-session* files (`Ollama_Powerhouse_Analysis.md`, `PromptForge_Analysis.md`, `SmartBrain_Analysis.md`). Those are "Executive Competitive Analysis" marketing write-ups ("the first professional IDE…", "the only Alexa skill…"), not code reads. Every number in flagship #3 (Q5_K_M/Q6_K_XL, 128K–192K context, Watchtower, Tailscale, SearxNG) is **unverified** until I read that repo.

---

## 2. Factual defects in the current résumé set

| # | Claim | Where | Evidence says | Fix |
|---|---|---|---|---|
| 1 | "originally built for a **partner's** IDE workflow" | FDE_PROFILE:219; PROJECT_NEXUS.xml:45 ("do not name partner"); `.ai/_VAULT/ACTIVE_SESSION.md:34`; SOURCE_AUDIT:70; PROJECT_EXPERTISE_ANALYSIS:83,210 | You: "it is mine… It's all mine." | Rewrite as your own IDE-integration work; sweep all 6 places |
| 2 | **Full-Stack Reference App** (ReactTSApp) listed as a supporting system | FDE_PROFILE:311; PROJECT_NEXUS.xml:70; PROJECT_EXPERTISE_ANALYSIS:154 | §20: Replit scaffold, no routes, 4 of 5 commits by GitHub identity `nitinkak22`, Dockerfile can't start | Remove from all outward docs |
| 3 | AI Companion Toolkit: "**API-key redaction**" | FDE_PROFILE:306; PROJECT_EXPERTISE_ANALYSIS:152 | §17: v2.7.3 leaks the Gemini key in HTTPError text (regression from v1.x which did redact) | Say "secret redaction in error paths (v1.x)" or drop |
| 4 | "**~700 Python modules**" (vision agent) | FDE_PROFILE:250; Resume_TechnoFunctional:55; PROJECT_NEXUS.xml:47 | Never re-counted in §10; the count may include venv/duplicates | Count `*.py` excluding venv/old versions, then state the real number |
| 5 | AI Protocol Template "installed in **10+ projects**" | FDE_PROFILE:110,117; README:91; TechnoFunctional:108; BA_PM:31; Quick_Reference:49; Interview_Questions:302 | Not measured anywhere in the notes | Count `.ai/` installs across `~/Documents/GitHub`; use the measured number |
| 6 | "**2.5 years** of hands-on engineering on LLM systems" | FDE_PROFILE:11,409; TechnoFunctional:10; LinkedIn:19; Quick_Reference:14; EXPERTISE:20,174 | Repo evidence starts **Sep 2025** (13 months). AKM USA chatbots (2017–22) are pre-LLM | **Need your answer:** what work covers Apr 2024 → Sep 2025? Otherwise say "since 2024" only if true, or "a year of intensive…" |
| 7 | "Computational Ephemeris… **46 commits**" | FDE_PROFILE:267 | §13 header doesn't record a commit count | Verify from git log |
| 8 | Interview prep still teaches "**prompt engineering**" | Interview_Questions.md:117–123 (Section 3 title + Q8) | Your rule: soften to "modular instruction design / LLM instruction sets" | Rewrite Section 3 |
| 9 | "**AMX Plan**" used 7× | PROJECT_EXPERTISE_ANALYSIS_2026-10-25.md:30,45,94,166,182,183,201 | Your rule: "AMTrix", never "AMX" | Replace |
| 10 | Superseded source files still carry banned content ("prompt engineering", "111+ principles", "AI Development Partner") | DATA_REFERENCES/RESUME_PORTFOLIO_MASTER.md, RESUME_PORTFOLIO_CONTENT_v1.md | Earlier-session drafts | Move to `_ARCHIVE/` with a SUPERSEDED banner so nobody copies from them |
| 11 | Identity Engine row: "generates adaptive CSS, documentation and presentation assets" | FDE_PROFILE:310 | §21: true for `brand.css`; the stronger, verified story is the one-script drop-in theming layer + live tuner | Reword |
| 12 | Mermaid diagram in the FDE profile | FDE_PROFILE:76–113 | Won't render in PDF/DOCX/ATS | FIXED (second pass): replaced with a dependency table |
| 13 | Private AI "128K–192K-token context windows" | FDE_PROFILE flagship 3 | `ollama show` reports 262,144 native context and `num_ctx 256000` on two of the 30B models | FIXED: "256K-token context as configured" |
| 14 | "Hooks for all three agents (Claude Code, Codex, Gemini)" and "deployed across multiple projects" | FDE_PROFILE flagship 2 | FAQ: Codex and Antigravity adapters "not yet seen running in the real app"; deployed to 3 projects | FIXED: "used live with Claude Code; adapters for Codex and Antigravity"; "deployed to three of my projects" |
| 15 | Availability platform "62 commits (Dec 2025–Oct 2026)" and "30+ retail locations" | FDE_PROFILE flagship 8 | v2 origin Oct 2025; v3 record Oct 2026; profiles carry a 35-store registry | FIXED with the verified runtime, parser and dispatcher facts |

Verified-OK spot checks: Frontier Triage "recursive secret redaction" (§3 audit_tracer), notify-bus/VoiceBus stack lists, Patch-TUI description, Claude Code Center Vertex/MaaS claims (§1 code read).

---

## 3. Shape of the deliverables

- `AMIT_MALHOTRA_FDE_PROFILE_2026.md` is **424 lines**. It's a good *dossier* (portfolio site / long-form PDF), not a résumé. Recruiters and ATS need a **2-page résumé**; LinkedIn needs a **≤220-char headline, ≤2,600-char About, Experience bullets, Featured items**.
- `LinkedIn_Profile.md` (149 lines) and `Resume_Complete_TechnoFunctional.md` (114 lines) exist but inherit defects #1–#7 above.
- Nothing yet for **job applications**: no cover-letter template, no 3–4 STAR stories keyed to FDE job-description bullets, no "why FDE" paragraph, no tailored variants (enterprise AI platform team vs. AI-startup FDE vs. 1099 consulting).
- Not reviewed by anyone this session: `STRATEGIC_PITCH/` (Jan 2026), `INTERVIEW_PREP/Resume_FullDetail_PERSONAL.md`, `.ai/_CORE/USER_PROFILE.md`.

---

## 4. Proposed plan (in order)

1. **You:** re-grant `/Users/Amit_Malhotra/Documents/GitHub` (parent folder).
2. **Deep-read the 6 unread projects** (§22–27), same method: visibility check, git authors, full docs-or-code read, run tests/probes on a scratch copy, no paid APIs, no secrets.
3. **Second pass** on §4, §5, §6, §10, §11b to close the "partial" gaps; re-count the two numbers (#4, #5).
4. **Apply the 12 fixes** across FINAL_RESUMES, PROJECT_NEXUS.xml, README, INTERVIEW_PREP; archive the two superseded DATA_REFERENCES drafts.
5. **Rebuild the outward set:** 2-page ATS résumé · LinkedIn (headline / About / Experience / Featured / skills) · application kit (cover-letter template with 3 variants, 4 STAR stories, 30-second pitch) · keep the long profile as the dossier with the Mermaid swapped for a table.
6. **Export** PDF/DOCX of the résumé and dossier.

Decisions I need from you before step 4: (a) confirm "mine, not partner's" wording and removing ReactTSApp; (b) what the "2.5 years" rests on; (c) OK to apply the fixes in one sweep without asking per file.