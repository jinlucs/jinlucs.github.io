---
layout: post
title: "Daily arXiv Digest — 2026-03-18 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Preconditioned Proximal Gradient Methods with Conjugate Momentum: A Subspace Perspective
- **Authors:** Jian Chen, Xinmin Yang
- **arXiv:** [2603.16573](https://arxiv.org/abs/2603.16573v1) · [pdf](https://arxiv.org/pdf/2603.16573v1)
- **Categories:** math.OC

### Abstract
> In this paper, we propose a descent method for composite optimization problems with linear operators. Specifically, we first design a structure-exploiting preconditioner tailored to the linear operator so that the resulting preconditioned proximal subproblem admits a closed-form solution through its dual formulation. However, such a structure-driven preconditioner may be poorly aligned with the local curvature of the smooth component, which can lead to slow practical convergence. To address this issue, we develop a subspace proximal Newton framework that incorporates curvature information within a low-dimensional subspace. At each iteration, the search direction is obtained by minimizing a proximal Newton model restricted to a two-dimensional subspace spanned by the current preconditioned proximal gradient direction and a momentum direction derived from the previous iterate. By orthogonalizing the subspace basis with respect to the local Hessian-induced metric, the resulting two-dimensional nonsmooth subproblem can be efficiently approximated by solving two one-dimensional optimization problems. This orthogonalization plays a crucial role: it allows a single pass of alternating one-dimensional updates to provide a good approximation to the original coupled two-dimensional subproblem while keeping the per-iteration computational cost low. We establish global convergence of the proposed method and prove a $Q$-linear convergence rate under strong convexity. Comparative numerical experiments demonstrate the effectiveness of the proposed algorithm, particularly on high-dimensional and ill-conditioned problems.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Prescribed-Time Distributed Generalized Nash Equilibrium Seeking
- **Authors:** Liraz Mudrik, Isaac Kaminer, Sean Kragelund, Abram H. Clark
- **arXiv:** [2603.16865](https://arxiv.org/abs/2603.16865v1) · [pdf](https://arxiv.org/pdf/2603.16865v1)
- **Categories:** math.OC, eess.SY

### Abstract
> This paper proposes the first fully distributed algorithm for finding the Generalized Nash Equilibrium (GNE) of a non-cooperative game with shared coupling constraints and general cost coupling at a user-prescribed finite time T. As a foundation, a centralized gradient-based prescribed-time convergence result is established for the GNE problem, extending the optimization Lyapunov function framework to gradient dynamics, the only known realization among existing alternatives that naturally decomposes into per-agent computations. Building on this, a fully distributed architecture is designed in which each agent concurrently runs three coupled dynamics: a prescribed-time distributed state observer, a gradient-based optimization law, and a dual consensus mechanism that enforces the shared-multiplier requirement of the variational GNE, thus guaranteeing convergence to the same solution as the centralized case. The simultaneous operation of these layers creates bidirectional perturbations between consensus and optimization, which are resolved through gain synchronization that matches the temporal singularities of the optimization and consensus layers, ensuring all error components vanish exactly at T. The Fischer-Burmeister reformulation renders the algorithm projection-free and guarantees constraint satisfaction at the deadline. Numerical simulations on a Nash-Cournot game and a time-critical sensor coverage problem validate the approach.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Stochastic Resetting Accelerates Policy Convergence in Reinforcement Learning
- **Authors:** Jello Zhou, Vudtiwat Ngampruetikorn, David J. Schwab
- **arXiv:** [2603.16842](https://arxiv.org/abs/2603.16842v1) · [pdf](https://arxiv.org/pdf/2603.16842v1)
- **Categories:** cs.LG, cond-mat.dis-nn, cond-mat.stat-mech, eess.SY, physics.bio-ph

### Abstract
> Stochastic resetting, where a dynamical process is intermittently returned to a fixed reference state, has emerged as a powerful mechanism for optimizing first-passage properties. Existing theory largely treats static, non-learning processes. Here we ask how stochastic resetting interacts with reinforcement learning, where the underlying dynamics adapt through experience. In tabular grid environments, we find that resetting accelerates policy convergence even when it does not reduce the search time of a purely diffusive agent, indicating a novel mechanism beyond classical first-passage optimization. In a continuous control task with neural-network-based value approximation, we show that random resetting improves deep reinforcement learning when exploration is difficult and rewards are sparse. Unlike temporal discounting, resetting preserves the optimal policy while accelerating convergence by truncating long, uninformative trajectories to enhance value propagation. Our results establish stochastic resetting as a simple, tunable mechanism for accelerating learning, translating a canonical phenomenon of statistical mechanics into an optimization principle for reinforcement learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Unifying Optimization and Dynamics to Parallelize Sequential Computation: A Guide to Parallel Newton Methods for Breaking Sequential Bottlenecks
- **Authors:** Xavier Gonzalez
- **arXiv:** [2603.16850](https://arxiv.org/abs/2603.16850v1) · [pdf](https://arxiv.org/pdf/2603.16850v1)
- **Categories:** math.NA, cs.AI, cs.DC, math.DS, math.OC

### Abstract
> Massively parallel hardware (GPUs) and long sequence data have made parallel algorithms essential for machine learning at scale. Yet dynamical systems, like recurrent neural networks and Markov chain Monte Carlo, were thought to suffer from sequential bottlenecks. Recent work showed that dynamical systems can in fact be parallelized across the sequence length by reframing their evaluation as a system of nonlinear equations, which can be solved with Newton's method using a parallel associative scan. However, these parallel Newton methods struggled with limitations, primarily inefficiency, instability, and lack of convergence guarantees. This thesis addresses these limitations with methodological and theoretical contributions, drawing particularly from optimization. Methodologically, we develop scalable and stable parallel Newton methods, based on quasi-Newton and trust-region approaches. The quasi-Newton methods are faster and more memory efficient, while the trust-region approaches are significantly more stable. Theoretically, we unify many fixed-point methods into our parallel Newton framework, including Picard and Jacobi iterations. We establish a linear convergence rate for these techniques that depends on the method's approximation accuracy and stability. Moreover, we give a precise condition, rooted in dynamical stability, that characterizes when parallelization provably accelerates a dynamical system and when it cannot. Specifically, the sign of the Largest Lyapunov Exponent of a dynamical system determines whether or not parallel Newton methods converge quickly. In sum, this thesis unlocks scalable and stable methods for parallelizing sequential computation, and provides a firm theoretical basis for when such techniques will and will not work. This thesis also serves as a guide to parallel Newton methods for researchers who want to write the next chapter in this ongoing story.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) OT-DETECT: Optimal transport-driven attack detection in cyber-physical systems
- **Authors:** Souvik Das, Siddhartha Ganguly
- **arXiv:** [2603.16588](https://arxiv.org/abs/2603.16588v1) · [pdf](https://arxiv.org/pdf/2603.16588v1)
- **Categories:** math.OC, eess.SP, eess.SY

### Abstract
> This article presents an optimal-transport (OT)-driven, distributionally robust attack detection algorithm, OT-DETECT, for cyber-physical systems (CPS) modeled as partially observed linear stochastic systems. The underlying detection problem is formulated as a minmax optimization problem using 1-Wasserstein ambiguity sets constructed from observer residuals under both the nominal (attack-free) and attacked regimes. We show that the minmax detection problem can be reduced to a finite-dimensional linear program for computing the worst-case distribution (WCD). Off-support residuals are handled via a kernel-smoothed score function that drives a CUSUM procedure for sequential detection. We also establish a non-asymptotic tail bound on the false-positive error of the CUSUM statistic under the nominal (attack-free) condition, under mild assumptions. Numerical illustrations are provided to evaluate the robustness properties of OT-DETECT.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
