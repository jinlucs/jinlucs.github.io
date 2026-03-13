---
layout: post
title: "Daily arXiv Digest — 2026-03-13 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Dictionary-Restricted First-Order Descent Methods: Bounds and Convergence Rates
- **Authors:** Miguel Berasategui, Pablo M. Berná, Antonio Falcó
- **arXiv:** [2603.12209](https://arxiv.org/abs/2603.12209v1) · [pdf](https://arxiv.org/pdf/2603.12209v1)
- **Categories:** math.OC

### Abstract
> This paper develops a general theory for first-order descent methods whose search directions are restricted to a prescribed dictionary in a reflexive Banach space. Instead of assuming that the linear span of the dictionary is dense, as in the classical Proper Generalized Decomposition framework of Falcó and Nouy or in the universality approach of Berná and Falcó, we introduce a geometric condition based on norming sets that guarantees density through a duality argument. This makes it possible to treat dictionaries arising from tensor formats, neural network units, and other nonlinear or parameterized approximation families within a unified setting. On the algorithmic side, we analyze a simple greedy update rule in which each iterate is obtained by minimizing the energy functional along one direction from the dictionary. Under mild differentiability, Lipschitz continuity, and ellipticity assumptions on the objective, we derive explicit quantitative descent bounds and sharp convergence rates. These include algebraic rates that improve those of classical steepest-descent schemes in Banach spaces, as well as arbitrarily high polynomial rates and exponential convergence in a critical regime. The results apply broadly to convex variational problems, high-dimensional approximation, and structured optimization methods that rely on restricted or compressed search directions.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Operator Splitting, Policy Iteration, and Machine Learning for Stochastic Optimal Control
- **Authors:** Alain Bensoussan, Thien P. B. Nguyen, Minh-Binh Tran, Son N. T. Tu
- **arXiv:** [2603.12167](https://arxiv.org/abs/2603.12167v1) · [pdf](https://arxiv.org/pdf/2603.12167v1)
- **Categories:** math.OC, math.AP, math.NA

### Abstract
> We propose a splitting approach to solve the second-order Hamilton--Jacobi equation, reducing it to a heat step and a purely first-order step. The latter is implemented using a gradient value policy iteration algorithm, enabling efficient characteristic-based machine learning methods. We establish convergence rates for the splitting method. In particular, the $L^\infty$ error is bounded below by $\mathcal{O}(h)$ and above by $\mathcal{O}(h^{1/7})$ for Lipschitz initial data; this improves to $\mathcal{O}(h^{1/5})$ for semiconcave data and to $\mathcal{O}(h^{1/3})$ for $C^2$ data. We also prove an upper $L^1$ error estimate of order $\mathcal{O}(h^{1/2})$ in the periodic setting, where $h$ is the splitting step. For the first-order step, we provide a weighted $L^2$ error analysis that shows exponential convergence. Each iteration solves linear characteristic equations and learns the value function by minimizing a weighted value gradient loss. The approach yields stable and accurate numerical results.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Wasserstein Gradient Flows for Batch Bayesian Optimal Experimental Design
- **Authors:** Louis Sharrock
- **arXiv:** [2603.12102](https://arxiv.org/abs/2603.12102v1) · [pdf](https://arxiv.org/pdf/2603.12102v1)
- **Categories:** stat.ML, cs.LG, stat.CO, stat.ME

### Abstract
> Bayesian optimal experimental design (BOED) provides a powerful, decision-theoretic framework for selecting experiments so as to maximise the expected utility of the data to be collected. In practice, however, its applicability can be limited by the difficulty of optimising the chosen utility. The expected information gain (EIG), for example, is often high-dimensional and strongly non-convex. This challenge is particularly acute in the batch setting, where multiple experiments are to be designed simultaneously. In this paper, we introduce a new approach to batch EIG-based BOED via a probabilistic lifting of the original optimisation problem to the space of probability measures. In particular, we propose to optimise an entropic regularisation of the expected utility over the space of design measures. Under mild conditions, we show that this objective admits a unique minimiser, which can be explicitly characterised in the form of a Gibbs distribution. The resulting design law can be used directly as a randomised batch-design policy, or as a computational relaxation from which a deterministic batch is extracted. To obtain scalable approximations when the batch size is large, we then consider two tractable restrictions of the full batch distribution: a mean-field family, and an i.i.d. product family. For the i.i.d. objective, and formally for its mean-field extension, we derive the corresponding Wasserstein gradient flow, characterise its long-time behaviour, and obtain particle-based algorithms via space-time discretisations. We also introduce doubly stochastic variants that combine interacting particle updates with Monte Carlo estimators of the EIG gradient. Finally, we illustrate the performance of the proposed methods in several numerical experiments, demonstrating their ability to explore multimodal optimisation landscapes and obtain high-utility batches in challenging examples.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Controlled Swarm Gradient Dynamics
- **Authors:** Louison Aubert
- **arXiv:** [2603.12039](https://arxiv.org/abs/2603.12039v1) · [pdf](https://arxiv.org/pdf/2603.12039v1)
- **Categories:** math.OC, math.PR

### Abstract
> We consider the global optimization of a non-convex potential $U : \mathbb{R}^d \to \mathbb{R}$ and extend the controlled simulated annealing framework introduced by Molin et al. (2026) to the class of swarm gradient dynamics, a family of Langevin-type mean-field diffusions whose noise intensity depends locally on the marginal density of the process. Building on the time-homogeneous model of Huang and Malik (2025), we first analyze its invariant probability density and show that, as the inverse temperature parameter tends to infinity, it converges weakly to a probability measure supported on the set of global minimizers of $U$. This result justifies using this family of invariant measures as an annealing curve in a controlled swarm setting. Given an arbitrary non-decreasing cooling schedule, we then prove the existence of a velocity field solving the continuity equation associated with the curve of invariant densities. Superimposing this field onto the swarm gradient dynamics yields a well-posed controlled process whose marginal law follows exactly the prescribed annealing curve. As a consequence, the controlled swarm dynamics converges toward global minimizers with, in principle, arbitrarily fast convergence rates, entirely dictated by the choice of the cooling schedule. Finally, we discuss an algorithmic implementation of the controlled dynamics and compare its performance with controlled simulated annealing, highlighting some numerical limitations.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Few-for-Many Personalized Federated Learning
- **Authors:** Ping Guo, Tiantian Zhang, Xi Lin, Xiang Li, Zhi-Ri Tang, Qingfu Zhang
- **arXiv:** [2603.11992](https://arxiv.org/abs/2603.11992v1) · [pdf](https://arxiv.org/pdf/2603.11992v1)
- **Categories:** cs.AI, cs.LG

### Abstract
> Personalized Federated Learning (PFL) aims to train customized models for clients with highly heterogeneous data distributions while preserving data privacy. Existing approaches often rely on heuristics like clustering or model interpolation, which lack principled mechanisms for balancing heterogeneous client objectives. Serving $M$ clients with distinct data distributions is inherently a multi-objective optimization problem, where achieving optimal personalization ideally requires $M$ distinct models on the Pareto front. However, maintaining $M$ separate models poses significant scalability challenges in federated settings with hundreds or thousands of clients. To address this challenge, we reformulate PFL as a few-for-many optimization problem that maintains only $K$ shared server models ($K \ll M$) to collectively serve all $M$ clients. We prove that this framework achieves near-optimal personalization: the approximation error diminishes as $K$ increases and each client's model converges to each client's optimum as data grows. Building on this reformulation, we propose FedFew, a practical algorithm that jointly optimizes the $K$ server models through efficient gradient-based updates. Unlike clustering-based approaches that require manual client partitioning or interpolation-based methods that demand careful hyperparameter tuning, FedFew automatically discovers the optimal model diversity through its optimization process. Experiments across vision, NLP, and real-world medical imaging datasets demonstrate that FedFew, with just 3 models, consistently outperforms other state-of-the-art approaches. Code is available at https://github.com/pgg3/FedFew.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
