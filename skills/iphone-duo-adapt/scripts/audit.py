#!/usr/bin/env python3
"""Find iPhone Duo problem candidates in an iOS project.

Usage: audit.py <project-dir> [--json]

Prints one candidate per line: CHECK-ID<TAB>path:line<TAB>code.
A candidate is not a proven problem. Read the context before you record it.
Check IDs match references/checks.md.
"""
import json
import os
import plistlib
import re
import sys

SKIP_DIRS = {
    ".git", ".build", "build", "DerivedData", "Pods", "Carthage", "node_modules",
    ".swiftpm", "SourcePackages", "vendor", "fastlane",
}
CODE_EXT = {".swift", ".m", ".mm", ".h"}
UI_EXT = {".storyboard", ".xib"}
STRING_EXT = {".strings", ".xcstrings"}

# (check id, regex, file kinds). Line-based. Comment lines are skipped.
LINE_RULES = [
    ("R01", r"\bUIScreen\.main\b|\[UIScreen\s+mainScreen\]", "code"),
    ("R02", r"\binterfaceOrientation\b|\bstatusBarOrientation\b|UIDevice\.current\.orientation"
            r"|\[\[UIDevice\s+currentDevice\]\s+orientation\]|UIDeviceOrientationDidChange"
            r"|orientationDidChangeNotification|\.isLandscape\b|\.isPortrait\b", "code"),
    ("R03", r"\buserInterfaceIdiom\b|\bUI_USER_INTERFACE_IDIOM\b", "code"),
    ("R04", r"UIApplication\.shared\.windows|\.keyWindow\b|connectedScenes\.first"
            r"|\[\[UIApplication\s+sharedApplication\]\s+(keyWindow|windows)\]", "code"),
    ("R05", r"(safeAreaInsets|layoutMargins|safeArea\w*)\.(left|right|leading|trailing)\s*\*\s*2"
            r"|\b(topLayoutGuide|bottomLayoutGuide)\b"
            r"|safeAreaInsets\.\w+\s*\?\?\s*\d+"
            r"|if\s+[^{]*safeAreaInsets\.\w+\s*>\s*0", "code"),
    ("R06", r"UIDevice\.current\.model|\butsname\b|hw\.machine|\"iPhone\d+,\d+\""
            r"|(width|height)\s*(==|<=|>=|<|>)\s*(320|375|390|393|402|414|428|430|440|667|736|812|844|852|874|896|926|932|956)(\.0)?\b", "code"),
    ("R07", r"_?displayCornerRadius|cornerRadius\s*[:=]\s*(39|47|55)(\.0)?\b", "code"),
    ("R08", r"keyboardFrameEndUserInfoKey|UIKeyboardFrameEndUserInfoKey", "code"),
    ("R09", r"biometryType\s*==\s*\.faceID|\"[^\"]*Face ID[^\"]*\"", "code"),
    ("R09", r"Face ID", "strings"),
    ("B01", r"\b(UIToolbar|UINavigationBar|UITabBar)\((frame:[^)]*)?\)"
            r"|\[\[(UIToolbar|UINavigationBar|UITabBar)\s+alloc\]"
            r"|\.safeAreaInset\(edge:\s*\.(bottom|top)"
            r"|\.overlay\(alignment:\s*\.(bottom|top)"
            r"|navigationBarHidden\(true\)|\.toolbar\(\.hidden|setNavigationBarHidden\(true"
            r"|isNavigationBarHidden\s*=\s*true", "code"),
    ("B02", r"\bNavigationView\b", "code"),
    ("B04", r"UIBarButtonItem\(customView:|initWithCustomView:", "code"),
    ("B06", r"\"ellipsis(\.circle)?(\.fill)?\"", "code"),
    ("F01", r"\.position\(x:|\.width\s*/\s*2\b|bounds\.midX|\.center\s*=\s*"
            r"|centerXAnchor\.constraint\(equalTo:\s*(self\.)?view\.centerXAnchor", "code"),
    ("F02", r"size\.width\s*\*\s*0?\.\d+|size\.width\s*/\s*3\b", "code"),
    ("F04", r"Array\(repeating:\s*GridItem|GridItem\(\.fixed|itemSize\s*=\s*CGSize\(width:\s*\d", "code"),
    ("F05", r"\.ignoresSafeArea\(|\.edgesIgnoringSafeArea\(", "code"),
    ("S01", r"requestSceneSessionActivation|\bopenWindow\b", "code"),
    ("S03", r"didConnectNotification|UIScreenDidConnectNotification|UIScreen\.screens\b|\[UIScreen\s+screens\]", "code"),
    ("C01", r"position:\s*\.front|builtInTrueDepthCamera|AVCaptureDevicePositionFront", "code"),
    ("C02", r"position\s*==\s*\.front|position\s*==\s*AVCaptureDevicePositionFront", "code"),
    ("C03", r"\bvideoOrientation\b|AVCaptureVideoOrientation", "code"),
]
LINE_RULES = [(cid, re.compile(rx), kind) for cid, rx, kind in LINE_RULES]

COMMENT = re.compile(r"^\s*(//|/\*|\*)")
TOOLBAR_ITEM = re.compile(r"ToolbarItem(Group)?\s*(\([^)]*\))?\s*\{")
TEXT_BUTTON = re.compile(r"Button\(\s*\"[^\"]*\"\s*(\)\s*\{|,\s*action:)")
UIKIT_TEXT_ITEM = re.compile(r"UIBarButtonItem\(\s*title:")


def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.endswith(".xcassets")]
        for name in filenames:
            yield os.path.join(dirpath, name)


def kind_of(path):
    ext = os.path.splitext(path)[1]
    if ext in CODE_EXT:
        return "code"
    if ext in UI_EXT:
        return "ui"
    if ext in STRING_EXT:
        return "strings"
    if ext == ".plist":
        return "plist"
    if path.endswith(".pbxproj"):
        return "pbxproj"
    if ext == ".xcconfig":
        return "xcconfig"
    return None


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def block_after(text, start):
    """Return text from start to the brace that closes the first '{' after start."""
    i = text.find("{", start)
    if i < 0:
        return ""
    depth = 0
    for j in range(i, min(len(text), i + 4000)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[start:j + 1]
    return text[start:i + 4000]


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(2)
    root = os.path.abspath(sys.argv[1])
    as_json = "--json" in sys.argv
    findings = []
    rel = lambda p: os.path.relpath(p, root)

    def add(cid, path, line, code):
        findings.append({"check": cid, "file": rel(path), "line": line, "code": code.strip()[:160]})

    launch_keys = False
    scene_manifest = False
    swiftui_app = False
    uikit_window_delegate = None
    uses_capture = False
    plist_like = []

    for path in walk(root):
        kind = kind_of(path)
        if kind is None:
            continue
        text = read(path)

        if kind in ("pbxproj", "xcconfig"):
            plist_like.append(path)
            if re.search(r"INFOPLIST_KEY_UILaunch(Screen_Generation|StoryboardName)\s*=\s*(YES|\"?[A-Za-z])", text):
                launch_keys = True
            if re.search(r"INFOPLIST_KEY_UIApplicationSceneManifest_Generation\s*=\s*YES", text):
                scene_manifest = True
            for m in re.finditer(r"INFOPLIST_KEY_UIRequiresFullScreen\s*=\s*YES", text):
                add("D02", path, line_of(text, m.start()), m.group(0))
            for m in re.finditer(r"INFOPLIST_KEY_UISupportedInterfaceOrientations\s*=\s*\"?([^;\n]*)", text):
                if "Landscape" not in m.group(1):
                    add("D04", path, line_of(text, m.start()), m.group(0))
            continue

        if kind == "plist":
            try:
                with open(path, "rb") as f:
                    data = plistlib.load(f)
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            if any(k in data for k in ("UILaunchScreen", "UILaunchScreens", "UILaunchStoryboardName", "UILaunchStoryboards")):
                launch_keys = True
            if "UIApplicationSceneManifest" in data:
                scene_manifest = True
            if data.get("UIRequiresFullScreen") is True:
                add("D02", path, line_of(text, text.find("UIRequiresFullScreen")), "UIRequiresFullScreen = YES")
            for key in ("UISupportedInterfaceOrientations", "UISupportedInterfaceOrientations~iphone"):
                orients = data.get(key)
                if isinstance(orients, list) and orients and not any("Landscape" in o for o in orients):
                    add("D04", path, line_of(text, text.find(key)), f"{key} = {orients}")
            continue

        if kind == "ui":
            for m in re.finditer(r"<(toolbar|navigationBar|tabBar)\b[^>]*>", text):
                if 'key="' not in m.group(0):  # container-owned bars carry a key attribute
                    add("B01", path, line_of(text, m.start()), m.group(0))
            continue

        # code and strings
        lines = text.split("\n")
        for n, line in enumerate(lines, 1):
            if kind == "code" and COMMENT.match(line):
                continue
            for cid, rx, rkind in LINE_RULES:
                if rkind == kind and rx.search(line):
                    add(cid, path, n, line)

        if kind != "code":
            continue

        if re.search(r"@main\s+struct\s+\w+\s*:\s*(SwiftUI\.)?App\b", text):
            swiftui_app = True
        if re.search(r"UIApplicationDelegate", text) and re.search(r"var\s+window\s*:\s*UIWindow", text):
            uikit_window_delegate = path
        if "AVCaptureSession" in text:
            uses_capture = True
        if re.search(r"override\s+var\s+supportedInterfaceOrientations", text):
            m = re.search(r"override\s+var\s+supportedInterfaceOrientations", text)
            add("D04", path, line_of(text, m.start()), m.group(0))

        # B03: text-only buttons inside a ToolbarItem body (multi-line).
        for m in TOOLBAR_ITEM.finditer(text):
            body = block_after(text, m.start())
            if "systemImage" in body or "Image(" in body or "Label(" in body:
                continue
            b = TEXT_BUTTON.search(body)
            if b:
                off = m.start() + b.start()
                add("B03", path, line_of(text, off), lines[line_of(text, off) - 1])
        for m in UIKIT_TEXT_ITEM.finditer(text):
            call = text[m.start():m.start() + 300].split("\n\n")[0]
            if "image:" not in call:
                add("B03", path, line_of(text, m.start()), lines[line_of(text, m.start()) - 1])

        # F06: navigation container swapped on size class.
        if re.search(r"horizontalSizeClass\s*==", text) and "NavigationSplitView" in text and "NavigationStack" in text:
            m = re.search(r"horizontalSizeClass\s*==", text)
            add("F06", path, line_of(text, m.start()), lines[line_of(text, m.start()) - 1])

        # C06: flash mode set without a supportedFlashModes check in the same file.
        if "supportedFlashModes" not in text:
            for m in re.finditer(r"flashMode\s*=", text):
                add("C06", path, line_of(text, m.start()), lines[line_of(text, m.start()) - 1])

    if not launch_keys:
        add("D03", root, 0, "no UILaunchScreen / UILaunchStoryboardName key found in any Info.plist or build setting")
    if not scene_manifest and not swiftui_app:
        where = uikit_window_delegate or root
        add("R04", where, 0, "no UIApplicationSceneManifest: app uses the application lifecycle (crashes at launch with the iOS 27 SDK)")

    # Camera checks only matter when the app captures.
    if not uses_capture:
        findings = [f for f in findings if not f["check"].startswith("C")]

    findings.sort(key=lambda f: (f["check"], f["file"], f["line"]))
    if as_json:
        print(json.dumps({"root": root, "uses_capture": uses_capture, "findings": findings}, indent=1))
        return
    for f in findings:
        print(f"{f['check']}\t{f['file']}:{f['line']}\t{f['code']}")
    counts = {}
    for f in findings:
        counts[f["check"]] = counts.get(f["check"], 0) + 1
    summary = " ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "none"
    print(f"# {len(findings)} candidates: {summary}. camera={'yes' if uses_capture else 'no'}", file=sys.stderr)


if __name__ == "__main__":
    main()
