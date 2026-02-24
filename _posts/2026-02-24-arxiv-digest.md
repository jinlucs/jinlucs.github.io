---
layout: post
title: "Daily arXiv Digest — 2026-02-24 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Generalized Random Direction Newton Algorithms for Stochastic Optimization
- **Authors:** Soumen Pachal, Prashanth L. A., Shalabh Bhatnagar, Avinash Achar
- **arXiv:** [2602.19893](https://arxiv.org/abs/2602.19893v1) · [pdf](https://arxiv.org/pdf/2602.19893v1)
- **Categories:** cs.LG, stat.ML

### Abstract
> We present a family of generalized Hessian estimators of the objective using random direction stochastic approximation (RDSA) by utilizing only noisy function measurements. The form of each estimator and the order of the bias depend on the number of function measurements. In particular, we demonstrate that estimators with more function measurements exhibit lower-order estimation bias. We show the asymptotic unbiasedness of the estimators. We also perform asymptotic and non-asymptotic convergence analyses for stochastic Newton methods that incorporate our generalized Hessian estimators. Finally, we perform numerical experiments to validate our theoretical findings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Local Second-Order Limit Dynamics of the Alternating Direction Method of Multipliers for Semidefinite Programming
- **Authors:** Shucheng Kang, Heng Yang
- **arXiv:** [2602.20103](https://arxiv.org/abs/2602.20103v1) · [pdf](https://arxiv.org/pdf/2602.20103v1)
- **Categories:** math.OC

### Abstract
> The alternating direction method of multipliers (ADMM) is widely used for solving large-scale semidefinite programs (SDPs), yet on instances with multiple primal--dual optimal solution pairs, it often enters prolonged slow-convergence regions where the Karush--Kuhn--Tucker (KKT) residuals nearly stall. To explain and predict the fine-grained dynamical behavior inside these regions, we develop a local second-order limit dynamics framework for ADMM near an arbitrary KKT point -- not necessarily the eventual limit point of the iterates. Assuming the existence of a strictly complementary primal--dual solution pair, we derive a second-order local expansion of the ADMM dynamics by leveraging a refined and simplified variational characterization of the (parabolic) second-order directional derivative of the PSD projection operator. This expansion reveals a closed convex cone of directions along which the local first-order update vanishes, and it induces a second-order limit map that governs the persistent drift after transient effects are filtered out. We characterize fundamental properties of this mapping, including its kernel, range, and continuity. A primal--dual decoupling further yields a clean scaling law for the effect of the penalty parameter in ADMM. We connect these properties to second-order dynamical features of ADMM, including fixed points, almost-invariant sets, and microscopic phases. Three empirical phenomena in slow-convergence regions are then explained or predicted: (i) angles between consecutive iterate differences are small yet nonzero, except for sparse spikes; (ii) primal and dual infeasibilities are insensitive to penalty-parameter updates; and (iii) iterates can be transiently trapped in a low-dimensional subspace for an extended period. Extensive numerical experiments on the Mittelmann dataset corroborate our theoretical predictions.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning
- **Authors:** Zhongwei Wan, Yun Shen, Zhihao Dou, Donghao Zhou, Yu Zhang, Xin Wang, Hui Shen, Jing Xiong, Chaofan Tao, Zixuan Zhong, Peizhou Huang, Mi Zhang
- **arXiv:** [2602.19895](https://arxiv.org/abs/2602.19895v1) · [pdf](https://arxiv.org/pdf/2602.19895v1)
- **Categories:** cs.LG, cs.CL

### Abstract
> Reinforcement learning with verifiers (RLVR) is a central paradigm for improving large language model (LLM) reasoning, yet existing methods often suffer from limited exploration. Policies tend to collapse onto a few reasoning patterns and prematurely stop deep exploration, while conventional entropy regularization introduces only local stochasticity and fails to induce meaningful path-level diversity, leading to weak and unstable learning signals in group-based policy optimization. We propose DSDR, a Dual-Scale Diversity Regularization reinforcement learning framework that decomposes diversity in LLM reasoning into global and coupling components. Globally, DSDR promotes diversity among correct reasoning trajectories to explore distinct solution modes. Locally, it applies a length-invariant, token-level entropy regularization restricted to correct trajectories, preventing entropy collapse within each mode while preserving correctness. The two scales are coupled through a global-to-local allocation mechanism that emphasizes local regularization for more distinctive correct trajectories. We provide theoretical support showing that DSDR preserves optimal correctness under bounded regularization, sustains informative learning signals in group-based optimization, and yields a principled global-to-local coupling rule. Experiments on multiple reasoning benchmarks demonstrate consistent improvements in accuracy and pass@k, highlighting the importance of dual-scale diversity for deep exploration in RLVR. Code is available at https://github.com/SUSTechBruce/DSDR.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Exact Discrete Stochastic Simulation with Deep-Learning-Scale Gradient Optimization
- **Authors:** Jose M. G. Vilar, Leonor Saiz
- **arXiv:** [2602.19775](https://arxiv.org/abs/2602.19775v1) · [pdf](https://arxiv.org/pdf/2602.19775v1)
- **Categories:** q-bio.QM, cond-mat.stat-mech, cs.LG, physics.comp-ph, q-bio.MN

### Abstract
> Exact stochastic simulation of continuous-time Markov chains (CTMCs) is essential when discreteness and noise drive system behavior, but the hard categorical event selection in Gillespie-type algorithms blocks gradient-based learning. We eliminate this constraint by decoupling forward simulation from backward differentiation, with hard categorical sampling generating exact trajectories and gradients propagating through a continuous massively-parallel Gumbel-Softmax straight-through surrogate. Our approach enables accurate optimization at parameter scales over four orders of magnitude beyond existing simulators. We validate for accuracy, scalability, and reliability on a reversible dimerization model (0.09% error), a genetic oscillator (1.2% error), a 203,796-parameter gene regulatory network achieving 98.4% MNIST accuracy (a prototypical deep-learning multilayer perceptron benchmark), and experimental patch-clamp recordings of ion channel gating (R^2 = 0.987) in the single-channel regime. Our GPU implementation delivers 1.9 billion steps per second, matching the scale of non-differentiable simulators. By making exact stochastic simulation massively parallel and autodiff-compatible, our results enable high-dimensional parameter inference and inverse design across systems biology, chemical kinetics, physics, and related CTMC-governed domains.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Behavior Learning (BL): Learning Hierarchical Optimization Structures from Data
- **Authors:** Zhenyao Ma, Yue Liang, Dongxu Li
- **arXiv:** [2602.20152](https://arxiv.org/abs/2602.20152v1) · [pdf](https://arxiv.org/pdf/2602.20152v1)
- **Categories:** cs.LG, cs.AI, stat.ML

### Abstract
> Inspired by behavioral science, we propose Behavior Learning (BL), a novel general-purpose machine learning framework that learns interpretable and identifiable optimization structures from data, ranging from single optimization problems to hierarchical compositions. It unifies predictive performance, intrinsic interpretability, and identifiability, with broad applicability to scientific domains involving optimization. BL parameterizes a compositional utility function built from intrinsically interpretable modular blocks, which induces a data distribution for prediction and generation. Each block represents and can be written in symbolic form as a utility maximization problem (UMP), a foundational paradigm in behavioral science and a universal framework of optimization. BL supports architectures ranging from a single UMP to hierarchical compositions, the latter modeling hierarchical optimization structures. Its smooth and monotone variant (IBL) guarantees identifiability. Theoretically, we establish the universal approximation property of BL, and analyze the M-estimation properties of IBL. Empirically, BL demonstrates strong predictive performance, intrinsic interpretability and scalability to high-dimensional data. Code: https://github.com/MoonYLiang/Behavior-Learning ; install via pip install blnetwork.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
