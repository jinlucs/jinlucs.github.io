---
layout: post
title: "Daily arXiv Digest — 2026-03-17 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Grokking as a Variance-Limited Phase Transition: Spectral Gating and the Epsilon-Stability Threshold
- **Authors:** Pratyush Acharya, Habish Dhakal
- **arXiv:** [2603.15492](https://arxiv.org/abs/2603.15492v1) · [pdf](https://arxiv.org/pdf/2603.15492v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Standard optimization theories struggle to explain grokking, where generalization occurs long after training convergence. While geometric studies attribute this to slow drift, they often overlook the interaction between the optimizer's noise structure and landscape curvature. This work analyzes AdamW dynamics on modular arithmetic tasks, revealing a ``Spectral Gating'' mechanism that regulates the transition from memorization to generalization. We find that AdamW operates as a variance-gated stochastic system. Grokking is constrained by a stability condition: the generalizing solution resides in a sharp basin ($λ_{max}^H$) initially inaccessible under low-variance regimes. The ``delayed'' phase represents the accumulation of gradient variance required to lift the effective stability ceiling, permitting entry into this sharp manifold. Our ablation studies identify three complexity regimes: (1) \textbf{Capacity Collapse} ($P < 23$), where rank-deficiency prevents structural learning; (2) \textbf{The Variance-Limited Regime} ($P \approx 41$), where generalization waits for the spectral gate to open; and (3) \textbf{Stability Override} ($P > 67$), where memorization becomes dimensionally unstable. Furthermore, we challenge the "Flat Minima" hypothesis for algorithmic tasks, showing that isotropic noise injection fails to induce grokking. Generalization requires the \textit{anisotropic rectification} unique to adaptive optimizers, which directs noise into the tangent space of the solution manifold.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Saddle Point Evasion via Curvature-Regularized Gradient Dynamics
- **Authors:** Liraz Mudrik, Isaac Kaminer, Sean Kragelund, Abram H. Clark
- **arXiv:** [2603.15606](https://arxiv.org/abs/2603.15606v1) · [pdf](https://arxiv.org/pdf/2603.15606v1)
- **Categories:** math.OC, eess.SY

### Abstract
> Nonconvex optimization underlies many modern machine learning and control tasks, where saddle points pose the dominant obstacle to reliable convergence in high-dimensional settings. Escaping these saddle points deterministically and at a controllable rate remains an open challenge: gradient descent is blind to curvature, stochastic perturbation methods lack deterministic guarantees, and Newton-type approaches suffer from Hessian singularity. We present Curvature-Regularized Gradient Dynamics (CRGD), which augments the objective with a smooth penalty on the most negative Hessian eigenvalue, yielding an augmented cost that serves as an optimization Lyapunov function with user-selectable convergence rates to second-order stationary points. Numerical experiments on a nonconvex matrix factorization example confirm that CRGD escapes saddle points across all tested configurations, with escape time that decreases with the eigenvalue gap, in contrast to gradient descent, whose escape time grows inversely with the gap.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Unbiased and Biased Variance-Reduced Forward-Reflected-Backward Splitting Methods for Stochastic Composite Inclusions
- **Authors:** Quoc Tran-Dinh, Nghia Nguyen-Trung
- **arXiv:** [2603.15576](https://arxiv.org/abs/2603.15576v1) · [pdf](https://arxiv.org/pdf/2603.15576v1)
- **Categories:** cs.LG, math.OC, stat.ML

### Abstract
> This paper develops new variance-reduction techniques for the forward-reflected-backward splitting (FRBS) method to solve a class of possibly nonmonotone stochastic composite inclusions. Unlike unbiased estimators such as mini-batching, developing stochastic biased variants faces a fundamental technical challenge and has not been utilized before for inclusions and fixed-point problems. We fill this gap by designing a new framework that can handle both unbiased and biased estimators. Our main idea is to construct stochastic variance-reduced estimators for the forward-reflected direction and use them to perform iterate updates. First, we propose a class of unbiased variance-reduced estimators and show that increasing mini-batch SGD, loopless-SVRG, and SAGA estimators fall within this class. For these unbiased estimators, we establish a $\mathcal{O}(1/k)$ best-iterate convergence rate for the expected squared residual norm, together with almost-sure convergence of the iterate sequence to a solution. Consequently, we prove that the best oracle complexities for the $n$-finite-sum and expectation settings are $\mathcal{O}(n^{2/3}ε^{-2})$ and $\mathcal{O}(ε^{-10/3})$, respectively, when employing loopless-SVRG or SAGA, where $ε$ is a desired accuracy. Second, we introduce a new class of biased variance-reduced estimators for the forward-reflected direction, which includes SARAH, Hybrid SGD, and Hybrid SVRG as special instances. While the convergence rates remain valid for these biased estimators, the resulting oracle complexities are $\mathcal{O}(n^{3/4}ε^{-2})$ and $\mathcal{O}(ε^{-5})$ for the $n$-finite-sum and expectation settings, respectively. Finally, we conduct two numerical experiments on AUC optimization for imbalanced classification and policy evaluation in reinforcement learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) A Parameter-Free Zeroth-Order Algorithm for Decentralized Stochastic Convex Optimization
- **Authors:** Jiawei Chen, Alexander Rogozin
- **arXiv:** [2603.15219](https://arxiv.org/abs/2603.15219v1) · [pdf](https://arxiv.org/pdf/2603.15219v1)
- **Categories:** math.OC

### Abstract
> We consider decentralized stochastic convex optimization on connected network, in which gradients of agents are unavailable and each agent can query only noisy function values of its own local objective. The goal is to minimize the average objective over a compact convex domain using only local two point zeroth-order oracles and peer-to-peer communication. We propose a decentralized POEM method (D-POEM) that combines symmetric two point smoothing with adaptive radius and stepsize rules, thereby avoiding prior knowledge of the Lipschitz constant and diameter. For convex Lipschitz continuous objectives, we prove an convergence rate that separates a centralized optimization term from a network disagreement term. We further conduct the numerical experiments to demonstrate POEM outperforms existing distributed zeroth-order method.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) A Technical Note on the Implementation and Use of PDCS
- **Authors:** Zhenwei Lin, Zikai Xiong, Dongdong Ge, Yinyu Ye
- **arXiv:** [2603.15504](https://arxiv.org/abs/2603.15504v1) · [pdf](https://arxiv.org/pdf/2603.15504v1)
- **Categories:** math.OC

### Abstract
> This technical note documents the implementation and use of the Primal-Dual Conic Programming Solver (PDCS), a first-order solver for large-scale conic optimization problems introduced by Lin et al. (arXiv:2505.00311). It describes the algorithmic and implementation details underlying PDCS, including the restarted primal-dual hybrid gradient method framework, adaptive step-size selection, adaptive reflected Halpern iterations, adaptive restarts, and diagonal preconditioning. It also provides practical instructions for using PDCS, including its interfaces with JuMP and CVXPY, solver options, and illustrative code examples. PDCS is available at https://github.com/ZikaiXiong/PDCS under the Apache License 2.0.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
