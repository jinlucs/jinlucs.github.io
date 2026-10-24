---
layout: page
title: Research Reading Notes
subtitle: One paper, worked mathematics, and a visual explanation
permalink: /arxiv/
---

Recent work in machine learning, optimization, and distributed learning, read in depth. Each note links to the original paper and distinguishes the authors' claims from our own calculations and research questions.

{% assign reading_posts = site.posts | where_exp: "p", "p.categories contains 'paper-analysis'" | sort: "date" | reverse %}

{% if reading_posts.size > 0 %}
<div class="reading-list">
{% for post in reading_posts %}
<article class="reading-card">
  <p class="reading-date">{{ post.date | date: "%B %-d, %Y" }} · Paper published {{ post.paper_date }}</p>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p>{{ post.description }}</p>
  {% if post.comic %}<a href="{{ post.url | relative_url }}" aria-label="Read {{ post.title | escape }}"><img src="{{ post.comic | relative_url }}" alt="{{ post.comic_alt | escape }}" loading="lazy" /></a>{% endif %}
  <p><a href="{{ post.url | relative_url }}">Read the analysis and worked example &rarr;</a> · <a href="{{ post.source_url }}" rel="noopener">Original paper</a></p>
</article>
{% endfor %}
</div>
{% else %}
<p>The next reading note will appear here after the paper and its mathematics have been checked.</p>
{% endif %}
