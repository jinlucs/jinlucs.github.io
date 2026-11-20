---
layout: post
title: "A Silent Gradient Is Not a Finished Run"
subtitle: "Waiting times, confidence and averaging in interpolating SGD"
description: "Exact outcome probabilities distinguish a successful run from a falling mean, and reveal how averaging and mini-batching change the same sample budget."
date: 2026-11-20 09:00:00 -0500
permalink: /reading/2026-11-20-silent-gradient-waiting-time/
categories: [paper-analysis]
mathjax: true
source_url: https://arxiv.org/html/2611.24562v1
paper_date: "2026-11-18"
comic: /assets/img/reading/2026-11-20-silent-gradient-waiting-time.png
comic_alt: "Four panels show Bernoulli gradient sampling, four silent draws with probability 81 over 256, a terminal normalized error of either zero or one, and the seventeen draws needed for at least ninety-nine percent probability of zero terminal error."
author: "Research reading notes"
comments: false
social-share: false
---

A falling mean can hide runs that have made no progress. This matters when a distributed learner sees an informative feature only occasionally: a quiet sequence of updates is weak evidence that optimization has finished. Confidence should describe the outcomes of individual runs, with the sampling budget and the returned model both specified.

Galli, Parletta and Paudice's [*Taming the Tails of Stochastic Gradient Descent in the Interpolation Regime*](https://arxiv.org/abs/2611.24562v1), first public on November 18, studies high-probability SGD guarantees. Its [strongly convex analysis](https://arxiv.org/html/2611.24562v1#S4) trades confidence dependence against exponential decay rate.

## Start with the paper's obstruction

Specialize the [Appendix C.3 construction](https://arxiv.org/html/2611.24562v1#A3.SS3) to

$$
Z\sim\operatorname{Bernoulli}(q),\quad
f(x,Z)=\frac{Zx^2}{2},\quad
F(x)=\mathbb E[f(x,Z)]=\frac{qx^2}{2},\quad 0<q<1.
$$

Draws are independent. Both sample losses are convex and 1-smooth, with common minimizer zero: interpolation. Population strong convexity is $$\mu=q$$. The stochastic condition number $$\kappa=L/\mu=1/q$$ uses sample smoothness $$L=1$$. The population quadratic alone has condition number one.

The construction is the authors'; the calculations below extend it.

## An exact law for one run

Start at $$x_0=1$$ and take step size $$\eta=1$$. Index $$x_n$$ after exactly $$n$$ updates. Let $$T$$ be the first draw with $$Z=1$$. A zero draw leaves the parameter unchanged; a one draw sends it to zero permanently. Define normalized population error $$R_n=F(x_n)/F(x_0)$$. Then

$$
x_{k+1}=(1-Z_{k+1})x_k,\qquad
R_n=x_n^2=\mathbf 1_{\{T>n\}}.
$$

Write $$a=1-q$$. Consequently $$\mathbb P(R_n=1)=a^n$$, $$\mathbb P(R_n=0)=1-a^n$$, and $$\mathbb E[R_n]=a^n$$. The mean is an exponentially falling probability of complete stagnation. No individual run has the intermediate error shown by that mean.

For $$q=1/4$$ and four updates, the exact probabilities are $$81/256$$ for error one and $$175/256$$ for error zero. Thus the mean normalized error is about $$0.3164$$, while roughly $$31.64\%$$ of runs retain their entire initial error. These are probabilities, not counts from a simulation.

![{{ page.comic_alt }}]({{ page.comic | relative_url }})

Independent draws, unit steps; success means a zero last iterate.

For any fixed threshold $$0\leq\epsilon<1$$, success means $$R_n\leq\epsilon$$, which here is exactly $$R_n=0$$. Requiring success probability at least $$1-\beta$$ gives the exact sample budget

$$
a^n\leq\beta
\quad\Longleftrightarrow\quad
n\geq\left\lceil\frac{\log\beta}{\log a}\right\rceil.
$$

At $$q=1/4$$ and $$\beta=0.01$$, sixteen draws leave probability $$0.0100225958$$ of no progress, just above one percent. Seventeen reduce it to $$0.0075169468$$. Seventeen is therefore the smallest integer budget giving at least 99 percent success. For small $$q$$, the budget scales as $$\log(1/\beta)/q$$: waiting for useful information determines this confidence cost.

There is also a useful check on moment bounds. Since $$R_n$$ is binary, $$\mathbb E[R_n^{1/p}]=a^n$$ for every $$0<p\leq1$$. Applying Markov's inequality to that moment gives

$$
\mathbb P\!\left(R_n>\beta^{-p}a^{pn}\right)\leq\beta.
$$

If $$a^n>\beta$$, the stated error bound exceeds one and says nothing beyond the deterministic bound. Decreasing $$p$$ cannot turn those same draws into a success guarantee. This exact toy calculation explains the confidence-versus-decay tension; its sharp normalization is specific to this problem, not the paper's general prefactor.

## Averaging remembers the wait

Return instead the average of the parameters before each of the first $$n$$ updates, $$\bar x_n=n^{-1}\sum_{k=0}^{n-1}x_k$$. There are exactly $$\min(T,n)$$ ones in this sum. Its normalized population error is therefore

$$
\frac{F(\bar x_n)}{F(x_0)}
=\left(\frac{\min(T,n)}{n}\right)^2,
\qquad
\mathbb E\!\left[\frac{F(\bar x_n)}{F(x_0)}\right]
=\frac{1}{n^2}\sum_{t=1}^{n}(2t-1)a^{t-1}.
$$

The expectation follows by writing any nonnegative integer square as the sum of its first odd numbers, then using $$\mathbb P(T\geq t)=a^{t-1}$$. For four draws with $$q=1/4$$ it equals $$577/1024\approx0.5635$$, compared with $$81/256\approx0.3164$$ for the last iterate. A useful first draw solves the last iterate immediately, but the average still includes $$x_0$$. Indeed, for fixed positive $$q$$, its mean normalized error is asymptotic to $$(2-q)/(q^2n^2)$$ because $$\mathbb E[T^2]=(2-q)/q^2$$. Averaging changes the law of the returned error, even with identical updates.

## Four samples do not determine four updates

Consider a batch of $$b$$ independent samples and one update using their **mean** gradient, still with step size one. If $$B\sim\operatorname{Binomial}(b,q)$$ counts the useful samples, then

$$
x^+=\left(1-\frac{B}{b}\right)x,\qquad
\mathbb E[(x^+/x)^2]=(1-q)^2+\frac{q(1-q)}{b}\quad(x\ne0).
$$

This follows from $$\mathbb E[B/b]=q$$ and $$\operatorname{Var}(B/b)=q(1-q)/b$$. With four samples and $$q=1/4$$, one batch update has mean normalized error $$39/64\approx0.6094$$. Four sequential updates have mean error $$81/256\approx0.3164$$. Both have probability $$81/256$$ of seeing no useful sample, but one useful sample only partially moves the batch update. Equal coverage does not imply equal optimization progress.

Changing the sampler can change coverage itself. For a finite population of four records with exactly one useful record, uniform sampling without replacement has miss probability $$(4-n)/4$$ for $$0\leq n\leq4$$. Four draws guarantee coverage; independent sampling with replacement misses with probability $$81/256$$. This comparison changes the sampling model and lies outside the independent-draw calculation.

## What I would measure next

For federated optimization, I would log a coverage statistic for each important feature or client group alongside loss quantiles. A mean learning curve cannot distinguish many fully solved runs from a substantial minority that never received useful information. Compare samplers at equal sample and communication budgets, and report which model is returned. The batch calculation shows why counting only successful contacts is insufficient.

This scalar example has bounded random gradients along its trajectory. The tail under discussion is the distribution of optimization error, not a requirement for heavy-tailed gradient noise. Common minimizers and independent draws are substantive assumptions; neither follows from small average training loss. Heterogeneous clients may have incompatible minima, and an informative client need not solve a realistic model in one step. A concrete next question is whether coverage-aware scheduling improves upper error quantiles under a fixed communication budget while preserving the intended population weighting.

The comic was created with AI.
