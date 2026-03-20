---
layout: post
title: "Daily arXiv Digest — 2026-03-20 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Rigorous Error Certification for Neural PDE Solvers: From Empirical Residuals to Solution Guarantees
- **Authors:** Amartya Mukherjee, Maxwell Fitzsimmons, David C. Del Rey Fernández, Jun Liu
- **arXiv:** [2603.19165](https://arxiv.org/abs/2603.19165v1) · [pdf](https://arxiv.org/pdf/2603.19165v1)
- **Categories:** cs.LG, math.AP, math.FA

### Abstract
> Uncertainty quantification for partial differential equations is traditionally grounded in discretization theory, where solution error is controlled via mesh/grid refinement. Physics-informed neural networks fundamentally depart from this paradigm: they approximate solutions by minimizing residual losses at collocation points, introducing new sources of error arising from optimization, sampling, representation, and overfitting. As a result, the generalization error in the solution space remains an open problem. Our main theoretical contribution establishes generalization bounds that connect residual control to solution-space error. We prove that when neural approximations lie in a compact subset of the solution space, vanishing residual error guarantees convergence to the true solution. We derive deterministic and probabilistic convergence results and provide certified generalization bounds translating residual, boundary, and initial errors into explicit solution error guarantees.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Stochastic Virtual Power Plant Dispatch via Temporally Aggregated Distributed Predictive Control with Performance Guarantees
- **Authors:** Luca Santosuosso, Fei Teng, Sonja Wogrin
- **arXiv:** [2603.19106](https://arxiv.org/abs/2603.19106v1) · [pdf](https://arxiv.org/pdf/2603.19106v1)
- **Categories:** math.OC

### Abstract
> This paper addresses the energy dispatch of a virtual power plant comprising renewable generation, energy storage, and thermal units under uncertainty in renewable output, energy prices, and energy demand. The nonlinear dynamics and multiple sources of uncertainty render traditional stochastic model predictive control (MPC) computationally intractable as the dispatch horizon, scenario set, and asset portfolio expand. To overcome this limitation, we propose a novel controller that seamlessly integrates MPC with time series aggregation and distributed optimization, simultaneously reducing the temporal, asset, and scenario dimensions of the problem. The resulting controller provides a rigorous performance guarantee through theoretically validated bounds on its approximation error, while leveraging dual information from previous MPC iterations to adaptively optimize the temporal aggregation. Numerical results show that the proposed controller reduces runtime by over 50% relative to traditional stochastic MPC and, crucially, restores tractability where the full-scale dispatch model proves intractable.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Fast and Interpretable Autoregressive Estimation with Neural Network Backpropagation
- **Authors:** Anaísa Lucena, Ana Martins, Armando J. Pinho, Sónia Gouveia
- **arXiv:** [2603.19041](https://arxiv.org/abs/2603.19041v1) · [pdf](https://arxiv.org/pdf/2603.19041v1)
- **Categories:** stat.ML, cs.LG

### Abstract
> Autoregressive (AR) models remain widely used in time series analysis due to their interpretability, but convencional parameter estimation methods can be computationally expensive and prone to convergence issues. This paper proposes a Neural Network (NN) formulation of AR estimation by embedding the autoregressive structure directly into a feedforward NN, enabling coefficient estimation through backpropagation while preserving interpretability. Simulation experiments on 125,000 synthetic AR(p) time series with short-term dependence (1 <= p <= 5) show that the proposed NN-based method consistently recovers model coefficients for all series, while Conditional Maximum Likelihood (CML) fails to converge in approximately 55% of cases. When both methods converge, estimation accuracy is comparable with negligible differences in relative error, R2 and, perplexity/likelihood. However, when CML fails, the NN-based approach still provides reliable estimates. In all cases, the NN estimator achieves substantial computational gains, reaching a median speedup of 12.6x and up to 34.2x for higher model orders. Overall, results demonstrate that gradient-descent NN optimization can provide a fast and efficient alternative for interpretable AR parameter estimation.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Uniform a priori bounds and error analysis for the Adam stochastic gradient descent optimization method
- **Authors:** Steffen Dereich, Thang Do, Arnulf Jentzen
- **arXiv:** [2603.18899](https://arxiv.org/abs/2603.18899v1) · [pdf](https://arxiv.org/pdf/2603.18899v1)
- **Categories:** cs.LG, math.OC

### Abstract
> The adaptive moment estimation (Adam) optimizer proposed by Kingma & Ba (2014) is presumably the most popular stochastic gradient descent (SGD) optimization method for the training of deep neural networks (DNNs) in artificial intelligence (AI) systems. Despite its groundbreaking success in the training of AI systems, it still remains an open research problem to provide a complete error analysis of Adam, not only for optimizing DNNs but even when applied to strongly convex stochastic optimization problems (SOPs). Previous error analysis results for strongly convex SOPs in the literature provide conditional convergence analyses that rely on the assumption that Adam does not diverge to infinity but remains uniformly bounded. It is the key contribution of this work to establish uniform a priori bounds for Adam and, thereby, to provide -- for the first time -- an unconditional error analysis for Adam for a large class of strongly convex SOPs.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) On Optimizing Multimodal Jailbreaks for Spoken Language Models
- **Authors:** Aravind Krishnan, Karolina Stańczak, Dietrich Klakow
- **arXiv:** [2603.19127](https://arxiv.org/abs/2603.19127v1) · [pdf](https://arxiv.org/pdf/2603.19127v1)
- **Categories:** cs.LG

### Abstract
> As Spoken Language Models (SLMs) integrate speech and text modalities, they inherit the safety vulnerabilities of their LLM backbone and an expanded attack surface. SLMs have been previously shown to be susceptible to jailbreaking, where adversarial prompts induce harmful responses. Yet existing attacks largely remain unimodal, optimizing either text or audio in isolation. We explore gradient-based multimodal jailbreaks by introducing JAMA (Joint Audio-text Multimodal Attack), a joint multimodal optimization framework combining Greedy Coordinate Gradient (GCG) for text and Projected Gradient Descent (PGD) for audio, to simultaneously perturb both modalities. Evaluations across four state-of-the-art SLMs and four audio types demonstrate that JAMA surpasses unimodal jailbreak rate by 1.5x to 10x. We analyze the operational dynamics of this joint attack and show that a sequential approximation method makes it 4x to 6x faster. Our findings suggest that unimodal safety is insufficient for robust SLMs. The code and data are available at https://repos.lsv.uni-saarland.de/akrishnan/multimodal-jailbreak-slm

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
