---
layout: post
title: "Daily arXiv Digest — 2026-05-15 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Eradicating Negative Transfer in Multi-Physics Foundation Models via Sparse Mixture-of-Experts Routing
- **Authors:** Ellwil Sharma, Arastu Sharma
- **arXiv:** [2605.15179](https://arxiv.org/abs/2605.15179v1) · [pdf](https://arxiv.org/pdf/2605.15179v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.15179v1))
- **Categories:** cs.LG, cs.AI, physics.comp-ph

### Abstract
> Scaling Scientific Machine Learning (SciML) toward universal foundation models is bottlenecked by negative transfer: the simultaneous co-training of disparate partial differential equation (PDE) regimes can induce gradient conflict, unstable optimization, and plasticity loss in dense neural operators. In particular, broadband open-channel fluid dynamics and boundary-dominated porous media flows impose incompatible spectral and geometric demands on a single dense parameter path. We introduce Shodh-MoE, a sparse-activated latent transformer architecture for multi-physics transport. Shodh-MoE operates on compressed 16^3 physical latents produced by a physics-informed autoencoder with an intra-tokenizer Helmholtz-style velocity parameterization, restricting decoded states to divergence-free velocity manifolds. The model guarantees exact mass conservation, achieving a physically verifiable velocity divergence of ~2.8 x 10^-10 (evaluated post-hoc in FP64) on 128^3 grids. A Top-1 soft-semantic router dynamically assigns localized latent patches to expert subnetworks, enabling specialized parameter paths for distinct physical mechanisms while preserving shared experts for universal symmetries. In a 20,000-step distributed pretraining run over mixed three-dimensional physical tensors, routing telemetry shows autonomous domain bifurcation: held-out validation tokens from the open-channel domain route exclusively to Expert 0, while porous-media tokens route exclusively to Expert 1. The model converges simultaneously across both regimes, achieving latent validation MSEs of 2.46 x 10^-5 and 9.76 x 10^-6, and decoded physical MSEs of 2.48 x 10^-6 and 1.76 x 10^-6. These results support sparse expert routing as a practical architectural mechanism for mitigating multi-physics interference in universal neural operators.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `16^{3}`

* Equation: `16^{3}`
* Symbols: `16`
* Why it matters: This equation represents the size of the physical latents produced by the physics-informed autoencoder. The authors use a 16x16x16 grid to represent the physical space, which is a common choice for simulating fluid dynamics and other physical phenomena.

### Equation 2: `∼ 2.8 × 10^{-10}`

* Equation: `∼ 2.8 × 10^{-10}`
* Symbols: `∼` (approximately equal to), `2.8`, `10^{-10}`
* Why it matters: This equation represents the physically verifiable velocity divergence of the model, which is a measure of the accuracy of the model's simulation. The authors claim that the model achieves a divergence of approximately 2.8 × 10^{-10}, which is a very small value indicating good accuracy.

### Equation 3: `128^{3}`

* Equation: `128^{3}`
* Symbols: `128`
* Why it matters: This equation represents the size of the grid used to evaluate the model's performance. The authors use a 128x128x128 grid to evaluate the model's performance, which is a common choice for simulating complex physical phenomena.

### Equation 4: `2.46 × 10^{-5}`

* Equation: `2.46 × 10^{-5}`
* Symbols: `2.46`, `10^{-5}`
* Why it matters: This equation represents the latent validation MSE (mean squared error) of the model on the held-out validation set. The authors claim that the model achieves a latent validation MSE of 2.46 × 10^{-5}, which is a very small value indicating good performance.

### Equation 5: `9.76 × 10^{-6}`

* Equation: `9.76 × 10^{-6}`
* Symbols: `9.76`, `10^{-6}`
* Why it matters: This equation represents the decoded physical MSE of the model on the held-out validation set. The authors claim that the model achieves a decoded physical MSE of 9.76 × 10^{-6}, which is a very small value indicating good performance.

### Equation 6: `2.48 × 10^{-6}`

* Equation: `2.48 × 10^{-6}`
* Symbols: `2.48`, `10^{-6}`
* Why it matters: This equation represents the decoded physical MSE of the model on the held-out validation set. The authors claim that the model achieves a decoded physical MSE of 2.48 × 10^{-6}, which is a very small value indicating good performance.

### Equation 7: `1.76 × 10^{-6}`

* Equation: `1.76 × 10^{-6}`
* Symbols: `1.76`, `10^{-6}`
* Why it matters: This equation represents the decoded physical MSE of the model on the held-out validation set. The authors claim that the model achieves a decoded physical MSE of 1.76 × 10^{-6}, which is a very small value indicating good performance.

**Method Summary**
================

* The Shodh-MoE architecture combines a physics-informed latent autoencoder with a sparse-activated transformer backbone.
* The design goal is to move physical structure from soft penalties into architectural constraints, then use routing to prevent heterogeneous PDE regimes from competing for the same dense subspace.
* The model uses a sparse-activated transformer backbone to enable specialized parameter paths for distinct physical mechanisms while preserving shared experts for universal symmetries.

**Experimental Overview**
=====================

* Tasks/Datasets: The authors use a mixed pretraining corpus of approximately 61,000 three-dimensional tensors at 128x128x128 resolution.
* Baselines/Comparisons: The authors do not mention any specific baselines or comparisons.
* Main Claimed Findings: The authors claim that the Shodh-MoE model achieves good performance on both open-channel and porous-media domains, with a latent validation MSE of 2.46 × 10^{-5} and 9.76 × 10^{-6} and decoded physical MSE of 2.48 × 10^{-6} and 1.76 × 10^{-6} respectively.

**What to Verify in the PDF**
==========================

* The authors mention that the model guarantees exact mass conservation, but it would be interesting to see the mathematical proof or derivation of this claim.
* The authors also mention that the model achieves a physically verifiable velocity divergence of ∼ 2.8 × 10^{-10}, but it would be interesting to see the derivation of this value and how it is calculated.
* The authors mention that the model converges simultaneously across both regimes, but it would be interesting to see the detailed convergence plot or analysis to understand the dynamics of the model's training process.
{% endraw %}

{% raw %}
## 2) Evidential Reasoning Advances Interpretable Real-World Disease Screening
- **Authors:** Chenyu Lian, Hong-Yu Zhou, Jing Qin
- **arXiv:** [2605.15171](https://arxiv.org/abs/2605.15171v1) · [pdf](https://arxiv.org/pdf/2605.15171v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.15171v1))
- **Categories:** cs.CV, cs.AI, cs.LG

### Abstract
> Disease screening is critical for early detection and timely intervention in clinical practice. However, most current screening models for medical images suffer from limited interpretability and suboptimal performance. They often lack effective mechanisms to reference historical cases or provide transparent reasoning pathways. To address these challenges, we introduce EviScreen, an evidential reasoning framework for disease screening that leverages region-level evidence from historical cases. The proposed EviScreen offers retrospection interpretability through regional evidence retrieved from dual knowledge banks. Using this evidential mechanism, the subsequent evidence-aware reasoning module makes predictions using both the current case and evidence from historical cases, thereby enhancing disease screening performance. Furthermore, rather than relying on post-hoc saliency maps, EviScreen enhances localization interpretability by leveraging abnormality maps derived from contrastive retrieval. Our method achieves superior performance on our carefully established benchmarks for real-world disease screening, yielding notably higher specificity at clinical-level recall. Code is publicly available at https://github.com/DopamineLcy/EviScreen.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{K}_{N}$

* Equation: $\mathcal{K}_{N}$
* Symbols: $\mathcal{K}_{N}$ (unknown)
* Why it matters: This equation is not explicitly defined in the provided context, but it seems to represent some kind of knowledge bank or feature extraction mechanism for normal cases.

### Equation 2: $\mathcal{K}_{P}$

* Equation: $\mathcal{K}_{P}$
* Symbols: $\mathcal{K}_{P}$ (unknown)
* Why it matters: Similar to Equation 1, this equation represents some kind of knowledge bank or feature extraction mechanism for pathological cases.

### Equation 3: $\mathbf{x}$

* Equation: $\mathbf{x}$
* Symbols: $\mathbf{x}$ (input features)
* Why it matters: This equation represents the input features to the EviScreen model.

### Equation 4: $\mathbf{E}_{N}$

* Equation: $\mathbf{E}_{N}$
* Symbols: $\mathbf{E}_{N}$ (evidence for normal cases)
* Why it matters: This equation represents the evidence retrieved from the dual knowledge bank for normal cases.

### Equation 5: $\mathbf{E}_{P}$

* Equation: $\mathbf{E}_{P}$
* Symbols: $\mathbf{E}_{P}$ (evidence for pathological cases)
* Why it matters: This equation represents the evidence retrieved from the dual knowledge bank for pathological cases.

### Equation 6: $\mathbf{M}_{N}$

* Equation: $\mathbf{M}_{N}$
* Symbols: $\mathbf{M}_{N}$ (normal case features)
* Why it matters: This equation represents the features extracted from normal cases.

### Equation 7: $\mathbf{M}_{P}$

* Equation: $\mathbf{M}_{P}$
* Symbols: $\mathbf{M}_{P}$ (pathological case features)
* Why it matters: This equation represents the features extracted from pathological cases.

### Equation 8: $\mathbf{M}$

* Equation: $\mathbf{M}$
* Symbols: $\mathbf{M}$ (final output)
* Why it matters: This equation represents the final output of the EviScreen model.

**Method Summary**
==================

* The EviScreen framework consists of two stages: dual knowledge bank construction and evidential reasoning.
* The dual knowledge bank construction stage extracts intermediate regional features from historical normal and pathological cases using a pretrained foundation model.
* The evidential reasoning stage retrieves evidence from the dual knowledge banks and performs cross-attention and self-attention to enable interpretable disease screening.
* The framework also includes a contrastive retrieval mechanism for training-free disease screening.

**Experimental Overview**
========================

* Tasks: Real-world disease screening across three medical domains (ophthalmology, radiology, and dermatology).
* Datasets: Ten public datasets spanning three modalities (color fundus photography, chest X-rays, and dermoscopic images).
* Baselines: Various state-of-the-art methods, including direct prediction, deviation-based anomaly detection, supervised variants, and a prototype-based interpretable method.
* Main claimed findings: EviScreen outperforms various approaches for real-world disease screening, achieving the highest AUROC, AP, Spe@X%R, and CSR across all datasets.

**What to Verify in the PDF**
=============================

* The implementation details of the contrastive retrieval mechanism.
* The evaluation metrics used to assess the performance of the EviScreen model.
* The clinical significance of the results and how they relate to real-world disease screening.
{% endraw %}

{% raw %}
## 3) Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment
- **Authors:** Sayantan Kumar, Shahriar Noroozizadeh, Juyong Kim, Jeremy C. Weiss
- **arXiv:** [2605.15168](https://arxiv.org/abs/2605.15168v1) · [pdf](https://arxiv.org/pdf/2605.15168v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.15168v1))
- **Categories:** cs.CL, cs.AI, cs.LG, stat.ML

### Abstract
> Reconstructing precise clinical timelines is essential for modeling patient trajectories and forecasting risk in complex, heterogeneous conditions like sepsis. While unstructured clinical narratives offer semantically rich and contextually complete descriptions of a patient's course, they often lack temporal precision and contain ambiguous event timing. Conversely, structured electronic health record (EHR) data provides precise temporal anchors but misses a substantial portion of clinically meaningful events. We introduce a retrieval-augmented multimodal alignment framework that bridges this gap to improve the temporal precision of absolute clinical timelines extracted from text. Our approach formulates timeline reconstruction as a graph-based multistep process: it first extracts central anchor events from narratives to build an initial temporal scaffold, places non-central events relative to this backbone, and then calibrates the timeline using retrieved structured EHR rows as external temporal evidence. Evaluated using instruction-tuned large language models on the i2m4 benchmark spanning MIMIC-III and MIMIC-IV, our multimodal pipeline consistently improves absolute timestamp accuracy (AULTC) and improves temporal concordance across nearly all evaluated models over unimodal text-only reconstruction, without compromising event match rates. Furthermore, our empirical gap analysis reveals that 34.8% of text-derived events are entirely absent from tabular records, demonstrating that aligning these modalities can produce a more temporally faithful and clinically informative reconstruction of patient trajectories than either source alone.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
===============

### Equation 1: S = {(e1, t1), (e2, t2), ..., (en, tn)}

* Equation: S = {(e1, t1), (e2, t2), ..., (en, tn)}
* Symbols:
	+ S: A set of tuples containing clinical events and their timestamps
	+ e_i: A clinical event
	+ t_i: The timestamp of the clinical event in hours relative to a case-specific reference time
* Why it matters: This equation defines the set of clinical events and their timestamps, which is used to reconstruct the clinical timeline.

### Equation 2: ei ∈ ℝ

* Equation: ei ∈ ℝ
* Symbols:
	+ ei: A clinical event
	+ ℝ: The set of real numbers
* Why it matters: This equation specifies that each clinical event is represented as a real number, which is used to assign a timestamp to each event.

### Equation 3: ti ∈ ℝ

* Equation: ti ∈ ℝ
* Symbols:
	+ ti: The timestamp of a clinical event in hours relative to a case-specific reference time
	+ ℝ: The set of real numbers
* Why it matters: This equation specifies that the timestamp of each clinical event is a real number, which is used to measure the time difference between events.

### Equation 4: R = {rm}m=1M

* Equation: R = {rm}m=1M
* Symbols:
	+ R: A set of structured EHR rows
	+ rm: A structured EHR row
	+ m: The index of the structured EHR row
	+ M: The total number of structured EHR rows
* Why it matters: This equation defines the set of structured EHR rows, which are used to provide temporal evidence for the clinical timeline.

### Equation 5: rm = (νm, xm, sm)

* Equation: rm = (νm, xm, sm)
* Symbols:
	+ rm: A structured EHR row
	+ νm: The clinical event associated with the structured EHR row
	+ xm: The timestamp of the clinical event in hours relative to a case-specific reference time
	+ sm: The semantic meaning of the clinical event
* Why it matters: This equation defines the components of a structured EHR row, which are used to represent the clinical event and its timestamp.

**Method Summary**
===============

* The proposed method uses a retrieval-augmented multimodal alignment framework to reconstruct clinical timelines from clinical text and structured EHR data.
* The method consists of three main steps:
	+ Extracting central anchor events from clinical text to build an initial temporal scaffold.
	+ Placing non-central events relative to the anchor events.
	+ Calibrating the timeline using retrieved structured EHR rows as external temporal evidence.
* The method uses a combination of natural language processing (NLP) and machine learning techniques to improve the accuracy and temporal precision of the reconstructed clinical timeline.

**Experimental Overview**
=====================

* **Tasks/Datasets**: The proposed method is evaluated on the i2m4 benchmark, which consists of clinical text and structured EHR data from the MIMIC-III and MIMIC-IV datasets.
* **Baselines/Comparisons**: The method is compared to unimodal text-only reconstruction and single-step multimodal reconstruction.
* **Main Claimed Findings**: The proposed method consistently improves absolute timestamp accuracy (AULTC) and temporal concordance across nearly all evaluated models, while maintaining strong event match rates.

**What to Verify in the PDF**
==========================

* The evaluation metrics used to measure the performance of the proposed method, including AULTC and temporal concordance.
* The details of the retrieval-augmented scoring system used to assess semantic adequacy.
* The results of the sensitivity analysis across gold-standard variants, including the original released annotations and the rule-based cleaned version.
{% endraw %}

{% raw %}
## 4) When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability
- **Authors:** ML Nissen Gonzalez, Melwina Albuquerque, Laurence Wroe, Jacob Meyer Cohen, Logan Riggs Smith, Thomas Dooms
- **arXiv:** [2605.15183](https://arxiv.org/abs/2605.15183v1) · [pdf](https://arxiv.org/pdf/2605.15183v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.15183v1))
- **Categories:** cs.LG

### Abstract
> Mechanistic interpretability aims to break models into meaningful parts; verifying that two such parts implement the same computation is a prerequisite. Existing similarity measures evaluate either empirical behaviour, leaving them blind to out-of-distribution mechanisms, or basis-dependent parameters, meaning they disregard weight-space symmetries. To address these issues for the class of tensor-based models, we introduce a weight-based metric, tensor similarity, that is invariant to such symmetries. This metric captures global functional equivalence and accounts for cross-layer mechanisms using an efficient recursive algorithm. Empirically, tensor similarity tracks functional training dynamics, such as grokking and backdoor insertion, with higher fidelity than existing metrics. This reduces measuring similarity and verifying faithfulness into a solved algebraic problem rather than one of empirical approximation.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\Delta$
* Equation: $\Delta$
* Symbols: $\Delta$, $\mathcal{N}(0,\mathbf{I})$
* Why it matters: This equation is not explicitly defined in the provided context, but it seems to represent a difference or a change in some quantity.

### Equation 2: $L^{2}(\mathcal{N}(0,\mathbf{I}))$
* Equation: $L^{2}(\mathcal{N}(0,\mathbf{I}))$
* Symbols: $L$, $\mathcal{N}(0,\mathbf{I})$
* Why it matters: This equation is related to the Gaussian metric, which is used to measure similarity between two networks. The notation $\mathcal{N}(0,\mathbf{I})$ represents a multivariate normal distribution with mean 0 and identity covariance matrix.

### Equation 3: $\tilde{\mathbf{x}} = (1, \mathbf{x}) \in \mathbb{R}^{d+1}$
* Equation: $\tilde{\mathbf{x}} = (1, \mathbf{x})$
* Symbols: $\tilde{\mathbf{x}}$, $\mathbf{x}$, $d$
* Why it matters: This equation defines a new vector $\tilde{\mathbf{x}}$ by concatenating a 1 with the original vector $\mathbf{x}$, effectively increasing its dimension by 1.

### Equation 4: $\mathbb{R}^{K}$
* Equation: $\mathbb{R}^{K}$
* Symbols: $\mathbb{R}^{K}$
* Why it matters: This notation represents the set of all real numbers with $K$ dimensions. It is likely used to denote a matrix or a vector space.

### Equation 5: $\mathcal{A}(\mathbf{x}) = \mathbf{D} \bigl((\mathbf{L}\tilde{\mathbf{x}}) \odot (\mathbf{R}\tilde{\mathbf{x}})\bigr)$
* Equation: $\mathcal{A}(\mathbf{x}) = \mathbf{D} \bigl((\mathbf{L}\tilde{\mathbf{x}}) \odot (\mathbf{R}\tilde{\mathbf{x}})\bigr)$
* Symbols: $\mathcal{A}(\mathbf{x})$, $\mathbf{D}$, $\mathbf{L}$, $\mathbf{R}$, $\tilde{\mathbf{x}}$, $\odot$
* Why it matters: This equation defines a function $\mathcal{A}(\mathbf{x})$ that takes an input $\mathbf{x}$ and applies a transformation involving matrices $\mathbf{L}$, $\mathbf{R}$, and $\mathbf{D}$. The $\odot$ symbol represents the element-wise product.

**Method Summary**
==================

* The authors introduce a weight-based metric, tensor similarity, to measure the similarity between two networks.
* The metric is invariant to symmetries in the weight space and captures global functional equivalence.
* The authors use a recursive algorithm to compute the tensor similarity.
* The method is applied to various tasks, including catastrophic forgetting, grokking, and backdoor injection.

**Experimental Overview**
========================

* The authors evaluate the tensor similarity metric on four tasks:
	+ Catastrophic forgetting on SVHN
	+ Grokking on modular addition
	+ Backdoor injection on SVHN
	+ Scaling to language models (a two-layer bilinear attention transformer on The Pile)
* The authors compare the tensor similarity metric with existing similarity measures and demonstrate its ability to track functional changes in the network.

**What to Verify in the PDF**
=============================

* The derivation of the Gram recursion and its symmetrisation compatibility
* The derivation of the Gaussian metric and its expected output similarity
* The experimental setup and results for the additional plots mentioned in the appendix
{% endraw %}

{% raw %}
## 5) RoSHAP: A Distributional Framework and Robust Metric for Stable Feature Attribution
- **Authors:** Lanxin Xiang, Liang Shi, Youhui Ye, Boyu Jiang, Dawei Zhou, Feng Guo
- **arXiv:** [2605.15154](https://arxiv.org/abs/2605.15154v1) · [pdf](https://arxiv.org/pdf/2605.15154v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.15154v1))
- **Categories:** stat.ML, cs.LG

### Abstract
> Feature attribution analysis is critical for interpreting machine learning models and supporting reliable data-driven decisions. However, feature attribution measures often exhibit stochastic variation: different train--test splits, random seeds, or model-fitting procedures can produce substantially different attribution values and feature rankings. This paper proposes a framework for incorporating stochastic nature of feature attribution and a robust attribution metric, RoSHAP, for stable feature ranking based on the SHAP metric. The proposed framework models the distribution of feature attribution scores and estimates it through bootstrap resampling and kernel density estimation. We show that, under mild regularity conditions, the aggregated feature attribution score is asymptotically Gaussian, which greatly reduces the computational cost of distribution estimation. The RoSHAP summarizes the distribution of SHAP into a robust feature-ranking criterion that simultaneously rewards features that are active, strong, and stable. Through simulations and real-data experiments, the proposed framework and RoSHAP outperform standard single-run attribution measures in identifying signal features. In addition, models built using RoSHAP-selected features achieve predictive performance comparable to full-feature models while using substantially fewer predictors. The proposed RoSHAP approach improves the stability and interpretability of machine learning models, enabling reliable and consistent insights for analysis.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{D}$

* Equation: $\mathcal{D}$
* Symbols: $\mathcal{D}$ (distribution of feature attribution scores)
* Why it matters: This equation represents the distribution of feature attribution scores, which is the foundation of the RoSHAP framework.

### Equation 2: $b=1,\ldots,B$

* Equation: $b=1,\ldots,B$
* Symbols: $b$ (bootstrap index), $B$ (number of bootstrap runs)
* Why it matters: This equation defines the range of bootstrap indices used to estimate the distribution of feature attribution scores.

### Equation 3: $\mathcal{D}^{(b)}_{\mathrm{train}}$

* Equation: $\mathcal{D}^{(b)}_{\mathrm{train}}$
* Symbols: $\mathcal{D}^{(b)}_{\mathrm{train}}$ (training set for bootstrap index $b$)
* Why it matters: This equation represents the training set used to estimate the distribution of feature attribution scores for a specific bootstrap index.

### Equation 4: $\mathcal{D}^{(b)}_{\mathrm{oob}}=\mathcal{D}\setminus\mathcal{D}^{(b)}_{\mathrm{train}}$

* Equation: $\mathcal{D}^{(b)}_{\mathrm{oob}}=\mathcal{D}\setminus\mathcal{D}^{(b)}_{\mathrm{train}}$
* Symbols: $\mathcal{D}^{(b)}_{\mathrm{oob}}$ (out-of-bag set for bootstrap index $b$), $\mathcal{D}$ (original dataset)
* Why it matters: This equation represents the out-of-bag set used to estimate the distribution of feature attribution scores for a specific bootstrap index.

### Equation 5: $\hat{f}^{(b)}$

* Equation: $\hat{f}^{(b)}$
* Symbols: $\hat{f}^{(b)}$ (model trained on bootstrap index $b$)
* Why it matters: This equation represents the model trained on a specific bootstrap index, which is used to estimate the distribution of feature attribution scores.

**Method Summary**
==================

* The RoSHAP framework models the distribution of feature attribution scores using bootstrapping and kernel density estimation.
* The framework estimates the distribution of feature attribution scores and uses it to rank features based on their stability and signal.
* The RoSHAP metric jointly accounts for inactivity, signal, and noise level in feature attribution.
* The framework is robust to stochastic variation in feature attribution measures.

**Experimental Overview**
=========================

* Tasks:
	+ Binary classification
	+ High-dimensional small-sample classification
	+ Moderate-sized high-dimensional molecular classification
	+ High-dimensional regression
	+ 10-class image classification
* Datasets:
	+ Golub dataset
	+ Musk (Version 2) dataset
	+ UJIIndoorLoc dataset
	+ CIFAR-10 dataset
* Baselines/comparisons:
	+ Standard single-run attribution measures
	+ 1000-run bootstrap
	+ 10-run bootstrap
* Main claimed findings:
	+ The RoSHAP framework outperforms standard single-run attribution measures in identifying signal features.
	+ The framework achieves predictive performance comparable to full-feature models while using substantially fewer predictors.
	+ The RoSHAP approach improves the stability and interpretability of machine learning models.

**What to Verify in the PDF**
=============================

* The implementation details of the RoSHAP framework, including the bootstrapping and kernel density estimation procedures.
* The results of the experiments, including the accuracy, F1 score, average precision, and AUC-ROC for classification tasks, and the root mean squared error, mean absolute error, and mean absolute percentage error for regression tasks.
* The feature selection performance of the RoSHAP framework compared to other methods, including information gain, model-based gain, LIME, and SHAP.
{% endraw %}
