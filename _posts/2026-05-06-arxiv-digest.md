---
layout: post
title: "Daily arXiv Digest — 2026-05-06 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Conditional Diffusion Sampling
- **Authors:** Francisco M. Castro-Macías, Pablo Morales-Álvarez, Saifuddin Syed, Daniel Hernández-Lobato, Rafael Molina, José Miguel Hernández-Lobato
- **arXiv:** [2605.04013](https://arxiv.org/abs/2605.04013v1) · [pdf](https://arxiv.org/pdf/2605.04013v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.04013v1))
- **Categories:** stat.ML, cs.LG

### Abstract
> Sampling from unnormalized multimodal distributions with limited density evaluations remains a fundamental challenge in machine learning and natural sciences. Successful approaches construct a bridge between a tractable reference and the target distribution. Parallel Tempering (PT) serves as the gold standard, while recent diffusion-based approaches offer a continuous alternative at the cost of neural training. In this work, we introduce Conditional Diffusion Sampling (CDS), a framework that combines these two paradigms. To this end, we derive Conditional Interpolants, a class of stochastic processes whose transport dynamics are governed by an exact, closed-form stochastic differential equation (SDE), requiring no neural approximation. Although these dynamics require sampling from a non-trivial initialization distribution, we show both theoretically and empirically that the cost of this initialization diminishes for sufficiently short diffusion times. CDS leverages this by a two-stage procedure: (1) PT is used to efficiently sample the initial distribution, and then (2) samples are transported via the transport SDE. This combination couples the robust global exploration of PT with efficient local transport. Experiments suggest that CDS has the potential to achieve a superior trade-off between sample quality and density evaluation cost compared to state-of-the-art samplers.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: π_ref

* Equation: π_ref
* Symbols: π_ref (π_ref)
* Why it matters: This is the reference distribution, which serves as a bridge between the target distribution and the initial distribution.

### Equation 2: π_t0 | z

* Equation: π_t0 | z = π_t0 ∘ F_t | z
* Symbols: π_t0 | z, π_t0, F_t | z
* Why it matters: This is the conditional distribution of the initial distribution π_t0 given the current state z.

### Equation 3: X ⊂ ℝ^D

* Equation: X ⊂ ℝ^D
* Symbols: X, ℝ^D
* Why it matters: This is the domain of the target distribution, which is a subset of the real numbers with dimension D.

### Equation 4: π(x) = Z^-1 \tilde{π}(x)

* Equation: π(x) = Z^-1 \tilde{π}(x)
* Symbols: π(x), Z, \tilde{π}(x)
* Why it matters: This is the definition of the target distribution π, which is proportional to the unnormalized density \tilde{π}(x).

### Equation 5: π(x) = Z^-1 \tilde{π}(x)

* Equation: π(x) = Z^-1 \tilde{π}(x)
* Symbols: π(x), Z, \tilde{π}(x)
* Why it matters: This is the definition of the target distribution π, which is proportional to the unnormalized density \tilde{π}(x).

**Method Summary**
================

* **Conditional Diffusion Sampling (CDS)**: A framework that combines parallel tempering and diffusion-based sampling.
* **Two-stage procedure**: (1) PT is used to efficiently sample the initial distribution, and then samples are transported via the transport SDE.
* **Advantages**: Robust global exploration of PT and efficient local transport.
* **Hyperparameters**: Number of steps in Stage 1 (K) and in Stage 2 (N).

**Experimental Overview**
=======================

* **Tasks/Datasets**: Eight target distributions across four diverse tasks (synthetic benchmarks, physical systems, molecular dynamics, and high-dimensional Bayesian inference problems).
* **Baselines/Comparisons**: State-of-the-art samplers (e.g., PT, AIS, SMC).
* **Main claimed findings**: CDS achieves a superior trade-off between sample quality and density evaluation cost compared to state-of-the-art samplers.

**What to Verify in the PDF**
==========================

* **Theoretical results**: The proof of the convergence of the transport SDE and the analysis of the transport mechanism.
* **Hyperparameter tuning**: The optimal values of K and N for different tasks and datasets.
* **Robustness to noise and outliers**: The performance of CDS under noisy or outlier-prone data.
{% endraw %}

{% raw %}
## 2) Flow Sampling: Learning to Sample from Unnormalized Densities via Denoising Conditional Processes
- **Authors:** Aaron Havens, Brian Karrer, Neta Shaul
- **arXiv:** [2605.03984](https://arxiv.org/abs/2605.03984v1) · [pdf](https://arxiv.org/pdf/2605.03984v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.03984v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Sampling from unnormalized densities is analogous to the generative modeling problem, but the target distribution is defined by a known energy function instead of data samples. Because evaluating the energy function is often costly, a primary challenge is to learn an efficient sampler. We introduce Flow Sampling, a framework built on diffusion models and flow matching for the data-free setting. Our training objective is conditioned on a noise sample and regresses onto a denoising diffusion drift constructed from the energy function. In contrast, diffusion models' objective is conditioned on a data sample and regresses onto a noising diffusion drift. We utilize the interpolant process to minimize the number of energy function evaluations during training, resulting in an efficient and scalable method for sampling unnormalized densities. Furthermore, our formulation naturally extends to Riemannian manifolds, enabling diffusion-based sampling in geometries beyond Euclidean space. We derive a closed-form formula for the conditional drift on constant curvature manifolds, including hyperspheres and hyperbolic spaces. We evaluate Flow Sampling on synthetic energy benchmarks, small peptides, large-scale amortized molecular conformer generation, and distributions supported on the sphere, demonstrating strong empirical performance.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: q(x) = \frac{\exp(r(x))}{Z}

* Equation: `q(x) = \frac{\exp(r(x))}{Z}`
* Symbols: `q(x)`, `r(x)`, `Z`
* Why it matters: This equation represents the probability density function `q(x)` of the target distribution, which is proportional to the exponential of the energy function `r(x)`. The denominator `Z` is the partition function, which normalizes the density to ensure it integrates to 1.

### Equation 2: r(x)

* Equation: `r(x)`
* Symbols: `r(x)`
* Why it matters: The energy function `r(x)` is a key component of the target distribution. It is used to define the energy landscape of the system.

### Equation 3: \nabla r(x)

* Equation: `\nabla r(x)`
* Symbols: `\nabla r(x)`
* Why it matters: The gradient of the energy function `r(x)` is used in the optimization process to update the parameters of the model.

### Equation 4: x_{1}

* Equation: `x_{1}`
* Symbols: `x_{1}`
* Why it matters: This equation is not explicitly defined in the context, but it is likely related to the initial condition of the flow process.

### Equation 5: x_{0}

* Equation: `x_{0}`
* Symbols: `x_{0}`
* Why it matters: The initial condition `x_{0}` is used to initialize the flow process.

**Method Summary**
================

* Flow Sampling is a framework for sampling from unnormalized densities using diffusion models and flow matching.
* The training objective is conditioned on a noise sample and regresses onto a denoising diffusion drift constructed from the energy function.
* The framework utilizes the interpolant process to minimize the number of energy function evaluations during training.
* Flow Sampling can be extended to Riemannian manifolds, enabling diffusion-based sampling in geometries beyond Euclidean space.

**Experimental Overview**
========================

* Tasks/Datasets:
	+ Synthetic energy benchmarks (e.g. Double-Well potential, Lennard-Jones system)
	+ Alanine dipeptide and tetrapeptide experiments
	+ Conformer generation experiment
* Baselines/Comparisons:
	+ iDEM
	+ PIS
	+ DDS
	+ AS and ASBS
* Main claimed findings:
	+ Flow Sampling achieves strong empirical performance on various benchmarks and datasets.

**What to Verify in the PDF**
=============================

* The mathematical derivation of the closed-form formula for the conditional drift on constant curvature manifolds (Section 2.3).
* The implementation details of the flow process and the interpolant (Section 3.2).
* The experimental results for the conformer generation experiment, including the Average Minimum RMSD and Coverage metrics.
{% endraw %}

{% raw %}
## 3) TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis
- **Authors:** Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin
- **arXiv:** [2605.03944](https://arxiv.org/abs/2605.03944v1) · [pdf](https://arxiv.org/pdf/2605.03944v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.03944v1))
- **Categories:** cs.LG, cs.AI, stat.ML

### Abstract
> Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Data Set Representation
```latex
\mathcal{D}=\{(\mathbf{x}_{1},\delta_{1},t_{1}),\dots,(\mathbf{x}_{n},\delta_{n},t_{n})\}
```
* Symbols: `D` (data set), `x_i` (feature vector), `δ_i` (censoring indicator), `t_i` (observed time)
* Matters: This equation represents the dataset used for training and testing the survival analysis model.

### Equation 2: Feature Vector Dimension
```latex
\mathbf{x}_{i}\in\mathbb{R}^{d}
```
* Symbols: `x_i` (feature vector), `d` (dimensionality)
* Matters: This equation specifies the dimensionality of the feature vectors in the dataset.

### Equation 3: Observed Time
```latex
t_{i}
```
* Symbols: `t_i` (observed time)
* Matters: This equation represents the observed time for each data point in the dataset.

### Equation 4: Censoring Indicator
```latex
\delta_{i}\in\{0,1\}
```
* Symbols: `δ_i` (censoring indicator), `0` (censored), `1` (uncensored)
* Matters: This equation specifies the censoring indicator for each data point in the dataset.

### Equation 5: Censoring Indicator Value
```latex
\delta_{i}=1
```
* Symbols: `δ_i` (censoring indicator)
* Matters: This equation specifies the value of the censoring indicator for uncensored data points.

**Method Summary**
================

* The authors propose TabSurv, a method for adapting modern tabular neural networks to survival analysis.
* TabSurv uses a histogram loss function (SurvHL) that supports censored data.
* The method is evaluated on 10 diverse real-world survival datasets.
* The authors compare TabSurv with established classical and deep learning baselines, such as RSF, DeepSurv, and DeepHit.

**Experimental Overview**
========================

* Tasks: Survival analysis on 10 diverse real-world datasets.
* Baselines: RSF, DeepSurv, DeepHit, and TabSurv (with different variants).
* Main claimed findings: TabSurv outperforms established baselines on average, with the WAS variant achieving the highest C-index and time-dependent AUC.

**What to Verify in the PDF**
==========================

* The authors mention that the simulation study in Appendix E shows that non-parametric variants are better suited to genuinely multimodal event-time distributions. Verify that this is indeed the case.
* The authors also mention that the Weibull head is only one parametric instance; verify that other distribution families can be substituted by changing the distribution used to map predicted parameters to survival probabilities.
* Verify the experimental setup, including the hardware and software used, and the hyperparameter tuning process.
{% endraw %}

{% raw %}
## 4) Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes
- **Authors:** Cyrille Kone, Kevin Jamieson
- **arXiv:** [2605.03921](https://arxiv.org/abs/2605.03921v1) · [pdf](https://arxiv.org/pdf/2605.03921v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, stat.ML

### Abstract
> We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/δ)$. We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP. Our method achieves asymptotic optimality in sample complexity, also in terms of posterior contraction rate, and runs in $O(S^2AH)$ per episode, matching standard model-based approaches. Unlike prior algorithms such as MOCA and PEDEL, our guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/δ)$. Our results provide both theoretical insights and practical tools for efficient policy identification in tabular MDPs.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### 1. $(\varepsilon, δ)$-PAC policy identification problem
```markdown
Not found in extracted context.
```

### 2. Finite-time guarantees for approximate settings ($\varepsilon>0$)
```markdown
Not found in extracted context.
```

### 3. Asymptotic optimality in sample complexity
```markdown
Not found in extracted context.
```

### 4. Posterior contraction rate
```markdown
Not found in extracted context.
```

### 5. Computational cost: $O(S^2AH)$ per episode
```markdown
Not found in extracted context.
```

**Method Summary**
================

* The proposed algorithm combines posterior sampling with an online learning algorithm to guide exploration in the MDP.
* The algorithm achieves asymptotic optimality in sample complexity.
* The method has a computational cost of $O(S^2AH)$ per episode.
* The guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/δ)$.

**Experimental Overview**
=====================

* Tasks/Datasets: Not mentioned in the extracted context.
* Baselines/Comparisons: MOCA and PEDEL.
* Main claimed findings: The proposed algorithm achieves asymptotic optimality in sample complexity and has a computational cost of $O(S^2AH)$ per episode.

**What to Verify in the PDF**
=========================

* Details of the online learning algorithm used in the proposed method.
* The theoretical derivation of the asymptotic optimality in sample complexity.
* The analysis of the posterior contraction rate.
{% endraw %}

{% raw %}
## 5) Raising the Ceiling: Better Empirical Fixation Densities for Saliency Benchmarking
- **Authors:** Susmit Agrawal, Jannis Hollman, Matthias Kümmerer
- **arXiv:** [2605.03885](https://arxiv.org/abs/2605.03885v1) · [pdf](https://arxiv.org/pdf/2605.03885v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.03885v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> Empirical fixation densities, spatial distributions estimated from human eye-tracking data, are foundational to saliency benchmarking. They directly shape benchmark conclusions, leaderboard rankings, failure case analyses, and scientific claims about human visual behavior. Yet the standard estimation method, fixed-bandwidth isotropic Gaussian KDE, has gone essentially unchanged for decades. This matters now more than ever: as the field shifts toward sample-level evaluation (failure case analysis, inverse benchmarking, per-image model comparison), reliable per-image density estimates become critical. We propose a principled mixture model that combines an adaptive-bandwidth KDE based on Abramson's method, center bias and uniform components, and a state-of-the-art saliency model, to capture different spatial and semantic types of interobserver consistency, and optimize all parameters per image via leave-one-subject-out cross-validation. Our method yields substantially higher interobserver consistency estimates across multiple benchmarks, with median per-image gains of 5-15% in log-likelihood and up to 2 percentage points in AUC. For the most affected images -- precisely those most relevant to failure case analysis -- improvements exceed 25%. We leverage these improved estimates to identify and analyze remaining failure cases of state-of-the-art saliency models, demonstrating that significant headroom for model improvement remains. More broadly, our findings highlight that empirical fixation densities should not be treated as fixed ground truths but as evolving estimates that improve with better methodology.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: p(\mathbf{x}\mid I)
\[ p(\mathbf{x}\mid I) \]
Matters: This is the probability density function of the fixation locations given the image I.

### Equation 2: \mathbf{x}=(x,y)
Matters: This represents the spatial location of fixation, with x and y being the coordinates.

### Equation 3: \mathcal{L}=\frac{1}{N}\sum_{i=1}^{N}\log p(\mathbf{x}_{i}\mid I)
\[ \mathcal{L} = \frac{1}{N} \sum_{i=1}^{N} \log p(\mathbf{x}_{i} \mid I) \]
Matters: This is the log-likelihood of the fixation locations given the image I, averaged over all fixation locations.

### Equation 4: \{\mathbf{x}_{i}\}_{i=1}^{N}
Matters: This represents the set of fixation locations.

### Equation 5: \log_{2}
Matters: This is the logarithm base 2.

### Equation 6: \{\mathbf{x}_{j}\}_{j=1}^{M}
Matters: This represents the set of data points used for kernel density estimation.

### Equation 7: \hat{p}_{\mathrm{KDE}}(\mathbf{x})=\frac{1}{M}\sum_{j=1}^{M}\mathcal{N}(\mathbf{x};\,\mathbf{x}_{j},h^{2}\mathbf{I})
\[ \hat{p}_{\mathrm{KDE}}(\mathbf{x}) = \frac{1}{M} \sum_{j=1}^{M} \mathcal{N}(\mathbf{x}; \mathbf{x}_{j}, h^{2} \mathbf{I}) \]
Matters: This is the kernel density estimate of the fixation locations, using a Gaussian kernel with bandwidth h.

### Equation 8: \mathbf{I}
Matters: This represents the image.

**Method Summary**
================

* The authors propose a new method for estimating fixation densities using a mixture model framework.
* The method combines adaptive bandwidth estimation with the mixture model framework.
* The authors evaluate their method on four datasets and compare it to a fixed-bandwidth isotropic Gaussian KDE.
* The method yields substantially higher log-likelihood estimates compared to the baseline method.

**Experimental Overview**
================--------

* The authors evaluate their method on four datasets: MIT1003, CAT2000 train split, COCO-Freeview validation split, and DAEMONS validation split.
* The primary metric used is log-likelihood, measured in bits per fixation relative to a uniform baseline model.
* The authors compare their method to a fixed-bandwidth isotropic Gaussian KDE with one degree of visual angle.
* The main claimed finding is that the proposed method yields substantially higher log-likelihood estimates compared to the baseline method.

**What to Verify in the PDF**
=============================

* The authors mention that the CAT2000 dataset has an artifact reported by [36] that needs to be removed.
* The authors also mention that the authors remove the artifact reported by [36] from the CAT2000 dataset.
* The authors provide extended per-image analyses for the case studies presented in the main paper.
* The authors provide extended cross-validation design analysis, including Figure 23, which shows both cross-validated and pooled estimates across all three DeepGaze configurations.
{% endraw %}
