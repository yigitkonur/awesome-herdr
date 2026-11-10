#!/usr/bin/env python3
"""Rebuild the catalog counts and the README from catalog/*.md.

catalog/NN-*.md hold the full tables, one file per domain; they are the files to
edit. This script recounts every table there, rewrites the count lines and each
file's own index, then regenerates the README between "## Contents" and
"## Resources": the Contents list and, per subcategory, the top projects by
GitHub stars (tables are kept in star order) with a link to the full list.
Prints duplicate repo links.

Usage: python3 scripts/sync-counts.py [--check]
--check exits 1 if anything is stale or duplicated, without writing.
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOP = 10
ROW = re.compile(r"^\| \[\*\*.+?\*\*\]\((\S+?)\) \| .* \|$")
slug = lambda t: re.sub(r"[^\w\- ]", "", t.lower()).replace(" ", "-")
plural = lambda n: f"{n} project" if n == 1 else f"{n} projects"


def parse(path):
    dom, sub = None, None
    for line in path.read_text().split("\n"):
        if m := re.match(r"^## (\d+)\. (.+)$", line):
            dom = {"n": int(m.group(1)), "title": m.group(2), "blurb": "", "note": None, "subs": [], "file": path.name}
            sub = None
        elif line.startswith("### ") and dom:
            sub = {"title": line[4:], "blurb": "", "note": None, "rows": []}
            dom["subs"].append(sub)
        elif dom and (m := re.match(r"^\*\d+ projects?\. (.*)\*$", line)):
            (sub or dom)["blurb"] = m.group(1).rstrip(".")
        elif dom and line.startswith("> "):
            (sub or dom)["note"] = line[2:]
        elif dom and sub and ROW.match(line):
            sub["rows"].append(line)
    return dom


def block(d, rows_for, more=None):
    total = sum(len(s["rows"]) for s in d["subs"])
    out = [f"## {d['n']}. {d['title']}", "", f"*{plural(total)}. {d['blurb']}.*", ""]
    if more:
        out = out[:2] + [more, ""]
    if d["note"]:
        out += [f"> {d['note']}", ""]
    for s in d["subs"]:
        n = len(s["rows"])
        out += [f"### {s['title']}", "", f"*{plural(n)}. {s['blurb']}.*", ""]
        if s["note"]:
            out += [f"> {s['note']}", ""]
        out += ["| Project | What it does |", "|---|---|"] + rows_for(s) + [""]
        if n > len(rows_for(s)):
            out += [f"**[All {n} projects →](catalog/{d['file']}#{slug(s['title'])})**", ""]
    return out, total


files = sorted((ROOT / "catalog").glob("[0-9][0-9]-*.md"))
domains = [parse(f) for f in files]
changed, new_files = [], {}
for f, d in zip(files, domains):
    body, total = block(d, lambda s: s["rows"])
    index = [f"- [{s['title']} ({len(s['rows'])})](#{slug(s['title'])})" for s in d["subs"]]
    text = "\n".join([f"# Awesome Herdr: {d['title']}", "",
                      f"The full list for domain {d['n']} of [Awesome Herdr](../README.md#{slug(str(d['n']) + '. ' + d['title'])}), ordered by GitHub stars.", ""]
                     + index + ["", "---", ""] + body).rstrip("\n") + "\n"
    new_files[f] = text

readme = (ROOT / "README.md").read_text()
head, foot = readme[: readme.index("## Contents")], readme[readme.index("## Resources"):]
toc, body = ["## Contents", ""], []
for d in domains:
    total = sum(len(s["rows"]) for s in d["subs"])
    toc.append(f"{d['n']}. [{d['title']} ({total})](#{slug(str(d['n']) + '. ' + d['title'])})")
    toc += [f"   - [{s['title']} ({len(s['rows'])})](#{slug(s['title'])})" for s in d["subs"]]
    part, _ = block(d, lambda s: s["rows"][:TOP],
                    more=f"*{plural(total)}. {d['blurb']}.* The top {TOP} of each subcategory by stars are below; the full list is in [catalog/{d['file']}](catalog/{d['file']}).")
    body += ["---", ""] + part
toc += [f"{len(domains) + 1}. [Resources](#resources)", f"{len(domains) + 2}. [Reference](#reference)", ""]
new_readme = head + "\n".join(toc + body + ["---", "", ""]) + foot

links = [ROW.match(r).group(1).lower().rstrip("/") for d in domains for s in d["subs"] for r in s["rows"]]
dups = [u for u, c in Counter(links).items() if c > 1]
for u in dups:
    print(f"duplicate: {u}")
stale = [f.name for f, t in new_files.items() if f.read_text() != t] + (["README.md"] if readme != new_readme else [])
print(f"{len(links)} projects in {sum(len(d['subs']) for d in domains)} subcategories across {len(domains)} catalog files; README {len(new_readme.encode()) // 1024} KB")
if "--check" in sys.argv:
    print("stale: " + ", ".join(stale) if stale else "counts ok")
    sys.exit(1 if stale or dups else 0)
for f, t in new_files.items():
    f.write_text(t)
(ROOT / "README.md").write_text(new_readme)
