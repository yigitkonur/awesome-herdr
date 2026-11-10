#!/usr/bin/env python3
"""Refresh GitHub stars for every catalog row, drop archived or deleted repos,
and re-sort each table by stars (the official subcategory keeps its order).

Removed repos are appended to scripts/skipped.txt so discover.py does not bring
them back. Run scripts/sync-counts.py afterwards. Needs `gh` (GraphQL).
Usage: python3 scripts/refresh-stars.py [--dry-run]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROW = re.compile(r"^\| \[\*\*(.+?)\*\*\]\((\S+?)\) \|(?: ([\d,]+|—) \|)? (.*) \|$")
HEADER = ["| Project | Stars | What it does |", "|---|--:|---|"]
KEEP_ORDER = {"Official Herdr projects and skill"}


def key(url):
    m = re.match(r"https://github\.com/([^/\s)]+)/([^/\s)#?]+)", url)
    return f"{m.group(1)}/{m.group(2)}".lower().removesuffix(".git") if m else None


def fetch(keys):
    out = {}
    keys = sorted(keys)
    for i in range(0, len(keys), 80):
        chunk = keys[i:i + 80]
        q = "query{" + "".join(
            f'r{j}:repository(owner:{json.dumps(k.split("/")[0])},name:{json.dumps(k.split("/")[1])})'
            "{stargazerCount isArchived}" for j, k in enumerate(chunk)) + "}"
        res = subprocess.run(["gh", "api", "graphql", "-f", f"query={q}"], capture_output=True, text=True, timeout=120)
        body = json.loads(res.stdout or "{}")
        if "data" not in body or body["data"] is None:
            sys.exit(f"GraphQL failed: {res.stderr.strip() or body}")
        for j, k in enumerate(chunk):
            out[k] = body["data"].get(f"r{j}")  # None: deleted, renamed away, or private
    return out


files = sorted((ROOT / "catalog").glob("[0-9][0-9]-*.md"))
texts = {f: f.read_text().split("\n") for f in files}
meta = fetch({k for lines in texts.values() for l in lines if (m := ROW.match(l)) and (k := key(m.group(2)))})

removed = []
for f, lines in texts.items():
    out, sub, table = [], None, []

    def flush():
        if table and sub not in KEEP_ORDER:
            table.sort(key=lambda r: -r[0])
        out.extend(r[1] for r in table)
        table.clear()

    for l in lines:
        m = ROW.match(l)
        if not m:
            flush()
            if l.startswith("### "):
                sub = l[4:]
            if l == "| Project | What it does |":
                l = HEADER[0]
            elif l == "|---|---|" and out and out[-1] == HEADER[0]:
                l = HEADER[1]
            out.append(l)
            continue
        label, url, _, desc = m.groups()
        k = key(url)
        info = meta.get(k) if k else {"stargazerCount": None, "isArchived": False}
        if k and (info is None or info["isArchived"]):
            removed.append((k, "repository is archived" if info else "repository returns 404"))
            continue
        stars = info["stargazerCount"]
        table.append((stars or 0, f"| [**{label}**]({url}) | {'—' if stars is None else f'{stars:,}'} | {desc} |"))
    flush()
    texts[f] = out

print(f"{len(meta)} repos checked, {len(removed)} removed")
for k, why in removed:
    print(f"  {why}: {k}")
if "--dry-run" in sys.argv:
    sys.exit(0)
for f, lines in texts.items():
    f.write_text("\n".join(lines))
if removed:
    sk = ROOT / "scripts" / "skipped.txt"
    have = {l.split()[0] for l in sk.read_text().split("\n") if l.strip() and not l.startswith("#")}
    add = [f"{k}  # {why}" for k, why in dict(removed).items() if k not in have]
    sk.write_text(sk.read_text().rstrip("\n") + "\n" + "\n".join(add) + "\n")
