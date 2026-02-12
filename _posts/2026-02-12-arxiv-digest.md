---
layout: post
title: "Daily arXiv Digest — 2026-02-12 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Natural Hypergradient Descent: Algorithm Design, Convergence Analysis, and Parallel Implementation
- **Authors:** Deyi Kong, Zaiwei Chen, Shuzhong Zhang, Shancong Mou
- **arXiv:** [2602.10905](https://arxiv.org/abs/2602.10905v1) · [pdf](https://arxiv.org/pdf/2602.10905v1)
- **Categories:** cs.LG, math.OC, stat.ML

### Abstract
> In this work, we propose Natural Hypergradient Descent (NHGD), a new method for solving bilevel optimization problems. To address the computational bottleneck in hypergradient estimation--namely, the need to compute or approximate Hessian inverse--we exploit the statistical structure of the inner optimization problem and use the empirical Fisher information matrix as an asymptotically consistent surrogate for the Hessian. This design enables a parallel optimize-and-approximate framework in which the Hessian-inverse approximation is updated synchronously with the stochastic inner optimization, reusing gradient information at negligible additional cost. Our main theoretical contribution establishes high-probability error bounds and sample complexity guarantees for NHGD that match those of state-of-the-art optimize-then-approximate methods, while significantly reducing computational time overhead. Empirical evaluations on representative bilevel learning tasks further demonstrate the practical advantages of NHGD, highlighting its scalability and effectiveness in large-scale machine learning settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) SCRAPL: Scattering Transform with Random Paths for Machine Learning
- **Authors:** Christopher Mitcheltree, Vincent Lostanlen, Emmanouil Benetos, Mathieu Lagrange
- **arXiv:** [2602.11145](https://arxiv.org/abs/2602.11145v1) · [pdf](https://arxiv.org/pdf/2602.11145v1)
- **Categories:** cs.SD, cs.LG, eess.AS

### Abstract
> The Euclidean distance between wavelet scattering transform coefficients (known as paths) provides informative gradients for perceptual quality assessment of deep inverse problems in computer vision, speech, and audio processing. However, these transforms are computationally expensive when employed as differentiable loss functions for stochastic gradient descent due to their numerous paths, which significantly limits their use in neural network training. Against this problem, we propose "Scattering transform with Random Paths for machine Learning" (SCRAPL): a stochastic optimization scheme for efficient evaluation of multivariable scattering transforms. We implement SCRAPL for the joint time-frequency scattering transform (JTFS) which demodulates spectrotemporal patterns at multiple scales and rates, allowing a fine characterization of intermittent auditory textures. We apply SCRAPL to differentiable digital signal processing (DDSP), specifically, unsupervised sound matching of a granular synthesizer and the Roland TR-808 drum machine. We also propose an initialization heuristic based on importance sampling, which adapts SCRAPL to the perceptual content of the dataset, improving neural network convergence and evaluation performance. We make our code and audio samples available and provide SCRAPL as a Python package.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) PRISM: Parallel Residual Iterative Sequence Model
- **Authors:** Jie Jiang, Ke Cheng, Xin Xu, Mengyang Pang, Tianhao Lu, Jiaheng Li, Yue Liu, Yuan Wang, Jun Zhang, Huan Yu, Zhouchen Lin
- **arXiv:** [2602.10796](https://arxiv.org/abs/2602.10796v1) · [pdf](https://arxiv.org/pdf/2602.10796v1)
- **Categories:** cs.LG

### Abstract
> Generative sequence modeling faces a fundamental tension between the expressivity of Transformers and the efficiency of linear sequence models. Existing efficient architectures are theoretically bounded by shallow, single-step linear updates, while powerful iterative methods like Test-Time Training (TTT) break hardware parallelism due to state-dependent gradients. We propose PRISM (Parallel Residual Iterative Sequence Model) to resolve this tension. PRISM introduces a solver-inspired inductive bias that captures key structural properties of multi-step refinement in a parallelizable form. We employ a Write-Forget Decoupling strategy that isolates non-linearity within the injection operator. To bypass the serial dependency of explicit solvers, PRISM utilizes a two-stage proxy architecture: a short-convolution anchors the initial residual using local history energy, while a learned predictor estimates the refinement updates directly from the input. This design distills structural patterns associated with iterative correction into a parallelizable feedforward operator. Theoretically, we prove that this formulation achieves Rank-$L$ accumulation, structurally expanding the update manifold beyond the single-step Rank-$1$ bottleneck. Empirically, it achieves comparable performance to explicit optimization methods while achieving 174x higher throughput.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Asymmetric Prompt Weighting for Reinforcement Learning with Verifiable Rewards
- **Authors:** Reinhard Heckel, Mahdi Soltanolkotabi, Christos Thramboulidis
- **arXiv:** [2602.11128](https://arxiv.org/abs/2602.11128v1) · [pdf](https://arxiv.org/pdf/2602.11128v1)
- **Categories:** cs.LG

### Abstract
> Reinforcement learning with verifiable rewards has driven recent advances in LLM post-training, in particular for reasoning. Policy optimization algorithms generate a number of responses for a given prompt and then effectively weight the corresponding gradients depending on the rewards. The most popular algorithms including GRPO, DAPO, and RLOO focus on ambiguous prompts, i.e., prompts with intermediate success probability, while downgrading gradients with very easy and very hard prompts. In this paper, we consider asymmetric prompt weightings that assign higher weights to prompts with low, or even zero, empirical success probability. We find that asymmetric weighting particularly benefits from-scratch RL (as in R1-Zero), where training traverses a wide accuracy range, and less so in post-SFT RL where the model already starts at high accuracy. We also provide theory that characterizes prompt weights which minimize the time needed to raise success probability from an initial level to a target accuracy under a fixed update budget. In low-success regimes, where informative responses are rare and response cost dominates, these optimal weights become asymmetric, upweighting low success probabilities and thereby accelerating effective-time convergence.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Statistical Learning Analysis of Physics-Informed Neural Networks
- **Authors:** David A. Barajas-Solano
- **arXiv:** [2602.11097](https://arxiv.org/abs/2602.11097v1) · [pdf](https://arxiv.org/pdf/2602.11097v1)
- **Categories:** cs.LG, physics.comp-ph

### Abstract
> We study the training and performance of physics-informed learning for initial and boundary value problems (IBVP) with physics-informed neural networks (PINNs) from a statistical learning perspective. Specifically, we restrict ourselves to parameterizations with hard initial and boundary condition constraints and reformulate the problem of estimating PINN parameters as a statistical learning problem. From this perspective, the physics penalty on the IBVP residuals can be better understood not as a regularizing term bus as an infinite source of indirect data, and the learning process as fitting the PINN distribution of residuals $p(y \mid x, t, w) q(x, t) $ to the true data-generating distribution $δ(0) q(x, t)$ by minimizing the Kullback-Leibler divergence between the true and PINN distributions. Furthermore, this analysis show that physics-informed learning with PINNs is a singular learning problem, and we employ singular learning theory tools, namely the so-called Local Learning Coefficient (Lau et al., 2025) to analyze the estimates of PINN parameters obtained via stochastic optimization for a heat equation IBVP. Finally, we discuss implications of this analysis on the quantification of predictive uncertainty of PINNs and the extrapolation capacity of PINNs.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
