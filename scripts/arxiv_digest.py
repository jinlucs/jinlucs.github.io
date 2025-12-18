#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlencode

import feedparser
import requests


ARXIV_API = "https://export.arxiv.org/api/query"


@dataclass
class Paper:
    arxiv_id: str          # without version, e.g. 2501.01234
    title: str
    authors: List[str]
    abstract: str
    categories: List[str]
    published: datetime
    abs_url: str
    pdf_url: str


def _norm_space(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def _strip_version(arxiv_abs_url: str) -> str:
    # e.g. http://arxiv.org/abs/2501.01234v2 -> 2501.01234
    m = re.search(r"/abs/([^/]+)$", arxiv_abs_url)
    if not m:
        return arxiv_abs_url
    raw = m.group(1)
    return re.sub(r"v\d+$", "", raw)


def fetch_recent_arxiv(
    cats: List[str],
    hours_back: int = 36,
    max_results: int = 80,
    user_agent: str = "jinlucs.github.io arxiv-digest (contact: jin.lu@uga.edu)",
) -> List[Paper]:
    # One request total (good for arXiv rate limits).
    search_query = " OR ".join([f"cat:{c.strip()}" for c in cats if c.strip()])
    params = {
        "search_query": f"({search_query})",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "start": 0,
        "max_results": max_results,
    }
    url = f"{ARXIV_API}?{urlencode(params)}"

    r = requests.get(url, headers={"User-Agent": user_agent}, timeout=30)
    r.raise_for_status()

    feed = feedparser.parse(r.text)
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=hours_back)

    papers_by_id: Dict[str, Paper] = {}

    for e in feed.entries:
        published = datetime(*e.published_parsed[:6], tzinfo=timezone.utc)
        if published < cutoff:
            continue

        title = _norm_space(e.title)
        abstract = _norm_space(e.summary)

        abs_url = ""
        pdf_url = ""
        for link in getattr(e, "links", []):
            if link.get("rel") == "alternate" and link.get("type") == "text/html":
                abs_url = link.get("href", "")
            if link.get("title") == "pdf":
                pdf_url = link.get("href", "")

        if not abs_url:
            abs_url = e.id
        if not pdf_url and abs_url:
            pdf_url = abs_url.replace("/abs/", "/pdf/")

        arxiv_id = _strip_version(abs_url)
        authors = [a.name for a in getattr(e, "authors", [])]
        categories = [t.term for t in getattr(e, "tags", [])] if getattr(e, "tags", None) else []

        papers_by_id[arxiv_id] = Paper(
            arxiv_id=arxiv_id,
            title=title,
            authors=authors,
            abstract=abstract,
            categories=categories,
            published=published,
            abs_url=abs_url,
            pdf_url=pdf_url,
        )

    # Newest first
    return sorted(papers_by_id.values(), key=lambda p: p.published, reverse=True)


# -------------------------
# Free-tier LLM providers
# -------------------------

class LLM:
    def generate(self, system: str, user: str, max_tokens: int = 1200) -> str:
        raise NotImplementedError



class CloudflareWorkersAILLM(LLM):
    """
    Cloudflare Workers AI OpenAI-compatible chat completions endpoint.

    Docs show:
      baseURL: https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1
      POST   : https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions
      Header : Authorization: Bearer {api_token}
    """

    def __init__(self, api_token: str, account_id: str, model: str) -> None:
        self.api_token = api_token
        self.account_id = account_id
        self.model = model
        self.url = (
            f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions"
        )

    def generate(self, system: str, user: str, max_tokens: int = 1200) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.2,
            "max_tokens": max_tokens,
        }

        r = requests.post(
            self.url,
            headers={
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()

        # Cloudflare's OpenAI-compat endpoint should return an OpenAI-style object.
        # Some Cloudflare endpoints wrap payloads under "result", so handle both.
        root = data.get("result") if isinstance(data, dict) and "result" in data else data

        if isinstance(root, dict):
            if "choices" in root and isinstance(root["choices"], list) and root["choices"]:
                msg = root["choices"][0].get("message") or {}
                if isinstance(msg, dict) and "content" in msg:
                    return str(msg["content"]).strip()

            # Fallback for /ai/run style responses: {"result": {"response": "..."}, ...}
            if "response" in root:
                return str(root["response"]).strip()

        raise ValueError(f"Unexpected Workers AI response schema: {data}")


class GroqLLM(LLM):
    """
    Groq provides an OpenAI-compatible endpoint:
      base_url: https://api.groq.com/openai/v1
      chat completions: POST https://api.groq.com/openai/v1/chat/completions
    :contentReference[oaicite:2]{index=2}
    """
    def __init__(self, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def generate(self, system: str, user: str, max_tokens: int = 1200) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.2,
            "max_tokens": max_tokens,
        }
        r = requests.post(
            self.url,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]


class GeminiLLM(LLM):
    """
    Gemini generateContent endpoint:
      POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key=...
    :contentReference[oaicite:3]{index=3}
    """
    def __init__(self, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model

    def generate(self, system: str, user: str, max_tokens: int = 1200) -> str:
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{self.model}:generateContent?key={self.api_key}"
        )
        # System instruction supported by API; keep it simple as first content.
        payload = {
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"parts": [{"text": user}]}],
            "generationConfig": {"temperature": 0.2, "maxOutputTokens": max_tokens},
        }
        r = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()
        # candidates[0].content.parts[0].text
        return data["candidates"][0]["content"]["parts"][0]["text"]


def get_llm_from_env() -> Optional[LLM]:
    provider = (os.getenv("LLM_PROVIDER") or "").strip().lower()

    # Cloudflare Workers AI (OpenAI compatible)
    if provider in {"cloudflare", "workersai", "workers-ai", "workers_ai", "cf"}:
        token = (
            os.getenv("CF_API_TOKEN")
            or os.getenv("CLOUDFLARE_API_TOKEN")
            or os.getenv("CLOUDFLARE_API_KEY")
            or ""
        ).strip()
        account_id = (
            os.getenv("CF_ACCOUNT_ID")
            or os.getenv("CLOUDFLARE_ACCOUNT_ID")
            or ""
        ).strip()
        model = (
            os.getenv("CF_MODEL")
            or os.getenv("CLOUDFLARE_MODEL")
            or "@cf/meta/llama-3.1-8b-instruct"
        ).strip()

        if token and account_id:
            return CloudflareWorkersAILLM(token, account_id, model)

    # Groq (kept for optional use)
    if provider == "groq":
        key = (os.getenv("GROQ_API_KEY") or "").strip()
        model = (os.getenv("GROQ_MODEL") or "llama-3.3-70b-versatile").strip()
        if key:
            return GroqLLM(key, model)

    # Gemini (kept for optional use)
    if provider == "gemini":
        key = (os.getenv("GEMINI_API_KEY") or "").strip()
        model = (os.getenv("GEMINI_MODEL") or "gemini-2.0-flash").strip()
        if key:
            return GeminiLLM(key, model)

    return None


def choose_interesting(papers: List[Paper], top_n: int, llm: Optional[LLM]) -> List[Paper]:
    if not papers:
        return []
    if llm is None:
        # Fallback heuristic: keep newest, and slightly boost optimization keywords.
        keywords = ("optimization", "convergence", "prox", "admm", "gradient", "stochastic", "dual", "lagrang")
        def score(p: Paper) -> Tuple[int, datetime]:
            k = sum(1 for w in keywords if w in p.title.lower() or w in p.abstract.lower())
            return (k, p.published)
        return sorted(papers, key=score, reverse=True)[:top_n]

    # LLM-based selection: ask for indices in JSON.
    # Keep payload short to reduce token usage.
    compact = []
    for i, p in enumerate(papers[:40]):
        abs_short = p.abstract[:500] + ("…" if len(p.abstract) > 500 else "")
        compact.append(f"[{i}] {p.title} | cats={','.join(p.categories[:4])}\nABS: {abs_short}\n")

    system = (
        "You are a careful ML + optimization researcher. "
        "Select the most interesting papers ONLY from the provided list. "
        "Prefer novelty, clarity, and relevance to modern ML/optimization. "
        "Return STRICT JSON only."
    )
    user = (
        f"Pick top {top_n} papers.\n\n"
        "Return JSON as:\n"
        "{\n"
        '  "selected": [{"index": 3, "why": "..."}, ...]\n'
        "}\n\n"
        "List:\n" + "\n".join(compact)
    )

    try:
        out = llm.generate(system, user, max_tokens=700)
        # Extract first JSON object defensively
        m = re.search(r"\{.*\}", out, flags=re.S)
        if not m:
            raise ValueError("No JSON found")
        data = json.loads(m.group(0))
        idxs = []
        for item in data.get("selected", []):
            if isinstance(item, dict) and "index" in item:
                idxs.append(int(item["index"]))
        idxs = [i for i in idxs if 0 <= i < len(papers[:40])]
        chosen = [papers[i] for i in idxs][:top_n]
        return chosen if chosen else papers[:top_n]
    except Exception:
        return papers[:top_n]


def explain_with_math(p: Paper, llm: Optional[LLM]) -> str:
    if llm is None:
        return (
            "_(No LLM key configured — showing abstract only. "
            "Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_"
        )

    system = (
        "You write concise research notes for ML/optimization papers.\n"
        "CRITICAL: You may ONLY use information from the provided title + abstract.\n"
        "If something is not specified, say: 'Not specified in abstract.'\n"
        "Produce a math-oriented explanation with 1–3 LaTeX display equations using $$...$$.\n"
        "No hallucinated theorem statements."
    )
    user = (
        f"TITLE: {p.title}\n"
        f"AUTHORS: {', '.join(p.authors)}\n"
        f"CATEGORIES: {', '.join(p.categories)}\n\n"
        f"ABSTRACT:\n{p.abstract}\n\n"
        "Write sections:\n"
        "1) Intuition (2-3 bullets)\n"
        "2) Problem setup (with notation)\n"
        "3) Key method (equations/pseudocode if possible)\n"
        "4) Guarantees (only if stated)\n"
        "5) Practical takeaways\n"
    )
    return llm.generate(system, user, max_tokens=1200).strip()


def write_digest_post(
    date_utc: datetime,
    chosen: List[Paper],
    llm: Optional[LLM],
    out_dir: Path = Path("_posts"),
) -> Optional[Path]:
    if not chosen:
        return None

    yyyy_mm_dd = date_utc.strftime("%Y-%m-%d")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{yyyy_mm_dd}-arxiv-digest.md"

    force = (os.getenv("FORCE") or "").strip().lower() in ("1", "true", "yes")

    # Avoid overwriting unless forced
    if out_path.exists() and not force:
        return None

    lines: List[str] = []
    lines.append("---")
    lines.append('layout: post')
    lines.append(f'title: "Daily arXiv Digest — {yyyy_mm_dd} (ML + Optimization)"')
    lines.append("categories: [arxiv]")
    lines.append("tags: [arxiv, digest, ml, optimization]")
    lines.append("mathjax: true")
    lines.append("---")
    lines.append("")
    lines.append("> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.")
    lines.append("> Equations are **interpretive**; always verify with the PDF.")
    lines.append("")

    for i, p in enumerate(chosen, start=1):
        lines.append(f"## {i}) {p.title}")
        lines.append(f"- **Authors:** {', '.join(p.authors)}")
        lines.append(f"- **arXiv:** [{p.arxiv_id}]({p.abs_url}) · [pdf]({p.pdf_url})")
        if p.categories:
            lines.append(f"- **Categories:** {', '.join(p.categories)}")
        lines.append("")
        lines.append("### Abstract")
        lines.append(f"> {p.abstract}")
        lines.append("")
        lines.append("### Math explanation (LLM)")
        lines.append(explain_with_math(p, llm))
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def update_seen_ids(chosen: List[Paper], path: Path = Path("_data/arxiv_seen.json")) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    seen = set()
    if path.exists():
        try:
            seen = set(json.loads(path.read_text(encoding="utf-8")))
        except Exception:
            seen = set()
    for p in chosen:
        seen.add(p.arxiv_id)
    path.write_text(json.dumps(sorted(seen), indent=2), encoding="utf-8")


def main() -> None:
    cats = [c.strip() for c in (os.getenv("ARXIV_CATS") or "cs.LG,stat.ML,math.OC").split(",") if c.strip()]
    hours_back = int(os.getenv("HOURS_BACK") or "36")
    max_results = int(os.getenv("MAX_RESULTS") or "80")
    top_n = int(os.getenv("TOP_N") or "5")

    llm = get_llm_from_env()
    force = (os.getenv("FORCE") or "").strip().lower() in ("1", "true", "yes")

    papers = fetch_recent_arxiv(cats=cats, hours_back=hours_back, max_results=max_results)

    # Filter out already-seen papers
    seen_path = Path("_data/arxiv_seen.json")
    seen = set()
    if seen_path.exists():
        try:
            seen = set(json.loads(seen_path.read_text(encoding="utf-8")))
        except Exception:
            seen = set()

    if not force:
        papers = [p for p in papers if p.arxiv_id not in seen]

    chosen = choose_interesting(papers, top_n=top_n, llm=llm)

    today_utc = datetime.now(timezone.utc)
    out = write_digest_post(today_utc, chosen, llm)
    if out:
        update_seen_ids(chosen)
        print(f"Wrote digest: {out}")
    else:
        print("No new digest written (maybe already exists, or no new papers).")


if __name__ == "__main__":
    main()
