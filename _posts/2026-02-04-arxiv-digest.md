---
layout: post
title: "Daily arXiv Digest — 2026-02-04 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) WARP Logic Neural Networks
- **Authors:** Lino Gerlach, Thore Gerlach, Liv Våge, Elliott Kauffman, Isobel Ojalvo
- **arXiv:** [2602.03527](https://arxiv.org/abs/2602.03527v1) · [pdf](https://arxiv.org/pdf/2602.03527v1)
- **Categories:** cs.LG

### Abstract
> Fast and efficient AI inference is increasingly important, and recent models that directly learn low-level logic operations have achieved state-of-the-art performance. However, existing logic neural networks incur high training costs, introduce redundancy or rely on approximate gradients, which limits scalability. To overcome these limitations, we introduce WAlsh Relaxation for Probabilistic (WARP) logic neural networks -- a novel gradient-based framework that efficiently learns combinations of hardware-native logic blocks. We show that WARP yields the most parameter-efficient representation for exactly learning Boolean functions and that several prior approaches arise as restricted special cases. Training is improved by introducing learnable thresholding and residual initialization, while we bridge the gap between relaxed training and discrete logic inference through stochastic smoothing. Experiments demonstrate faster convergence than state-of-the-art baselines, while scaling effectively to deeper architectures and logic functions with higher input arity.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Efficient Estimation of Kernel Surrogate Models for Task Attribution
- **Authors:** Zhenshuo Zhang, Minxuan Duan, Hongyang R. Zhang
- **arXiv:** [2602.03783](https://arxiv.org/abs/2602.03783v1) · [pdf](https://arxiv.org/pdf/2602.03783v1)
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Modern AI agents such as large language models are trained on diverse tasks -- translation, code generation, mathematical reasoning, and text prediction -- simultaneously. A key question is to quantify how each individual training task influences performance on a target task, a problem we refer to as task attribution. The direct approach, leave-one-out retraining, measures the effect of removing each task, but is computationally infeasible at scale. An alternative approach that builds surrogate models to predict a target task's performance for any subset of training tasks has emerged in recent literature. Prior work focuses on linear surrogate models, which capture first-order relationships, but miss nonlinear interactions such as synergy, antagonism, or XOR-type effects. In this paper, we first consider a unified task weighting framework for analyzing task attribution methods, and show a new connection between linear surrogate models and influence functions through a second-order analysis. Then, we introduce kernel surrogate models, which more effectively represent second-order task interactions. To efficiently learn the kernel surrogate, we develop a gradient-based estimation procedure that leverages a first-order approximation of pretrained models; empirically, this yields accurate estimates with less than $2\%$ relative error without repeated retraining. Experiments across multiple domains -- including math reasoning in transformers, in-context learning, and multi-objective reinforcement learning -- demonstrate the effectiveness of kernel surrogate models. They achieve a $25\%$ higher correlation with the leave-one-out ground truth than linear surrogates and influence-function baselines. When used for downstream task selection, kernel surrogate models yield a $40\%$ improvement in demonstration selection for in-context learning and multi-objective reinforcement learning benchmarks.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) VR-VFL: Joint Rate and Client Selection for Vehicular Federated Learning Under Imperfect CSI
- **Authors:** Metehan Karatas, Subhrakanti Dey, Christian Rohner, Jose Mairton Barros da Silva
- **arXiv:** [2602.03711](https://arxiv.org/abs/2602.03711v1) · [pdf](https://arxiv.org/pdf/2602.03711v1)
- **Categories:** eess.SP, cs.LG

### Abstract
> Federated learning in vehicular edge networks faces major challenges in efficient resource allocation, largely due to high vehicle mobility and the presence of imperfect channel state information. Many existing methods oversimplify these realities, often assuming fixed communication rounds or ideal channel conditions, which limits their effectiveness in real-world scenarios. To address this, we propose variable rate vehicular federated learning (VR-VFL), a novel federated learning method designed specifically for vehicular networks under imperfect channel state information. VR-VFL combines dynamic client selection with adaptive transmission rate selection, while also allowing round times to flex in response to changing wireless conditions. At its core, VR-VFL is built on a bi-objective optimization framework that strikes a balance between improving learning convergence and minimizing the time required to complete each round. By accounting for both the challenges of mobility and realistic wireless constraints, VR-VFL offers a more practical and efficient approach to federated learning in vehicular edge networks. Simulation results show that the proposed VR-VFL scheme achieves convergence approximately 40% faster than other methods in the literature.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Anytime Pretraining: Horizon-Free Learning-Rate Schedules with Weight Averaging
- **Authors:** Alexandru Meterez, Pranav Ajit Nair, Depen Morwani, Cengiz Pehlevan, Sham Kakade
- **arXiv:** [2602.03702](https://arxiv.org/abs/2602.03702v1) · [pdf](https://arxiv.org/pdf/2602.03702v1)
- **Categories:** cs.LG, cs.AI, math.OC, stat.ML

### Abstract
> Large language models are increasingly trained in continual or open-ended settings, where the total training horizon is not known in advance. Despite this, most existing pretraining recipes are not anytime: they rely on horizon-dependent learning rate schedules and extensive tuning under a fixed compute budget. In this work, we provide a theoretical analysis demonstrating the existence of anytime learning schedules for overparameterized linear regression, and we highlight the central role of weight averaging - also known as model merging - in achieving the minimax convergence rates of stochastic gradient descent. We show that these anytime schedules polynomially decay with time, with the decay rate determined by the source and capacity conditions of the problem. Empirically, we evaluate 150M and 300M parameter language models trained at 1-32x Chinchilla scale, comparing constant learning rates with weight averaging and $1/\sqrt{t}$ schedules with weight averaging against a well-tuned cosine schedule. Across the full training range, the anytime schedules achieve comparable final loss to cosine decay. Taken together, our results suggest that weight averaging combined with simple, horizon-free step sizes offers a practical and effective anytime alternative to cosine learning rate schedules for large language model pretraining.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Universal One-third Time Scaling in Learning Peaked Distributions
- **Authors:** Yizhou Liu, Ziming Liu, Cengiz Pehlevan, Jeff Gore
- **arXiv:** [2602.03685](https://arxiv.org/abs/2602.03685v1) · [pdf](https://arxiv.org/pdf/2602.03685v1)
- **Categories:** cs.LG, cs.AI, stat.ML

### Abstract
> Training large language models (LLMs) is computationally expensive, partly because the loss exhibits slow power-law convergence whose origin remains debatable. Through systematic analysis of toy models and empirical evaluation of LLMs, we show that this behavior can arise intrinsically from the use of softmax and cross-entropy. When learning peaked probability distributions, e.g., next-token distributions, these components yield power-law vanishing losses and gradients, creating a fundamental optimization bottleneck. This ultimately leads to power-law time scaling of the loss with a universal exponent of $1/3$. Our results provide a mechanistic explanation for observed neural scaling and suggest new directions for improving LLM training efficiency.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
