---
layout: post
title: "Daily arXiv Digest — 2026-02-11 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Supervised Metric Regularization Through Alternating Optimization for Multi-Regime Physics-Informed Neural Networks
- **Authors:** Enzo Nicolas Spotorno, Josafat Ribeiro Leal, Antonio Augusto Frohlich
- **arXiv:** [2602.09980](https://arxiv.org/abs/2602.09980v1) · [pdf](https://arxiv.org/pdf/2602.09980v1)
- **Categories:** cs.LG, cs.AI, physics.comp-ph

### Abstract
> Standard Physics-Informed Neural Networks (PINNs) often face challenges when modeling parameterized dynamical systems with sharp regime transitions, such as bifurcations. In these scenarios, the continuous mapping from parameters to solutions can result in spectral bias or "mode collapse", where the network averages distinct physical behaviors. We propose a Topology-Aware PINN (TAPINN) that aims to mitigate this challenge by structuring the latent space via Supervised Metric Regularization. Unlike standard parametric PINNs that map physical parameters directly to solutions, our method conditions the solver on a latent state optimized to reflect the metric-based separation between regimes, showing ~49% lower physics residual (0.082 vs. 0.160). We train this architecture using a phase-based Alternating Optimization (AO) schedule to manage gradient conflicts between the metric and physics objectives. Preliminary experiments on the Duffing Oscillator demonstrate that while standard baselines suffer from spectral bias and high-capacity Hypernetworks overfit (memorizing data while violating physics), our approach achieves stable convergence with 2.18x lower gradient variance than a multi-output Sobolev Error baseline, and 5x fewer parameters than a hypernetwork-based alternative.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Hybrid Responsible AI-Stochastic Approach for SLA Compliance in Multivendor 6G Networks
- **Authors:** Emanuel Figetakis, Ahmed Refaey Hussein
- **arXiv:** [2602.09841](https://arxiv.org/abs/2602.09841v1) · [pdf](https://arxiv.org/pdf/2602.09841v1)
- **Categories:** cs.NI, cs.AI, cs.LG

### Abstract
> The convergence of AI and 6G network automation introduces new challenges in maintaining transparency, fairness, and accountability across multivendor management systems. Although closed-loop AI orchestration improves adaptability and self-optimization, it also creates a responsibility gap, where violations of SLAs cannot be causally attributed to specific agents or vendors. This paper presents a hybrid responsible AI-stochastic learning framework that embeds fairness, robustness, and auditability directly into the network control loop. The framework integrates RAI games with stochastic optimization, enabling dynamic adversarial reweighting and probabilistic exploration across heterogeneous vendor domains. An RAAP continuously records AI-driven decision trajectories and produces dual accountability reports: user-level SLA summaries and operator-level responsibility analytics. Experimental evaluations on synthetic two-class multigroup datasets demonstrate that the proposed hybrid model improves the accuracy of the worst group by up to 10.5\%. Specifically, hybrid RAI achieved a WGAcc of 60.5\% and an AvgAcc of 72.7\%, outperforming traditional RAI-GA (50.0\%) and ERM (21.5\%). The audit mechanism successfully traced 99\% simulated SLA violations to the AI entities responsible, producing both vendor and agent-level accountability indices. These results confirm that the proposed hybrid approach enhances fairness and robustness as well as establishes a concrete accountability framework for autonomous SLA assurance in multivendor 6G networks.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) ADORA: Training Reasoning Models with Dynamic Advantage Estimation on Reinforcement Learning
- **Authors:** Qingnan Ren, Shiting Huang, Zhen Fang, Zehui Chen, Lin Chen, Lijun Li, Feng Zhao
- **arXiv:** [2602.10019](https://arxiv.org/abs/2602.10019v1) · [pdf](https://arxiv.org/pdf/2602.10019v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Reinforcement learning has become a cornerstone technique for developing reasoning models in complex tasks, ranging from mathematical problem-solving to imaginary reasoning. The optimization of these models typically relies on policy gradient methods, whose efficacy hinges on the accurate estimation of an advantage function. However, prevailing methods typically employ static advantage estimation, a practice that leads to inefficient credit assignment by neglecting the dynamic utility of training samples over time. This limitation results in suboptimal policy updates, which in turn manifest as slower convergence rates and increased learning instability, as models fail to adapt to evolving sample utilities effectively. To address this problem, we introduce \textbf{ADORA} (\textbf{A}dvantage \textbf{D}ynamics via \textbf{O}nline \textbf{R}ollout \textbf{A}daptation), a novel framework for policy optimization. ADORA dynamically adjusts the advantage function's weighting by adaptively categorizing training data into temporarily advantageous and disadvantageous samples, based on their evolving utility during online model rollouts. This tailored data differentiation strategy allows ADORA to be seamlessly integrated into existing policy optimization algorithms without significant architectural modifications, enabling the policy to prioritize learning from more informative experiences and thereby achieve more efficient policy updates. Extensive evaluations across diverse model families and varying data scales demonstrate that ADORA is a robust and efficient framework. It significantly enhances long reasoning in both geometric and mathematical tasks, consistently achieving notable performance gains without requiring sensitive hyperparameter tuning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Adaptive Single-Loop Methods for Stochastic Minimax Optimization on Riemannian Manifolds
- **Authors:** Hongye Wang, Chang He, Bo Jiang
- **arXiv:** [2602.09840](https://arxiv.org/abs/2602.09840v1) · [pdf](https://arxiv.org/pdf/2602.09840v1)
- **Categories:** math.OC

### Abstract
> Stochastic minimax optimization on Riemannian manifolds has recently attracted significant attention due to its broad range of applications, such as robust training of neural networks and robust maximum likelihood estimation. Existing optimization methods for these problems typically require selecting stepsizes based on prior knowledge of specific problem parameters, such as Lipschitz-type constants and (geodesic) strong concavity constants. Unfortunately, these parameters are often unknown in practice. To overcome this issue, we develop single-loop adaptive methods that automatically adjust stepsizes using cumulative Riemannian (stochastic) gradient norms. We first propose a deterministic single-loop Riemannian adaptive gradient descent ascent method and show that it attains an $ε$-stationary point within $O(ε^{-2})$ iterations. This deterministic method is of independent interest and lays the foundation for our subsequent stochastic method. In particular, we propose the Riemannian stochastic adaptive gradient descent ascent method, which finds an $ε$-stationary point in $O(ε^{-6})$ iterations. Under additional second-order smoothness, this iteration complexity is further improved to $O(ε^{-4})$, which even outperforms the corresponding complexity result in Euclidean space. Some numerical experiments on real-world applications are conducted, including the regularized robust maximum likelihood estimation problem, and the robust training of neural networks with orthonormal weights. The results are encouraging and demonstrate the effectiveness of adaptivity in practice.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) ExO-PPO: an Extended Off-policy Proximal Policy Optimization Algorithm
- **Authors:** Hanyong Wang, Menglong Yang
- **arXiv:** [2602.09726](https://arxiv.org/abs/2602.09726v1) · [pdf](https://arxiv.org/pdf/2602.09726v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Deep reinforcement learning has been able to solve various tasks successfully, however, due to the construction of policy gradient and training dynamics, tuning deep reinforcement learning models remains challenging. As one of the most successful deep reinforcement-learning algorithm, the Proximal Policy Optimization algorithm (PPO) clips the policy gradient within a conservative on-policy updates, which ensures reliable and stable policy improvement. However, this training pattern may sacrifice sample efficiency. On the other hand, off-policy methods make more adequate use of data through sample reuse, though at the cost of increased the estimation variance and bias. To leverage the advantages of both, in this paper, we propose a new PPO variant based on the stability guarantee from conservative on-policy iteration with a more efficient off-policy data utilization. Specifically, we first derive an extended off-policy improvement from an expectation form of generalized policy improvement lower bound. Then, we extend the clipping mechanism with segmented exponential functions for a suitable surrogate objective function. Third, the trajectories generated by the past $M$ policies are organized in the replay buffer for off-policy training. We refer to this method as Extended Off-policy Proximal Policy Optimization (ExO-PPO). Compared with PPO and some other state-of-the-art variants, we demonstrate an improved performance of ExO-PPO with balanced sample efficiency and stability on varied tasks in the empirical experiments.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
