---
layout: post
title: "Daily arXiv Digest — 2026-01-28 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Revisiting Incremental Stochastic Majorization-Minimization Algorithms with Applications to Mixture of Experts
- **Authors:** TrungKhang Tran, TrungTin Nguyen, Gersende Fort, Tung Doan, Hien Duy Nguyen, Binh T. Nguyen, Florence Forbes, Christopher Drovandi
- **arXiv:** [2601.19811](https://arxiv.org/abs/2601.19811v1) · [pdf](https://arxiv.org/pdf/2601.19811v1)
- **Categories:** stat.ML, cs.AI, cs.LG, math.ST, stat.ME

### Abstract
> Processing high-volume, streaming data is increasingly common in modern statistics and machine learning, where batch-mode algorithms are often impractical because they require repeated passes over the full dataset. This has motivated incremental stochastic estimation methods, including the incremental stochastic Expectation-Maximization (EM) algorithm formulated via stochastic approximation. In this work, we revisit and analyze an incremental stochastic variant of the Majorization-Minimization (MM) algorithm, which generalizes incremental stochastic EM as a special case. Our approach relaxes key EM requirements, such as explicit latent-variable representations, enabling broader applicability and greater algorithmic flexibility. We establish theoretical guarantees for the incremental stochastic MM algorithm, proving consistency in the sense that the iterates converge to a stationary point characterized by a vanishing gradient of the objective. We demonstrate these advantages on a softmax-gated mixture of experts (MoE) regression problem, for which no stochastic EM algorithm is available. Empirically, our method consistently outperforms widely used stochastic optimizers, including stochastic gradient descent, root mean square propagation, adaptive moment estimation, and second-order clipped stochastic optimization. These results support the development of new incremental stochastic algorithms, given the central role of softmax-gated MoE architectures in contemporary deep neural networks for heterogeneous data modeling. Beyond synthetic experiments, we also validate practical effectiveness on two real-world datasets, including a bioinformatics study of dent maize genotypes under drought stress that integrates high-dimensional proteomics with ecophysiological traits, where incremental stochastic MM yields stable gains in predictive performance.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Stability and Generalization of Nonconvex Optimization with Heavy-Tailed Noise
- **Authors:** Hongxu Chen, Ke Wei, Xiaoming Yuan, Luo Luo
- **arXiv:** [2601.19730](https://arxiv.org/abs/2601.19730v1) · [pdf](https://arxiv.org/pdf/2601.19730v1)
- **Categories:** cs.LG

### Abstract
> The empirical evidence indicates that stochastic optimization with heavy-tailed gradient noise is more appropriate to characterize the training of machine learning models than that with standard bounded gradient variance noise. Most existing works on this phenomenon focus on the convergence of optimization errors, while the analysis for generalization bounds under the heavy-tailed gradient noise remains limited. In this paper, we develop a general framework for establishing generalization bounds under heavy-tailed noise. Specifically, we introduce a truncation argument to achieve the generalization error bound based on the algorithmic stability under the assumption of bounded $p$th centered moment with $p\in(1,2]$. Building on this framework, we further provide the stability and generalization analysis for several popular stochastic algorithms under heavy-tailed noise, including clipped and normalized stochastic gradient descent, as well as their mini-batch and momentum variants.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Post-LayerNorm Is Back: Stable, ExpressivE, and Deep
- **Authors:** Chen Chen, Lai Wei
- **arXiv:** [2601.19895](https://arxiv.org/abs/2601.19895v1) · [pdf](https://arxiv.org/pdf/2601.19895v1)
- **Categories:** cs.LG, cs.CL

### Abstract
> Large language model (LLM) scaling is hitting a wall. Widening models yields diminishing returns, and extending context length does not improve fundamental expressivity. In contrast, depth scaling offers theoretically superior expressivity, yet current Transformer architectures struggle to train reliably at extreme depths. We revisit the Post-LayerNorm (Post-LN) formulation, whose instability at scale caused its replacement by Pre-LN in modern LLMs. We show that the central failure mode of Post-LN arises from the ResNet-style residual pathway, which introduces gradient vanishing in deep networks. We present Keel, a Post-LN Transformer that replaces this residual path with a Highway-style connection. This modification preserves the gradient flow through the residual branch, preventing signal vanishing from the top layers to the bottom. Unlike prior methods, Keel enables stable training at extreme depths without requiring specialized initialization or complex optimization tricks. Keel trains robustly at depths exceeding 1000 layers and consistently improves perplexity and depth-scaling characteristics over Pre-LN. These findings indicate that Post-LN, when paired with a Highway-style connection, provides a simple and effective foundation for building deeply scalable LLMs, opening the possibility for future infinite-depth architectures.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Learn and Verify: A Framework for Rigorous Verification of Physics-Informed Neural Networks
- **Authors:** Kazuaki Tanaka, Kohei Yatabe
- **arXiv:** [2601.19818](https://arxiv.org/abs/2601.19818v1) · [pdf](https://arxiv.org/pdf/2601.19818v1)
- **Categories:** cs.LG, math.NA

### Abstract
> The numerical solution of differential equations using neural networks has become a central topic in scientific computing, with Physics-Informed Neural Networks (PINNs) emerging as a powerful paradigm for both forward and inverse problems. However, unlike classical numerical methods that offer established convergence guarantees, neural network-based approximations typically lack rigorous error bounds. Furthermore, the non-deterministic nature of their optimization makes it difficult to mathematically certify their accuracy. To address these challenges, we propose a "Learn and Verify" framework that provides computable, mathematically rigorous error bounds for the solutions of differential equations. By combining a novel Doubly Smoothed Maximum (DSM) loss for training with interval arithmetic for verification, we compute rigorous a posteriori error bounds as machine-verifiable proofs. Numerical experiments on nonlinear Ordinary Differential Equations (ODEs), including problems with time-varying coefficients and finite-time blow-up, demonstrate that the proposed framework successfully constructs rigorous enclosures of the true solutions, establishing a foundation for trustworthy scientific machine learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) A refined nonlinear least-squares method for the rational approximation problem
- **Authors:** Michael S. Ackermann, Linus Balicki, Serkan Gugercin, Steffen W. R. Werner
- **arXiv:** [2601.19813](https://arxiv.org/abs/2601.19813v1) · [pdf](https://arxiv.org/pdf/2601.19813v1)
- **Categories:** math.NA, eess.SY, math.DS, math.OC

### Abstract
> The adaptive Antoulas-Anderson (AAA) algorithm for rational approximation is a widely used method for the efficient construction of highly accurate rational approximations to given data. While AAA can often produce rational approximations accurate to any prescribed tolerance, these approximations may have degrees larger than what is actually required to meet the given tolerance. In this work, we consider the adaptive construction of interpolating rational approximations while aiming for the smallest feasible degree to satisfy a given error tolerance. To this end, we introduce refinement approaches to the linear least-squares step of the classical AAA algorithm that aim to minimize the true nonlinear least-squares error with respect to the given data. Furthermore, we theoretically analyze the derived approaches in terms of the corresponding gradients from the resulting minimization problems and use these insights to propose a new greedy framework that ensures monotonic error convergence. Numerical examples from function approximation and model order reduction verify the effectiveness of the proposed algorithm to construct accurate rational approximations of small degrees.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
