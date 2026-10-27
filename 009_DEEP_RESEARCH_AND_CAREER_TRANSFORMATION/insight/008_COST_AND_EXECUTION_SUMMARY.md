# OpenRouter Deep Research Execution & Cost Summary

> **Run ID:** `OR-DR-20261027-020520`  
> **Executed At:** 2026-10-27 02:08:25 UTC  
> **Protocol:** 6-Phase OpenRouter Deep Research (`_1050_openrouter_deep_research.md`)  
> **Astra Final Verdict:** **PASS** (100% Executive Approval)

---

## 1. Multi-Model Pipeline Telemetry

| Phase | Model | Provider | Prompt Tokens | Completion Tokens | Total Cost (USD) | Latency | Status |
|---|---|---|---|---|---|---|---|
| Phase 1 - Planning | `deepseek/deepseek-v4.1-flash-1017` | Relace | 928 | 2,500 | $0.001315 | 1.47s | ✅ COMPLETED |
| Phase 2 - Extraction (Ling) | `inclusionai/ling-3.1-flash` | DeepInfra | 2,593 | 3,000 | $0.000869 | 0.69s | ✅ COMPLETED |
| Phase 3 - Synthesis (DeepSeek) | `deepseek/deepseek-v4.1-flash-1017` | Wafer | 1,178 | 3,000 | $0.001653 | 1.19s | ✅ COMPLETED |
| Phase 4 - Drafting (GLM) | `z-ai/glm-5.3-flash` | Together | 857 | 3,000 | $0.001629 | 2.49s | ✅ COMPLETED |
| Phase 5 - Validation (DeepSeek) | `deepseek/deepseek-v4.1-flash-1017` | Wafer | 829 | 2,500 | $0.001358 | 1.33s | ✅ COMPLETED |
| Phase 6 - Final Review (Astra) | `openai/gpt-6-astra` | OpenAI | 286 | 1,099 | $0.057810 | 1.11s | ✅ COMPLETED |

---

## 2. Aggregate Run Metrics

- **Total Prompt Tokens Ingested:** 6,671 tokens
- **Total Completion Tokens Generated:** 15,099 tokens
- **Total OpenRouter Model Invocations:** 6 API calls
- **Total Spend (USD):** **$0.064634**
- **Ling Empirical Extraction Status:** Verified (DeepInfra)
- **OpenAI GPT-6 Astra Final Status:** Verified (OpenAI)

---

## 3. Artifact Receipts

All primary model responses and evidence ledgers are permanently stored:
- Phase 1 Plan: `processed/006_RESEARCH_PLAN.md`
- Phase 2 Extraction: `processed/008_EVIDENCE_LEDGER.jsonl` (Ling 3.1 Flash)
- Phase 3 Analysis: `processed/009_ANALYSIS.md` (DeepSeek)
- Phase 4 Executive Draft: `processed/010_EXECUTIVE_DRAFT.md` (GLM 5.3 Flash)
- Phase 5 Audit: `processed/011_VALIDATION.md` (DeepSeek)
- Phase 6 Authoritative Review: `processed/012_ASTRA_REVIEW.md` (OpenAI GPT-6 Astra)
- Token & Cost Receipts: `processed/013_USAGE_LEDGER.jsonl`
