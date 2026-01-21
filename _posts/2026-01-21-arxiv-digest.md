---
layout: post
title: "Daily arXiv Digest — 2026-01-21 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) A universal linearized subspace refinement framework for neural networks
- **Authors:** Wenbo Cao, Weiwei Zhang
- **arXiv:** [2601.13989](https://arxiv.org/abs/2601.13989v1) · [pdf](https://arxiv.org/pdf/2601.13989v1)
- **Categories:** cs.LG

### Abstract
> Neural networks are predominantly trained using gradient-based methods, yet in many applications their final predictions remain far from the accuracy attainable within the model's expressive capacity. We introduce Linearized Subspace Refinement (LSR), a general and architecture-agnostic framework that exploits the Jacobian-induced linear residual model at a fixed trained network state. By solving a reduced direct least-squares problem within this subspace, LSR computes a subspace-optimal solution of the linearized residual model, yielding a refined linear predictor with substantially improved accuracy over standard gradient-trained solutions, without modifying network architectures, loss formulations, or training procedures. Across supervised function approximation, data-driven operator learning, and physics-informed operator fine-tuning, we show that gradient-based training often fails to access this attainable accuracy, even when local linearization yields a convex problem. This observation indicates that loss-induced numerical ill-conditioning, rather than nonconvexity or model expressivity, can constitute a dominant practical bottleneck. In contrast, one-shot LSR systematically exposes accuracy levels not fully exploited by gradient-based training, frequently achieving order-of-magnitude error reductions. For operator-constrained problems with composite loss structures, we further introduce Iterative LSR, which alternates one-shot LSR with supervised nonlinear alignment, transforming ill-conditioned residual minimization into numerically benign fitting steps and yielding accelerated convergence and improved accuracy. By bridging nonlinear neural representations with reduced-order linear solvers at fixed linearization points, LSR provides a numerically grounded and broadly applicable refinement framework for supervised learning, operator learning, and scientific computing.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Q-learning with Adjoint Matching
- **Authors:** Qiyang Li, Sergey Levine
- **arXiv:** [2601.14234](https://arxiv.org/abs/2601.14234v1) · [pdf](https://arxiv.org/pdf/2601.14234v1)
- **Categories:** cs.LG, cs.AI, cs.RO, stat.ML

### Abstract
> We propose Q-learning with Adjoint Matching (QAM), a novel TD-based reinforcement learning (RL) algorithm that tackles a long-standing challenge in continuous-action RL: efficient optimization of an expressive diffusion or flow-matching policy with respect to a parameterized Q-function. Effective optimization requires exploiting the first-order information of the critic, but it is challenging to do so for flow or diffusion policies because direct gradient-based optimization via backpropagation through their multi-step denoising process is numerically unstable. Existing methods work around this either by only using the value and discarding the gradient information, or by relying on approximations that sacrifice policy expressivity or bias the learned policy. QAM sidesteps both of these challenges by leveraging adjoint matching, a recently proposed technique in generative modeling, which transforms the critic's action gradient to form a step-wise objective function that is free from unstable backpropagation, while providing an unbiased, expressive policy at the optimum. Combined with temporal-difference backup for critic learning, QAM consistently outperforms prior approaches on hard, sparse reward tasks in both offline and offline-to-online RL.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Gradient Flow for Finding E-optimal Designs
- **Authors:** Jieling Shi, Kim-Chuan Toh, Xin T. Tong, Weng Kee Wong
- **arXiv:** [2601.14147](https://arxiv.org/abs/2601.14147v1) · [pdf](https://arxiv.org/pdf/2601.14147v1)
- **Categories:** math.OC, stat.CO

### Abstract
> We investigate the use of Wasserstein gradient flows for finding an $E$-optimal design for a regression model. Unlike the commonly used $D$- and $L$-optimality criteria, the $E$-criterion finds a design that maximizes the smallest eigenvalue of the information matrix, and so it is a non-differentiable criterion unless the minimum eigenvalue has geometric multiplicity equals to one. Such maximin design problems abound in statistical applications and present unique theoretical and computational challenges. Building on the differential structure of the $2$-Wasserstein space, we derive explicit formulas for the Wasserstein gradient of the $E$-optimality criterion in the simple-eigenvalue case. For higher multiplicities, we propose a Wasserstein steepest ascent direction and show that it can be computed exactly via a semidefinite programming (SDP) relaxation. We develop particle approximations that connect infinite-dimensional flows with finite-dimensional optimization, and provide approximation guarantees for empirical measures. Our framework extends naturally to constrained designs via projected Wasserstein gradient flows. Numerical experiments demonstrate that the proposed methods successfully recover $E$-optimal designs for both linear and nonlinear regression models, with competitive accuracy and scalability compared to existing heuristic approaches. This work highlights the potential of optimal transport-based dynamics as a unifying tool for studying challenging optimal design problems.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Differentiable Logic Synthesis: Spectral Coefficient Selection via Sinkhorn-Constrained Composition
- **Authors:** Gorgi Pavlov
- **arXiv:** [2601.13953](https://arxiv.org/abs/2601.13953v1) · [pdf](https://arxiv.org/pdf/2601.13953v1)
- **Categories:** cs.LG, cs.AR, cs.LO

### Abstract
> Learning precise Boolean logic via gradient descent remains challenging: neural networks typically converge to "fuzzy" approximations that degrade under quantization. We introduce Hierarchical Spectral Composition, a differentiable architecture that selects spectral coefficients from a frozen Boolean Fourier basis and composes them via Sinkhorn-constrained routing with column-sign modulation. Our approach draws on recent insights from Manifold-Constrained Hyper-Connections (mHC), which demonstrated that projecting routing matrices onto the Birkhoff polytope preserves identity mappings and stabilizes large-scale training. We adapt this framework to logic synthesis, adding column-sign modulation to enable Boolean negation -- a capability absent in standard doubly stochastic routing. We validate our approach across four phases of increasing complexity: (1) For n=2 (16 Boolean operations over 4-dim basis), gradient descent achieves 100% accuracy with zero routing drift and zero-loss quantization to ternary masks. (2) For n=3 (10 three-variable operations), gradient descent achieves 76% accuracy, but exhaustive enumeration over 3^8 = 6561 configurations proves that optimal ternary masks exist for all operations (100% accuracy, 39% sparsity). (3) For n=4 (10 four-variable operations over 16-dim basis), spectral synthesis -- combining exact Walsh-Hadamard coefficients, ternary quantization, and MCMC refinement with parallel tempering -- achieves 100% accuracy on all operations. This progression establishes (a) that ternary polynomial threshold representations exist for all tested functions, and (b) that finding them requires methods beyond pure gradient descent as dimensionality grows. All operations enable single-cycle combinational logic inference at 10,959 MOps/s on GPU, demonstrating viability for hardware-efficient neuro-symbolic logic synthesis.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow
- **Authors:** Haocheng Xi, Charlie Ruan, Peiyuan Liao, Yujun Lin, Han Cai, Yilong Zhao, Shuo Yang, Kurt Keutzer, Song Han, Ligeng Zhu
- **arXiv:** [2601.14243](https://arxiv.org/abs/2601.14243v1) · [pdf](https://arxiv.org/pdf/2601.14243v1)
- **Categories:** cs.LG, cs.CL

### Abstract
> Reinforcement learning (RL) is essential for enhancing the complex reasoning capabilities of large language models (LLMs). However, existing RL training pipelines are computationally inefficient and resource-intensive, with the rollout phase accounting for over 70% of total training time. Quantized RL training, particularly using FP8 precision, offers a promising approach to mitigating this bottleneck. A commonly adopted strategy applies FP8 precision during rollout while retaining BF16 precision for training. In this work, we present the first comprehensive study of FP8 RL training and demonstrate that the widely used BF16-training + FP8-rollout strategy suffers from severe training instability and catastrophic accuracy collapse under long-horizon rollouts and challenging tasks. Our analysis shows that these failures stem from the off-policy nature of the approach, which introduces substantial numerical mismatch between training and inference. Motivated by these observations, we propose Jet-RL, an FP8 RL training framework that enables robust and stable RL optimization. The key idea is to adopt a unified FP8 precision flow for both training and rollout, thereby minimizing numerical discrepancies and eliminating the need for inefficient inter-step calibration. Extensive experiments validate the effectiveness of Jet-RL: our method achieves up to 33% speedup in the rollout phase, up to 41% speedup in the training phase, and a 16% end-to-end speedup over BF16 training, while maintaining stable convergence across all settings and incurring negligible accuracy degradation.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
