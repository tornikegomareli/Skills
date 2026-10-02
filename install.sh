#!/usr/bin/env bash
# Install skills from this repo into Claude Code, Codex, and pi.
#
#   ./install.sh tdd bro            install named skills
#   ./install.sh --all              install every skill
#   ./install.sh --list             list available skills
#
# Set SKILL_TARGETS to override the target directories (space separated).

set -euo pipefail

repo="$(cd "$(dirname "$0")" && pwd)"
targets=${SKILL_TARGETS:-"$HOME/.claude/skills $HOME/.codex/skills $HOME/.pi/skills"}

if [ $# -eq 0 ]; then
  sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
fi

case "$1" in
  --list) ls "$repo/skills"/*/SKILL.md | xargs -n1 dirname | xargs -n1 basename; exit 0 ;;
  --all) set -- $(ls "$repo/skills"/*/SKILL.md | xargs -n1 dirname | xargs -n1 basename) ;;
esac

for name in "$@"; do
  if [ ! -f "$repo/skills/$name/SKILL.md" ]; then
    echo "No skill named '$name'. Run ./install.sh --list." >&2
    exit 1
  fi
done

for name in "$@"; do
  for dir in $targets; do
    mkdir -p "$dir"
    rm -rf "${dir:?}/$name"
    cp -R "$repo/skills/$name" "$dir/$name"
    echo "installed $name -> $dir/$name"
  done
done
