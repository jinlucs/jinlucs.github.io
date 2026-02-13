---
layout: post
title: "Daily arXiv Digest — 2026-02-13 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Batch-based Bayesian Optimal Experimental Design in Linear Inverse Problems
- **Authors:** Sofia Mäkinen, Andrew B. Duncan, Tapio Helin
- **arXiv:** [2602.12234](https://arxiv.org/abs/2602.12234v1) · [pdf](https://arxiv.org/pdf/2602.12234v1)
- **Categories:** stat.ME, math.OC

### Abstract
> Experimental design is central to science and engineering. A ubiquitous challenge is how to maximize the value of information obtained from expensive or constrained experimental settings. Bayesian optimal experimental design (OED) provides a principled framework for addressing such questions. In this paper, we study experimental design problems such as the optimization of sensor locations over a continuous domain in the context of linear Bayesian inverse problems. We focus in particular on batch design, that is, the simultaneous optimization of multiple design variables, which leads to a notoriously difficult non-convex optimization problem. We tackle this challenge using a promising strategy recently proposed in the frequentist setting, which relaxes A-optimal design to the space of finite positive measures. Our main contribution is the rigorous identification of the Bayesian inference problem corresponding to this relaxed A-optimal OED formulation. Moreover, building on recent work, we develop a Wasserstein gradient-flow -based optimization algorithm for the expected utility and introduce novel regularization schemes that guarantee convergence to an empirical measure. These theoretical results are supported by numerical experiments demonstrating both convergence and the effectiveness of the proposed regularization strategy.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Learning to Control: The iUzawa-Net for Nonsmooth Optimal Control of Linear PDEs
- **Authors:** Yongcun Song, Xiaoming Yuan, Hangrui Yue, Tianyou Zeng
- **arXiv:** [2602.12273](https://arxiv.org/abs/2602.12273v1) · [pdf](https://arxiv.org/pdf/2602.12273v1)
- **Categories:** math.OC, cs.LG, math.NA

### Abstract
> We propose an optimization-informed deep neural network approach, named iUzawa-Net, aiming for the first solver that enables real-time solutions for a class of nonsmooth optimal control problems of linear partial differential equations (PDEs). The iUzawa-Net unrolls an inexact Uzawa method for saddle point problems, replacing classical preconditioners and PDE solvers with specifically designed learnable neural networks. We prove universal approximation properties and establish the asymptotic $\varepsilon$-optimality for the iUzawa-Net, and validate its promising numerical efficiency through nonsmooth elliptic and parabolic optimal control problems. Our techniques offer a versatile framework for designing and analyzing various optimization-informed deep learning approaches to optimal control and other PDE-constrained optimization problems. The proposed learning-to-control approach synergizes model-based optimization algorithms and data-driven deep learning techniques, inheriting the merits of both methodologies.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Is Online Linear Optimization Sufficient for Strategic Robustness?
- **Authors:** Yang Cai, Haipeng Luo, Chen-Yu Wei, Weiqiang Zheng
- **arXiv:** [2602.12253](https://arxiv.org/abs/2602.12253v1) · [pdf](https://arxiv.org/pdf/2602.12253v1)
- **Categories:** cs.GT, cs.LG

### Abstract
> We consider bidding in repeated Bayesian first-price auctions. Bidding algorithms that achieve optimal regret have been extensively studied, but their strategic robustness to the seller's manipulation remains relatively underexplored. Bidding algorithms based on no-swap-regret algorithms achieve both desirable properties, but are suboptimal in terms of statistical and computational efficiency. In contrast, online gradient ascent is the only algorithm that achieves $O(\sqrt{TK})$ regret and strategic robustness [KSS24], where $T$ denotes the number of auctions and $K$ the number of bids. In this paper, we explore whether simple online linear optimization (OLO) algorithms suffice for bidding algorithms with both desirable properties. Our main result shows that sublinear linearized regret is sufficient for strategic robustness. Specifically, we construct simple black-box reductions that convert any OLO algorithm into a strategically robust no-regret bidding algorithm, in both known and unknown value distribution settings. For the known value distribution case, our reduction yields a bidding algorithm that achieves $O(\sqrt{T \log K})$ regret and strategic robustness (with exponential improvement on the $K$-dependence compared to [KSS24]). For the unknown value distribution case, our reduction gives a bidding algorithm with high-probability $O(\sqrt{T (\log K+\log(T/δ)})$ regret and strategic robustness, while removing the bounded density assumption made in [KSS24].

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Learning to Forget Attention: Memory Consolidation for Adaptive Compute Reduction
- **Authors:** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma
- **arXiv:** [2602.12204](https://arxiv.org/abs/2602.12204v1) · [pdf](https://arxiv.org/pdf/2602.12204v1)
- **Categories:** cs.LG

### Abstract
> Hybrid architectures combining state-space models with attention have achieved strong efficiency-quality tradeoffs, yet existing approaches either apply attention uniformly or learn static sparse patterns. This misses a key opportunity: \emph{attention demand should decrease over time as recurring patterns become familiar}. We present a surprising finding from analyzing GPT-2 models: \textbf{88\%} of attention operations retrieve information already predictable from the model's hidden state, and this redundancy does \emph{not} decrease during training. Motivated by this observation, we introduce \textbf{\ours{}} (\textbf{C}onsolidation-based \textbf{R}outing for \textbf{A}daptive \textbf{M}emory), a biologically inspired memory consolidation mechanism that gradually distills episodic retrievals into parametric semantic memory. Unlike prior sparse attention methods, \ours{} exhibits \emph{decreasing attention utilization} over training, achieving a \textbf{37.8$\times$} reduction through a sharp phase transition at approximately 3K steps. We prove that this capability is \emph{impossible} without consolidation: any static routing scheme requires $Ω(f \cdot n)$ attention for tasks with recurring patterns of frequency $f$. On our proposed SRCD benchmark, \ours{} achieves \textbf{100\% retrieval accuracy} at 1.6\% attention compute (vs.\ 68\% for baselines), and consolidated patterns transfer to unseen tasks with \textbf{48--52\%} attention reduction without retraining. Remarkably, the learned consolidation dynamics quantitatively match human episodic-to-semantic memory transition curves from cognitive psychology ($γ= 0.43$ vs.\ $γ_{\text{human}} \approx 0.4$--$0.5$). Code and benchmarks are available at [anonymized].

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Convex Markov Games and Beyond: New Proof of Existence, Characterization and Learning Algorithms for Nash Equilibria
- **Authors:** Anas Barakat, Ioannis Panageas, Antonios Varvitsiotis
- **arXiv:** [2602.12181](https://arxiv.org/abs/2602.12181v1) · [pdf](https://arxiv.org/pdf/2602.12181v1)
- **Categories:** cs.GT, cs.LG, cs.MA

### Abstract
> Convex Markov Games (cMGs) were recently introduced as a broad class of multi-agent learning problems that generalize Markov games to settings where strategic agents optimize general utilities beyond additive rewards. While cMGs expand the modeling frontier, their theoretical foundations, particularly the structure of Nash equilibria (NE) and guarantees for learning algorithms, are not yet well understood. In this work, we address these gaps for an extension of cMGs, which we term General Utility Markov Games (GUMGs), capturing new applications requiring coupling between agents' occupancy measures. We prove that in GUMGs, Nash equilibria coincide with the fixed points of projected pseudo-gradient dynamics (i.e., first-order stationary points), enabled by a novel agent-wise gradient domination property. This insight also yields a simple proof of NE existence using Brouwer's fixed-point theorem. We further show the existence of Markov perfect equilibria. Building on this characterization, we establish a policy gradient theorem for GUMGs and design a model-free policy gradient algorithm. For potential GUMGs, we establish iteration complexity guarantees for computing approximate-NE under exact gradients and provide sample complexity bounds in both the generative model and on-policy settings. Our results extend beyond prior work restricted to zero-sum cMGs, providing the first theoretical analysis of common-interest cMGs.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
