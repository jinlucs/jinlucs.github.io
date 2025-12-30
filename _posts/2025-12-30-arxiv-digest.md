---
layout: post
title: "Daily arXiv Digest — 2025-12-30 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Clipped Gradient Methods for Nonsmooth Convex Optimization under Heavy-Tailed Noise: A Refined Analysis
- **Authors:** Zijian Liu
- **arXiv:** [2512.23178](https://arxiv.org/abs/2512.23178v1) · [pdf](https://arxiv.org/pdf/2512.23178v1)
- **Categories:** math.OC, cs.LG, stat.ML

### Abstract
> Optimization under heavy-tailed noise has become popular recently, since it better fits many modern machine learning tasks, as captured by empirical observations. Concretely, instead of a finite second moment on gradient noise, a bounded ${\frak p}$-th moment where ${\frak p}\in(1,2]$ has been recognized to be more realistic (say being upper bounded by $σ_{\frak l}^{\frak p}$ for some $σ_{\frak l}\ge0$). A simple yet effective operation, gradient clipping, is known to handle this new challenge successfully. Specifically, Clipped Stochastic Gradient Descent (Clipped SGD) guarantees a high-probability rate ${\cal O}(σ_{\frak l}\ln(1/δ)T^{1/{\frak p}-1})$ (resp. ${\cal O}(σ_{\frak l}^2\ln^2(1/δ)T^{2/{\frak p}-2})$) for nonsmooth convex (resp. strongly convex) problems, where $δ\in(0,1]$ is the failure probability and $T\in\mathbb{N}$ is the time horizon. In this work, we provide a refined analysis for Clipped SGD and offer two faster rates, ${\cal O}(σ_{\frak l}d_{\rm eff}^{-1/2{\frak p}}\ln^{1-1/{\frak p}}(1/δ)T^{1/{\frak p}-1})$ and ${\cal O}(σ_{\frak l}^2d_{\rm eff}^{-1/{\frak p}}\ln^{2-2/{\frak p}}(1/δ)T^{2/{\frak p}-2})$, than the aforementioned best results, where $d_{\rm eff}\ge1$ is a quantity we call the $\textit{generalized effective dimension}$. Our analysis improves upon the existing approach on two sides: better utilization of Freedman's inequality and finer bounds for clipping error under heavy-tailed noise. In addition, we extend the refined analysis to convergence in expectation and obtain new rates that break the known lower bounds. Lastly, to complement the study, we establish new lower bounds for both high-probability and in-expectation convergence. Notably, the in-expectation lower bounds match our new upper bounds, indicating the optimality of our refined analysis for convergence in expectation.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Joint Link Adaptation and Device Scheduling Approach for URLLC Industrial IoT Network: A DRL-based Method with Bayesian Optimization
- **Authors:** Wei Gao, Paul Zheng, Peng Wu, Yulin Hu, Anke Schmeink
- **arXiv:** [2512.23493](https://arxiv.org/abs/2512.23493v1) · [pdf](https://arxiv.org/pdf/2512.23493v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> In this article, we consider an industrial internet of things (IIoT) network supporting multi-device dynamic ultra-reliable low-latency communication (URLLC) while the channel state information (CSI) is imperfect. A joint link adaptation (LA) and device scheduling (including the order) design is provided, aiming at maximizing the total transmission rate under strict block error rate (BLER) constraints. In particular, a Bayesian optimization (BO) driven Twin Delayed Deep Deterministic Policy Gradient (TD3) method is proposed, which determines the device served order sequence and the corresponding modulation and coding scheme (MCS) adaptively based on the imperfect CSI. Note that the imperfection of CSI, error sample imbalance in URLLC networks, as well as the parameter sensitivity nature of the TD3 algorithm likely diminish the algorithm's convergence speed and reliability. To address such an issue, we proposed a BO based training mechanism for the convergence speed improvement, which provides a more reliable learning direction and sample selection method to track the imbalance sample problem. Via extensive simulations, we show that the proposed algorithm achieves faster convergence and higher sum-rate performance compared to existing solutions.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Dynamic Subspace Composition: Efficient Adaptation via Contractive Basis Expansion
- **Authors:** Vladimer Khasia
- **arXiv:** [2512.23448](https://arxiv.org/abs/2512.23448v1) · [pdf](https://arxiv.org/pdf/2512.23448v1)
- **Categories:** cs.LG

### Abstract
> Mixture of Experts (MoE) models scale capacity but often suffer from representation collapse and gradient instability. We propose Dynamic Subspace Composition (DSC), a framework that approximates context-dependent weights via a state-dependent, sparse expansion of a shared basis bank. Formally, DSC models the weight update as a residual trajectory within a Star- Shaped Domain, employing a Magnitude-Gated Simplex Interpolation to ensure continuity at the identity. Unlike standard Mixture-of-LoRAs, which incurs O(M rd) parameter complexity by retrieving independent rank-r matrices, DSC constructs a compositional rank-K approximation from decoupled unit-norm basis vectors. This reduces parameter complexity to O(M d) and memory traffic to O(Kd), while Frame-Theoretic regularization and spectral constraints provide rigorous worst-case bounds on the dynamic update. The code is available at https://github. com/VladimerKhasia/DSC

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) ISOPO: Proximal policy gradients without pi-old
- **Authors:** Nilin Abrahamsen
- **arXiv:** [2512.23353](https://arxiv.org/abs/2512.23353v1) · [pdf](https://arxiv.org/pdf/2512.23353v1)
- **Categories:** cs.LG

### Abstract
> This note introduces Isometric Policy Optimization (ISOPO), an efficient method to approximate the natural policy gradient in a single gradient step. In comparison, existing proximal policy methods such as GRPO or CISPO use multiple gradient steps with variants of importance ratio clipping to approximate a natural gradient step relative to a reference policy. In its simplest form, ISOPO normalizes the log-probability gradient of each sequence in the Fisher metric before contracting with the advantages. Another variant of ISOPO transforms the microbatch advantages based on the neural tangent kernel in each layer. ISOPO applies this transformation layer-wise in a single backward pass and can be implemented with negligible computational overhead compared to vanilla REINFORCE.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Spectral Analysis of Hard-Constraint PINNs: The Spatial Modulation Mechanism of Boundary Functions
- **Authors:** Yuchen Xie, Honghang Chi, Haopeng Quan, Yahui Wang, Wei Wang, Yu Ma
- **arXiv:** [2512.23295](https://arxiv.org/abs/2512.23295v1) · [pdf](https://arxiv.org/pdf/2512.23295v1)
- **Categories:** cs.LG, physics.comp-ph

### Abstract
> Physics-Informed Neural Networks with hard constraints (HC-PINNs) are increasingly favored for their ability to strictly enforce boundary conditions via a trial function ansatz $\tilde{u} = A + B \cdot N$, yet the theoretical mechanisms governing their training dynamics have remained unexplored. Unlike soft-constrained formulations where boundary terms act as additive penalties, this work reveals that the boundary function $B$ introduces a multiplicative spatial modulation that fundamentally alters the learning landscape. A rigorous Neural Tangent Kernel (NTK) framework for HC-PINNs is established, deriving the explicit kernel composition law. This relationship demonstrates that the boundary function $B(\vec{x})$ functions as a spectral filter, reshaping the eigenspectrum of the neural network's native kernel. Through spectral analysis, the effective rank of the residual kernel is identified as a deterministic predictor of training convergence, superior to classical condition numbers. It is shown that widely used boundary functions can inadvertently induce spectral collapse, leading to optimization stagnation despite exact boundary satisfaction. Validated across multi-dimensional benchmarks, this framework transforms the design of boundary functions from a heuristic choice into a principled spectral optimization problem, providing a solid theoretical foundation for geometric hard constraints in scientific machine learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
