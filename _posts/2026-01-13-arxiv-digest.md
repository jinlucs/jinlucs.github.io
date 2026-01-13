---
layout: post
title: "Daily arXiv Digest — 2026-01-13 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Self-Creating Random Walks for Decentralized Learning under Pac-Man Attacks
- **Authors:** Xingran Chen, Parimal Parag, Rohit Bhagat, Salim El Rouayheb
- **arXiv:** [2601.07674](https://arxiv.org/abs/2601.07674v1) · [pdf](https://arxiv.org/pdf/2601.07674v1)
- **Categories:** cs.MA, cs.LG

### Abstract
> Random walk (RW)-based algorithms have long been popular in distributed systems due to low overheads and scalability, with recent growing applications in decentralized learning. However, their reliance on local interactions makes them inherently vulnerable to malicious behavior. In this work, we investigate an adversarial threat that we term the ``Pac-Man'' attack, in which a malicious node probabilistically terminates any RW that visits it. This stealthy behavior gradually eliminates active RWs from the network, effectively halting the learning process without triggering failure alarms. To counter this threat, we propose the CREATE-IF-LATE (CIL) algorithm, which is a fully decentralized, resilient mechanism that enables self-creating RWs and prevents RW extinction in the presence of Pac-Man. Our theoretical analysis shows that the CIL algorithm guarantees several desirable properties, such as (i) non-extinction of the RW population, (ii) almost sure boundedness of the RW population, and (iii) convergence of RW-based stochastic gradient descent even in the presence of Pac-Man with a quantifiable deviation from the true optimum. Moreover, the learning process experiences at most a linear time delay due to Pac-Man interruptions and RW regeneration. Our extensive empirical results on both synthetic and public benchmark datasets validate our theoretical findings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Data-Driven Stochastic VRP: Integration of Forecast Duration into Optimization for Utility Workforce Management
- **Authors:** Matteo Garbelli
- **arXiv:** [2601.07514](https://arxiv.org/abs/2601.07514v1) · [pdf](https://arxiv.org/pdf/2601.07514v1)
- **Categories:** math.OC, cs.AI

### Abstract
> This paper investigates the integration of machine learning forecasts of intervention durations into a stochastic variant of the Capacitated Vehicle Routing Problem with Time Windows (CVRPTW). In particular, we exploit tree-based gradient boosting (XGBoost) trained on eight years of gas meter maintenance data to produce point predictions and uncertainty estimates, which then drive a multi-objective evolutionary optimization routine. The methodology addresses uncertainty through sub-Gaussian concentration bounds for route-level risk buffers and explicitly accounts for competing operational KPIs through a multi-objective formulation. Empirical analysis of prediction residuals validates the sub-Gaussian assumption underlying the risk model. From an empirical point of view, our results report improvements around 20-25\% in operator utilization and completion rates compared with plans computed using default durations. The integration of uncertainty quantification and risk-aware optimization provides a practical framework for handling stochastic service durations in real-world routing applications.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning
- **Authors:** Ziheng Li, Liu Kang, Feng Xiao, Luxi Xing, Qingyi Si, Zhuoran Li, Weikang Gong, Deqing Yang, Yanghua Xiao, Hongcheng Guo
- **arXiv:** [2601.07408](https://arxiv.org/abs/2601.07408v1) · [pdf](https://arxiv.org/pdf/2601.07408v1)
- **Categories:** cs.CL, cs.LG

### Abstract
> Group Relative Policy Optimization (GRPO) has emerged as a promising critic-free reinforcement learning paradigm for reasoning tasks. However, standard GRPO employs a coarse-grained credit assignment mechanism that propagates group-level rewards uniformly to to every token in a sequence, neglecting the varying contribution of individual reasoning steps. We address this limitation by introducing Outcome-grounded Advantage Reshaping (OAR), a fine-grained credit assignment mechanism that redistributes advantages based on how much each token influences the model's final answer. We instantiate OAR via two complementary strategies: (1) OAR-P, which estimates outcome sensitivity through counterfactual token perturbations, serving as a high-fidelity attribution signal; (2) OAR-G, which uses an input-gradient sensitivity proxy to approximate the influence signal with a single backward pass. These importance signals are integrated with a conservative Bi-Level advantage reshaping scheme that suppresses low-impact tokens and boosts pivotal ones while preserving the overall advantage mass. Empirical results on extensive mathematical reasoning benchmarks demonstrate that while OAR-P sets the performance upper bound, OAR-G achieves comparable gains with negligible computational overhead, both significantly outperforming a strong GRPO baseline, pushing the boundaries of critic-free LLM reasoning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Backward Reconstruction of the Chafee--Infante Equation via Physics-Informed WGAN-GP
- **Authors:** Joseph L. Shomberg
- **arXiv:** [2601.07733](https://arxiv.org/abs/2601.07733v1) · [pdf](https://arxiv.org/pdf/2601.07733v1)
- **Categories:** math.AP, cs.LG

### Abstract
> We present a physics-informed Wasserstein GAN with gradient penalty (WGAN-GP) for solving the inverse Chafee--Infante problem on two-dimensional domains with Dirichlet boundary conditions. The objective is to reconstruct an unknown initial condition from a near-equilibrium state obtained after 100 explicit forward Euler iterations of the reaction-diffusion equation \[ u_t - γΔu + κ\left(u^3 - u\right)=0. \] Because this mapping strongly damps high-frequency content, the inverse problem is severely ill-posed and sensitive to noise. Our approach integrates a U-Net generator, a PatchGAN critic with spectral normalization, Wasserstein loss with gradient penalty, and several physics-informed auxiliary terms, including Lyapunov energy matching, distributional statistics, and a crucial forward-simulation penalty. This penalty enforces consistency between the predicted initial condition and its forward evolution under the \emph{same} forward Euler discretization used for dataset generation. Earlier experiments employing an Eyre-type semi-implicit solver were not compatible with this residual mechanism due to the cost and instability of Newton iterations within batched GPU training. On a dataset of 50k training and 10k testing pairs on $128\times128$ grids (with natural $[-1,1]$ amplitude scaling), the best trained model attains a mean absolute error (MAE) of approximately \textbf{0.23988159} on the full test set, with a sample-wise standard deviation of about \textbf{0.00266345}. The results demonstrate stable inversion, accurate recovery of interfacial structure, and robustness to high-frequency noise in the initial data.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Dual-Level Models for Physics-Informed Multi-Step Time Series Forecasting
- **Authors:** Mahdi Nasiri, Johanna Kortelainen, Simo Särkkä
- **arXiv:** [2601.07640](https://arxiv.org/abs/2601.07640v1) · [pdf](https://arxiv.org/pdf/2601.07640v1)
- **Categories:** stat.ML, cs.LG

### Abstract
> This paper develops an approach for multi-step forecasting of dynamical systems by integrating probabilistic input forecasting with physics-informed output prediction. Accurate multi-step forecasting of time series systems is important for the automatic control and optimization of physical processes, enabling more precise decision-making. While mechanistic-based and data-driven machine learning (ML) approaches have been employed for time series forecasting, they face significant limitations. Incomplete knowledge of process mathematical models limits mechanistic-based direct employment, while purely data-driven ML models struggle with dynamic environments, leading to poor generalization. To address these limitations, this paper proposes a dual-level strategy for physics-informed forecasting of dynamical systems. On the first level, input variables are forecast using a hybrid method that integrates a long short-term memory (LSTM) network into probabilistic state transition models (STMs). On the second level, these stochastically predicted inputs are sequentially fed into a physics-informed neural network (PINN) to generate multi-step output predictions. The experimental results of the paper demonstrate that the hybrid input forecasting models achieve a higher log-likelihood and lower mean squared errors (MSE) compared to conventional STMs. Furthermore, the PINNs driven by the input forecasting models outperform their purely data-driven counterparts in terms of MSE and log-likelihood, exhibiting stronger generalization and forecasting performance across multiple test cases.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
