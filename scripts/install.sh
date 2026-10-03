#!/usr/bin/env bash
# Install skills from this repo into Claude Code, Codex, and pi.
#
#   scripts/install.sh tdd bro      install named skills
#   scripts/install.sh --all        install every skill
#   scripts/install.sh --list       list available skills
#
# Set SKILL_TARGETS to override the target directories (space separated).

set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
targets=${SKILL_TARGETS:-"$HOME/.claude/skills $HOME/.codex/skills $HOME/.pi/skills"}

skills() { ls "$repo"/*/SKILL.md | xargs -n1 dirname | xargs -n1 basename; }

if [ $# -eq 0 ]; then
  sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
fi

case "$1" in
  --list) skills; exit 0 ;;
  --all) set -- $(skills) ;;
esac

for name in "$@"; do
  if [ ! -f "$repo/$name/SKILL.md" ]; then
    echo "No skill named '$name'. Run scripts/install.sh --list." >&2
    exit 1
  fi
done

for name in "$@"; do
  for dir in $targets; do
    mkdir -p "$dir"
    rm -rf "${dir:?}/$name"
    cp -R "$repo/$name" "$dir/$name"
    echo "installed $name -> $dir/$name"
  done
done
