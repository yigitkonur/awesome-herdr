#!/usr/bin/env python3
"""List Herdr projects that are not in README.md yet.

Sources, in order of signal:
  plugins  herdr.dev TUI marketplace index (GitHub topic:herdr-plugin, manifest-validated)
  gallery  herdr.dev/gallery layouts and mods for the Herdr app
  topics   GitHub search on topic:herdr, herdr-layout, herdr-mod, herdr-app (needs `gh`)

Skips repos already in README.md or listed in scripts/skipped.txt.
Writes .tmp/candidates.json (gitignored) sorted by stars, prints counts per source.
Usage: python3 scripts/discover.py [--no-github] [--since YYYY-MM-DD]
"""
import html
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = "https://assets.herdr.dev/plugins/index.json"
GALLERY = "https://herdr.dev/gallery/"
TOPICS = ["herdr", "herdr-layout", "herdr-mod", "herdr-app"]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-herdr-discover"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def listed():
    text = (ROOT / "README.md").read_text().lower()
    skipped = (ROOT / "scripts" / "skipped.txt").read_text().lower().split("\n")
    return set(re.findall(r"github\.com/([^/)\s]+/[^/)#\s]+)", text)) | {
        line.split()[0] for line in skipped if line.strip() and not line.startswith("#")}


def from_plugins():
    for p in json.loads(get(PLUGINS))["plugins"]:
        m = (p.get("manifests") or [{}])[0]
        yield {
            "repo": p["fullName"], "source": "plugins", "product": "herdr-tui",
            "stars": p.get("stars", 0), "updated": p.get("pushedAt", ""),
            "name": m.get("name", p["name"]),
            "blurb": p.get("description") or m.get("description") or "",
        }


def from_gallery():
    page = get(GALLERY)
    for card in re.findall(r'<div class="card"[^>]*>', page):
        a = dict(re.findall(r'data-([a-z]+)="([^"]*)"', card))
        m = re.match(r"https://github\.com/([^/]+/[^/]+)", a.get("gh", ""))
        if not m:
            continue
        yield {
            "repo": m.group(1), "source": "gallery", "product": "herdr-app",
            "kind": a.get("type", "").rstrip("s"), "path": a.get("gh"),
            "stars": int(a.get("stars") or 0), "updated": a.get("updated", ""),
            "name": html.unescape(a.get("name", "")), "blurb": html.unescape(a.get("blurb", "")),
        }


def from_topics():
    for topic in TOPICS:
        out = subprocess.run(
            ["gh", "search", "repos", f"--topic={topic}", "--limit", "1000",
             "--json", "fullName,stargazersCount,pushedAt,description"],
            capture_output=True, text=True, timeout=300, check=True).stdout
        for r in json.loads(out):
            yield {
                "repo": r["fullName"], "source": f"topic:{topic}", "product": "unclear",
                "stars": r["stargazersCount"], "updated": r["pushedAt"],
                "name": r["fullName"].split("/")[1], "blurb": r.get("description") or "",
            }


have = listed()
since = sys.argv[sys.argv.index("--since") + 1] if "--since" in sys.argv else ""
sources = [from_plugins, from_gallery] + ([] if "--no-github" in sys.argv else [from_topics])
found = {}
for source in sources:
    n = 0
    for c in source():
        key = c["repo"].lower()
        if key in have or c["updated"] < since:
            continue
        n += 1
        if key in found:  # keep the first, richer source; remember the others
            found[key].setdefault("also", []).append(c["source"])
        else:
            found[key] = c
    print(f"{source.__name__[5:]}: {n} not in README")

rows = sorted(found.values(), key=lambda c: -c["stars"])
(ROOT / ".tmp").mkdir(exist_ok=True)
(ROOT / ".tmp" / "candidates.json").write_text(json.dumps(rows, indent=1))
print(f"{len(rows)} unique candidates -> .tmp/candidates.json")
