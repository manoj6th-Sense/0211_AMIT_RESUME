import glob
import re
import sys

banned_patterns = [
    r'AMX Plan',
    r'\bAMX\b',
    r'\bn8n\b',
    r'prompt engineer',
    r'bypass(es|ing)? bot',
    r'\bsandbox\b',
    r'high\.availability',
    r'all three agents',
    r'(make|made|making) [a-z0-9 ]{0,30}(repos?|repositor(y|ies)) public',
    r'(repos?|repositor(y|ies)) (go|goes|went) public'
]

rule_line_regex = re.compile(r'(not "|not just|say "|say \*\*|never "|instead of "|do not claim|Strictly Avoid|Avoided Term)', re.IGNORECASE)

files = glob.glob('009_DEEP_RESEARCH_AND_CAREER_TRANSFORMATION/*.md')
print(f'Checking {len(files)} files in 009_DEEP_RESEARCH_AND_CAREER_TRANSFORMATION...')

failures = 0
for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for i, line in enumerate(lines, 1):
        if rule_line_regex.search(line):
            continue
        for pat in banned_patterns:
            if re.search(pat, line, re.IGNORECASE):
                print(f'FAILED: {f}:{i} matched pattern /{pat}/ -> {line.strip()}')
                failures += 1

# Check LinkedIn limits
linkedin_file = '009_DEEP_RESEARCH_AND_CAREER_TRANSFORMATION/004_AMIT_MALHOTRA_ENHANCED_LINKEDIN_PROFILE.md'
with open(linkedin_file, 'r', encoding='utf-8') as fp:
    content = fp.read()

# Headline
hl_match = re.search(r'## HEADLINE\s*\n\s*\*\*(.*?)\*\*', content, re.DOTALL)
if hl_match:
    headline = hl_match.group(1).replace('\n', ' ').strip()
    hl_len = len(headline)
    print(f'LinkedIn Headline length: {hl_len} characters (limit <= 220)')
    if hl_len > 220:
        print(f'FAILED: Headline exceeds 220 chars!')
        failures += 1
else:
    print('FAILED: Could not find headline')
    failures += 1

# About
ab_match = re.search(r'## ABOUT\s*\n(.*?)\n---', content, re.DOTALL)
if ab_match:
    about = ab_match.group(1).strip()
    ab_len = len(about)
    print(f'LinkedIn About length: {ab_len} characters (limit <= 2600)')
    if ab_len > 2600:
        print(f'FAILED: About exceeds 2600 chars!')
        failures += 1
else:
    print('FAILED: Could not find About section')
    failures += 1

if failures == 0:
    print('SUCCESS: All 009 deliverables passed 100% of quality & compliance tests!')
    sys.exit(0)
else:
    print(f'FAILURES: {failures} check(s) failed.')
    sys.exit(1)
