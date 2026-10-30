---
layout: post
title: "How an Optimizer Can Undo a Gradient Projection"
subtitle: "Two coordinates show why the realized step matters"
date: 2026-10-30 09:00:00 -0400
permalink: /reading/2026-10-30-project-the-update/
categories: [paper-analysis]
tags: [optimization, machine-unlearning, trustworthy-ai]
author: "Research reading notes"
description: "An exact two-coordinate example shows how diagonal rescaling can break a projected gradient's protection, and how projecting the full proposed change restores the linear constraint."
source_url: "https://arxiv.org/abs/2610.40483v1"
paper_date: "2026-10-29"
comic: "/assets/img/reading/2026-10-30-project-the-update.png"
comic_alt: "A protected linear response starts at 2. Projecting gradient (3,1) gives (1,-1), preserving it under SGD. Rescaling to (1,-2) changes the response to 2.25. Projecting that proposed direction gives (3/2,-3/2) and preserves 2."
mathjax: true
comments: false
social-share: false
---

## The paper and the question

Juan Belieni and colleagues posted *Preserving Utility in Continual LLM Unlearning via Orthogonal Projections* on 29 October 2026. Their COP method caches activation directions from earlier deletion requests and projects later gradients away from them. [Full paper](https://arxiv.org/html/2610.40483v1).

The geometry raises an implementation question: does a protected gradient remain protected after the optimizer transforms it? The following original two-coordinate example separates the gradient from the parameter change actually applied.

## Four panels, one response

![A four-panel mathematical comic showing projection, subsequent coordinate rescaling, and projection of the full proposed direction](/assets/img/reading/2026-10-30-project-the-update.png)

*The anchored response is 2. Projected SGD preserves it. A diagonal rescaling after projection moves it to 2.25. Reprojecting the proposed direction restores the nulling condition.*

## State the condition on the change

For an orthonormal activation basis V, the paper projects a layer gradient as G(I-VV^T). Its exact persistence theorem requires the applied weight change to annihilate protected activations, with nested subspaces, complete per-layer coverage and all trainable parameters being projected linear weights. [Equation (9), Theorem 1 and Appendix E](https://arxiv.org/html/2610.40483v1#S3.SS2).

Our example uses a single linear response

$$
y(w)=w^\top h,\qquad
w=\begin{pmatrix}2\\0\end{pmatrix},\qquad
h=\begin{pmatrix}1\\1\end{pmatrix}.
$$

All vectors are columns; transposing w gives one weight row in the paper's convention. The initial response is two. Treat it as an abstract anchor after an earlier request.

A parameter change preserves this response exactly when

$$
y(w+\Delta w)-y(w)=h^\top\Delta w=0.
$$

There is no Taylor remainder for this linear model. The constraint applies to the parameter change, regardless of how an optimizer constructed it.

## Project onto the allowed line

The orthogonal projector onto the directions perpendicular to h is

$$
Q=I-\frac{hh^\top}{h^\top h}
=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
$$

It is symmetric, satisfies Q^2=Q and sends h to zero. Its allowed directions have coordinates that sum to zero.

Take a gradient g=(3,1)^T. Projection gives

$$
Qg=\begin{pmatrix}1\\-1\end{pmatrix},
\qquad h^\top Qg=0.
$$

With step size eta=1/4, projected SGD produces weights (7/4,1/4)^T. Their sum remains two. Projection works because the applied change is exactly a scalar multiple of the projected gradient.

## Rescaling can reintroduce the removed direction

Now place a positive diagonal operator after the projection:

$$
D=\begin{pmatrix}1&0\\0&2\end{pmatrix},
\qquad
v=DQg=\begin{pmatrix}1\\-2\end{pmatrix}.
$$

D is fixed and has no moment state. This example isolates coordinatewise rescaling.

The new direction has inner product -1 with h. Applying it gives

$$
w_{\rm scaled}=w-\frac14v
=\begin{pmatrix}7/4\\1/2\end{pmatrix},
\qquad
y(w_{\rm scaled})=\frac94=2.25.
$$

The protected response changed by one quarter even though the gradient before rescaling passed the orthogonality test.

For this h and a general diagonal D=diag(d_1,d_2), the leakage is

$$
h^\top DQg=\frac{(d_1-d_2)(g_1-g_2)}2.
$$

Equal coordinate scaling preserves the allowed line. Unequal scaling can move a nonzero projected direction out of it. The order of these operations therefore matters.

## Project the full proposed direction

Applying Q to v gives

$$
Qv=\begin{pmatrix}3/2\\-3/2\end{pmatrix},
\qquad h^\top Qv=0.
$$

The resulting weights are (13/8,3/8)^T and the response is two. This fixes the particular rescaling leak in our example.

It also has a precise geometric interpretation. Among all directions u satisfying h-transpose u=0, Qv is the closest to v in Euclidean norm. Decompose v into its perpendicular and parallel components. For any feasible u, orthogonality yields

$$
\|v-u\|^2
=\|(I-Q)v\|^2+\|Qv-u\|^2.
$$

Only the second term depends on u, and it vanishes at u=Qv. This is a projection of the optimizer's proposed change onto the constraint set; it does not establish convergence of the resulting optimization method.

The same requirement includes every contribution to that proposed change. For instance, a separate weight-decay change -eta*gamma*w changes this response by -eta*gamma*y(w), even when the gradient contribution is orthogonal to h. Leaving decay outside the final constraint can therefore create another leak.

## Compare the actual weight changes

| Applied direction | New weights | Response |
|---|---|---:|
| Qg | (7/4, 1/4) | 2 |
| DQg | (7/4, 1/2) | 2.25 |
| QDQg | (13/8, 3/8) | 2 |

All rows use the same starting weights, input, gradient and step size.

~~~python
from fractions import Fraction as F

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def project(v):
    a = (v[0]-v[1])/2
    return a, -a

w, h, g = (F(2), F(0)), (F(1), F(1)), (F(3), F(1))
eta = F(1, 4)
qg = project(g)
scaled = qg[0], 2*qg[1]
final = project(scaled)

assert qg == (F(1), F(-1))
assert scaled == (F(1), F(-2))
assert final == (F(3, 2), F(-3, 2))

def updated_response(direction):
    new_w = tuple(a-eta*b for a, b in zip(w, direction))
    return dot(h, new_w)

assert updated_response(qg) == 2
assert updated_response(scaled) == F(9, 4)
assert updated_response(final) == 2
~~~

## Separate the exact statement from practical coverage

The source explicitly notes that its experiments project raw gradients before AdamW and weight decay, use compressed bases and leave some parameter types unprojected. Its Limitations describe the resulting protection as approximate. [Section 3.2 and Limitations](https://arxiv.org/html/2610.40483v1).

Our single-layer calculation addresses the order of projection and rescaling. Projecting the realized change does not recover activation directions discarded by compression, constrain other unprotected parameters, or establish preservation on new paraphrases.

There is another boundary in what is being preserved: an anchored output is whatever the earlier request achieved. Keeping it fixed does not establish that the earlier deletion succeeded. In our example, the number two carries no semantic claim about forgetting.

A constraint can also remove useful update directions. Preserving one response is an algebraic property; whether that constraint leaves enough room for a new request is a separate learning question.

## What I would inspect in an unlearning implementation

I would measure the nulling residual on the realized parameter difference after each complete optimizer step. A zero residual on the raw gradient cannot rule out changes introduced by rescaling, momentum or decay. The measurement should use the full parameter change and the protected basis.

Next, I would distinguish two failures: an applied update that violates its stored constraints, and an example whose relevant activations were never fully represented. Improving the first does not resolve the second. Report basis coverage and remaining update capacity alongside the residual.

Finally, I would compare forgetting and utility over a longer stream of requests while varying the basis budget. The useful research question is whether stronger protection preserves earlier outcomes without blocking later changes, rather than whether a projection formula is satisfied in isolation.

## Sources

- Belieni, Erthal, da Silva and Mesquita, [*Preserving Utility in Continual LLM Unlearning via Orthogonal Projections*, v1](https://arxiv.org/abs/2610.40483v1), first posted 29 October 2026.
- [Full text and proof](https://arxiv.org/html/2610.40483v1): Section 3.2; Theorem 1; Appendix E; Limitations.
- [PDF](https://arxiv.org/pdf/2610.40483v1).

The comic was created with AI.

