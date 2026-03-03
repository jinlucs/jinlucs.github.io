---
layout: post
title: "Daily arXiv Digest — 2026-03-03 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Accelerating Single-Pass SGD for Generalized Linear Prediction
- **Authors:** Qian Chen, Shihong Ding, Cong Fang
- **arXiv:** [2603.01951](https://arxiv.org/abs/2603.01951v1) · [pdf](https://arxiv.org/pdf/2603.01951v1)
- **Categories:** cs.LG, math.OC, stat.ML

### Abstract
> We study generalized linear prediction under a streaming setting, where each iteration uses only one fresh data point for a gradient-level update. While momentum is well-established in deterministic optimization, a fundamental open question is whether it can accelerate such single-pass non-quadratic stochastic optimization. We propose the first algorithm that successfully incorporates momentum via a novel data-dependent proximal method, achieving dual-momentum acceleration. Our derived excess risk bound decomposes into three components: an improved optimization error, a minimax optimal statistical error, and a higher-order model-misspecification error. The proof handles mis-specification via a fine-grained stationary analysis of inner updates, while localizing statistical error through a two-phase outer-loop analysis. As a result, we resolve the open problem posed by Jain et al. [2018a] and demonstrate that momentum acceleration is more effective than variance reduction for generalized linear prediction in the streaming setting.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Multiresolution Adaptive Block-Coordinate Forward-Backward for Image Reconstruction
- **Authors:** Edgar Desainte-Maréville, Marion Foare, Paulo Gonçalves, Nelly Pustelnik, Elisa Riccietti
- **arXiv:** [2603.01860](https://arxiv.org/abs/2603.01860v1) · [pdf](https://arxiv.org/pdf/2603.01860v1)
- **Categories:** eess.SP, math.OC

### Abstract
> Classical first-order optimization methods for imaging inverse problems scale poorly with image resolution. Wavelet based multilevel strategies can accelerate convergence under strong blur, but their fixed coarse-to-fine schedules lose effectiveness in moderate-blur or noise-dominated regimes. In this work, we propose an adaptive multiresolution block coordinate Forward-Backward algorithm for image restoration. Multiresolution block selection is driven by the local magnitude of the proximal update via a stochastic non-smooth Gauss-Southwell rule applied to the wavelet decomposition of the image. This adaptive selection strategy dynamically balances updates across scales, emphasizing coarse or fine blocks according to the degradation regime. As a result, the proposed method automatically adapts to varying blur and noise levels without relying on a predefined hierarchical update scheme.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Never Saddle for Reparameterized Steepest Descent as Mirror Flow
- **Authors:** Tom Jacobs, Chao Zhou, Rebekka Burkholz
- **arXiv:** [2603.02064](https://arxiv.org/abs/2603.02064v1) · [pdf](https://arxiv.org/pdf/2603.02064v1)
- **Categories:** cs.LG

### Abstract
> How does the choice of optimization algorithm shape a model's ability to learn features? To address this question for steepest descent methods --including sign descent, which is closely related to Adam --we introduce steepest mirror flows as a unifying theoretical framework. This framework reveals how optimization geometry governs learning dynamics, implicit bias, and sparsity and it provides two explanations for why Adam and AdamW often outperform SGD in fine-tuning. Focusing on diagonal linear networks and deep diagonal linear reparameterizations (a simplified proxy for attention), we show that steeper descent facilitates both saddle-point escape and feature learning. In contrast, gradient descent requires unrealistically large learning rates to escape saddles, an uncommon regime in fine-tuning. Empirically, we confirm that saddle-point escape is a central challenge in fine-tuning. Furthermore, we demonstrate that decoupled weight decay, as in AdamW, stabilizes feature learning by enforcing novel balance equations. Together, these results highlight two mechanisms how steepest descent can aid modern optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) CausalWrap: Model-Agnostic Causal Constraint Wrappers for Tabular Synthetic Data
- **Authors:** Amir Asiaee, Zhuohui J. Liang, Chao Yan
- **arXiv:** [2603.02015](https://arxiv.org/abs/2603.02015v1) · [pdf](https://arxiv.org/pdf/2603.02015v1)
- **Categories:** cs.LG

### Abstract
> Tabular synthetic data generators are typically trained to match observational distributions, which can yield high conventional utility (e.g., column correlations, predictive accuracy) yet poor preservation of structural relations relevant to causal analysis and out-of-distribution (OOD) reasoning. When the downstream use of synthetic data involves causal reasoning -- estimating treatment effects, evaluating policies, or testing mediation pathways -- merely matching the observational distribution is insufficient: structural fidelity and treatment-mechanism preservation become essential. We propose CausalWrap (CW), a model-agnostic wrapper that injects partial causal knowledge (PCK) -- trusted edges, forbidden edges, and qualitative/monotonic constraints -- into any pretrained base generator (GAN, VAE, or diffusion model), without requiring access to its internals. CW learns a lightweight, differentiable post-hoc correction map applied to samples from the base generator, optimized with causal penalty terms under an augmented-Lagrangian schedule. We provide theoretical results connecting penalty-based optimization to constraint satisfaction and relating approximate factorization to joint distributional control. We validate CW on simulated structural causal models (SCMs) with known ground-truth interventions, semi-synthetic causal benchmarks (IHDP and an ACIC-style suite), and a real-world ICU cohort (MIMIC-IV) with expert-elicited partial graphs. CW improves causal fidelity across diverse base generators -- e.g., reducing average treatment effect (ATE) error by up to 63% on ACIC and lifting ATE agreement from 0.00 to 0.38 on the intensive care unit (ICU) cohort -- while largely retaining conventional utility.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Instrumental and Proximal Causal Inference with Gaussian Processes
- **Authors:** Yuqi Zhang, Krikamol Muandet, Dino Sejdinovic, Edwin Fong, Siu Lun Chau
- **arXiv:** [2603.02159](https://arxiv.org/abs/2603.02159v1) · [pdf](https://arxiv.org/pdf/2603.02159v1)
- **Categories:** stat.ML, cs.LG

### Abstract
> Instrumental variable (IV) and proximal causal learning (Proxy) methods are central frameworks for causal inference in the presence of unobserved confounding. Despite substantial methodological advances, existing approaches rarely provide reliable epistemic uncertainty (EU) quantification. We address this gap through a Deconditional Gaussian Process (DGP) framework for uncertainty-aware causal learning. Our formulation recovers popular kernel estimators as the posterior mean, ensuring predictive precision, while the posterior variance yields principled and well-calibrated EU. Moreover, the probabilistic structure enables systematic model selection via marginal log-likelihood optimization. Empirical results demonstrate strong predictive performance alongside informative EU quantification, evaluated via empirical coverage frequencies and decision-aware accuracy rejection curves. Together, our approach provides a unified, practical solution for causal inference under unobserved confounding with reliable uncertainty.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
