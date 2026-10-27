import os
import urllib.request
import json

api_key = os.environ.get("OPENROUTER_API_KEY")

prompt = """You are a world-class executive career architect and elite Silicon Valley technical hiring director.

We are harmonizing the complete career dossier and portfolio for Amit Malhotra across all outward documents.

CRITICAL INVARIANTS:
1. TENURE: Amit has 21+ YEARS of continuous software systems, enterprise data platforms, and AI engineering (from 2005 to 2026).
   NEVER say "15 years" or "15+ years" as if his career was 15 years.
   His trajectory:
   - 2005–2007: Intelligent Search Technology (Software Developer, C/C++ fuzzy matching engine)
   - 2007–2013: Moody's Analytics (Assistant Director / Lead Systems Consultant, RiskAnalyst & RiskOrigin client implementations, CRD automation, Default Detection app in C#/.NET with RiskCalc EDF)
   - 2013–2017: Malhotra Enterprise Solutions LLC (Strategic Consulting: Synovus Bank Dual Risk Rating for 30+ banks; PNC Bank Wholesale PD SME across 4 portfolios; Santander Bank VP for CCAR stress testing & FR Y-14 via Copal Amba/Moody's)
   - 2018–Present: AKM USA TRADING INC (Technology Lead: real-time market data ingestion, algorithmic execution, conversational AI & voice/chat automation bots)
   - 2022–Present: AMTrix Solutions Inc. (Principal AI Systems Architect: multi-provider LLM gateways, streaming SSE tool translation, AMTrix Plan agent governance with 700+ tests, Vision-LLM desktop automation with 28.6K audited actions, FastMCP servers, local Apple Silicon inference).

2. PROJECTS MUST "WOW":
   Highlight his 6 flagship technical achievements with authentic, authoritative engineering precision:
   a. Multi-Provider LLM Gateway: unified Anthropic-compatible tool calling across Vertex AI, Bedrock, OpenRouter, and Ollama with streaming SSE chunk reassembly.
   b. AMTrix Plan Agent Reliability Harness: ~23K lines Python stdlib, 700+ tests, OS-level file write locks, pre-tool hooks protecting uncommitted files, mandatory test-passing gates.
   c. Vision-LLM Desktop Automation & Control Framework: 3-tier architecture (Perception -> Decision -> Verified Action), React coordinate zone builder, session token budgeting, 28,600+ audited actions across 270 live runs on legacy desktop GUIs without APIs.
   d. FastMCP Servers: 10 production tools for pass-by-path file retrieval, schema compaction, and reference-based storage.
   e. Private Apple Silicon Workstation: local Ollama GGUF inference over Tailscale.
   f. Enterprise Banking Architecture: Synovus Dual Risk Rating for 30+ banks, PNC Wholesale PD calculation engines, Santander CCAR FR Y-14 pipelines, Moody's CRD complete automation.

3. STRIP ALL ARTIFICIAL NOISE:
   - Zero "C-Corp" tags.
   - Zero "30B parameter models" (say "GGUF quantized models including Qwen and Llama architectures").
   - Zero document metadata wrappers ("Document Version", "100% Factually Verified").

Please provide a concise, razor-sharp review confirming the unified positioning narrative for:
1. Staff / Principal AI Systems Engineer
2. Forward Deployed AI Architect / Enterprise Solutions Director
3. Head of AI Platform
Give us the exact punchy, executive wording to use across all profile summaries.
"""

models = [
    ("openai/gpt-6-astra", "Astra (GPT-6)"),
    ("anthropic/claude-fable-5.1", "Fable 5.1 (Claude)")
]

for model_id, model_name in models:
    print(f"Querying {model_name} ({model_id})...")
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1500,
        "temperature": 0.2
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/amit-malhotra1",
            "X-Title": "Portfolio Harmonization Review"
        },
        data=json.dumps(payload).encode("utf-8")
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            content = res["choices"][0]["message"].get("content") or res["choices"][0]["message"].get("reasoning") or ""
            print(f"\n=== {model_name} Response ===\n{content}\n")
            out_file = f"009_DEEP_RESEARCH_AND_CAREER_TRANSFORMATION/processed/017_HARMONIZATION_{model_name[:5].upper()}.md"
            with open(out_file, "w", encoding="utf-8") as fp:
                fp.write(f"# Harmonization Review: {model_name}\n\n{content}\n")
    except Exception as e:
        print(f"Error querying {model_name}: {e}")
