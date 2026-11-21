---
layout: post
title: "Lower Loss, Farther from the Solution"
subtitle: "An exact norm-ball step separates objective decrease from distance decrease"
description: "A smooth quadratic and a unique local step lower the loss while increasing two distances to the optimum. Exact arithmetic identifies the geometry and a usable descent guarantee."
date: 2026-11-21 09:00:00 -0500
permalink: /reading/2026-11-21-lower-loss-greater-distance/
categories: [paper-analysis]
mathjax: true
source_url: https://arxiv.org/html/2611.24645v1
paper_date: "2026-11-18"
comic: /assets/img/reading/2026-11-21-lower-loss-greater-distance.png
comic_alt: "Four panels define a positive definite quadratic, take its exact ell-four norm-ball step, show the loss falling from three to 1.645, and show the fourth power of ell-four distance rising from seventeen to 19.8577 and squared Euclidean distance from five to 5.05."
author: "Research reading notes"
comments: false
social-share: false
---

Changing an optimizer's step geometry changes what its direction optimizes. In distributed learning, a bound on parameter movement can be useful for communication or stability. It does not automatically make distance to a solution decrease. A small example separates that distance from both the loss and the linear improvement promised by the update.

Richtárik and Qian's [*Broximal Gradient Descent in General Norms: Convergence without Fejér Monotonicity*](https://arxiv.org/abs/2611.24645v1), first public on November 18, analyzes exact local linear minimization in a chosen norm. Its [one-step analysis](https://arxiv.org/html/2611.24645v1#S2) uses objective comparisons and stationarity certificates.

For a closed convex feasible set $$C$$ and radius $$r>0$$, the update is

$$
x^+\in\operatorname*{arg\,min}_{u\in C,\;\lVert u-x\rVert\leq r}
\langle\nabla f(x),u-x\rangle.
$$

## A quadratic with a unique answer

Here is a separate constructed example. Work in $$C=\mathbb R^2$$ with $$\lVert z\rVert_4=(\lvert z_1\rvert^4+\lvert z_2\rvert^4)^{1/4}$$ and

$$
f(z)=\frac12z^\top Hz,\qquad
H=\begin{pmatrix}14&-3\\-3&1\end{pmatrix},\qquad
x=\begin{pmatrix}1\\2\end{pmatrix}.
$$

The leading principal minor is 14 and the determinant is 5, so $$H$$ is positive definite. The unique minimizer is $$x_\star=0$$, the initial loss is $$f(x)=3$$, and the gradient is $$g=Hx=(8,-1)^\top$$.

Choose $$r=17^{1/4}/10$$. The dual of the fourth norm is the $$4/3$$ norm, so $$\lVert g\rVert_{4/3}=(8^{4/3}+1)^{3/4}=17^{3/4}$$. Hölder's inequality bounds every allowed displacement $$h$$ by $$g^\top h\geq-r\lVert g\rVert_{4/3}=-17/10$$. Equality is attained at

$$
h=\begin{pmatrix}-1/5\\1/10\end{pmatrix},\qquad
\lVert h\rVert_4^4=\frac{17}{10000},\qquad
g^\top h=-\frac{17}{10},\qquad
x^+=\begin{pmatrix}4/5\\21/10\end{pmatrix}.
$$

Indeed, the gradient coordinates are the cubes of $$(2,-1)$$, giving exactly the equality direction in Hölder's inequality. The fourth-norm ball is strictly convex, so this nonzero linear functional has a unique minimizer. No tie-breaking choice causes the effect.

![{{ page.comic_alt }}]({{ page.comic | relative_url }})

The two distance cards use powers of distances; both powers are strictly increasing functions of distance.

The loss after this exact step is $$f(x^+)=329/200=1.645$$. Yet the fourth power of the chosen-norm distance rises from $$17$$ to $$198577/10000=19.8577$$, and squared Euclidean distance rises from $$5$$ to $$101/20=5.05$$. Thus the endpoint is farther from the same unique solution in both norms.

## The effect survives smaller radii

Keep this center and linearization, and parameterize the exact oracle displacement by $$h(t)=t(-2,1)^\top$$, whose radius is $$r(t)=17^{1/4}t$$. Direct expansion gives

$$
\begin{aligned}
f(x+h(t))&=3-17t+\frac{69}{2}t^2,\\
\lVert x+h(t)\rVert_2^2&=5+5t^2,\\
\lVert x+h(t)\rVert_4^4&=17+24t+48t^2-24t^3+17t^4.
\end{aligned}
$$

For every $$0<t\leq1/10$$, the loss decreases and both distances increase. For the last inequality, $$48t^2-24t^3\geq0$$ on this interval and the other added terms are positive. Euclidean distance increases only at second order: $$x^\top(-2,1)=0$$, so the displacement is tangent to the Euclidean sphere at the starting point. The chosen-norm distance already increases at first order. Reducing the radius cannot restore distance monotonicity here.

Along this fixed ray, the loss stays below its starting value for $$0<t<34/69$$ and reaches its minimum at $$t=17/69$$. Our choice $$t=1/10$$ precedes that ray minimum. Also $$r\lVert g\rVert_{4/3}=17/10<g^\top x=6$$. The example has neither an excessively long step along its descent ray nor a violated analogue of the usual radius-to-solution comparison. Future iterations would recompute the gradient and direction; this ray calculation does not describe their trajectory.

## A guarantee that can actually be checked

[Lemma 6](https://arxiv.org/html/2611.24645v1#Thmtheorem6) bounds the new loss using model decrease $$d=-g^\top h$$ and a valid quadratic upper-model constant $$L$$:

$$
f(x^+)\leq f(x)-d+\frac{L}{2}r^2.
$$

For our quadratic, take the conservative constant $$L=15\sqrt2$$. Since $$H$$ is positive definite with trace 15, every displacement $$z$$ satisfies $$z^\top Hz\leq15\lVert z\rVert_2^2\leq15\sqrt2\lVert z\rVert_4^2$$. Taylor's formula is exact for this quadratic, which proves the required upper model globally. Substituting the observed $$d=17/10$$ and our radius gives

$$
f(x^+)\leq\frac{13}{10}+\frac{3\sqrt{34}}{40}
\approx1.73732<3.
$$

The bound certifies descent and safely contains the exact value 1.645. It needs the gradient, the step, the radius and a valid curvature bound. Distance to the unknown optimum is absent. The new gradient is $$(49/10,-3/10)^\top$$, so this particular endpoint still has a nonzero stationarity residual.

Convergence conclusions require a complete radius schedule. [Corollary 13](https://arxiv.org/html/2611.24645v1#Thmtheorem13) gives value convergence for convex objectives with a quadratic upper model when $$\sum_k r_k=\infty$$ and $$\sum_k r_k^2<\infty$$. For example, continue the exact method with $$r_k=r/(k+1)$$. In this quadratic, $$H-\tfrac13I$$ is positive definite: its leading minor is $$41/3$$ and determinant $$1/9$$. Consequently $$\lVert x_k\rVert_2^2\leq6f(x_k)\to0$$. The first step moves farther away, while that full schedule ultimately converges to zero. One-step distance increase is compatible with eventual convergence.

## What this changes in an optimizer comparison

For a communication-limited learner, I would report the chosen norm, radius budget, actual loss change and a stationarity measure together. Step length constrains movement around the current model; it does not directly constrain movement relative to the solution. The example also shows why a coordinate-based direction should be evaluated against the objective's curvature: the parameter-space measuring tape and the quadratic's loss contours encode different geometry.

The calculation assumes exact gradients and an exact local oracle. Inexact solves, stochastic noise and coupled client constraints require additional error terms. A local linear solve can also be expensive, so an oracle-call guarantee alone cannot establish lower wall-clock or communication cost. Our fourth-norm ball is strictly convex, but its squared norm is not strongly convex; the example makes no stronger claim about that norm property.

A concrete next experiment is to compare two geometries under the same communicated update budget, log both realized model decrease and the curvature remainder, and check whether an inexpensive local solver preserves the descent certificate. That would test whether a geometry helps optimization in the intended system, beyond making individual parameter movements look favorable.

The comic was created with AI.
