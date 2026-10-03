#!/usr/bin/env bash
# Check that a symbol exists in the iOS 27.1 SDK and show its availability.
# Usage: find-api.sh <symbol>   e.g. find-api.sh onHingeChange
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; source "$here/_xcode.sh"
sym="${1:?usage: find-api.sh <symbol>}"
export DEVELOPER_DIR="$(find_developer_dir)"
sdk="$(xcrun --sdk iphoneos --show-sdk-path)"
found=0
for fw in UIKit SwiftUI SwiftUICore AVFoundation AVKit; do
  root="$sdk/System/Library/Frameworks/$fw.framework"
  for f in $(find "$root" \( -name "arm64e-apple-ios.swiftinterface" -o -name "*.h" \) 2>/dev/null); do
    if grep -q -- "$sym" "$f"; then
      found=1
      echo "== $fw: ${f#$root/}"
      grep -n -B4 -- "$sym" "$f" | grep -E "available|$sym" | grep -vE "^\s*[0-9]+-\s*//" | sed 's/SwiftUICore:://g; s/Swift:://g' | head -12
    fi
  done
done
[ $found -eq 1 ] || { echo "not found in the iOS SDK: $sym. Do not use it."; exit 1; }
