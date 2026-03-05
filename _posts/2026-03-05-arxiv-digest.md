---
layout: post
title: "Daily arXiv Digest — 2026-03-05 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) When to restart? Exploring escalating restarts on convergence
- **Authors:** Ayush K. Varshney, Šarūnas Girdzijauskas, Konstantinos Vandikas, Aneta Vulgarakis Feljan
- **arXiv:** [2603.04117](https://arxiv.org/abs/2603.04117v1) · [pdf](https://arxiv.org/pdf/2603.04117v1)
- **Categories:** cs.LG

### Abstract
> Learning rate scheduling plays a critical role in the optimization of deep neural networks, directly influencing convergence speed, stability, and generalization. While existing schedulers such as cosine annealing, cyclical learning rates, and warm restarts have shown promise, they often rely on fixed or periodic triggers that are agnostic to the training dynamics, such as stagnation or convergence behavior. In this work, we propose a simple yet effective strategy, which we call Stochastic Gradient Descent with Escalating Restarts (SGD-ER). It adaptively increases the learning rate upon convergence. Our method monitors training progress and triggers restarts when stagnation is detected, linearly escalating the learning rate to escape sharp local minima and explore flatter regions of the loss landscape. We evaluate SGD-ER across CIFAR-10, CIFAR-100, and TinyImageNet on a range of architectures including ResNet-18/34/50, VGG-16, and DenseNet-101. Compared to standard schedulers, SGD-ER improves test accuracy by 0.5-4.5%, demonstrating the benefit of convergence-aware escalating restarts for better local optima.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) An Adaptive KKT-Based Indicator for Convergence Assessment in Multi-Objective Optimization
- **Authors:** Thiago Santos, Sebastiao Xavier
- **arXiv:** [2603.04053](https://arxiv.org/abs/2603.04053v1) · [pdf](https://arxiv.org/pdf/2603.04053v1)
- **Categories:** math.OC, cs.NE

### Abstract
> Performance indicators are essential tools for assessing the convergence behavior of multi-objective optimization algorithms, particularly when the true Pareto front is unknown or difficult to approximate. Classical reference-based metrics such as hypervolume and inverted generational distance are widely used, but may suffer from scalability limitations and sensitivity to parameter choices in many-objective scenarios. Indicators derived from Karush--Kuhn--Tucker (KKT) optimality conditions provide an intrinsic alternative by quantifying stationarity without relying on external reference sets. This paper revisits an entropy-inspired KKT-based convergence indicator and proposes a robust adaptive reformulation based on quantile normalization. The proposed indicator preserves the stationarity-based interpretation of the original formulation while improving robustness to heterogeneous distributions of stationarity residuals, a recurring issue in many-objective optimization.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) PTOPOFL: Privacy-Preserving Personalised Federated Learning via Persistent Homology
- **Authors:** Kelly L Vomo-Donfack, Adryel Hoszu, Grégory Ginot, Ian Morilla
- **arXiv:** [2603.04323](https://arxiv.org/abs/2603.04323v1) · [pdf](https://arxiv.org/pdf/2603.04323v1)
- **Categories:** cs.LG, cs.CR, cs.DC, math.AT, stat.ML

### Abstract
> Federated learning (FL) faces two structural tensions: gradient sharing enables data-reconstruction attacks, while non-IID client distributions degrade aggregation quality. We introduce PTOPOFL, a framework that addresses both challenges simultaneously by replacing gradient communication with topological descriptors derived from persistent homology (PH). Clients transmit only 48-dimensional PH feature vectors-compact shape summaries whose many-to-one structure makes inversion provably ill-posed-rather than model gradients. The server performs topology-guided personalised aggregation: clients are clustered by Wasserstein similarity between their PH diagrams, intra-cluster models are topology-weighted,and clusters are blended with a global consensus. We prove an information-contraction theorem showing that PH descriptors leak strictly less mutual information per sample than gradients under strongly convex loss functions, and we establish linear convergence of the Wasserstein-weighted aggregation scheme with an error floor strictly smaller than FedAvg. Evaluated against FedAvg, FedProx, SCAFFOLD, and pFedMe on a non-IID healthcare scenario (8 hospitals, 2 adversarial) and a pathological benchmark (10 clients), PTOPOFL achieves AUC 0.841 and 0.910 respectively-the highest in both settings-while reducing reconstruction risk by a factor of 4.5 relative to gradient sharing. Code is publicly available at https://github.com/MorillaLab/TopoFederatedL and data at https://doi.org/10.5281/zenodo.18827595.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization
- **Authors:** Haodong Zhu, Yangyang Ren, Yanjing Li, Mingbao Lin, Linlin Yang, Xuhui Liu, Xiantong Zhen, Haiguang Liu, Baochang Zhang
- **arXiv:** [2603.04135](https://arxiv.org/abs/2603.04135v1) · [pdf](https://arxiv.org/pdf/2603.04135v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Group Relative Policy Optimization (GRPO) effectively scales LLM reasoning but incurs prohibitive computational costs due to its extensive group-based sampling requirement. While recent selective data utilization methods can mitigate this overhead, they could induce estimation bias by altering the underlying sampling distribution, compromising theoretical rigor and convergence behavior. To address this limitation, we propose Dynamic Pruning Policy Optimization (DPPO), a framework that enables dynamic pruning while preserving unbiased gradient estimation through importance sampling-based correction. By incorporating mathematically derived rescaling factors, DPPO significantly accelerates GRPO training without altering the optimization objective of the full-batch baseline. Furthermore, to mitigate the data sparsity induced by pruning, we introduce Dense Prompt Packing, a window-based greedy strategy that maximizes valid token density and hardware utilization. Extensive experiments demonstrate that DPPO consistently accelerates training across diverse models and benchmarks. For instance, on Qwen3-4B trained on MATH, DPPO achieves 2.37$\times$ training speedup and outperforms GRPO by 3.36% in average accuracy across six mathematical reasoning benchmarks.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Robustness of Agentic AI Systems via Adversarially-Aligned Jacobian Regularization
- **Authors:** Furkan Mumcu, Yasin Yilmaz
- **arXiv:** [2603.04378](https://arxiv.org/abs/2603.04378v1) · [pdf](https://arxiv.org/pdf/2603.04378v1)
- **Categories:** cs.LG, cs.AI, cs.CR, cs.MA

### Abstract
> As Large Language Models (LLMs) transition into autonomous multi-agent ecosystems, robust minimax training becomes essential yet remains prone to instability when highly non-linear policies induce extreme local curvature in the inner maximization. Standard remedies that enforce global Jacobian bounds are overly conservative, suppressing sensitivity in all directions and inducing a large Price of Robustness. We introduce Adversarially-Aligned Jacobian Regularization (AAJR), a trajectory-aligned approach that controls sensitivity strictly along adversarial ascent directions. We prove that AAJR yields a strictly larger admissible policy class than global constraints under mild conditions, implying a weakly smaller approximation gap and reduced nominal performance degradation. Furthermore, we derive step-size conditions under which AAJR controls effective smoothness along optimization trajectories and ensures inner-loop stability. These results provide a structural theory for agentic robustness that decouples minimax stability from global expressivity restrictions.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
