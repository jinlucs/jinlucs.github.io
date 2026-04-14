---
layout: post
title: "Daily arXiv Digest — 2026-04-14 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Emulating Non-Differentiable Metrics via Knowledge-Guided Learning: Introducing the Minkowski Image Loss
- **Authors:** Filippo Quarenghi, Ryan Cotsakis, Tom Beucler
- **arXiv:** [2604.11422](https://arxiv.org/abs/2604.11422v1) · [pdf](https://arxiv.org/pdf/2604.11422v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> The ``differentiability gap'' presents a primary bottleneck in Earth system deep learning: since models cannot be trained directly on non-differentiable scientific metrics and must rely on smooth proxies (e.g., MSE), they often fail to capture high-frequency details, yielding ``blurry'' outputs. We develop a framework that bridges this gap using two different methods to deal with non-differentiable functions: the first is to analytically approximate the original non-differentiable function into a differentiable equivalent one; the second is to learn differentiable surrogates for scientific functionals. We formulate the analytical approximation by relaxing discrete topological operations using temperature-controlled sigmoids and continuous logical operators. Conversely, our neural emulator uses Lipschitz-convolutional neural networks to stabilize gradient learning via: (1) spectral normalization to bound the Lipschitz constant; and (2) hard architectural constraints enforcing geometric principles. We demonstrate this framework's utility by developing the Minkowski image loss, a differentiable equivalent for the integral-geometric measures of surface precipitation fields (area, perimeter, connected components). Validated on the EUMETNET OPERA dataset, our constrained neural surrogate achieves high emulation accuracy, completely eliminating the geometric violations observed in unconstrained baselines. However, applying these differentiable surrogates to a deterministic super-resolution task reveals a fundamental trade-off: while strict Lipschitz regularization ensures optimization stability, it inherently over-smooths gradient signals, restricting the recovery of highly localized convective textures. This work highlights the necessity of coupling such topological constraints with stochastic generative architectures to achieve full morphological realism.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) A Distributed Bilevel Framework for the Macroscopic Optimization of Multi-Agent Systems
- **Authors:** Riccardo Brumali, Guido Carnevale, Sonia Martínez, Giuseppe Notarstefano
- **arXiv:** [2604.11712](https://arxiv.org/abs/2604.11712v1) · [pdf](https://arxiv.org/pdf/2604.11712v1)
- **Categories:** math.OC

### Abstract
> In this paper, we propose a novel distributed algorithm to optimize the emergent macroscopic behavior of large-scale multi-agent systems via microscopic actions. We cast this task as a bilevel optimization problem, where the upper level formalizes the desired macroscopic target behavior through a suitable performance criterion, which is shaped in the lower level by leveraging a compressed aggregate representation estimating the macroscopic state. More precisely, the macroscopic state is parametrized by an exponential-family of distributions and constructed from the multi-agent microscopic configuration. The proposed algorithm integrates a distributed estimation mechanism, through which each agent reconstructs the macroscopic state locally, with a hypergradient-based update of the microscopic states aimed at improving the collective macroscopic behavior. We prove convergence to the set of stationary points of the bilevel problem via timescale separation arguments. Numerical simulations validate the effectiveness of the proposed method.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Generative Path-Finding Method for Wasserstein Gradient Flow
- **Authors:** Chengyu Liu, Xiang Zhou
- **arXiv:** [2604.11519](https://arxiv.org/abs/2604.11519v1) · [pdf](https://arxiv.org/pdf/2604.11519v1)
- **Categories:** cs.LG, math-ph

### Abstract
> Wasserstein gradient flows (WGFs) describe the evolution of probability distributions in Wasserstein space as steepest descent dynamics for a free energy functional. Computing the full path from an arbitrary initial distribution to equilibrium is challenging, especially in high dimensions. Eulerian methods suffer from the curse of dimensionality, while existing Lagrangian approaches based on particles or generative maps do not naturally improve efficiency through time step tuning. We propose GenWGP, a generative path finding framework for Wasserstein gradient paths. GenWGP learns a generative flow that transports mass from an initial density to an unknown equilibrium distribution by minimizing a path loss that encodes the full trajectory and its terminal equilibrium condition. The loss is derived from a geometric action functional motivated by Dawson Gartner large deviation theory for empirical distributions of interacting diffusion systems. We formulate both a finite horizon action under physical time parametrization and a reparameterization invariant geometric action based on Wasserstein arclength. Using normalizing flows, GenWGP computes a geometric curve toward equilibrium while enforcing approximately constant intrinsic speed between adjacent network layers, so that discretized distributions remain nearly equidistant in the Wasserstein metric along the path. This avoids delicate time stepping constraints and enables stable training that is largely independent of temporal or geometric discretization. Experiments on Fokker Planck and aggregation type problems show that GenWGP matches or exceeds high fidelity reference solutions with only about a dozen discretization points while capturing complex dynamics.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Not All Forgetting Is Equal: Architecture-Dependent Retention Dynamics in Fine-Tuned Image Classifiers
- **Authors:** Miit Daga, Swarna Priya Ramu
- **arXiv:** [2604.11508](https://arxiv.org/abs/2604.11508v1) · [pdf](https://arxiv.org/pdf/2604.11508v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Fine-tuning pretrained image classifiers is standard practice, yet which individual samples are forgotten during this process, and whether forgetting patterns are stable or architecture dependent, remains unclear. Understanding these dynamics has direct implications for curriculum design, data pruning, and ensemble construction. We track per-sample correctness at every epoch during fine-tuning of ResNet-18 and DeiT-Small on a retinal OCT dataset (7 classes, 56:1 imbalance) and CUB-200-2011 (200 bird species), fitting Ebbinghaus-style exponential decay curves to each sample's retention trace. Five findings emerge. First, the two architectures forget fundamentally different samples: Jaccard overlap of the top 10 percent most-forgotten is 0.34 on OCTDL and 0.15 on CUB-200. Second, ViT forgetting is more structured (mean $R^2 = 0.74$) than CNN forgetting ($R^2 = 0.52$). Third, per-sample forgetting is stochastic across random seeds (Spearman $ρ\approx 0.01$), challenging the assumption that sample difficulty is an intrinsic property. Fourth, class-level forgetting is consistent and semantically interpretable: visually similar species are forgotten most, distinctive ones least. Fifth, a sample's loss after head warmup predicts its long-term decay constant ($ρ= 0.30$ to $0.50$, $p < 10^{-45}$). These findings suggest that architectural diversity in ensembles provides complementary retention coverage, and that curriculum or pruning methods based on per-sample difficulty may not generalize across runs. A spaced repetition sampler built on these decay constants does not outperform random sampling, indicating that static scheduling cannot exploit unstable per-sample signals.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Inter-Layer Hessian Analysis of Neural Networks with DAG Architectures
- **Authors:** Maxim Bolshim, Alexander Kugaevskikh
- **arXiv:** [2604.11639](https://arxiv.org/abs/2604.11639v1) · [pdf](https://arxiv.org/pdf/2604.11639v1)
- **Categories:** cs.LG

### Abstract
> Modern automatic differentiation frameworks (JAX, PyTorch) return the Hessian of the loss function as a monolithic tensor, without exposing the internal structure of inter-layer interactions. This paper presents an analytical formalism that explicitly decomposes the full Hessian into blocks indexed by the DAG of an arbitrary architecture. The canonical decomposition $H = H^{GN} + H^T$ separates the Gauss--Newton component (convex part) from the tensor component (residual curvature responsible for saddle points). For piecewise-linear activations (ReLU), the tensor component of the input Hessian vanishes ($H^{T}_{v,w}\!\equiv\!0$ a.e., $H^f_{v,w}\!=\!H^{GN}_{v,w}\!\succeq\!0$); the full parametric Hessian contains residual terms that do not reduce to the GGN. Building on this decomposition, we introduce diagnostic metrics (inter-layer resonance~$\mathcal{R}$, geometric coupling~$\mathcal{C}$, stable rank~$\mathcal{D}$, GN-Gap) that are estimated stochastically in $O(P)$ time and reveal structural curvature interactions between layers. The theoretical analysis explains exponential decay of resonance in vanilla networks and its preservation under skip connections; empirical validation spans fully connected MLPs (Exp.\,1--5) and convolutional architectures (ResNet-18, ${\sim}11$M~parameters, Exp.\,6). When the architecture reduces to a single node, all definitions collapse to the standard Hessian $\nabla^2_θ\mathcal{L}(θ)\in\mathbb{R}^{p\times p}$.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
