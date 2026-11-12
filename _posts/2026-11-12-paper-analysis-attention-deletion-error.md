---
layout: post
title: "Removing More Attention Can Change Less"
subtitle: "How softmax renormalization changes the cost of dropping a block"
description: "Three attention blocks show why a large mass can be harmless to delete, a zero-valued block can matter, and two removal errors can cancel."
date: 2026-11-12 09:00:00 -0500
permalink: /reading/2026-11-12-attention-deletion-error/
categories: [paper-analysis]
mathjax: true
source_url: https://arxiv.org/html/2611.13578v1
paper_date: "2026-11-10"
comic: /assets/img/reading/2026-11-12-attention-deletion-error.png
comic_alt: "Four panels show attention blocks A, B, C with masses (1/2, 1/4, 1/4), values (2, 0, 4) and dense output 2. Removing A leaves output 2. Removing B gives output 8/3 and absolute error 2/3. Removing B and C together leaves output 2 because their signed deviations cancel."
author: "Research reading notes"
comments: false
social-share: false
---

A block can carry half of an attention head's probability mass and still be harmless to remove for a particular query. The remaining weights grow when softmax is recomputed, and that growth can replace the deleted block's contribution exactly. POEM uses this observation to design a block score for long-context prefilling. It adds a block's deviation from the dense output to the mass information used by a cheaper candidate selector. The distinction matters for efficient inference because a selector must decide what to skip before computing dense attention. [Wu et al., *POEM: Output-Relative Block-Sparse Attention for Long-Context Prefilling*, arXiv:2611.13578v1](https://arxiv.org/html/2611.13578v1#S4.SS1).

Fix one query and one head. Let $$m_b$$ be the dense attention mass of visible block $$b$$, with $$\sum_bm_b=1$$. Let $$v_b$$ be its attention-weighted mean value, so the dense output is $$o=\sum_bm_bv_b$$. For a discarded set $$D$$ with total mass $$\delta=\sum_{b\in D}m_b<1$$, the remaining blocks produce $$\widetilde o=(o-\sum_{b\in D}m_bv_b)/(1-\delta)$$. Subtracting this expression from $$o$$ gives

$$
o-\widetilde o
=\frac{\sum_{b\in D}m_b(v_b-o)}{1-\delta}.
$$

This is a vector identity. Its numerator sums the signed deviations before taking any norm. For one discarded block, the exact norm of the error is $$m_b\lVert v_b-o\rVert/(1-m_b)$$. For several blocks, directions and cancellation enter as well. [Section 4.1, Equation (3)](https://arxiv.org/html/2611.13578v1#S4.E3), [Appendix A.2](https://arxiv.org/html/2611.13578v1#A1.SS2).

Take three visible blocks with scalar values. Their mass–value pairs are $$A=(1/2,2)$$, $$B=(1/4,0)$$ and $$C=(1/4,4)$$. One token per block realizes this example exactly with attention logits $$(\log2,0,0)$$. The dense output is $$o=(1/2)2+(1/4)0+(1/4)4=2$$. The following removals are illustrative choices for that head. POEM's mandatory blocks and threshold rules further restrict its actual selections.

- **Remove A.** The retained mass is $$1/2$$ and the retained weighted sum is $$1$$. Renormalizing gives output $$2$$, so the error is zero. A carried the largest mass, but its value matched the dense output.
- **Remove B.** The retained mass is $$3/4$$ and the weighted sum remains $$2$$. The sparse output is $$8/3$$ and the absolute error is $$2/3$$. B's weighted value contribution was zero, yet its presence in the softmax denominator mattered.
- **Remove B and C.** The retained mass is $$1/2$$ and A alone again gives output $$2$$. The removed signed deviations are $$-1/2$$ and $$1/2$$, which cancel exactly.

![{{ page.comic_alt }}]({{ page.comic | relative_url }})

The first comparison holds the number of deleted blocks fixed. Removing more probability mass causes less error. The last comparison holds the deleted mass at $$1/2$$ but uses a different subset. It shows why individual removal errors cannot simply be added to predict the joint result.

A second check is to add the same vector $$c$$ to every value. Both dense and sparse outputs increase by $$c$$, leaving their difference unchanged. The deviations $$v_b-o$$ also stay unchanged. In the scalar toy, adding ten changes the values to $$(12,10,14)$$ and the dense output to $$12$$. Removing B now gives sparse output $$38/3$$, still an absolute error of $$2/3$$. A score based on the raw value contribution changes under this shift, while the exact deletion error remains invariant.

POEM motivates its per-block importance proxy $$I_b=m_b\lVert v_b-o\rVert$$ with the triangle inequality

$$
\lVert o-\widetilde o\rVert
\leq\frac{\sum_{b\in D}I_b}{1-\delta}.
$$

For the toy, these scores are $$(0,1/2,1/2)$$. For singleton removals they agree with the exact errors after division by the retained mass. For deleting B and C, the bound is $$2$$ although the actual error is zero. The bound sacrifices cancellation to make separate block scores possible. Its denominator also depends on which blocks are retained, so using the numerator alone assumes that retained masses are sufficiently comparable. [Equation (4)](https://arxiv.org/html/2611.13578v1#S4.E4).

Practical POEM estimates the dense reference and block outputs, preselects candidates by mass, then reranks candidates using an approximate log mass plus a weighted log deviation. The weight is tuned, and the retention threshold accumulates pooled attention masses in that new order. These approximations make the exact identity a guide for the selector. [Equation (6) and the selection procedure](https://arxiv.org/html/2611.13578v1#S4.E6), [Appendix B](https://arxiv.org/html/2611.13578v1#A2).

The proof connecting attention output to final prediction KL divergence is local. It perturbs one layer, assumes a smooth downstream map and keeps a cubic remainder in the output perturbation norm. Cross-head errors are then bounded with projection norms. This supports sensitivity-aware calibration while leaving whole-model behavior to empirical evaluation. [Appendix A.1](https://arxiv.org/html/2611.13578v1#A1.SS1).

On Qwen3-8B at 128K, the authors report attention latency, including selection, falling from 928.0 to 143.9 ms. The RULER score for that model and length falls from 75.29 to 72.71. These paired results describe the measured quality–latency tradeoff. [Section 5 and Figure 5](https://arxiv.org/html/2611.13578v1#S5).

I would evaluate the selector on queries with nearly canceling block deviations, recording exact head error at matched **actual retained mass** as well as matched block count. Separate candidates excluded by the first stage from candidates misranked by the second stage. The toy suggests a further experiment with block pairs whose signed deviations cancel. Any benefit would have to exceed the cost of finding those pairs, so the final comparison should include selection time and full-model prefill latency alongside attention latency.

The comic was created with AI.
