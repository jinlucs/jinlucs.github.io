---
layout: post
title: "Daily arXiv Digest — 2026-03-10 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Group Entropies and Mirror Duality: A Class of Flexible Mirror Descent Updates for Machine Learning
- **Authors:** Andrzej Cichocki, Piergiulio Tempesta
- **arXiv:** [2603.08651](https://arxiv.org/abs/2603.08651v1) · [pdf](https://arxiv.org/pdf/2603.08651v1)
- **Categories:** cs.LG, hep-th, math-ph

### Abstract
> We introduce a comprehensive theoretical and algorithmic framework that bridges formal group theory and group entropies with modern machine learning, paving the way for an infinite, flexible family of Mirror Descent (MD) optimization algorithms. Our approach exploits the rich structure of group entropies, which are generalized entropic functionals governed by group composition laws, encompassing and significantly extending all trace-form entropies such as the Shannon, Tsallis, and Kaniadakis families. By leveraging group-theoretical mirror maps (or link functions) in MD, expressed via multi-parametric generalized logarithms and their inverses (group exponentials), we achieve highly flexible and adaptable MD updates that can be tailored to diverse data geometries and statistical distributions. To this end, we introduce the notion of \textit{mirror duality}, which allows us to seamlessly switch or interchange group-theoretical link functions with their inverses, subject to specific learning rate constraints. By tuning or learning the hyperparameters of the group logarithms enables us to adapt the model to the statistical properties of the training distribution, while simultaneously ensuring desirable convergence characteristics via fine-tuning. This generality not only provides greater flexibility and improved convergence properties, but also opens new perspectives for applications in machine learning and deep learning by expanding the design of regularizers and natural gradient algorithms. We extensively evaluate the validity, robustness, and performance of the proposed updates on large-scale, simplex-constrained quadratic programming problems.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) DualFlexKAN: Dual-stage Kolmogorov-Arnold Networks with Independent Function Control
- **Authors:** Andrés Ortiz, Nicolás J. Gallego-Molina, Carmen Jiménez-Mesa, Juan M. Górriz, Javier Ramírez
- **arXiv:** [2603.08583](https://arxiv.org/abs/2603.08583v1) · [pdf](https://arxiv.org/pdf/2603.08583v1)
- **Categories:** cs.LG, cs.CV

### Abstract
> Multi-Layer Perceptrons (MLPs) rely on pre-defined, fixed activation functions, imposing a static inductive bias that forces the network to approximate complex topologies solely through increased depth and width. Kolmogorov-Arnold Networks (KANs) address this limitation through edge-centric learnable functions, yet their formulation suffers from quadratic parameter scaling and architectural rigidity that hinders the effective integration of standard regularization techniques. This paper introduces the DualFlexKAN (DFKAN), a flexible architecture featuring a dual-stage mechanism that independently controls pre-linear input transformations and post-linear output activations. This decoupling enables hybrid networks that optimize the trade-off between expressiveness and computational cost. Unlike standard formulations, DFKAN supports diverse basis function families, including orthogonal polynomials, B-splines, and radial basis functions, integrated with configurable regularization strategies that stabilize training dynamics. Comprehensive evaluations across regression benchmarks, physics-informed tasks, and function approximation demonstrate that DFKAN outperforms both MLPs and conventional KANs in accuracy, convergence speed, and gradient fidelity. The proposed hybrid configurations achieve superior performance with one to two orders of magnitude fewer parameters than standard KANs, effectively mitigating the parameter explosion problem while preserving KAN-style expressiveness. DFKAN provides a principled, scalable framework for incorporating adaptive non-linearities, proving particularly advantageous for data-efficient learning and interpretable function discovery in scientific applications.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Loopless Proximal Riemannian Gradient EXTRA for Distributed Optimization on Compact Manifolds
- **Authors:** Yongyang Xiong, Chen Ouyang, Keyou You, Yang Shi, Ligang Wu
- **arXiv:** [2603.08367](https://arxiv.org/abs/2603.08367v1) · [pdf](https://arxiv.org/pdf/2603.08367v1)
- **Categories:** math.OC

### Abstract
> Distributed optimization has gained substantial interest in recent years due to its wide applications in machine learning. However, most of existing algorithms are designed for Euclidean spaces, leaving composite optimization on Riemannian manifolds largely unexplored. To bridge this gap, we propose the proximal Riemannian gradient EXTRA algorithm (PR-EXTRA) to solve distributed composite optimization problem with nonsmooth regularizer over compact manifolds. In each iteration, PR-EXTRA requires only a single round communication, coupled with local gradient evaluations and proximal mappings. Furthermore, a manifold projection operator is integrated to ensure the feasibility of all iterates throughout the optimization process. Theoretical analysis shows that with a constant stepsize, PR-EXTRA achieves a sublinear convergence rate of $\mathcal{O}(1/K)$ to a stationary point, matching the proximal gradient EXTRA algorithm in Euclidean spaces. Numerical experiments show the effectiveness of the proposed algorithm.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Airborne Magnetic Anomaly Navigation with Neural-Network-Augmented Online Calibration
- **Authors:** Antonia Hager, Sven Nebendahl, Alexej Klushyn, Jasper Krauser, Torleiv H. Bryne, Tor Arne Johansen
- **arXiv:** [2603.08265](https://arxiv.org/abs/2603.08265v1) · [pdf](https://arxiv.org/pdf/2603.08265v1)
- **Categories:** cs.LG

### Abstract
> Airborne Magnetic Anomaly Navigation (MagNav) provides a jamming-resistant and robust alternative to satellite navigation but requires the real-time compensation of the aircraft platform's large and dynamic magnetic interference. State-of-the-art solutions often rely on extensive offline calibration flights or pre-training, creating a logistical barrier to operational deployment. We present a fully adaptive MagNav architecture featuring a "cold-start" capability that identifies and compensates for the aircraft's magnetic signature entirely in-flight. The proposed method utilizes an extended Kalman filter with an augmented state vector that simultaneously estimates the aircraft's kinematic states as well as the coefficients of the physics-based Tolles-Lawson calibration model and the parameters of a Neural Network to model aircraft interferences. The Kalman filter update is mathematically equivalent to an online Natural Gradient descent, integrating superior convergence and data efficiency of state-of-the-art second-order optimization directly into the navigation filter. To enhance operational robustness, the neural network is constrained to a residual learning role, modeling only the nonlinearities uncorrected by the explainable physics-based calibration baseline. Validated on the MagNav Challenge dataset, our framework effectively bounds inertial drift using a magnetometer-only feature set. The results demonstrate navigation accuracy comparable to state-of-the-art models trained offline, without requiring prior calibration flights or dedicated maneuvers.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Momentum SVGD-EM for Accelerated Maximum Marginal Likelihood Estimation
- **Authors:** Adam Rozzio, Rafael Athanasiades, O. Deniz Akyildiz
- **arXiv:** [2603.08676](https://arxiv.org/abs/2603.08676v1) · [pdf](https://arxiv.org/pdf/2603.08676v1)
- **Categories:** stat.ML, cs.LG, stat.CO

### Abstract
> Maximum marginal likelihood estimation (MMLE) can be formulated as the optimization of a free energy functional. From this viewpoint, the Expectation-Maximisation (EM) algorithm admits a natural interpretation as a coordinate descent method over the joint space of model parameters and probability measures. Recently, a significant body of work has adopted this perspective, leading to interacting particle algorithms for MMLE. In this paper, we propose an accelerated version of one such procedure, based on Stein variational gradient descent (SVGD), by introducing Nesterov acceleration in both the parameter updates and in the space of probability measures. The resulting method, termed Momentum SVGD-EM, consistently accelerates convergence in terms of required iterations across various tasks of increasing difficulty, demonstrating effectiveness in both low- and high-dimensional settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
