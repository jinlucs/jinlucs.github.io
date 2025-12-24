---
layout: post
title: "Daily arXiv Digest — 2025-12-24 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Random Gradient-Free Optimization in Infinite Dimensional Spaces
- **Authors:** Caio Lins Peixoto, Daniel Csillag, Bernardo F. P. da Costa, Yuri F. Saporito
- **arXiv:** [2512.20566](https://arxiv.org/abs/2512.20566v1) · [pdf](https://arxiv.org/pdf/2512.20566v1)
- **Categories:** math.OC

### Abstract
> In this paper, we propose a random gradient-free method for optimization in infinite dimensional Hilbert spaces, applicable to functional optimization in diverse settings. Though such problems are often solved through finite-dimensional gradient descent over a parametrization of the functions, such as neural networks, an interesting alternative is to instead perform gradient descent directly in the function space by leveraging its Hilbert space structure, thus enabling provable guarantees and fast convergence. However, infinite-dimensional gradients are often hard to compute in practice, hindering the applicability of such methods. To overcome this limitation, our framework requires only the computation of directional derivatives and a pre-basis for the Hilbert space domain, i.e., a linearly-independent set whose span is dense in the Hilbert space. This fully resolves the tractability issue, as pre-bases are much more easily obtained than full orthonormal bases or reproducing kernels -- which may not even exist -- and individual directional derivatives can be easily computed using forward-mode scalar automatic differentiation. We showcase the use of our method to solve partial differential equations à la physics informed neural networks (PINNs), where it effectively enables provable convergence.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) HGAN-SDEs: Learning Neural Stochastic Differential Equations with Hermite-Guided Adversarial Training
- **Authors:** Yuanjian Xu, Yuan Shuai, Jianing Hao, Guang Zhang
- **arXiv:** [2512.20272](https://arxiv.org/abs/2512.20272v1) · [pdf](https://arxiv.org/pdf/2512.20272v1)
- **Categories:** cs.LG

### Abstract
> Neural Stochastic Differential Equations (Neural SDEs) provide a principled framework for modeling continuous-time stochastic processes and have been widely adopted in fields ranging from physics to finance. Recent advances suggest that Generative Adversarial Networks (GANs) offer a promising solution to learning the complex path distributions induced by SDEs. However, a critical bottleneck lies in designing a discriminator that faithfully captures temporal dependencies while remaining computationally efficient. Prior works have explored Neural Controlled Differential Equations (CDEs) as discriminators due to their ability to model continuous-time dynamics, but such architectures suffer from high computational costs and exacerbate the instability of adversarial training. To address these limitations, we introduce HGAN-SDEs, a novel GAN-based framework that leverages Neural Hermite functions to construct a structured and efficient discriminator. Hermite functions provide an expressive yet lightweight basis for approximating path-level dynamics, enabling both reduced runtime complexity and improved training stability. We establish the universal approximation property of our framework for a broad class of SDE-driven distributions and theoretically characterize its convergence behavior. Extensive empirical evaluations on synthetic and real-world systems demonstrate that HGAN-SDEs achieve superior sample quality and learning efficiency compared to existing generative models for SDEs

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Leveraging High-Fidelity Digital Models and Reinforcement Learning for Mission Engineering: A Case Study of Aerial Firefighting Under Perfect Information
- **Authors:** İbrahim Oğuz Çetinkaya, Sajad Khodadadian, Taylan G. Topçu
- **arXiv:** [2512.20589](https://arxiv.org/abs/2512.20589v1) · [pdf](https://arxiv.org/pdf/2512.20589v1)
- **Categories:** cs.CY, cs.AI, eess.SY, math.OC

### Abstract
> As systems engineering (SE) objectives evolve from design and operation of monolithic systems to complex System of Systems (SoS), the discipline of Mission Engineering (ME) has emerged which is increasingly being accepted as a new line of thinking for the SE community. Moreover, mission environments are uncertain, dynamic, and mission outcomes are a direct function of how the mission assets will interact with this environment. This proves static architectures brittle and calls for analytically rigorous approaches for ME. To that end, this paper proposes an intelligent mission coordination methodology that integrates digital mission models with Reinforcement Learning (RL), that specifically addresses the need for adaptive task allocation and reconfiguration. More specifically, we are leveraging a Digital Engineering (DE) based infrastructure that is composed of a high-fidelity digital mission model and agent-based simulation; and then we formulate the mission tactics management problem as a Markov Decision Process (MDP), and employ an RL agent trained via Proximal Policy Optimization. By leveraging the simulation as a sandbox, we map the system states to actions, refining the policy based on realized mission outcomes. The utility of the RL-based intelligent mission coordinator is demonstrated through an aerial firefighting case study. Our findings indicate that the RL-based intelligent mission coordinator not only surpasses baseline performance but also significantly reduces the variability in mission performance. Thus, this study serves as a proof of concept demonstrating that DE-enabled mission simulations combined with advanced analytical tools offer a mission-agnostic framework for improving ME practice; which can be extended to more complicated fleet design and selection problems in the future from a mission-first perspective.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Adaptive Accelerated Gradient Method for Smooth Convex Optimization
- **Authors:** Zepeng Wang, Juan Peypouquet
- **arXiv:** [2512.20478](https://arxiv.org/abs/2512.20478v1) · [pdf](https://arxiv.org/pdf/2512.20478v1)
- **Categories:** math.OC

### Abstract
> We propose an adaptive accelerated gradient method for solving smooth convex optimization problems. The method incorporates a scheme to determine the step size adaptively, by means of a local estimation of the smoothness constant, which is assumed unknown, without resorting to line search procedures. The sequence generated by this method converges weakly to a minimizer of the objective function, and the function values converge at a fast rate of $\mathcal{O}\left( \frac{1}{k^2} \right)$. Moreover, if the objective function is strongly convex, the function values converge at a linear rate.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Shadow splitting methods for nonconvex optimisation: epi-approximation, convergence and saddle point avoidance
- **Authors:** Felipe Atenas
- **arXiv:** [2512.20433](https://arxiv.org/abs/2512.20433v1) · [pdf](https://arxiv.org/pdf/2512.20433v1)
- **Categories:** math.OC

### Abstract
> We propose the shadow Davis-Yin three-operator splitting method to solve nonconvex optimisation problems. Its convergence analysis is based on a merit function resembling the Moreau envelope. We explore variational analysis properties behind the merit function and the iteration operators associated with the shadow method. By capitalising on these results, we establish convergence of a damped version of the shadow method via sufficient descent of the merit function, and obtain (almost surely) guarantees of avoidance of strict saddle points of weakly convex semialgebraic optimisation problems. We perform numerical experiments for a nonconvex variable selection problem to test our findings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
