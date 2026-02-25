---
layout: post
title: "Daily arXiv Digest — 2026-02-25 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Efficient Online Learning in Interacting Particle Systems
- **Authors:** Louis Sharrock, Nikolas Kantas, Grigorios A. Pavliotis
- **arXiv:** [2602.20875](https://arxiv.org/abs/2602.20875v1) · [pdf](https://arxiv.org/pdf/2602.20875v1)
- **Categories:** math.ST, math.OC, math.PR, stat.ME, stat.ML

### Abstract
> We introduce a new method for online parameter estimation in stochastic interacting particle systems, based on continuous observation of a small number of particles from the system. Our method recursively updates the model parameters using a stochastic approximation of the gradient of the asymptotic log likelihood, which is computed using the continuous stream of observations. Under suitable assumptions, we rigorously establish convergence of our method to the stationary points of the asymptotic log-likelihood of the interacting particle system. We consider asymptotics both in the limit as the time horizon $t\rightarrow\infty$, for a fixed and finite number of particles, and in the joint limit as the number of particles $N\rightarrow\infty$ and the time horizon $t\rightarrow\infty$. Under additional assumptions on the asymptotic log-likelihood, we also establish an $\mathrm{L}^2$ convergence rate and a central limit theorem. Finally, we present several numerical examples of practical interest, including a model for systemic risk, a model of interacting FitzHugh--Nagumo neurons, and a Cucker--Smale flocking model. Our numerical results corroborate our theoretical results, and also suggest that our estimator is effective even in cases where the assumptions required for our theoretical analysis do not hold.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) On the Convergence of Stochastic Gradient Descent with Perturbed Forward-Backward Passes
- **Authors:** Boao Kong, Hengrui Zhang, Kun Yuan
- **arXiv:** [2602.20646](https://arxiv.org/abs/2602.20646v1) · [pdf](https://arxiv.org/pdf/2602.20646v1)
- **Categories:** math.OC, cs.LG, stat.ML

### Abstract
> We study stochastic gradient descent (SGD) for composite optimization problems with $N$ sequential operators subject to perturbations in both the forward and backward passes. Unlike classical analyses that treat gradient noise as additive and localized, perturbations to intermediate outputs and gradients cascade through the computational graph, compounding geometrically with the number of operators. We present the first comprehensive theoretical analysis of this setting. Specifically, we characterize how forward and backward perturbations propagate and amplify within a single gradient step, derive convergence guarantees for both general non-convex objectives and functions satisfying the Polyak--Łojasiewicz condition, and identify conditions under which perturbations do not deteriorate the asymptotic convergence order. As a byproduct, our analysis furnishes a theoretical explanation for the gradient spiking phenomenon widely observed in deep learning, precisely characterizing the conditions under which training recovers from spikes or diverges. Experiments on logistic regression with convex and non-convex regularization validate our theories, illustrating the predicted spike behavior and the asymmetric sensitivity to forward versus backward perturbations.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) A subdifferential characterization via Busemann functions and applications to DC optimization on Hadamard manifolds
- **Authors:** O. P. Ferreira, D. S. Gonçalves, M. S. Louzeiro, S. Z. Németh, J. Zhu
- **arXiv:** [2602.20931](https://arxiv.org/abs/2602.20931v1) · [pdf](https://arxiv.org/pdf/2602.20931v1)
- **Categories:** math.OC

### Abstract
> This paper investigates the properties of Busemann functions on Hadamard manifolds and their use in optimization algorithms in Riemannian settings. We present a new Busemann-based characterization of the subdifferential, which is particularly well suited to Riemannian optimization. In the classical Hadamard manifold framework, a subgradient provides a global lower model of a convex function expressed through the inverse exponential map. However, this model may fail to exhibit a useful convexity or concavity structure. By contrast, our characterization yields a concave bounding function by exploiting key properties of Busemann functions. We use this concavity to design and analyze difference-of-convex (DC) optimization methods on Hadamard manifolds. In particular, we reformulate the classical DC algorithm (DCA) for Riemannian contexts and study its convergence properties. We also report preliminary numerical experiments comparing the proposed Busemann DCA, which leads to geodesically convex subproblems, with the classical Riemannian DCA.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Maximum entropy based testing in network models: ERGMs and constrained optimization
- **Authors:** Subhrosekhar Ghosh, Rathindra Nath Karmakar, Samriddha Lahiry
- **arXiv:** [2602.20844](https://arxiv.org/abs/2602.20844v1) · [pdf](https://arxiv.org/pdf/2602.20844v1)
- **Categories:** math.ST, cs.IT, math.PR, stat.ME, stat.ML

### Abstract
> Stochastic network models play a central role across a wide range of scientific disciplines, and questions of statistical inference arise naturally in this context. In this paper we investigate goodness-of-fit and two-sample testing procedures for statistical networks based on the principle of maximum entropy (MaxEnt). Our approach formulates a constrained entropy-maximization problem on the space of networks, subject to prescribed structural constraints. The resulting test statistics are defined through the Lagrange multipliers associated with the constrained optimization problem, which, to our knowledge, is novel in the statistical networks literature. We establish consistency in the classical regime where the number of vertices is fixed. We then consider asymptotic regimes in which the graph size grows with the sample size, developing tests for both dense and sparse settings. In the dense case, we analyze exponential random graph models (ERGM) (including the Erdös-Rènyi models), while in the sparse regime our theory applies to Erd{ö}s-R{è}nyi graphs. Our analysis leverages recent advances in nonlinear large deviation theory for random graphs. We further show that the proposed Lagrange-multiplier framework connects naturally to classical score tests for constrained maximum likelihood estimation. The results provide a unified entropy-based framework for network model assessment across diverse growth regimes.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Convergent Lifted Lasserre Hierarchy of SDPs for Minimizing Expectation of Piecewise Polynomial Loss over Wasserstein Balls
- **Authors:** N. D. Dizon, Q. Y. Huang, T. D. Chuong, G. Li, V. Jeyakumar
- **arXiv:** [2602.20660](https://arxiv.org/abs/2602.20660v1) · [pdf](https://arxiv.org/pdf/2602.20660v1)
- **Categories:** math.OC

### Abstract
> This paper investigates the minimization of the expectation of piecewise polynomial loss functions over Wasserstein balls. This optimization problem often appears as a key sub-problem of distributionally robust optimization problems. We establish the asymptotic convergence of a hierarchy of semi-definite programming (SDP) relaxations, providing a framework for approximating the optimal values of these inherently infinite-dimensional optimization problems. A central foundational contribution is the development of a new lifted positivity certificate: we demonstrate that piecewise polynomials positive over Archimedean basic semi-algebraic sets admit a structured system of sum-of-squares (SOS) representations. Furthermore, we prove that the proposed hierarchy achieves finite convergence under suitable conditions when the defining polynomials are convex. The practical utility and versatility of this approach are demonstrated via numerical experiments in revenue estimation and portfolio optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
