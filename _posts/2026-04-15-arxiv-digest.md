---
layout: post
title: "Daily arXiv Digest — 2026-04-15 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Evolution of Optimization Methods: Algorithms, Scenarios, and Evaluations
- **Authors:** Tong Zhang, Jiangning Zhang, Zhucun Xue, Juntao Jiang, Yicheng Xu, Chengming Xu, Teng Hu, Xingyu Xie, Xiaobin Hu, Yabiao Wang, Yong Liu, Shuicheng Yan
- **arXiv:** [2604.12968](https://arxiv.org/abs/2604.12968v1) · [pdf](https://arxiv.org/pdf/2604.12968v1)
- **Categories:** cs.LG, cs.CV

### Abstract
> Balancing convergence speed, generalization capability, and computational efficiency remains a core challenge in deep learning optimization. First-order gradient descent methods, epitomized by stochastic gradient descent (SGD) and Adam, serve as the cornerstone of modern training pipelines. However, large-scale model training, stringent differential privacy requirements, and distributed learning paradigms expose critical limitations in these conventional approaches regarding privacy protection and memory efficiency. To mitigate these bottlenecks, researchers explore second-order optimization techniques to surpass first-order performance ceilings, while zeroth-order methods reemerge to alleviate memory constraints inherent to large-scale training. Despite this proliferation of methodologies, the field lacks a cohesive framework that unifies underlying principles and delineates application scenarios for these disparate approaches. In this work, we retrospectively analyze the evolutionary trajectory of deep learning optimization algorithms and present a comprehensive empirical evaluation of mainstream optimizers across diverse model architectures and training scenarios. We distill key emerging trends and fundamental design trade-offs, pinpointing promising directions for future research. By synthesizing theoretical insights with extensive empirical evidence, we provide actionable guidance for designing next-generation highly efficient, robust, and trustworthy optimization methods. The code is available at https://github.com/APRIL-AIGC/Awesome-Optimizer.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Classical and Quantum Speedups for Non-Convex Optimization via Energy Conserving Descent
- **Authors:** Yihang Sun, Huaijin Wang, Patrick Hayden, Jose Blanchet
- **arXiv:** [2604.13022](https://arxiv.org/abs/2604.13022v1) · [pdf](https://arxiv.org/pdf/2604.13022v1)
- **Categories:** quant-ph, cs.LG, math.OC, stat.ML

### Abstract
> The Energy Conserving Descent (ECD) algorithm was recently proposed (De Luca & Silverstein, 2022) as a global non-convex optimization method. Unlike gradient descent, appropriately configured ECD dynamics escape strict local minima and converge to a global minimum, making it appealing for machine learning optimization. We present the first analytical study of ECD, focusing on the one-dimensional setting for this first installment. We formalize a stochastic ECD dynamics (sECD) with energy-preserving noise, as well as a quantum analog of the ECD Hamiltonian (qECD), providing the foundation for a quantum algorithm through Hamiltonian simulation. For positive double-well objectives, we compute the expected hitting time from a local to the global minimum. We prove that both sECD and qECD yield exponential speedup over respective gradient descent baselines--stochastic gradient descent and its quantization. For objectives with tall barriers, qECD achieves a further speedup over sECD.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Finite-Time Optimization via Scaled Gradient-Momentum Flows
- **Authors:** Yu Zhou, Mengmou Li, Masaaki Nagahara
- **arXiv:** [2604.12751](https://arxiv.org/abs/2604.12751v1) · [pdf](https://arxiv.org/pdf/2604.12751v1)
- **Categories:** math.OC, eess.SY

### Abstract
> In this paper, we develop a scaled gradient-momentum framework for continuous-time optimization that achieves global finite-time convergence. A state-dependent scaling mechanism is introduced to enable classical dynamics, such as Heavy-Ball-type and proportional-integral (PI)-type flows, to attain finite-time convergence. We establish explicit conditions that bridge the gradient-dominance property of the objective function and finite-time stability of the proposed scaled dynamics. Numerical experiments validate the theoretical results.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Monte Carlo Stochastic Depth for Uncertainty Estimation in Deep Learning
- **Authors:** Adam T. Müller, Tobias Rögelein, Nicolaj C. Stache
- **arXiv:** [2604.12719](https://arxiv.org/abs/2604.12719v1) · [pdf](https://arxiv.org/pdf/2604.12719v1)
- **Categories:** cs.LG, stat.ML

### Abstract
> The deployment of deep neural networks in safety-critical systems necessitates reliable and efficient uncertainty quantification (UQ). A practical and widespread strategy for UQ is repurposing stochastic regularizers as scalable approximate Bayesian inference methods, such as Monte Carlo Dropout (MCD) and MC-DropBlock (MCDB). However, this paradigm remains under-explored for Stochastic Depth (SD), a regularizer integral to the residual-based backbones of most modern architectures. While prior work demonstrated its empirical promise for segmentation, a formal theoretical connection to Bayesian variational inference and a benchmark on complex, multi-task problems like object detection are missing. In this paper, we first provide theoretical insights connecting Monte Carlo Stochastic Depth (MCSD) to principled approximate variational inference. We then present the first comprehensive empirical benchmark of MCSD against MCD and MCDB on state-of-the-art detectors (YOLO, RT-DETR) using the COCO and COCO-O datasets. Our results position MCSD as a robust and computationally efficient method that achieves highly competitive predictive accuracy (mAP), notably yielding slight improvements in calibration (ECE) and uncertainty ranking (AUARC) compared to MCD. We thus establish MCSD as a theoretically-grounded and empirically-validated tool for efficient Bayesian approximation in modern deep learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Bilevel Late Acceptance Hill Climbing for the Electric Capacitated Vehicle Routing Problem
- **Authors:** Yinghao Qin, Mosab Bazargani, Edmund K. Burke, Carlos A. Coello Coello, Zhongmin Song, Jun Chen
- **arXiv:** [2604.13013](https://arxiv.org/abs/2604.13013v1) · [pdf](https://arxiv.org/pdf/2604.13013v1)
- **Categories:** cs.AI, math.OC

### Abstract
> This paper tackles the Electric Capacitated Vehicle Routing Problem (E-CVRP) through a bilevel optimization framework that handles routing and charging decisions separately or jointly depending on the search stage. By analyzing their interaction, we introduce a surrogate objective at the upper level to guide the search and accelerate convergence. A bilevel Late Acceptance Hill Climbing algorithm (b-LAHC) is introduced that operates through three phases: greedy descent, neighborhood exploration, and final solution refinement. b-LAHC operates with fixed parameters, eliminating the need for complex adaptation while remaining lightweight and effective. Extensive experiments on the IEEE WCCI-2020 benchmark show that b-LAHC achieves superior or competitive performance against eight state-of-the-art algorithms. Under a fixed evaluation budget, it attains near-optimal solutions on small-scale instances and sets 9/10 new best-known results on large-scale benchmarks, improving existing records by an average of 1.07%. Moreover, the strong correlation (though not universal) observed between the surrogate objective and the complete cost justifies the use of the surrogate objective while still necessitating a joint solution of both levels, thereby validating the effectiveness of the proposed bilevel framework and highlighting its potential for efficiently solving large-scale routing problems with a hierarchical structure.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
