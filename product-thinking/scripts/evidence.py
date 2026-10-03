#!/usr/bin/env python3
"""Fetch live user evidence about a product or its competitors.

  evidence.py appstore "<app name or numeric id>" [--country us] [--pages 2]
  evidence.py hn "<query>" [--comments]
  evidence.py github <owner/repo> "<terms>"
  evidence.py stackoverflow "<query>"
  evidence.py releases <owner/repo>

Prints one item per line: date, rating or score, text, URL. Cite the URL in findings.
No API keys needed. Set GITHUB_TOKEN to raise the GitHub limit from 10 to 30 requests per minute.
"""

import argparse
import html
import re
import json
import os
import sys
import time
import urllib.parse
import urllib.request


def report_empty(source, count):
    if count == 0:
        print(f"{source}: no results. Treat this as missing evidence, not as zero complaints.")


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "product-thinking-skill", **(headers or {})})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def short(text, n=300):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = " ".join(text.split())
    return text if len(text) <= n else text[:n] + "..."


def appstore(args):
    app_id = args.app
    if not app_id.isdigit():
        q = urllib.parse.urlencode({"term": args.app, "entity": "software", "limit": 5, "country": args.country})
        results = get(f"https://itunes.apple.com/search?{q}")["results"]
        if not results:
            sys.exit(f"No App Store app found for '{args.app}'.")
        for r in results:
            print(f"match: {r['trackName']} id={r['trackId']} rating={r.get('averageUserRating', 0):.1f} ({r.get('userRatingCount', 0)} ratings)")
        app_id = str(results[0]["trackId"])
        print(f"using id={app_id}\n")
    count = 0
    for page in range(1, min(args.pages, 10) + 1):
        url = f"https://itunes.apple.com/{args.country}/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json"
        entries = get(url).get("feed", {}).get("entry", [])
        if isinstance(entries, dict):
            entries = [entries]
        for e in entries:
            if "im:rating" not in e:
                continue
            count += 1
            print(f"{e['updated']['label'][:10]} | {e['im:rating']['label']}/5 | v{e['im:version']['label']} | "
                  f"{short(e['title']['label'] + ': ' + e['content']['label'])} | https://apps.apple.com/{args.country}/app/id{app_id}")
    if count == 0:
        print("appstore reviews: no results. Apple's review feed is unofficial and sometimes returns nothing. Retry later; treat as missing evidence.")


def hn(args):
    tags = "comment" if args.comments else "story"
    q = urllib.parse.urlencode({"query": args.query, "tags": tags, "hitsPerPage": 30,
                               "typoTolerance": "false", "advancedSyntax": "true"})
    hits = get(f"https://hn.algolia.com/api/v1/search?{q}")["hits"]
    report_empty("hn", len(hits))
    for h in hits:
        text = h.get("title") or h.get("comment_text")
        print(f"{h['created_at'][:10]} | {h.get('points') or 0} pts | {short(text)} | https://news.ycombinator.com/item?id={h['objectID']}")


def github(args):
    q = urllib.parse.urlencode({"q": f"{args.terms} repo:{args.repo} is:issue", "sort": "reactions", "per_page": 30})
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    items = get(f"https://api.github.com/search/issues?{q}", headers)["items"]
    report_empty("github issues", len(items))
    for i in items:
        print(f"{i['created_at'][:10]} | {i['reactions']['total_count']} reactions | {i['state']} | {short(i['title'])} | {i['html_url']}")


def stackoverflow(args):
    q = urllib.parse.urlencode({"q": args.query, "site": "stackoverflow", "pagesize": 20, "order": "desc", "sort": "votes"})
    items = get(f"https://api.stackexchange.com/2.3/search/advanced?{q}")["items"]
    report_empty("stackoverflow", len(items))
    for i in items:
        print(f"{time.strftime('%Y-%m-%d', time.gmtime(i['creation_date']))} | {i['score']} votes | {short(i['title'])} | {i['link']}")


def releases(args):
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    rels = get(f"https://api.github.com/repos/{args.repo}/releases?per_page=30", headers)
    report_empty("github releases", len(rels))
    for r in rels:
        downloads = sum(a["download_count"] for a in r["assets"])
        print(f"{(r['published_at'] or '')[:10]} | {downloads} downloads | {r['tag_name']} | {r['html_url']}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("appstore"); a.add_argument("app"); a.add_argument("--country", default="us"); a.add_argument("--pages", type=int, default=2)
    h = sub.add_parser("hn"); h.add_argument("query"); h.add_argument("--comments", action="store_true")
    g = sub.add_parser("github"); g.add_argument("repo"); g.add_argument("terms")
    s = sub.add_parser("stackoverflow"); s.add_argument("query")
    r = sub.add_parser("releases"); r.add_argument("repo")
    args = p.parse_args()
    try:
        {"appstore": appstore, "hn": hn, "github": github, "stackoverflow": stackoverflow, "releases": releases}[args.cmd](args)
    except urllib.error.HTTPError as e:
        sys.exit(f"{args.cmd}: HTTP {e.code}. The source may be rate limiting or the endpoint changed.")


if __name__ == "__main__":
    main()
