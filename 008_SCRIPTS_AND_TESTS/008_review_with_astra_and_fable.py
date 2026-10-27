import os
import urllib.request
import json

api_key = os.environ.get("OPENROUTER_API_KEY")

cv_path = r"c:\AI_PROJECTS\04_6TH_SENSE_PRODUCT_DEVELOPMENT\0211_AMIT_RESUME\009_DEEP_RESEARCH_AND_CAREER_TRANSFORMATION\002_AMIT_MALHOTRA_ENHANCED_ATS_CV.md"
linkedin_path = r"c:\AI_PROJECTS\04_6TH_SENSE_PRODUCT_DEVELOPMENT\0211_AMIT_RESUME\009_DEEP_RESEARCH_AND_CAREER_TRANSFORMATION\004_AMIT_MALHOTRA_ENHANCED_LINKEDIN_PROFILE.md"

with open(cv_path, "r", encoding="utf-8") as f:
    cv_content = f.read()

with open(linkedin_path, "r", encoding="utf-8") as f:
    linkedin_content = f.read()

models = [
    ("openai/gpt-6-astra", "Astra (GPT-6)"),
    ("anthropic/claude-fable-5.1", "Fable 5.1 (Claude)")
]

review_prompt = f"""You are a ruthless, world-class executive resume writer and Silicon Valley technical hiring director evaluating a candidate for Staff AI Systems Engineer and Forward Deployed AI Architect roles.

Please review the following CV and LinkedIn Profile for Amit Malhotra.

=== CANDIDATE ATS CV ===
{cv_content}

=== CANDIDATE LINKEDIN PROFILE ===
{linkedin_content}

CRITICAL REVIEW INSTRUCTIONS:
1. Tone & Language Audit: Is the language natural, human, and executive-level, or is it robotic, repetitive, overly jargon-dense, or synthetic AI-generated soup? Give brutal, specific examples of awkward or unnatural phrasing.
2. Logical Flow & Coherence: Does the narrative make logical sense? Does an executive or recruiter reading this understand who he is and what he actually delivered, or does it sound disjointed?
3. Actionable Corrections: Give specific, direct recommendations and line-by-line rewrites of the weakest sections (Headline, Summary, Experience bullets) so they read with high clarity, impact, natural authority, and genuine credibility.
"""

output_dir = r"c:\AI_PROJECTS\04_6TH_SENSE_PRODUCT_DEVELOPMENT\0211_AMIT_RESUME\009_DEEP_RESEARCH_AND_CAREER_TRANSFORMATION\processed"

for model_id, model_name in models:
    print(f"\nSending review request to {model_name} ({model_id})...")
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": review_prompt}],
        "max_tokens": 4000,
        "temperature": 0.3
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/amit-malhotra1",
            "X-Title": "Executive Resume Review"
        },
        data=json.dumps(payload).encode("utf-8")
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            choice = res["choices"][0]
            msg = choice["message"]
            content = msg.get("content") or msg.get("reasoning") or ""
            provider = res.get("provider", "unknown")
            usage = res.get("usage", {})
            cost = usage.get("cost", 0.0)
            print(f"SUCCESS: Received review from {model_name} via {provider} (cost=${cost:.4f})")
            
            clean_name = "ASTRA" if "astra" in model_id.lower() else "FABLE_5_1"
            out_file = os.path.join(output_dir, f"016_REVIEW_{clean_name}.md")
            with open(out_file, "w", encoding="utf-8") as out_fp:
                out_fp.write(f"# Executive Review: {model_name}\n\n**Model:** `{model_id}` ({provider})\n\n---\n\n{content}\n")
            print(f"Saved to {out_file}")
    except Exception as e:
        print(f"ERROR querying {model_name}: {e}")
