---
layout: page
title: Papers
permalink: /papers/
---

<p>
  This page is auto-generated from my BibTeX file.
  <a href="/assets/bib/publications.bib">Download BibTeX</a>
</p>

{% assign pubs = site.data.publications | sort: "sort_key" | reverse %}
{% assign pubs_by_year = pubs | group_by: "year" %}

{% for y in pubs_by_year %}
### {{ y.name }}

<ul>
{% for p in y.items %}
  <li>
    {% if p.url %}
      <a href="{{ p.url }}">{{ p.title }}</a>
    {% else %}
      {{ p.title }}
    {% endif %}
    <br/>
    {{ p.authors_html }}
    {% if p.venue and p.venue != "" %}
      <br/><em>{{ p.venue }}</em>
    {% endif %}
    {% if p.note and p.note != "" %}
      — {{ p.note }}
    {% endif %}
  </li>
{% endfor %}
</ul>

{% endfor %}
