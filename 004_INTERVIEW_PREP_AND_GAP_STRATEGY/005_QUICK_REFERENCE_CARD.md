# Quick Reference Card — Interview Day
> 🕒 Last changed: v0.1.1 · 26-10-25__14.33.21
> 🗓️ Created: 26-10-25__14.33.21
> **Document Version:** v1.0  
> **Last Modified:** 2026-10-27 00:00 UTC+4  
> **Status:** Baseline
<!-- Updated 2026-10-25: FDE positioning -->

**Print this. Carry it.**

---

## Your Headline
> Forward Deployed AI Engineer | Agent Reliability, LLM Gateways, Private AI & MCP | Ex-Moody's Analytics | 21+ Years

---

## Your 20-Second Pitch
> "I build the harness that makes AI agents dependable. They resume where they stopped, can't silently destroy work, prove what they did, and cost less. I've lived these failure modes across 20+ shipped systems and fixed each one in code. Before that, I spent 15 years validating credit-risk models for banks, so I build with audit trails by default."

---

## Your 4 Proof Points (pick one per question)

| Proof | One-liner |
|---|---|
| **Claude Code Center** | "My own gateway runs Claude Code on Vertex AI, including Kimi K2 and DeepSeek, plus Bedrock, OpenRouter or local models, with caching and tool calling and no subscription." |
| **AMTrix Plan** | "A folder you drop into any repo. Every agent then resumes, backs up before editing, waits for approval and proves its work. 365 commits in 22 days." |
| **Private AI Platform** | "30B models with 128K+ context on my 64 GB Mac through Ollama, my own Open WebUI assistant, and private search." |
| **Universal MCP Server** | "The IDE passes file paths, not file contents. The server does deep multi-model analysis and continues automatically when output is truncated." |

---

## The 2018–Present Tech & AI Systems Story (30 Seconds)
> "From 2018 onward at AKM USA TRADING INC (C-Corp), I served as Technology Lead & Systems Architect, engineering real-time data ingestion pipelines, automated trading signal execution interfaces, and conversational task automation bots. In April 2022, I founded AMTrix Solutions Inc. (C-Corp) to develop dedicated software and Generative AI systems full-time. Trading operations and market execution reinforced my risk-first architecture: deterministic validation, strict approval gates, and real-time execution safety."

---

## The "AI-Generated" Defense (20 Seconds)
> "I use AI agents as implementation partners, and that's exactly why I built the governance around them. The architecture decisions are mine: pass-by-path MCP, compute-then-narrate, priority lookup policies, owning the gateway. I can walk you through why each earlier approach failed."

---

## Your Biggest Strength
**I turn failures into code.** Every mistake goes into a friction log, becomes a rule, and the rule is enforced by hooks and tests.

---

## 5 Things to Say If You Blank

1. "Measured, not claimed: test counts are written by code, never typed by the model."
2. "I built context engineering seven ways. Owning the proxy won."
3. "Compute, then narrate: the LLM never does the math."
4. "Lightweight, portable, plug-and-play. My protocol template runs in every active project."
5. "Moody's taught me model validation; now I validate agents."

---

## Technical Vocab (If They Test You)

| Term | Meaning |
|------|---------|
| Prompt caching (1h TTL) | Provider stores a prompt prefix; repeat reads cost far less |
| `rawPredict` | Vertex AI endpoint used for Claude on Vertex |
| Vertex MaaS | Third-party models (Kimi K2, DeepSeek) served by Vertex |
| SSE accumulator | Rebuilds streamed tool-call fragments into one tool block |
| MCP | Model Context Protocol: standard way to give agents tools |
| Pass-by-path | Send file paths, not contents; the server reads from disk |
| GGUF / Q5_K_M | Quantized local-model format / quantization level |
| MoE (30B-A3B) | Mixture of experts: 30B total, ~3B active per token |
| finish_reason=length | The model was truncated; treat the output as PARTIAL |

## Credit Risk Vocab (If They Test You)

| Term | Meaning |
|------|---------|
| PD / LGD / EAD | Probability of Default / Loss Given Default / Exposure at Default |
| RWA | Risk-Weighted Assets |
| CCAR | Fed stress test |
| FR Y-14 | The CCAR reporting forms |
| Dual Risk Rating | Obligor + facility rated separately |

---

## Calm-Down Phrase
*"The truth is my friend. I just need to frame it right."*

---

*Good luck. You built this. You know it.*