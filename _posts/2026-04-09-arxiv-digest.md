---
layout: post
title: "Daily arXiv Digest — 2026-04-09 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization
- **Authors:** Qiyao Ma, Dechen Gao, Rui Cai, Boqi Zhao, Hanchu Zhou, Junshan Zhang, Zhe Zhao
- **arXiv:** [2604.07343](https://arxiv.org/abs/2604.07343v1) · [pdf](https://arxiv.org/pdf/2604.07343v1)
- **Categories:** cs.CL, cs.LG

### Abstract
> Pluralistic alignment has emerged as a critical frontier in the development of Large Language Models (LLMs), with reward models (RMs) serving as a central mechanism for capturing diverse human values. While benchmarks for general response quality are prevalent, evaluating how well reward models account for individual user preferences remains an open challenge. To bridge this gap, we introduce Personalized RewardBench, a novel benchmark designed to rigorously assess reward models' capacity to model personalized preferences. We construct chosen and rejected response pairs based on strict adherence to (or violation of) user-specific rubrics, ensuring that preference distinctions are uniquely tailored to the individual. In particular, human evaluations confirm that the primary discriminative factor between pairs is strictly personal preference, with both responses maintaining high general quality (e.g., correctness, relevance and helpfulness). Extensive testing reveals that existing state-of-the-art reward models struggle significantly with personalization, peaking at an accuracy of just 75.94%. Crucially, because an effective reward model benchmark should predict a reward model's performance on downstream tasks, we conduct experiments demonstrating that our benchmark exhibits a significantly higher correlation with downstream performance in both Best-of-N (BoN) sampling and Proximal Policy Optimization (PPO) compared to existing baselines. These findings establish Personalized RewardBench as a robust and accurate proxy for evaluating reward models' performance in downstream applications.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) An Inexact Trust-Region Method for Structured Nonsmooth Optimization with Application to Risk-Averse Stochastic Programming
- **Authors:** Drew P. Kouri
- **arXiv:** [2604.07216](https://arxiv.org/abs/2604.07216v1) · [pdf](https://arxiv.org/pdf/2604.07216v1)
- **Categories:** math.OC

### Abstract
> We develop a trust-region method for efficiently minimizing the sum of a smooth function, a nonsmooth convex function, and the composition of a finite-valued support function with a smooth function. Optimization problems with this structure arise in numerous applications including risk-averse stochastic programming and subproblems for nonsmooth penalty nonlinear programming methods. Our method permits the use of inexact value and derivative information, enabling the solution of infinite-dimensional problems governed by, e.g., partial differential equations (PDEs). We prove global convergence of our method and under additional regularity assumptions, demonstrate that the sequence of iterates accumulates at a stationary point of our target problem. We demonstrate our method's efficiency on two PDE-constrained optimization examples, showing that its performance is invariant to the PDE discretization size.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Model-Free Aggregative Cooperative Optimization via Randomized Gradient-Free Minimization and Exploration Momentum
- **Authors:** Amir Mehrnoosh, Giuseppe Speciale, Riccardo Brumali, Giuseppe Notarstefano, Gianluca Bianchin
- **arXiv:** [2604.07164](https://arxiv.org/abs/2604.07164v1) · [pdf](https://arxiv.org/pdf/2604.07164v1)
- **Categories:** math.OC

### Abstract
> Aggregative cooperative optimization problems arise in distributed decision-making settings where each agent's objective depends on its own decision as well as on an aggregate variable capturing global system behavior. Motivated by practical scenarios where gradient information is unavailable, this paper introduces a randomized gradient-free algorithm, named ARGFree, for solving such problems. ARGFree combines finite-difference gradient approximations with a set of tracking variables, emulating the behavior of a gradient-based method. We prove that ARGFree converges in expectation to an approximate optimizer, with the approximation error stemming from the use of a randomized gradient estimator. To enhance performance in high-dimensional settings, we further propose an improved variant, ARGFree-EM, which incorporates momentum in the exploration signals to smooth sudden fluctuations in the gradient exploration signals and thereby improve the accuracy of the underlying distributed tracking mechanism. To the best of our knowledge, the class of ARGFree methods is the first in the literature capable of solving aggregating cooperative optimization problems without gradient information.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Continuous-Time Dynamics of the Difference-of-Convex Algorithm
- **Authors:** Yi-Shuai Niu
- **arXiv:** [2604.06926](https://arxiv.org/abs/2604.06926v1) · [pdf](https://arxiv.org/pdf/2604.06926v1)
- **Categories:** math.OC, cs.LG, math.DS

### Abstract
> We study the continuous-time structure of the difference-of-convex algorithm (DCA) for smooth DC decompositions with a strongly convex component. In dual coordinates, classical DCA is exactly the full-step explicit Euler discretization of a nonlinear autonomous system. This viewpoint motivates a damped DCA scheme, which is also a Bregman-regularized DCA variant, and whose vanishing-step limit yields a Hessian-Riemannian gradient flow generated by the convex part of the decomposition. For the damped scheme we prove monotone descent, asymptotic criticality, Kurdyka-Lojasiewicz convergence under boundedness, and a global linear rate under a metric DC-PL inequality. For the limiting flow we establish an exact energy identity, asymptotic criticality of bounded trajectories, explicit global rates under metric relative error bounds, finite-length and single-point convergence under a Kurdyka-Lojasiewicz hypothesis, and local exponential convergence near nondegenerate local minima. The analysis also reveals a global-local tradeoff: the half-relaxed scheme gives the best provable global guarantee in our framework, while the full-step scheme is locally fastest near a nondegenerate minimum. Finally, we show that different DC decompositions of the same objective induce different continuous dynamics through the metric generated by the convex component, providing a geometric criterion for decomposition quality and linking DCA with Bregman geometry.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Gaussian Approximation for Asynchronous Q-learning
- **Authors:** Artemy Rubtsov, Sergey Samsonov, Vladimir Ulyanov, Alexey Naumov
- **arXiv:** [2604.07323](https://arxiv.org/abs/2604.07323v1) · [pdf](https://arxiv.org/pdf/2604.07323v1)
- **Categories:** stat.ML, cs.LG, math.PR

### Abstract
> In this paper, we derive rates of convergence in the high-dimensional central limit theorem for Polyak-Ruppert averaged iterates generated by the asynchronous Q-learning algorithm with a polynomial stepsize $k^{-ω},\, ω\in (1/2, 1]$. Assuming that the sequence of state-action-next-state triples $(s_k, a_k, s_{k+1})_{k \geq 0}$ forms a uniformly geometrically ergodic Markov chain, we establish a rate of order up to $n^{-1/6} \log^{4} (nS A)$ over the class of hyper-rectangles, where $n$ is the number of samples used by the algorithm and $S$ and $A$ denote the numbers of states and actions, respectively. To obtain this result, we prove a high-dimensional central limit theorem for sums of martingale differences, which may be of independent interest. Finally, we present bounds for high-order moments for the algorithm's last iterate.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
