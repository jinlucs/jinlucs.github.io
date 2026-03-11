---
layout: post
title: "Daily arXiv Digest — 2026-03-11 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) A Short Survey of Averaging Techniques in Stochastic Gradient Methods
- **Authors:** K. Lakshmanan
- **arXiv:** [2603.09634](https://arxiv.org/abs/2603.09634v1) · [pdf](https://arxiv.org/pdf/2603.09634v1)
- **Categories:** math.OC

### Abstract
> Stochastic gradient methods are among the most widely used algorithms for large-scale optimization and machine learning. A key technique for improving the statistical efficiency and stability of these methods is the use of averaging schemes applied to the sequence of iterates generated during optimization. Starting from the classical work on stochastic approximation, averaging techniques such as Polyak--Ruppert averaging have been shown to achieve optimal asymptotic variance and improved convergence behavior. In recent years, averaging methods have gained renewed attention in machine learning applications, particularly in the training of deep neural networks and large-scale learning systems. Techniques such as tail averaging, exponential moving averages, and stochastic weight averaging have demonstrated strong empirical performance and improved generalization properties. This paper provides a survey of averaging techniques in stochastic gradient optimization. We review the theoretical foundations of averaged stochastic approximation, discuss modern developments in stochastic gradient methods, and examine applications of averaging in machine learning. In addition, we summarize recent results on the finite-sample behavior of averaging schemes and highlight several open problems and directions for future research.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) A Unifying Primal-Dual Proximal Framework for Distributed Nonconvex Optimization
- **Authors:** Zichong Ou, Jie Lu
- **arXiv:** [2603.09524](https://arxiv.org/abs/2603.09524v1) · [pdf](https://arxiv.org/pdf/2603.09524v1)
- **Categories:** math.OC

### Abstract
> We consider distributed nonconvex optimization over an undirected network, where each node privately possesses its local objective and communicates exclusively with its neighboring nodes, striving to collectively achieve a common optimal solution. To handle the nonconvexity of the objective, we linearize the augmented Lagrangian function and introduce a time-varying proximal term. This approach leads to a Unifying Primal-Dual Proximal (UPP) framework that unifies a variety of existing first-order and second-order methods. Building on this framework, we further derive two specialized realizations with different communication strategies, namely UPP-MC and UPP-SC. We prove that both UPP-MC and UPP-SC achieve stationary solutions for nonconvex smooth problems at a sublinear rate. Furthermore, under the additional Polyak-Łojasiewics (P-Ł) condition, UPP-MC is linearly convergent to the global optimum. These convergence results provide new or improved guarantees for many existing methods that can be viewed as specializations of UPP-MC or UPP-SC. To further optimize the mixing process, we incorporate Chebyshev acceleration into UPP-SC, resulting in UPP-SC-OPT, which attains an optimal communication complexity bound. Extensive experiments across diverse network topologies demonstrate that our proposed algorithms outperform state-of-the-art methods in both convergence speed and communication efficiency.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) OptEMA: Adaptive Exponential Moving Average for Stochastic Optimization with Zero-Noise Optimality
- **Authors:** Ganzhao Yuan
- **arXiv:** [2603.09923](https://arxiv.org/abs/2603.09923v1) · [pdf](https://arxiv.org/pdf/2603.09923v1)
- **Categories:** cs.LG, math.NA, math.OC

### Abstract
> The Exponential Moving Average (EMA) is a cornerstone of widely used optimizers such as Adam. However, existing theoretical analyses of Adam-style methods have notable limitations: their guarantees can remain suboptimal in the zero-noise regime, rely on restrictive boundedness conditions (e.g., bounded gradients or objective gaps), use constant or open-loop stepsizes, or require prior knowledge of Lipschitz constants. To overcome these bottlenecks, we introduce OptEMA and analyze two novel variants: OptEMA-M, which applies an adaptive, decreasing EMA coefficient to the first-order moment with a fixed second-order decay, and OptEMA-V, which swaps these roles. Crucially, OptEMA is closed-loop and Lipschitz-free in the sense that its effective stepsizes are trajectory-dependent and do not require the Lipschitz constant for parameterization. Under standard stochastic gradient descent (SGD) assumptions, namely smoothness, a lower-bounded objective, and unbiased gradients with bounded variance, we establish rigorous convergence guarantees. Both variants achieve a noise-adaptive convergence rate of $\widetilde{\mathcal{O}}(T^{-1/2}+σ^{1/2} T^{-1/4})$ for the average gradient norm, where $σ$ is the noise level. In particular, in the zero-noise regime where $σ=0$, our bounds reduce to the nearly optimal deterministic rate $\widetilde{\mathcal{O}}(T^{-1/2})$ without manual hyperparameter retuning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) A Globally Convergent Third-Order Newton Method via Unified Semidefinite Programming Subproblems
- **Authors:** Yubo Cai, Wenqi Zhu, Coralia Cartis, Gioele Zardini
- **arXiv:** [2603.09682](https://arxiv.org/abs/2603.09682v1) · [pdf](https://arxiv.org/pdf/2603.09682v1)
- **Categories:** math.OC, math.NA

### Abstract
> We propose the Adaptive Levenberg-Marquardt Third-Order Newton Method (ALMTON) for unconstrained nonconvex optimization, providing the first globally convergent realization of the unregularized third-order Newton method. Unlike the standard Adaptive Regularization framework with third-order models (AR3), which enforces global behavior through a quartic term, ALMTON employs an adaptive Levenberg-Marquardt (quadratic) regularization. This choice preserves a cubic model at every iteration, so that every subproblem is a tractable semidefinite program (SDP). In particular, the ALMTON-Simple variant requires exactly one SDP solve per iteration, making the per-iteration cost uniform and predictable. Algorithmically, ALMTON follows a mixed-mode strategy: it attempts an unregularized third-order step whenever the cubic Taylor model admits a strict local minimizer with adequate curvature, and activates (or increases) quadratic regularization only when needed to ensure that the model is well posed and the step is globally reliable. We establish global convergence and prove an $O(ε^{-2})$ worst-case evaluation complexity for computing an $ε$-approximate first-order stationary point. Numerical experiments show that ALMTON enlarges the basin of attraction relative to classical baselines (gradient descent and damped Newton), and can progress on landscapes where second-order methods typically stagnate. When compared with a state-of-the-art third-order implementation (AR3-interp), ALMTON converges more consistently and often in fewer iterations. We also characterize the practical scalability limits of the approach, highlighting the computational bottlenecks introduced by current SDP solvers as dimension grows.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Faster Stochastic ADMM for Nonsmooth Composite Convex Optimization in Hilbert Space
- **Authors:** Weihua Deng, Haiming Song, Hao Wang, Jinda Yang
- **arXiv:** [2603.09447](https://arxiv.org/abs/2603.09447v1) · [pdf](https://arxiv.org/pdf/2603.09447v1)
- **Categories:** math.OC

### Abstract
> In this paper, a stochastic alternating direction method of multipliers (ADMM) is proposed for a class of nonsmooth composite and stochastic convex optimization problems in Hilbert space, motivated by optimization problems constrained by partial differential equation (PDE) with random coefficients. We prove the strong convergence of the proposed ADMM algorithm in the strongly convex case, and show the faster nonergodic convergence rates in terms of functional values and feasibility violation for both strongly convex and general convex cases. We demonstrate the application of the proposed method to solve certain model problems, along with its associated probability bound of large deviation. Some preliminary numerical results illustrate the efficiency of our method.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
