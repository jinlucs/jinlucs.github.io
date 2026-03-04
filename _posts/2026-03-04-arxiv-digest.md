---
layout: post
title: "Daily arXiv Digest — 2026-03-04 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Robust principal component analysis with rank and cardinality regularization under matrix factorization
- **Authors:** Wenjing Li, Wei Bian, Kim-Chuan Toh
- **arXiv:** [2603.03107](https://arxiv.org/abs/2603.03107v1) · [pdf](https://arxiv.org/pdf/2603.03107v1)
- **Categories:** math.OC

### Abstract
> Robust principal component analysis is an important representative method in data analysis. It is usually viewed as an optimization problem involving the rank and $\ell_0$-norm of matrices. In this paper, we study the rank and $\ell_0$ regularized optimization problem and its matrix factorization problem. We establish their equivalences on global minimizers and stationary points, respectively. Furthermore, we construct a broadly applicable equivalent nonconvex relaxation framework for the constrained factorization model in the sense of global minimizers and stationary points with strong optimality conditions (called strong stationary points). For the general factorization problem with lower semicontinuous regularizers and a loss function whose gradient is locally Lipschitz, we propose a novel proximal gradient-based algorithm based on joint and alternating calculation with convergence to its limiting-critical points. The algorithm can attain the stationary points of the original problem and its adaptive counterpart can attain the strong stationary points of the factorization problem.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Stabilized Adaptive Loss and Residual-Based Collocation for Physics-Informed Neural Networks
- **Authors:** Divyavardhan Singh, Shubham Kamble, Dimple Sonone, Kishor Upla
- **arXiv:** [2603.03224](https://arxiv.org/abs/2603.03224v1) · [pdf](https://arxiv.org/pdf/2603.03224v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Physics-Informed Neural Networks (PINNs) have been recognized as a mesh-free alternative to solve partial differential equations where physics information is incorporated. However, in dealing with problems characterized by high stiffness or shock-dominated dynamics, traditional PINNs have been found to have limitations, including unbalanced training and inaccuracy in solution, even with small physics residuals. In this research, we seek to address these limitations using the viscous Burgers' equation with low viscosity and the Allen-Cahn equation as test problems. In addressing unbalanced training, we have developed a new adaptive loss balancing scheme using smoothed gradient norms to ensure satisfaction of initial and boundary conditions. Further, to address inaccuracy in the solution, we have developed an adaptive residual-based collocation scheme to improve the accuracy of solutions in the regions with high physics residuals. The proposed new approach significantly improves solution accuracy with consistent satisfaction of physics residuals. For instance, in the case of Burgers' equation, the relative L2 error is reduced by about 44 percent compared to traditional PINNs, while for the Allen-Cahn equation, the relative L2 error is reduced by approximately 70 percent. Additionally, we show the trustworthy solution comparison of the proposed method using a robust finite difference solver.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Shape Derivative-Informed Neural Operators with Application to Risk-Averse Shape Optimization
- **Authors:** Xindi Gong, Dingcheng Luo, Thomas O'Leary-Roseberry, Ruanui Nicholson, Omar Ghattas
- **arXiv:** [2603.03211](https://arxiv.org/abs/2603.03211v1) · [pdf](https://arxiv.org/pdf/2603.03211v1)
- **Categories:** math.OC, cs.LG, math.NA

### Abstract
> Shape optimization under uncertainty (OUU) is computationally intensive for classical PDE-based methods due to the high cost of repeated sampling-based risk evaluation across many uncertainty realizations and varying geometries, while standard neural surrogates often fail to provide accurate and efficient sensitivities for optimization. We introduce Shape-DINO, a derivative-informed neural operator framework for learning PDE solution operators on families of varying geometries, with a particular focus on accelerating PDE-constrained shape OUU. Shape-DINOs encode geometric variability through diffeomorphic mappings to a fixed reference domain and employ a derivative-informed operator learning objective that jointly learns the PDE solution and its Fréchet derivatives with respect to design variables and uncertain parameters, enabling accurate state predictions and reliable gradients for large-scale OUU. We establish a priori error bounds linking surrogate accuracy to optimization error and prove universal approximation results for multi-input reduced basis neural operators in suitable $C^1$ norms. We demonstrate efficiency and scalability on three representative shape OUU problems, including boundary design for a Poisson equation and shape design governed by steady-state Navier-Stokes exterior flows in two and three dimensions. Across these examples, Shape-DINOs produce more reliable optimization results than operator surrogates trained without derivative information. In our examples, Shape-DINOs achieve 3-8 orders-of-magnitude speedups in state and gradient evaluations. Counting training data generation, Shape-DINOs reduce necessary PDE solves by 1-2 orders-of-magnitude compared to a strictly PDE-based approach for a single OUU problem. Moreover, Shape-DINO construction costs can be amortized across many objectives and risk measures, enabling large-scale shape OUU for complex systems.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) LAGO: A Local-Global Optimization Framework Combining Trust Region Methods and Bayesian Optimization
- **Authors:** Eliott Van Dieren, Tommaso Vanzan, Fabio Nobile
- **arXiv:** [2603.02970](https://arxiv.org/abs/2603.02970v1) · [pdf](https://arxiv.org/pdf/2603.02970v1)
- **Categories:** cs.LG, math.OC

### Abstract
> We introduce LAGO, a LocAl-Global Optimization algorithm that combines gradient-enhanced Bayesian Optimization (BO) with gradient-based trust region local refinement through an adaptive competition mechanism. At each iteration, global and local optimization strategies independently propose candidate points, and the next evaluation is selected based on predicted improvement. LAGO separates global exploration from local refinement at the proposal level: the BO acquisition function is optimized outside the active trust region, while local function and gradient evaluations are incorporated into the global gradient-enhanced Gaussian process only when they satisfy a lengthscale-based minimum-distance criterion, reducing the risk of numerical instability during the local exploitation. This enables efficient local refinement when reaching promising regions, without sacrificing a global search of the design space. As a result, the method achieves an improved exploration of the full design space compared to standard non-linear local optimization algorithms for smooth functions, while maintaining fast local convergence in regions of interest.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model
- **Authors:** Giorgio Ferrari, Tim Niclas Schütz
- **arXiv:** [2603.02820](https://arxiv.org/abs/2603.02820v1) · [pdf](https://arxiv.org/pdf/2603.02820v1)
- **Categories:** math.OC, math.PR, q-fin.MF

### Abstract
> In this paper, we study an intertemporal utility maximization problem in which an investor chooses consumption and portfolio strategies in the presence of a stochastic factor and a no-borrowing constraint. In the spirit of the Kim-Omberg model, the stochastic factor represents the excess return of the risky asset and follows an Ornstein-Uhlenbeck process, capturing the mean reversion of expected excess returns-a feature well supported by empirical evidence in financial markets. The investor seeks to maximize expected utility from consumption, subject to the constraint that wealth remains nonnegative at all times. To address the dynamic no-borrowing constraint, we use Lagrange duality to transform the primal problem into a singular control problem in the dual space. We then characterize the solution to the dual singular control problem via an auxiliary two-dimensional optimal stopping problem featuring stochastic volatility, and subsequently retrieve the primal value function as well as the optimal portfolio and consumption plans. Finally, a numerical study is conducted to derive economic and financial implications.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
