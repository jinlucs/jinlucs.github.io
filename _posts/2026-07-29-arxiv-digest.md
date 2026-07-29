---
layout: post
title: "Daily arXiv Digest — 2026-07-29 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance
- **Authors:** Gaspard Lambrechts, Adrien Bolland, Daniel Ebi, Damien Ernst
- **arXiv:** [2607.26040](https://arxiv.org/abs/2607.26040v1) · [pdf](https://arxiv.org/pdf/2607.26040v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, stat.ML

### Abstract
> Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to learn better representations and behaviors has been the focus of asymmetric reinforcement learning. This learning paradigm has proven effective under partial observability when additional state information is available, but also under full observability when more refined state information is available. Focusing on model-based reinforcement learning, we study the effect of asymmetric learning on observation representations and on privileged information representations. First, we identify a limitation in the privileged information representations learned by an asymmetric model-based algorithm known as the Informed Dreamer. Then, we propose a novel asymmetric representation learning objective using latent guidance, resulting in a new algorithm called the Reinformed Dreamer. Experiments across several benchmarks show a more consistent improvement over Dreamer than previous asymmetric approaches.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
Unfortunately, the extracted context does not provide any formulas to explain.

### Method Summary
* The authors propose a novel asymmetric representation learning objective using latent guidance, resulting in a new algorithm called the Reinformed Dreamer.
* The Reinformed Dreamer algorithm is designed to learn better representations and behaviors by leveraging additional information during training.
* The authors identify a limitation in the privileged information representations learned by an asymmetric model-based algorithm known as the Informed Dreamer.
* The Reinformed Dreamer algorithm is compared to previous asymmetric approaches, showing a more consistent improvement.
* The authors study the effect of asymmetric learning on observation representations and on privileged information representations.

### Experimental Overview
* Tasks/Datasets: Not found in extracted context.
* Baselines/Comparisons: The authors compare the Reinformed Dreamer algorithm to previous asymmetric approaches, including the Informed Dreamer algorithm.
* Main Claimed Findings: The Reinformed Dreamer algorithm shows a more consistent improvement over previous asymmetric approaches.

### What to Verify in the PDF
* The specific tasks and datasets used in the experiments.
* The details of the Informed Dreamer algorithm and its limitations.
* The experimental results and hyperparameters used to train the Reinformed Dreamer algorithm.
{% endraw %}

{% raw %}
## 2) Optimization under Persistent State-Dependent Bias: Gradient-based Method and Complexity Analysis
- **Authors:** Zhaoxian Wu, Quan Xiao, Tayfun Gokmen, Tianyi Chen
- **arXiv:** [2607.26032](https://arxiv.org/abs/2607.26032v1) · [pdf](https://arxiv.org/pdf/2607.26032v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.26032v1))
- **Categories:** math.OC

### Abstract
> This paper studies the convergence of stochastic gradient descent (SGD) when the implemented updates are subject to a persistent and state-dependent bias, in which the desired update is scaled by response functions component-wise. Our first contribution is to demonstrate that SGD in this setting implicitly optimizes a penalized problem whose minimizer does not coincide with the true minimizer. To mitigate this convergence failure, we reformulate the original task as an equivalent bilevel optimization problem and propose a gradient-based algorithm, termed Residual Learning. Theoretical analysis shows that Residual Learning finds a solution to the original, unbiased optimization problem despite the hardware imperfections. Beyond exact convergence, we quantify how the response functions affect convergence complexity via the hardware condition number and show that a polynomial dependence on it is unavoidable in general, via a construction of a hard instance. The theoretical results are supported by numerical simulations that demonstrate the effectiveness of the proposed algorithm.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1) Formula walkthrough**
### Equation 1: f(\,\cdot\,) :{\mathbb{R}}^{D}\to{\mathbb{R}}
* Equation: f(\,\cdot\,) :{\mathbb{R}}^{D}\to{\mathbb{R}}
* Symbols: f, \,\cdot\, (dot), {\mathbb{R}}^{D} (D-dimensional real space)
* Why it matters: This equation defines the function f, which is the objective function that we want to optimize.

### Equation 2: W\in{\mathbb{R}}^{D}
* Equation: W\in{\mathbb{R}}^{D}
* Symbols: W, {\mathbb{R}}^{D} (D-dimensional real space)
* Why it matters: This equation defines the variable W, which is the parameter that we want to optimize.

### Equation 3: \displaystyle({\mathcal{P}}):~~W^{*}=\operatornamewithlimits{arg\,min}_{W\in{\mathbb{R}}^{D}}~f(W):={\mathbb{E}}_{\xi}[f(W;\xi)]
* Equation: \displaystyle({\mathcal{P}}):~~W^{*}=\operatornamewithlimits{arg\,min}_{W\in{\mathbb{R}}^{D}}~f(W):={\mathbb{E}}_{\xi}[f(W;\xi)]
* Symbols: {\mathcal{P}}, W^{*}, f, {\mathbb{E}}_{\xi} (expectation over \xi)
* Why it matters: This equation defines the problem {\mathcal{P}}, which is to find the optimal solution W^{*} that minimizes the expected value of f(W;\xi) over \xi.

### Equation 4: \nabla f(W_{k};\xi_{k})
* Equation: \nabla f(W_{k};\xi_{k})
* Symbols: \nabla, f, W_{k}, \xi_{k} (stochastic gradient)
* Why it matters: This equation defines the stochastic gradient of f at W_{k} with respect to \xi_{k}.

### Equation 5: W_{k}
* Equation: W_{k}
* Symbols: W_{k} (iteration of W)
* Why it matters: This equation defines the current estimate of W at iteration k.

**2) Method summary**
* The paper proposes a gradient-based algorithm called Residual Learning to optimize under persistent state-dependent bias.
* The algorithm reformulates the original task as an equivalent bilevel optimization problem and uses a gradient-based approach to find the optimal solution.
* The paper also analyzes the convergence properties and optimization difficulty introduced by state-dependent bias.

**3) Experimental overview**
* Tasks/Datasets: CIFAR10 and CIFAR100 datasets
* Baselines/Comparisons: Digital SGD (analog training) and Residual Learning
* Main claimed findings: Residual Learning achieves a great accuracy gain from increasing the mixing coefficient γ, and the performance is robust to the γ selection.

**4) What to verify in the PDF**
* The mathematical proof of the convergence of Residual Learning in Section 4.
* The detailed analysis of the objective landscape and noise distribution in Section 4.
* The experimental results and analysis of the CIFAR10 and CIFAR100 datasets in Section 5.
{% endraw %}

{% raw %}
## 3) Parallel Decoding Distillation for Fast Image and Video Generation
- **Authors:** Neta Shaul, Chao Liu, Arash Vahdat, Julius Berner
- **arXiv:** [2607.26004](https://arxiv.org/abs/2607.26004v1) · [pdf](https://arxiv.org/pdf/2607.26004v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.26004v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process. Current state-of-the-art (SOTA) acceleration methods heavily rely on variational score distillation (VSD) and adversarial losses to distill diffusion models into few-step generators. Albeit achieving high-quality video generation, these training losses are notoriously hard to optimize and suffer from mode collapse, leading to loss of video diversity and lack of motion. In this paper, we introduce Parallel Decoding Distillation (PDD), a simplified and scalable trajectory-based distillation method for fast inference of diffusion and flow matching models. Our architecture and training procedure are compatible with any pre-trained model and support sampling with a varying number of function evaluations (NFE). PDD accelerates generation by predicting multiple denoising steps per network evaluation. Conceptually, it learns a representation of the mean velocity without regressing its derivative using JVPs or finite-difference approximations. Our method achieves SOTA performance with 4-8 NFE on LTX-2.3 Text-to-Video/Audio, Wan 14B Text-to-Video, and Qwen-Image Text-to-Image. Moreover, PDD presents a significant improvement in generated video diversity.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1. Formula Walkthrough**
### Equation 1: State Space
{\mathcal{X}}
### Symbols: 
- {\mathcal{X}}: State space
- ℝ: Real numbers
- c, h, w: Dimensions of the state space
### Why it matters: Defines the state space for images and videos.

### Equation 2: State Space (Video)
{\mathcal{X}}=\mathbb{R}^{f\times c\times h\times w}
### Symbols: 
- {\mathcal{X}}: State space
- ℝ: Real numbers
- f: Number of frames in the video
- c, h, w: Dimensions of the state space
### Why it matters: Defines the state space for videos.

### Equation 3: State Space (Image)
{\mathcal{X}}=\mathbb{R}^{c\times h\times w}
### Symbols: 
- {\mathcal{X}}: State space
- ℝ: Real numbers
- c, h, w: Dimensions of the state space
### Why it matters: Defines the state space for images.

### Equation 4: Natural Numbers
N,L\in{\mathbb{N}}
### Symbols: 
- N, L: Natural numbers
### Why it matters: Defines the domain of N and L.

### Equation 5: Time-Dependent State
\left(X_{t}\right)_{0\leq t\leq 1}
### Symbols: 
- X_t: Time-dependent state
- t: Time index
- X: State
### Why it matters: Defines the time-dependent state for the model.

**2. Method Summary**
- The authors propose Parallel Decoding Distillation (PDD) for fast image and video generation.
- PDD is a simplified and scalable trajectory-based distillation method that accelerates generation by predicting multiple denoising steps per network evaluation.
- The method is compatible with any pre-trained model and supports sampling with a varying number of function evaluations (NFE).
- PDD achieves state-of-the-art performance with 4-8 NFE on various tasks.

**3. Experimental Overview**
- The authors evaluate PDD on three tasks: class-conditional image generation, text-to-image generation, and text-to-video generation.
- The tasks are performed on the ImageNet-256, Qwen-Image, Wan2.1, and LTX-2.3 datasets.
- The authors compare PDD with the DMD2 (Lightning-v2) baseline.

**4. What to Verify in the PDF**
- The authors claim that PDD achieves state-of-the-art performance with 4-8 NFE on various tasks. Verify the results for each task and dataset.
- The authors mention that PDD is compatible with any pre-trained model. Verify that the authors have used the same pre-trained models for all tasks and datasets.
- The authors propose a new distillation method, but the paper does not provide a detailed analysis of the existing methods. Verify that the authors have compared PDD with the existing state-of-the-art methods.
{% endraw %}

{% raw %}
## 4) Sharpness-Aware Minimization and Muon: Robustness under the Spectral Norm
- **Authors:** Wenzhi Zhong, Edward Milsom, Michael Murray
- **arXiv:** [2607.26001](https://arxiv.org/abs/2607.26001v1) · [pdf](https://arxiv.org/pdf/2607.26001v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.26001v1))
- **Categories:** cs.LG, stat.ML

### Abstract
> Sharpness-Aware Minimization (SAM) aims to improve generalization by encouraging insensitivity to small, worst-case parameter perturbations. However, the notion of a "small" perturbation is inherently geometry-dependent: while existing SAM variants have explored a wide range of choices, a clear perspective on which geometries are most effective in practice remains elusive. Recent work on matrix-aware optimization, particularly the Muon optimizer, suggests that respecting the matrix structure of hidden-layer weights can lead to strong empirical performance. Motivated by this, we study matrix-aware geometry in both stages of SAM: we introduce a layerwise spectral inner perturbation for matrix-valued hidden-layer parameters and combine it with either AdamW/SGDW or Muon in the outer update. Across ImageNet-1K experiments on ViT-Small/16 and ResNet-50, we find that the combination of a spectral inner step with a Muon outer step performs consistently strongly, achieving the best validation accuracy on both models among the evaluated methods.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Θ ≅ ℝ^p
```markdown
Θ ≅ ℝ^p
```
* Symbols: Θ (theta), ℝ^p (real numbers to the power of p)
* Why it matters: This equation defines the parameter space, which is a set of real numbers to the power of p.

### Equation 2: ∥ ⋅ ∥ in
```markdown
∥ ⋅ ∥ in
```
* Symbols: ∥ ⋅ ∥ (norm), in (inner product)
* Why it matters: This equation defines a norm on the parameter space, which is used to measure the distance between two parameters.

### Equation 3: Θ
```markdown
Θ
```
* Symbols: Θ (theta)
* Why it matters: This equation is a placeholder for the parameter vector, which is a vector of real numbers.

### Equation 4: L: Θ → ℝ ≥ 0
```markdown
L: Θ → ℝ ≥ 0
```
* Symbols: L (loss function), Θ (parameter space), ℝ ≥ 0 (non-negative real numbers)
* Why it matters: This equation defines the loss function, which is a function that takes a parameter vector as input and returns a non-negative real number.

### Equation 5: ρ ≥ 0
```markdown
ρ ≥ 0
```
* Symbols: ρ (perturbation size), ≥ 0 (non-negative real numbers)
* Why it matters: This equation defines the perturbation size, which is a non-negative real number that represents the size of the perturbation applied to the parameter vector.

**Method Summary**
==================

* The proposed method combines Sharpness-Aware Minimization (SAM) with a spectral inner perturbation and a Muon outer optimizer.
* The spectral inner perturbation is a layerwise perturbation that takes into account the linear operator structure of the hidden-layer weights.
* The Muon outer optimizer is a matrix-aware optimizer that uses a spectral norm step-size penalty to improve the optimization process.
* The proposed method is evaluated on two common SAM settings: ImageNet-1K classification with a vision transformer and a convolutional neural network.

**Experimental Overview**
========================

* Tasks/Datasets: ImageNet-1K classification, CIFAR-100 diagnostics
* Baselines/Comparisons: AdamW, SGDW, Muon
* Main Claimed Findings:
	+ The proposed method achieves the best validation accuracy on both models among the evaluated methods.
	+ The spectral inner geometry is more effective when paired with a similarly motivated outer step.
	+ The spectral inner geometry more harshly penalizes memorizing the training data.

**What to Verify in the PDF**
=============================

* The implementation details of the proposed method, including the specific hyperparameters used and the training procedure.
* The results of the diagnostic experiments on CIFAR-100, including the sharpness, effective rank, and generalization gap.
* The theoretical justification for the use of the spectral norm step-size penalty in the Muon outer optimizer.
{% endraw %}

{% raw %}
## 5) Empirical Evaluation of Out-Of-Distribution Performance of Tabular Foundation Models
- **Authors:** Malena Loza, David Chushig-Muzo, Eva Milara, Luis Bote-Curiel, Luis Estrada-Petrocelli, Felipe Grijalva
- **arXiv:** [2607.26000](https://arxiv.org/abs/2607.26000v1) · [pdf](https://arxiv.org/pdf/2607.26000v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.26000v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Tabular Foundation Models (TFMs) have emerged as novel approaches for tabular predictive tasks, demonstrating competitive predictive performance to ensemble tree-based models. Most TFMs are trained and evaluated on independent and identically distributed data, but this assumption changes in real-world scenarios due to distribution shifts, which compromise the robustness of models. Limited research has been conducted of TFMs under distribution shifts. We present an empirical evaluation of Out-Of-Distribution (OOD) performance of nine TFMs, spanning diverse pre-training strategies and architectures: TabPFNv2, TabPFNv2.5, TabPFNv2.6, TabPFNv3, TabICL, TabICLv2, Mitra, LimiX and TabFM. Three real-world datasets from the TableShift study were considered (HELOC, Voting, Childhood Lead), covering label, socioeconomic, and geographic shift types. Our results show that all evaluated TFMs degrade systematically under distribution shift regardless of pre-training strategy, with shift gaps ranging from 0.003 to 0.060 depending on shift type. The relationship between in-distribution and OOD predictive performance documented for classical tabular models extends into TFMs. We also identified a scalability gap, as high-performing models demand significant memory and computational resources beyond what standard deployment infrastructure can support. This study extends existing benchmarks for OOD in tabular data, providing evidence to support their adoption in high-stakes domains characterized by structural distribution shifts.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: Δ

* Equation: Δ
* Symbols: Δ (delta)
* Why it matters: The shift gap (Δ) is defined as the difference between ID and OOD performance, where larger positive values indicate greater degradation under shift.

### Equation 2: \approx

* Equation: \approx
* Symbols: ≈ (approximately equal to)
* Why it matters: The equation is used to compare the ID and OOD performance of models, indicating that the gap between the two is substantial.

### Equation 3: Not found in extracted context

### Equation 4: Not found in extracted context

### Equation 5: Not found in extracted context

**Method Summary**
================

* The authors evaluate different Tabular Foundation Models (TFMs) on three datasets from TableShift, covering a range of domains and distribution shift types.
* The datasets considered are HELOC, Childhood Lead, and Voting, each with a different type of shift (label, socioeconomic, and geographic).
* The authors use the default inference configurations of the TFMs without task-specific fine-tuning and employ the default setup in the original papers.
* The evaluation metric is the Area Under the Receiver Operating Characteristic (ROC-AUC) value, which is considered due to the class imbalance present in several datasets.

**Experimental Overview**
=====================

* Tasks/Datasets:
	+ HELOC (financial risk dataset with label shift)
	+ Childhood Lead (health dataset with socioeconomic shift)
	+ Voting (election dataset with geographic shift)
* Baselines/Comparisons:
	+ The authors compare the performance of nine TFMs on the three datasets.
	+ The results are reported for each model-dataset combination, with the shift gap (Δ) calculated as the difference between ID and OOD performance.
* Main Claimed Findings:
	+ All TFMs degrade systematically under distribution shift, regardless of pre-training strategy.
	+ The shift gap varies substantially by dataset and shift type.
	+ Models based on real-world pre-training (TabPFN variants) consistently achieve the highest performance both ID and OOD across all three datasets.

**What to Verify in the PDF**
==========================

* The detailed results for the Voting dataset, which were not reported due to high inference computational cost.
* The specific pre-training strategies and architectures used for each TFM.
* The evaluation of the scalability gap of high-performing models, which demands significant memory and computational resources beyond what standard deployment infrastructure can support.
{% endraw %}
