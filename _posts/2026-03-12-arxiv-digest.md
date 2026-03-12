---
layout: post
title: "Daily arXiv Digest — 2026-03-12 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Prioritizing Gradient Sign Over Modulus: An Importance-Aware Framework for Wireless Federated Learning
- **Authors:** Yiyang Yue, Jiacheng Yao, Wei Xu, Zhaohui Yang, George K. Karagiannidis, Dusit Niyato
- **arXiv:** [2603.10763](https://arxiv.org/abs/2603.10763v1) · [pdf](https://arxiv.org/pdf/2603.10763v1)
- **Categories:** cs.LG, cs.IT, eess.SP

### Abstract
> Wireless federated learning (FL) facilitates collaborative training of artificial intelligence (AI) models to support ubiquitous intelligent applications at the wireless edge. However, the inherent constraints of limited wireless resources inevitably lead to unreliable communication, which poses a significant challenge to wireless FL. To overcome this challenge, we propose Sign-Prioritized FL (SP-FL), a novel framework that improves wireless FL by prioritizing the transmission of important gradient information through uneven resource allocation. Specifically, recognizing the importance of descent direction in model updating, we transmit gradient signs in individual packets and allow their reuse for gradient descent if the remaining gradient modulus cannot be correctly recovered. To further improve the reliability of transmission of important information, we formulate a hierarchical resource allocation problem based on the importance disparity at both the packet and device levels, optimizing bandwidth allocation across multiple devices and power allocation between sign and modulus packets. To make the problem tractable, the one-step convergence behavior of SP-FL, which characterizes data importance at both levels in an explicit form, is analyzed. We then propose an alternating optimization algorithm to solve this problem using the Newton-Raphson method and successive convex approximation (SCA). Simulation results confirm the superiority of SP-FL, especially in resource-constrained scenarios, demonstrating up to 9.96\% higher testing accuracy on the CIFAR-10 dataset compared to existing methods.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Computing and Optimizing the $H^2$-norm of Delay Differential Algebraic Systems
- **Authors:** Evert Provoost, Wim Michiels
- **arXiv:** [2603.10734](https://arxiv.org/abs/2603.10734v1) · [pdf](https://arxiv.org/pdf/2603.10734v1)
- **Categories:** math.NA, math.OC

### Abstract
> We present a Lanczos tau method for the approximation and optimization of the $H^2$-norm of time-delay systems described by semi-explicit delay differential algebraic equations. The soundness of this approach is proven under the assumption of a finite strong $H^2$-norm. Furthermore, we prove convergence if the rational approximation of the exponential underlying the discretization is well-behaved and the discretization is stability preserving. Numerical results suggest that, for multiple delays, the method converges at cubic rate in the discretization degree for systems of retarded type and linearly for those of neutral type. In the single delay case, we note geometric convergence of the $H^2$-norm for systems of both retarded and neutral type when a symmetric basis is chosen. Explicit formulas are derived for the gradient of the approximation with respect to system parameters and delays. These allow us to compute the entire gradient using only about double the computational time of approximating the $H^2$-norm alone. We illustrate how these can be used to synthesize robust feedback controllers and stable approximate models. The article is concluded by a discussion of how the presented results extend and improve for approximations based on splines. We note acceleration of the convergence rate by about two orders for such a choice. Finally, we prove that a Lanczos tau method using a spline based on Legendre orthogonal polynomials preserves stability and guarantees convergence of the $H^2$-norm.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) SCORE: Replacing Layer Stacking with Contractive Recurrent Depth
- **Authors:** Guillaume Godin
- **arXiv:** [2603.10544](https://arxiv.org/abs/2603.10544v1) · [pdf](https://arxiv.org/pdf/2603.10544v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Residual connections are central to modern deep neural networks, enabling stable optimization and efficient information flow across depth. In this work, we propose SCORE (Skip-Connection ODE Recurrent Embedding), a discrete recurrent alternative to classical layer stacking. Instead of composing multiple independent layers, SCORE iteratively applies a single shared neural block using an ODE (Ordinary Differential Equation)-inspired contractive update: ht+1 = (1 - dt) * ht + dt * F(ht) This formulation can be interpreted as a depth-by-iteration refinement process, where the step size dt explicitly controls stability and update magnitude. Unlike continuous Neural ODE approaches, SCORE uses a fixed number of discrete iterations and standard backpropagation without requiring ODE solvers or adjoint methods. We evaluate SCORE across graph neural networks (ESOL molecular solubility), multilayer perceptrons, and Transformer-based language models (nanoGPT). Across architectures, SCORE generally improves convergence speed and often accelerates training. SCORE is reducing parameter count through shared weights. In practice, simple Euler integration provides the best trade-off between computational cost and performance, while higher-order integrators yield marginal gains at increased compute. These results suggest that controlled recurrent depth with contractive residual updates offers a lightweight and effective alternative to classical stacking in deep neural networks.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) UAV-MARL: Multi-Agent Reinforcement Learning for Time-Critical and Dynamic Medical Supply Delivery
- **Authors:** Islam Guven, Mehmet Parlak
- **arXiv:** [2603.10528](https://arxiv.org/abs/2603.10528v1) · [pdf](https://arxiv.org/pdf/2603.10528v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Unmanned aerial vehicles (UAVs) are increasingly used to support time-critical medical supply delivery, providing rapid and flexible logistics during emergencies and resource shortages. However, effective deployment of UAV fleets requires coordination mechanisms capable of prioritizing medical requests, allocating limited aerial resources, and adapting delivery schedules under uncertain operational conditions. This paper presents a multi-agent reinforcement learning (MARL) framework for coordinating UAV fleets in stochastic medical delivery scenarios where requests vary in urgency, location, and delivery deadlines. The problem is formulated as a partially observable Markov decision process (POMDP) in which UAV agents maintain awareness of medical delivery demands while having limited visibility of other agents due to communication and localization constraints. The proposed framework employs Proximal Policy Optimization (PPO) as the primary learning algorithm and evaluates several variants, including asynchronous extensions, classical actor--critic methods, and architectural modifications to analyze scalability and performance trade-offs. The model is evaluated using real-world geographic data from selected clinics and hospitals extracted from the OpenStreetMap dataset. The framework provides a decision-support layer that prioritizes medical tasks, reallocates UAV resources in real time, and assists healthcare personnel in managing urgent logistics. Experimental results show that classical PPO achieves superior coordination performance compared to asynchronous and sequential learning strategies, highlighting the potential of reinforcement learning for adaptive and scalable UAV-assisted healthcare logistics.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) On Utility Maximization under Multivariate Fake Stationary Affine Volterra Models
- **Authors:** Emmanuel Gnabeyeu
- **arXiv:** [2603.11046](https://arxiv.org/abs/2603.11046v1) · [pdf](https://arxiv.org/pdf/2603.11046v1)
- **Categories:** math.OC, math.PR, q-fin.CP

### Abstract
> This paper is concerned with Merton's portfolio optimization problem in a Volterra stochastic environment described by a multivariate fake stationary Volterra--Heston model. Due to the non-Markovianity and non-semimartingality of the underlying processes, the classical stochastic control approach cannot be directly applied in this setting. Instead, the problem is tackled using a stochastic factor solution to a Riccati backward stochastic differential equation (BSDE). Our approach is inspired by the martingale optimality principle combined with a suitable verification argument. The resulting optimal strategies for Merton's problems are derived in semi-closed form depending on the solutions to time-dependent multivariate Riccati-Volterra equations. Numerical results on a two dimensional fake stationary rough Heston model illustrate the impact of stationary rough volatilities on the optimal Merton strategies.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
