---
layout: post
title: "Daily arXiv Digest — 2026-02-05 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Theory of Optimal Learning Rate Schedules and Scaling Laws for a Random Feature Model
- **Authors:** Blake Bordelon, Francesco Mori
- **arXiv:** [2602.04774](https://arxiv.org/abs/2602.04774v1) · [pdf](https://arxiv.org/pdf/2602.04774v1)
- **Categories:** cond-mat.dis-nn, cs.LG, stat.ML

### Abstract
> Setting the learning rate for a deep learning model is a critical part of successful training, yet choosing this hyperparameter is often done empirically with trial and error. In this work, we explore a solvable model of optimal learning rate schedules for a powerlaw random feature model trained with stochastic gradient descent (SGD). We consider the optimal schedule $η_T^\star(t)$ where $t$ is the current iterate and $T$ is the total training horizon. This schedule is computed both numerically and analytically (when possible) using optimal control methods. Our analysis reveals two regimes which we term the easy phase and hard phase. In the easy phase the optimal schedule is a polynomial decay $η_T^\star(t) \simeq T^{-ξ} (1-t/T)^δ$ where $ξ$ and $δ$ depend on the properties of the features and task. In the hard phase, the optimal schedule resembles warmup-stable-decay with constant (in $T$) initial learning rate and annealing performed over a vanishing (in $T$) fraction of training steps. We investigate joint optimization of learning rate and batch size, identifying a degenerate optimality condition. Our model also predicts the compute-optimal scaling laws (where model size and training steps are chosen optimally) in both easy and hard regimes. Going beyond SGD, we consider optimal schedules for the momentum $β(t)$, where speedups in the hard phase are possible. We compare our optimal schedule to various benchmarks in our task including (1) optimal constant learning rates $η_T(t) \sim T^{-ξ}$ (2) optimal power laws $η_T(t) \sim T^{-ξ} t^{-χ}$, finding that our schedule achieves better rates than either of these. Our theory suggests that learning rate transfer across training horizon depends on the structure of the model and task. We explore these ideas in simple experimental pretraining setups.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Improved Dimension Dependence for Bandit Convex Optimization with Gradient Variations
- **Authors:** Hang Yu, Yu-Hu Yan, Peng Zhao
- **arXiv:** [2602.04761](https://arxiv.org/abs/2602.04761v1) · [pdf](https://arxiv.org/pdf/2602.04761v1)
- **Categories:** cs.LG, stat.ML

### Abstract
> Gradient-variation online learning has drawn increasing attention due to its deep connections to game theory, optimization, etc. It has been studied extensively in the full-information setting, but is underexplored with bandit feedback. In this work, we focus on gradient variation in Bandit Convex Optimization (BCO) with two-point feedback. By proposing a refined analysis on the non-consecutive gradient variation, a fundamental quantity in gradient variation with bandits, we improve the dimension dependence for both convex and strongly convex functions compared with the best known results (Chiang et al., 2013). Our improved analysis for the non-consecutive gradient variation also implies other favorable problem-dependent guarantees, such as gradient-variance and small-loss regrets. Beyond the two-point setup, we demonstrate the versatility of our technique by achieving the first gradient-variation bound for one-point bandit linear optimization over hyper-rectangular domains. Finally, we validate the effectiveness of our results in more challenging tasks such as dynamic/universal regret minimization and bandit games, establishing the first gradient-variation dynamic and universal regret bounds for two-point BCO and fast convergence rates in bandit games.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Stochastic Decision Horizons for Constrained Reinforcement Learning
- **Authors:** Nikola Milosevic, Leonard Franz, Daniel Haeufle, Georg Martius, Nico Scherf, Pavel Kolev
- **arXiv:** [2602.04599](https://arxiv.org/abs/2602.04599v1) · [pdf](https://arxiv.org/pdf/2602.04599v1)
- **Categories:** cs.LG

### Abstract
> Constrained Markov decision processes (CMDPs) provide a principled model for handling constraints, such as safety and other auxiliary objectives, in reinforcement learning. The common approach of using additive-cost constraints and dual variables often hinders off-policy scalability. We propose a Control as Inference formulation based on stochastic decision horizons, where constraint violations attenuate reward contributions and shorten the effective planning horizon via state-action-dependent continuation. This yields survival-weighted objectives that remain replay-compatible for off-policy actor-critic learning. We propose two violation semantics, absorbing and virtual termination, that share the same survival-weighted return but result in distinct optimization structures that lead to SAC/MPO-style policy improvement. Experiments demonstrate improved sample efficiency and favorable return-violation trade-offs on standard benchmarks. Moreover, MPO with virtual termination (VT-MPO) scales effectively to our high-dimensional musculoskeletal Hyfydy setup.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Reinforced Attention Learning
- **Authors:** Bangzheng Li, Jianmo Ni, Chen Qu, Ian Miao, Liu Yang, Xingyu Fu, Muhao Chen, Derek Zhiyuan Cheng
- **arXiv:** [2602.04884](https://arxiv.org/abs/2602.04884v1) · [pdf](https://arxiv.org/pdf/2602.04884v1)
- **Categories:** cs.CL, cs.CV, cs.LG

### Abstract
> Post-training with Reinforcement Learning (RL) has substantially improved reasoning in Large Language Models (LLMs) via test-time scaling. However, extending this paradigm to Multimodal LLMs (MLLMs) through verbose rationales yields limited gains for perception and can even degrade performance. We propose Reinforced Attention Learning (RAL), a policy-gradient framework that directly optimizes internal attention distributions rather than output token sequences. By shifting optimization from what to generate to where to attend, RAL promotes effective information allocation and improved grounding in complex multimodal inputs. Experiments across diverse image and video benchmarks show consistent gains over GRPO and other baselines. We further introduce On-Policy Attention Distillation, demonstrating that transferring latent attention behaviors yields stronger cross-modal alignment than standard knowledge distillation. Our results position attention policies as a principled and general alternative for multimodal post-training.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Rethinking the Trust Region in LLM Reinforcement Learning
- **Authors:** Penghui Qi, Xiangxin Zhou, Zichen Liu, Tianyu Pang, Chao Du, Min Lin, Wee Sun Lee
- **arXiv:** [2602.04879](https://arxiv.org/abs/2602.04879v1) · [pdf](https://arxiv.org/pdf/2602.04879v1)
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Reinforcement learning (RL) has become a cornerstone for fine-tuning Large Language Models (LLMs), with Proximal Policy Optimization (PPO) serving as the de facto standard algorithm. Despite its ubiquity, we argue that the core ratio clipping mechanism in PPO is structurally ill-suited for the large vocabularies inherent to LLMs. PPO constrains policy updates based on the probability ratio of sampled tokens, which serves as a noisy single-sample Monte Carlo estimate of the true policy divergence. This creates a sub-optimal learning dynamic: updates to low-probability tokens are aggressively over-penalized, while potentially catastrophic shifts in high-probability tokens are under-constrained, leading to training inefficiency and instability. To address this, we propose Divergence Proximal Policy Optimization (DPPO), which substitutes heuristic clipping with a more principled constraint based on a direct estimate of policy divergence (e.g., Total Variation or KL). To avoid huge memory footprint, we introduce the efficient Binary and Top-K approximations to capture the essential divergence with negligible overhead. Extensive empirical evaluations demonstrate that DPPO achieves superior training stability and efficiency compared to existing methods, offering a more robust foundation for RL-based LLM fine-tuning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
