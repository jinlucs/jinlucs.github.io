---
layout: post
title: "Daily arXiv Digest — 2026-01-15 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) DP-FEDSOFIM: Differentially Private Federated Stochastic Optimization using Regularized Fisher Information Matrix
- **Authors:** Sidhant R. Nair, Tanmay Sen, Mrinmay Sen
- **arXiv:** [2601.09166](https://arxiv.org/abs/2601.09166v1) · [pdf](https://arxiv.org/pdf/2601.09166v1)
- **Categories:** cs.LG, cs.CR, cs.DC

### Abstract
> Differentially private federated learning (DP-FL) suffers from slow convergence under tight privacy budgets due to the overwhelming noise introduced to preserve privacy. While adaptive optimizers can accelerate convergence, existing second-order methods such as DP-FedNew require O(d^2) memory at each client to maintain local feature covariance matrices, making them impractical for high-dimensional models. We propose DP-FedSOFIM, a server-side second-order optimization framework that leverages the Fisher Information Matrix (FIM) as a natural gradient preconditioner while requiring only O(d) memory per client. By employing the Sherman-Morrison formula for efficient matrix inversion, DP-FedSOFIM achieves O(d) computational complexity per round while maintaining the convergence benefits of second-order methods. Our analysis proves that the server-side preconditioning preserves (epsilon, delta)-differential privacy through the post-processing theorem. Empirical evaluation on CIFAR-10 demonstrates that DP-FedSOFIM achieves superior test accuracy compared to first-order baselines across multiple privacy regimes.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection
- **Authors:** Ziyu Yang, Guibin Chen, Yuxin Yang, Aoxiong Zeng, Xiangquan Yang
- **arXiv:** [2601.09684](https://arxiv.org/abs/2601.09684v1) · [pdf](https://arxiv.org/pdf/2601.09684v1)
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Multi-Task Learning (MTL) combined with Low-Rank Adaptation (LoRA) has emerged as a promising direction for parameter-efficient deployment of Large Language Models (LLMs). By sharing a single adapter across multiple tasks, one can significantly reduce storage overhead. However, this approach suffers from negative transfer, where conflicting gradient updates from distinct tasks degrade the performance of individual tasks compared to single-task fine-tuning. This problem is exacerbated in LoRA due to the low-rank constraint, which limits the optimization landscape's capacity to accommodate diverse task requirements. In this paper, we propose Ortho-LoRA, a gradient projection method specifically tailored for the bipartite structure of LoRA. Ortho-LoRA dynamically projects conflicting task gradients onto the orthogonal complement of each other within the intrinsic LoRA subspace. Extensive experiments on the GLUE benchmark demonstrate that Ortho-LoRA effectively mitigates task interference, outperforming standard joint training and recovering 95\% of the performance gap between multi-task and single-task baselines with negligible computational overhead.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Deep Operator Networks for Surrogate Modeling of Cyclic Adsorption Processes with Varying Initial Conditions
- **Authors:** Beatrice Ceccanti, Mattia Galanti, Ivo Roghair, Martin van Sint Annaland
- **arXiv:** [2601.09491](https://arxiv.org/abs/2601.09491v1) · [pdf](https://arxiv.org/pdf/2601.09491v1)
- **Categories:** cs.LG

### Abstract
> Deep Operator Networks are emerging as fundamental tools among various neural network types to learn mappings between function spaces, and have recently gained attention due to their ability to approximate nonlinear operators. In particular, DeepONets offer a natural formulation for PDE solving, since the solution of a partial differential equation can be interpreted as an operator mapping an initial condition to its corresponding solution field. In this work, we applied DeepONets in the context of process modeling for adsorption technologies, to assess their feasibility as surrogates for cyclic adsorption process simulation and optimization. The goal is to accelerate convergence of cyclic processes such as Temperature-Vacuum Swing Adsorption (TVSA), which require repeated solution of transient PDEs, which are computationally expensive. Since each step of a cyclic adsorption process starts from the final state of the preceding step, effective surrogate modeling requires generalization across a wide range of initial conditions. The governing equations exhibit steep traveling fronts, providing a demanding benchmark for operator learning. To evaluate functional generalization under these conditions, we construct a mixed training dataset composed of heterogeneous initial conditions and train DeepONets to approximate the corresponding solution operators. The trained models are then tested on initial conditions outside the parameter ranges used during training, as well as on completely unseen functional forms. The results demonstrate accurate predictions both within and beyond the training distribution, highlighting DeepONets as potential efficient surrogates for accelerating cyclic adsorption simulations and optimization workflows.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) BalDRO: A Distributionally Robust Optimization based Framework for Large Language Model Unlearning
- **Authors:** Pengyang Shao, Naixin Zhai, Lei Chen, Yonghui Yang, Fengbin Zhu, Xun Yang, Meng Wang
- **arXiv:** [2601.09172](https://arxiv.org/abs/2601.09172v1) · [pdf](https://arxiv.org/pdf/2601.09172v1)
- **Categories:** cs.LG

### Abstract
> As Large Language Models (LLMs) increasingly shape online content, removing targeted information from well-trained LLMs (also known as LLM unlearning) has become critical for web governance. A key challenge lies in sample-wise imbalance within the forget set: different samples exhibit widely varying unlearning difficulty, leading to asynchronous forgetting where some knowledge remains insufficiently erased while others become over-forgotten. To address this, we propose BalDRO, a novel and efficient framework for balanced LLM unlearning. BalDRO formulates unlearning as a min-sup process: an inner step identifies a worst-case data distribution that emphasizes hard-to-unlearn samples, while an outer step updates model parameters under this distribution. We instantiate BalDRO via two efficient variants: BalDRO-G, a discrete GroupDRO-based approximation focusing on high-loss subsets, and BalDRO-DV, a continuous Donsker-Varadhan dual method enabling smooth adaptive weighting within standard training pipelines. Experiments on TOFU and MUSE show that BalDRO significantly improves both forgetting quality and model utility over existing methods, and we release code for reproducibility.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) From Prompt to Protocol: Fast Charging Batteries with Large Language Models
- **Authors:** Ge Lei, Ferran Brosa Planella, Sterling G. Baird, Samuel J. Cooper
- **arXiv:** [2601.09626](https://arxiv.org/abs/2601.09626v1) · [pdf](https://arxiv.org/pdf/2601.09626v1)
- **Categories:** cs.LG, cs.AI, eess.SY

### Abstract
> Efficiently optimizing battery charging protocols is challenging because each evaluation is slow, costly, and non-differentiable. Many existing approaches address this difficulty by heavily constraining the protocol search space, which limits the diversity of protocols that can be explored, preventing the discovery of higher-performing solutions. We introduce two gradient-free, LLM-driven closed-loop methods: Prompt-to-Optimizer (P2O), which uses an LLM to propose the code for small neural-network-based protocols, which are then trained by an inner loop, and Prompt-to-Protocol (P2P), which simply writes an explicit function for the current and its scalar parameters. Across our case studies, LLM-guided P2O outperforms neural networks designed by Bayesian optimization, evolutionary algorithms, and random search. In a realistic fast charging scenario, both P2O and P2P yield around a 4.2 percent improvement in state of health (capacity retention based health metric under fast charging cycling) over a state-of-the-art multi-step constant current (CC) baseline, with P2P achieving this under matched evaluation budgets (same number of protocol evaluations). These results demonstrate that LLMs can expand the space of protocol functional forms, incorporate language-based constraints, and enable efficient optimization in high cost experimental settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
