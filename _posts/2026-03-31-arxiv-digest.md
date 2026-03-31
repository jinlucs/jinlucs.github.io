---
layout: post
title: "Daily arXiv Digest — 2026-03-31 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) On the Convergence of Proximal Algorithms for Weakly-convex Min-max Optimization
- **Authors:** Guido Tapia-Riera, Camille Castera, Nicolas Papadakis
- **arXiv:** [2603.28484](https://arxiv.org/abs/2603.28484v1) · [pdf](https://arxiv.org/pdf/2603.28484v1)
- **Categories:** math.OC

### Abstract
> We study alternating first-order algorithms with no inner loops for solving nonconvex-strongly-concave min-max problems. We show the convergence of the alternating gradient descent--ascent algorithm method by proposing a substantially simplified proof compared to previous ones. It allows us to enlarge the set of admissible step-sizes. Building on this general reformulation, we also prove the convergence of a doubly proximal algorithm in the weakly convex-strongly concave setting. Finally, we show how this new result opens the way to new applications of min-max optimization algorithms for solving regularized imaging inverse problems with neural networks in a plug-and-play manner.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Machine Learning-Assisted High-Dimensional Matrix Estimation
- **Authors:** Wan Tian, Hui Yang, Zhouhui Lian, Lingyue Zhang, Yijie Peng
- **arXiv:** [2603.28346](https://arxiv.org/abs/2603.28346v1) · [pdf](https://arxiv.org/pdf/2603.28346v1)
- **Categories:** cs.LG, stat.ML

### Abstract
> Efficient estimation of high-dimensional matrices-including covariance and precision matrices-is a cornerstone of modern multivariate statistics. Most existing studies have focused primarily on the theoretical properties of the estimators (e.g., consistency and sparsity), while largely overlooking the computational challenges inherent in high-dimensional settings. Motivated by recent advances in learning-based optimization method-which integrate data-driven structures with classical optimization algorithms-we explore high-dimensional matrix estimation assisted by machine learning. Specifically, for the optimization problem of high-dimensional matrix estimation, we first present a solution procedure based on the Linearized Alternating Direction Method of Multipliers (LADMM). We then introduce learnable parameters and model the proximal operators in the iterative scheme with neural networks, thereby improving estimation accuracy and accelerating convergence. Theoretically, we first prove the convergence of LADMM, and then establish the convergence, convergence rate, and monotonicity of its reparameterized counterpart; importantly, we show that the reparameterized LADMM enjoys a faster convergence rate. Notably, the proposed reparameterization theory and methodology are applicable to the estimation of both high-dimensional covariance and precision matrices. We validate the effectiveness of our method by comparing it with several classical optimization algorithms across different structures and dimensions of high-dimensional matrices.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Taming the Instability: A Robust Second-Order Optimizer for Federated Learning over Non-IID Data
- **Authors:** Yuanqiao Zhang, Tiantian He, Yuan Gao, Yixin Wang, Yew-Soon Ong, Maoguo Gong, A. K. Qin, Hui Li
- **arXiv:** [2603.28316](https://arxiv.org/abs/2603.28316v1) · [pdf](https://arxiv.org/pdf/2603.28316v1)
- **Categories:** cs.LG

### Abstract
> In this paper, we present Federated Robust Curvature Optimization (FedRCO), a novel second-order optimization framework designed to improve convergence speed and reduce communication cost in Federated Learning systems under statistical heterogeneity. Existing second-order optimization methods are often computationally expensive and numerically unstable in distributed settings. In contrast, FedRCO addresses these challenges by integrating an efficient approximate curvature optimizer with a provable stability mechanism. Specifically, FedRCO incorporates three key components: (1) a Gradient Anomaly Monitor that detects and mitigates exploding gradients in real-time, (2) a Fail-Safe Resilience protocol that resets optimization states upon numerical instability, and (3) a Curvature-Preserving Adaptive Aggregation strategy that safely integrates global knowledge without erasing the local curvature geometry. Theoretical analysis shows that FedRCO can effectively mitigate instability and prevent unbounded updates while preserving optimization efficiency. Extensive experiments show that FedRCO achieves superior robustness against diverse non-IID scenarios while achieving higher accuracy and faster convergence than both state-of-the-art first-order and second-order methods.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Bundle EXTRA for Decentralized Optimization
- **Authors:** Haijuan Liu, Zhuoqing Zheng, Cong Li, Wenying Xu, Xuyang Wu
- **arXiv:** [2603.28220](https://arxiv.org/abs/2603.28220v1) · [pdf](https://arxiv.org/pdf/2603.28220v1)
- **Categories:** math.OC

### Abstract
> Decentralized primal-dual methods are widely used for solving decentralized optimization problems, but their updates often rely on the potentially crude first-order Taylor approximations of the objective functions, which can limit convergence speed. To overcome this, we replace the first-order Taylor approximation in the primal update of EXTRA, which can be interpreted as a primal-dual method, with a more accurate multi-cut bundle model, resulting in a fully decentralized bundle EXTRA method. The bundle model incorporates historical information to improve the approximation accuracy, potentially leading to faster convergence. Under mild assumptions, we show that a KKT residual converges to zero. Numerical experiments on decentralized least-squares problems demonstrate that, compared to EXTRA, the bundle EXTRA method converges faster and is more robust to step-size choices.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Constrained Optimization on Matrix Lie Groups via Interior-Point Method
- **Authors:** Aclécio J. Santos, Jean C. Pereira, Guilherme V. Raffo
- **arXiv:** [2603.28747](https://arxiv.org/abs/2603.28747v1) · [pdf](https://arxiv.org/pdf/2603.28747v1)
- **Categories:** math.OC, eess.SY

### Abstract
> This paper proposes an interior-point framework for constrained optimization problems whose decision variables evolve on matrix Lie groups. The proposed method, termed the Matrix Lie Group Interior-Point Method (MLG-IPM), operates directly on the group structure using a minimal Lie algebra parametrization, avoiding redundant matrix representations and eliminating explicit dependence on Riemannian metrics. A primal-dual formulation is developed in which the Newton system is constructed through sensitivity and curvature matrices. Also, multiplicative updates are performed via the exponential map, ensuring intrinsic feasibility with respect to the group structure while maintaining strict positivity of slack and dual variables through a barrier strategy. A local analysis establishes quadratic convergence under standard regularity assumptions and characterizes the behavior under inexact Newton steps. Statistical comparisons against Riemannian Interior-Point Methods, specifically for optimization problems defined over the Special Orthogonal Group SO(n) and Special Linear Group SL(n), demonstrate that the proposed approach achieves higher success rates, fewer iterations, and superior numerical accuracy. Furthermore, its robustness under perturbations suggests that this method serves as a consistent and reliable alternative for structured manifold optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
