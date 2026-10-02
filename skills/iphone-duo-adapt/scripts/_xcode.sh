# Sourced by the other scripts. Sets DEVELOPER_DIR to an Xcode with the iOS 27.1+ simulator SDK.
# Never changes the global xcode-select. Override with DUO_DEVELOPER_DIR=<path>/Contents/Developer.

sdk_ok() { # $1 = developer dir
  local v
  v=$(DEVELOPER_DIR="$1" xcrun --sdk iphonesimulator --show-sdk-version 2>/dev/null) || return 1
  python3 -c "import sys; a=[int(x) for x in '$v'.split('.')]+[0]; sys.exit(0 if (a[0],a[1])>=(27,1) else 1)"
}

find_developer_dir() {
  local cand
  if [ -n "${DUO_DEVELOPER_DIR:-}" ]; then
    sdk_ok "$DUO_DEVELOPER_DIR" && { echo "$DUO_DEVELOPER_DIR"; return 0; }
    echo "error: DUO_DEVELOPER_DIR has no iOS 27.1 simulator SDK: $DUO_DEVELOPER_DIR" >&2; return 1
  fi
  cand=$(xcode-select -p 2>/dev/null)
  [ -n "$cand" ] && sdk_ok "$cand" && { echo "$cand"; return 0; }
  while IFS= read -r app; do
    [ -d "$app/Contents/Developer" ] && sdk_ok "$app/Contents/Developer" && { echo "$app/Contents/Developer"; return 0; }
  done < <(mdfind "kMDItemCFBundleIdentifier == 'com.apple.dt.Xcode'" 2>/dev/null; ls -d /Applications/Xcode*.app ~/Applications/Xcode*.app ~/Downloads/*[Xx]code*.app 2>/dev/null)
  echo "error: no Xcode with the iOS 27.1 simulator SDK found. Install Xcode 27.1 or set DUO_DEVELOPER_DIR." >&2
  return 1
}

# Prints the .xcworkspace or .xcodeproj to build, preferring a workspace that is not inside a project.
find_container() { # $1 = project dir
  local ws proj
  ws=$(find "$1" -maxdepth 3 -name "*.xcworkspace" -not -path "*.xcodeproj/*" -not -path "*/Pods/*" -not -path "*/.build/*" 2>/dev/null | head -1)
  [ -n "$ws" ] && { echo "$ws"; return 0; }
  proj=$(find "$1" -maxdepth 3 -name "*.xcodeproj" -not -path "*/Pods/*" -not -path "*/.build/*" 2>/dev/null | head -1)
  [ -n "$proj" ] && { echo "$proj"; return 0; }
  echo "error: no .xcworkspace or .xcodeproj under $1" >&2; return 1
}

container_flag() { case "$1" in *.xcworkspace) echo "-workspace";; *) echo "-project";; esac; }

# Prints the scheme to build: $DUO_SCHEME, else the first scheme that builds an app.
find_scheme() { # $1 = container
  if [ -n "${DUO_SCHEME:-}" ]; then echo "$DUO_SCHEME"; return 0; fi
  xcodebuild -list -json $(container_flag "$1") "$1" 2>/dev/null | python3 -c '
import json,sys
d=json.load(sys.stdin); c=d.get("workspace") or d.get("project") or {}
s=c.get("schemes",[]); t=c.get("targets",[])
pick=[x for x in s if x in t] or s
print(pick[0] if pick else "")'
}
