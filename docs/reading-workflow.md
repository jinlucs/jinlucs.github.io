# Daily research reading workflow

Site: https://jinlucs.github.io/
Repository: https://github.com/jinlucs/jinlucs.github.io (main).
Local checkout: E:\git\jinlucs\jinlucs.github.io.
Timezone: America/New_York. The Codex heartbeat runs daily at 09:00.

Read this file and synchronize the checkout before editing. Preserve unrelated
changes. Never restore the retired abstract-only generator. Its 71 historical
digest posts were removed on 2026-10-24; they remain recoverable in Git history.

## Select and read
Choose one previously uncovered paper relevant to optimization, efficient AI,
federated/distributed learning, or trustworthy systems. Prefer a first public
version within seven days, then extend to 30 days if necessary. Record its actual
publication/version date. Read the full paper, relevant proofs and limitations;
if full text is inaccessible, choose another. Do not invent a new paper or claim
an older work was published today. If no suitable paper is available, preserve
the previous notes and report a skipped update.

## Write
Use English throughout: titles, subtitles, descriptions, body text, comic labels,
captions, alt text, and homepage news. Do not add a Chinese reading guide or
Chinese translations. The user explicitly requires English-only publication.
Use your own reasoning rather than a separate small-model/API summarizer.
Provide a concise source-backed account, then original analysis:
- problem and connection to this research group;
- definitions, assumptions, a key formula, and a checked derivation;
- a reproducible toy example, clearly separate from reported experiments;
- limitations, proof boundaries, and concrete next research questions.
Respect copyright and source word limits. Quote minimally and link original
full text with section/equation locators. Never claim experiments were reproduced
unless they actually were. Obtain an independent review of math and prose.

## Public credit and tone
End each note with the simple credit: "The comic was created with AI."
Use "Research reading notes" as the author label. Do not add reading-date
footers, Codex or ImageGen bylines, QA/process reports, or boilerplate about
experiments that were not run. Keep this process narration out of introductions,
descriptions, and footers. Preserve relevant mathematical assumptions, limits,
and source attribution in the analysis. Keep verification records in local
working files rather than adding production reports to the published note.

## Comic
Use the built-in image generation tool for a four-panel mathematical comic
whose panels correspond to the worked example. Inspect every label, fraction,
arrow and result. Fix errors before publication. Save the final image under
assets/img/reading/ and provide useful alt text plus a text explanation. Preserve
an image-generation prompt beside the asset as a .txt file. Do not publish a
decorative image that substitutes for mathematical explanation.

## Publish
New notes: _posts/YYYY-MM-DD-paper-analysis-SLUG.md.
Front matter must include categories: [paper-analysis], mathjax: true,
source_url, paper_date, comic, comic_alt, description, comments: false,
social-share: false, and author: "Research reading notes".
Use a stable /reading/YYYY-MM-DD-SLUG/ permalink. Do not impersonate the site's
owner as the author of AI-prepared notes. The reading index is arxiv.md.

Local scoped publishing helper:
D:\Chores\homepage-maintenance\publish_reading.py
Use its --help. It accepts article text on stdin and a generated image path.
It can synchronize, validate and publish only reading posts and their assets.
Never print/read credentials, weaken protection, force-push or stage all files.
For changes outside its scope, use normal reviewed file operations.

Check front matter, source links, equations, toy arithmetic, image and mobile
layout; run the repository Jekyll checks in CI. Read back the live page and verify
the matching commit's Pages deployment. If authentication or rendering fails,
retain the draft and report the precise failure; do not claim publication.

## Homepage news
Review Outlook for new confirmed awards, acceptance/publication and research
support. Deduplicate against index.md. Use official decisions and public primary
links when available. Distinguish main conference, Findings, workshop, accepted
and published. Do not expose private reviews, budgets or email links publicly.
Respect any stated embargo/announcement date. Do not send emails. When there is
no new verified news, keep the news unchanged.
