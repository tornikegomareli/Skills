#!/usr/bin/env bash
# Build the app for the iOS 27.1 simulator SDK. Usage: build.sh <project-dir>
# Env: DUO_SCHEME (scheme), DUO_DEVELOPER_DIR (Xcode). Prints a short summary and the log path.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; source "$here/_xcode.sh"
dir="$(cd "${1:?usage: build.sh <project-dir>}" && pwd)"
export DEVELOPER_DIR="$(find_developer_dir)"
container="$(find_container "$dir")"
scheme="$(find_scheme "$container")"
[ -n "$scheme" ] || { echo "error: no scheme found; set DUO_SCHEME" >&2; exit 1; }
out="${TMPDIR:-/tmp}/duo-build/$(echo "$dir" | shasum | cut -c1-12)"
mkdir -p "$out"; log="$out/build.log"
echo "xcode: $(xcodebuild -version | head -1) ($DEVELOPER_DIR)"
echo "building: $scheme in $(basename "$container")"
set +e
xcodebuild $(container_flag "$container") "$container" -scheme "$scheme" -configuration Debug \
  -sdk iphonesimulator -destination "generic/platform=iOS Simulator" -derivedDataPath "$out/dd" \
  CODE_SIGNING_ALLOWED=NO build > "$log" 2>&1
status=$?
set -e
grep -E ": error: " "$log" | sort -u | head -20 || true
warnings=$( (grep -E ": warning: " "$log" || true) | sort -u | wc -l | tr -d ' ')
app=$(find "$out/dd/Build/Products" -maxdepth 2 -name "*.app" -type d 2>/dev/null | head -1 || true)
echo "warnings: $warnings (unique)"
echo "log: $log"
if [ -n "$app" ]; then echo "app: $app"; fi
if [ $status -eq 0 ]; then echo "BUILD SUCCEEDED"; else echo "BUILD FAILED"; fi
exit $status
