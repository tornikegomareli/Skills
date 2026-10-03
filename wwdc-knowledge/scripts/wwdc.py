#!/usr/bin/env python3
"""Search Apple WWDC session transcripts, code snippets, and doc links.

Backed by a local clone of github.com/guitaripod/wwdc-sessions. Output is trimmed
to stay cheap to read: search windows each hit, show reads only what you ask for.

  wwdc.py info
  wwdc.py search "guided generation" --event wwdc2025
  wwdc.py show wwdc2025-286 --at 2:26
  wwdc.py show wwdc2025-286 --code
  wwdc.py setup | wwdc.py refresh
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = "https://github.com/guitaripod/wwdc-sessions"
DEFAULT_DIR = Path(
    os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share"
) / "wwdc-sessions"
STALE_DAYS = 30
TIMECODE = re.compile(r"^\*\*\[(\d+(?::\d+){1,2})\]\*\*\s*(.*)$")


def root(required=True):
    """Resolve the dataset directory, or exit with the command that creates it."""
    path = Path(os.environ.get("WWDC_SESSIONS_DIR") or DEFAULT_DIR).expanduser()
    if required and not (path / "catalog.json").is_file():
        sys.exit(
            f"No WWDC dataset at {path}\n"
            f"Ask the user before downloading (~175 MB), then run:\n"
            f"  python3 {Path(__file__).name} setup"
        )
    return path


def catalog(path):
    return json.loads((path / "catalog.json").read_text())


def seconds(text):
    """'2:26' or '1:04:30' or '146' -> int seconds."""
    parts = [int(p) for p in str(text).split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def clock(total):
    if total is None:
        return "?"
    total = int(total)
    h, m, s = total // 3600, (total % 3600) // 60, total % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def matches_filters(session, args):
    def has(values, needle):
        return any(needle.lower() in v.lower() for v in values)

    if args.event and args.event.lower() not in session["event"].lower():
        return False
    if args.year and session["year"] != args.year:
        return False
    if args.topic and not has(session.get("topics", []), args.topic):
        return False
    if args.platform and not has(session.get("platforms", []), args.platform):
        return False
    return True


def window(text, term, width):
    """Trim text to `width` chars around the first case-insensitive hit on term."""
    text = " ".join(text.split())
    if len(text) <= width:
        return text
    at = text.lower().find(term.lower()) if term else 0
    start = max(0, (at if at >= 0 else 0) - width // 3)
    end = min(len(text), start + width)
    if start:
        start = text.find(" ", start) + 1 or start
    if end < len(text):
        cut = text.rfind(" ", start, end)
        end = cut if cut > start else end
    return ("…" if start else "") + text[start:end].strip() + ("…" if end < len(text) else "")


def grep(path, pattern, fixed):
    """Run ripgrep over every transcript.md; yield (session dir, timecode, paragraph).

    Only timecoded paragraphs are yielded, which skips each file's frontmatter and headings.
    """
    if not shutil.which("rg"):
        sys.exit("ripgrep (rg) not found on PATH; install it to enable transcript search.")
    cmd = ["rg", "--no-heading", "--no-messages", "--ignore-case", "--glob", "transcript.md"]
    cmd += ["--fixed-strings"] if fixed else []
    cmd += ["--regexp", pattern, str(path / "sessions")]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode not in (0, 1):
        sys.exit(out.stderr.strip() or "ripgrep failed")
    for line in out.stdout.splitlines():
        file, _, text = line.partition(":")
        found = TIMECODE.match(text)
        if found:
            rel = str(Path(file).parent.relative_to(path)) + "/"
            yield rel, found.group(1), found.group(2)


def cmd_search(args):
    path = root()
    data = catalog(path)
    terms = args.query.split() if args.query else []

    # ASL sessions duplicate a signed talk word for word; surface them only when asked for.
    wants_asl = "asl" in args.query.lower().split()
    sessions = {s["path"]: s for s in data["sessions"]
                if matches_filters(s, args)
                and (wants_asl or not s["title"].strip().endswith("(ASL)"))}
    # Search on the longest term (the rarest, so ripgrep does the least work), then require
    # the remaining terms in the same paragraph.
    pattern = args.regex or (max(terms, key=len) if terms else "")
    hits = {}
    if pattern:
        rest = [] if args.regex else [t.lower() for t in terms if t != pattern]
        for rel, timecode, body in grep(path, pattern, fixed=not args.regex):
            if rel not in sessions:
                continue
            if all(t in body.lower() for t in rest):
                hits.setdefault(rel, []).append((timecode, body))

    def titled(rel):
        return all(t.lower() in sessions[rel]["title"].lower() for t in terms) if terms else False

    def keyworded(rel):
        blob = (sessions[rel]["title"] + " "
                + " ".join(sessions[rel].get("keywords", []))).lower()
        return all(t.lower() in blob for t in terms) if terms else False

    def score(rel):
        boost = 12 * titled(rel) + 6 * keyworded(rel)
        return (boost + min(len(hits.get(rel, [])), 10), sessions[rel]["year"])

    if pattern:
        # A session with no transcript hit earns a slot only when every term is in its metadata.
        ranked = sorted({*hits} | {r for r in sessions if keyworded(r)},
                        key=score, reverse=True)[: args.max_sessions]
    else:
        # Apple tags many sessions with a second topic, so a --topic survey otherwise leads with
        # talks that only mention it. Sessions owning the topic come first, then newest, then
        # session order.
        def owns_topic(rel):
            primary = sessions[rel].get("primaryTopic") or ""
            return bool(args.topic) and args.topic.lower() in primary.lower()

        ranked = sorted(sorted(sessions),
                        key=lambda r: (owns_topic(r), sessions[r]["year"]),
                        reverse=True)[: args.max_sessions]

    if not ranked:
        print("No matches." if pattern else "No sessions match those filters. Check "
              "the vocabulary with: wwdc.py info")
        return

    for rel in ranked:
        s = sessions[rel]
        flag = "" if s["hasTranscript"] else "  [no transcript]"
        print(f"\n{s['id']}  {s['title']}{flag}")
        print(f"  {s['eventName' if 'eventName' in s else 'event']} · "
              f"{s.get('primaryTopic', '?')} · {clock(s['duration'])} · {rel}")
        for timecode, body in hits.get(rel, [])[: args.excerpts]:
            print(f"  [{timecode}] {window(body, pattern, args.width)}")

    total = len(hits)
    print(f"\n{len(ranked)} shown"
          + (f" of {total} sessions with transcript hits" if total > len(ranked) else "")
          + f" · built {data['generatedAt'][:10]}")


def resolve(data, ident):
    """Accept 'wwdc2025-286', '286', or a path; return the session record."""
    ident = ident.rstrip("/")
    for s in data["sessions"]:
        if ident in (s["id"], s["path"].rstrip("/")):
            return s
    candidates = [s for s in data["sessions"] if str(s["eventContentId"]) == ident]
    if len(candidates) == 1:
        return candidates[0]
    if candidates:
        ids = " ".join(sorted(c["id"] for c in candidates))
        sys.exit(f"'{ident}' matches several sessions; pick one: {ids}")
    sys.exit(f"No session '{ident}'. Find one with: wwdc.py search \"<query>\"")


def cmd_show(args):
    path = root()
    session = resolve(catalog(path), args.session)
    folder = path / session["path"]
    meta = json.loads((folder / "metadata.json").read_text())

    print(f"{session['id']}  {session['title']}")
    print(f"{meta['eventName']} · {', '.join(session.get('topics') or ['?'])} · "
          f"{', '.join(session.get('platforms') or ['?'])} · {clock(session['duration'])}")
    print(session["url"])
    if session.get("description"):
        print(f"\n{session['description']}")

    if args.code:
        snippets = meta.get("codeSnippets") or []
        print(f"\n--- code snippets ({len(snippets)}) ---")
        for snip in snippets:
            print(f"\n[{clock(snip['startTimeSeconds'])}] {snip['title']}  ({snip['language']})")
            print(snip["code"])

    if args.resources:
        print(f"\n--- resources ({len(meta.get('resources') or [])}) ---")
        for res in meta.get("resources") or []:
            print(f"- {res['title']} ({res.get('type', '?')})")
            print(f"  {res['url']}")
            if res.get("sosumiURL"):
                print(f"  markdown: {res['sosumiURL']}")

    if args.at is not None:
        target = seconds(args.at)
        file = folder / "transcript.json"
        if not file.is_file():
            sys.exit(f"{session['id']} has no transcript.")
        segments = json.loads(file.read_text())["segments"]
        picked = [s for s in segments if abs(s["start"] - target) <= args.pad]
        print(f"\n--- transcript {clock(max(0, target - args.pad))}"
              f"–{clock(target + args.pad)} ---")
        for seg in picked:
            print(f"[{clock(seg['start'])}] {seg['text']}")
        if not picked:
            last = clock(segments[-1]["start"]) if segments else "0:00"
            print(f"Nothing at that timecode; this transcript runs to {last}. "
                  f"Widen with --pad, or find the moment with: wwdc.py search")

    if args.full:
        file = folder / "transcript.md"
        if not file.is_file():
            sys.exit(f"{session['id']} has no transcript.")
        body = file.read_text().split("---", 2)[-1]
        print(f"\n--- full transcript ({session['transcriptWordCount']} words) ---")
        print(body.strip())

    if not any((args.code, args.resources, args.at is not None, args.full)):
        counts = (len(meta.get("codeSnippets") or []), len(meta.get("resources") or []))
        print(f"\n{counts[0]} code snippets · {counts[1]} resources · "
              f"{session['transcriptWordCount'] or 0} transcript words")
        print("Read more with: --at M:SS [--pad SECONDS] | --code | --resources | --full")


def cmd_info(args):
    path = root()
    data = catalog(path)
    built = datetime.fromisoformat(data["generatedAt"])
    age = (datetime.now(timezone.utc) - built).days
    print(f"dataset   {path}")
    print(f"built     {data['generatedAt'][:10]}  ({age} days ago)")
    print(f"counts    {data['counts']['sessions']} sessions · "
          f"{data['counts']['transcripts']} transcripts · {data['counts']['events']} events")
    if age > STALE_DAYS:
        print(f"          stale by more than {STALE_DAYS} days — refresh with: wwdc.py refresh")
    print("\nevents    " + " ".join(e["id"] for e in data["events"]))
    print("\ntopics")
    for topic in sorted({t for s in data["sessions"] for t in s.get("topics", [])}):
        print(f"  {topic}")
    print("\nplatforms " + " ".join(
        sorted({p for s in data["sessions"] for p in s.get("platforms", [])})))


def cmd_setup(args):
    path = root(required=False)
    if (path / "catalog.json").is_file() and not args.force:
        print(f"Dataset already at {path}. Update it with: wwdc.py refresh")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and args.force:
        shutil.rmtree(path)
    print(f"Cloning {REPO} (~175 MB) into {path} …")
    subprocess.run(["git", "clone", "--depth", "1", REPO, str(path)], check=True)
    cmd_info(args)


def cmd_refresh(args):
    path = root()
    for cmd in (["git", "fetch", "--depth", "1", "origin", "master"],
                ["git", "reset", "--hard", "origin/master"]):
        subprocess.run(cmd, cwd=path, check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["git", "gc", "--prune=now", "--quiet"], cwd=path, check=False)
    cmd_info(args)


def main():
    parser = argparse.ArgumentParser(prog="wwdc.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    search = sub.add_parser("search", help="find sessions by transcript text and metadata")
    search.add_argument("query", nargs="?", default="",
                        help="terms that must all appear in one transcript paragraph")
    search.add_argument("--regex", help="use this regex instead of the query terms")
    search.add_argument("--event", help="e.g. wwdc2026, tech-talks")
    search.add_argument("--year", type=int)
    search.add_argument("--topic", help="substring of a topic name, e.g. 'swiftui'")
    search.add_argument("--platform", help="iOS, macOS, visionOS, …")
    search.add_argument("--max-sessions", type=int, default=6)
    search.add_argument("--excerpts", type=int, default=2, help="excerpts per session")
    search.add_argument("--width", type=int, default=170, help="excerpt characters")
    search.set_defaults(func=cmd_search)

    show = sub.add_parser("show", help="read one session")
    show.add_argument("session", help="wwdc2025-286, 286, or a dataset path")
    show.add_argument("--at", help="transcript around this timecode (M:SS or H:MM:SS)")
    show.add_argument("--pad", type=int, default=45, help="seconds either side of --at")
    show.add_argument("--code", action="store_true", help="Apple's code snippets")
    show.add_argument("--resources", action="store_true", help="linked docs, with markdown URLs")
    show.add_argument("--full", action="store_true", help="entire transcript")
    show.set_defaults(func=cmd_show)

    info = sub.add_parser("info", help="dataset location, build date, filter vocabulary")
    info.set_defaults(func=cmd_info)

    setup = sub.add_parser("setup", help="clone the dataset (~175 MB)")
    setup.add_argument("--force", action="store_true", help="re-clone over an existing dataset")
    setup.set_defaults(func=cmd_setup)

    refresh = sub.add_parser("refresh", help="update the dataset to Apple's latest sessions")
    refresh.set_defaults(func=cmd_refresh)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
