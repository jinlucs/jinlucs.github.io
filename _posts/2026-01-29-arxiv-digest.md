---
layout: post
title: "Daily arXiv Digest — 2026-01-29 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Adaptive Dimension Reduction for Overlapping Group Sparsity
- **Authors:** Yifan Bai, Clarice Poon, Jingwei Liang
- **arXiv:** [2601.20697](https://arxiv.org/abs/2601.20697v1) · [pdf](https://arxiv.org/pdf/2601.20697v1)
- **Categories:** math.OC

### Abstract
> Typical dimension reduction techniques for nonoverlapping sparse optimization involve screening or sieving strategies based on a dual certificate derived from the first-order optimality condition, approximating the gradients or exploiting certain inherent low-dimensional structure of the sparse solution. In comparison, dimension reduction rules for overlapping group sparsity are generally less developed because the subgradient structure is more complex, making the link between sparsity pattern and the dual variable indirect due to the non-separability. In this work, we propose new dual certificates for overlapping group sparsity and a novel adaptive scheme for identifying the support of the overlapping group LASSO. We demonstrate how this scheme can be integrated into and significantly accelerate existing algorithms, including Primal-Dual splitting method, alternating direction method of multipliers and a recently developed variable projection scheme based on over-parameterization. We provide convergence analysis of the method and verify its practical effectiveness through experiments on standard datasets.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Regularized Gradient Temporal-Difference Learning
- **Authors:** Hyunjun Na, Donghwan Lee
- **arXiv:** [2601.20599](https://arxiv.org/abs/2601.20599v1) · [pdf](https://arxiv.org/pdf/2601.20599v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Gradient temporal-difference (GTD) learning algorithms are widely used for off-policy policy evaluation with function approximation. However, existing convergence analyses rely on the restrictive assumption that the so-called feature interaction matrix (FIM) is nonsingular. In practice, the FIM can become singular and leads to instability or degraded performance. In this paper, we propose a regularized optimization objective by reformulating the mean-square projected Bellman error (MSPBE) minimization. This formulation naturally yields a regularized GTD algorithms, referred to as R-GTD, which guarantees convergence to a unique solution even when the FIM is singular. We establish theoretical convergence guarantees and explicit error bounds for the proposed method, and validate its effectiveness through empirical experiments.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) A penalty-interior point method combined with MADS for equality and inequality constrained optimization
- **Authors:** Charles Audet, Andrea Brilli, Youssef Diouane, Sébastien Le Digabel, Everton J. Silva, Christophe Tribes
- **arXiv:** [2601.20811](https://arxiv.org/abs/2601.20811v1) · [pdf](https://arxiv.org/pdf/2601.20811v1)
- **Categories:** math.OC

### Abstract
> This work introduces MADS-PIP, an efficient framework that integrates a penalty-interior point strategy into the mesh adaptive direct search (MADS) algorithm for solving nonsmooth blackbox optimization problems with general inequality and equality constraints. Inequality constraints are partitioned into two subsets: one treated via a logarithmic barrier applied to an aggregated interior constraint violation, and the other handled through an exterior quadratic penalty. All equality constraints are treated by the exterior penalty. A merit function defines a sequence of unconstrained subproblems, which are solved approximately using MADS, while a carefully designed update rule drives the penalty-barrier parameter to zero. In the nonsmooth setting, we establish convergence results ensuring feasibility for general constraints as well as Clarke stationarity for inequality-constrained problems. Computational experiments on both analytical test sets and challenging blackbox problems demonstrate that the proposed MADS-PIP algorithm is competitive with, and often outperforms, MADS with the progressive barrier strategy, particularly in the presence of equality constraints.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Leveraging Second-Order Curvature for Efficient Learned Image Compression: Theory and Empirical Evidence
- **Authors:** Yichi Zhang, Fengqing Zhu
- **arXiv:** [2601.20769](https://arxiv.org/abs/2601.20769v1) · [pdf](https://arxiv.org/pdf/2601.20769v1)
- **Categories:** eess.IV, cs.LG

### Abstract
> Training learned image compression (LIC) models entails navigating a challenging optimization landscape defined by the fundamental trade-off between rate and distortion. Standard first-order optimizers, such as SGD and Adam, struggle with \emph{gradient conflicts} arising from competing objectives, leading to slow convergence and suboptimal rate-distortion performance. In this work, we demonstrate that a simple utilization of a second-order quasi-Newton optimizer, \textbf{SOAP}, dramatically improves both training efficiency and final performance across diverse LICs. Our theoretical and empirical analyses reveal that Newton preconditioning inherently resolves the intra-step and inter-step update conflicts intrinsic to the R-D objective, facilitating faster, more stable convergence. Beyond acceleration, we uncover a critical deployability benefit: second-order trained models exhibit significantly fewer activation and latent outliers. This substantially enhances robustness to post-training quantization. Together, these results establish second-order optimization, achievable as a seamless drop-in replacement of the imported optimizer, as a powerful, practical tool for advancing the efficiency and real-world readiness of LICs.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) SA-PEF: Step-Ahead Partial Error Feedback for Efficient Federated Learning
- **Authors:** Dawit Kiros Redie, Reza Arablouei, Stefan Werner
- **arXiv:** [2601.20738](https://arxiv.org/abs/2601.20738v1) · [pdf](https://arxiv.org/pdf/2601.20738v1)
- **Categories:** cs.LG, cs.DC, eess.SP, math.OC, stat.ML

### Abstract
> Biased gradient compression with error feedback (EF) reduces communication in federated learning (FL), but under non-IID data, the residual error can decay slowly, causing gradient mismatch and stalled progress in the early rounds. We propose step-ahead partial error feedback (SA-PEF), which integrates step-ahead (SA) correction with partial error feedback (PEF). SA-PEF recovers EF when the step-ahead coefficient $α=0$ and step-ahead EF (SAEF) when $α=1$. For non-convex objectives and $δ$-contractive compressors, we establish a second-moment bound and a residual recursion that guarantee convergence to stationarity under heterogeneous data and partial client participation. The resulting rates match standard non-convex Fed-SGD guarantees up to constant factors, achieving $O((η,η_0TR)^{-1})$ convergence to a variance/heterogeneity floor with a fixed inner step size. Our analysis reveals a step-ahead-controlled residual contraction $ρ_r$ that explains the observed acceleration in the early training phase. To balance SAEF's rapid warm-up with EF's long-term stability, we select $α$ near its theory-predicted optimum. Experiments across diverse architectures and datasets show that SA-PEF consistently reaches target accuracy faster than EF.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
