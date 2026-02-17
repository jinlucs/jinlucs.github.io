---
layout: post
title: "Daily arXiv Digest — 2026-02-17 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) On Convergence Analysis of Network-GIANT: An approximate Hessian-based fully distributed optimization algorithm
- **Authors:** Souvik Das, Luca Schenato, Subhrakanti Dey
- **arXiv:** [2602.14830](https://arxiv.org/abs/2602.14830v1) · [pdf](https://arxiv.org/pdf/2602.14830v1)
- **Categories:** math.OC, eess.SP, eess.SY

### Abstract
> In this paper, we present a detailed convergence analysis of a recently developed approximate Newton-type fully distributed optimization method for smooth, strongly convex local loss functions, called Network-GIANT, which has been empirically illustrated to show faster linear convergence properties while having the same communication complexity (per iteration) as its first order distributed counterparts. By using consensus based parameter updates, and a local Hessian based descent direction at the individual nodes with gradient tracking, we first explicitly characterize a global linear convergence rate for Network-GIANT, which can be computed as the spectral radius of a $3 \times 3$ matrix dependent on the Lipschitz continuity ($L$) and strong convexity ($μ$) parameters of the objective functions, and the spectral norm ($σ$) of the underlying undirected graph represented by a doubly stochastic consensus matrix. We provide an explicit bound on the step size parameter $η$, below which this spectral radius is guaranteed to be less than $1$. Furthermore, we derive a mixed linear-quadratic inequality based upper bound for the optimality gap norm, which allows us to conclude that, under small step size values, asymptotically, as the algorithm approaches the global optimum, it achieves a locally linear convergence rate of $1-η(1 -\fracγμ)$ for Network-GIANT, provided the Hessian approximation error $γ$ (between the harmonic mean of the local Hessians and the global hessian (the arithmetic mean of the local Hessians) is smaller than $μ$. This asymptotically linear convergence rate of $\approx 1-η$ explains the faster convergence rate of Network-GIANT for the first time. Numerical experiments are carried out with a reduced CovType dataset for binary logistic regression over a variety of graphs to illustrate the above theoretical results.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) ALiA: Adaptive Linearized ADMM
- **Authors:** Uijeong Jang, Kaizhao Sun, Wotao Yin, Ernest K Ryu
- **arXiv:** [2602.15000](https://arxiv.org/abs/2602.15000v1) · [pdf](https://arxiv.org/pdf/2602.15000v1)
- **Categories:** math.OC

### Abstract
> We propose ALiA, a novel adaptive variant of the alternating direction method of multipliers (ADMM). Specifically, ALiA is a variant of function-linearized proximal ADMM (FLiP ADMM), which generalizes the classical ADMM by leveraging the differentiable structure of the objective function, making it highly versatile. Notably, ALiA features an adaptive stepsize selection scheme that eliminates the need for backtracking linesearch. Motivated by recent advances in adaptive gradient and proximal methods, we establish point convergence of ALiA for convex and differentiable objectives. Furthermore, by introducing negligible computational overhead, we develop an alternative stepsize selection scheme for ALiA that improves the convergence speed both theoretically and empirically. Extensive numerical experiments on practical datasets confirm the accelerated performance of ALiA compared to standard FLiP ADMM. Additionally, we demonstrate that ALiA either outperforms or matches the practical performance of existing adaptive methods across problem classes where it is applicable.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Variance-Reduced $(\varepsilon,δ)-$Unlearning using Forget Set Gradients
- **Authors:** Martin Van Waerebeke, Marco Lorenzi, Kevin Scaman, El Mahdi El Mhamdi, Giovanni Neglia
- **arXiv:** [2602.14938](https://arxiv.org/abs/2602.14938v1) · [pdf](https://arxiv.org/pdf/2602.14938v1)
- **Categories:** cs.LG, math.OC

### Abstract
> In machine unlearning, $(\varepsilon,δ)-$unlearning is a popular framework that provides formal guarantees on the effectiveness of the removal of a subset of training data, the forget set, from a trained model. For strongly convex objectives, existing first-order methods achieve $(\varepsilon,δ)-$unlearning, but they only use the forget set to calibrate injected noise, never as a direct optimization signal. In contrast, efficient empirical heuristics often exploit the forget samples (e.g., via gradient ascent) but come with no formal unlearning guarantees. We bridge this gap by presenting the Variance-Reduced Unlearning (VRU) algorithm. To the best of our knowledge, VRU is the first first-order algorithm that directly includes forget set gradients in its update rule, while provably satisfying ($(\varepsilon,δ)-$unlearning. We establish the convergence of VRU and show that incorporating the forget set yields strictly improved rates, i.e. a better dependence on the achieved error compared to existing first-order $(\varepsilon,δ)-$unlearning methods. Moreover, we prove that, in a low-error regime, VRU asymptotically outperforms any first-order method that ignores the forget set.Experiments corroborate our theory, showing consistent gains over both state-of-the-art certified unlearning methods and over empirical baselines that explicitly leverage the forget set.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) On the Stability of Nonlinear Dynamics in GD and SGD: Beyond Quadratic Potentials
- **Authors:** Rotem Mulayoff, Sebastian U. Stich
- **arXiv:** [2602.14789](https://arxiv.org/abs/2602.14789v1) · [pdf](https://arxiv.org/pdf/2602.14789v1)
- **Categories:** cs.LG, stat.ML

### Abstract
> The dynamical stability of the iterates during training plays a key role in determining the minima obtained by optimization algorithms. For example, stable solutions of gradient descent (GD) correspond to flat minima, which have been associated with favorable features. While prior work often relies on linearization to determine stability, it remains unclear whether linearized dynamics faithfully capture the full nonlinear behavior. Recent work has shown that GD may stably oscillate near a linearly unstable minimum and still converge once the step size decays, indicating that linear analysis can be misleading. In this work, we explicitly study the effect of nonlinear terms. Specifically, we derive an exact criterion for stable oscillations of GD near minima in the multivariate setting. Our condition depends on high-order derivatives, generalizing existing results. Extending the analysis to stochastic gradient descent (SGD), we show that nonlinear dynamics can diverge in expectation even if a single batch is unstable. This implies that stability can be dictated by a single batch that oscillates unstably, rather than an average effect, as linear analysis suggests. Finally, we prove that if all batches are linearly stable, the nonlinear dynamics of SGD are stable in expectation.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Distributed Quantum Gaussian Processes for Multi-Agent Systems
- **Authors:** Meet Gandhi, George P. Kontoudis
- **arXiv:** [2602.15006](https://arxiv.org/abs/2602.15006v1) · [pdf](https://arxiv.org/pdf/2602.15006v1)
- **Categories:** cs.MA, cs.LG, math.DG

### Abstract
> Gaussian Processes (GPs) are a powerful tool for probabilistic modeling, but their performance is often constrained in complex, largescale real-world domains due to the limited expressivity of classical kernels. Quantum computing offers the potential to overcome this limitation by embedding data into exponentially large Hilbert spaces, capturing complex correlations that remain inaccessible to classical computing approaches. In this paper, we propose a Distributed Quantum Gaussian Process (DQGP) method in a multiagent setting to enhance modeling capabilities and scalability. To address the challenging non-Euclidean optimization problem, we develop a Distributed consensus Riemannian Alternating Direction Method of Multipliers (DR-ADMM) algorithm that aggregates local agent models into a global model. We evaluate the efficacy of our method through numerical experiments conducted on a quantum simulator in classical hardware. We use real-world, non-stationary elevation datasets of NASA's Shuttle Radar Topography Mission and synthetic datasets generated by Quantum Gaussian Processes. Beyond modeling advantages, our framework highlights potential computational speedups that quantum hardware may provide, particularly in Gaussian processes and distributed optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
