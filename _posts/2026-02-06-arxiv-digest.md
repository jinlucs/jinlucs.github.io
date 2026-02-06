---
layout: post
title: "Daily arXiv Digest — 2026-02-06 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Visualizing the loss landscapes of physics-informed neural networks
- **Authors:** Conor Rowan, Finn Murphy-Blanchard
- **arXiv:** [2602.05849](https://arxiv.org/abs/2602.05849v1) · [pdf](https://arxiv.org/pdf/2602.05849v1)
- **Categories:** cs.LG

### Abstract
> Training a neural network requires navigating a high-dimensional, non-convex loss surface to find parameters that minimize this loss. In many ways, it is surprising that optimizers such as stochastic gradient descent and ADAM can reliably locate minima which perform well on both the training and test data. To understand the success of training, a "loss landscape" community has emerged to study the geometry of the loss function and the dynamics of optimization, often using visualization techniques. However, these loss landscape studies have mostly been limited to machine learning for image classification. In the newer field of physics-informed machine learning, little work has been conducted to visualize the landscapes of losses defined not by regression to large data sets, but by differential operators acting on state fields discretized by neural networks. In this work, we provide a comprehensive review of the loss landscape literature, as well as a discussion of the few existing physics-informed works which investigate the loss landscape. We then use a number of the techniques we survey to empirically investigate the landscapes defined by the Deep Ritz and squared residual forms of the physics loss function. We find that the loss landscapes of physics-informed neural networks have many of the same properties as the data-driven classification problems studied in the literature. Unexpectedly, we find that the two formulations of the physics loss often give rise to similar landscapes, which appear smooth, well-conditioned, and convex in the vicinity of the solution. The purpose of this work is to introduce the loss landscape perspective to the scientific machine learning community, compare the Deep Ritz and the strong form losses, and to challenge prevailing intuitions about the complexity of the loss landscapes of physics-informed networks.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) The Signed Wasserstein Barycenter Problem
- **Authors:** Matt Jacobs, Bohan Zhou
- **arXiv:** [2602.05976](https://arxiv.org/abs/2602.05976v1) · [pdf](https://arxiv.org/pdf/2602.05976v1)
- **Categories:** math.OC, math.PR

### Abstract
> Barycenter problems encode important geometric information about a metric space. While these problems are typically studied with positive weight coefficients associated to each distance term, more general signed Wasserstein barycenter problems have recently drawn a great deal of interest. These mixed sign problems have appeared in statistical inference setting as a way to generalize least squares regression to measure valued outputs and have appeared in numerical methods to improve the accuracy of Wasserstein gradient flow solvers. Unfortunately, the presence of negatively weighted distance terms destroys the Euclidean convexity of the unsigned problem, resulting in a much more challenging optimization task. The main focus of this work is to study properties of the signed barycenter problem for a general transport cost with a focus on establishing uniqueness of solutions. In particular, when there is only one positive weight, we extend the uniqueness result of Tornabene et al. (2025) to any cost satisfying a certain convexity property. In the case of arbitrary weights, we introduce the dual problem in terms of Kantorovich potentials and provide a sufficient condition for a stationary solution of the dual problem to induce an optimal signed barycenter.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Normalization of ReLU Dual for Cut Generation in Stochastic Mixed-Integer Programs
- **Authors:** Akul Bansal, Simge Küçükyavuz
- **arXiv:** [2602.05974](https://arxiv.org/abs/2602.05974v1) · [pdf](https://arxiv.org/pdf/2602.05974v1)
- **Categories:** math.OC, eess.SY

### Abstract
> We study the Rectified Linear Unit (ReLU) dual, an existing dual formulation for stochastic programs that reformulates non-anticipativity constraints using ReLU functions to generate tight, non-convex, and mixed-integer representable cuts. While this dual reformulation guarantees convergence with mixed-integer state variables, it admits multiple optimal solutions that can yield weak cuts. To address this issue, we propose normalizing the dual in the extended space to identify solutions that yield stronger cuts. We prove that the resulting normalized cuts are tight and Pareto-optimal in the original state space. We further compare normalization with existing regularization-based approaches for handling dual degeneracy and explain why normalization offers key advantages. In particular, we show that normalization can recover any cut obtained via regularization, whereas the converse does not hold. Computational experiments demonstrate that the proposed approach outperforms existing methods by consistently yielding stronger cuts and reducing solution times on harder instances.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Escaping Local Minima Provably in Non-convex Matrix Sensing: A Deterministic Framework via Simulated Lifting
- **Authors:** Tianqi Shen, Jinji Yang, Junze He, Kunhan Gao, Ziye Ma
- **arXiv:** [2602.05887](https://arxiv.org/abs/2602.05887v1) · [pdf](https://arxiv.org/pdf/2602.05887v1)
- **Categories:** cs.LG, math.OC

### Abstract
> Low-rank matrix sensing is a fundamental yet challenging nonconvex problem whose optimization landscape typically contains numerous spurious local minima, making it difficult for gradient-based optimizers to converge to the global optimum. Recent work has shown that over-parameterization via tensor lifting can convert such local minima into strict saddle points, an insight that also partially explains why massive scaling can improve generalization and performance in modern machine learning. Motivated by this observation, we propose a Simulated Oracle Direction (SOD) escape mechanism that simulates the landscape and escape direction of the over-parametrized space, without resorting to actually lifting the problem, since that would be computationally intractable. In essence, we designed a mathematical framework to project over-parametrized escape directions onto the original parameter space to guarantee a strict decrease of objective value from existing local minima. To the best of the our knowledge, this represents the first deterministic framework that could escape spurious local minima with guarantee, especially without using random perturbations or heuristic estimates. Numerical experiments demonstrate that our framework reliably escapes local minima and facilitates convergence to global optima, while incurring minimal computational cost when compared to explicit tensor over-parameterization. We believe this framework has non-trivial implications for nonconvex optimization beyond matrix sensing, by showcasing how simulated over-parameterization can be leveraged to tame challenging optimization landscapes.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Large-scale Score-based Variational Posterior Inference for Bayesian Deep Neural Networks
- **Authors:** Minyoung Kim
- **arXiv:** [2602.05873](https://arxiv.org/abs/2602.05873v1) · [pdf](https://arxiv.org/pdf/2602.05873v1)
- **Categories:** cs.LG

### Abstract
> Bayesian (deep) neural networks (BNN) are often more attractive than the mainstream point-estimate vanilla deep learning in various aspects including uncertainty quantification, robustness to noise, resistance to overfitting, and more. The variational inference (VI) is one of the most widely adopted approximate inference methods. Whereas the ELBO-based variational free energy method is a dominant choice in the literature, in this paper we introduce a score-based alternative for BNN variational inference. Although there have been quite a few score-based variational inference methods proposed in the community, most are not adequate for large-scale BNNs for various computational and technical reasons. We propose a novel scalable VI method where the learning objective combines the score matching loss and the proximal penalty term in iterations, which helps our method avoid the reparametrized sampling, and allows for noisy unbiased mini-batch scores through stochastic gradients. This in turn makes our method scalable to large-scale neural networks including Vision Transformers, and allows for richer variational density families. On several benchmarks including visual recognition and time-series forecasting with large-scale deep networks, we empirically show the effectiveness of our approach.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
