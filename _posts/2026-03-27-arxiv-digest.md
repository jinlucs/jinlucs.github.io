---
layout: post
title: "Daily arXiv Digest — 2026-03-27 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) A Representation Optimization Dichotomy, Lie-Algebraic Policy Optimization
- **Authors:** Sooraj KC, Vivek Mishra
- **arXiv:** [2603.25525](https://arxiv.org/abs/2603.25525v1) · [pdf](https://arxiv.org/pdf/2603.25525v1)
- **Categories:** math.OC

### Abstract
> Structured reinforcement learning and stochastic optimization often involve parameters evolving on matrix Lie groups such as rotations and rigid-body transformations. We establish a representation-optimization dichotomy for Lie-algebra-parameterized Gaussian policy objectives in the Lie Group MDP class: the gradient Lipschitz constant L(R), governing step size, convergence, and sample complexity of first-order methods, depends only on the algebraic type of g, uniformly over all objectives, independent of reward or transition structure. Specifically, L = O(1) for compact g (e.g., so(n), su(n)), and L = Theta(exp(2R)) for g = gl(n), with O(exp(2R)) for all algebras with a hyperbolic element. A key lower bound shows this exponential growth cannot be canceled by interaction between the exponential map and the objective, making the dichotomy intrinsic to the algebra.This yields an algorithmic consequence: for compact algebras, radius-independent smoothness enables O(1/sqrt(T)) convergence using an O(n^2 J) Lie-algebraic projection step instead of O(d_g^3) Fisher inversion. A Kantorovich alignment bound alpha >= 2 kappa / (kappa + 1) provides a computable condition under which this projection approximates natural gradient updates. Experiments on SO(3)^J and SE(3) confirm the theory: constant smoothness for compact algebras, polynomial growth for SE(3), and alignment across condition regimes. The projection step achieves 1.1-1.7x speedup over Cholesky-based Fisher inversion, with increasing gains at larger scales.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Residual-as-Teacher: Mitigating Bias Propagation in Student--Teacher Estimation
- **Authors:** Kakei Yamamoto, Martin J. Wainwright
- **arXiv:** [2603.25466](https://arxiv.org/abs/2603.25466v1) · [pdf](https://arxiv.org/pdf/2603.25466v1)
- **Categories:** stat.ML, cs.LG, math.ST

### Abstract
> We study statistical estimation in a student--teacher setting, where predictions from a pre-trained teacher are used to guide a student model. A standard approach is to train the student to directly match the teacher's outputs, which we refer to as student soft matching (SM). This approach directly propagates any systematic bias or mis-specification present in the teacher, thereby degrading the student's predictions. We propose and analyze an alternative scheme, known as residual-as-teacher (RaT), in which the teacher is used to estimate residuals in the student's predictions. Our analysis shows how the student can thereby emulate a proximal gradient scheme for solving an oracle optimization problem, and this provably reduces the effect of teacher bias. For general student--teacher pairs, we establish non-asymptotic excess risk bounds for any RaT fixed point, along with convergence guarantees for the student-teacher iterative scheme. For kernel-based student--teacher pairs, we prove a sharp separation: the RaT method achieves the minimax-optimal rate, while the SM method incurs constant prediction error for any sample size. Experiments on both synthetic data and ImageNette classification under covariate shift corroborate our theoretical findings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Atomic Gradient Flows: Gradient Flows on Sparse Representations
- **Authors:** Christian Amend, Marcello Carioni, Konstantinos Zemas
- **arXiv:** [2603.25675](https://arxiv.org/abs/2603.25675v1) · [pdf](https://arxiv.org/pdf/2603.25675v1)
- **Categories:** math.OC

### Abstract
> One of the most popular approaches for solving total variation-regularized optimization problems in the space of measures are Particle Gradient Flows (PGFs). These restrict the problem to linear combinations of Dirac deltas and then perform a Euclidean gradient flow in the weights and positions, significantly reducing the computational cost while still decreasing the energy. In this work, we generalize PGFs to convex optimization problems in arbitrary Banach spaces, which we call Atomic Gradient Flows (AGFs). To this end, the crucial ingredient turns out to be the right notion of particles, chosen here as the extremal points of the unit ball of the regularizer. This choice is motivated by the Krein-Milman theorem, which ensures that minimizers can be approximated by linear combinations of extremal points. We investigate metric gradient flows of the optimization problem when restricted to such sparse representations, for which we define a suitable discretized functional that we show to be to be consistent with the original problem via the means of $Γ$-convergence. We prove that the resulting evolution of the latter is well-defined using a minimizing movement scheme, and we establish conditions ensuring $λ$-convexity and uniqueness of the flow. Then, using Choquet's theorem, we lift the problem into the Wasserstein space on weights and extremal points, and consider Wasserstein gradient flows in this lifted setting. Our main result is that the lifting of the AGF evolution is again a metric gradient flow in the Wasserstein space, verifying the consistency of the approach with respect to a Wasserstein-type dynamic. Finally, we illustrate the applicability of AGFs to several relevant infinite-dimensional problems, including optimization of functions of bounded variation and curves of measures regularized by Optimal Transport-type penalties.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Instance-optimal stochastic convex optimization: Can we improve upon sample-average and robust stochastic approximation?
- **Authors:** Liwei Jiang, Ashwin Pananjady
- **arXiv:** [2603.25657](https://arxiv.org/abs/2603.25657v1) · [pdf](https://arxiv.org/pdf/2603.25657v1)
- **Categories:** math.OC, stat.ML

### Abstract
> We study the unconstrained minimization of a smooth and strongly convex population loss function under a stochastic oracle that introduces both additive and multiplicative noise; this is a canonical and widely-studied setting that arises across operations research, signal processing, and machine learning. We begin by showing that standard approaches such as sample average approximation and robust (or averaged) stochastic approximation can lead to suboptimal -- and in some cases arbitrarily poor -- performance with realistic finite sample sizes. In contrast, we demonstrate that a carefully designed variance reduction strategy, which we term VISOR for short, can significantly outperform these approaches while using the same sample size. Our upper bounds are complemented by finite-sample, information-theoretic local minimax lower bounds, which highlight fundamental, instance-dependent factors that govern the performance of any estimator. Taken together, these results demonstrate that an accelerated variant of VISOR is instance-optimal, achieving the best possible sample complexity up to logarithmic factors while also attaining optimal oracle complexity. We apply our theory to generalized linear models and improve upon classical results. In particular, we obtain the best-known non-asymptotic, instance-dependent generalization error bounds for stochastic methods, even in linear regression.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Particle method for a nonlinear multimarginal optimal transport problem
- **Authors:** Adrien Cances, Quentin Mérigot, Luca Nenna
- **arXiv:** [2603.25584](https://arxiv.org/abs/2603.25584v1) · [pdf](https://arxiv.org/pdf/2603.25584v1)
- **Categories:** math.OC, math.NA

### Abstract
> We study a nonlinear multimarginal optimal transport problem arising in risk management, where the objective is to maximize a spectral risk measure of the pushforward of a coupling by a cost function. Although this problem is inherently nonlinear, it is known to have an equivalent linear reformulation as a multimarginal transport problem with an additional marginal. We introduce a Lagrangian particle discretization of this problem, in which admissible couplings are approximated by uniformly weighted point clouds, and marginal constraints are enforced through Wasserstein penalization. We prove quantitative convergence results for this discretization as the number of particles tends to infinity. The convergence rate is shown to be governed by the uniform quantization error of an optimal solution, and can be bounded in terms of the geometric properties of its support, notably its box dimension. In the case of univariate marginals and supermodular cost functions, where optimal couplings are known to be comonotone, we obtain sharper convergence rates expressed in terms of the asymptotic quantization errors of the marginals themselves. We also discuss the particular case of conditional value at risk, for which the problem reduces to a multimarginal partial transport formulation. Finally, we illustrate our approach with numerical experiments in several application domains, including risk management and partial barycenters, as well as some artificial examples with a repulsive cost.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
