---
layout: post
title: "Daily arXiv Digest — 2025-12-25 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Analytic and Variational Stability of Deep Learning Systems
- **Authors:** Ronald Katende
- **arXiv:** [2512.21208](https://arxiv.org/abs/2512.21208v1) · [pdf](https://arxiv.org/pdf/2512.21208v1)
- **Categories:** cs.LG, math.DS, math.OC

### Abstract
> We propose a unified analytic and variational framework for studying stability in deep learning systems viewed as coupled representation-parameter dynamics. The central object is the Learning Stability Profile, which tracks the infinitesimal response of representations, parameters, and update mechanisms to perturbations along the learning trajectory. We prove a Fundamental Analytic Stability Theorem showing that uniform boundedness of these stability signatures is equivalent, up to norm equivalence, to the existence of a Lyapunov-type energy that dissipates along the learning flow. In smooth regimes, the framework yields explicit stability exponents linking spectral norms, activation regularity, step sizes, and learning rates to contractivity of the learning dynamics. Classical spectral stability results for feedforward networks, a discrete CFL-type condition for residual architectures, and parametric and temporal stability laws for stochastic gradient methods arise as direct consequences. The theory extends to non-smooth learning systems, including ReLU networks, proximal and projected updates, and stochastic subgradient flows, by replacing classical derivatives with Clarke generalized derivatives and smooth energies with variational Lyapunov functionals. The resulting framework provides a unified dynamical description of stability across architectures and optimization methods, clarifying how architectural and algorithmic choices jointly govern robustness and sensitivity to perturbations. It also provides a foundation for further extensions to continuous-time limits and geometric formulations of learning dynamics.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Variationally correct operator learning: Reduced basis neural operator with a posteriori error estimation
- **Authors:** Yuan Qiu, Wolfgang Dahmen, Peng Chen
- **arXiv:** [2512.21319](https://arxiv.org/abs/2512.21319v1) · [pdf](https://arxiv.org/pdf/2512.21319v1)
- **Categories:** math.NA, cs.LG

### Abstract
> Minimizing PDE-residual losses is a common strategy to promote physical consistency in neural operators. However, standard formulations often lack variational correctness, meaning that small residuals do not guarantee small solution errors due to the use of non-compliant norms or ad hoc penalty terms for boundary conditions. This work develops a variationally correct operator learning framework by constructing first-order system least-squares (FOSLS) objectives whose values are provably equivalent to the solution error in PDE-induced norms. We demonstrate this framework on stationary diffusion and linear elasticity, incorporating mixed Dirichlet-Neumann boundary conditions via variational lifts to preserve norm equivalence without inconsistent penalties. To ensure the function space conformity required by the FOSLS loss, we propose a Reduced Basis Neural Operator (RBNO). The RBNO predicts coefficients for a pre-computed, conforming reduced basis, thereby ensuring variational stability by design while enabling efficient training. We provide a rigorous convergence analysis that bounds the total error by the sum of finite element discretization bias, reduced basis truncation error, neural network approximation error, and statistical estimation errors arising from finite sampling and optimization. Numerical benchmarks validate these theoretical bounds and demonstrate that the proposed approach achieves superior accuracy in PDE-compliant norms compared to standard baselines, while the residual loss serves as a reliable, computable a posteriori error estimator.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) The Dynamical Anatomy of Anderson Acceleration:From Adaptive Momentum to Variable-Mass ODEs
- **Authors:** Kewang Chen, Yongqiu Jiang, Kees Vuik
- **arXiv:** [2512.21269](https://arxiv.org/abs/2512.21269v1) · [pdf](https://arxiv.org/pdf/2512.21269v1)
- **Categories:** math.OC, math.NA

### Abstract
> This paper provides a rigorous derivation and analysis of accelerated optimization algorithms through the lens of High-Resolution Ordinary Differential Equations (ODEs). While classical Nesterov acceleration is well-understood via asymptotic vanishing damping, the dynamics of Anderson Acceleration (AA) remain less transparent. This work makes significant theoretical contributions to AA by bridging discrete acceleration algorithms with continuous dynamical systems, while also providing practical algorithmic innovations. Our work addresses fundamental questions about the physical nature of Anderson Acceleration that have remained unanswered since its introduction in 1965. Firstly, we prove that AA can be exactly rewritten as an adaptive momentum method and, in the high-resolution limit, converges to a second-order ODE with Variable Effective Mass. Through a Lyapunov energy analysis, we reveal the specific instability mechanism of standard AA: unchecked growth in effective mass acts as negative damping, physically injecting energy into the system and violating dissipation constraints. Conversely, high-resolution analysis identifies an implicit Hessian-driven damping term that provides stabilization in stiff regimes. Leveraging these dynamical insights, we then propose Energy-Guarded Anderson Acceleration (EG-AA), an algorithm that acts as an inertial governor to enforce thermodynamic consistency. Morevoer, our convergence analysis, formulated via the Acceleration Gain Factor, proves that EG-AA improves upon gradient descent by maximizing the geometric contraction of the linear subspace projection while actively suppressing nonlinear approximation errors. Theoretical bounds confirm that EG-AA is no worse than standard AA, and numerical experiments demonstrate strictly improved convergence stability and rates in ill-conditioned convex composite problems compared to standard Anderson mixing.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Improving the Convergence Rate of Ray Search Optimization for Query-Efficient Hard-Label Attacks
- **Authors:** Xinjie Xu, Shuyu Cheng, Dongwei Xu, Qi Xuan, Chen Ma
- **arXiv:** [2512.21241](https://arxiv.org/abs/2512.21241v1) · [pdf](https://arxiv.org/pdf/2512.21241v1)
- **Categories:** cs.LG, cs.AI, cs.CR, cs.CV

### Abstract
> In hard-label black-box adversarial attacks, where only the top-1 predicted label is accessible, the prohibitive query complexity poses a major obstacle to practical deployment. In this paper, we focus on optimizing a representative class of attacks that search for the optimal ray direction yielding the minimum $\ell_2$-norm perturbation required to move a benign image into the adversarial region. Inspired by Nesterov's Accelerated Gradient (NAG), we propose a momentum-based algorithm, ARS-OPT, which proactively estimates the gradient with respect to a future ray direction inferred from accumulated momentum. We provide a theoretical analysis of its convergence behavior, showing that ARS-OPT enables more accurate directional updates and achieves faster, more stable optimization. To further accelerate convergence, we incorporate surrogate-model priors into ARS-OPT's gradient estimation, resulting in PARS-OPT with enhanced performance. The superiority of our approach is supported by theoretical guarantees under standard assumptions. Extensive experiments on ImageNet and CIFAR-10 demonstrate that our method surpasses 13 state-of-the-art approaches in query efficiency.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Understanding Scaling Laws in Deep Neural Networks via Feature Learning Dynamics
- **Authors:** Zihan Yao, Ruoyu Wu, Tianxiang Gao
- **arXiv:** [2512.21075](https://arxiv.org/abs/2512.21075v1) · [pdf](https://arxiv.org/pdf/2512.21075v1)
- **Categories:** cs.LG, cs.AI, math.PR, stat.ML

### Abstract
> The empirical success of deep learning is often attributed to scaling laws that predict consistent gains as model, data, and compute grow; however, large models can exhibit training instability and diminishing returns, suggesting that scaling laws describe what success looks like but not when and why scaling succeeds or fails. A central obstacle is the lack of a rigorous understanding of feature learning at large depth. While muP characterizes feature-learning dynamics in the infinite-width limit and enables hyperparameter transfer across width, its depth extension (depth-muP) breaks down for residual blocks with more than one internal layer. We derive Neural Feature Dynamics (NFD) for ResNets with single-layer residual blocks, characterizing feature learning via a coupled forward-backward stochastic system in the joint infinite-width and infinite-depth limit. In this regime, NFD identifies when scaling-law trends persist and explains diminishing returns. It also reveals a vanishing mechanism induced by the 1/sqrt(depth) residual scaling under which the gradient-independence assumption (GIA), known to fail during training at finite depth, becomes provably valid again at infinite depth, yielding an analytically tractable regime for end-to-end feature learning. Motivated by this insight, we study two-layer residual blocks and show that the same mechanism causes feature-learning collapse in the first internal layer at large depth, providing a structural explanation for the empirical failure of depth-muP. Based on this diagnosis, we propose a depth-aware learning-rate correction that counteracts the collapse and empirically restores depth-wise hyperparameter transfer, yielding stronger performance in deeper ResNets.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
