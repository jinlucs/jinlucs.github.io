---
layout: post
title: "Daily arXiv Digest — 2026-02-03 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Variational Entropic Optimal Transport
- **Authors:** Roman Dyachenko, Nikita Gushchin, Kirill Sokolov, Petr Mokrov, Evgeny Burnaev, Alexander Korotin
- **arXiv:** [2602.02241](https://arxiv.org/abs/2602.02241v1) · [pdf](https://arxiv.org/pdf/2602.02241v1)
- **Categories:** cs.LG

### Abstract
> Entropic optimal transport (EOT) in continuous spaces with quadratic cost is a classical tool for solving the domain translation problem. In practice, recent approaches optimize a weak dual EOT objective depending on a single potential, but doing so is computationally not efficient due to the intractable log-partition term. Existing methods typically resolve this obstacle in one of two ways: by significantly restricting the transport family to obtain closed-form normalization (via Gaussian-mixture parameterizations), or by using general neural parameterizations that require simulation-based training procedures. We propose Variational Entropic Optimal Transport (VarEOT), based on an exact variational reformulation of the log-partition $\log \mathbb{E}[\exp(\cdot)]$ as a tractable minimization over an auxiliary positive normalizer. This yields a differentiable learning objective optimized with stochastic gradients and avoids the necessity of MCMC simulations during the training. We provide theoretical guarantees, including finite-sample generalization bounds and approximation results under universal function approximation. Experiments on synthetic data and unpaired image-to-image translation demonstrate competitive or improved translation quality, while comparisons within the solvers that use the same weak dual EOT objective support the benefit of the proposed optimization principle.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Finite-Sample Wasserstein Error Bounds and Concentration Inequalities for Nonlinear Stochastic Approximation
- **Authors:** Seo Taek Kong, R. Srikant
- **arXiv:** [2602.02445](https://arxiv.org/abs/2602.02445v1) · [pdf](https://arxiv.org/pdf/2602.02445v1)
- **Categories:** cs.LG, math.ST

### Abstract
> This paper derives non-asymptotic error bounds for nonlinear stochastic approximation algorithms in the Wasserstein-$p$ distance. To obtain explicit finite-sample guarantees for the last iterate, we develop a coupling argument that compares the discrete-time process to a limiting Ornstein-Uhlenbeck process. Our analysis applies to algorithms driven by general noise conditions, including martingale differences and functions of ergodic Markov chains. Complementing this result, we handle the convergence rate of the Polyak-Ruppert average through a direct analysis that applies under the same general setting. Assuming the driving noise satisfies a non-asymptotic central limit theorem, we show that the normalized last iterates converge to a Gaussian distribution in the $p$-Wasserstein distance at a rate of order $γ_n^{1/6}$, where $γ_n$ is the step size. Similarly, the Polyak-Ruppert average is shown to converge in the Wasserstein distance at a rate of order $n^{-1/6}$. These distributional guarantees imply high-probability concentration inequalities that improve upon those derived from moment bounds and Markov's inequality. We demonstrate the utility of this approach by considering two applications: (1) linear stochastic approximation, where we explicitly quantify the transition from heavy-tailed to Gaussian behavior of the iterates, thereby bridging the gap between recent finite-sample analyses and asymptotic theory and (2) stochastic gradient descent, where we establish rate of convergence to the central limit theorem.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Backpropagation as Physical Relaxation: Exact Gradients in Finite Time
- **Authors:** Antonino Emanuele Scurria
- **arXiv:** [2602.02281](https://arxiv.org/abs/2602.02281v1) · [pdf](https://arxiv.org/pdf/2602.02281v1)
- **Categories:** cs.LG, cs.AI, cs.NE, physics.class-ph, physics.comp-ph

### Abstract
> Backpropagation, the foundational algorithm for training neural networks, is typically understood as a symbolic computation that recursively applies the chain rule. We show it emerges exactly as the finite-time relaxation of a physical dynamical system. By formulating feedforward inference as a continuous-time process and applying Lagrangian theory of non-conservative systems to handle asymmetric interactions, we derive a global energy functional on a doubled state space encoding both activations and sensitivities. The saddle-point dynamics of this energy perform inference and credit assignment simultaneously through local interactions. We term this framework ''Dyadic Backpropagation''. Crucially, we prove that unit-step Euler discretization, the natural timescale of layer transitions, recovers standard backpropagation exactly in precisely 2L steps for an L-layer network, with no approximations. Unlike prior energy-based methods requiring symmetric weights, asymptotic convergence, or vanishing perturbations, our framework guarantees exact gradients in finite time. This establishes backpropagation as the digitally optimized shadow of a continuous physical relaxation, providing a rigorous foundation for exact gradient computation in analog and neuromorphic substrates where continuous dynamics are native.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Unsupervised Physics-Informed Operator Learning through Multi-Stage Curriculum Training
- **Authors:** Paolo Marcandelli, Natansh Mathur, Stefano Markidis, Martina Siena, Stefano Mariani
- **arXiv:** [2602.02264](https://arxiv.org/abs/2602.02264v1) · [pdf](https://arxiv.org/pdf/2602.02264v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Solving partial differential equations remains a central challenge in scientific machine learning. Neural operators offer a promising route by learning mappings between function spaces and enabling resolution-independent inference, yet they typically require supervised data. Physics-informed neural networks address this limitation through unsupervised training with physical constraints but often suffer from unstable convergence and limited generalization capability. To overcome these issues, we introduce a multi-stage physics-informed training strategy that achieves convergence by progressively enforcing boundary conditions in the loss landscape and subsequently incorporating interior residuals. At each stage the optimizer is re-initialized, acting as a continuation mechanism that restores stability and prevents gradient stagnation. We further propose the Physics-Informed Spline Fourier Neural Operator (PhIS-FNO), combining Fourier layers with Hermite spline kernels for smooth residual evaluation. Across canonical benchmarks, PhIS-FNO attains a level of accuracy comparable to that of supervised learning, using labeled information only along a narrow boundary region, establishing staged, spline-based optimization as a robust paradigm for physics-informed operator learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Maximizing Reliability with Bayesian Optimization
- **Authors:** Jack M. Buckingham, Ivo Couckuyt, Juergen Branke
- **arXiv:** [2602.02432](https://arxiv.org/abs/2602.02432v1) · [pdf](https://arxiv.org/pdf/2602.02432v1)
- **Categories:** cs.LG, math.OC, stat.ML

### Abstract
> Bayesian optimization (BO) is a popular, sample-efficient technique for expensive, black-box optimization. One such problem arising in manufacturing is that of maximizing the reliability, or equivalently minimizing the probability of a failure, of a design which is subject to random perturbations - a problem that can involve extremely rare failures ($P_\mathrm{fail} = 10^{-6}-10^{-8}$). In this work, we propose two BO methods based on Thompson sampling and knowledge gradient, the latter approximating the one-step Bayes-optimal policy for minimizing the logarithm of the failure probability. Both methods incorporate importance sampling to target extremely small failure probabilities. Empirical results show the proposed methods outperform existing methods in both extreme and non-extreme regimes.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
