#!/bin/sh
# Preview what a git repository of this folder would share, under .gitignore.
# Run from anywhere: sh scripts/preview_share.sh
# Uses a throwaway git folder in the system temp directory; the project gets no .git.
# Prints every file that would be committed, then "SHARE_OK" or "SHARE_LEAK" and exits 1 on a leak.

cd "$(dirname "$0")/.." || exit 2

tmp=$(mktemp -d) || exit 2
trap 'rm -rf "$tmp"' EXIT
export GIT_DIR="$tmp/git" GIT_WORK_TREE="$PWD"
git init -q || exit 2

files=$(git ls-files --others --exclude-standard)
echo "$files"
echo "---"
echo "$(printf '%s\n' "$files" | grep -c .) files would be shared"

# The only roots a shared file may live under (keep in step with the "!" lines of .gitignore).
SHARED='^(\.gitignore|README\.md|PROJECT_INDEX\.md|(000_GITHUB_BACKUP|000_PROJECT_HISTORY|001_FINAL_RESUMES|002_STRATEGIC_PITCH|003_INTERVIEW_PREP|004_DATA_REFERENCES|005_SCRIPTS|006_TESTS)/.+)$'
# Never shared even under those roots: edit backups and system clutter.
CLUTTER='_v[0-9]+\.[0-9]+\.[0-9]+_[0-9]{2}-[0-9]{2}-[0-9]{2}__|\.DS_Store|__pycache__|\.pyc$'
bad_path=$(printf '%s\n' "$files" | grep -vE -- "$SHARED"; printf '%s\n' "$files" | grep -E -- "$CLUTTER")

# Secret-shaped strings inside a shared text file (bot token, Google key, OpenAI-style key, private key, GitHub token).
SECRET='[0-9]{8,10}:[A-Za-z0-9_-]{35}|AIza[0-9A-Za-z_-]{35}|sk-[A-Za-z0-9_-]{20,}|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{36}'
bad_text=""
for f in $files; do
  case "$f" in *.md|*.txt|*.py|*.html|*.json|*.xml|.gitignore) ;; *) continue ;; esac
  grep -qE -- "$SECRET" "$f" && bad_text="$bad_text $f"
done

if [ -z "$bad_path" ] && [ -z "$bad_text" ]; then
  echo "SHARE_OK only the shared folders and files; no backup, no secret-shaped string"
else
  [ -n "$bad_path" ] && echo "SHARE_LEAK path(s): $bad_path"
  [ -n "$bad_text" ] && echo "SHARE_LEAK secret-shaped string in:$bad_text"
  exit 1
fi
