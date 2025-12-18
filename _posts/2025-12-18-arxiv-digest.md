---
layout: post
title: "Daily arXiv Digest — 2025-12-18 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Historical Information Accelerates Decentralized Optimization: A Proximal Bundle Method
- **Authors:** Zhao Zhu, Yu-Ping Tian, Xuyang Wu
- **arXiv:** [2512.15189](https://arxiv.org/abs/2512.15189v1) · [pdf](https://arxiv.org/pdf/2512.15189v1)
- **Categories:** math.OC, eess.SY

### Abstract
> Historical information, such as past function values or gradients, has significant potential to enhance decentralized optimization methods for two key reasons: first, it provides richer information about the objective function, which also explains its established success in centralized optimization; second, unlike the second-order derivative or its alternatives, historical information has already been computed or communicated and requires no additional cost to acquire. Despite this potential, it remains underexploited. In this work, we employ a proximal bundle framework to incorporate the function values and gradients at historical iterates and adapt the framework to the proximal decentralized gradient descent method, resulting in a Decentralized Proximal Bundle Method (DPBM). To broaden its applicability, we further extend DPBM to the asynchronous and stochastic setting. We theoretically analysed the convergence of the proposed methods. Notably, both the asynchronous DPBM and its stochastic variant can converge with fixed step-sizes that are independent of delays, which is superior to the delay-dependent step-sizes required by most existing asynchronous optimization methods, as it is easier to determine and often leads to faster convergence. Numerical experiments on classification problems demonstrate that by using historical information, our methods yield faster convergence and stronger robustness in the step-sizes.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Asymptotic behaviour of stochastic inertial dynamics incorporating a Tikhonov regularization term
- **Authors:** Chiara Schindler
- **arXiv:** [2512.15392](https://arxiv.org/abs/2512.15392v1) · [pdf](https://arxiv.org/pdf/2512.15392v1)
- **Categories:** math.OC

### Abstract
> In a separable Hilbert space, we study the minimization problem of a convex smooth function with Lipschitz continuous gradient whose evaluations are corrupted by random noise. To this end, we associate a stochastic inertial system that incorporates Tikhonov regularization with the optimization problem. We establish existence and uniqueness of a solution trajectory for this system. Then, we derive an upper bound on the expected value of an appropriate associated energy function given square-integrability of the diffusion $σ_X$ before focusing on the particular case where the parameter function multiplied by the Tikhonov term is given by $\frac{1}{t^r}$ for $0<r<2$. For this setting, we show a.s. convergence rates as well as convergence rates in expectation for the function values along the trajectory to an infimal value, the trajectory process to an optimal solution and its time derivative to zero under a stronger integrability condition on $σ_X$.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Exact Learning of Linear Model Predictive Control Laws using Oblique Decision Trees with Linear Predictions
- **Authors:** Jiayang Ren, Qiangqiang Mao, Tianwei Zhao, Yankai Cao
- **arXiv:** [2512.15568](https://arxiv.org/abs/2512.15568v1) · [pdf](https://arxiv.org/pdf/2512.15568v1)
- **Categories:** math.OC, eess.SY

### Abstract
> Model Predictive Control (MPC) is a powerful strategy for constrained multivariable systems but faces computational challenges in real-time deployment due to its online optimization requirements. While explicit MPC and neural network approximations mitigate this burden, they suffer from scalability issues or lack interpretability, limiting their applicability in safety-critical systems. This work introduces a data-driven framework that directly learns the Linear MPC control law from sampled state-action pairs using Oblique Decision Trees with Linear Predictions (ODT-LP), achieving both computational efficiency and interpretability. By leveraging the piecewise affine structure of Linear MPC, we prove that the Linear MPC control law can be replicated by finite-depth ODT-LP models. We develop a gradient-based training algorithm using smooth approximations of tree routing functions to learn this structure from grid-sampled Linear MPC solutions, enabling end-to-end optimization. Input-to-state stability is established under bounded approximation errors, with explicit error decomposition into learning inaccuracies and sampling errors to inform model design. Numerical experiments demonstrate that ODT-LP controllers match MPC's closed-loop performance while reducing online evaluation time by orders of magnitude compared to MPC, explicit MPC, neural network, and random forest counterparts. The transparent tree structure enables formal verification of control logic, bridging the gap between computational efficiency and certifiable reliability for safety-critical systems.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) A Regression-Based Prediction-Correction Method for Stochastic Time-Varying Optimization Problems
- **Authors:** Tomoya Kamijima, Naoki Marumo, Akiko Takeda
- **arXiv:** [2512.15205](https://arxiv.org/abs/2512.15205v1) · [pdf](https://arxiv.org/pdf/2512.15205v1)
- **Categories:** math.OC

### Abstract
> In many real-world applications, optimization problems evolve continuously over time and are often subject to stochastic noise. We consider a stochastic time-varying optimization problem in which the objective function $f(x;t)$ changes continuously and only noisy gradient observations are available. In deterministic settings, the prediction-correction method that exploits the time derivative of the solution is effective for accurately tracking the solution trajectory. However, a straightforward extension to stochastic problems requires an estimate of $\nabla_{xt} f(x;t)$ and the computation of a Hessian inverse at each step--requirements that are difficult or costly in practice. To address these issues, we propose a prediction-correction algorithm that uses a regression-based prediction step: the prediction is formed as a linear combination of recent iterates, which can be computed efficiently without estimating $\nabla_{xt}f(x;t)$ or computing Hessian inversions. We prove a tracking-error bound for the proposed method under standard smoothness and stochastic assumptions. Numerical experiments show that the regression-based prediction improves tracking accuracy while reducing computational cost compared with existing methods.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) A Clustering-Based Variable Ordering Framework for Relaxed Decision Diagrams for Maximum Weighted Independent Set Problem
- **Authors:** Mohsen Nafar, Michael Römer, Lin Xie
- **arXiv:** [2512.15198](https://arxiv.org/abs/2512.15198v1) · [pdf](https://arxiv.org/pdf/2512.15198v1)
- **Categories:** cs.AI, math.OC

### Abstract
> Efficient exact algorithms for Discrete Optimization (DO) rely heavily on strong primal and dual bounds. Relaxed Decision Diagrams (DDs) provide a versatile mechanism for deriving such dual bounds by compactly over-approximating the solution space through node merging. However, the quality of these relaxed diagrams, i.e. the tightness of the resulting dual bounds, depends critically on the variable ordering and the merging decisions executed during compilation. While dynamic variable ordering heuristics effectively tighten bounds, they often incur computational overhead when evaluated globally across the entire variable set. To mitigate this trade-off, this work introduces a novel clustering-based framework for variable ordering. Instead of applying dynamic ordering heuristics to the full set of unfixed variables, we first partition variables into clusters. We then leverage this structural decomposition to guide the ordering process, significantly reducing the heuristic's search space. Within this framework, we investigate two distinct strategies: Cluster-to-Cluster, which processes clusters sequentially using problem-specific aggregate criteria (such as cumulative vertex weights in the Maximum Weighted Independent Set Problem (MWISP)), and Pick-and-Sort, which iteratively selects and sorts representative variables from each cluster to balance local diversity with heuristic guidance. Later on, developing some theoretical results on the growth of the size of DDs for MWISP we propose two different policies for setting the number of clusters within the proposed framework. We embed these strategies into a DD-based branch-and-bound algorithm and evaluate them on the MWISP. Across benchmark instances, the proposed methodology consistently reduces computational costs compared to standard dynamic variable ordering baseline.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
