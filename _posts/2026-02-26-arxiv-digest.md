---
layout: post
title: "Daily arXiv Digest — 2026-02-26 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Provable Last-Iterate Convergence for Multi-Objective Safe LLM Alignment via Optimistic Primal-Dual
- **Authors:** Yining Li, Peizhong Ju, Ness Shroff
- **arXiv:** [2602.22146](https://arxiv.org/abs/2602.22146v1) · [pdf](https://arxiv.org/pdf/2602.22146v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Reinforcement Learning from Human Feedback (RLHF) plays a significant role in aligning Large Language Models (LLMs) with human preferences. While RLHF with expected reward constraints can be formulated as a primal-dual optimization problem, standard primal-dual methods only guarantee convergence with a distributional policy where the saddle-point problem is in convex-concave form. Moreover, standard primal-dual methods may exhibit instability or divergence in the last iterate under policy parameterization in practical applications. In this work, we propose a universal primal-dual framework for safe RLHF that unifies a broad class of existing alignment algorithms, including safe-RLHF, one-shot, and multi-shot based methods. Building on this framework, we introduce an optimistic primal-dual (OPD) algorithm that incorporates predictive updates for both primal and dual variables to stabilize saddle-point dynamics. We establish last-iterate convergence guarantees for the proposed method, covering both exact policy optimization in the distributional space and convergence to a neighborhood of the optimal solution whose gap is related to approximation error and bias under parameterized policies. Our analysis reveals that optimism plays a crucial role in mitigating oscillations inherent to constrained alignment objectives, thereby closing a key theoretical gap between constrained RL and practical RLHF.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Robust Kaczmarz methods for nearly singular linear systems
- **Authors:** Yunying Ke, Hao Luo
- **arXiv:** [2602.21916](https://arxiv.org/abs/2602.21916v1) · [pdf](https://arxiv.org/pdf/2602.21916v1)
- **Categories:** math.NA, math.OC

### Abstract
> The Kaczmarz method is an efficient iterative algorithm for large-scale linear systems. However, its linear convergence rate suffers from ill-conditioned problems and is highly sensitive to the smallest nonzero singular value. In this work, we aim to extend the classical Kaczmarz to nearly singular linear systems that are row rank-deficient. We introduce a new concept of nearly singular property by treating the row space as an unstable subspace in the Grassman manifold. We then define a related important space called the approximate kernel, based on which a robust kernel-augmented Kaczmarz (KaK) is introduced via the subspace correction framework and analyzed by the well-known Xu--Zikatanov identity. To get an implementable version, we further introduce the approximate dual kernel and transform KaK into an equivalent kernel-augmented coordinate descent. Furthermore, we develop an accelerated variant and establish the improved rate of convergence matching the optimal complexity of first-order methods. Compared with existing methods, ours achieve uniform convergence rates for nearly singular linear systems, and the robustness has been confirmed by some numerical tests.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Applying a Random-Key Optimizer on Mixed Integer Programs
- **Authors:** Antonio A. Chaves, Mauricio G. C. Resende, Carise E. Schmidt, J. Kyle Brubaker, Helmut G. Katzgraber
- **arXiv:** [2602.22173](https://arxiv.org/abs/2602.22173v1) · [pdf](https://arxiv.org/pdf/2602.22173v1)
- **Categories:** math.OC, cs.NE

### Abstract
> Mixed-Integer Programs (MIPs) are NP-hard optimization models that arise in a broad range of decision-making applications, including finance, logistics, energy systems, and network design. Although modern commercial solvers have achieved remarkable progress and perform effectively on many small- and medium-sized instances, their performance often degrades when confronted with large-cale or highly constrained formulations. This paper explores the use of the Random-Key Optimizer (RKO) framework as a flexible, metaheuristic alternative for computing high-quality solutions to MIPs through the design of problem-specific decoders. The proposed approach separates the search process from feasibility enforcement by operating in a continuous random-key space while mapping candidate solutions to feasible integer solutions via efficient decoding procedures. We evaluate the methodology on two representative and structurally distinct benchmark problems: the mean-variance Markowitz portfolio optimization problem with buy-in and cardinality constraints, and the Time-Dependent Traveling Salesman Problem. For each formulation, tailored decoders are developed to reduce the effective search space, promote feasibility, and accelerate convergence. Computational experiments demonstrate that RKO consistently produces competitive, and in several cases superior, solutions compared to a state-of-the-art commercial MIP solver, both in terms of solution quality and computational time. These results highlight the potential of RKO as a scalable and versatile heuristic framework for tackling challenging large-scale MIPs.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Robust Permutation Flowshops Under Budgeted Uncertainty
- **Authors:** Noam Goldberg, Danny Hermelin, Dvir Shabtay
- **arXiv:** [2602.22110](https://arxiv.org/abs/2602.22110v1) · [pdf](https://arxiv.org/pdf/2602.22110v1)
- **Categories:** cs.DS, cs.DM, math.OC

### Abstract
> We consider the robust permutation flowshop problem under the budgeted uncertainty model, where at most a given number of job processing times may deviate on each machine. We show that solutions for this problem can be determined by solving polynomially many instances of the corresponding nominal problem. As a direct consequence, our result implies that this robust flowshop problem can be solved in polynomial time for two machines, and can be approximated in polynomial time for any fixed number of machines. The reduction that is our main result follows from an analysis similar to Bertsimas and Sim (2003) except that dualization is applied to the terms of a min-max objective rather than to a linear objective function. Our result may be surprising considering that heuristic and exact integer programming based methods have been developed in the literature for solving the two-machine flowshop problem. We conclude by showing a logarithmic factor improvement in the overall running time implied by a naive reduction to nominal problems in the case of two machines and three machines.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Stochastic Optimal Control with Side Information and Bayesian Learning
- **Authors:** Johannes Milz, Alexander Shapiro, Enlu Zhou
- **arXiv:** [2602.22047](https://arxiv.org/abs/2602.22047v1) · [pdf](https://arxiv.org/pdf/2602.22047v1)
- **Categories:** math.OC, math.ST

### Abstract
> We study infinite-horizon stochastic optimal control problems with observable side information: a Markov chain that modulates an unknown context-conditional randomness distribution. Since this distribution is unknown, we propose a Bayesian reformulation based on a parametric density model and posterior predictive dynamics, which yields a Bayesian Bellman equation. We prove posterior consistency under Markov samples and, under correct specification and identifiability, uniform convergence of the Bayesian value function. Finally, we establish Bernstein--von Mises-type asymptotic normality for the data-driven contextual optimal value.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
