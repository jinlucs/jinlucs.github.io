---
layout: post
title: "Daily arXiv Digest — 2026-04-10 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Inexact Limited Memory Bundle Method
- **Authors:** Jenni Lampainen, Kaisa Joki, Napsu Karmitsa, Marko M. Mäkelä
- **arXiv:** [2604.08067](https://arxiv.org/abs/2604.08067v1) · [pdf](https://arxiv.org/pdf/2604.08067v1)
- **Categories:** math.OC

### Abstract
> Large-scale nonsmooth optimization problems arise in many real-world applications, but obtaining exact function and subgradient values for these problems may be computationally expensive or even infeasible. In many practical settings, only inexact information is available due to measurement or modeling errors, privacy-preserving computations, or stochastic approximations, making inexact optimization methods particularly relevant. In this paper, we propose a novel inexact limited memory bundle method for large-scale nonsmooth nonconvex optimization. The method tolerates noise in both function values and subgradients. We prove the global convergence of the proposed method to an approximate stationary point. Numerical experiments with different levels of noise in function and/or subgradient values show that the method performs well with both exact and noisy data. In particular, the results demonstrate competitiveness in large-scale nonsmooth optimization and highlight the suitability of the method for applications where noise is unavoidable, such as differential privacy in machine learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Density-Driven Optimal Control: Convergence Guarantees for Stochastic LTI Multi-Agent Systems
- **Authors:** Kooktae Lee
- **arXiv:** [2604.08495](https://arxiv.org/abs/2604.08495v1) · [pdf](https://arxiv.org/pdf/2604.08495v1)
- **Categories:** math.OC, cs.MA, cs.RO, eess.SY

### Abstract
> This paper addresses the decentralized non-uniform area coverage problem for multi-agent systems, a critical task in missions with high spatial priority and resource constraints. While existing density-based methods often rely on computationally heavy Eulerian PDE solvers or heuristic planning, we propose Stochastic Density-Driven Optimal Control (D$^2$OC). This is a rigorous Lagrangian framework that bridges the gap between individual agent dynamics and collective distribution matching. By formulating a stochastic MPC-like problem that minimizes the Wasserstein distance as a running cost, our approach ensures that the time-averaged empirical distribution converges to a non-parametric target density under stochastic LTI dynamics. A key contribution is the formal convergence guarantee established via reachability analysis, providing a bounded tracking error even in the presence of process and measurement noise. Numerical results verify that Stochastic D$^2$OC achieves robust, decentralized coverage while outperforming previous heuristic methods in optimality and consistency.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Improved Convergence for Decentralized Stochastic Optimization with Biased Gradients
- **Authors:** Qing Xu, Yiwei Liao, Wenqi Fan, Xingxing You, Songyi Dian
- **arXiv:** [2604.08236](https://arxiv.org/abs/2604.08236v1) · [pdf](https://arxiv.org/pdf/2604.08236v1)
- **Categories:** math.OC

### Abstract
> Decentralized stochastic optimization has emerged as a fundamental paradigm for large-scale machine learning. However, practical implementations often rely on biased gradient estimators arising from communication compression or inexact local oracles, which severely degrade convergence in the presence of data heterogeneity. To address the challenge, we propose Decentralized Momentum Tracking with Biased Gradients (Biased-DMT), a novel decentralized algorithm designed to operate reliably under biased gradient information. We establish a comprehensive convergence theory for Biased-DMT in nonconvex settings and show that it achieves linear speedup with respect to the number of agents. The theoretical analysis shows that Biased-DMT decouples the effects of network topology from data heterogeneity, enabling robust performance even in sparse communication networks. Notably, when the gradient oracle introduces only absolute bias, the proposed method eliminates the structural heterogeneity error and converges to the exact physical error floor. For the case of relative bias, we further characterize the convergence limit and show that the remaining error is an unavoidable physical consequence of locally injected noise. Extensive numerical experiments corroborate our theoretical analysis and demonstrate the practical effectiveness of Biased-DMT across a range of decentralized learning scenarios.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs
- **Authors:** Wenqi Fan, Yiwei Liao, Qing Xu, Bin Guo, Songyi Dian
- **arXiv:** [2604.08219](https://arxiv.org/abs/2604.08219v1) · [pdf](https://arxiv.org/pdf/2604.08219v1)
- **Categories:** math.OC

### Abstract
> Decentralized optimization over directed networks is frequently challenged by asymmetric communication and the inherent high variance of stochastic gradients, which collectively cause severe oscillations and hinder algorithmic convergence. To address these challenges, we propose the Stochastic Momentum Tracking Push-Pull (SMTPP) algorithm, which tracks the momentum term rather than raw stochastic gradients within the Push-Pull architecture. This design successfully decouples the variance reduction capacity from the algebraic connectivity of the graph.Although the inherent topology mismatch of directed graphs precludes exact convergence under persistent stochastic noise, SMTPP rigorously compresses this unavoidable steady-state error floor into a minimal neighborhood determined by network connectivity and gradient variance. Furthermore, SMTPP guarantees convergence on any strongly connected directed graph. Extensive experiments on non-convex logistic regression demonstrate that the algorithm is highly robust to network connectivity. By effectively dampening topology-induced oscillations, SMTPP achieves convergence rates and overall performance that closely match those of centralized baselines, regardless of whether the network is sparse or dense.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Dead Weights, Live Signals: Feedforward Graphs of Frozen Language Models
- **Authors:** Marcus Armstrong, Navid Ayoobi, Arjun Mukherjee
- **arXiv:** [2604.08335](https://arxiv.org/abs/2604.08335v1) · [pdf](https://arxiv.org/pdf/2604.08335v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> We present a feedforward graph architecture in which heterogeneous frozen large language models serve as computational nodes, communicating through a shared continuous latent space via learned linear projections. Building on recent work demonstrating geometric compatibility between independently trained LLM latent spaces~\cite{armstrong2026thinking}, we extend this finding from static two-model steering to end-to-end trainable multi-node graphs, where projection matrices are optimized jointly via backpropagation through residual stream injection hooks. Three small frozen models (Llama-3.2-1B, Qwen2.5-1.5B, Gemma-2-2B) encode the input into a shared latent space whose aggregate signal is injected into two larger frozen models (Phi-3-mini, Mistral-7B), whose representations feed a lightweight cross-attention output node. With only 17.6M trainable parameters against approximately 12B frozen, the architecture achieves 87.3\% on ARC-Challenge, 82.8\% on OpenBookQA, and 67.2\% on MMLU, outperforming the best single constituent model by 11.4, 6.2, and 1.2 percentage points respectively, and outperforming parameter-matched learned classifiers on frozen single models by 9.1, 5.2, and 6.7 points. Gradient flow through multiple frozen model boundaries is empirically verified to be tractable, and the output node develops selective routing behavior across layer-2 nodes without explicit supervision.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
