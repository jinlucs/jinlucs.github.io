---
layout: post
title: "Daily arXiv Digest — 2025-12-23 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Mean-field optimal control with stochastic leaders
- **Authors:** Sebastian Zimper, Ana Djurdjevac, Carsten Hartmann, Christof Schütte, Nataša Djurdjevac Conrad
- **arXiv:** [2512.19201](https://arxiv.org/abs/2512.19201v1) · [pdf](https://arxiv.org/pdf/2512.19201v1)
- **Categories:** math.OC, math.PR

### Abstract
> We consider interacting agent systems with a large number of stochastic agents (or particles) influenced by a fixed number of external stochastic lead agents. Such examples arise, for example in models of opinion dynamics, where a small number of leaders (influencers) can steer the behaviour of a large population of followers. In this context, we study a partial mean-field limit where the number of followers tends to infinity, while the number of leaders stays constant. The partial mean-field limit dynamics is then given by a McKean-Vlasov stochastic differential equation (SDE) for the followers, coupled to a controlled Itô-SDE governing the dynamics of the lead agents. For a given cost functional that the lead agents seek to minimise, we show that the unique optimal control of the finite agent system convergences to the optimal control of the limiting system. This establishes that the low-dimensional control of the partial (mean-field) system provides an effective approximation for controlling the high-dimensional finite agent system. In addition, we propose a stochastic gradient descent algorithm that can efficiently approximate the mean-field control. Our theoretical results are illustrated on opinion dynamics model with lead agents, where the control objective is to drive the followers to reach consensus in finite time.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies
- **Authors:** Yuqiao Tan, Minzheng Wang, Shizhu He, Huanxuan Liao, Chengfeng Zhao, Qiunan Lu, Tian Liang, Jun Zhao, Kang Liu
- **arXiv:** [2512.19673](https://arxiv.org/abs/2512.19673v1) · [pdf](https://arxiv.org/pdf/2512.19673v1)
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Existing reinforcement learning (RL) approaches treat large language models (LLMs) as a single unified policy, overlooking their internal mechanisms. Understanding how policy evolves across layers and modules is therefore crucial for enabling more targeted optimization and raveling out complex reasoning mechanisms. In this paper, we decompose the language model policy by leveraging the intrinsic split of the Transformer residual stream and the equivalence between the composition of hidden states with the unembedding matrix and the resulting samplable policy. This decomposition reveals Internal Layer Policies, corresponding to contributions from individual layers, and Internal Modular Policies, which align with the self-attention and feed-forward network (FFN) components within each layer. By analyzing the entropy of internal policy, we find that: (a) Early layers keep high entropy for exploration, top layers converge to near-zero entropy for refinement, with convergence patterns varying across model series. (b) LLama's prediction space rapidly converges in the final layer, whereas Qwen-series models, especially Qwen3, exhibit a more human-like, progressively structured reasoning pattern. Motivated by these findings, we propose Bottom-up Policy Optimization (BuPO), a novel RL paradigm that directly optimizes the internal layer policy during early training. By aligning training objective at lower layer, BuPO reconstructs foundational reasoning capabilities and achieves superior performance. Extensive experiments on complex reasoning benchmarks demonstrates the effectiveness of our method. Our code is available at https://github.com/Trae1ounG/BuPO.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Deep Legendre Transform
- **Authors:** Aleksey Minabutdinov, Patrick Cheridito
- **arXiv:** [2512.19649](https://arxiv.org/abs/2512.19649v1) · [pdf](https://arxiv.org/pdf/2512.19649v1)
- **Categories:** cs.LG, math.OC

### Abstract
> We introduce a novel deep learning algorithm for computing convex conjugates of differentiable convex functions, a fundamental operation in convex analysis with various applications in different fields such as optimization, control theory, physics and economics. While traditional numerical methods suffer from the curse of dimensionality and become computationally intractable in high dimensions, more recent neural network-based approaches scale better, but have mostly been studied with the aim of solving optimal transport problems and require the solution of complicated optimization or max-min problems. Using an implicit Fenchel formulation of convex conjugation, our approach facilitates an efficient gradient-based framework for the minimization of approximation errors and, as a byproduct, also provides a posteriori error estimates for the approximation quality. Numerical experiments demonstrate our method's ability to deliver accurate results across different high-dimensional examples. Moreover, by employing symbolic regression with Kolmogorov--Arnold networks, it is able to obtain the exact convex conjugates of specific convex functions.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) A perturbed preconditioned gradient descent method for the unconstrained minimization of composite objectives
- **Authors:** Jea-Hyun Park, Abner J. Salgado, Steven M. Wise
- **arXiv:** [2512.19532](https://arxiv.org/abs/2512.19532v1) · [pdf](https://arxiv.org/pdf/2512.19532v1)
- **Categories:** math.OC, math.NA

### Abstract
> We introduce a perturbed preconditioned gradient descent (PPGD) method for the unconstrained minimization of a strongly convex objective $G$ with a locally Lipschitz continuous gradient. We assume that $G(v)=E(v)+F(v)$ and that the gradient of $F$ is only known approximately. Our analysis is conducted in infinite dimensions with a preconditioner built into the framework. We prove a linear rate of convergence, up to an error term dependent on the gradient approximation. We apply the PPGD to the stationary Cahn-Hilliard equations with variable mobility under periodic boundary conditions. Numerical experiments are presented to validate the theoretical convergence rates and explore how the mobility affects the computation.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Binary Kernel Logistic Regression: a sparsity-inducing formulation and a convergent decomposition training algorithm
- **Authors:** Antonio Consolo, Andrea Manno, Edoardo Amaldi
- **arXiv:** [2512.19440](https://arxiv.org/abs/2512.19440v1) · [pdf](https://arxiv.org/pdf/2512.19440v1)
- **Categories:** cs.LG, math.OC

### Abstract
> Kernel logistic regression (KLR) is a widely used supervised learning method for binary and multi-class classification, which provides estimates of the conditional probabilities of class membership for the data points. Unlike other kernel methods such as Support Vector Machines (SVMs), KLRs are generally not sparse. Previous attempts to deal with sparsity in KLR include a heuristic method referred to as the Import Vector Machine (IVM) and ad hoc regularizations such as the $\ell_{1/2}$-based one. Achieving a good trade-off between prediction accuracy and sparsity is still a challenging issue with a potential significant impact from the application point of view. In this work, we revisit binary KLR and propose an extension of the training formulation proposed by Keerthi et al., which is able to induce sparsity in the trained model, while maintaining good testing accuracy. To efficiently solve the dual of this formulation, we devise a decomposition algorithm of Sequential Minimal Optimization type which exploits second-order information, and for which we establish global convergence. Numerical experiments conducted on 12 datasets from the literature show that the proposed binary KLR approach achieves a competitive trade-off between accuracy and sparsity with respect to IVM, $\ell_{1/2}$-based regularization for KLR, and SVM while retaining the advantages of providing informative estimates of the class membership probabilities.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
