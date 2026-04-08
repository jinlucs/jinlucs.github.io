---
layout: post
title: "Daily arXiv Digest — 2026-04-08 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Value Mirror Descent for Reinforcement Learning
- **Authors:** Zhichao Jia, Guanghui Lan
- **arXiv:** [2604.06039](https://arxiv.org/abs/2604.06039v1) · [pdf](https://arxiv.org/pdf/2604.06039v1)
- **Categories:** math.OC, cs.LG, math.PR

### Abstract
> Value iteration-type methods have been extensively studied for computing a nearly optimal value function in reinforcement learning (RL). Under a generative sampling model, these methods can achieve sharper sample complexity than policy optimization approaches, particularly in their dependence on the discount factor. In practice, they are often employed for offline training or in simulated environments. In this paper, we consider discounted Markov decision processes with state space S, action space A, discount factor $γ\in(0,1)$ and costs in $[0,1]$. We introduce a novel value optimization method, termed value mirror descent (VMD), which integrates mirror descent from convex optimization into the classical value iteration framework. In the deterministic setting with known transition kernels, we show that VMD converges linearly. For the stochastic setting with a generative model, we develop a stochastic variant, SVMD, which incorporates variance reduction commonly used in stochastic value iteration-type methods. For RL problems with general convex regularizers, SVMD attains a near-optimal sample complexity of $\tilde{O}(|S||A|(1-γ)^{-3}ε^{-2})$. Moreover, we establish that the Bregman divergence between the generated and optimal policies remains bounded throughout the iterations. This property is absent in existing stochastic value iteration-type methods but is important for enabling effective online (continual) learning following offline training. Under a strongly convex regularizer, SVMD achieves sample complexity of $\tilde{O}(|S||A|(1-γ)^{-5}ε^{-1})$, improving performance in the high-accuracy regime. Furthermore, we prove convergence of the generated policy to the optimal policy. Overall, the proposed method, its analysis, and the resulting guarantees, constitute new contributions to the RL and optimization literature.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Neural Network Pruning via QUBO Optimization
- **Authors:** Osama Orabi, Artur Zagitov, Hadi Salloum, Viktor A. Lobachev, Kasymkhan Khubiev, Yaroslav Kholodov
- **arXiv:** [2604.05856](https://arxiv.org/abs/2604.05856v1) · [pdf](https://arxiv.org/pdf/2604.05856v1)
- **Categories:** cs.CV, cs.AI, cs.LG, cs.NE

### Abstract
> Neural network pruning can be formulated as a combinatorial optimization problem, yet most existing approaches rely on greedy heuristics that ignore complex interactions between filters. Formal optimization methods such as Quadratic Unconstrained Binary Optimization (QUBO) provide a principled alternative but have so far underperformed due to oversimplified objective formulations based on metrics like the L1-norm. In this work, we propose a unified Hybrid QUBO framework that bridges heuristic importance estimation with global combinatorial optimization. Our formulation integrates gradient-aware sensitivity metrics - specifically first-order Taylor and second-order Fisher information - into the linear term, while utilizing data-driven activation similarity in the quadratic term. This allows the QUBO objective to jointly capture individual filter relevance and inter-filter functional redundancy. We further introduce a dynamic capacity-driven search to strictly enforce target sparsity without distorting the optimization landscape. Finally, we employ a two-stage pipeline featuring a Tensor-Train (TT) Refinement stage - a gradient-free optimizer that fine-tunes the QUBO-derived solution directly against the true evaluation metric. Experiments on the SIDD image denoising dataset demonstrate that the proposed Hybrid QUBO significantly outperforms both greedy Taylor pruning and traditional L1-based QUBO, with TT Refinement providing further consistent gains at appropriate combinatorial scales. This highlights the potential of hybrid combinatorial formulations for robust, scalable, and interpretable neural network compression.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) High-dimensional reliability-based design optimization using stochastic emulators
- **Authors:** M. Moustapha, B. Sudret
- **arXiv:** [2604.05759](https://arxiv.org/abs/2604.05759v1) · [pdf](https://arxiv.org/pdf/2604.05759v1)
- **Categories:** stat.CO, stat.ME, stat.ML

### Abstract
> Reliability-based design optimization (RBDO) is traditionally formulated as a nested optimization and reliability problem. Although surrogate models are generally employed to improve efficiency, the approach remains computationally prohibitive in high-dimensional settings. This paper proposes a novel RBDO framework based on a stochastic simulator viewpoint, in which the deterministic limit-state function and the uncertainty in the model inputs are combined into a unified stochastic representation. Under this formulation, the system response conditioned on a given design is modeled directly through its output distribution, rather than through an explicit limit-state function. Stochastic emulators are constructed in the design space to approximate the conditional response distribution, enabling the semi-analytical evaluation of failure probabilities or associated quantiles without resorting to Monte Carlo simulation. Two classes of stochastic emulators are investigated, namely generalized lambda models and stochastic polynomial chaos expansions. Both approaches provide a deterministic mapping between design variables and reliability constraints, which breaks the classical double-loop structure of RBDO and allows the use of standard deterministic optimization algorithms. The performance of the proposed approach is evaluated on a set of benchmark problems with dimensionality ranging from low to very high, including a case with stochastic excitation. The results are compared against a Kriging-based approach formulated in the full input space. The proposed method yields substantial computational gains, particularly in high-dimensional settings. While its efficiency is comparable to Kriging for low-dimensional problems, it significantly outperforms Kriging as the dimensionality increases.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Consensus-based optimization with $α$-stable jump processes
- **Authors:** Pedro Aceves-Sanchez, Giacomo Albi, Federica Ferrarese, Michael Herty
- **arXiv:** [2604.05626](https://arxiv.org/abs/2604.05626v1) · [pdf](https://arxiv.org/pdf/2604.05626v1)
- **Categories:** math.OC

### Abstract
> In this paper, we introduce a novel variant of the CBO method that incorporates jumps according to an $α$-stable stochastic process in a kinetic framework. This extension gives rise to nonlocal stochastic effects, which improve the exploration capabilities of the method. We formulate the method at the particle level, detailing the corresponding stochastic dynamics and its asymptotic behavior. In particular, through a Fourier-based representation, we derive the associated fractional Fokker-Planck equation, which naturally accounts for the nonlocal diffusion behaviors induced by $α$-stable processes. As a central result, we establish a rigorous convergence result for the proposed approach. Finally, we evaluate the performance of the method through a set of numerical experiments. The results demonstrate the effectiveness of the $α$-stable jump process and emphasize its potential advantages over standard diffusion-based methods, particularly in complex optimization settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Accelerating Full-Scale Nonlinear Model Predictive Control via Surrogate Dynamics Optimization
- **Authors:** Perceval Beja-Battais, Guillaume Dupré, Alain Grossetête, Nicolas Vayatis
- **arXiv:** [2604.05566](https://arxiv.org/abs/2604.05566v1) · [pdf](https://arxiv.org/pdf/2604.05566v1)
- **Categories:** math.OC

### Abstract
> Driven by advances in hardware and software technologies, nonlinear model predictive control (NMPC) has gained increasing adoption in both industry and academia over the past decades. However, its practical deployment is often limited by the computational cost of simulating the embedded process model, especially for high-dimensional, multi-time-scale, or nonlinear systems commonly found in real-world applications. Thus, this paper introduces Surrogate Dynamics Optimization (SDO), a warm-start framework for full-scale NMPC to address the limitation of standard initialization strategies. The approach relies on a machine learning surrogate model to solve a lightweight auxiliary problem that approximates the original one. The methodology is reproducible and compatible with inhouse simulation and optimization tools, a key consideration in industrial contexts. Data efficiency of SDO, as well as the impact of surrogate design on the overall performance, are evaluated through a non-trivial simulation case study: 24-hour optimal load-following control of a pressurized water reactor. The results show consistent improvements in NMPC convergence speed within a fixed computational budget, while reducing training data generation costs by two orders of magnitude compared to behavior cloning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
