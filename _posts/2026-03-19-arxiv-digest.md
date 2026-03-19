---
layout: post
title: "Daily arXiv Digest — 2026-03-19 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Stochastic set-valued optimization and its application to robust learning
- **Authors:** Tommaso Giovannelli, Jingfu Tan, Luis Nunes Vicente
- **arXiv:** [2603.17691](https://arxiv.org/abs/2603.17691v1) · [pdf](https://arxiv.org/pdf/2603.17691v1)
- **Categories:** math.OC, cs.LG

### Abstract
> In this paper, we develop a stochastic set-valued optimization (SVO) framework tailored for robust machine learning. In the SVO setting, each decision variable is mapped to a set of objective values, and optimality is defined via set relations. We focus on SVO problems with hyperbox sets, which can be reformulated as multi-objective optimization (MOO) problems with finitely many objectives and serve as a foundation for representing or approximating more general mapped sets. Two special cases of hyperbox-valued optimization (HVO) are interval-valued (IVO) and rectangle-valued (RVO) optimization. We construct stochastic IVO/RVO formulations that incorporate subquantiles and superquantiles into the objective functions of the MOO reformulations, providing a new characterization for subquantiles. These formulations provide interpretable trade-offs by capturing both lower- and upper-tail behaviors of loss distributions, thereby going beyond standard empirical risk minimization and classical robust models. To solve the resulting multi-objective problems, we adopt stochastic multi-gradient algorithms and select a Pareto knee solution. In numerical experiments, the proposed algorithms with this selection strategy exhibit improved robustness and reduced variability across test replications under distributional shift compared with empirical risk minimization, while maintaining competitive accuracy.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Mirror Descent on Riemannian Manifolds
- **Authors:** Jiaxin Jiang, Lei Shi, Jiyuan Tan
- **arXiv:** [2603.17527](https://arxiv.org/abs/2603.17527v1) · [pdf](https://arxiv.org/pdf/2603.17527v1)
- **Categories:** stat.ML, cs.LG, math.OC

### Abstract
> Mirror Descent (MD) is a scalable first-order method widely used in large-scale optimization, with applications in image processing, policy optimization, and neural network training. This paper generalizes MD to optimization on Riemannian manifolds. In particular, we develop a Riemannian Mirror Descent (RMD) framework via reparameterization and further propose a stochastic variant of RMD. We also establish non-asymptotic convergence guarantees for both RMD and stochastic RMD. As an application to the Stiefel manifold, our RMD framework reduces to the Curvilinear Gradient Descent (CGD) method proposed in [26]. Moreover, when specializing the stochastic RMD framework to the Stiefel setting, we obtain a stochastic extension of CGD, which effectively addresses large-scale manifold optimization problems.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Operator-Theoretic Foundations and Policy Gradient Methods for General MDPs with Unbounded Costs
- **Authors:** Abhishek Gupta, Aditya Mahajan
- **arXiv:** [2603.17875](https://arxiv.org/abs/2603.17875v1) · [pdf](https://arxiv.org/pdf/2603.17875v1)
- **Categories:** cs.LG, math.OC

### Abstract
> Markov decision processes (MDPs) is viewed as an optimization of an objective function over certain linear operators over general function spaces. Using the well-established perturbation theory of linear operators, this viewpoint allows one to identify derivatives of the objective function as a function of the linear operators. This leads to generalization of many well-known results in reinforcement learning to cases with generate state and action spaces. Prior results of this type were only established in the finite-state finite-action MDP settings and in settings with certain linear function approximations. The framework also leads to new low-complexity PPO-type reinforcement learning algorithms for general state and action space MDPs.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) A Dual Certificate Approach to Sparsity in Infinite-Width Shallow Neural Networks
- **Authors:** Leonardo Del Grande, Christoph Brune, Marcello Carioni
- **arXiv:** [2603.17785](https://arxiv.org/abs/2603.17785v1) · [pdf](https://arxiv.org/pdf/2603.17785v1)
- **Categories:** math.OC, cs.AI

### Abstract
> In this paper, we study total variation (TV)-regularized training of infinite-width shallow ReLU neural networks, formulated as a convex optimization problem over measures on the unit sphere. Our approach leverages the duality theory of TV-regularized optimization problems to establish rigorous guarantees on the sparsity of the solutions to the training problem. Our analysis further characterizes how and when this sparsity persists in a low noise regime and for small regularization parameter. The key observation that motivates our analysis is that, for ReLU activations, the associated dual certificate is piecewise linear in the weight space. Its linearity regions, which we name dual regions, are determined by the activation patterns of the data via the induced hyperplane arrangement. Taking advantage of this structure, we prove that, on each dual region, the dual certificate admits at most one extreme value. As a consequence, the support of any minimizer is finite, and its cardinality can be bounded from above by a constant depending only on the geometry of the data-induced hyperplane arrangement. Then, we further investigate sufficient conditions ensuring uniqueness of such sparse solution. Finally, under a suitable non-degeneracy condition on the dual certificate along the boundaries of the dual regions, we prove that in the presence of low label noise and for small regularization parameter, solutions to the training problem remain sparse with the same number of Dirac deltas. Additionally, their location and the amplitudes converge, and, in case the locations lie in the interior of a dual region, the convergence happens with a rate that depends linearly on the noise and the regularization parameter.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Flow Matching Policy with Entropy Regularization
- **Authors:** Ting Gao, Stavros Orfanoudakis, Nan Lin, Elvin Isufi, Winnie Daamen, Serge Hoogendoorn
- **arXiv:** [2603.17685](https://arxiv.org/abs/2603.17685v1) · [pdf](https://arxiv.org/pdf/2603.17685v1)
- **Categories:** cs.LG

### Abstract
> Diffusion-based policies have gained significant popularity in Reinforcement Learning (RL) due to their ability to represent complex, non-Gaussian distributions. Stochastic Differential Equation (SDE)-based diffusion policies often rely on indirect entropy control due to the intractability of the exact entropy, while also suffering from computationally prohibitive policy gradients through the iterative denoising chain. To overcome these issues, we propose Flow Matching Policy with Entropy Regularization (FMER), an Ordinary Differential Equation (ODE)-based online RL framework. FMER parameterizes the policy via flow matching and samples actions along a straight probability path, motivated by optimal transport. FMER leverages the model's generative nature to construct an advantage-weighted target velocity field from a candidate set, steering policy updates toward high-value regions. By deriving a tractable entropy objective, FMER enables principled maximum-entropy optimization for enhanced exploration. Experiments on sparse multi-goal FrankaKitchen benchmarks demonstrate that FMER outperforms state-of-the-art methods, while remaining competitive on standard MuJoco benchmarks. Moreover, FMER reduces training time by 7x compared to heavy diffusion baselines (QVPO) and 10-15% relative to efficient variants.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
