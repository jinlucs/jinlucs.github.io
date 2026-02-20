---
layout: post
title: "Daily arXiv Digest — 2026-02-20 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) A Theoretical Framework for Modular Learning of Robust Generative Models
- **Authors:** Corinna Cortes, Mehryar Mohri, Yutao Zhong
- **arXiv:** [2602.17554](https://arxiv.org/abs/2602.17554v1) · [pdf](https://arxiv.org/pdf/2602.17554v1)
- **Categories:** cs.LG, stat.ML

### Abstract
> Training large-scale generative models is resource-intensive and relies heavily on heuristic dataset weighting. We address two fundamental questions: Can we train Large Language Models (LLMs) modularly-combining small, domain-specific experts to match monolithic performance-and can we do so robustly for any data mixture, eliminating heuristic tuning? We present a theoretical framework for modular generative modeling where a set of pre-trained experts are combined via a gating mechanism. We define the space of normalized gating functions, $G_{1}$, and formulate the problem as a minimax game to find a single robust gate that minimizes divergence to the worst-case data mixture. We prove the existence of such a robust gate using Kakutani's fixed-point theorem and show that modularity acts as a strong regularizer, with generalization bounds scaling with the lightweight gate's complexity. Furthermore, we prove that this modular approach can theoretically outperform models retrained on aggregate data, with the gap characterized by the Jensen-Shannon Divergence. Finally, we introduce a scalable Stochastic Primal-Dual algorithm and a Structural Distillation method for efficient inference. Empirical results on synthetic and real-world datasets confirm that our modular architecture effectively mitigates gradient conflict and can robustly outperform monolithic baselines.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Variational inference via radial transport
- **Authors:** Luca Ghafourpour, Sinho Chewi, Alessio Figalli, Aram-Alexandre Pooladian
- **arXiv:** [2602.17525](https://arxiv.org/abs/2602.17525v1) · [pdf](https://arxiv.org/pdf/2602.17525v1)
- **Categories:** cs.LG, math.ST, stat.ML

### Abstract
> In variational inference (VI), the practitioner approximates a high-dimensional distribution $π$ with a simple surrogate one, often a (product) Gaussian distribution. However, in many cases of practical interest, Gaussian distributions might not capture the correct radial profile of $π$, resulting in poor coverage. In this work, we approach the VI problem from the perspective of optimizing over these radial profiles. Our algorithm radVI is a cheap, effective add-on to many existing VI schemes, such as Gaussian (mean-field) VI and Laplace approximation. We provide theoretical convergence guarantees for our algorithm, owing to recent developments in optimization over the Wasserstein space--the space of probability distributions endowed with the Wasserstein distance--and new regularity properties of radial transport maps in the style of Caffarelli (2000).

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Linear Convergence in Games with Delayed Feedback via Extra Prediction
- **Authors:** Yuma Fujimoto, Kenshi Abe, Kaito Ariu
- **arXiv:** [2602.17486](https://arxiv.org/abs/2602.17486v1) · [pdf](https://arxiv.org/pdf/2602.17486v1)
- **Categories:** cs.LG, cs.GT, cs.MA, math.OC

### Abstract
> Feedback delays are inevitable in real-world multi-agent learning. They are known to severely degrade performance, and the convergence rate under delayed feedback is still unclear, even for bilinear games. This paper derives the rate of linear convergence of Weighted Optimistic Gradient Descent-Ascent (WOGDA), which predicts future rewards with extra optimism, in unconstrained bilinear games. To analyze the algorithm, we interpret it as an approximation of the Extra Proximal Point (EPP), which is updated based on farther future rewards than the classical Proximal Point (PP). Our theorems show that standard optimism (predicting the next-step reward) achieves linear convergence to the equilibrium at a rate $\exp(-Θ(t/m^{5}))$ after $t$ iterations for delay $m$. Moreover, employing extra optimism (predicting farther future reward) tolerates a larger step size and significantly accelerates the rate to $\exp(-Θ(t/(m^{2}\log m)))$. Our experiments also show accelerated convergence driven by the extra optimism and are qualitatively consistent with our theorems. In summary, this paper validates that extra optimism is a promising countermeasure against performance degradation caused by feedback delays.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Continual uncertainty learning
- **Authors:** Heisei Yonezawa, Ansei Yonezawa, Itsuro Kajiwara
- **arXiv:** [2602.17174](https://arxiv.org/abs/2602.17174v1) · [pdf](https://arxiv.org/pdf/2602.17174v1)
- **Categories:** cs.LG, cs.AI, eess.SY

### Abstract
> Robust control of mechanical systems with multiple uncertainties remains a fundamental challenge, particularly when nonlinear dynamics and operating-condition variations are intricately intertwined. While deep reinforcement learning (DRL) combined with domain randomization has shown promise in mitigating the sim-to-real gap, simultaneously handling all sources of uncertainty often leads to sub-optimal policies and poor learning efficiency. This study formulates a new curriculum-based continual learning framework for robust control problems involving nonlinear dynamical systems in which multiple sources of uncertainty are simultaneously superimposed. The key idea is to decompose a complex control problem with multiple uncertainties into a sequence of continual learning tasks, in which strategies for handling each uncertainty are acquired sequentially. The original system is extended into a finite set of plants whose dynamic uncertainties are gradually expanded and diversified as learning progresses. The policy is stably updated across the entire plant sets associated with tasks defined by different uncertainty configurations without catastrophic forgetting. To ensure learning efficiency, we jointly incorporate a model-based controller (MBC), which guarantees a shared baseline performance across the plant sets, into the learning process to accelerate the convergence. This residual learning scheme facilitates task-specific optimization of the DRL agent for each uncertainty, thereby enhancing sample efficiency. As a practical industrial application, this study applies the proposed method to designing an active vibration controller for automotive powertrains. We verified that the resulting controller is robust against structural nonlinearities and dynamic variations, realizing successful sim-to-real transfer.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization
- **Authors:** Yicheng Lang, Changsheng Wang, Yihua Zhang, Mingyi Hong, Zheng Zhang, Wotao Yin, Sijia Liu
- **arXiv:** [2602.17155](https://arxiv.org/abs/2602.17155v1) · [pdf](https://arxiv.org/pdf/2602.17155v1)
- **Categories:** cs.LG

### Abstract
> Zeroth-order (ZO) optimization provides a gradient-free alternative to first-order (FO) methods by estimating gradients via finite differences of function evaluations, and has recently emerged as a memory-efficient paradigm for fine-tuning large-scale models by avoiding backpropagation. However, ZO optimization has a fundamental tension between accuracy and query efficiency. In this work, we show that ZO optimization can be substantially improved by unifying two complementary principles: (i) a projection-based subspace view that reduces gradient estimation variance by exploiting the intrinsic low-rank structure of model updates, and (ii) Muon-style spectral optimization that applies gradient orthogonalization to extract informative spectral structure from noisy ZO gradients. These findings form a unified framework of subspace gradient orthogonalization, which we instantiate in a new method, ZO-Muon, admitting a natural interpretation as a low-rank Muon optimizer in the ZO setting. Extensive experiments on large language models (LLMs) and vision transformers (ViTs) demonstrate that ZO-Muon significantly accelerates convergence and achieves a win-win improvement in accuracy and query/runtime efficiency. Notably, compared to the popular MeZO baseline, ZO-Muon requires only 24.7% of the queries to reach the same SST-2 performance for LLM fine-tuning, and improves accuracy by 25.1% on ViT-B fine-tuning on CIFAR-100.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
