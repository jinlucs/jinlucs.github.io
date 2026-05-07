---
layout: post
title: "Daily arXiv Digest — 2026-05-07 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Estimating the expected output of wide random MLPs more efficiently than sampling
- **Authors:** Wilson Wu, Victor Lecomte, Michael Winer, George Robinson, Jacob Hilton, Paul Christiano
- **arXiv:** [2605.05179](https://arxiv.org/abs/2605.05179v1) · [pdf](https://arxiv.org/pdf/2605.05179v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cond-mat.dis-nn, stat.ML

### Abstract
> By far the most common way to estimate an expected loss in machine learning is to draw samples, compute the loss on each one, and take the empirical average. However, sampling is not necessarily optimal. Given an MLP at initialization, we show how to estimate its expected output over Gaussian inputs without running samples through the network at all. Instead, we produce approximate representations of the distributions of activations at each layer, leveraging tools such as cumulants and Hermite expansions. We show both theoretically and empirically that for sufficiently wide networks, our estimator achieves a target mean squared error using substantially fewer FLOPs than Monte Carlo sampling. We find moreover that our methods perform particularly well at estimating the probabilities of rare events, and additionally demonstrate how they can be used for model training. Together, these findings suggest a path to producing models with a greatly reduced probability of catastrophic tail risks.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Equation: `E[σ^2] = ∫∫∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫ ∫
{% endraw %}

{% raw %}
## 2) Superposition Is Not Necessary: A Mechanistic Interpretability Analysis of Transformer Representations for Time Series Forecasting
- **Authors:** Alper Yıldırım
- **arXiv:** [2605.05151](https://arxiv.org/abs/2605.05151v1) · [pdf](https://arxiv.org/pdf/2605.05151v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.05151v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Transformer architectures have been widely adopted for time series forecasting, yet whether the representational mechanisms that make them powerful in NLP actually engage on time series data remains unexplored. The persistent competitiveness of simple linear models such as DLinear has fueled ongoing debate, but no mechanistic explanation for this phenomenon has been offered. We address this gap by applying sparse autoencoders (SAEs), a tool from mechanistic interpretability, to probe the internal representations of PatchTST. We first establish that a single-layer, narrow-dimensional transformer matches the forecasting performance of deeper configurations across commonly used benchmarks. We then train SAEs on the post-GELU intermediate FFN activations with dictionary sizes ranging from 0.5x to 4.0x the native dimensionality. Expanding the dictionary yields negligible downstream performance change (average 0.214%), with large portions of overcomplete dictionaries remaining inactive. Targeted causal interventions on dominant latent features produce minimal forecast perturbation. Across all evaluated settings, we observe no empirical evidence that the analyzed FFN representations rely on strong superposition. Instead, the representations remain sparse, stable under aggressive dictionary expansion, and largely insensitive to latent interventions. These results demonstrate that superposition is not necessary for competitive performance on standard forecasting benchmarks, suggesting they may not demand the rich compositional representations that drive transformer success in language modeling, and helping explain the persistent competitiveness of simple linear models
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 0.5 × 0.5 ×

* Equation: `0.5 × 0.5 ×`
* Symbols: `×` (multiplication)
* Why it matters: This equation represents the range of dictionary sizes used in the sparse autoencoder (SAE) analysis. The authors test the impact of expanding the dictionary size on the forecasting performance of the PatchTST model.

### Equation 2: 4.0 × 4.0 ×

* Equation: `4.0 × 4.0 ×`
* Symbols: `×` (multiplication)
* Why it matters: This equation represents the upper limit of the dictionary size used in the SAE analysis. The authors test the impact of expanding the dictionary size to this limit on the forecasting performance of the PatchTST model.

### Equation 3: 0.214%

* Equation: `0.214%`
* Symbols: `%` (percentage)
* Why it matters: This equation represents the average percentage change in test MSE (mean squared error) when expanding the dictionary size from 0.5 × 0.5 × to 4.0 × 4.0 ×. The authors find that expanding the dictionary size has a negligible impact on forecasting performance.

### Equation 4: ≈ 10

* Equation: `≈ 10`
* Symbols: `≈` (approximation)
* Why it matters: This equation represents the activation threshold used to measure dead latent rates in the SAE analysis. The authors track which latents exceed this threshold to determine whether the expanded dictionary capacity is being utilized.

### Equation 5: d_{\text{model}}

* Equation: `d_{\text{model}}`
* Symbols: `d_{\text{model}}` (dimension of the model)
* Why it matters: This equation represents the dimensionality of the model used in the SAE analysis. The authors test the impact of expanding the dictionary size on the forecasting performance of the PatchTST model with different dimensions.

### Equation 6: 2 × d_{\text{model}}

* Equation: `2 × d_{\text{model}}`
* Symbols: `×` (multiplication)
* Why it matters: This equation represents the relationship between the dimensionality of the model and the dictionary size used in the SAE analysis. The authors test the impact of expanding the dictionary size on the forecasting performance of the PatchTST model with different dimensions.

**Method Summary**
================

* The authors use PatchTST as the base forecasting model, with modifications to the original configuration, including:
	+ Replacing learned absolute positional embeddings with Rotary Position Embeddings (RoPE)
	+ Replacing BatchNorm with RMSNorm
* The authors use sparse autoencoders (SAEs) to probe the internal representations of the PatchTST model
* The SAE analysis is performed on the post-GELU intermediate FFN activations with dictionary sizes ranging from 0.5 × 0.5 × to 4.0 × 4.0 ×

**Experimental Overview**
================--------

* Tasks/Datasets: Time series forecasting
* Baselines/Comparisons: PatchTST (Nie et al., 2023)
* Main claimed findings:
	+ A single-layer, narrow-dimensional transformer matches the forecasting performance of deeper configurations
	+ Expanding the dictionary size has a negligible impact on forecasting performance
	+ The representations remain sparse, stable under aggressive dictionary expansion, and largely insensitive to latent interventions

**What to Verify in the PDF**
=============================

* The authors claim that the PatchTST model achieves broadly comparable performance to the published results (Nie et al., 2023) with a minimal configuration. Verify the full forecasting results in the appendix to understand the basis of this claim.
* The authors use a specific activation threshold (≈ 10) to measure dead latent rates. Verify the rationale behind this choice and its impact on the results.
* The authors discuss the implications of their findings for the representational mechanisms employed by the FFN layer. Verify the detailed analysis and conclusions drawn from the SAE analysis.
{% endraw %}

{% raw %}
## 3) Joint Treatment Effect Estimation from Incomplete Healthcare Data: Temporal Causal Normalizing Flows with LLM-driven Evolutionary MNAR Imputation
- **Authors:** Olivia Jullian Parra, Sara Zoccheddu, David Catalan Cerezo, Tom Forzy, Franziska Ulrich, William Sutcliffe, Jakob Martin Burgstaller, Oliver Senn, Patrick Owen, Nicola Serra
- **arXiv:** [2605.05125](https://arxiv.org/abs/2605.05125v1) · [pdf](https://arxiv.org/pdf/2605.05125v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.05125v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Target trial emulation (TTE) enables causal questions to be studied with observational data when randomized controlled trials (RCTs) are infeasible. Yet treatment-effect methods often address causal estimation, missingness, and temporal structure separately, limiting their robustness in electronic health records (EHRs), where time-varying confounding and missing-not-at-random (MNAR) biomarkers can reach 50%--80%. We propose a two-stage pipeline for treatment effect estimation from incomplete longitudinal EHRs. First, CausalFlow-T, a directed acyclic graph (DAG)-constrained normalizing flow with long short-term memory (LSTM)-encoded patient history, performs exact invertible counterfactual inference, avoiding approximation errors from variational inference and separating confounding through explicit causal structure. Ablations on four synthetic and one semi-synthetic benchmark with known counterfactuals show that DAG constraints and exact inference address distinct failure modes: neither compensates for the other. Second, because CausalFlow-T requires completed inputs, we introduce an LLM-driven evolutionary imputer that proposes executable imputation operators rather than individual entries, and evaluate it with three large language model (LLM) backends, including two open-source models. Across 30%--80% MNAR missingness, this imputer achieves the best pooled rank over biomarker and causal metrics, leading in point-wise accuracy and temporal extrapolation while preserving average treatment effect (ATE) recovery as statistical baselines degrade. On Swiss primary-care EHRs from adults with type 2 diabetes initiating a GLP-1 receptor agonist or SGLT-2 inhibitor, the pipeline estimates a per-protocol weight-loss difference of -0.98 kg [95% CI -1.01, -0.96] favoring GLP-1 receptor agonists, consistent with randomized evidence and obtained from realistically incomplete real-world EHRs.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `−0.98`

* Equation: `−0.98`
* Symbols: `−0.98` (a numerical value)
* Why it matters: This is the per-protocol weight-loss difference in favor of GLP-1 receptor agonists, as reported in the paper.

### Equation 2: `95%`

* Equation: `95%`
* Symbols: `%` (percentage sign)
* Why it matters: This is the confidence interval for the per-protocol weight-loss difference, indicating the range of values within which the true effect is likely to lie.

### Equation 3: `-1.01`

* Equation: `-1.01`
* Symbols: `-1.01` (a numerical value)
* Why it matters: This is the lower bound of the confidence interval for the per-protocol weight-loss difference, indicating the minimum value within which the true effect is likely to lie.

### Equation 4: `-0.96`

* Equation: `-0.96`
* Symbols: `-0.96` (a numerical value)
* Why it matters: This is the upper bound of the confidence interval for the per-protocol weight-loss difference, indicating the maximum value within which the true effect is likely to lie.

### Equation 5: `>50%`

* Equation: `>50%`
* Symbols: `%` (percentage sign), `>` (greater than)
* Why it matters: This is the threshold for MNAR missingness, indicating that the probability of a value being unobserved depends on the unobserved value itself, with a value greater than 50% indicating significant missingness.

**Method Summary**
================

* The authors propose a two-stage pipeline for treatment effect estimation from incomplete longitudinal observational data.
* The pipeline consists of a causal normalizing flow (CausalFlow-T) that addresses time-varying confounding and exact counterfactual inference, and an LLM-driven evolutionary imputer that handles MNAR missingness.
* The authors evaluate the pipeline on four synthetic datasets with known counterfactuals and a semi-synthetic dataset built on a real-world EHR backbone.

**Experimental Overview**
================--------

* Tasks:
	+ Evaluate the pipeline on four synthetic datasets with known counterfactuals.
	+ Evaluate the pipeline on a semi-synthetic dataset built on a real-world EHR backbone with MNAR missingness at 30%, 50%, and 80%.
* Baselines:
	+ CVAE (Variational Autoencoder)
	+ GNN-CVAE (Graph Neural Network-based Variational Autoencoder)
	+ TARNet (Temporal Attention-based Autoencoder)
* Main claimed findings:
	+ CausalFlow-T is the only model satisfying all reliability criteria.
	+ LLM-driven imputation achieves the best pooled performance across biomarker and causal metrics.
	+ The full pipeline recovers a robust per-protocol treatment effect from incomplete real-world EHR data.

**What to Verify in the PDF**
=============================

* The authors claim that the LLM-driven evolutionary imputer achieves the best pooled performance across biomarker and causal metrics. Verify that the results are indeed robust across different LLM backends and that the performance is not overly sensitive to hyperparameters.
* The authors report that the pipeline recovers a robust per-protocol treatment effect from incomplete real-world EHR data. Verify that the results are consistent across different datasets and that the pipeline is able to handle complex causal relationships.
* The authors propose a two-stage pipeline that jointly handles MNAR missingness and causal structure across time. Verify that the pipeline is able to handle non-linear relationships between covariates and outcomes, and that it is robust to different levels of missingness.
{% endraw %}

{% raw %}
## 4) On the Wasserstein Gradient Flow Interpretation of Drifting Models
- **Authors:** Arthur Gretton, Li Kevin Wenliang, Alexandre Galashov, James Thornton, Valentin De Bortoli, Arnaud Doucet
- **arXiv:** [2605.05118](https://arxiv.org/abs/2605.05118v1) · [pdf](https://arxiv.org/pdf/2605.05118v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.05118v1))
- **Categories:** cs.LG, cs.AI, stat.ML

### Abstract
> Recently, Deng et al. (2026) proposed Generative Modeling via Drifting (GMD), a novel framework for generative tasks. This note presents an analysis of GMD through the lens of Wasserstein Gradient Flows (WGF), i.e., the path of steepest descent for a functional in the space of probability measures, equipped with the geometry of optimal transport. Unlike previous WGF-based contributions, GMD can be thought of as directly targeting a fixed point of a specific WGF flow. We demonstrate three main results: first, that one algorithm proposed by Deng et al. (2026) corresponds to finding the limiting point of a WGF on the KL divergence, with Parzen smoothing on the densities. Second, that the algorithm actually implemented by Deng et al. (2026) corresponds to a different procedure, which bears some resemblance to the fixed point of a WGF on the Sinkhorn divergence, but lacks certain desirable properties of the latter. Third, the same same idea can be extended to the limiting point of other WGFs, including the Maximum Mean Discrepancy (MMD), the sliced Wasserstein distance, and GAN critic functions.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\mathbb{R}^{d}$
```markdown
* Equation type: Space of probability measures
* Symbols: $\mathbb{R}^{d}$ (d-dimensional Euclidean space)
* Why it matters: Defines the space of probability measures in the context of the paper
```

### Equation 2: $f_{\theta}:\mathbb{R}^{c}\to\mathbb{R}^{d}$
```markdown
* Equation type: Function definition
* Symbols: $f_{\theta}$ (function), $\mathbb{R}^{c}$ (input space), $\mathbb{R}^{d}$ (output space)
* Why it matters: Defines the generator function used in the Generative Modeling via Drifting (GMD) framework
```

### Equation 3: $\epsilon\sim\mu$
```markdown
* Equation type: Probability measure
* Symbols: $\epsilon$ (random variable), $\mu$ (probability measure)
* Why it matters: Represents the noise or perturbation added to the input of the generator function
```

### Equation 4: $\epsilon\sim\mathcal{N}(0,I_{c})$
```markdown
* Equation type: Probability distribution
* Symbols: $\epsilon$ (random variable), $\mathcal{N}(0,I_{c})$ (standard normal distribution with covariance matrix $I_{c}$)
* Why it matters: Specifies the distribution of the noise added to the input of the generator function
```

### Equation 5: $x=f_{\theta}(\epsilon)$
```markdown
* Equation type: Function composition
* Symbols: $x$ (output), $f_{\theta}$ (generator function), $\epsilon$ (input)
* Why it matters: Represents the output of the generator function given the input noise
```

### Equation 6: $q_{\theta}$
```markdown
* Equation type: Probability measure
* Symbols: $q_{\theta}$ (probability measure)
* Why it matters: Represents the target probability measure in the GMD framework
```

### Equation 7: $f_{\theta}(\epsilon)$
```markdown
* Equation type: Function composition
* Symbols: $f_{\theta}$ (generator function), $\epsilon$ (input)
* Why it matters: Same as Equation 5, represents the output of the generator function given the input noise
```

### Equation 8: $\theta$
```markdown
* Equation type: Parameter
* Symbols: $\theta$ (parameter)
* Why it matters: Represents the learnable parameters of the generator function
```

**Method Summary**
================

* The authors analyze the Generative Modeling via Drifting (GMD) framework through the lens of Wasserstein Gradient Flows (WGF).
* They demonstrate three main results:
	+ The algorithm proposed by Deng et al. (2026) corresponds to finding the limiting point of a WGF on the KL divergence with Parzen smoothing.
	+ The algorithm implemented by Deng et al. (2026) corresponds to a different procedure that bears some resemblance to the fixed point of a WGF on the Sinkhorn divergence.
	+ The same idea can be extended to other WGFs, including the Maximum Mean Discrepancy (MMD), the sliced Wasserstein distance, and GAN critic functions.

**Experimental Overview**
================--------

* The authors present experimental results for various toy examples in Figures 3-6.
* The tasks and datasets used are not specified in the provided context.
* The main claimed findings are not explicitly stated in the provided context.

**What to Verify in the PDF**
=============================

* The authors mention the use of the unnormalized Gibbs kernel in the Sinkhorn proxy, but the derivation and implementation details are not provided in the provided context.
* The authors also mention the use of the normalizer in the original algorithm, but the specific formula and implementation details are not provided.
* The authors claim that the velocity field of the Sinkhorn proxy does not correspond to a Wasserstein gradient flow, but the proof and details are not provided in the provided context.
{% endraw %}

{% raw %}
## 5) Unified Framework of Distributional Regret in Multi-Armed Bandits and Reinforcement Learning
- **Authors:** Harin Lee, Min-hwan Oh
- **arXiv:** [2605.05102](https://arxiv.org/abs/2605.05102v1) · [pdf](https://arxiv.org/pdf/2605.05102v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, stat.ML

### Abstract
> We study the distribution of regret in stochastic multi-armed bandits and episodic reinforcement learning through a unified framework. We formalize a distributional regret bound as a probabilistic guarantee that holds uniformly over all confidence levels $δ\in (0,1]$, thereby characterizing the regret distribution across the full range of $δ$. We present a simple UCBVI-style algorithm with exploration bonus $\min\{c_{1,k}/N, c_{2,k}/\sqrt{N}\}$, where $N$ denotes the visit count and $(c_{1,k},c_{2,k})$ are user-specified parameters. For arbitrary parameter sequences, we derive general gap-independent and gap-dependent distributional regret bounds, yielding a principled characterization of how the parameters control the trade-off between expected performance, tail risk, and instance-dependent behavior. In particular, our bounds achieve optimal trade-offs between expected and distributional regret in both minimax and instance-dependent regimes. As a special case, for multi-armed bandits with $A$ arms and horizon $T$, we obtain a distributional regret bound of order $\mathcal{O}(\sqrt{AT}\log(1/δ))$, confirming the conjecture of Lattimore & Szepesvári (2020, Section 17.1) for the first time.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Exploration bonus
```math
\min\{c_{1,k}/N, c_{2,k}/\sqrt{N}\}
```
* Symbols: `c_{1,k}`, `c_{2,k}`, `N`
* Why it matters: This formula defines the exploration bonus used in the UCBVI-style algorithm, which balances exploration and exploitation. The parameters `c_{1,k}` and `c_{2,k}` control the trade-off between these two.

### 2. Distributional regret bound
```math
\mathcal{O}(\sqrt{AT}\log(1/δ))
```
* Symbols: `A`, `T`, `δ`
* Why it matters: This bound characterizes the distributional regret in the context of multi-armed bandits with `A` arms and horizon `T`. The bound is gap-independent and depends on the confidence level `δ`.

### 3. Distributional regret bound (minimax regime)
```math
\mathcal{O}(\sqrt{AT}\log(1/δ))
```
* Symbols: `A`, `T`, `δ`
* Why it matters: This bound is a special case of the previous bound, where the algorithm achieves optimal trade-offs between expected and distributional regret in the minimax regime.

### 4. Distributional regret bound (instance-dependent regime)
```math
\mathcal{O}(\sqrt{AT}\log(1/δ))
```
* Symbols: `A`, `T`, `δ`
* Why it matters: This bound is another special case of the previous bound, where the algorithm achieves optimal trade-offs between expected and distributional regret in the instance-dependent regime.

### 5. Exploration bonus formula
```math
\min\{c_{1,k}/N, c_{2,k}/\sqrt{N}\}
```
* Symbols: `c_{1,k}`, `c_{2,k}`, `N`
* Why it matters: This formula is used to balance exploration and exploitation in the UCBVI-style algorithm. The parameters `c_{1,k}` and `c_{2,k}` control the trade-off between these two.

**Method Summary**
==================

* The authors propose a unified framework for distributional regret in multi-armed bandits and reinforcement learning.
* The framework provides a probabilistic guarantee that holds uniformly over all confidence levels `δ∈ (0,1]`.
* The authors derive general gap-independent and gap-dependent distributional regret bounds for arbitrary parameter sequences.
* The bounds achieve optimal trade-offs between expected performance, tail risk, and instance-dependent behavior.

**Experimental Overview**
=========================

* Tasks/Datasets: Multi-armed bandits with `A` arms and horizon `T`.
* Baselines/Comparisons: The authors compare their algorithm with existing algorithms (not specified in the abstract).
* Main claimed findings:
	+ The algorithm achieves optimal trade-offs between expected and distributional regret in both minimax and instance-dependent regimes.
	+ The distributional regret bound is of order `O(√AT log(1/δ))`.

**What to Verify in the PDF**
==========================

* The authors' derivation of the distributional regret bounds for arbitrary parameter sequences.
* The proof of the optimality of the trade-offs between expected and distributional regret in both minimax and instance-dependent regimes.
* The experimental results that demonstrate the effectiveness of the proposed algorithm.
{% endraw %}
