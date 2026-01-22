---
layout: post
title: "Daily arXiv Digest — 2026-01-22 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Penalty-Based Smoothing of Convex Nonsmooth Supremum Functions with Accelerated Inertial Dynamics
- **Authors:** Samir Adly, Juan José Maulén, Emilio Vilches
- **arXiv:** [2601.15208](https://arxiv.org/abs/2601.15208v1) · [pdf](https://arxiv.org/pdf/2601.15208v1)
- **Categories:** math.OC

### Abstract
> We propose a penalty-based smoothing framework for convex nonsmooth functions with a supremum structure. The regularization yields a differentiable surrogate with controlled approximation error, a single-valued dual maximizer, and explicit gradient formulas. We then study an accelerated inertial dynamic with vanishing damping driven by a time-dependent regularized function whose parameter decreases to zero. Under mild integrability and boundedness conditions on the regularization schedule, we establish an accelerated $\mathcal{O}(t^{-2})$ decay estimate for the regularized residual and, in the regime $α>3$, a sharper $o(t^{-2})$ decay together with weak convergence of trajectories to a minimizer of the original nonsmooth problem via an Opial-type argument. Applications to multiobjective optimization (through Chebyshev/max scalarization) and to distributionally robust optimization (via entropic regularization over ambiguity sets) illustrate the scope of the framework.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Adaptive Exponential Integration for Stable Gaussian Mixture Black-Box Variational Inference
- **Authors:** Baojun Che, Yifan Chen, Daniel Zhengyu Huang, Xinying Mao, Weijie Wang
- **arXiv:** [2601.14855](https://arxiv.org/abs/2601.14855v1) · [pdf](https://arxiv.org/pdf/2601.14855v1)
- **Categories:** cs.LG

### Abstract
> Black-box variational inference (BBVI) with Gaussian mixture families offers a flexible approach for approximating complex posterior distributions without requiring gradients of the target density. However, standard numerical optimization methods often suffer from instability and inefficiency. We develop a stable and efficient framework that combines three key components: (1) affine-invariant preconditioning via natural gradient formulations, (2) an exponential integrator that unconditionally preserves the positive definiteness of covariance matrices, and (3) adaptive time stepping to ensure stability and to accommodate distinct warm-up and convergence phases. The proposed approach has natural connections to manifold optimization and mirror descent. For Gaussian posteriors, we prove exponential convergence in the noise-free setting and almost-sure convergence under Monte Carlo estimation, rigorously justifying the necessity of adaptive time stepping. Numerical experiments on multimodal distributions, Neal's multiscale funnel, and a PDE-based Bayesian inverse problem for Darcy flow demonstrate the effectiveness of the proposed method.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Proximal Policy Optimization with Evolutionary Mutations
- **Authors:** Casimir Czworkowski, Stephen Hornish, Alhassan S. Yasin
- **arXiv:** [2601.14705](https://arxiv.org/abs/2601.14705v1) · [pdf](https://arxiv.org/pdf/2601.14705v1)
- **Categories:** cs.NE, cs.AI, cs.GT, cs.LG

### Abstract
> Proximal Policy Optimization (PPO) is a widely used reinforcement learning algorithm known for its stability and sample efficiency, but it often suffers from premature convergence due to limited exploration. In this paper, we propose POEM (Proximal Policy Optimization with Evolutionary Mutations), a novel modification to PPO that introduces an adaptive exploration mechanism inspired by evolutionary algorithms. POEM enhances policy diversity by monitoring the Kullback-Leibler (KL) divergence between the current policy and a moving average of previous policies. When policy changes become minimal, indicating stagnation, POEM triggers an adaptive mutation of policy parameters to promote exploration. We evaluate POEM on four OpenAI Gym environments: CarRacing, MountainCar, BipedalWalker, and LunarLander. Through extensive fine-tuning using Bayesian optimization techniques and statistical testing using Welch's t-test, we find that POEM significantly outperforms PPO on three of the four tasks (BipedalWalker: t=-2.0642, p=0.0495; CarRacing: t=-6.3987, p=0.0002; MountainCar: t=-6.2431, p<0.0001), while performance on LunarLander is not statistically significant (t=-1.8707, p=0.0778). Our results highlight the potential of integrating evolutionary principles into policy gradient methods to overcome exploration-exploitation tradeoffs.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) ZENITH: Automated Gradient Norm Informed Stochastic Optimization
- **Authors:** Dhrubo Saha
- **arXiv:** [2601.15212](https://arxiv.org/abs/2601.15212v1) · [pdf](https://arxiv.org/pdf/2601.15212v1)
- **Categories:** cs.LG, cs.CV

### Abstract
> Training deep computer vision models requires manual oversight or hyperparameter tuning of the learning rate (LR) schedule. While existing adaptive optimizers schedule the LR automatically, they suffer from computational and memory overhead, incompatibility with regularization, and suboptimal LR choices. In this work, we introduce the ZENITH (Zero-overhead Evolution using Norm-Informed Training History) optimizer, which adapts the LR using the temporal evolution of the gradient norm. Image classification experiments spanning 6 CNN architectures and 6 benchmarks demonstrate that ZENITH achieves higher test accuracy in lower wall-clock time than baselines. It also yielded superior mAP in object detection, keypoint detection, and instance segmentation on MS COCO using the R-CNN family of models. Furthermore, its compatibility with regularization enables even better generalization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Finite de Finetti for convex bodies and Polynomial Optimization
- **Authors:** Julius A. Zeiss, Gereon Koßmann, René Schwonnek, Martin Plávala
- **arXiv:** [2601.15184](https://arxiv.org/abs/2601.15184v1) · [pdf](https://arxiv.org/pdf/2601.15184v1)
- **Categories:** math.OC, math-ph, quant-ph

### Abstract
> Leveraging a recently proposed notion of relative entropy in general probabilistic theories (GPT), we prove a finite de Finetti representation theorem for general convex bodies. We apply this result to address a fundamental question in polynomial optimization: the existence of a convergent outer hierarchy for problems with inequality constraints and analytical convergence guarantees. Our strategy generalizes a quantitative monogamy-of-entanglement argument from quantum theory to arbitrary convex bodies, establishing a uniform upper bound on mutual information in multipartite extensions. This leads to a finite de Finetti theorem and, subsequently, a convergent conic hierarchy for a wide class of polynomial optimization problems subject to both equality and inequality constraints. We further provide a constructive rounding scheme that yields certified interior points with controlled approximation error. As an application, we express the optimal GPT value of a two-player non-local game as a polynomial optimization problem, allowing our techniques to produce approximation schemes with finite convergence guarantees.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
