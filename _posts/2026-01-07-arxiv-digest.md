---
layout: post
title: "Daily arXiv Digest — 2026-01-07 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) On the Convergence Behavior of Preconditioned Gradient Descent Toward the Rich Learning Regime
- **Authors:** Shuai Jiang, Alexey Voronin, Eric Cyr, Ben Southworth
- **arXiv:** [2601.03162](https://arxiv.org/abs/2601.03162v1) · [pdf](https://arxiv.org/pdf/2601.03162v1)
- **Categories:** cs.LG

### Abstract
> Spectral bias, the tendency of neural networks to learn low frequencies first, can be both a blessing and a curse. While it enhances the generalization capabilities by suppressing high-frequency noise, it can be a limitation in scientific tasks that require capturing fine-scale structures. The delayed generalization phenomenon known as grokking is another barrier to rapid training of neural networks. Grokking has been hypothesized to arise as learning transitions from the NTK to the feature-rich regime. This paper explores the impact of preconditioned gradient descent (PGD), such as Gauss-Newton, on spectral bias and grokking phenomena. We demonstrate through theoretical and empirical results how PGD can mitigate issues associated with spectral bias. Additionally, building on the rich learning regime grokking hypothesis, we study how PGD can be used to reduce delays associated with grokking. Our conjecture is that PGD, without the impediment of spectral bias, enables uniform exploration of the parameter space in the NTK regime. Our experimental results confirm this prediction, providing strong evidence that grokking represents a transitional behavior between the lazy regime characterized by the NTK and the rich regime. These findings deepen our understanding of the interplay between optimization dynamics, spectral bias, and the phases of neural network learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Revisiting a Fast Newton Solver for a 2-D Spectral Estimation Problem: Computations with the Full Hessian
- **Authors:** Ji Cheng, Bin Zhu
- **arXiv:** [2601.02690](https://arxiv.org/abs/2601.02690v1) · [pdf](https://arxiv.org/pdf/2601.02690v1)
- **Categories:** math.OC

### Abstract
> Spectral estimation plays a fundamental role in frequency-domain identification and related signal processing problems. This paper revisits a 2-D spectral estimation problem formulated in terms of convex optimization. More precisely, we work with the dual optimization problem and show that the full Hessian of the dual function admits a Toeplitz-block Toeplitz structure which is consistent with our finding in a previous work. This particular structure of the Hessian enables a fast inversion algorithm in the solution of the dual optimization problem via Newton's method whose superior speed of convergence is illustrated via simulations.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Dynamic Hyperparameter Importance for Efficient Multi-Objective Optimization
- **Authors:** Daphne Theodorakopoulos, Marcel Wever, Marius Lindauer
- **arXiv:** [2601.03166](https://arxiv.org/abs/2601.03166v1) · [pdf](https://arxiv.org/pdf/2601.03166v1)
- **Categories:** cs.LG

### Abstract
> Choosing a suitable ML model is a complex task that can depend on several objectives, e.g., accuracy, model size, fairness, inference time, or energy consumption. In practice, this requires trading off multiple, often competing, objectives through multi-objective optimization (MOO). However, existing MOO methods typically treat all hyperparameters as equally important, overlooking that hyperparameter importance (HPI) can vary significantly depending on the trade-off between objectives. We propose a novel dynamic optimization approach that prioritizes the most influential hyperparameters based on varying objective trade-offs during the search process, which accelerates empirical convergence and leads to better solutions. Building on prior work on HPI for MOO post-analysis, we now integrate HPI, calculated with HyperSHAP, into the optimization. For this, we leverage the objective weightings naturally produced by the MOO algorithm ParEGO and adapt the configuration space by fixing the unimportant hyperparameters, allowing the search to focus on the important ones. Eventually, we validate our method with diverse tasks from PyMOO and YAHPO-Gym. Empirical results demonstrate improvements in convergence speed and Pareto front quality compared to baselines.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Finite Memory Belief Approximation for Optimal Control in Partially Observable Markov Decision Processes
- **Authors:** Mintae Kim
- **arXiv:** [2601.03132](https://arxiv.org/abs/2601.03132v1) · [pdf](https://arxiv.org/pdf/2601.03132v1)
- **Categories:** eess.SY, cs.IT, cs.LG

### Abstract
> We study finite memory belief approximation for partially observable (PO) stochastic optimal control (SOC) problems. While belief states are sufficient for SOC in partially observable Markov decision processes (POMDPs), they are generally infinite-dimensional and impractical. We interpret truncated input-output (IO) histories as inducing a belief approximation and develop a metric-based theory that directly relates information loss to control performance. Using the Wasserstein metric, we derive policy-conditional performance bounds that quantify value degradation induced by finite memory along typical closed-loop trajectories. Our analysis proceeds via a fixed-policy comparison: we evaluate two cost functionals under the same closed-loop execution and isolate the effect of replacing the true belief by its finite memory approximation inside the belief-level cost. For linear quadratic Gaussian (LQG) systems, we provide closed-form belief mismatch evaluation and empirically validate the predicted mechanism, demonstrating that belief mismatch decays approximately exponentially with memory length and that the induced performance mismatch scales accordingly. Together, these results provide a metric-aware characterization of what finite memory belief approximation can and cannot achieve in PO settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) A Relaxation Method for Nonsmooth Nonlinear Optimization with Binary Constraints
- **Authors:** Lianghai Xiao, Yitian Qian, Shaohua Pan
- **arXiv:** [2601.03008](https://arxiv.org/abs/2601.03008v1) · [pdf](https://arxiv.org/pdf/2601.03008v1)
- **Categories:** math.OC

### Abstract
> We study binary optimization problems of the form \( \min_{x\in\{-1,1\}^n} f(Ax-b) \) with possibly nonsmooth loss \(f\). Following the lifted rank-one semidefinite programming (SDP) approach\cite{qian2023matrix}, we develop a majorization-minimization algorithm by using the difference-of-convexity (DC) reformuation for the rank-one constraint and the Moreau envelop for the nonsmooth loss. We provide global complexity guarantees for the proposed \textbf{D}ifference of \textbf{C}onvex \textbf{R}elaxation \textbf{A}lgorithm (DCRA) and show that it produces an approximately feasible binary solution with an explicit bound on the optimality gap. Numerical experiments on synthetic and real datasets confirm that our method achieves superior accuracy and scalability compared with existing approaches.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
