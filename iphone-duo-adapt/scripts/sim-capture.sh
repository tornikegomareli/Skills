#!/usr/bin/env bash
# Build, install, launch on the iPhone Duo simulator, and screenshot each display.
# Usage: sim-capture.sh [--no-install] <project-dir> [label]
# Screenshots go to <project-dir>/duo-captures/<label>-display<N>.png.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; source "$here/_xcode.sh"
install=1
if [ "${1:-}" = "--no-install" ]; then install=0; shift; fi
dir="$(cd "${1:?usage: sim-capture.sh [--no-install] <project-dir> [label]}" && pwd)"
label="${2:-closed-portrait}"
export DEVELOPER_DIR="$(find_developer_dir)"

udid=$(xcrun simctl list devices available -j | python3 -c '
import json,sys
d=json.load(sys.stdin)["devices"]
for rt,devs in d.items():
    for x in devs:
        if x["name"].startswith("iPhone Duo"): print(x["udid"]); sys.exit()')
if [ -z "$udid" ]; then
  runtime=$(xcrun simctl list runtimes -j | python3 -c '
import json,sys
r=[x for x in json.load(sys.stdin)["runtimes"] if x["platform"]=="iOS" and x["isAvailable"]]
r=[x for x in r if tuple(int(v) for v in (x["version"].split(".")+["0"])[:2])>=(27,1)]
print(r[-1]["identifier"] if r else "")')
  [ -n "$runtime" ] || { echo "error: no iOS 27.1 simulator runtime. Install it in Xcode > Settings > Components." >&2; exit 1; }
  udid=$(xcrun simctl create "iPhone Duo" com.apple.CoreSimulator.SimDeviceType.iPhone-Duo "$runtime")
fi
xcrun simctl boot "$udid" 2>/dev/null || true
xcrun simctl bootstatus "$udid" -b > /dev/null

out="${TMPDIR:-/tmp}/duo-build/$(echo "$dir" | shasum | cut -c1-12)"
if [ $install -eq 1 ]; then
  "$here/build.sh" "$dir" | tail -3
  app=$(find "$out/dd/Build/Products" -maxdepth 2 -name "*.app" -type d | head -1)
  bundle=$(/usr/libexec/PlistBuddy -c "Print :CFBundleIdentifier" "$app/Info.plist")
  xcrun simctl install "$udid" "$app"
  xcrun simctl launch --terminate-running-process "$udid" "$bundle" > /dev/null
  echo "launched: $bundle"
  sleep 4
fi

mkdir -p "$dir/duo-captures"
n=0
for port in $(xcrun simctl io "$udid" enumerate | python3 -c '
import sys,re
blocks=sys.stdin.read().split("Port:")
for b in blocks:
    u=re.search(r"UUID:\s*(\S+)",b)
    if u and re.search(r"Display class:\s*0",b): print(u.group(1))'); do
  n=$((n+1))
  file="$dir/duo-captures/$label-display$n.png"
  xcrun simctl io "$udid" screenshot --display="$port" "$file" > /dev/null 2>&1 && echo "screenshot: $file"
done
[ $n -gt 0 ] || { echo "error: no internal displays found" >&2; exit 1; }
echo "device: $udid. The display that is off shows black. Fold poses: set them in Xcode's Device Hub, then run with --no-install."
