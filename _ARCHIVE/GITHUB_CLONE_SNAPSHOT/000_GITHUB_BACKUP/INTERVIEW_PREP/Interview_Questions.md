# Interview Questions Based on Amit Malhotra's Resume

**Prepared For:** Interview Preparation  
**Based On:** Complete career history and AI portfolio

---

## SECTION 1: CREDIT RISK & MOODY'S EXPERIENCE

### Q1: Walk me through a PD model implementation you led.
**What they're really asking:** Do you understand the end-to-end process, or did you just watch?

**Expected Answer:**
At PNC, I implemented Wholesale PD models for 4 portfolios: Small Business, FI Insurance, CRE, and another. The process started with raw data inputs — borrower financials, external ratings, collateral data. From there:

1. **Ratio calculation** — transformed raw financials into credit ratios (debt service coverage, leverage, liquidity)
2. **Score calculation** — mapped ratios to quantitative scores, added qualitative overlays
3. **Rating assignment** — combined scores into a single rating
4. **PD mapping** — converted rating to probability of default

I built standalone T-SQL prototypes that ran this entire flow, not just Excel. The prototypes served three purposes: Credit Appraisal (real-time decisions), Regulatory Capital (Basel calculations), and Stress Testing (CCAR scenarios).

**Follow-up they might ask:** What was the hardest part?

**Answer:** Financial spreading on Pega. Pega didn't have out-of-box financial spreading, so we had to build ratio calculation logic from scratch. That meant defining every ratio formula, handling edge cases (what if denominator is zero?), and testing against the Excel prototypes.

---

### Q2: Explain Basel II IRB approach.
**What they're really asking:** Do you understand the regulatory framework, not just the acronym?

**Expected Answer:**
Basel II Internal Ratings Based (IRB) approach lets banks use their own models to calculate credit risk capital requirements. There are two flavors:

- **Foundation IRB:** Bank estimates PD, regulator provides LGD and EAD
- **Advanced IRB:** Bank estimates everything — PD, LGD, EAD

The math boils down to: **Risk Weight = f(PD, LGD, Maturity, Correlation)**

The risk weight gets applied to exposure to calculate Risk-Weighted Assets (RWA), which drives capital requirements.

What I actually worked on: implementing the PD estimation piece. The models I built calculated obligor-level PDs that fed into the RWA calculation done by downstream systems.

---

### Q3: What's the difference between CCAR and Basel?
**What they're really asking:** Can you distinguish regulatory frameworks?

**Expected Answer:**
- **Basel II/III** = International capital standards. Defines how much capital banks need based on risk-weighted assets. It's a minimum floor.

- **CCAR** = US-specific stress test. The Fed asks: "If the economy tanks (Severely Adverse scenario), do you have enough capital?" Banks have to prove they'd survive with models and data.

The connection: Basel gives you the RWA formula. CCAR makes you project RWA forward under stress and show you won't breach capital minimums.

At Santander, I worked on the CCAR side — RWA forecasting under stress scenarios. At Synovus, I built infrastructure that served both Basel reporting and CCAR stress testing.

---

### Q4: What is Dual Risk Rating?
**What they're really asking:** Do you understand obligor vs. facility concepts?

**Expected Answer:**
Dual Risk Rating separates two things:

1. **Obligor Rating** — How likely is this borrower to default? (PD)
2. **Facility Rating** — If they default, how much will I lose on this specific loan? (LGD)

The same borrower can have multiple loans with different collateral, so each facility gets its own LGD rating even though they share the same PD.

At Synovus, I designed a Dual Risk Rating data warehouse that captured both and synced with their multi-collateral system. The tricky part was loans with multiple pieces of collateral — you need to properly allocate collateral values across facilities.

---

## SECTION 2: PROJECT MANAGEMENT & BA SKILLS

### Q5: How do you translate business requirements into technical specs?
**What they're really asking:** Can you be the bridge between business and IT?

**Expected Answer:**
My process:
1. **Discovery** — Meet with business, understand the "why," document BRD
2. **Prototype** — Build a working model (Excel or SQL) so business can see the logic
3. **FRD** — Translate to technical specs: data sources, transformations, outputs
4. **Validation** — Run test cases through prototype and target system, compare results

At PNC, the Excel prototypes weren't just documentation — they were executable. Business could put in test data and see the outputs. When we found discrepancies between the prototype and the Pega implementation, we knew exactly where the logic diverged.

---

### Q6: Describe a difficult stakeholder situation.
**What they're really asking:** Can you handle conflict?

**Expected Answer:**
At PNC, the Strategy Testing team was implementing ratio calculation logic in Pega, but Pega didn't have out-of-box financial spreading. They wanted to simplify the logic; I knew simplification would break edge cases.

I built a side-by-side comparison: their simplified version vs. my prototype, with 50 test cases covering normal and edge scenarios. Seven cases failed. That data convinced them to implement the full logic.

The lesson: don't argue, prove. Show the failure cases.

---

### Q7: How do you manage a SIT team?
**What they're really asking:** Have you actually led testing, or just participated?

**Expected Answer:**
At PNC, I managed the System Integration Testing team. My responsibilities:
- Help them understand system-specific requirements (what the model is supposed to do)
- Defect detection process — when results don't match, how do we find the bug?
- Root cause analysis — is it data, logic, or configuration?
- QC on deliverables — before they sign off, I review their work

The key is having a reliable source of truth. My Model Implementation Accuracy Testing platform served that role — we could compare any output against the expected result and immediately see where it broke.

---

## SECTION 3: AI SYSTEMS & INSTRUCTION DESIGN

### Q8: What is "modular instruction design" and why does it matter?
**What they're really asking:** Is this a real discipline or just typing into ChatGPT?

**Expected Answer:**
Modular instruction design treats an LLM's instruction set like code: small components, explicit structure, versioning and tests, so the model produces reliable, consistent, useful outputs. It matters because:

1. **LLMs are stochastic** — same input can produce different outputs
2. **Context is limited** — you can't give the model unlimited information
3. **Behavior drifts** — models forget instructions in long conversations

My work addresses all three. The CURSOR system has token thresholds (60k/70k) that trigger saves before context degrades. The AI CEO prompt uses a structured format (XML/CSV) so the model can't misinterpret. The RPIV cycle forces the model through explicit phases rather than letting it wander.

---

### Q9: Explain your "Motherboard + Cartridge" architecture.
**What they're really asking:** What makes your AI work unique?

**Expected Answer:**
Think of a game console. The Motherboard is the system logic — how to format responses, what rules to follow, what checks to run. The Cartridge is the user's identity — their preferences, cognitive patterns, knowledge, and hard-won lessons.

In my AI CEO system:
- **Motherboard** = Execution protocols, HUD format, pre-flight mandates
- **Cartridge** = User BIOS (ADHD, flow state, triggers), embedded Knowledge Base

The innovation is separation of concerns. I can swap cartridges without rebuilding the motherboard. Different users, same system. Different use cases, same user.

The practical benefit: zero warm-up time. The AI knows me from the first word because my entire identity is loaded upfront.

---

### Q10: What is the "Verification Mandate" in CURSOR?
**What they're really asking:** How do you ensure AI code quality?

**Expected Answer:**
Every code output in CURSOR v5.3 must include explicit test steps. Not "run your tests" — actual steps like:

```
🧪 Verification Steps:
1. Run: npm test
2. Expected: All 47 tests pass
3. If fails: Check lines 23-25 for null handling
```

Why? Because AI-generated code that you can't verify is dangerous. The Verification Mandate forces the model to think about testability as it writes code, not as an afterthought.

---

### Q11: How does SmartBrain's persona switching work?
**What they're really asking:** Is this clever or gimmicky?

**Expected Answer:**
It's keyword-triggered, not command-triggered. In most Alexa skills, you'd say "Alexa, open Doctor skill, then ask about headaches." In SmartBrain, you just say "doc, I have a headache" — mid-conversation, no special syntax.

The implementation: I scan user input for trigger keywords. "doc" or "doctor" activates the Doctor persona. "funny" or "joker" activates the Joker. The personas are JSON-defined with their own system prompts and generation parameters (TopP, TopK).

The technical breakthrough was V4 session memory. Before that, the Doctor would forget symptoms within the same conversation. Now it maintains 4-turn recall — enough for a coherent medical Q&A.

---

### Q12: Why build a local AI stack (Ollama Powerhouse)?
**What they're really asking:** Why not just use ChatGPT?

**Expected Answer:**
Three reasons:

1. **Privacy** — Some prompts contain sensitive business logic. I don't want them on OpenAI's servers.
2. **Cost** — Running 1000s of test prompts during development is expensive on API. Local is free after hardware.
3. **Control** — I can run the exact model version I want, with the exact parameters. No surprise updates.

The dual-machine architecture was the key insight. My old 2013 laptop runs Open WebUI 24/7 — it's just a frontend, uses no GPU. When I need inference, my M1 Max wakes up via Tailscale. Best of both: always-on UI, on-demand compute.

---

## SECTION 4: LEADERSHIP & SOFT SKILLS

### Q13: How do you handle working with ADHD?
**What they're really asking:** Are you going to be reliable?

**Expected Answer:**
Yes — because I've built systems to manage it.

"Out of sight, out of mind" is real for me. So my AI systems have always-visible HUDs. Token counts, session health, momentum status — all displayed constantly.

Frustration derails focus. So my systems detect frustration (through profanity flags, for example) and auto-save before I lose work.

Flow state is fragile. So my systems minimize "meta-work" — I shouldn't be debugging the AI, I should be working with it.

These aren't just nice-to-haves. They're survival mechanisms I've codified. And they make the systems better for everyone, not just me.

---

### Q14: Why leave Moody's?
**What they're really asking:** Were you fired, or is there a good reason?

**Expected Answer:**
I left to build. At Moody's, I was implementing other people's models in other people's systems. After 6 years, I knew credit risk deeply enough to create — not just deploy.

My consulting firm let me work with multiple banks (PNC, Santander, Synovus) and see how different organizations approach the same problems. That breadth made me a better architect.

The AI pivot in 2023 was the natural next step. I'd been building tools for myself for years — the prompt systems, the knowledge bases. Eventually I realized they were products, not just utilities.

---

### Q15: Where do you see yourself in 5 years?
**What they're really asking:** Are you going to leave quickly?

**Expected Answer:**
Building AI products that ship.

I've spent 20 years in enterprise software — first building other people's systems, then consulting, now building my own. The pattern is clear: I move toward more ownership and more creation.

In 5 years, I want to be leading an AI product team — either at a company that shares my values around human-centric AI, or continuing to build AMTrix products if they gain traction.

What I'm not interested in: going back to pure consulting where I implement and leave. I want to see things through.

---

## PART 2 — FORWARD DEPLOYED ENGINEER QUESTIONS (Added 2026-10-25)

### Q16: Walk me through the most complex system you've built.
**What they're really asking:** Can you go deep and explain architecture clearly?

**Expected Answer (Claude Code Center):**
A local gateway between the Claude Code agent and every model provider. The agent speaks Anthropic's Messages format. My proxy:
- translates that into Vertex AI, Bedrock, OpenRouter or Ollama formats;
- handles Google service-account OAuth with token caching;
- injects 1-hour prompt caching;
- rebuilds streamed tool-call fragments so the agent's tool loop works on Gemini and other models;
- meters every request on a cost HUD.

The hardest bug was a silent "no endpoints found" from OpenRouter. It came down to provider-key casing in the routing config, and it taught me to always verify end to end with real calls.

---

### Q17: How do you stop an AI agent from hallucinating or destroying work?
**What they're really asking:** Do you understand agent failure modes in production?

**Expected Answer (AMTrix Plan):**
You don't fix it with wording. You fix it with process enforced by code:
- Hooks back up every file before its first edit.
- Plans need human approval and are locked once seen.
- Test counts and timings are written by the finish script, never typed by the model.
- Scope guards block edits outside the allowed paths.
- A pre-commit hook refuses secrets.

The agent is treated like a talented but untrusted junior engineer.

---

### Q18: What is context engineering, and what have you learned about it?
**What they're really asking:** Do you know what's beyond prompts?

**Expected Answer:**
I built it seven ways: modular instruction files, on-disk memory vaults, compression, request-level routing with payload capture, compiled context handoffs, my own gateway, and finally governance by hooks. The lesson: what a tool actually **sends** matters more than what you **tell** it. Own the request layer, keep memory on disk, pass paths instead of contents, and remove redundancy instead of summarizing.

---

### Q19: A client has rolled out coding agents to 300 developers. Costs are up and quality is uneven. What do you do in the first 30 days?
**What they're really asking:** Can you act as a forward-deployed engineer?

**Expected Answer:**
- **Week 1:** Shadow developers and capture real traffic: what gets sent, cache hit rates, where sessions fail.
- **Week 2:** Put a gateway in front of the agents for routing, caching and per-team cost attribution.
- **Week 3:** Pilot a governance standard in 2–3 repos: resume, backups, approval gates, measured tests.
- **Week 4:** Measure before and after (spend, rework, incidents), then roll out with a one-command installer.

---

### Q20: Why would you run models locally?
**Expected Answer:**
Privacy, cost and evaluation. On my 64 GB Apple Silicon machine I run 30B mixture-of-experts models with 128K+ context through Ollama, behind my own Open WebUI assistant with private search. It's the $0 tier in my gateway and lets me test a model before spending on cloud. For clients with sensitive data, it's often the only option.

---

### Q21: How do you make LLM output reliable for calculations?
**Expected Answer:**
Compute, then narrate. In my ephemeris and scoring engine, every calculation (high-precision astronomy, coordinate transforms, weighted scoring matrices) happens in tested Python. The LLM receives strictly schema-validated evidence and only interprets it. The same pattern works for credit scoring or actuarial rating: the model should never be the one doing the math.

---

### Q22: How do your tools fit together?
**Expected Answer:**
They are built as Lego pieces:
- My protocol template is installed in every active project.
- The Frontier Triage Engine started inside AMTrix Plan, became standalone, and is now embedded in my MCP server.
- The local Ollama tier feeds the gateway, Studio and my coding assistant.

While building any one tool, I'm already thinking about how it plugs into the others. Lightweight, portable, plug-and-play.

---

*Document prepared for interview preparation — not for distribution*
