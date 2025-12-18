from pathlib import Path
import json
from semanticscholar import SemanticScholar

# TODO: put your own author ID here:
AUTHOR_ID = "1234567"   # from your Semantic Scholar profile URL

def fetch_publications():
    sch = SemanticScholar()  # uses public API

    author = sch.get_author(AUTHOR_ID)
    pubs = []

    # author.papers is a list of paper objects
    for paper in author.papers:
        pubs.append({
            "title": paper.title,
            "year": paper.year,
            "venue": getattr(paper, "venue", None),
            "authors": [a.name for a in paper.authors],
            "paperId": paper.paperId,
            "doi": getattr(paper, "doi", None),
            "url": paper.url,
        })

    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    out_path = data_dir / "publications.json"

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(pubs, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(pubs)} publications to {out_path}")

if __name__ == "__main__":
    fetch_publications()
