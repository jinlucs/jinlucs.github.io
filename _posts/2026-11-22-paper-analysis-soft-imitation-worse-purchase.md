---
layout: post
title: "Soft Imitation Can Favor the Worse Purchase"
subtitle: "A conditional average of teacher targets need not minimize expected Brier loss"
description: "Two hidden worlds give the same visible input. An exact calculation separates the best population imitation, the best affordable feature, and the extra loss caused by their different objectives."
date: 2026-11-22 09:00:00 -0500
permalink: /reading/2026-11-22-soft-imitation-worse-purchase/
categories: [paper-analysis]
mathjax: true
source_url: https://arxiv.org/html/2611.26598v1
paper_date: "2026-11-19"
comic: /assets/img/reading/2026-11-22-soft-imitation-worse-purchase.png
comic_alt: "Four panels show two hidden worlds with identical visible inputs, teacher probabilities of three quarters and one over eighty-two for action A, a population soft-cross-entropy optimum of 371 over 656 selecting A, and a lower expected Brier loss of three eighths for B versus one half for A."
author: "Research reading notes"
comments: false
social-share: false
---

A teacher can identify a useful purchase after inspecting hidden information. A deployed learner must choose before receiving that information. These are different decision problems. For a federated or distributed system that pays to request another feature, it matters whether the student learns to agree with its teacher or to minimize the expected error of the purchase.

Meng and colleagues' [*Active Feature Acquisition by Distilling an Oracle Teacher*](https://arxiv.org/abs/2611.26598v1), first public on November 19, distills a privileged teacher into a visible-state acquisition policy.

[Algorithm 1](https://arxiv.org/html/2611.26598v1#alg1) forms soft targets from these losses; [Algorithm 2](https://arxiv.org/html/2611.26598v1#alg2) takes the student's highest-scoring affordable action. For candidates $$a$$, write

$$
b_a=\lVert p_a-e_y\rVert_2^2,\qquad
q_a=\frac{\exp(-b_a/T)}{\sum_j\exp(-b_j/T)},\qquad T>0,
$$

where $$p_a$$ is the fixed predictor's class-probability vector after acquisition and $$e_y$$ is the true-label vector. The following is a separate constructed example of this action-loss objective.

## What population-optimal imitation learns

Let $$z$$ denote everything visible when the student chooses. The teacher's distribution $$q$$ also depends on hidden information. An unrestricted action head minimizing population soft cross-entropy at this state solves

$$
\mathbb E\!\left[-\sum_a q_a\log\pi_a(z)\mid z\right]
=-\sum_a\underbrace{\mathbb E[q_a\mid z]}_{m_a(z)}\log\pi_a(z).
$$

The right side equals $$H(m(z))+D_{\mathrm{KL}}(m(z)\Vert\pi(z))$$. Thus the optimal action distribution is $$\pi^*(z)=m(z)$$. It averages teacher probability targets. With positive targets, that distribution is unique.

For the one-purchase expected-Brier objective, the optimal deployable action instead minimizes $$\mathbb E[b_a\mid z]$$. A nonlinear softmax applied before conditional averaging can change which action wins. This remains possible with unlimited data and capacity. The action head generally cannot match every hidden world's teacher distribution separately.

## Two worlds, one purchase

Both candidates cost one unit, the budget is one unit, and the visible state is identical in both worlds. The hidden world has probabilities $$3/4$$ and $$1/4$$. Specify the fixed predictor's post-acquisition Brier losses by

$$
\begin{array}{ccc}
 & b_A & b_B\\
W_1\ (\mathbb P=3/4)&0&1/2\\
W_2\ (\mathbb P=1/4)&2&0
\end{array}
$$

These are valid binary Brier losses. With true label 1, let the predictor's probability for that label after actions $$(A,B)$$ be $$(1,1/2)$$ in $$W_1$$ and $$(0,1)$$ in $$W_2$$. Summing the squared errors over both classes gives $$b=2(1-p_y)^2$$, exactly the entries above. Candidate values can encode the world, which is unavailable before acquisition. This specifies a deliberately imperfect, mask-dependent fixed predictor; it assumes no Bayes-optimality or calibration. The policy chooses a feature and cannot replace this predictor.

Choose the toy temperature $$T=1/(2\log3)$$. In $$W_1$$ the teacher puts $$q_A=1/(1+\exp(-1/(2T)))=3/4$$ on A. In $$W_2$$ it puts $$q_A=1/(1+\exp(2/T))=1/82$$ on A. Therefore

$$
\pi_A^*=\mathbb E[q_A\mid z]
=\frac34\frac34+\frac14\frac1{82}
=\frac{371}{656}>\frac12.
$$

The population-optimal imitation deploys **A** under argmax. But always buying A has expected Brier loss $$\tfrac34\cdot0+\tfrac14\cdot2=1/2$$. Always buying B has expected loss $$\tfrac34\cdot\tfrac12+\tfrac14\cdot0=3/8$$. **B** is the better purchase by $$1/8$$.

![{{ page.comic_alt }}]({{ page.comic | relative_url }})

All loss values are summed Brier errors; teacher action probabilities are labeled separately. The student chooses before seeing the hidden world.

No randomized visible-state policy can beat B here. If it buys A with probability $$u$$ independently of the hidden world, its expected loss is $$3/8+u/8$$, minimized at $$u=0$$. The mismatch concerns the population action-loss optimum, with no representation tradeoff from an auxiliary classifier. Finite-capacity joint training can introduce further effects.

## Separate the information gap from the objective gap

The privileged teacher can choose A in $$W_1$$ and B in $$W_2$$, achieving zero Brier loss. The best policy with the student's information pays $$3/8$$. Optimal soft imitation adds another $$1/8$$. The total gap therefore splits into an information restriction and an additional objective mismatch:

$$
\frac12-0=\underbrace{\frac38}_{\text{best visible risk}}
+\underbrace{\frac18}_{\text{extra imitation risk}}.
$$

The paper's [Section 6](https://arxiv.org/html/2611.26598v1#S6) analyzes agreement with the teacher's hard action; its neighborhood recoverability estimate is empirical. In our example, A agrees with the hard teacher on $$3/4$$ of cases, attaining the highest possible agreement, while B agrees on $$1/4$$. Better teacher agreement therefore selects the worse expected-Brier action in this construction.

The order of operations makes the difference explicit. Applying softmax to the **conditional mean losses** at the toy temperature gives

$$
\left[\operatorname{softmax}\!\left(-\mathbb E[b\mid z]/T\right)\right]_A
=\frac{1}{1+3^{1/4}}\approx0.43177<\frac12.
$$

This favors B, whereas the mean of the teacher softmaxes favors A. The two expressions average different objects.

Temperature also matters. The paper's [Appendix A.2](https://arxiv.org/html/2611.26598v1#A1.SS2) reports $$T=0.5$$. On our constructed loss table, that temperature gives mean target mass $$m_A\approx0.55279$$ and still selects A. At $$T=1$$ the mass is about $$0.49665$$ and selects B. This demonstrates an objective mismatch that can occur, rather than a failure for every temperature or dataset.

## What I would compare next

I would train a second head to regress the per-action losses directly, then select the smallest predicted conditional mean. Under squared regression loss, unlimited capacity and the same visible information, its population target is $$\mathbb E[b_a\mid z]$$. In this one-purchase problem that is decision-consistent for expected Brier loss. A useful comparison would hold the predictor, affordable candidates, state distribution and budget fixed, while reporting teacher agreement alongside held-out purchase loss.

This analysis evaluates a one-step Brier objective. The paper's downstream metric is budgeted classification accuracy, and sequential acquisition can have complementary features and changing visible states. The calculation does not establish a globally optimal multi-step policy or an ordering on those benchmarks. A fixed predictor's proper scoring rule also does not make every transformation of its per-instance scores consistent with deployment utility. That is the distinction I would test before treating an irreducible teacher-agreement gap as the whole explanation for residual task error.

The comic was created with AI.
