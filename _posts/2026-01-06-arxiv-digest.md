---
layout: post
title: "Daily arXiv Digest — 2026-01-06 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Asymptotic Convergence and Stability of Adaptive Gradient Methods in Smooth Non-convex Optimization
- **Authors:** Ruinan Jin, Xiaoyu Wang
- **arXiv:** [2601.01853](https://arxiv.org/abs/2601.01853v1) · [pdf](https://arxiv.org/pdf/2601.01853v1)
- **Categories:** math.OC

### Abstract
> Adaptive gradient methods, such as AdaGrad, have become fundamental tools in deep learning. Despite their widespread use, the asymptotic convergence of AdaGrad remains poorly understood in non-convex scenarios. In this work, we present the first rigorous asymptotic convergence analysis of AdaGrad-Norm for smooth non-convex optimization. Using a novel stopping-time partitioning technique, we establish a key stability result: the objective function values remain bounded in expectation, and the iterates are bounded almost surely under a mild coercivity assumption. Building on these stability results, we prove that AdaGrad-Norm achieves both almost sure and mean-square convergence. Furthermore, we extend our analysis to RMSProp and show that, with appropriate hyperparameter choices, it also enjoys stability and asymptotic convergence. The techniques developed herein may be of independent interest for analyzing other adaptive stochastic optimization algorithms.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) LION-DG: Layer-Informed Initialization with Deep Gradient Protocols for Accelerated Neural Network Training
- **Authors:** Hyunjun Kim
- **arXiv:** [2601.02105](https://arxiv.org/abs/2601.02105v1) · [pdf](https://arxiv.org/pdf/2601.02105v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Weight initialization remains decisive for neural network optimization, yet existing methods are largely layer-agnostic. We study initialization for deeply-supervised architectures with auxiliary classifiers, where untrained auxiliary heads can destabilize early training through gradient interference. We propose LION-DG, a layer-informed initialization that zero-initializes auxiliary classifier heads while applying standard He-initialization to the backbone. We prove that this implements Gradient Awakening: auxiliary gradients are exactly zero at initialization, then phase in naturally as weights grow -- providing an implicit warmup without hyperparameters. Experiments on CIFAR-10 and CIFAR-100 with DenseNet-DS and ResNet-DS architectures demonstrate: (1) DenseNet-DS: +8.3% faster convergence on CIFAR-10 with comparable accuracy, (2) Hybrid approach: Combining LSUV with LION-DG achieves best accuracy (81.92% on CIFAR-10), (3) ResNet-DS: Positive speedup on CIFAR-100 (+11.3%) with side-tap auxiliary design. We identify architecture-specific trade-offs and provide clear guidelines for practitioners. LION-DG is simple, requires zero hyperparameters, and adds no computational overhead.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Horizon Activation Mapping for Neural Networks in Time Series Forecasting
- **Authors:** Hans Krupakar, V A Kandappan
- **arXiv:** [2601.02094](https://arxiv.org/abs/2601.02094v1) · [pdf](https://arxiv.org/pdf/2601.02094v1)
- **Categories:** cs.LG, math.FA

### Abstract
> Neural networks for time series forecasting have relied on error metrics and architecture-specific interpretability approaches for model selection that don't apply across models of different families. To interpret forecasting models agnostic to the types of layers across state-of-the-art model families, we introduce Horizon Activation Mapping (HAM), a visual interpretability technique inspired by grad-CAM that uses gradient norm averages to study the horizon's subseries where grad-CAM studies attention maps over image data. We introduce causal and anti-causal modes to calculate gradient update norm averages across subseries at every timestep and lines of proportionality signifying uniform distributions of the norm averages. Optimization landscape studies with respect to changes in batch sizes, early stopping, train-val-test splits, univariate forecasting and dropouts are studied with respect to performances and subseries in HAM. Interestingly, batch size based differences in activities seem to indicate potential for existence of an exponential approximation across them per epoch relative to each other. Multivariate forecasting models including MLP-based CycleNet, N-Linear, N-HITS, self attention-based FEDformer, Pyraformer, SSM-based SpaceTime and diffusion-based Multi-Resolution DDPM over different horizon sizes trained over the ETTm2 dataset are used for HAM plots in this study. NHITS' neural approximation theorem and SpaceTime's exponential autoregressive activities have been attributed to trends in HAM plots over their training, validation and test sets. In general, HAM can be used for granular model selection, validation set choices and comparisons across different neural network model families.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) GDRO: Group-level Reward Post-training Suitable for Diffusion Models
- **Authors:** Yiyang Wang, Xi Chen, Xiaogang Xu, Yu Liu, Hengshuang Zhao
- **arXiv:** [2601.02036](https://arxiv.org/abs/2601.02036v1) · [pdf](https://arxiv.org/pdf/2601.02036v1)
- **Categories:** cs.LG, cs.CV

### Abstract
> Recent advancements adopt online reinforcement learning (RL) from LLMs to text-to-image rectified flow diffusion models for reward alignment. The use of group-level rewards successfully aligns the model with the targeted reward. However, it faces challenges including low efficiency, dependency on stochastic samplers, and reward hacking. The problem is that rectified flow models are fundamentally different from LLMs: 1) For efficiency, online image sampling takes much more time and dominates the time of training. 2) For stochasticity, rectified flow is deterministic once the initial noise is fixed. Aiming at these problems and inspired by the effects of group-level rewards from LLMs, we design Group-level Direct Reward Optimization (GDRO). GDRO is a new post-training paradigm for group-level reward alignment that combines the characteristics of rectified flow models. Through rigorous theoretical analysis, we point out that GDRO supports full offline training that saves the large time cost for image rollout sampling. Also, it is diffusion-sampler-independent, which eliminates the need for the ODE-to-SDE approximation to obtain stochasticity. We also empirically study the reward hacking trap that may mislead the evaluation, and involve this factor in the evaluation using a corrected score that not only considers the original evaluation reward but also the trend of reward hacking. Extensive experiments demonstrate that GDRO effectively and efficiently improves the reward score of the diffusion model through group-wise offline optimization across the OCR and GenEval tasks, while demonstrating strong stability and robustness in mitigating reward hacking.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Policy Optimization with Differentiable MPC: Convergence Analysis under Uncertainty
- **Authors:** Riccardo Zuliani, Efe C. Balta, John Lygeros
- **arXiv:** [2601.01940](https://arxiv.org/abs/2601.01940v1) · [pdf](https://arxiv.org/pdf/2601.01940v1)
- **Categories:** eess.SY, math.OC

### Abstract
> Model-based policy optimization is a well-established framework for designing reliable and high-performance controllers across a wide range of control applications. Recently, this approach has been extended to model predictive control policies, where explicit dynamical models are embedded within the control law. However, the performance of the resulting controllers, and the convergence of the associated optimization algorithms, critically depends on the accuracy of the models. In this paper, we demonstrate that combining gradient-based policy optimization with recursive system identification ensures convergence to an optimal controller design and showcase our finding in several control examples.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
