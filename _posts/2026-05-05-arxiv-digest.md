---
layout: post
title: "Daily arXiv Digest — 2026-05-05 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
- **Authors:** Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
- **arXiv:** [2605.02867](https://arxiv.org/abs/2605.02867v1) · [pdf](https://arxiv.org/pdf/2605.02867v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.02867v1))
- **Categories:** cs.LG, cs.AI, cs.RO

### Abstract
> Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Not found in extracted context.

### Equation 2: Not found in extracted context.

### Equation 3: Not found in extracted context.

### Equation 4: Not found in extracted context.

### Equation 5: 
\[ \mathcal{D}_{S} \]
Matters: This equation represents the set of samples used for training a model.

### Equation 6: 
\[ \bm{\omega}_{S} \]
Matters: This equation represents the parameters of the model used for training.

### Equation 7: 
\[ \mathcal{D}_{T} \]
Matters: This equation represents the set of samples used for testing a model.

### Equation 8: 
\[ \bm{\omega}_{T} \]
Matters: This equation represents the parameters of the model used for testing.

**Method Summary**
================

* The authors propose a framework that uses SHapley Additive exPlanations (SHAP) to evaluate the impact of RL algorithm and hyperparameter configurations on generalization.
* The framework consists of a theoretical foundation, a SHAP-based framework for configuration sampling, model training, and evaluation, and a result analysis and configuration selection guidance.
* The authors introduce two theorems: one on the generalization bound and another on the decomposition of the generalization gap into interpretable contributions.

**Experimental Overview**
========================

* The authors evaluate the proposed framework across four robotic environments (MuJoCo and PyBullet) and four RL algorithms (PPO, A2C, DDPG, SAC).
* The experiments focus on the impact of algorithm and hyperparameter configurations on generalization, as well as the interaction between configurations.
* The authors compare the performance of the proposed framework to baseline methods and claim to achieve improved generalizability.

**What to Verify in the PDF**
==========================

* The implementation details of the SHAP explainer construction and result analysis.
* The theoretical foundation of the generalization bound and its connection to Shapley values.
* The results of the experiments, including the beeswarm plots and the analysis of Shapley values.
{% endraw %}

{% raw %}
## 2) Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring
- **Authors:** Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian
- **arXiv:** [2605.02853](https://arxiv.org/abs/2605.02853v1) · [pdf](https://arxiv.org/pdf/2605.02853v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.02853v1))
- **Categories:** cs.LG

### Abstract
> Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-wise learning quality. This challenge is particularly acute for transformer-based language models, where training is expensive, models are often reused in frozen form, and poorly optimized layers can silently degrade performance. We propose a layer-wise peeling framework for monitoring training dynamics, in which each transformer layer is locally optimized against intermediate representations of the trained model. By constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations, we obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers. Experiments on decoder-only transformer models show that these layer-wise reference bounds can match or even surpass the trained model at various stages of training, exposing inefficiencies that remain hidden in aggregate loss curves. We further demonstrate that this analysis remains effective under binarization and quantized settings, where training dynamics are particularly fragile. Across all numerical results, the proposed bounds consistently separate apparent convergence from effective optimality, highlighting optimization opportunities that are invisible when relying on training loss alone.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathbf{W}_{k}$

* Equation: $\mathbf{W}_{k}$
* Symbols: $\mathbf{W}_{k}$ (weight matrix)
* Why it matters: This equation represents the weight matrix of the k-th layer of the transformer network.

### Equation 2: $\mathbf{b}_{k}$

* Equation: $\mathbf{b}_{k}$
* Symbols: $\mathbf{b}_{k}$ (bias vector)
* Why it matters: This equation represents the bias vector of the k-th layer of the transformer network.

### Equation 3: $k \in [K]$

* Equation: $k \in [K]$
* Symbols: $k$ (layer index), $K$ (number of layers)
* Why it matters: This equation represents the range of layer indices for which the YES framework is applied.

### Equation 4: $\mathbf{X} \in \mathbb{R}^{n \times d}$

* Equation: $\mathbf{X} \in \mathbb{R}^{n \times d}$
* Symbols: $\mathbf{X}$ (input matrix), $n$ (number of rows), $d$ (number of columns)
* Why it matters: This equation represents the input matrix of the transformer network.

### Equation 5: $\mathbf{Y} \in \mathbb{R}^{m \times d}$

* Equation: $\mathbf{Y} \in \mathbb{R}^{m \times d}$
* Symbols: $\mathbf{Y}$ (output matrix), $m$ (number of rows), $d$ (number of columns)
* Why it matters: This equation represents the output matrix of the transformer network.

**Method Summary**
================

* The proposed framework, called YES (Yield Estimation and Sampling), is a layer-wise peeling approach for monitoring training dynamics of transformer networks.
* The framework involves constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations.
* The goal is to obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers.
* The framework is designed to work with transformer networks, which are notoriously difficult to optimize due to their non-convex landscape.

**Experimental Overview**
=====================

* The experiments are conducted on a range of tasks and datasets, including:
	+ WikiText-2 (a large-scale language model)
	+ MNIST (a small-scale classification dataset)
* The proposed framework is compared to the standard training process, and the results show that the YES framework can identify under-optimized layers and improve training performance.
* The experiments demonstrate the effectiveness of the YES framework in various scenarios, including:
	+ Training with different hyperparameters and architectures
	+ Training with and without quantization
	+ Training with and without binarization

**What to Verify in the PDF**
==========================

* The mathematical derivations of the YES framework, particularly the construction of the reference solutions and the projection of layers onto intermediate outputs.
* The experimental results, including the test results and the analysis of the optimization behavior under different scenarios.
* The theoretical guarantees of the YES framework, such as its ability to identify under-optimized layers and improve training performance.
{% endraw %}

{% raw %}
## 3) A Closed-Form Persistence-Landmark Pipeline for Certified Point-Cloud and Graph Classification
- **Authors:** Sushovan Majhi, Atish Mitra, Žiga Virk, Pramita Bagchi
- **arXiv:** [2605.02836](https://arxiv.org/abs/2605.02836v1) · [pdf](https://arxiv.org/pdf/2605.02836v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, math.AT

### Abstract
> We introduce PLACE (Persistence-Landmark Analytic Classification Engine), a closed-form pipeline for classifying point clouds and graphs through their persistent-homology signatures. Three quantitative guarantees -- a margin-based excess-risk rate, a closed-form descriptor-selection rule, and a per-prediction certificate -- are derived from training labels alone, with no learned weights or held-out calibration. The embedding sums Mitra-Virk single-point coordinate functions over a sparse landmark grid; closed-form weights maximize a structural distortion constant $λ(ν)$ (a Lipschitz lower bound on $\mathcal{D}_n$ under non-interference). (i) An $O(kR/(Δ\sqrt{m_{\min}}))$ margin bound, driven by class-mean separation $Δ$ and embedding radius $R$, matched by a sample-starved minimax lower bound. (ii) The Mahalanobis margin under Ledoit-Wolf-shrunk covariance is the strongest closed-form descriptor selector on a heterogeneous 64-descriptor chemical-graph pool (mean Spearman $ρ\approx +0.54$ across 10 benchmarks, positive on 9 of 10); the isotropic surrogate $Δ/\sqrt\ell$ admits a closed-form selection-consistency rate on homogeneous (14-15 descriptor) protein/social pools. (iii) A training-time-decided certificate with no per-prediction overhead, in non-asymptotic Pinelis and asymptotic Gaussian plug-in forms. Empirically, PLACE is the strongest diagram-based method on Orbit5k and matches the strongest topology-based baseline within statistical noise on MUTAG and COX2. The remaining gaps fall into two diagnosable regimes: descriptor blindness on NCI1/NCI109, and pool-coverage limits elsewhere. Both radii exceed the firing threshold $\hatΔ/2$ on every benchmark at our training-set sizes, dominated by the $\sqrt\ell$ scaling of the multivariate-norm bound; the per-prediction certificate is constructive but not yet operational at these sizes.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### 1. Structural Distortion Constant
\[ λ(ν) = \max_{x \in X} \left\{ \left\| \sum_{i=1}^{k} w_i f_i(x) \right\|_2 \right\} \]
Symbols:
- \( λ(ν) \): structural distortion constant
- \( X \): input space
- \( w_i \): weights
- \( f_i(x) \): Mitra-Virk single-point coordinate functions
- \( k \): number of landmarks
- \( \left\| \cdot \right\|_2 \): Euclidean norm

Matters: This equation defines the structural distortion constant, which is a Lipschitz lower bound on the distance between the embedding and the true label.

### 2. Mahalanobis Margin
\[ \Delta = \frac{\Delta}{\sqrt{\ell}} \]
Symbols:
- \( \Delta \): class-mean separation
- \( \ell \): isotropic surrogate

Matters: This equation defines the Mahalanobis margin, which is used as a closed-form descriptor selector.

### 3. Closed-Form Weights
\[ \hat{w} = \argmax_{w} \left\{ \min_{x \in X} \left\| \sum_{i=1}^{k} w_i f_i(x) \right\|_2 \right\} \]
Symbols:
- \( \hat{w} \): closed-form weights
- \( w \): weights
- \( f_i(x) \): Mitra-Virk single-point coordinate functions
- \( X \): input space
- \( k \): number of landmarks

Matters: This equation defines the closed-form weights that maximize the structural distortion constant.

### 4. Sample-Starved Minimax Lower Bound
\[ O\left(\frac{kR}{\Delta\sqrt{m_{\min}}} \right) \]
Symbols:
- \( k \): number of landmarks
- \( R \): embedding radius
- \( \Delta \): class-mean separation
- \( m_{\min} \): minimum number of samples

Matters: This equation provides a sample-starved minimax lower bound on the margin-based excess-risk rate.

### 5. Per-Prediction Certificate
\[ \text{Certificate} = \text{Ledoit-Wolf-shrunk covariance} \]
Symbols:
- \( \text{Certificate} \): per-prediction certificate
- Ledoit-Wolf-shrunk covariance: a measure of the covariance matrix

Matters: This equation defines the per-prediction certificate, which is a training-time-decided certificate with no per-prediction overhead.

**Method Summary**
================

* The PLACE (Persistence-Landmark Analytic Classification Engine) pipeline uses a closed-form approach to classify point clouds and graphs through their persistent-homology signatures.
* The pipeline consists of three main components:
	+ A sparse landmark grid
	+ A structural distortion constant
	+ A closed-form weights selection rule
* The pipeline is trained on a dataset and provides a margin-based excess-risk rate, a closed-form descriptor-selection rule, and a per-prediction certificate.

**Experimental Overview**
=======================

* Tasks/Datasets: Point cloud and graph classification
* Baselines/Comparisons: Topology-based and diagram-based methods
* Main Claimed Findings:
	+ PLACE outperforms the strongest topology-based baseline on Orbit5k
	+ PLACE matches the strongest diagram-based baseline within statistical noise on MUTAG and COX2
	+ PLACE has a stronger closed-form descriptor selector than other methods

**What to Verify in the PDF**
==========================

* The derivation of the structural distortion constant and the closed-form weights selection rule
* The empirical results on the 64-descriptor chemical-graph pool and the protein/social pool
* The theoretical guarantees on the margin-based excess-risk rate and the per-prediction certificate
{% endraw %}

{% raw %}
## 4) The Bayesian Reflex: Online Learning as the Autonomic Nervous System of Modern and Future AI
- **Authors:** Durba Bhattacharya, Sucharita Roy, Sourabh Bhattacharya
- **arXiv:** [2605.02825](https://arxiv.org/abs/2605.02825v1) · [pdf](https://arxiv.org/pdf/2605.02825v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.02825v1))
- **Categories:** stat.ME, stat.ML

### Abstract
> This chapter introduces the Bayesian reflex -- an analogy with the autonomic nervous system -- as a unifying framework for online learning in AI. Bayesian online algorithms automatically maintain equilibrium in dynamic environments via three mechanisms: belief maintenance through probabilistic representations, sequential updating via Bayes' theorem, and uncertainty-driven action balancing exploration and exploitation. We survey online Bayesian methods, highlighting two computational principles: the look-up table principle for sequential inference in function space, and the ellipsoidal decomposition framework for nearly exact i.i.d. sampling from arbitrary posteriors. These principles are generalized across dynamic emulation, nonparametric state-space models, circular time series, inverse regression for climate model evaluation, and deep architectures via Recursive Gaussian Processes. Decision-making is explored via Thompson sampling and restless bandits. We extend the framework to assess infinite series convergence (applied to climate dynamics and the Riemann Hypothesis), model prime number distributions leading to the discovery of 184 strong Mersenne prime candidates, detect stationarity, and characterize point processes. The Bayesian reflex provides a foundational infrastructure for adaptive AI that continuously learns in a complex world.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\theta$

* Equation: $\theta$
* Symbols: $\theta$
* Why it matters: This is the parameter of interest, representing the state or value that the algorithm is trying to optimize or estimate.

### Equation 2: $\mathcal{D}$

* Equation: $\mathcal{D}$
* Symbols: $\mathcal{D}$
* Why it matters: This represents the data or observations that are used to update the parameter $\theta$.

### Equation 3: $p(\theta \mid \mathcal{D}) = \frac{p(\mathcal{D} \mid \theta)p(\theta)}{p(\mathcal{D})}$

* Equation: $p(\theta \mid \mathcal{D}) = \frac{p(\mathcal{D} \mid \theta)p(\theta)}{p(\mathcal{D})}$
* Symbols: $p(\theta \mid \mathcal{D})$, $p(\mathcal{D} \mid \theta)$, $p(\theta)$, $p(\mathcal{D})$
* Why it matters: This is the posterior probability of the parameter $\theta$ given the data $\mathcal{D}$, which is calculated using Bayes' theorem.

### Equation 4: $p(\theta)$

* Equation: $p(\theta)$
* Symbols: $p(\theta)$
* Why it matters: This represents the prior probability distribution of the parameter $\theta$, which is used as a starting point for the Bayesian inference.

### Equation 5: $p(\mathcal{D} \mid \theta)$

* Equation: $p(\mathcal{D} \mid \theta)$
* Symbols: $p(\mathcal{D} \mid \theta)$
* Why it matters: This represents the likelihood of the data $\mathcal{D}$ given the parameter $\theta$, which is used to update the posterior probability.

### Equation 6: $p(\mathcal{D}) = \int p(\mathcal{D} \mid \theta)p(\theta) \, d\theta$

* Equation: $p(\mathcal{D}) = \int p(\mathcal{D} \mid \theta)p(\theta) \, d\theta$
* Symbols: $p(\mathcal{D})$, $p(\mathcal{D} \mid \theta)$, $p(\theta)$
* Why it matters: This is the marginal likelihood of the data $\mathcal{D}$, which is used to normalize the posterior probability.

### Equation 7: $p(\theta \mid \mathcal{D}) = \frac{p(\mathcal{D} \mid \theta)p(\theta)}{p(\mathcal{D})}$

* Equation: $p(\theta \mid \mathcal{D}) = \frac{p(\mathcal{D} \mid \theta)p(\theta)}{p(\mathcal{D})}$
* Symbols: $p(\theta \mid \mathcal{D})$, $p(\mathcal{D} \mid \theta)$, $p(\theta)$, $p(\mathcal{D})$
* Why it matters: This is the same equation as Equation 3, but it's repeated here for emphasis.

**Method Summary**
================

* The Bayesian reflex is a unifying framework for online learning in AI, inspired by the autonomic nervous system.
* The framework consists of three fundamental mechanisms: belief maintenance via probabilistic representations, sequential updating through Bayes' theorem, and uncertainty-driven action that balances exploration and exploitation.
* The algorithm uses a combination of component selection and perfect sampling to generate iid samples from any target distribution.
* The algorithm also incorporates Kalman filter and particle filter methods for handling linear and nonlinear dynamics, respectively.

**Experimental Overview**
=====================

* The algorithm has been tested on a variety of problems, including simple one-dimensional functions, 50- and 100-dimensional optimization problems.
* The algorithm outperforms classical optimization methods in terms of accuracy and gradient norm.
* The algorithm is computationally feasible even in high dimensions, thanks to parallel implementation of importance weight computation.

**What to Verify in the PDF**
==========================

* The mathematical derivations of the Bayesian reflex algorithm, particularly the proofs of its convergence and optimality.
* The empirical results of the experiments, including the performance of the algorithm on different problem types and dimensions.
* The theoretical foundations of the algorithm, including its relationship to other machine learning and optimization methods.
{% endraw %}

{% raw %}
## 5) Adaptive Interpolation-Synthesis for Motion In-Betweening on Keyframe-Based Animation
- **Authors:** Anton Raël, Julien Boucher, Antoine Lhermitte
- **arXiv:** [2605.02742](https://arxiv.org/abs/2605.02742v1) · [pdf](https://arxiv.org/pdf/2605.02742v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.02742v1))
- **Categories:** cs.GR, cs.LG

### Abstract
> Motion in-betweening is one of the most artistically demanding and time consuming stages of 3D animation, where the expressivity and rhythm of motion are defined. The level of creative control it requires makes it a major production bottleneck, underscoring the need for intelligent tools that assist animators in this process. Although recent deep learning approaches have achieved strong results in motion synthesis and in-betweening, they assume data characteristics, motion styles, and problem formulations that diverge from professional animation workflows. To bridge this gap, we propose a method explicitly aligned with the constraints of motion in-betweening for keyframe-based animation in production environments. At its core, the Adaptive Interpolation-Synthesis (AIS) layer mirrors the animator's creative process by dynamically balancing learned interpolation and direct pose synthesis. In addition, a domain-based input keypose schedule reflects the distribution of production data, improving stylistic consistency and alignment between training and real-world usage. Our method achieves state-of-the-art performance on production data; when integrated into Autodesk Maya, it enables animators to complete in-betweening tasks with a 3.5x speedup.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 3.5 ×

* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 2: S0

* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 3: ht

* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 4: αt

* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 5: pt^synth

* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 6: βt

* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 7: pt^prev

* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

**Method Summary**
==================

* The Adaptive Interpolation-Synthesis (AIS) layer mirrors the animator's creative process by dynamically balancing learned interpolation and direct pose synthesis.
* The method uses a domain-based input keypose schedule to improve stylistic consistency and alignment between training and real-world usage.
* The network input is constructed by zeroing out non-input poses and appending a binary mask.
* The method achieves state-of-the-art performance on production data and enables animators to complete in-betweening tasks with a 3.5 × speedup.

**Experimental Overview**
========================

* Tasks/Datasets:
	+ In-House Dataset of professionally handcrafted animations
	+ Three test sets: Algorithmic Test Set, Random Test Set, and Production Test Set
* Baselines/Comparisons:
	+ Δ-Interpolator (Oreshkin et al., 2024)
	+ CITL (Mo et al., 2023)
	+ CondMDI (Cohan et al., 2024)
* Main claimed findings:
	+ AIS achieves state-of-the-art performance on production data
	+ AIS enables animators to complete in-betweening tasks with a 3.5 × speedup

**What to Verify in the PDF**
=============================

* The implementation details of the Domain-Based Algorithm (DBA) keypose extraction method
* The optimization and architectural parameters of the baseline methods (Δ-Interpolator, CITL, and CondMDI)
* The evaluation metrics used to measure performance on the test sets (Algorithmic Test Set, Random Test Set, and Production Test Set)
{% endraw %}
