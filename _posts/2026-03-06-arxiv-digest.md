---
layout: post
title: "Daily arXiv Digest — 2026-03-06 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Latent Policy Steering through One-Step Flow Policies
- **Authors:** Hokyun Im, Andrey Kolobov, Jianlong Fu, Youngwoon Lee
- **arXiv:** [2603.05296](https://arxiv.org/abs/2603.05296v1) · [pdf](https://arxiv.org/pdf/2603.05296v1)
- **Categories:** cs.RO, cs.LG

### Abstract
> Offline reinforcement learning (RL) allows robots to learn from offline datasets without risky exploration. Yet, offline RL's performance often hinges on a brittle trade-off between (1) return maximization, which can push policies outside the dataset support, and (2) behavioral constraints, which typically require sensitive hyperparameter tuning. Latent steering offers a structural way to stay within the dataset support during RL, but existing offline adaptations commonly approximate action values using latent-space critics learned via indirect distillation, which can lose information and hinder convergence. We propose Latent Policy Steering (LPS), which enables high-fidelity latent policy improvement by backpropagating original-action-space Q-gradients through a differentiable one-step MeanFlow policy to update a latent-action-space actor. By eliminating proxy latent critics, LPS allows an original-action-space critic to guide end-to-end latent-space optimization, while the one-step MeanFlow policy serves as a behavior-constrained generative prior. This decoupling yields a robust method that works out-of-the-box with minimal tuning. Across OGBench and real-world robotic tasks, LPS achieves state-of-the-art performance and consistently outperforms behavioral cloning and strong latent steering baselines.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Optimization with Parametric Variational Inequality Constraints on a Moving Set
- **Authors:** Xiaojun Chen, Jin Zhang, Yixuan Zhang
- **arXiv:** [2603.05196](https://arxiv.org/abs/2603.05196v1) · [pdf](https://arxiv.org/pdf/2603.05196v1)
- **Categories:** math.OC

### Abstract
> This paper focuses on optimization problems constrained by Parametric Variational Inequalities (PVI) defined on a moving set. Unlike most existing works on mathematical programs with equilibrium constraints, the equilibrium constraints have parameters not only in the function but also in the related set. We show that the solution function of the PVI is Lipschitz continuous with respect to the upper-level decision variables and the solution set of the optimization problem is nonempty and bounded. Moreover, we prove that the metric regularity of the constraints holds automatically, which allow us to characterize stationary points without any additional assumptions. A Smoothing Implicit Gradient Algorithm (SIGA) is proposed based on the smoothing approximation of the PVI. We prove the convergence of SIGA to a stationary point of the optimization problem and numerically validate the efficiency of SIGA by portfolio management problems with real data.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) SRasP: Self-Reorientation Adversarial Style Perturbation for Cross-Domain Few-Shot Learning
- **Authors:** Wenqian Li, Pengfei Fang, Hui Xue
- **arXiv:** [2603.05135](https://arxiv.org/abs/2603.05135v1) · [pdf](https://arxiv.org/pdf/2603.05135v1)
- **Categories:** cs.CV, cs.LG

### Abstract
> Cross-Domain Few-Shot Learning (CD-FSL) aims to transfer knowledge from a seen source domain to unseen target domains, serving as a key benchmark for evaluating the robustness and transferability of models. Existing style-based perturbation methods mitigate domain shift but often suffer from gradient instability and convergence to sharp minima.To address these limitations, we propose a novel crop-global style perturbation network, termed Self-Reorientation Adversarial \underline{S}tyle \underline{P}erturbation (SRasP). Specifically, SRasP leverages global semantic guidance to identify incoherent crops, followed by reorienting and aggregating the style gradients of these crops with the global style gradients within one image. Furthermore, we propose a novel multi-objective optimization function to maximize visual discrepancy while enforcing semantic consistency among global, crop, and adversarial features. Applying the stabilized perturbations during training encourages convergence toward flatter and more transferable solutions, improving generalization to unseen domains. Extensive experiments are conducted on multiple CD-FSL benchmarks, demonstrating consistent improvements over state-of-the-art methods.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) FedBCD:Communication-Efficient Accelerated Block Coordinate Gradient Descent for Federated Learning
- **Authors:** Junkang Liu, Fanhua Shang, Yuanyuan Liu, Hongying Liu, Yuangang Li, YunXiang Gong
- **arXiv:** [2603.05116](https://arxiv.org/abs/2603.05116v1) · [pdf](https://arxiv.org/pdf/2603.05116v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Although Federated Learning has been widely studied in recent years, there are still high overhead expenses in each communication round for large-scale models such as Vision Transformer. To lower the communication complexity, we propose a novel Federated Block Coordinate Gradient Descent (FedBCGD) method for communication efficiency. The proposed method splits model parameters into several blocks, including a shared block and enables uploading a specific parameter block by each client, which can significantly reduce communication overhead. Moreover, we also develop an accelerated FedBCGD algorithm (called FedBCGD+) with client drift control and stochastic variance reduction. To the best of our knowledge, this paper is the first work on parameter block communication for training large-scale deep models. We also provide the convergence analysis for the proposed algorithms. Our theoretical results show that the communication complexities of our algorithms are a factor $1/N$ lower than those of existing methods, where $N$ is the number of parameter blocks, and they enjoy much faster convergence than their counterparts. Empirical results indicate the superiority of the proposed algorithms compared to state-of-the-art algorithms. The code is available at https://github.com/junkangLiu0/FedBCGD.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Cheap Thrills: Effective Amortized Optimization Using Inexpensive Labels
- **Authors:** Khai Nguyen, Petros Ellinas, Anvita Bhagavathula, Priya Donti
- **arXiv:** [2603.05495](https://arxiv.org/abs/2603.05495v1) · [pdf](https://arxiv.org/pdf/2603.05495v1)
- **Categories:** cs.LG, math.OC

### Abstract
> To scale the solution of optimization and simulation problems, prior work has explored machine-learning surrogates that inexpensively map problem parameters to corresponding solutions. Commonly used approaches, including supervised and self-supervised learning with either soft or hard feasibility enforcement, face inherent challenges such as reliance on expensive, high-quality labels or difficult optimization landscapes. To address their trade-offs, we propose a novel framework that first collects "cheap" imperfect labels, then performs supervised pretraining, and finally refines the model through self-supervised learning to improve overall performance. Our theoretical analysis and merit-based criterion show that labeled data need only place the model within a basin of attraction, confirming that only modest numbers of inexact labels and training epochs are required. We empirically validate our simple three-stage strategy across challenging domains, including nonconvex constrained optimization, power-grid operation, and stiff dynamical systems, and show that it yields faster convergence; improved accuracy, feasibility, and optimality; and up to 59x reductions in total offline cost.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
