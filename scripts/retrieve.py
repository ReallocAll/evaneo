#!/usr/bin/env python3
"""Offline search and exact reading of bundled Evaneo cases (stdlib only)."""

import argparse
import json
from collections import Counter
from dataclasses import dataclass
import math
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "references"
WORDS = re.compile(r"c\+\+|c#|[a-z0-9_]+|[\u3400-\u9fff]+", re.I)
HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)\s*$")
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})(.*)$")
ANCHOR = re.compile(r"\s+\{#([^\s{}#]+)\}\s*$")
HTML_ANCHOR = re.compile(r'''<a\s+id\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+)\s*>\s*</a>''', re.I)
STOP = set("""a an and are as at be by can do does for from has have how in into is it
its of on or that the their then there these this to was were what when where which
while with without would you your use using should""".split())


def terms(text):
    """Use labels rather than URLs; preserve technical tokens and CJK bigrams."""
    text = re.sub(r"!?\[([^\]]+)\]\([^\n]*?\)", r"\1", text)
    text = re.sub(r"https?://[^\s)]+", " ", text)
    result = []
    for match in WORDS.finditer(text.casefold()):
        word = match.group()
        if "\u3400" <= word[0] <= "\u9fff":
            result.extend(word[i:i + 2] for i in range(len(word) - 1))
            if len(word) == 1:
                result.append(word)
        elif word not in STOP:
            result.append(word)
    return result


def slug(title):
    return re.sub(r"[^\w\u3400-\u9fff]+", "-", title.casefold()).strip("-") or "section"


def searchable_content(content):
    """Drop standalone HTML anchors from search terms and snippets."""
    return "\n".join(line for line in content.splitlines()
                     if not HTML_ANCHOR.fullmatch(line.strip()))


@dataclass
class Section:
    title: str
    anchor: str
    start: int
    end: int
    content: str


def read_sections(path):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    headings = []
    used = set()
    fence = None
    for number, line in enumerate(lines, 1):
        marker = FENCE.match(line)
        if marker:
            run, tail = marker.groups()
            if fence is None:
                fence = (run[0], len(run))
            elif run[0] == fence[0] and len(run) >= fence[1] and not tail.strip():
                fence = None
            continue
        if fence:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        title = re.sub(r"\s+#+\s*$", "", match.group(2)).strip()
        explicit = ANCHOR.search(title)
        anchor = explicit.group(1) if explicit else slug(title)
        if explicit:
            title = title[:explicit.start()].strip()
        base, suffix = anchor, 2
        while anchor in used:
            anchor = f"{base}-{suffix}"
            suffix += 1
        used.add(anchor)
        headings.append((title, anchor, number))
    if not headings:
        return [Section(path.stem, "document", 1, len(lines), "".join(lines))]
    sections = []
    for index, (title, anchor, start) in enumerate(headings):
        end = headings[index + 1][2] - 1 if index + 1 < len(headings) else len(lines)
        sections.append(Section(title, anchor, start, end, "".join(lines[start - 1:end])))
    return sections


def document_limit(path):
    """Return an optional document-wide evidence limit for section readers."""
    with path.open(encoding="utf-8") as source:
        header = source.readline().strip()
    prefix, suffix = "<!-- retrieval: ", " -->"
    if not header.startswith(prefix) or not header.endswith(suffix):
        return None
    try:
        metadata = json.loads(header[len(prefix):-len(suffix)])
    except (ValueError, TypeError):
        return None
    limit = metadata.get("limitations") if isinstance(metadata, dict) else None
    return limit.strip() if isinstance(limit, str) and limit.strip() else None


def case_files():
    return sorted(path for path in CASES.rglob("*.md") if path.is_file())


def reference_for(path, section=None):
    ref = path.relative_to(ROOT).as_posix()
    return ref + (f"#{section.anchor}" if section else "")


def find_reference(value):
    relative, separator, anchor = value.partition("#")
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(CASES.resolve()) or not path.is_file() or path.suffix.lower() != ".md":
        raise ValueError("Use a Markdown path returned by search, within references/.")
    sections = read_sections(path)
    if not separator:
        return path, sections, None
    selected = next((s for s in sections if s.anchor == anchor), None)
    if selected is None:
        raise ValueError(f"Section not found: {anchor}; run toc on {reference_for(path)}")
    return path, sections, selected


def search(query, limit):
    wanted = set(terms(query))
    if not wanted:
        raise ValueError("Search for a concrete engineering problem or mechanism.")
    entries = []
    frequency = Counter()
    for path in case_files():
        filename_terms = Counter(terms(path.stem.replace("-", " ")))
        sections = read_sections(path)
        for section in sections:
            content = searchable_content(section.content)
            # Opening a title-only section yields no evidence beyond its title.
            if not any(line.strip() for line in content.splitlines()
                       if not HEADING.match(line)):
                continue
            title_terms = Counter(terms(section.title))
            body_terms = Counter(terms(content))
            counts = body_terms + Counter({t: 4 * n for t, n in title_terms.items()})
            counts += Counter({t: 2 * n for t, n in filename_terms.items()})
            frequency.update(counts.keys())
            entries.append((path, section, counts))
    if not entries:
        print("No bundled cases found in references/.")
        return
    hits = []
    for path, section, counts in entries:
        matched = wanted.intersection(counts)
        if not matched:
            continue
        score = sum(math.log1p((len(entries) + 1) / (frequency[t] + 1))
                    * math.sqrt(min(counts[t], 9)) for t in matched)
        score *= 0.5 + 0.5 * len(matched) / len(wanted)
        # Source catalogues are navigation fallbacks, not primary evidence.
        is_index = path.parent == CASES / "indexes"
        hits.append((is_index, -score, reference_for(path, section), path, section))
    hits.sort(key=lambda item: (item[0], item[1], item[2]))
    if not hits:
        print("No matching case sections. Try a different failure mode or related terms.")
        return
    for _, _, reference, path, section in hits[:limit]:
        wanted_lines = (line.strip() for line in searchable_content(section.content).splitlines()
                        if not HEADING.match(line))
        excerpt = next((line for line in wanted_lines if wanted.intersection(terms(line))), "")
        if not excerpt:
            excerpt = section.title
        print(f"{reference}\n  {excerpt[:220]}")


def main(argv=None):
    # Bundled Markdown includes Unicode that may not fit the active Windows
    # console code page. Keep CLI output readable in terminals and pipelines.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    lookup = commands.add_parser("search", help="Find relevant case sections by problem.")
    lookup.add_argument("query", nargs="+")
    lookup.add_argument("--limit", type=int, default=5)
    read = commands.add_parser("show", help="Read a case or an exact #section from a search result.")
    read.add_argument("reference")
    table = commands.add_parser("toc", help="List exact section references in a case.")
    table.add_argument("reference")
    args = parser.parse_args(argv)
    try:
        if args.command == "search":
            if args.limit < 1:
                raise ValueError("--limit must be positive.")
            search(" ".join(args.query), args.limit)
        else:
            path, sections, selected = find_reference(args.reference)
            if args.command == "toc":
                for section in sections:
                    print(f"{reference_for(path, section)}  L{section.start}-{section.end}  {section.title}")
            elif selected is None:
                print(path.read_text(encoding="utf-8"), end="")
            else:
                limit = document_limit(path)
                if limit:
                    print(f"Evidence limit: {limit}")
                    print()
                print(selected.content, end="")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
