---
layout: post
title: "Daily arXiv Digest — 2026-02-10 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Switching Point Optimization for Abstract Parabolic Equations
- **Authors:** Christian Meyer, Alimhan Musalatov
- **arXiv:** [2602.08906](https://arxiv.org/abs/2602.08906v1) · [pdf](https://arxiv.org/pdf/2602.08906v1)
- **Categories:** math.OC

### Abstract
> This work is concerned with a switching point optimization problem governed by a semilinear parabolic equation in abstract function spaces. It is shown that the switching-point-to-control mapping is continuously Fréchet-differentiable when considered with values in the dual of Hölder continuous functions in time. By treating the state equation in weak form based on the concept of maximal parabolic regularity, one can then show that the reduced objective is continuously differentiable w.r.t.\ the switching points which allows to use gradient-based method like the proximal gradient method for its minimization. In order to apply the known convergence results of this method, the gradient of the reduced objective must be Lipschitz continuous, which requires additional assumptions on the data. Numerical experiments confirm our theoretical findings, but also illustrate that such a method will in general not be able to solve the problem up to global optimality due to the non-convex nature of the switching-point-to-control map.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling
- **Authors:** Yilang Zhang, Bingcong Li, Niao He, Georgios B. Giannakis
- **arXiv:** [2602.09009](https://arxiv.org/abs/2602.09009v1) · [pdf](https://arxiv.org/pdf/2602.09009v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Scaling network depth has been a central driver behind the success of modern foundation models, yet recent investigations suggest that deep layers are often underutilized. This paper revisits the default mechanism for deepening neural networks, namely residual connections, from an optimization perspective. Rigorous analysis proves that the layout of residual connections can fundamentally shape convergence behavior, and even induces an exponential gap in convergence rates. Prompted by this insight, we introduce adaptive neural connection reassignment (ANCRe), a principled and lightweight framework that parameterizes and learns residual connectivities from the data. ANCRe adaptively reassigns residual connections with negligible computational and memory overhead ($<1\%$), while enabling more effective utilization of network depth. Extensive numerical tests across pre-training of large language models, diffusion models, and deep ResNets demonstrate consistently accelerated convergence, boosted performance, and enhanced depth efficiency over conventional residual connections.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) ARO: A New Lens On Matrix Optimization For Large Models
- **Authors:** Wenbo Gong, Javier Zazo, Qijun Luo, Puqian Wang, James Hensman, Chao Ma
- **arXiv:** [2602.09006](https://arxiv.org/abs/2602.09006v1) · [pdf](https://arxiv.org/pdf/2602.09006v1)
- **Categories:** cs.LG, cs.AI, math.OC

### Abstract
> Matrix-based optimizers have attracted growing interest for improving LLM training efficiency, with significant progress centered on orthogonalization/whitening based methods. While yielding substantial performance gains, a fundamental question arises: can we develop new paradigms beyond orthogonalization, pushing the efficiency frontier further? We present \textbf{Adaptively Rotated Optimization (ARO}, a new matrix optimization framework that treats gradient rotation as a first class design principle. ARO accelerates LLM training by performing normed steepest descent in a rotated coordinate system, where the rotation is determined by a novel norm-informed policy. This perspective yields update rules that go beyond existing orthogonalization and whitening optimizers, improving sample efficiency in practice. To make comparisons reliable, we propose a rigorously controlled benchmarking protocol that reduces confounding and bias. Under this protocol, ARO consistently outperforms AdamW (by 1.3 $\sim$1.35$\times$) and orthogonalization methods (by 1.1$\sim$1.15$\times$) in LLM pretraining at up to 8B activated parameters, and up to $8\times$ overtrain budget, without evidence of diminishing returns. Finally, we discuss how ARO can be reformulated as a symmetry-aware optimizer grounded in rotational symmetries of residual streams, motivating advanced designs that enable computationally efficient exploitation of cross-layer/cross module couplings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Reduced-order Control and Geometric Structure of Learned Lagrangian Latent Dynamics
- **Authors:** Katharina Friedl, Noémie Jaquier, Seungyeon Kim, Jens Lundell, Danica Kragic
- **arXiv:** [2602.08963](https://arxiv.org/abs/2602.08963v1) · [pdf](https://arxiv.org/pdf/2602.08963v1)
- **Categories:** cs.RO, math.OC

### Abstract
> Model-based controllers can offer strong guarantees on stability and convergence by relying on physically accurate dynamic models. However, these are rarely available for high-dimensional mechanical systems such as deformable objects or soft robots. While neural architectures can learn to approximate complex dynamics, they are either limited to low-dimensional systems or provide only limited formal control guarantees due to a lack of embedded physical structure. This paper introduces a latent control framework based on learned structure-preserving reduced-order dynamics for high-dimensional Lagrangian systems. We derive a reduced tracking law for fully actuated systems and adopt a Riemannian perspective on projection-based model-order reduction to study the resulting latent and projected closed-loop dynamics. By quantifying the sources of modeling error, we derive interpretable conditions for stability and convergence. We extend the proposed controller and analysis to underactuated systems by introducing learned actuation patterns. Experimental results on simulated and real-world systems validate our theoretical investigation and the accuracy of our controllers.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Provably robust learning of regression neural networks using $β$-divergences
- **Authors:** Abhik Ghosh, Suryasis Jana
- **arXiv:** [2602.08933](https://arxiv.org/abs/2602.08933v1) · [pdf](https://arxiv.org/pdf/2602.08933v1)
- **Categories:** stat.ML, cs.LG, cs.NE, stat.ME

### Abstract
> Regression neural networks (NNs) are most commonly trained by minimizing the mean squared prediction error, which is highly sensitive to outliers and data contamination. Existing robust training methods for regression NNs are often limited in scope and rely primarily on empirical validation, with only a few offering partial theoretical guarantees. In this paper, we propose a new robust learning framework for regression NNs based on the $β$-divergence (also known as the density power divergence) which we call `rRNet'. It applies to a broad class of regression NNs, including models with non-smooth activation functions and error densities, and recovers the classical maximum likelihood learning as a special case. The rRNet is implemented via an alternating optimization scheme, for which we establish convergence guarantees to stationary points under mild, verifiable conditions. The (local) robustness of rRNet is theoretically characterized through the influence functions of both the parameter estimates and the resulting rRNet predictor, which are shown to be bounded for suitable choices of the tuning parameter $β$, depending on the error density. We further prove that rRNet attains the optimal 50\% asymptotic breakdown point at the assumed model for all $β\in(0, 1]$, providing a strong global robustness guarantee that is largely absent for existing NN learning methods. Our theoretical results are complemented by simulation experiments and real-data analyses, illustrating practical advantages of rRNet over existing approaches in both function approximation problems and prediction tasks with noisy observations.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
