#!/bin/sh
# The outward test: the checks code can make on the résumé set.
# Run from the project root: sh tests/check_outward.sh
# Each check prints one line, "ok" or "FAIL"; the last line is "N passed, M failed" (finish reads "N passed").

cd "$(dirname "$0")/.." || exit 2

OUTWARD="001_FINAL_RESUMES/*.md 003_INTERVIEW_PREP/*.md"
DOSSIER="001_FINAL_RESUMES/001_AMIT_MALHOTRA_FDE_PROFILE_2026.md"
RESUME="001_FINAL_RESUMES/002_AMIT_MALHOTRA_FDE_RESUME_2026_ATS.md"
LINKEDIN="001_FINAL_RESUMES/004_LINKEDIN_PROFILE.md"
EXPORTS="001_FINAL_RESUMES/007_EXPORTS"
BANNED="006_TESTS/001_banned_phrases.txt"
# A line that states a phrasing rule is allowed to name the phrase it bans.
RULE_LINE='(not "|not just|say "|say \*\*"|never "|instead of "|do not claim)'
HEADLINE_MAX=220
ABOUT_MAX=2600

passed=0
failed=0
ok()   { echo "ok   $1"; passed=$((passed + 1)); }
fail() { echo "FAIL $1"; failed=$((failed + 1)); }

# 1. No banned phrase in the outward files (the rule lines excepted).
if [ ! -f "$BANNED" ]; then
  fail "1 banned phrases: $BANNED is missing"
else
  hits=""
  while IFS= read -r pat; do
    case "$pat" in ''|'#'*) continue ;; esac
    # shellcheck disable=SC2086
    h=$(grep -niE -- "$pat" $OUTWARD 2>/dev/null | grep -viE -- "$RULE_LINE")
    [ -n "$h" ] && hits="$hits
$h"
  done < "$BANNED"
  if [ -z "$hits" ]; then
    ok "1 banned phrases: none in the outward files"
  else
    fail "1 banned phrases found:$hits"
  fi
fi

# 2. No Mermaid fence in the dossier (it must render in PDF and ATS parsers).
n=$(grep -c '```mermaid' "$DOSSIER" 2>/dev/null); n=${n:-0}
if [ "$n" = "0" ]; then ok "2 dossier: no Mermaid fence"; else fail "2 dossier: $n Mermaid fence(s)"; fi

# 3. LinkedIn headline and About within the platform limits.
headline=$(awk '/^## HEADLINE/{f=1;next} f&&/^\*\*/{print;exit}' "$LINKEDIN" | sed 's/^\*\*//; s/\*\*$//' | tr -d '\n')
hl=$(printf '%s' "$headline" | wc -m | tr -d ' ')
if [ -n "$headline" ] && [ "$hl" -le "$HEADLINE_MAX" ]; then
  ok "3a LinkedIn headline: $hl characters (limit $HEADLINE_MAX)"
else
  fail "3a LinkedIn headline: $hl characters (limit $HEADLINE_MAX) or not found"
fi
al=$(awk '/^## ABOUT/{f=1;next} f&&/^## /{exit} f&&/^---$/{exit} f' "$LINKEDIN" | sed '/./,$!d' | wc -m | tr -d ' ')
if [ "$al" -gt 0 ] && [ "$al" -le "$ABOUT_MAX" ]; then
  ok "3b LinkedIn About: $al characters (limit $ABOUT_MAX)"
else
  fail "3b LinkedIn About: $al characters (limit $ABOUT_MAX) or not found"
fi

# 4. The exports exist and are not empty.
missing=""
for f in 005_AMIT_MALHOTRA_FDE_RESUME_2026.pdf 003_AMIT_MALHOTRA_FDE_RESUME_2026.docx 004_AMIT_MALHOTRA_FDE_RESUME_2026.html \
         002_AMIT_MALHOTRA_FDE_PROFILE_2026.pdf 001_AMIT_MALHOTRA_FDE_PROFILE_2026.html; do
  [ -s "$EXPORTS/$f" ] || missing="$missing $f"
done
if [ -z "$missing" ]; then ok "4 exports: all five present"; else fail "4 exports missing or empty:$missing"; fi

# 5. The exports are not older than their Markdown sources.
stale=""
for pair in "$RESUME:005_AMIT_MALHOTRA_FDE_RESUME_2026.pdf" "$RESUME:003_AMIT_MALHOTRA_FDE_RESUME_2026.docx" \
            "$DOSSIER:002_AMIT_MALHOTRA_FDE_PROFILE_2026.pdf"; do
  src=${pair%%:*}; out=$EXPORTS/${pair#*:}
  if [ -f "$src" ] && [ -f "$out" ] && [ "$src" -nt "$out" ]; then stale="$stale ${pair#*:}"; fi
done
if [ -z "$stale" ]; then ok "5 exports: none older than its Markdown"; else fail "5 exports older than their Markdown (re-export):$stale"; fi

# 6. No secret-shaped string in the outward files (shapes only; no value is kept here).
# Bot token, Google API key, OpenAI-style key, a private key block, a GitHub token.
SECRET_SHAPES='[0-9]{8,10}:[A-Za-z0-9_-]{35}|AIza[0-9A-Za-z_-]{35}|sk-[A-Za-z0-9_-]{20,}|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{36}'
# shellcheck disable=SC2086
s=$(grep -nE -- "$SECRET_SHAPES" $OUTWARD 2>/dev/null | cut -d: -f1-2)
if [ -z "$s" ]; then ok "6 secrets: no secret-shaped string in the outward files"; else fail "6 secret-shaped string at (file:line, value not shown): $s"; fi

total=$((passed + failed))
echo "$passed passed, $failed failed ($total checks)"
[ "$failed" -eq 0 ]
