#!/usr/bin/env bash
# Read-only facts about the project and the toolchain. Usage: preflight.sh <project-dir>
set -uo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; source "$here/_xcode.sh"
dir="$(cd "${1:?usage: preflight.sh <project-dir>}" && pwd)"

echo "## Toolchain"
if dev="$(find_developer_dir)"; then
  export DEVELOPER_DIR="$dev"
  echo "xcode: $(xcodebuild -version | tr '\n' ' ')"
  echo "developer_dir: $dev"
  echo "ios_simulator_sdk: $(xcrun --sdk iphonesimulator --show-sdk-version)"
  duo=$(xcrun simctl list devices available | grep -m1 "iPhone Duo" || true)
  echo "duo_simulator: ${duo:-none (sim-capture.sh creates one)}"
  res="$dev/../PlugIns/IDEIntelligenceChat.framework/Versions/A/Resources"
  if ls "$res"/app-resizability-ref-*.md.packaged > /dev/null 2>&1; then
    echo "apple_app_resizability: yes"
    for f in "$res"/app-resizability-ref-*.md.packaged; do echo "  $(cd "$(dirname "$f")" && pwd)/$(basename "$f")"; done
  else
    echo "apple_app_resizability: no (use references/resizability.md)"
  fi
else
  echo "BLOCKER: no Xcode with the iOS 27.1 SDK"
fi

echo; echo "## Project"
container="$(find_container "$dir" 2>/dev/null || true)"
echo "container: ${container:-none}"
if [ -n "$container" ]; then
  echo "scheme: $(find_scheme "$container")"
fi
for p in $(find "$dir" -name project.pbxproj -not -path "*/Pods/*" -not -path "*/.build/*" 2>/dev/null); do
  echo "deployment_targets ($(basename "$(dirname "$p")")): $(grep -o "IPHONEOS_DEPLOYMENT_TARGET = [0-9.]*" "$p" | sort -u | sed 's/.*= //' | tr '\n' ' ')"
  grep -q "SUPPORTS_MACCATALYST = YES" "$p" && echo "mac_catalyst: yes (27.1 APIs need #if !targetEnvironment(macCatalyst) where unavailable)"
done
code_files=$(find "$dir" \( -name "*.swift" -o -name "*.m" \) -not -path "*/Pods/*" -not -path "*/.build/*" -not -path "*/DerivedData/*" 2>/dev/null)
count() { [ -z "$code_files" ] && { echo 0; return; }; echo "$code_files" | tr '\n' '\0' | xargs -0 grep -l -E "$1" 2>/dev/null | wc -l | tr -d ' '; }
echo "files_importing_SwiftUI: $(count '^import SwiftUI')"
echo "files_importing_UIKit: $(count '^import UIKit|#import <UIKit')"
echo "swiftui_app_lifecycle: $([ "$(count '@main[[:space:]]+struct[[:space:]]+[A-Za-z0-9_]+[[:space:]]*:[[:space:]]*App')" -gt 0 ] && echo yes || echo no)"
echo "scene_delegate: $([ "$(count 'UIWindowSceneDelegate')" -gt 0 ] && echo yes || echo no)"
echo "camera_capture: $([ "$(count 'AVCaptureSession')" -gt 0 ] && echo yes || echo no)"
echo "storyboards: $(find "$dir" \( -name "*.storyboard" -o -name "*.xib" \) -not -path "*/Pods/*" 2>/dev/null | wc -l | tr -d ' ')"

echo; echo "## Info.plist keys"
for p in $(find "$dir" -name "Info.plist" -not -path "*/Pods/*" -not -path "*/.build/*" -not -path "*.app/*" -not -path "*/DerivedData/*" 2>/dev/null); do
  echo "$p:"
  for k in UIApplicationSceneManifest UIRequiresFullScreen UIRequiresFullScreenIgnoredStartingWithVersion UILaunchScreen UILaunchStoryboardName UISupportedInterfaceOrientations; do
    v=$(/usr/libexec/PlistBuddy -c "Print :$k" "$p" 2>/dev/null | tr '\n' ' ' | sed 's/  */ /g')
    [ -n "$v" ] && echo "  $k: $v"
  done
done
grep -h -o "INFOPLIST_KEY_[A-Za-z_~]* = [^;]*" $(find "$dir" -name project.pbxproj -not -path "*/Pods/*" 2>/dev/null) 2>/dev/null | sort -u | grep -E "Scene|FullScreen|Launch|Orientation" | sed 's/^/  build setting: /'
exit 0
