---
layout: post
title: "Daily arXiv Digest — 2026-01-23 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Computing Fixpoints of Learned Functions: Chaotic Iteration and Simple Stochastic Games
- **Authors:** Paolo Baldan, Sebastian Gurke, Barbara König, Florian Wittbold
- **arXiv:** [2601.16142](https://arxiv.org/abs/2601.16142v1) · [pdf](https://arxiv.org/pdf/2601.16142v1)
- **Categories:** cs.LO, cs.LG

### Abstract
> The problem of determining the (least) fixpoint of (higher-dimensional) functions over the non-negative reals frequently occurs when dealing with systems endowed with a quantitative semantics. We focus on the situation in which the functions of interest are not known precisely but can only be approximated. As a first contribution we generalize an iteration scheme called dampened Mann iteration, recently introduced in the literature. The improved scheme relaxes previous constraints on parameter sequences, allowing learning rates to converge to zero or not converge at all. While seemingly minor, this flexibility is essential to enable the implementation of chaotic iterations, where only a subset of components is updated in each step, allowing to tackle higher-dimensional problems. Additionally, by allowing learning rates to converge to zero, we can relax conditions on the convergence speed of function approximations, making the method more adaptable to various scenarios. We also show that dampened Mann iteration applies immediately to compute the expected payoff in various probabilistic models, including simple stochastic games, not covered by previous work.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Partially Lazy Gradient Descent for Smoothed Online Learning
- **Authors:** Naram Mhaisen, George Iosifidis
- **arXiv:** [2601.15984](https://arxiv.org/abs/2601.15984v1) · [pdf](https://arxiv.org/pdf/2601.15984v1)
- **Categories:** cs.LG

### Abstract
> We introduce $k$-lazyGD, an online learning algorithm that bridges the gap between greedy Online Gradient Descent (OGD, for $k=1$) and lazy GD/dual-averaging (for $k=T$), creating a spectrum between reactive and stable updates. We analyze this spectrum in Smoothed Online Convex Optimization (SOCO), where the learner incurs both hitting and movement costs. Our main contribution is establishing that laziness is possible without sacrificing hitting performance: we prove that $k$-lazyGD achieves the optimal dynamic regret $\mathcal{O}(\sqrt{(P_T+1)T})$ for any laziness slack $k$ up to $Θ(\sqrt{T/P_T})$, where $P_T$ is the comparator path length. This result formally connects the allowable laziness to the comparator's shifts, showing that $k$-lazyGD can retain the inherently small movements of lazy methods without compromising tracking ability. We base our analysis on the Follow the Regularized Leader (FTRL) framework, and derive a matching lower bound. Since the slack depends on $P_T$, an ensemble of learners with various slacks is used, yielding a method that is provably stable when it can be, and agile when it must be.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Iteration complexity of the Difference-of-Convex Algorithm for unconstrained optimization: a simple proof
- **Authors:** Serge Gratton, Philippe L. Toint
- **arXiv:** [2601.15970](https://arxiv.org/abs/2601.15970v1) · [pdf](https://arxiv.org/pdf/2601.15970v1)
- **Categories:** math.OC

### Abstract
> We propose a simple proof of the worst-case iteration complexity for the Difference of Convex functions Algorithm (DCA) for unconstrained minimization, showing that the global rate of convergence of the norm of the objective function's gradients at the iterates converge to zero like o(1/k). A small example is also provided indicating that the rate cannot be improved.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Progressive Power Homotopy for Non-convex Optimization
- **Authors:** Chen Xu
- **arXiv:** [2601.15915](https://arxiv.org/abs/2601.15915v1) · [pdf](https://arxiv.org/pdf/2601.15915v1)
- **Categories:** math.OC, cs.AI, cs.LG

### Abstract
> We propose a novel first-order method for non-convex optimization of the form $\max_{\bm{w}\in\mathbb{R}^d}\mathbb{E}_{\bm{x}\sim\mathcal{D}}[f_{\bm{w}}(\bm{x})]$, termed Progressive Power Homotopy (Prog-PowerHP). The method applies stochastic gradient ascent to a surrogate objective obtained by first performing a power transformation and then Gaussian smoothing, $F_{N,σ}(\bmμ):=\mathbb{E}_{\bm{w}\sim\mathcal{N}(\bmμ,σ^2I_d),\bm{x}\sim\mathcal{D}}[e^{Nf_w(\bm{x})}]$, while progressively increasing the power parameter $N$ and decreasing the smoothing scale $σ$ along the optimization trajectory. We prove that, under mild regularity conditions, Prog-PowerHP converges to a small neighborhood of the global optimum with an iteration complexity scaling nearly as $O(d^2\varepsilon^{-2})$. Empirically, Prog-PowerHP demonstrates clear advantages in phase retrieval when the samples-to-dimension ratio approaches the information-theoretic limit, and in training two-layer neural networks in under-parameterized regimes. These results suggest that Prog-PowerHP is particularly effective for navigating cluttered non-convex landscapes where standard first-order methods struggle.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Parallelizable Riemannian Alternating Direction Method of Multipliers for Non-convex Pose Graph Optimization
- **Authors:** Xin Chen, Chunfeng Cui, Deren Han, Liqun Qi
- **arXiv:** [2601.15684](https://arxiv.org/abs/2601.15684v1) · [pdf](https://arxiv.org/pdf/2601.15684v1)
- **Categories:** math.OC

### Abstract
> Pose graph optimization (PGO) is fundamental to robot perception and navigation systems, serving as the mathematical backbone for solving simultaneous localization and mapping (SLAM). Existing solvers suffer from polynomial growth in computational complexity with graph size, hindering real-time deployment in large-scale scenarios. In this paper, by duplicating variables and introducing equality constraints, we reformulate the problem and propose a Parallelizable Riemannian Alternating Direction Method of Multipliers (PRADMM) to solve it efficiently. Compared with the state-of-the-art methods that usually exhibit polynomial time complexity growth with graph size, PRADMM enables efficient parallel computation across vertices regardless of graph size. Crucially, all subproblems admit closed-form solutions, ensuring PRADMM maintains exceptionally stable performance. Furthermore, by carefully exploiting the structures of the coefficient matrices in the constraints, we establish the global convergence of PRADMM under mild conditions, enabling larger relaxation step sizes within the interval $(0,2)$. Extensive empirical validation on two synthetic datasets and multiple real-world 3D SLAM benchmarks confirms the superior computational performance of PRADMM.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
