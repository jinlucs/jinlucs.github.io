---
layout: post
title: "When Softmax Loses a Small Gradient"
subtitle: "A worked reading of A Fix for Softmax and Cross-Entropy"
date: 2026-10-25 09:00:00 -0400
permalink: /reading/2026-10-25-softmax-small-gradient/
categories: [paper-analysis]
tags: [optimization, numerical-stability, efficient-learning]
author: "Research reading notes"
description: "An exact binary32 example shows how equivalent cross-entropy formulas produce different gradients, and why a zero-sum check is necessary but insufficient."
source_url: "https://arxiv.org/abs/2610.31642v1"
paper_date: "2026-10-22"
comic: "/assets/img/reading/2026-10-25-softmax-small-gradient.png"
comic_alt: "Four panels: a representable residual r=2^-25 disappears when added to one in binary32; the standard gradient (0,+r) has sum r; retaining the numerator gives (-r,+r) with sum zero."
mathjax: true
comments: false
social-share: false
---

## The paper and the question

Jonathan T. Barron, Dan Gnanapragasam and Michael Tschannen posted *A Fix for Softmax and Cross-Entropy* on 22 October 2026. They study numerical failures in high-confidence classification and near-matching teacher/student predictions, and propose stable reformulations. Their evaluation covers arithmetic-learning and distillation settings; it does not establish universal training acceleration. The margin-equilibrium discussion uses approximate assumptions about optimizer moments and gradient decay. [Full text, Sections 2–7](https://arxiv.org/html/2610.31642v1).

This note examines Section 2's hard-target case through an invariance argument, a worked binary32 example, and practical gradient diagnostics.

## Four panels, one rounding error

![A four-panel comic showing a small gradient surviving until an unstable subtraction removes it](/assets/img/reading/2026-10-25-softmax-small-gradient.png)

*The parcel r is an already-computed, exactly representable residual. Under round-to-nearest binary32 arithmetic, adding it to one loses it. The standard target gradient becomes zero while the other gradient stays positive. Keeping the small numerator restores opposite gradient entries in this toy example.*

## Start with a mathematical invariant

Let z be a vector of K finite logits, t the target class, and L the hard-target cross-entropy. In exact arithmetic,

$$
L(z,t)=\log\left(\sum_{j=1}^{K}e^{z_j}\right)-z_t.
$$

Adding the same scalar c to every logit cannot change this loss:

$$
L(z+c\mathbf{1},t)
=\log\left(e^c\sum_j e^{z_j}\right)-(z_t+c)
=L(z,t).
$$

Differentiating with respect to c at zero gives

$$
\sum_{k=1}^{K}\frac{\partial L}{\partial z_k}=0.
$$

This is a useful implementation check. The gradient should have no component along the common-shift direction. It describes sensitivity to the logits, rather than to every parameter of the network.

For two classes, let m be the target logit's margin over the other logit and set r equal to exp(-m). Then

$$
L=\log(1+r),\qquad
g_t=\frac{1}{1+r}-1=-\frac{r}{1+r},\qquad
g_o=\frac{r}{1+r}.
$$

The two target-gradient expressions are algebraically equal. Their operation sequences can lose different information. This is the key contrast in [Section 2, Equation (3)](https://arxiv.org/html/2610.31642v1#S2).

## An original binary32 calculation

Choose the residual directly:

$$
r=2^{-25}=0.0000000298023223876953125.
$$

We start after exponentiation so that the rounding effect is isolated. We do not assume a binary32 logit can represent the corresponding irrational margin, 25 log(2), exactly.

Assume IEEE binary32 and round to nearest. The next representable number above one is 1 + 2 to the power -23; the midpoint is 1 + 2 to the power -24. Our r is smaller than the midpoint distance. Therefore,

$$
d=\operatorname{fl}_{32}(1+r)=1.
$$

The standard operation sequence computes

$$
\widetilde g_t
=\operatorname{fl}_{32}(1/d-1)=0,\qquad
\widetilde g_o
=\operatorname{fl}_{32}(r/d)=r.
$$

Its gradient sum is r. A small signal has disappeared from only one entry.

Rearrange the target expression before evaluating it:

$$
\widehat g_t
=\operatorname{fl}_{32}(-r/d)=-r,\qquad
\widehat g_o=r.
$$

Now the computed sum is zero. The exact real-valued target gradient remains -r/(1+r); the computed value -r is a floating-point approximation, not a claim of exact real arithmetic.

The forward loss has a related issue: log(d) is zero, while a stable log1p(r) calculation preserves approximately r. The following calculation rounds each operation explicitly:

~~~python
import math
import struct

def f32(x):
    return struct.unpack("<f", struct.pack("<f", x))[0]

r = f32(2.0 ** -25)
d = f32(f32(1.0) + r)
other = f32(r / d)
standard = (f32(f32(1.0 / d) - 1.0), other)
rearranged = (f32(-r / d), other)

assert d == 1.0 and standard[0] == 0.0
assert f32(sum(standard)) == r
assert f32(sum(rearranged)) == 0.0
assert f32(math.log1p(r)) == r
~~~

This verifies the stated operation sequence. It does not model every fused kernel, reduction order or autodifferentiation rule. Python's log1p call is evaluated in binary64 before the result is rounded to binary32.

## Original analysis: zero-sum is necessary, not sufficient

It is tempting to repair a bad gradient by projecting it onto the zero-sum subspace. For two classes the Euclidean projection is

$$
P=I-\frac12\mathbf{1}\mathbf{1}^{\mathsf T},\qquad
P\begin{pmatrix}0\\r\end{pmatrix}
=\begin{pmatrix}-r/2\\r/2\end{pmatrix}.
$$

The sum is now zero, but both entries have roughly half the correct magnitude. Relative to the rearranged vector (-r,r), its Euclidean error is 50 percent. Passing an invariant check cannot establish that the useful gradient signal was recovered.

This suggests two complementary diagnostics for an optimization pipeline. First, check structure: the sum over logit gradients, invariance to a common logit shift, and the expected sign on the target. Second, check magnitude against a higher-precision reference across margins. A tiny absolute error can hide a large relative error when the true gradient itself is tiny.

I would begin with deterministic logits before comparing training curves. Sweep margins through the precision boundary, vary the number of classes, and inspect the actual backward path. Test the deployed kernel and dtype, rather than inferring behavior from a mathematically stable forward formula alone.

For efficient training or model adaptation, this gives a useful attribution question. If an apparent optimizer failure changes when only the loss arithmetic changes, part of the effect belongs to the numerical objective implementation. Label smoothing, soft targets and distributed reductions introduce additional questions; our binary hard-target calculation does not settle them.

## What to carry into research

The paper's broader fix constructs a stable loss through target-relative differences and an appropriate softplus operation; its autodiff path matters. See [Section 2, Equations (6)–(7)](https://arxiv.org/html/2610.31642v1#S2). The one-line rearrangement in our toy is an explanation, not a complete multiclass loss implementation.

A concrete next experiment is to hold initialization, batches, optimizer and learning-rate schedule fixed while changing only the cross-entropy implementation. Record gradient-reference error alongside loss and accuracy. That would distinguish a numerical correction from a change in statistical learning behavior.

The lesson is operational: preserve the small quantity before subtraction destroys it, and verify both the gradient's structure and its scale.

## Sources

- [Version and authors](https://arxiv.org/abs/2610.31642v1), first posted 22 October 2026.
- [Full text](https://arxiv.org/html/2610.31642v1): hard-target reformulation in Section 2; separate soft-target treatment in Section 3; approximate equilibrium analysis in Section 5; evaluations in Sections 6–7.
- [PDF](https://arxiv.org/pdf/2610.31642v1).

The comic was created with AI.
