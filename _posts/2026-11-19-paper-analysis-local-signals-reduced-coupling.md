---
layout: post
title: "When Local Signals Add Up to Too Much"
subtitle: "What a reduced collaboration space can miss in vertical ridge regression"
description: "Two feature holders share a small predictive direction. An exact ridge example shows why spectral projection can discard it, why full local fits can overcount it, and how an omitted coupling controls the resulting error."
date: 2026-11-19 09:00:00 -0500
permalink: /reading/2026-11-19-local-signals-reduced-coupling/
categories: [paper-analysis]
mathjax: true
source_url: https://arxiv.org/html/2611.24367v1
paper_date: "2026-11-18"
comic: /assets/img/reading/2026-11-19-local-signals-reduced-coupling.png
comic_alt: "Four panels show two parties with large local feature directions and one small shared target direction, a projected head predicting zero, reduced-coupling local fits adding to four thirds of the target, and signal-direction collaboration recovering the full ridge prediction of four fifths."
author: "Research reading notes"
comments: false
social-share: false
---

In vertical federated learning, different parties hold different features for the same aligned records. Reducing collaboration changes which relationships between those features are represented. A useful local feature can survive compression of the communication space while its correlation with another party's feature disappears. The resulting local predictions can then add up to too much.

Huang and colleagues' [*VAFL: A Vertical Analytic Federated Learning Mechanism for Efficient Crowdsourced Services via Closed-Form Solutions*](https://arxiv.org/abs/2611.24367v1), first public on November 18, fits ridge heads on fixed representations. [Section 4.3](https://arxiv.org/html/2611.24367v1#S4.SS3) separates an equivalent full-dimensional solve, local projection with coefficient lifting, and full local fitting with reduced cross-party correction (LC). Full-dimensional equivalence assumes the same representations, targets and penalty. Reduced-rank methods approximate different parts of that problem.

Use a scalar response $$y$$, feature matrix $$X=[X_A,X_B]$$ and positive penalty $$\lambda$$. The unaveraged ridge objective and its normal equation are

$$
J(w)=\lVert y-Xw\rVert^2+\lambda\lVert w\rVert^2,
\qquad Gw^*=h,
\qquad G=X^\top X+\lambda I,\quad h=X^\top y.
$$

Positive $$\lambda$$ makes $$G$$ positive definite, so the solution is unique. A block factorization solves the same system without forming its full inverse, preserving the optimum in exact arithmetic.

Consider our three-record example. Let $$e_1,e_2,e_3$$ be the standard orthonormal basis of $$\mathbb R^3$$, and set

$$
X_A=[4e_1,e_3],\qquad X_B=[4e_2,e_3],\qquad y=e_3,\qquad\lambda=\frac12.
$$

These are fixed, uncentered representations with no intercept and no further rescaling. The objective uses a sum of squared errors, rather than an average. Each party has a large direction unrelated to the target and a smaller direction equal to the target. Its local feature Gram matrix is $$\operatorname{diag}(16,1)$$.

The two large columns are orthogonal to everything relevant to fitting $$y$$, so their optimal coefficients are zero. Let $$a,b$$ denote the coefficients on the two copies of $$e_3$$. Full ridge fitting reduces to

$$
\begin{pmatrix}3/2&1\\1&3/2\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}
=\begin{pmatrix}1\\1\end{pmatrix},
\qquad a=b=\frac25,
\qquad \widehat y_{\rm full}=\frac45y.
$$

The off-diagonal ones encode the shared direction. They tell the joint fit that the two features overlap. The prediction shrinks below $$y$$ because of the positive ridge penalty. Its squared fitting error is $$1/25$$, its penalty is $$4/25$$, and $$J(w^*)=1/5$$.

Now retain the leading eigenvector of each local feature Gram matrix, one direction per party. This selects $$4e_1$$ and $$4e_2$$. The retained fraction of each Gram trace is $$16/17$$, but neither column correlates with $$y$$. Projected ridge fitting therefore gives zero coefficients and $$\widehat y_{\rm proj}=0$$. Lifting those coefficients back to the original coordinates preserves that zero predictor. Its objective is one.

The point is about uncentered Gram energy, not automatically mean-centered PCA variance. Replacing the amplitude four by any $$c>1$$ makes the retained fraction $$c^2/(c^2+1)$$. It approaches one as $$c$$ grows, while the projected prediction stays zero. An arbitrarily high energy-retention percentage can coexist with losing the entire target direction in this family.

LC preserves more local information. Its [coefficient recovery formula](https://arxiv.org/html/2611.24367v1#S4.SS3) combines a full local ridge fit with a correction in a chosen collaboration subspace. The local maps are normalized in the regularized local Gram metric. At reduced ranks, the resulting normal matrix retains the full diagonal blocks and approximates cross-party blocks ([Section 4.4.1](https://arxiv.org/html/2611.24367v1#S4.SS4.SSS1)).

In our example the regularized local matrix is $$A_k=\operatorname{diag}(33/2,3/2)$$. The full local fit is $$A_k^{-1}X_k^\top y=(0,2/3)^\top$$. Choose the leading local direction for collaboration, with normalized map $$M_k=\sqrt{2/33}(1,0)^\top$$. The reduced cross-party product is zero, and the reduced target products $$M_k^\top X_k^\top y$$ are zero too. The correction vanishes. Both full local fits survive, giving

$$
\widehat y_{\rm LC}=\left(\frac23+\frac23\right)y=\frac43y,
\qquad
J(w^{\rm LC})=\frac19+\frac49=\frac59.
$$

This overshoot occurs even with the formula's prescribed subtraction of the retained local component. The omitted relationship lies in the other direction, outside the collaboration space. Keeping both local target signals does not tell the fit how to account for their overlap.

![{{ page.comic_alt }}]({{ page.comic | relative_url }})

*All three fits use the same fixed features and penalty. Each reduced strategy keeps one collaboration direction per party. The final panel is a deliberate signal-direction control, rather than an automatic subspace-selection rule.*

The distinction between exact solving and a changed system is visible through residuals. In feature order $$[4e_1,e_3,4e_2,e_3]$$, let $$D=\operatorname{diag}(33/2,3/2,33/2,3/2)$$. Here the LC surrogate matrix is exactly $$\widehat G=D$$. Its solution has zero surrogate residual, yet the full normal-equation residual is

$$
r=Gw^{\rm LC}-h=(0,2/3,0,2/3)^\top\ne0.
$$

For any candidate $$\widetilde w$$, define $$r=G\widetilde w-h$$. Subtracting $$Gw^*=h$$ gives $$\widetilde w-w^*=G^{-1}r$$. Expanding the quadratic objective around its minimizer cancels the linear term, yielding the exact identity

$$
J(\widetilde w)-J(w^*)
=(\widetilde w-w^*)^\top G(\widetilde w-w^*)
=r^\top G^{-1}r.
$$

For our LC fit, the objective gap is $$5/9-1/5=16/45$$. A small residual for the surrogate system certifies that the surrogate was solved accurately. It does not measure the omitted cross-party coupling in the original system.

There is also a direct coefficient-error calculation. From $$\widehat G w^{\rm LC}=h=Gw^*$$,

$$
\widehat G(w^{\rm LC}-w^*)=(G-\widehat G)w^*,
\qquad
\lVert w^{\rm LC}-w^*\rVert
\le\frac{\lVert G-\widehat G\rVert_2}{\lambda_{\min}(\widehat G)}\lVert w^*\rVert.
$$

This is the paper's [LC approximation bound](https://arxiv.org/html/2611.24367v1#S4.SS4.SSS1) specialized to a single response. In the toy, $$\lVert G-\widehat G\rVert_2=1$$ and $$\lambda_{\min}(\widehat G)=3/2$$. The coefficient difference is $$w^{\rm LC}-w^*=(0,4/15,0,4/15)^\top$$, whose norm is exactly $$2/3$$ of $$\lVert w^*\rVert$$. The bound is attained. The missing interaction is enough to cause the full coefficient error allowed by this bound, even though the dominant local Gram directions were retained.

A different one-direction-per-party choice completely changes the result. Keep the smaller local direction, $$e_3$$, for collaboration. Pure projection now solves the same two-coefficient system as full ridge because the discarded large directions have zero coefficients at the optimum. LC also recovers the full solution: every nonzero cross-party interaction lies in the retained signal directions. Both give $$\widehat y=(4/5)y$$ while retaining only $$1/17$$ of each local Gram trace. Full-rank collaboration maps are sufficient for exact recovery, but this example shows that they are not necessary.

This control uses knowledge of the constructed target to choose the subspace. It establishes an algebraic possibility, not a generally available selection algorithm. In an actual vertical system, learning which directions carry shared predictive information also has computation, communication and information-access costs.

My research judgment is that local energy alone is an incomplete guide to collaboration budgets. The example contains two separate hazards: projection can eliminate predictive information, and reduced coupling can preserve that information locally while miscalibrating its combined use. A useful evaluation should hold representations and regularization fixed, and measure the original objective or full-system residual as well as prediction quality and fitting cost. Validation-selected penalties should be reported separately from gains attributable to the collaboration subspace.

A concrete next experiment would compare local spectral bases with coupling-aware and target-aware controls at the same per-party widths. Vary the strength of a shared low-energy direction and the ridge penalty, and examine whether full-system residuals identify the difficult cases. The algebra predicts where a low-rank correction is exact and where its error grows; generalization and protocol privacy require their own assumptions and evidence.

The comic was created with AI.
