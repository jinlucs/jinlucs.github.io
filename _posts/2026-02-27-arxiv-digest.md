---
layout: post
title: "Daily arXiv Digest — 2026-02-27 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction
- **Authors:** Chenhe Du, Xuanyu Tian, Qing Wu, Muyu Liu, Jingyi Yu, Hongjiang Wei, Yuyao Zhang
- **arXiv:** [2602.23214](https://arxiv.org/abs/2602.23214v1) · [pdf](https://arxiv.org/pdf/2602.23214v1)
- **Categories:** cs.CV, cs.LG, eess.IV

### Abstract
> Plug-and-Play diffusion prior (PnPDP) frameworks have emerged as a powerful paradigm for solving imaging inverse problems by treating pretrained generative models as modular priors. However, we identify a critical flaw in prevailing PnP solvers (e.g., based on HQS or Proximal Gradient): they function as memoryless operators, updating estimates solely based on instantaneous gradients. This lack of historical tracking inevitably leads to non-vanishing steady-state bias, where the reconstruction fails to strictly satisfy physical measurements under heavy corruption. To resolve this, we propose Dual-Coupled PnP Diffusion, which restores the classical dual variable to provide integral feedback, theoretically guaranteeing asymptotic convergence to the exact data manifold. However, this rigorous geometric coupling introduces a secondary challenge: the accumulated dual residuals exhibit spectrally colored, structured artifacts that violate the Additive White Gaussian Noise (AWGN) assumption of diffusion priors, causing severe hallucinations. To bridge this gap, we introduce Spectral Homogenization (SH), a frequency-domain adaptation mechanism that modulates these structured residuals into statistically compliant pseudo-AWGN inputs. This effectively aligns the solver's rigorous optimization trajectory with the denoiser's valid statistical manifold. Extensive experiments on CT and MRI reconstruction demonstrate that our approach resolves the bias-hallucination trade-off, achieving state-of-the-art fidelity with significantly accelerated convergence.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Efficient Interior-Point Methods for Hyperbolic Programming via Straight-Line Programs
- **Authors:** Mehdi Karimi, Levent Tuncel
- **arXiv:** [2602.23260](https://arxiv.org/abs/2602.23260v1) · [pdf](https://arxiv.org/pdf/2602.23260v1)
- **Categories:** math.OC

### Abstract
> Hyperbolic (HB) programming generalizes many popular convex optimization problems, including semidefinite and second-order cone programming. Despite substantial theoretical progress on HB programming, efficient computational tools for solving large-scale hyperbolic programs remain limited. This paper presents DDS 3.0, a new release of the Domain-Driven Solver, which provides an efficient interior-point implementation tailored for hyperbolic programming. A key innovation lies in a new straight-line program (SLP) representation that enables compact representation and efficient computation of hyperbolic polynomials, their gradients, and Hessians. The SLP structure significantly reduces computational cost, allowing the Hessian to be computed in the same asymptotic complexity as the gradient through a batched reverse-over-forward differentiation scheme. We further introduce an improved corrector step for the primal-dual interior-point method, enhancing stability and convergence on convex sets where only the primal self-concordant barrier is efficiently computable. We create a comprehensive benchmark library beyond the elementary symmetric polynomials, using several different techniques. Numerical experiments demonstrate substantial performance gains of DDS 3.0 compared to first-order Frank-Wolfe algorithm, homotopy method, and SDP software utilizing SDP relaxations.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Stochastic Differential Inclusions driven by Maximal Monotone Operators with empty interiors
- **Authors:** Juan Guillermo Garrido, Pedro Pérez-Aros, Mathias Staudigl
- **arXiv:** [2602.23145](https://arxiv.org/abs/2602.23145v1) · [pdf](https://arxiv.org/pdf/2602.23145v1)
- **Categories:** math.OC, math.DS

### Abstract
> This paper studies the long-time behavior of stochastic differential inclusions driven by maximal monotone operators, motivated by continuous-time models of first-order optimization methods under noisy or approximate operator information. We first address well-posedness and show that existence and uniqueness can be established without the customary requirement that the operator's domain has nonempty interior, by adopting an appropriate notion of solution. We then analyze asymptotic properties of the resulting stochastic dynamics, extending convergence guarantees beyond previously studied settings that rely on smooth potentials, full-domain subdifferentials, or Lipschitz monotone operators. In addition, we consider a Tikhonov-type regularization of the stochastic inclusion and prove corresponding well-posedness and long-time convergence results.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Iteration Complexity of Frank-Wolfe and Its Variants for Bilevel Optimization
- **Authors:** Anthony Palmieri, Francesco Rinaldi, Saverio Salzo, Sara Venturini
- **arXiv:** [2602.23076](https://arxiv.org/abs/2602.23076v1) · [pdf](https://arxiv.org/pdf/2602.23076v1)
- **Categories:** math.OC

### Abstract
> We study Frank-Wolfe (FW) methods for constrained bilevel optimization when the lower-level problem is solved only approximately, yielding biased and inexact hypergradients. We analyze inexact variants of vanilla FW as well as away-step and pairwise FW, and provide convergence rates in the nonconvex setting under gradient errors. By combining these results with recent bounds on hypergradient errors from iterative and approximate implicit differentiation, we derive overall iteration complexity guarantees for bilevel FW. Experiments on two real-world applications validate the theory and demonstrate practical effectiveness.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) MSINO: Curvature-Aware Sobolev Optimization for Manifold Neural Networks
- **Authors:** Suresan Pareth
- **arXiv:** [2602.22937](https://arxiv.org/abs/2602.22937v1) · [pdf](https://arxiv.org/pdf/2602.22937v1)
- **Categories:** cs.LG

### Abstract
> We introduce Manifold Sobolev Informed Neural Optimization (MSINO), a curvature aware training framework for neural networks defined on Riemannian manifolds. The method replaces standard Euclidean derivative supervision with a covariant Sobolev loss that aligns gradients using parallel transport and improves stability via a Laplace Beltrami smoothness regularization term. Building on classical results in Riemannian optimization and Sobolev theory on manifolds, we derive geometry dependent constants that yield (i) a Descent Lemma with a manifold Sobolev smoothness constant, (ii) a Sobolev Polyak Lojasiewicz inequality giving linear convergence guarantees for Riemannian gradient descent and stochastic gradient descent under explicit step size bounds, and (iii) a two step Newton Sobolev method with local quadratic contraction in curvature controlled neighborhoods. Unlike prior Sobolev training in Euclidean space, MSINO provides training time guarantees that explicitly track curvature and transported Jacobians. Applications include surface imaging, physics informed learning settings, and robotics on Lie groups such as SO(3) and SE(3). The framework unifies value and gradient based learning with curvature aware convergence guarantees for neural training on manifolds.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
