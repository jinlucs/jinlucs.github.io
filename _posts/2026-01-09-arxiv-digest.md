---
layout: post
title: "Daily arXiv Digest — 2026-01-09 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Stochastic convergence of a class of greedy-type algorithms for Configuration Optimization Problems
- **Authors:** Evie Nielen, Oliver Tse
- **arXiv:** [2601.05029](https://arxiv.org/abs/2601.05029v1) · [pdf](https://arxiv.org/pdf/2601.05029v1)
- **Categories:** math.OC, math.FA, math.NA, math.PR

### Abstract
> Greedy Sampling Methods (GSMs) are widely used to construct approximate solutions of Configuration Optimization Problems (COPs), where a loss functional is minimized over finite configurations of points in a compact domain. While effective in practice, deterministic convergence analyses of greedy-type algorithms are often restrictive and difficult to verify. We propose a stochastic framework in which greedy-type methods are formulated as continuous-time Markov processes on the space of configurations. This viewpoint enables convergence analysis in expectation and in probability under mild structural assumptions on the error functional and the transition kernel. For global error functionals, we derive explicit convergence rates, including logarithmic, polynomial, and exponential decay, depending on an abstract improvement condition. As a pedagogical example, we study stochastic greedy sampling for one-dimensional piecewise linear interpolation and prove exponential convergence of the $L^1$-interpolation error for $C^2$-functions. Motivated by this analysis, we introduce the Randomized Polytope Division Method (R-PDM), a randomized variant of the classical Polytope Division Method, and demonstrate its effectiveness and variance reduction in numerical experiments

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
- **Authors:** Shih-Yang Liu, Xin Dong, Ximing Lu, Shizhe Diao, Peter Belcak, Mingjie Liu, Min-Hung Chen, Hongxu Yin, Yu-Chiang Frank Wang, Kwang-Ting Cheng, Yejin Choi, Jan Kautz, Pavlo Molchanov
- **arXiv:** [2601.05242](https://arxiv.org/abs/2601.05242v1) · [pdf](https://arxiv.org/pdf/2601.05242v1)
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors. However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its suitability. In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure. We then introduce Group reward-Decoupled Normalization Policy Optimization (GDPO), a new policy optimization method to resolve these issues by decoupling the normalization of individual rewards, more faithfully preserving their relative differences and enabling more accurate multi-reward optimization, along with substantially improved training stability. We compare GDPO with GRPO across three tasks: tool calling, math reasoning, and coding reasoning, evaluating both correctness metrics (accuracy, bug ratio) and constraint adherence metrics (format, length). Across all settings, GDPO consistently outperforms GRPO, demonstrating its effectiveness and generalizability for multi-reward reinforcement learning optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Stochastic Deep Learning: A Probabilistic Framework for Modeling Uncertainty in Structured Temporal Data
- **Authors:** James Rice
- **arXiv:** [2601.05227](https://arxiv.org/abs/2601.05227v1) · [pdf](https://arxiv.org/pdf/2601.05227v1)
- **Categories:** stat.ML, cs.LG, econ.EM, math.ST

### Abstract
> I propose a novel framework that integrates stochastic differential equations (SDEs) with deep generative models to improve uncertainty quantification in machine learning applications involving structured and temporal data. This approach, termed Stochastic Latent Differential Inference (SLDI), embeds an Itô SDE in the latent space of a variational autoencoder, allowing for flexible, continuous-time modeling of uncertainty while preserving a principled mathematical foundation. The drift and diffusion terms of the SDE are parameterized by neural networks, enabling data-driven inference and generalizing classical time series models to handle irregular sampling and complex dynamic structure. A central theoretical contribution is the co-parameterization of the adjoint state with a dedicated neural network, forming a coupled forward-backward system that captures not only latent evolution but also gradient dynamics. I introduce a pathwise-regularized adjoint loss and analyze variance-reduced gradient flows through the lens of stochastic calculus, offering new tools for improving training stability in deep latent SDEs. My paper unifies and extends variational inference, continuous-time generative modeling, and control-theoretic optimization, providing a rigorous foundation for future developments in stochastic probabilistic machine learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) On the Value Function of Convex Bolza Problems Governed by Stochastic Difference Equations
- **Authors:** Sebastián Álvarez, Julio Deride, Cristopher Hermosilla
- **arXiv:** [2601.05207](https://arxiv.org/abs/2601.05207v1) · [pdf](https://arxiv.org/pdf/2601.05207v1)
- **Categories:** math.OC

### Abstract
> In this paper we study the value function of Bolza problems governed by stochastic difference equations, with particular emphasis on the convex non-anticipative case. Our goal is to provide some insights on the structure of the subdiferential of the value function. In particular, we establish a connection between the evolution of the subgradients of the value function and a stochastic difference equation of Hamiltonian type. This result can be seen as a transposition of the method of characteristics, introduced by Rockafellar and Wolenski in the 2000s, to the stochastic discrete-time setting. Similarly as done in the literature for the deterministic case, the analysis is based on a duality approach. For this reason we study first a dual representation for the value function in terms of the value function of a dual problem, which is a pseudo Bolza problem. The main difference with the deterministic case is that (due to the non-anticipativity) the symmetry between the Bolza problem and its dual is no longer valid. This in turn implies that ensuring the existence of minimizers for the Bolza problem (which is a key point for establishing the method of characteristics) is not as simple as in the deterministic case, and it should be addressed differently. To complete the exposition, we study the existence of minimizers for a particular class of Bolza problems governed by linear stochastic difference equations, the so-called linear-convex optimal control problems.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Learnable Multipliers: Freeing the Scale of Language Model Matrix Layers
- **Authors:** Maksim Velikanov, Ilyas Chahed, Jingwei Zuo, Dhia Eddine Rhaiem, Younes Belkada, Hakim Hacid
- **arXiv:** [2601.04890](https://arxiv.org/abs/2601.04890v1) · [pdf](https://arxiv.org/pdf/2601.04890v1)
- **Categories:** cs.LG

### Abstract
> Applying weight decay (WD) to matrix layers is standard practice in large-language-model pretraining. Prior work suggests that stochastic gradient noise induces a Brownian-like expansion of the weight matrices W, whose growth is counteracted by WD, leading to a WD-noise equilibrium with a certain weight norm ||W||. In this work, we view the equilibrium norm as a harmful artifact of the training procedure, and address it by introducing learnable multipliers to learn the optimal scale. First, we attach a learnable scalar multiplier to W and confirm that the WD-noise equilibrium norm is suboptimal: the learned scale adapts to data and improves performance. We then argue that individual row and column norms are similarly constrained, and free their scale by introducing learnable per-row and per-column multipliers. Our method can be viewed as a learnable, more expressive generalization of muP multipliers. It outperforms a well-tuned muP baseline, reduces the computational overhead of multiplier tuning, and surfaces practical questions such as forward-pass symmetries and the width-scaling of the learned multipliers. Finally, we validate learnable multipliers with both Adam and Muon optimizers, where it shows improvement in downstream evaluations matching the improvement of the switching from Adam to Muon.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
