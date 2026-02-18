---
layout: post
title: "Daily arXiv Digest — 2026-02-18 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) All roads lead to Rome: Path-following Augmented Lagrangian Methods via Bregman Proximal Regularization
- **Authors:** Emanuel Laude
- **arXiv:** [2602.15710](https://arxiv.org/abs/2602.15710v1) · [pdf](https://arxiv.org/pdf/2602.15710v1)
- **Categories:** math.OC

### Abstract
> We study Bregman proximal augmented Lagrangian methods with second-order oracles for convex convex-composite optimization problems. The outer loop is an instance of the Bregman proximal point algorithm with relative errors in the sense of Solodov and Svaiter, applied to the KKT operator associated with the problem. Akin to classical Lagrange-Newton methods, including primal-dual interior point methods the Bregman proximal point algorithm repeatedly solves regularized KKT inclusions by minimizing a smooth Bregman augmented Lagrangian function, obtained after marginalizing out the multiplier variables. Thanks to non-Euclidean geometries the marginal function is generalized self-concordant and therefore within the regime of Newton's method which converges quadratically if the step-size in the outer proximal point loop is chosen carefully. The operator-theoretic viewpoint allows us to employ the framework of metric subregularity to derive fast rates for the outer loop, and eventually state a joint complexity bound. Important special cases of our framework are a proximal variant of the exponential multiplier method due to Tseng and Bertsekas and interior-point proximal augmented Lagrangian schemes closely related to those of Pougkakiotis and Gondzio.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Fractional-Order Federated Learning
- **Authors:** Mohammad Partohaghighi, Roummel Marcia, YangQuan Chen
- **arXiv:** [2602.15380](https://arxiv.org/abs/2602.15380v1) · [pdf](https://arxiv.org/pdf/2602.15380v1)
- **Categories:** cs.LG

### Abstract
> Federated learning (FL) allows remote clients to train a global model collaboratively while protecting client privacy. Despite its privacy-preserving benefits, FL has significant drawbacks, including slow convergence, high communication cost, and non-independent-and-identically-distributed (non-IID) data. In this work, we present a novel FedAvg variation called Fractional-Order Federated Averaging (FOFedAvg), which incorporates Fractional-Order Stochastic Gradient Descent (FOSGD) to capture long-range relationships and deeper historical information. By introducing memory-aware fractional-order updates, FOFedAvg improves communication efficiency and accelerates convergence while mitigating instability caused by heterogeneous, non-IID client data. We compare FOFedAvg against a broad set of established federated optimization algorithms on benchmark datasets including MNIST, FEMNIST, CIFAR-10, CIFAR-100, EMNIST, the Cleveland heart disease dataset, Sent140, PneumoniaMNIST, and Edge-IIoTset. Across a range of non-IID partitioning schemes, FOFedAvg is competitive with, and often outperforms, these baselines in terms of test performance and convergence speed. On the theoretical side, we prove that FOFedAvg converges to a stationary point under standard smoothness and bounded-variance assumptions for fractional order $0<α\le 1$. Together, these results show that fractional-order, memory-aware updates can substantially improve the robustness and effectiveness of federated learning, offering a practical path toward distributed training on heterogeneous data.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing
- **Authors:** Zarif Ikram, Arad Firouzkouhi, Stephen Tu, Mahdi Soltanolkotabi, Paria Rashidinejad
- **arXiv:** [2602.15823](https://arxiv.org/abs/2602.15823v1) · [pdf](https://arxiv.org/pdf/2602.15823v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> A central challenge in large language model (LLM) editing is capability preservation: methods that successfully change targeted behavior can quietly game the editing proxy and corrupt general capabilities, producing degenerate behaviors reminiscent of proxy/reward hacking. We present CrispEdit, a scalable and principled second-order editing algorithm that treats capability preservation as an explicit constraint, unifying and generalizing several existing editing approaches. CrispEdit formulates editing as constrained optimization and enforces the constraint by projecting edit updates onto the low-curvature subspace of the capability-loss landscape. At the crux of CrispEdit is expressing capability constraint via Bregman divergence, whose quadratic form yields the Gauss-Newton Hessian exactly and even when the base model is not trained to convergence. We make this second-order procedure efficient at the LLM scale using Kronecker-factored approximate curvature (K-FAC) and a novel matrix-free projector that exploits Kronecker structure to avoid constructing massive projection matrices. Across standard model-editing benchmarks, CrispEdit achieves high edit success while keeping capability degradation below 1% on average across datasets, significantly improving over prior editors.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Latency-aware Human-in-the-Loop Reinforcement Learning for Semantic Communications
- **Authors:** Peizheng Li, Xinyi Lin, Adnan Aijaz
- **arXiv:** [2602.15640](https://arxiv.org/abs/2602.15640v1) · [pdf](https://arxiv.org/pdf/2602.15640v1)
- **Categories:** eess.SP, cs.LG

### Abstract
> Semantic communication promises task-aligned transmission but must reconcile semantic fidelity with stringent latency guarantees in immersive and safety-critical services. This paper introduces a time-constrained human-in-the-loop reinforcement learning (TC-HITL-RL) framework that embeds human feedback, semantic utility, and latency control within a semantic-aware Open radio access network (RAN) architecture. We formulate semantic adaptation driven by human feedback as a constrained Markov decision process (CMDP) whose state captures semantic quality, human preferences, queue slack, and channel dynamics, and solve it via a primal--dual proximal policy optimization algorithm with action shielding and latency-aware reward shaping. The resulting policy preserves PPO-level semantic rewards while tightening the variability of both air-interface and near-real-time RAN intelligent controller processing budgets. Simulations over point-to-multipoint links with heterogeneous deadlines show that TC-HITL-RL consistently meets per-user timing constraints, outperforms baseline schedulers in reward, and stabilizes resource consumption, providing a practical blueprint for latency-aware semantic adaptation.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Neural-POD: A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear Proper Orthogonal Decomposition
- **Authors:** Changhong Mou, Binghang Lu, Guang Lin
- **arXiv:** [2602.15632](https://arxiv.org/abs/2602.15632v1) · [pdf](https://arxiv.org/pdf/2602.15632v1)
- **Categories:** physics.comp-ph, cs.LG, math.NA

### Abstract
> The rapid development of AI for Science is often hindered by the "discretization", where learned representations remain restricted to the specific grids or resolutions used during training. We propose the Neural Proper Orthogonal Decomposition (Neural-POD), a plug-and-play neural operator framework that constructs nonlinear, orthogonal basis functions in infinite-dimensional space using neural networks. Unlike the classical Proper Orthogonal Decomposition (POD), which is limited to linear subspace approximations obtained through singular value decomposition (SVD), Neural-POD formulates basis construction as a sequence of residual minimization problems solved through neural network training. Each basis function is obtained by learning to represent the remaining structure in the data, following a process analogous to Gram--Schmidt orthogonalization. This neural formulation introduces several key advantages over classical POD: it enables optimization in arbitrary norms (e.g., $L^2$, $L^1$), learns mappings between infinite-dimensional function spaces that is resolution-invariant, generalizes effectively to unseen parameter regimes, and inherently captures nonlinear structures in complex spatiotemporal systems. The resulting basis functions are interpretable, reusable, and enabling integration into both reduced order modeling (ROM) and operator learning frameworks such as deep operator learning (DeepONet). We demonstrate the robustness of Neural-POD with different complex spatiotemporal systems, including the Burgers' and Navier-Stokes equations. We further show that Neural-POD serves as a high performance, plug-and-play bridge between classical Galerkin projection and operator learning that enables consistent integration with both projection-based reduced order models and DeepONet frameworks.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
