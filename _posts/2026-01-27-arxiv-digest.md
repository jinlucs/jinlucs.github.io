---
layout: post
title: "Daily arXiv Digest — 2026-01-27 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Rank-1 Approximation of Inverse Fisher for Natural Policy Gradients in Deep Reinforcement Learning
- **Authors:** Yingxiao Huo, Satya Prakash Dash, Radu Stoican, Samuel Kaski, Mingfei Sun
- **arXiv:** [2601.18626](https://arxiv.org/abs/2601.18626v1) · [pdf](https://arxiv.org/pdf/2601.18626v1)
- **Categories:** cs.LG, cs.AI, stat.ML

### Abstract
> Natural gradients have long been studied in deep reinforcement learning due to their fast convergence properties and covariant weight updates. However, computing natural gradients requires inversion of the Fisher Information Matrix (FIM) at each iteration, which is computationally prohibitive in nature. In this paper, we present an efficient and scalable natural policy optimization technique that leverages a rank-1 approximation to full inverse-FIM. We theoretically show that under certain conditions, a rank-1 approximation to inverse-FIM converges faster than policy gradients and, under some conditions, enjoys the same sample complexity as stochastic policy gradient methods. We benchmark our method on a diverse set of environments and show that it achieves superior performance to standard actor-critic and trust-region baselines.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Gradient Regularized Natural Gradients
- **Authors:** Satya Prakash Dash, Hossein Abdi, Wei Pan, Samuel Kaski, Mingfei Sun
- **arXiv:** [2601.18420](https://arxiv.org/abs/2601.18420v1) · [pdf](https://arxiv.org/pdf/2601.18420v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Gradient regularization (GR) has been shown to improve the generalizability of trained models. While Natural Gradient Descent has been shown to accelerate optimization in the initial phase of training, little attention has been paid to how the training dynamics of second-order optimizers can benefit from GR. In this work, we propose Gradient-Regularized Natural Gradients (GRNG), a family of scalable second-order optimizers that integrate explicit gradient regularization with natural gradient updates. Our framework provides two complementary algorithms: a frequentist variant that avoids explicit inversion of the Fisher Information Matrix (FIM) via structured approximations, and a Bayesian variant based on a Regularized-Kalman formulation that eliminates the need for FIM inversion entirely. We establish convergence guarantees for GRNG, showing that gradient regularization improves stability and enables convergence to global minima. Empirically, we demonstrate that GRNG consistently enhances both optimization speed and generalization compared to first-order methods (SGD, AdamW) and second-order baselines (K-FAC, Sophia), with strong results on vision and language benchmarks. Our findings highlight gradient regularization as a principled and practical tool to unlock the robustness of natural gradient methods for large-scale deep learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) A Unique Inverse Decomposition of Positive Definite Matrices under Linear Constraints
- **Authors:** Yan Dolinsky, Or Zuk
- **arXiv:** [2601.18662](https://arxiv.org/abs/2601.18662v1) · [pdf](https://arxiv.org/pdf/2601.18662v1)
- **Categories:** math.OC, math.NA

### Abstract
> We study a nonlinear decomposition of a positive definite matrix into two components: the inverse of another positive definite matrix and a symmetric matrix constrained to lie in a prescribed linear subspace. Equivalently, the inverse component is required to belong to the orthogonal complement of that subspace with respect to the trace inner product. Under a sharp nondegeneracy condition on the subspace, we show that every positive definite matrix admits a \emph{unique} decomposition of this form. This decomposition admits a variational characterization as the unique minimizer of a strictly convex log-determinant optimization problem, which in turn yields a natural dual formulation that can be efficiently exploited computationally. We derive several properties, including the stability of the decomposition. We further develop feasibility-preserving Newton-type algorithms with provable convergence guarantees and analyze their per-iteration complexity in terms of algebraic properties of the decomposed matrix and the underlying subspace. Finally, we show that the proposed decomposition arises naturally in exponential utility maximization, a central problem in mathematical finance.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Stability as a Liability:Systematic Breakdown of Linguistic Structure in LLMs
- **Authors:** Xianzhe Meng, Qiangsheng Zeng, Ling Luo, Qinghan Yang, Jiarui Hao, Wenbo Wu, Qinyu Wang, Rui Yin, Lin Qi, Renzhi Lu
- **arXiv:** [2601.18588](https://arxiv.org/abs/2601.18588v1) · [pdf](https://arxiv.org/pdf/2601.18588v1)
- **Categories:** cs.AI, cs.CL, cs.LG

### Abstract
> Training stability is typically regarded as a prerequisite for reliable optimization in large language models. In this work, we analyze how stabilizing training dynamics affects the induced generation distribution. We show that under standard maximum likelihood training, stable parameter trajectories lead stationary solutions to approximately minimize the forward KL divergence to the empirical distribution, while implicitly reducing generative entropy. As a consequence, the learned model can concentrate probability mass on a limited subset of empirical modes, exhibiting systematic degeneration despite smooth loss convergence. We empirically validate this effect using a controlled feedback-based training framework that stabilizes internal generation statistics, observing consistent low-entropy outputs and repetitive behavior across architectures and random seeds. It indicates that optimization stability and generative expressivity are not inherently aligned, and that stability alone is an insufficient indicator of generative quality.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Reuse your FLOPs: Scaling RL on Hard Problems by Conditioning on Very Off-Policy Prefixes
- **Authors:** Amrith Setlur, Zijian Wang, Andrew Cohen, Paria Rashidinejad, Sang Michael Xie
- **arXiv:** [2601.18795](https://arxiv.org/abs/2601.18795v1) · [pdf](https://arxiv.org/pdf/2601.18795v1)
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Typical reinforcement learning (RL) methods for LLM reasoning waste compute on hard problems, where correct on-policy traces are rare, policy gradients vanish, and learning stalls. To bootstrap more efficient RL, we consider reusing old sampling FLOPs (from prior inference or RL training) in the form of off-policy traces. Standard off-policy methods supervise against off-policy data, causing instabilities during RL optimization. We introduce PrefixRL, where we condition on the prefix of successful off-policy traces and run on-policy RL to complete them, side-stepping off-policy instabilities. PrefixRL boosts the learning signal on hard problems by modulating the difficulty of the problem through the off-policy prefix length. We prove that the PrefixRL objective is not only consistent with the standard RL objective but also more sample efficient. Empirically, we discover back-generalization: training only on prefixed problems generalizes to out-of-distribution unprefixed performance, with learned strategies often differing from those in the prefix. In our experiments, we source the off-policy traces by rejection sampling with the base model, creating a self-improvement loop. On hard reasoning problems, PrefixRL reaches the same training reward 2x faster than the strongest baseline (SFT on off-policy data then RL), even after accounting for the compute spent on the initial rejection sampling, and increases the final reward by 3x. The gains transfer to held-out benchmarks, and PrefixRL is still effective when off-policy traces are derived from a different model family, validating its flexibility in practical settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
