---
layout: post
title: "Daily arXiv Digest — 2026-05-01 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) An adaptive wavelet-based PINN for problems with localized high-magnitude source
- **Authors:** Himanshu Pandey, Ratikanta Behera
- **arXiv:** [2604.28180](https://arxiv.org/abs/2604.28180v1) · [pdf](https://arxiv.org/pdf/2604.28180v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.28180v1))
- **Categories:** cs.LG

### Abstract
> In recent years, physics-informed neural networks (PINNs) have gained significant attention for solving differential equations, although they suffer from two fundamental limitations, namely, spectral bias inherent in neural networks and loss imbalance arising from multiscale phenomena. This paper proposes an adaptive wavelet-based PINN (AW-PINN) to address the extreme loss imbalance characteristic of problems with localized high-magnitude source terms. Such problems frequently arise in various physical applications, such as thermal processing, electro-magnetics, impact mechanics, and fluid dynamics involving localized forcing. The proposed framework dynamically adjusts the wavelet basis function based on residual and supervised loss. This adaptive nature makes AW-PINN handle problems with high-scale features effectively without being memory-intensive. Additionally, AW-PINN does not rely on automatic differentiation to obtain derivatives involved in the loss function, which accelerates the training process. The method operates in two stages, an initial short pre-training phase with fixed bases to select physically relevant wavelet families, followed by an adaptive refinement that adapts scales and translations without populating high-resolution bases across entire domains. Theoretically, we show that under certain assumptions, AW-PINN admits a Gaussian process limit and derive its associated NTK structure. We evaluate AW-PINN on several challenging PDEs featuring localized high-magnitude source terms with extreme loss imbalances having ratios up to $10^{10}:1$. Across these PDEs, including transient heat conduction, highly localized Poisson problems, oscillatory flow equations, and Maxwell equations with a point charge source, AW-PINN consistently outperforms existing methods in its class.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: [Eq 1] $10^{10}:1$

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: \begin{cases}\mathscr{P}[u(\boldsymbol{x})]=f(\boldsymbol{x}),\quad\boldsymbol{x}\in\Omega,\\\mathscr{B}[u(\boldsymbol{x})]=g(\boldsymbol{x}),\quad\boldsymbol{x}\in\partial\Omega,\end{cases}

* Equation: A system of two equations, where $\mathscr{P}[u(\boldsymbol{x})]$ represents the partial differential equation, $f(\boldsymbol{x})$ is the source term, $\mathscr{B}[u(\boldsymbol{x})]$ represents the boundary condition, and $g(\boldsymbol{x})$ is the boundary data.
* Symbols:
	+ $\mathscr{P}[u(\boldsymbol{x})]$: Partial differential operator
	+ $f(\boldsymbol{x})$: Source term
	+ $g(\boldsymbol{x})$: Boundary data
	+ $\Omega$: Domain
	+ $\partial\Omega$: Boundary of the domain
* Why it matters: This equation represents a common problem in physics-informed neural networks (PINNs), where the goal is to solve a partial differential equation (PDE) with a given source term and boundary condition.

### Equation 3: $\mathscr{P}[\cdot]$

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 4: $\Omega\subset\mathbb{R}^{d}$

* Equation: Not found in extracted context.
* Symbols:
	+ $\Omega$: Domain
	+ $\mathbb{R}^{d}$: d-dimensional Euclidean space
* Why it matters: This equation represents the domain of the problem, which is a subset of the d-dimensional Euclidean space.

### Equation 5: $\mathscr{B}$

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 6: $\hat{u}(\boldsymbol{x};\boldsymbol{\theta})$

* Equation: Not found in extracted context.
* Symbols:
	+ $\hat{u}(\boldsymbol{x};\boldsymbol{\theta})$: Model prediction
	+ $\boldsymbol{\theta}$: Model parameters
* Why it matters: This equation represents the model's prediction, which is used to evaluate the performance of the PINN.

### Equation 7: $\boldsymbol{\theta}$

* Equation: Not found in extracted context.
* Symbols:
	+ $\boldsymbol{\theta}$: Model parameters
* Why it matters: This equation represents the model parameters, which are learned during training.

### Equation 8: $\mathcal{L}$

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

**Method Summary**
================

* The proposed AW-PINN framework is an adaptive wavelet-based PINN that addresses the loss imbalance issue in PINNs.
* The framework consists of two stages: an initial short pre-training phase with fixed bases to select physically relevant wavelet families, followed by an adaptive refinement that adapts scales and translations without populating high-resolution bases across entire domains.
* The adaptive nature of AW-PINN makes it effective in handling problems with high-scale features without being memory-intensive.
* AW-PINN does not rely on automatic differentiation to obtain derivatives involved in the loss function, which accelerates the training process.

**Experimental Overview**
=====================

* Tasks/Datasets: The proposed method is evaluated on several challenging PDEs featuring localized high-magnitude source terms, including transient heat conduction, highly localized Poisson problems, oscillatory flow equations, and Maxwell's equations with a point charge source.
* Baselines/Comparisons: The performance of AW-PINN is compared with baseline PINN, W-PINN, and MMPINN, all of which are designed to address the loss imbalance issue in PINNs.
* Main Claimed Findings: AW-PINN consistently outperforms existing methods in its class, achieving better performance on several challenging PDEs.

**What to Verify in the PDF**
==========================

* The mathematical derivation of the adaptive wavelet basis function and its relation to the Gaussian process limit.
* The theoretical analysis of the NTK structure of AW-PINN.
* The detailed implementation of the AW-PINN framework, including the training procedure and hyperparameter tuning.
{% endraw %}

{% raw %}
## 2) Defending Quantum Classifiers against Adversarial Perturbations through Quantum Autoencoders
- **Authors:** Emma Andrews, Sahan Sanjaya, Prabhat Mishra
- **arXiv:** [2604.28176](https://arxiv.org/abs/2604.28176v1) · [pdf](https://arxiv.org/pdf/2604.28176v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.28176v1))
- **Categories:** quant-ph, cs.LG

### Abstract
> Machine learning models can learn from data samples to carry out various tasks efficiently. When data samples are adversarially manipulated, such as by insertion of carefully crafted noise, it can cause the model to make mistakes. Quantum machine learning models are also vulnerable to such adversarial attacks, especially in image classification using variational quantum classifiers. While there are promising defenses against these adversarial perturbations, such as training with adversarial samples, they face practical limitations. For example, they are not applicable in scenarios where training with adversarial samples is either not possible or can overfit the models on one type of attack. In this paper, we propose an adversarial training-free defense framework that utilizes a quantum autoencoder to purify the adversarial samples through reconstruction. Moreover, our defense framework provides a confidence metric to identify potentially adversarial samples that cannot be purified the quantum autoencoder. Extensive evaluation demonstrates that our defense framework can significantly outperform state-of-the-art in prediction accuracy (up to 68%) under adversarial attacks.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `x ∈ ℝ^m`

* Equation: `x ∈ ℝ^m`
* Symbols: `x` (input data), `m` (dimensionality of input space)
* Why it matters: This equation defines the input space of the machine learning model, specifying that `x` is a vector of length `m` in the real number space.

### Equation 2: `z ∈ ℝ^n, m > n`

* Equation: `z ∈ ℝ^n, m > n`
* Symbols: `z` (quantum state), `n` (dimensionality of quantum state), `m` (dimensionality of input space)
* Why it matters: This equation defines the relationship between the input space and the quantum state, specifying that the quantum state has a lower dimensionality than the input space.

### Equation 3: `ĥ̂ ∈ ℝ^m`

* Equation: `ĥ̂ ∈ ℝ^m`
* Symbols: `ĥ̂` (reconstructed input), `m` (dimensionality of input space)
* Why it matters: This equation defines the reconstructed input, which is the output of the quantum autoencoder.

### Equation 4: `x ≈ ĥ̂`

* Equation: `x ≈ ĥ̂`
* Symbols: `x` (original input), `ĥ̂` (reconstructed input)
* Why it matters: This equation states that the original input is approximately equal to the reconstructed input, indicating that the quantum autoencoder has successfully purified the input.

### Equation 5: `U(θ)`

* Equation: `U(θ)`
* Symbols: `U` (unitary operator), `θ` (quantum parameters)
* Why it matters: This equation represents the unitary operator that acts on the quantum state, which is parameterized by the quantum parameters `θ`.

**Method Summary**
================

* Our defense framework uses a quantum autoencoder to purify adversarial samples through reconstruction.
* The framework provides a confidence metric to identify potentially adversarial samples that cannot be purified.
* Our approach is adversarial training-free, making it applicable in scenarios where training with adversarial samples is not possible or can overfit the model.

**Experimental Overview**
========================

* Tasks: Evaluating the effectiveness of our defense framework against adversarial attacks on MNIST and FashionMNIST datasets.
* Baselines: Comparing our framework with state-of-the-art defense approaches.
* Main claimed findings: Our framework outperforms state-of-the-art approaches in terms of prediction accuracy, with up to 68% improvement under adversarial attacks.

**What to Verify in the PDF**
==========================

* The experimental setup, including the specific implementation details of the quantum autoencoder and the adversarial attacks used.
* The confidence metric used to identify potentially adversarial samples, and how it is calculated.
* The results of the experiments, including the accuracy of our framework compared to the baselines.
{% endraw %}

{% raw %}
## 3) PhyCo: Learning Controllable Physical Priors for Generative Motion
- **Authors:** Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker
- **arXiv:** [2604.28169](https://arxiv.org/abs/2604.28169v1) · [pdf](https://arxiv.org/pdf/2604.28169v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.28169v1))
- **Categories:** cs.CV, cs.AI, cs.LG

### Abstract
> Modern video diffusion models excel at appearance synthesis but still struggle with physical consistency: objects drift, collisions lack realistic rebound, and material responses seldom match their underlying properties. We present PhyCo, a framework that introduces continuous, interpretable, and physically grounded control into video generation. Our approach integrates three key components: (i) a large-scale dataset of over 100K photorealistic simulation videos where friction, restitution, deformation, and force are systematically varied across diverse scenarios; (ii) physics-supervised fine-tuning of a pretrained diffusion model using a ControlNet conditioned on pixel-aligned physical property maps; and (iii) VLM-guided reward optimization, where a fine-tuned vision-language model evaluates generated videos with targeted physics queries and provides differentiable feedback. This combination enables a generative model to produce physically consistent and controllable outputs through variations in physical attributes-without any simulator or geometry reconstruction at inference. On the Physics-IQ benchmark, PhyCo significantly improves physical realism over strong baselines, and human studies confirm clearer and more faithful control over physical attributes. Our results demonstrate a scalable path toward physically consistent, controllable generative video models that generalize beyond synthetic training environments.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $G_{\theta}$

* Equation: Not explicitly provided in the extracted context.
* Symbols: Not provided.
* Why it matters: Not applicable.

### Equation 2: $p_{\theta}(\mathbf{x}_{1:T}|\mathbf{t},\mathbf{x}_{0}^{0},\mathbf{p})$

* Equation: Conditional probability of a sequence of frames $\mathbf{x}_{1:T}$ given time $\mathbf{t}$, initial state $\mathbf{x}_{0}^{0}$, and physical properties $\mathbf{p}$.
* Symbols:
	+ $\mathbf{x}_{1:T}$: sequence of frames
	+ $\mathbf{t}$: time
	+ $\mathbf{x}_{0}^{0}$: initial state
	+ $\mathbf{p}$: physical properties
* Why it matters: This equation represents the generative model's ability to predict a sequence of frames given the input conditions.

### Equation 3: $\mathbf{x}_{1:T}$

* Equation: Not explicitly provided in the extracted context.
* Symbols: Not provided.
* Why it matters: Not applicable.

### Equation 4: $\mathbf{t}$

* Equation: Not explicitly provided in the extracted context.
* Symbols: Not provided.
* Why it matters: Not applicable.

### Equation 5: $\mathbf{x}_{0}^{0}\in\mathbb{R}^{C\times H\times W}$

* Equation: Initial state $\mathbf{x}_{0}^{0}$ is a 3D tensor with shape $(C \times H \times W)$, where $C$ is the number of color channels, $H$ is the height, and $W$ is the width.
* Symbols:
	+ $\mathbf{x}_{0}^{0}$: initial state
	+ $\mathbb{R}^{C\times H\times W}$: 3D tensor with shape $(C \times H \times W)$
* Why it matters: This equation represents the initial state of the system, which is used as input to the generative model.

### Equation 6: $\mathbf{p}\in\mathbb{R}^{K\times H\times W}$

* Equation: Physical properties $\mathbf{p}$ is a 3D tensor with shape $(K \times H \times W)$, where $K$ is the number of physical properties.
* Symbols:
	+ $\mathbf{p}$: physical properties
	+ $\mathbb{R}^{K\times H\times W}$: 3D tensor with shape $(K \times H \times W)$
* Why it matters: This equation represents the physical properties of the system, which are used to control the generative model.

### Equation 7: $\mathbf{p}$

* Equation: Not explicitly provided in the extracted context.
* Symbols: Not provided.
* Why it matters: Not applicable.

### Equation 8: $[-1,1]$

* Equation: A constant vector with values ranging from -1 to 1.
* Symbols: Not provided.
* Why it matters: Not applicable.

**Method Summary**
================

* The proposed method, PhyCo, integrates three key components:
	+ A large-scale dataset of over 100K photorealistic simulation videos with varied physical properties.
	+ Physics-supervised fine-tuning of a pretrained diffusion model using a ControlNet conditioned on pixel-aligned physical property maps.
	+ VLM-guided reward optimization, where a fine-tuned vision–language model evaluates generated videos with targeted physics queries and provides differentiable feedback.
* The goal is to enable diffusion models with continuous and interpretable control over key physical properties while maintaining photorealistic synthesis and broad generalization.

**Experimental Overview**
=====================

* Tasks/Datasets:
	+ PhyCo dataset: a large-scale dataset of over 100K photorealistic simulation videos with varied physical properties.
	+ Physics-IQ benchmark: a benchmark for evaluating physical realism in video generation.
* Baselines:
	+ Cosmos-Predict2: a text-conditioned image-to-video world model.
	+ CogVideoX-I2V-5B: a text-conditioned image-to-video world model.
	+ SVD-XT: a text-conditioned image-to-video world model.
	+ LTX-Video-I2V: a text-conditioned image-to-video world model.
	+ Force-Prompting: a method for improving controllability and physics awareness through force-specific supervision.
	+ VLIPP: a method for extracting coarse motion trajectories using a VLM.
* Main claimed findings:
	+ PhyCo significantly improves physical realism over strong baselines on the Physics-IQ benchmark.
	+ Human studies confirm clearer and more faithful control over physical attributes.
	+ The method achieves the best or second-best FVMD scores across most domains, demonstrating improved temporal coherence and physically plausible motion.

**What to Verify in the PDF**
==========================

* The details of the ControlNet architecture and its role in physics-supervised fine-tuning.
* The implementation of the VLM-guided reward optimization and its impact on physical realism.
* The evaluation of the method on additional benchmarks and datasets beyond the Physics-IQ benchmark.
{% endraw %}

{% raw %}
## 4) Explainable Load Forecasting with Covariate-Informed Time Series Foundation Models
- **Authors:** Matthias Hertel, Alexandra Nikoltchovska, Sebastian Pütz, Ralf Mikut, Benjamin Schäfer, Veit Hagenmeyer
- **arXiv:** [2604.28149](https://arxiv.org/abs/2604.28149v1) · [pdf](https://arxiv.org/pdf/2604.28149v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.28149v1))
- **Categories:** cs.LG

### Abstract
> Time Series Foundation Models (TSFMs) have recently emerged as general-purpose forecasting models and show considerable potential for applications in energy systems. However, applications in critical infrastructure like power grids require transparency to ensure trust and reliability and cannot rely on pure black-box models. To enhance the transparency of TSFMs, we propose an efficient algorithm for computing Shapley Additive Explanations (SHAP) tailored to these models. The proposed approach leverages the flexibility of TSFMs with respect to input context length and provided covariates. This property enables efficient temporal and covariate masking (selectively withholding inputs), allowing for a scalable explanation of model predictions using SHAP. We evaluate two TSFMs - Chronos-2 and TabPFN-TS - on a day-ahead load forecasting task for a transmission system operator (TSO). In a zero-shot setting, both models achieve predictive performance competitive with a Transformer model trained specifically on multiple years of TSO data. The explanations obtained through our proposed approach align with established domain knowledge, particularly as the TSFMs appropriately use weather and calendar information for load prediction. Overall, we demonstrate that TSFMs can serve as transparent and reliable tools for operational energy forecasting.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: V = {v1, v2, ..., vn}

* Equation: V = {v1, v2, ..., vn}
* Symbols: V, v1, v2, ..., vn
* Why it matters: This equation represents the set of features used by the model.

### Equation 2: vi

* Equation: vi
* Symbols: vi
* Why it matters: This equation represents a single feature in the feature set V.

### Equation 3: SHAP(vi) = ∑[S ⊆ V \ {vi}] [(n-1-|S|)! \* |S|! / n!] \* (f(S ∪ {vi}) - f(S))

* Equation: SHAP(vi) = ∑[S ⊆ V \ {vi}] [(n-1-|S|)! \* |S|! / n!] \* (f(S ∪ {vi}) - f(S))
* Symbols: SHAP(vi), S, vi, n
* Why it matters: This equation calculates the SHAP value for feature vi, which represents the contribution of vi to the model's prediction.

### Equation 4: f(S ∪ {vi}) - f(S)

* Equation: f(S ∪ {vi}) - f(S)
* Symbols: f(S ∪ {vi}), f(S), S, vi
* Why it matters: This equation represents the difference in the model's output when the feature vi is included and when it is not.

### Equation 5: 2^n

* Equation: 2^n
* Symbols: n
* Why it matters: This equation represents the number of possible subsets of the feature set V.

### Equation 6: O(2^n)

* Equation: O(2^n)
* Symbols: n
* Why it matters: This equation represents the time complexity of the SHAP calculation.

**Method Summary**
==================

* The authors propose an efficient algorithm for computing SHAP values for Time Series Foundation Models (TSFMs).
* The algorithm leverages the flexibility of TSFMs to compute SHAP values for individual features.
* The authors use two TSFMs, Chronos-2 and TabPFN-TS, to evaluate their approach.
* The proposed approach is scalable and can handle large datasets.

**Experimental Overview**
========================

* The authors evaluate the performance of TSFMs on a day-ahead load forecasting task for a transmission system operator (TSO).
* The dataset consists of hourly load data from January 2015 to September 2025, enriched with weather data.
* The authors compare the performance of TSFMs with a Transformer model trained on the full dataset.
* The main claimed findings are that TSFMs achieve competitive performance with the Transformer model and provide more interpretable results.

**What to Verify in the PDF**
=============================

* The authors mention that the full technical details of the model architectures are provided in the original publications. Verify that these publications exist and provide the necessary information.
* The authors also mention that the dataset is downloaded from the ENTSO-E Transparency Platform. Verify that this platform exists and provides the necessary data.
* The authors claim that the reanalysis data is not available at prediction time, but is used as perfect forecasts in the absence of historical weather forecasts. Verify that this is the case and that the reanalysis data is used correctly.
{% endraw %}

{% raw %}
## 5) Do Sparse Autoencoders Capture Concept Manifolds?
- **Authors:** Usha Bhalla, Thomas Fel, Can Rager, Sheridan Feucht, Tal Haklay, Daniel Wurgaft, Siddharth Boppana, Matthew Kowal, Vasudev Shyam, Jack Merullo, Atticus Geiger, Ekdeep Singh Lubana
- **arXiv:** [2604.28119](https://arxiv.org/abs/2604.28119v1) · [pdf](https://arxiv.org/pdf/2604.28119v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.28119v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Sparse autoencoders (SAEs) are widely used to extract interpretable features from neural network representations, often under the implicit assumption that concepts correspond to independent linear directions. However, a growing body of evidence suggests that many concepts are instead organized along low-dimensional manifolds encoding continuous geometric relationships. This raises three basic questions: what does it mean for an SAE to capture a manifold, when do existing SAE architectures do so, and how? We develop a theoretical framework that answers these questions and show that SAEs can capture manifolds in two fundamentally different ways: globally, by allocating a compact group of atoms whose linear span contains the entire manifold, or locally, by distributing it across features that each selectively tile a restricted region of the underlying geometry. Empirically, we find that SAEs suboptimally recover continuous structures, mixing the global subspace and local tiling solutions in a fragmented regime we call dilution. This explains why manifold structure is rarely visible at the level of individual concepts and motivates post-hoc unsupervised discovery methods that search for coherent groups of atoms rather than isolated directions. More broadly, our results suggest that future representation learning methods should treat geometric objects, not just individual directions, as the basic units of interpretability.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1
\[ {}^{{\color[rgb]{0.72265625,0.59375,0.2265625}\definecolor[named]{pgfstrokecolor}{rgb}{0.72265625,0.59375,0.2265625}\bm{\star}}\raisebox{0.5pt}{\hskip 1.42262pt\includegraphics[height=6.0pt]{arxiv/goodfire_logo_small.png}},a} \]

* Symbols: `^`, `\bm{\star}`, `\raisebox`, `\hskip`, `\includegraphics`
* Matters: This equation is not explicitly defined in the provided context, but it appears to be a placeholder or a reference to a figure.

### Equation 2
\[ {}^{{\color[rgb]{0.72265625,0.59375,0.2265625}\definecolor[named]{pgfstrokecolor}{rgb}{0.72265625,0.59375,0.2265625}\bm{\star}}\raisebox{0.5pt}{\hskip 1.42262pt\includegraphics[height=6.0pt]{arxiv/goodfire_logo_small.png}} \]

* Symbols: Same as Equation 1
* Matters: Same as Equation 1 (not explicitly defined)

### Equation 3
\[ {}^{\raisebox{0.5pt}{\hskip 1.42262pt\includegraphics[height=6.0pt]{arxiv/goodfire_logo_small.png}} \]

* Symbols: `\raisebox`, `\hskip`, `\includegraphics`
* Matters: This equation is not explicitly defined in the provided context, but it appears to be a placeholder or a reference to a figure.

### Equation 4
\[ {}^{\raisebox{0.5pt}{\hskip 1.42262pt\includegraphics[height=6.0pt]{arxiv/goodfire_logo_small.png}},b} \]

* Symbols: Same as Equation 3
* Matters: Same as Equation 3 (not explicitly defined)

### Equation 5
\[ {}^{\raisebox{0.5pt}{\hskip 1.42262pt\includegraphics[height=6.0pt]{arxiv/goodfire_logo_small.png}},c} \]

* Symbols: Same as Equation 3
* Matters: Same as Equation 3 (not explicitly defined)

### Equation 6
\[ {}^{\raisebox{0.5pt}{\hskip 1.42262pt\includegraphics[height=6.0pt]{arxiv/goodfire_logo_small.png}},d} \]

* Symbols: Same as Equation 3
* Matters: Same as Equation 3 (not explicitly defined)

**Method Summary**
==================

* The authors develop a theoretical framework to answer three basic questions about sparse autoencoders (SAEs) and their ability to capture concept manifolds.
* SAEs extract latent representations by solving an optimization problem involving a dictionary.
* The authors propose two ways SAEs can capture manifolds: globally, by allocating a compact group of atoms, and locally, by distributing atoms across features that tile a restricted region of the underlying geometry.
* The authors also discuss the limitations of SAEs in capturing continuous structures and the importance of post-hoc unsupervised discovery methods.

**Experimental Overview**
=========================

* The authors conduct a controlled experiment to study how SAEs capture curved geometries, specifically manifolds.
* The experiment involves:
	+ Fitting PCA on cached layer-19 activations to retain 90% of variance.
	+ Selecting a base prompt near the manifold's midpoint and constructing a sweep by binning the manifold's primary continuous label into 5-10 equal-width bins.
	+ Computing the PCA centroid and linearly interpolating 5-10 points between consecutive centroids.
* The authors find that SAEs suboptimally recover continuous structures, mixing global subspace and local tiling solutions in a fragmented regime called "dilution."
* The authors also demonstrate that the manifold structure is not only present in the representation but also causally influences downstream behavior.

**What to Verify in the PDF**
=============================

* The authors mention that the intrinsic dimension `di` governs the manifold's degrees of freedom and determines the expected number of localized detectors in the tiling regime.
* The authors also mention that the embedding dimension `ki` determines the number of atoms required for subspace capture.
* The authors discuss the distinction between `di` and `ki` and provide examples to illustrate the difference.
* The authors also mention the importance of post-hoc unsupervised discovery methods that search for coherent groups of atoms rather than isolated directions.
{% endraw %}
