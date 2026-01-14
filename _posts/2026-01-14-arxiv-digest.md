---
layout: post
title: "Daily arXiv Digest — 2026-01-14 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Convergence of gradient flow for learning convolutional neural networks
- **Authors:** Jona-Maria Diederen, Holger Rauhut, Ulrich Terstiege
- **arXiv:** [2601.08547](https://arxiv.org/abs/2601.08547v1) · [pdf](https://arxiv.org/pdf/2601.08547v1)
- **Categories:** math.OC, cs.LG

### Abstract
> Convolutional neural networks are widely used in imaging and image recognition. Learning such networks from training data leads to the minimization of a non-convex function. This makes the analysis of standard optimization methods such as variants of (stochastic) gradient descent challenging. In this article we study the simplified setting of linear convolutional networks. We show that the gradient flow (to be interpreted as an abstraction of gradient descent) applied to the empirical risk defined via certain loss functions including the square loss always converges to a critical point, under a mild condition on the training data.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Riemannian optimization with finite-difference gradient approximations
- **Authors:** Timothé Taminiau, Estelle Massart, Geovani Nunes Grapiglia
- **arXiv:** [2601.08751](https://arxiv.org/abs/2601.08751v1) · [pdf](https://arxiv.org/pdf/2601.08751v1)
- **Categories:** math.OC

### Abstract
> Derivative-free Riemannian optimization (DFRO) aims to minimize an objective function using only function evaluations, under the constraint that the decision variables lie on a Riemannian manifold. The rapid increase in problem dimensions over the years calls for computationally cheap DFRO algorithms, that is, algorithms requiring as few function evaluations and retractions as possible. We propose a novel DFRO method based on finite-difference gradient approximations that relies on an adaptive selection of the finite-difference accuracy and stepsize that is novel even in the Euclidean setting. When endowed with an intrinsic finite-difference scheme, that measures variations of the objective in tangent directions using retractions, our proposed method requires $O(dε^{-2})$ function evaluations and retractions to find an $ε$-critical point, where $d$ is the manifold dimension. We then propose a variant of our method when the search space is a Riemannian submanifold of an $n$-dimensional Euclidean space. This variant relies on an extrinsic finite-difference scheme, approximating the Riemannian gradient directly in the embedding space, assuming that the objective function can be evaluated outside of the manifold. This approach leads to worst-case complexity bounds of $O(dε^{-2})$ function evaluations and $O(ε^{-2})$ retractions. We also present numerical results showing that the proposed methods achieve superior performance over existing derivative-free methods on various problems in both Euclidean and Riemannian settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Kernel Learning for Regression via Quantum Annealing Based Spectral Sampling
- **Authors:** Yasushi Hasegawa, Masayuki Ohzeki
- **arXiv:** [2601.08724](https://arxiv.org/abs/2601.08724v1) · [pdf](https://arxiv.org/pdf/2601.08724v1)
- **Categories:** quant-ph, cs.LG

### Abstract
> While quantum annealing (QA) has been developed for combinatorial optimization, practical QA devices operate at finite temperature and under noise, and their outputs can be regarded as stochastic samples close to a Gibbs--Boltzmann distribution. In this study, we propose a QA-in-the-loop kernel learning framework that integrates QA not merely as a substitute for Markov-chain Monte Carlo sampling but as a component that directly determines the learned kernel for regression. Based on Bochner's theorem, a shift-invariant kernel is represented as an expectation over a spectral distribution, and random Fourier features (RFF) approximate the kernel by sampling frequencies. We model the spectral distribution with a (multi-layer) restricted Boltzmann machine (RBM), generate discrete RBM samples using QA, and map them to continuous frequencies via a Gaussian--Bernoulli transformation. Using the resulting RFF, we construct a data-adaptive kernel and perform Nadaraya--Watson (NW) regression. Because the RFF approximation based on $\cos(\bmω^{\top}Δ\bm{x})$ can yield small negative values and cancellation across neighbors, the Nadaraya--Watson denominator $\sum_j k_{ij}$ may become close to zero. We therefore employ nonnegative squared-kernel weights $w_{ij}=k(\bm{x}_i,\bm{x}_j)^2$, which also enhances the contrast of kernel weights. The kernel parameters are trained by minimizing the leave-one-out NW mean squared error, and we additionally evaluate local linear regression with the same squared-kernel weights at inference. Experiments on multiple benchmark regression datasets demonstrate a decrease in training loss, accompanied by structural changes in the kernel matrix, and show that the learned kernel tends to improve $R^2$ and RMSE over the baseline Gaussian-kernel NW. Increasing the number of random features at inference further enhances accuracy.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Optimal Dirac controls for time-periodic bistable ODEs, application to population replacement
- **Authors:** Grégoire Nadin, David Nahmani, Nicolas Vauchelet
- **arXiv:** [2601.08630](https://arxiv.org/abs/2601.08630v1) · [pdf](https://arxiv.org/pdf/2601.08630v1)
- **Categories:** math.OC, math.AP, math.CA

### Abstract
> This work addresses an optimal control problem on a dynamics governed by a nonlinear differential equation with a bistable time-periodic nonlinearity. This problem, relevant in population dynamics, models the strategy of replacing a population of A-type individuals by a population of B-type individuals in a time-varying environment, focusing on the evolution of the proportion of B-type individuals among the whole population. The control term accounts for the instant release of B-type individuals. Our main goal, after noting some interesting properties on the differential equation, is to determine the optimal time at which this release should be operated to ensure population replacement while minimizing the release effort. The results establish that the optimal release time appears to be the minimizer of a function involving the carrying capacity of the environment and the threshold periodic solution of the dynamics; they also describe the convergence of the whole optimal release strategy. An application to the biocontrol of mosquito populations using Wolbachia-infected individuals illustrates the relevance of the theoretical results. Wolbachia is a bacterium that helps preventing the transmission of some viruses from mosquitoes to humans, making the optimization of Wolbachia propagation in a mosquito population a crucial issue.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Differentiating through Stochastic Differential Equations: A Primer
- **Authors:** Rishi Leburu, Levon Nurbekyan, Lars Ruthotto
- **arXiv:** [2601.08594](https://arxiv.org/abs/2601.08594v1) · [pdf](https://arxiv.org/pdf/2601.08594v1)
- **Categories:** math.NA, math.OC, math.PR

### Abstract
> Dynamical systems are essential to model various phenomena in physics, finance, economics, and are also of current interest in machine learning. A central modeling task is investigating parameter sensitivity, whether tuning atmospheric coefficients, computing financial Greeks, or optimizing neural networks. These sensitivities are mathematically expressed as derivatives of an objective function with respect to parameters of interest and are rarely available analytically, necessitating numerical methods for approximating them. While the literature for differentiation of deterministic systems is well-covered, the treatment of stochastic systems, such as stochastic differential equations (SDEs), in most curricula is less comprehensive than the subtleties arising from the interplay of noise and discretization require. This paper provides a primer on numerical differentiation of SDEs organized as a two-tale narrative. Tale 1 demonstrates differentiating through discretized SDEs, known the discretize-optimize approach, is reliable for both Itô and Stratonovich calculus. Tale 2 examines the optimize-discretize approach, investigating the continuous limit of backward equations from Tale 1 corresponding to the desired gradients. Our aim is to equip readers with a clear guide on the numerical differentiation of SDEs: computing gradients correctly in both Itô and Stratonovich settings, understanding when discretize-optimize and optimize-discretize agree or diverge, and developing intuition for reasoning about stochastic differentiation beyond the cases explicitly covered.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
