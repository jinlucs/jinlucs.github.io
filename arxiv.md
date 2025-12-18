---
layout: page
title: Daily arXiv Digest
permalink: /arxiv/
---

Daily ML + Optimization papers (auto-generated).

{% assign arxiv_posts = site.posts | where_exp: "p", "p.categories contains 'arxiv'" %}

{% if arxiv_posts and arxiv_posts.size > 0 %}
  {% assign arxiv_posts = arxiv_posts | sort: "date" | reverse %}

  <ul>
  {% for post in arxiv_posts limit: 60 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>({{ post.date | date: "%Y-%m-%d" }})</small>
    </li>
  {% endfor %}
  </ul>
{% else %}
  <p><strong>No digests yet.</strong></p>
  <p>
    Once your GitHub Action creates the first <code>_posts/YYYY-MM-DD-arxiv-digest.md</code>
    with <code>categories: [arxiv]</code>, they will appear here automatically.
  </p>
{% endif %}
