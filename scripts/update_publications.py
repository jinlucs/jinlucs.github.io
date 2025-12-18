#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convert a BibTeX file into a Jekyll-friendly YAML file:
  assets/bib/publications.bib  ->  _data/publications.yml

Designed for GitHub Pages / Beautiful Jekyll (no custom Jekyll plugins needed).
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

try:
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
except ImportError as e:
    raise SystemExit(
        "Missing dependency bibtexparser. Install with: pip install bibtexparser"
    ) from e


MONTH_MAP = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}


def _clean_tex(s: str) -> str:
    """Lightweight cleanup: removes braces and collapses whitespace."""
    s = s.replace("\n", " ").strip()
    # Remove outer braces used for BibTeX capitalization protection
    s = re.sub(r"[{}]", "", s)
    # Common TeX escapes (minimal)
    s = s.replace(r"\&", "&")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _parse_year(entry: Dict[str, Any]) -> Optional[int]:
    y = entry.get("year") or ""
    y = str(y).strip()
    if y.isdigit():
        return int(y)
    # Try parsing from "date" like 2023-05-01
    d = str(entry.get("date") or "").strip()
    m = re.match(r"^(\d{4})", d)
    if m:
        return int(m.group(1))
    return None


def _parse_month(entry: Dict[str, Any]) -> int:
    m = str(entry.get("month") or "").strip().lower()
    if not m:
        # try date
        d = str(entry.get("date") or "").strip()
        m2 = re.match(r"^\d{4}-(\d{2})", d)
        if m2:
            try:
                mm = int(m2.group(1))
                return max(1, min(12, mm))
            except Exception:
                return 0
        return 0
    # month can be numeric or "jan"
    if m.isdigit():
        mm = int(m)
        return max(1, min(12, mm))
    m = m.strip(".")
    return MONTH_MAP.get(m, 0)


def _split_authors(author_field: str) -> List[str]:
    # BibTeX author format: "Last, First and Last2, First2" or "First Last and ..."
    parts = [a.strip() for a in author_field.split(" and ") if a.strip()]
    out: List[str] = []
    for a in parts:
        if "," in a:
            # "Last, First Middle"
            last, first = [x.strip() for x in a.split(",", 1)]
            if first:
                out.append(f"{first} {last}".strip())
            else:
                out.append(last.strip())
        else:
            out.append(a.strip())
    return out


def _authors_html(authors: List[str], me_name: str) -> str:
    # Bold your name if it matches exactly (case-insensitive)
    me_low = me_name.lower()
    pretty = []
    for a in authors:
        if a.lower() == me_low:
            pretty.append(f"<strong>{a}</strong>")
        else:
            pretty.append(a)
    return ", ".join(pretty)


def _best_url(entry: Dict[str, Any]) -> Optional[str]:
    url = (entry.get("url") or "").strip()
    if url:
        return url

    doi = (entry.get("doi") or "").strip()
    if doi:
        return f"https://doi.org/{doi}"

    # arXiv fields sometimes appear as eprint + archivePrefix
    eprint = (entry.get("eprint") or "").strip()
    arch = (entry.get("archivePrefix") or "").strip().lower()
    if eprint and "arxiv" in arch:
        return f"https://arxiv.org/abs/{eprint}"

    return None


def _venue(entry: Dict[str, Any]) -> str:
    # Prefer journal or booktitle
    for k in ("journal", "booktitle", "publisher", "howpublished"):
        v = (entry.get(k) or "").strip()
        if v:
            return _clean_tex(v)
    return ""


def _entry_type(entry: Dict[str, Any]) -> str:
    return str(entry.get("ENTRYTYPE") or "").strip().lower()


def convert_bib_to_yaml(
    bib_path: Path,
    out_path: Path,
    me_name: str = "Jin Lu",
) -> int:
    if not bib_path.exists():
        raise FileNotFoundError(f"BibTeX not found: {bib_path}")

    parser = BibTexParser(common_strings=True)
    with bib_path.open("r", encoding="utf-8") as f:
        bib_db = bibtexparser.load(f, parser=parser)

    pubs: List[Dict[str, Any]] = []
    for entry in bib_db.entries:
        title = _clean_tex(str(entry.get("title") or "").strip())
        if not title:
            continue

        year = _parse_year(entry)
        month = _parse_month(entry)
        authors_raw = str(entry.get("author") or "").strip()
        authors = _split_authors(authors_raw) if authors_raw else []

        url = _best_url(entry)
        venue = _venue(entry)
        etype = _entry_type(entry)

        # A stable, sortable key (descending)
        sort_key = (year or 0) * 100 + (month or 0)

        pubs.append(
            {
                "bibkey": entry.get("ID"),
                "type": etype,
                "title": title,
                "authors": authors,
                "authors_html": _authors_html(authors, me_name) if authors else "",
                "year": year or 0,
                "month": month or 0,
                "venue": venue,
                "url": url,
                "note": _clean_tex(str(entry.get("note") or "").strip()) if entry.get("note") else "",
                "sort_key": sort_key,
            }
        )

    pubs.sort(key=lambda x: (x["sort_key"], x["title"]), reverse=True)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(pubs, f, sort_keys=False, allow_unicode=True)

    return len(pubs)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bib", required=True, help="Path to publications .bib")
    ap.add_argument("--out", required=True, help="Output YAML path (e.g. _data/publications.yml)")
    ap.add_argument("--me", default="Jin Lu", help="Name to bold in author lists")
    args = ap.parse_args()

    n = convert_bib_to_yaml(Path(args.bib), Path(args.out), me_name=args.me)
    print(f"Wrote {n} publications to {args.out}")


if __name__ == "__main__":
    main()
