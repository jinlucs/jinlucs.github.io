---
layout: post
title: "Daily arXiv Digest — 2026-01-01 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Many Minds from One Model: Bayesian Transformers for Population Intelligence
- **Authors:** Diji Yang, Yi Zhang
- **arXiv:** [2512.25063](https://arxiv.org/abs/2512.25063v1) · [pdf](https://arxiv.org/pdf/2512.25063v1)
- **Categories:** cs.LG, cs.CL

### Abstract
> Despite their scale and success, modern transformers are almost universally trained as single-minded systems: optimization produces one deterministic set of parameters, representing a single functional hypothesis about the data. Motivated by the idea that intelligence emerge from many minds, we propose Population Bayesian Transformers (B-Trans), which transform a standard Large Language Model into a Bayesian Transformer model to supports sampling diverse yet coherent model instances from a single set of pre-trained weights. B-Trans introduces a Bayesian-motivated posterior proxy by treating the bias-like offsets in normalization layers as stochastic variables with a Gaussian variational approximation, inducing a distribution over model behavior without the cost of training full Bayesian neural networks. Sampling from this proxy yields a set of model instances with diverse behaviors while maintaining general competence. To preserve coherence within each generation, we freeze the sampled noise at the sequence level, enforcing temporal consistency across tokens. B-Trans allows for population-level decision-making, where aggregating predictions across sampled individuals significantly enhances exploration. Experiments across zero-shot generation, Reinforcement Learning with Verifiable Rewards (RLVR), and RL without explicit labels demonstrate that B-Trans effectively leverage the wisdom of crowds, yielding superior semantic diversity while achieving better task performance compared to deterministic baselines.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Convergence of the generalization error for deep gradient flow methods for PDEs
- **Authors:** Chenguang Liu, Antonis Papapantoleon, Jasper Rou
- **arXiv:** [2512.25017](https://arxiv.org/abs/2512.25017v1) · [pdf](https://arxiv.org/pdf/2512.25017v1)
- **Categories:** math.NA, cs.LG, q-fin.CP, stat.ML

### Abstract
> The aim of this article is to provide a firm mathematical foundation for the application of deep gradient flow methods (DGFMs) for the solution of (high-dimensional) partial differential equations (PDEs). We decompose the generalization error of DGFMs into an approximation and a training error. We first show that the solution of PDEs that satisfy reasonable and verifiable assumptions can be approximated by neural networks, thus the approximation error tends to zero as the number of neurons tends to infinity. Then, we derive the gradient flow that the training process follows in the ``wide network limit'' and analyze the limit of this flow as the training time tends to infinity. These results combined show that the generalization error of DGFMs tends to zero as the number of neurons and the training time tend to infinity.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) A Pontryagin Maximum Principle on the Belief Space for Continuous-Time Optimal Control with Discrete Observations
- **Authors:** Christian Bayer, Saifeddine Ben naamia, Erik von Schwerin, Raul Tempone
- **arXiv:** [2512.24916](https://arxiv.org/abs/2512.24916v1) · [pdf](https://arxiv.org/pdf/2512.24916v1)
- **Categories:** math.OC, math.PR

### Abstract
> We study a continuous time stochastic optimal control problem under partial observations that are available only at discrete time instants. This hybrid setting, with continuous dynamics and intermittent noisy measurements, arises in applications ranging from robotic exploration and target tracking to epidemic control. We formulate the problem on the space of beliefs (information states), treating the controller's posterior distribution of the state as the state variable for decision making. On this belief space we derive a Pontryagin maximum principle that provides necessary conditions for optimality. The analysis carefully tracks both the continuous evolution of the state between observation times and the Bayesian jump updates of the belief at observation instants. A key insight is a relationship between the adjoint process in our maximum principle and the gradient of the value functional on the belief space, which links the optimality conditions to the dynamic programming approach on the space of probability measures. The resulting optimality system has a prediction and update structure that is closely related to the unnormalised Zakai equation and the normalised Kushner-Stratonovich equation in nonlinear filtering. Building on this analysis, we design a particle based numerical scheme to approximate the coupled forward (filter) and backward (adjoint) system. The scheme uses particle filtering to represent the evolving belief and regression techniques to approximate the adjoint, which yields a practical algorithm for computing near optimal controls under partial information. The effectiveness of the approach is illustrated on both linear and nonlinear examples and highlights in particular the benefits of actively controlling the observation process.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Tensor Based Proximal Alternating Minimization Method for A Kind of Inhomogeneous Quartic Optimization Problem
- **Authors:** Haibin Chen, Yixuan Chen, Chunyan Wang, Qi Fan
- **arXiv:** [2512.24872](https://arxiv.org/abs/2512.24872v1) · [pdf](https://arxiv.org/pdf/2512.24872v1)
- **Categories:** math.OC

### Abstract
> In this paper, we propose an efficient numerical approach for solving a specific type of quartic inhomogeneous polynomial optimization problem inspired by practical applications. The primary contribution of this work lies in establishing an inherent equivalence between the quartic inhomogeneous polynomial optimization problem and a multilinear optimization problem (MOP). This result extends the equivalence between fourth-order homogeneous polynomial optimization and multilinear optimization in the existing literature to the equivalence between fourth-order inhomogeneous polynomial optimization and multilinear optimization. By leveraging the multi-block structure embedded within the MOP, a tensor-based proximal alternating minimization algorithm is proposed to approximate the optimal value of the quartic problem. Under mild assumptions, the convergence of the algorithm is rigorously proven. Finally, the effectiveness of the proposed algorithm is demonstrated through preliminary computational results obtained using synthetic datasets.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Gradient Descent as Implicit EM in Distance-Based Neural Models
- **Authors:** Alan Oursland
- **arXiv:** [2512.24780](https://arxiv.org/abs/2512.24780v1) · [pdf](https://arxiv.org/pdf/2512.24780v1)
- **Categories:** cs.LG

### Abstract
> Neural networks trained with standard objectives exhibit behaviors characteristic of probabilistic inference: soft clustering, prototype specialization, and Bayesian uncertainty tracking. These phenomena appear across architectures -- in attention mechanisms, classification heads, and energy-based models -- yet existing explanations rely on loose analogies to mixture models or post-hoc architectural interpretation. We provide a direct derivation. For any objective with log-sum-exp structure over distances or energies, the gradient with respect to each distance is exactly the negative posterior responsibility of the corresponding component: $\partial L / \partial d_j = -r_j$. This is an algebraic identity, not an approximation. The immediate consequence is that gradient descent on such objectives performs expectation-maximization implicitly -- responsibilities are not auxiliary variables to be computed but gradients to be applied. No explicit inference algorithm is required because inference is embedded in optimization. This result unifies three regimes of learning under a single mechanism: unsupervised mixture modeling, where responsibilities are fully latent; attention, where responsibilities are conditioned on queries; and cross-entropy classification, where supervision clamps responsibilities to targets. The Bayesian structure recently observed in trained transformers is not an emergent property but a necessary consequence of the objective geometry. Optimization and inference are the same process.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
