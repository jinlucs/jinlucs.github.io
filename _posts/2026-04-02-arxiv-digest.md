---
layout: post
title: "Daily arXiv Digest — 2026-04-02 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Affine Normal Directions via Log-Determinant Geometry: Scalable Computation under Sparse Polynomial Structure
- **Authors:** Yi-Shuai Niu, Artan Sheshmani, Shing-Tung Yau
- **arXiv:** [2604.01163](https://arxiv.org/abs/2604.01163v1) · [pdf](https://arxiv.org/pdf/2604.01163v1)
- **Categories:** math.OC, math.AG, math.DG, math.NA

### Abstract
> Affine normal directions provide intrinsic affine-invariant descent directions derived from the geometry of level sets. Their practical use, however, has long been hindered by the need to evaluate third-order derivatives and invert tangent Hessians, which becomes computationally prohibitive in high dimensions. In this paper, we show that affine normal computation admits an exact reduction to second-order structure: the classical third-order contraction term is precisely the gradient of the log-determinant of the tangent Hessian. This identity replaces explicit third-order tensor contraction by a matrix-free formulation based on tangent linear solves, Hessian-vector products, and log-determinant gradient evaluation. Building on this reduction, we develop exact and stochastic matrix-free procedures for affine normal evaluation. For sparse polynomial objectives, the algebraic closure of derivatives further yields efficient sparse kernels for gradients, Hessian-vector products, and directional third-order contractions, leading to scalable implementations whose cost is governed by the sparsity structure of the polynomial representation. We establish end-to-end complexity bounds showing near-linear scaling with respect to the relevant sparsity scale under fixed stochastic and Krylov budgets. Numerical experiments confirm that the proposed MF-LogDet formulation reproduces the original autodifferentiation-based affine normal direction to near machine precision, delivers substantial runtime improvements in moderate and high dimensions, and exhibits empirical near-linear scaling in both dimension and sparsity. These results provide a practical computational route for affine normal evaluation and reveal a new connection between affine differential geometry, log-determinant curvature, and large-scale structured optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Approximating Pareto Frontiers in Stochastic Multi-Objective Optimization via Hashing and Randomization
- **Authors:** Jinzhao Li, Nan Jiang, Yexiang Xue
- **arXiv:** [2604.01098](https://arxiv.org/abs/2604.01098v1) · [pdf](https://arxiv.org/pdf/2604.01098v1)
- **Categories:** cs.LG, cs.AI, cs.LO

### Abstract
> Stochastic Multi-Objective Optimization (SMOO) is critical for decision-making trading off multiple potentially conflicting objectives in uncertain environments. SMOO aims at identifying the Pareto frontier, which contains all mutually non-dominating decisions. The problem is highly intractable due to the embedded probabilistic inference, such as computing the marginal, posterior probabilities, or expectations. Existing methods, such as scalarization, sample average approximation, and evolutionary algorithms, either offer arbitrarily loose approximations or may incur prohibitive computational costs. We propose XOR-SMOO, a novel algorithm that with probability $1-δ$, obtains $γ$-approximate Pareto frontiers ($γ>1$) for SMOO by querying an SAT oracle poly-log times in $γ$ and $δ$. A $γ$-approximate Pareto frontier is only below the true frontier by a fixed, multiplicative factor $γ$. Thus, XOR-SMOO solves highly intractable SMOO problems (\#P-hard) with only queries to SAT oracles while obtaining tight, constant factor approximation guarantees. Experiments on real-world road network strengthening and supply chain design problems demonstrate that XOR-SMOO outperforms several baselines in identifying Pareto frontiers that have higher objective values, better coverage of the optimal solutions, and the solutions found are more evenly distributed. Overall, XOR-SMOO significantly enhanced the practicality and reliability of SMOO solvers.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Bridging Structured Knowledge and Data: A Unified Framework with Finance Applications
- **Authors:** Yi Cao, Zexun Chen, Lin William Cong, Heqing Shi
- **arXiv:** [2604.00987](https://arxiv.org/abs/2604.00987v1) · [pdf](https://arxiv.org/pdf/2604.00987v1)
- **Categories:** stat.ML, cs.AI, cs.LG

### Abstract
> We develop Structured-Knowledge-Informed Neural Networks (SKINNs), a unified estimation framework that embeds theoretical, simulated, previously learned, or cross-domain insights as differentiable constraints within flexible neural function approximation. SKINNs jointly estimate neural network parameters and economically meaningful structural parameters in a single optimization problem, enforcing theoretical consistency not only on observed data but over a broader input domain through collocation, and therefore nesting approaches such as functional GMM, Bayesian updating, transfer learning, PINNs, and surrogate modeling. SKINNs define a class of M-estimators that are consistent and asymptotically normal with root-N convergence, sandwich covariance, and recovery of pseudo-true parameters under misspecification. We establish identification of structural parameters under joint flexibility, derive generalization and target-risk bounds under distributional shift in a convex proxy, and provide a restricted-optimal characterization of the weighting parameter that governs the bias-variance tradeoff. In an illustrative financial application to option pricing, SKINNs improve out-of-sample valuation and hedging performance, particularly at longer horizons and during high-volatility regimes, while recovering economically interpretable structural parameters with improved stability relative to conventional calibration. More broadly, SKINNs provide a general econometric framework for combining model-based reasoning with high-dimensional, data-driven estimation.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) WARP: Guaranteed Inner-Layer Repair of NLP Transformers
- **Authors:** Hsin-Ling Hsu, Min-Yu Chen, Nai-Chia Chen, Yan-Ru Chen, Yi-Ling Chang, Fang Yu
- **arXiv:** [2604.00938](https://arxiv.org/abs/2604.00938v1) · [pdf](https://arxiv.org/pdf/2604.00938v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Transformer-based NLP models remain vulnerable to adversarial perturbations, yet existing repair methods face a fundamental trade-off: gradient-based approaches offer flexibility but lack verifiability and often overfit; methods that do provide repair guarantees are restricted to the final layer or small networks, significantly limiting the parameter search space available for repair. We present WARP (Weight-Adjusted Repair with Provability), a constraint-based repair framework that extends repair beyond the last layer of Transformer models. WARP formulates repair as a convex quadratic program derived from a first-order linearization of the logit gap, enabling tractable optimization over a high-dimensional parameter space. Under the condition that the first-order approximation holds, this formulation induces three per-sample guarantees: (i) a positive margin constraint ensuring correct classification on repaired inputs, (ii) preservation constraints over a designated remain set, and (iii) a certified robustness radius derived from Lipschitz continuity. To ensure feasibility across varying model architectures, we introduce a sensitivity-based preprocessing step that conditions the optimization landscape accordingly. We further show that the iterative optimization procedure converges to solutions satisfying all repair constraints under mild assumptions. Empirical evaluation on encoder-only Transformers with varying layer architectures validates that these guarantees hold in practice while improving robustness to adversarial inputs. Our results demonstrate that guaranteed, generalizable Transformer repair is achievable through principled constraint-based optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Routing-Free Mixture-of-Experts
- **Authors:** Yilun Liu, Jinru Han, Sikuan Yan, Volker Tresp, Yunpu Ma
- **arXiv:** [2604.00801](https://arxiv.org/abs/2604.00801v1) · [pdf](https://arxiv.org/pdf/2604.00801v1)
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Standard Mixture-of-Experts (MoE) models rely on centralized routing mechanisms that introduce rigid inductive biases. We propose Routing-Free MoE which eliminates any hard-coded centralized designs including external routers, Softmax, Top-K and load balancing, instead encapsulating all activation functionalities within individual experts and directly optimized through continuous gradient flow, enabling each expert to determine its activation entirely on its own. We introduce a unified adaptive load-balancing framework to simultaneously optimize both expert-balancing and token-balancing objectives through a configurable interpolation, allowing flexible and customizable resource allocation. Extensive experiments show that Routing-Free MoE can consistently outperform baselines with better scalability and robustness. We analyze its behavior in detail and offer insights that may facilitate future MoE design ad optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
