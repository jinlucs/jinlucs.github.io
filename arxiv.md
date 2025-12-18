---
layout: page
title: Daily arXiv Digest
permalink: /arxiv/
---

Daily ML + Optimization papers (auto-generated).

<ul>
{% assign posts = site.categories.arxiv | sort: "date" | reverse %}
{% for post in posts limit: 60 %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%Y-%m-%d" }})</small>
  </li>
{% endfor %}
</ul>
