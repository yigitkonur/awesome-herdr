#!/usr/bin/env python3
"""Recount README.md table rows and rewrite every count: subcategory blurbs,
section blurbs, and the Table of Contents. Prints duplicate repo links.

Usage: python3 scripts/sync-counts.py [--check]
--check exits 1 if any count is stale, without writing.
"""
import re
import sys
from collections import Counter
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
ROW = re.compile(r"^\| \[\*\*")
SECTION = re.compile(r"^## (\d+)\. (.+)$")
SUB = re.compile(r"^### (.+)$")
BLURB = re.compile(r"^\*(\d+) projects?\. ")


def plural(n):
    return f"{n} project" if n == 1 else f"{n} projects"


lines = README.read_text().split("\n")
sec_counts, sub_counts = {}, {}
sec = sub = None
for line in lines:
    if m := SECTION.match(line):
        sec, sub = m.group(2), None
        sec_counts[sec] = 0
    elif line.startswith("## "):
        sec = sub = None
    elif (m := SUB.match(line)) and sec:
        sub = m.group(1)
        sub_counts[sub] = 0
    elif ROW.match(line) and sub:
        sub_counts[sub] += 1
        sec_counts[sec] += 1

out, sec, sub, pending = [], None, None, None
for line in lines:
    if m := SECTION.match(line):
        sec, sub = m.group(2), None
        pending = sec_counts[sec]
    elif line.startswith("## "):
        sec = sub = pending = None
    elif (m := SUB.match(line)) and sec:
        sub = m.group(1)
        pending = sub_counts[sub]
    elif pending is not None and BLURB.match(line):
        line = BLURB.sub(f"*{plural(pending)}. ", line, count=1)
        pending = None
    else:
        m = re.match(r"^(\s*(?:\d+\.|-) \[)(.+) \((\d+)\)(\]\(#.+\))$", line)
        if m and (m.group(2) in sec_counts or m.group(2) in sub_counts):
            n = sec_counts.get(m.group(2), sub_counts.get(m.group(2)))
            line = f"{m.group(1)}{m.group(2)} ({n}){m.group(4)}"
    out.append(line)

new = "\n".join(out)
links = re.findall(r"^\| \[\*\*[^]]*\*\*\]\((https://github\.com/[^/)]+/[^/)#]+)", new, re.M)
dups = [u for u, c in Counter(u.lower().rstrip("/") for u in links).items() if c > 1]
for u in dups:
    print(f"duplicate: {u}")
print(f"{sum(sub_counts.values())} projects in {len(sub_counts)} subcategories")

if "--check" in sys.argv:
    stale = new != README.read_text()
    print("counts stale" if stale else "counts ok")
    sys.exit(1 if stale or dups else 0)
README.write_text(new)
