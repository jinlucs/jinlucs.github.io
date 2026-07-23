---
layout: post
title: "Daily arXiv Digest — 2026-07-23 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) PG-KINN: A Physics-Informed Petrov-Galerkin Kolmogorov-Arnold Network for Solving Forward and Inverse PDEs
- **Authors:** Amirhossein Sadr, Nima Soltani, Vahideh Moghtadaiee, Aida Pakniyat, Dara Rahmati, Saeid Gorgin
- **arXiv:** [2607.20378](https://arxiv.org/abs/2607.20378v1) · [pdf](https://arxiv.org/pdf/2607.20378v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.20378v1))
- **Categories:** cs.LG, math.NA

### Abstract
> Physics-informed learning of partial differential equations (PDEs) has been dominated by multilayer perceptrons (MLPs), whose spectral bias and dense parameterization limit both accuracy and interpretability. Kolmogorov Arnold Networks (KANs) mitigate these limitations because their learnable spline activations are structurally aligned with the piecewise-polynomial bases of classical discretizations. However, the way a PDE is cast into a loss functional is as decisive as the choice of approximator: strong-form residual minimization requires high-order derivatives and heavily weighted losses, the energy (Bubnov-Galerkin) form is restricted to self-adjoint operators and, as we show, collapses to a trivial solution for parameter-identification problems, and boundary integral forms require a known fundamental solution. We propose PG-KINN, a physics-informed KAN built on a Petrov-Galerkin formulation in which the trial space is a KAN and the test space is an independent, compactly supported, piecewise-polynomial space evaluated with Gauss-Legendre quadrature. Integration by parts lowers the differentiation order while retaining applicability to general non-self-adjoint, nonlinear, and inverse problems; the localized test functions turn the global residual into a set of element-wise weak residuals with favorable conditioning. On a suite of benchmarks spanning crack singularities, stress concentration, Neo-Hookean hyperelasticity, inverse parameter identification in heterogeneous media, and complex geometries, PG-KINN consistently outperforms legacy MLP baselines and state-of-the-art KAN-based strong/energy/inverse formulations (PIKAN). These results position the Petrov-Galerkin coupling of KAN trial spaces and polynomial test spaces as a robust and accurate route for AI-based computational mechanics.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: C^{0}

* Equation: C^{0} = \sum_{i=1}^{G+r} c^{(i)}_{0} B_{0}(x_{i})
* Symbols:
	+ C^{0} (residual)
	+ c^{(i)}_{0} (coefficients)
	+ B_{0}(x_{i}) (basis functions)
* Why it matters: This equation represents the residual of the forward problem, which is used to compute the loss function in the inverse problem.

### Equation 2: l_{i}

* Equation: l_{i} = \sum_{j=1}^{G+r} c^{(i,j)}_{j} \phi_{ij}(x_{j})
* Symbols:
	+ l_{i} (residual)
	+ c^{(i,j)}_{j} (coefficients)
	+ \phi_{ij}(x_{j}) (basis functions)
* Why it matters: This equation represents the residual of the forward problem in the Petrov-Galerkin formulation.

### Equation 3: l_{o}

* Equation: l_{o} = \sum_{i=1}^{G+r} c^{(i)}_{o} B_{o}(x_{i})
* Symbols:
	+ l_{o} (residual)
	+ c^{(i)}_{o} (coefficients)
	+ B_{o}(x_{i}) (basis functions)
* Why it matters: This equation represents the residual of the forward problem in the Petrov-Galerkin formulation.

### Equation 4: \phi_{ij}

* Equation: \phi_{ij}(x_{j}) = \sum_{m=1}^{G+r} c^{(i,j)}_{m} B_{m}(x_{j})
* Symbols:
	+ \phi_{ij}(x_{j}) (basis functions)
	+ c^{(i,j)}_{m} (coefficients)
	+ B_{m}(x_{j}) (basis functions)
* Why it matters: This equation represents the basis functions used in the Petrov-Galerkin formulation.

### Equation 5: \phi_{ij}(x_{j})=\sum_{m=1}^{G+r}c^{(i,j)}_{m}\,B_{m}(x_{j})

* Equation: \phi_{ij}(x_{j})=\sum_{m=1}^{G+r}c^{(i,j)}_{m}\,B_{m}(x_{j})
* Symbols:
	+ \phi_{ij}(x_{j}) (basis functions)
	+ c^{(i,j)}_{m} (coefficients)
	+ B_{m}(x_{j}) (basis functions)
* Why it matters: This equation represents the basis functions used in the Petrov-Galerkin formulation.

**Method Summary**
==================

* PG-KINN is a physics-informed KAN built on a Petrov-Galerkin formulation.
* The trial space is a KAN and the test space is an independent, compactly supported, piecewise-polynomial space evaluated with Gauss-Legendre quadrature.
* The Petrov-Galerkin coupling of KAN trial spaces and polynomial test spaces is used to mitigate the limitations of traditional KAN-based methods.
* The method is robust and accurate for solving forward and inverse PDEs.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Benchmarks drawn from computational solid mechanics.
	+ Examples include crack singularities, stress concentration, Neo-Hookean hyperelasticity, inverse parameter identification in heterogeneous media, and complex geometries.
* Baselines/Comparisons:
	+ Legacy MLP baselines.
	+ State-of-the-art KAN-based strong/energy/inverse formulations (PIKAN).
* Main Claimed Findings:
	+ PG-KINN consistently outperforms legacy MLP baselines and state-of-the-art KAN-based strong/energy/inverse formulations.
	+ The one exception is extreme complex geometries, where the axis-aligned spline grid remains a bottleneck.

**What to Verify in the PDF**
=============================

* The mathematical derivation of the Petrov-Galerkin weak form in Section 4.1.
* The energy-based inverse problem collapse in Section 3.4.
* The numerical experiments and results in Section 5.
{% endraw %}

{% raw %}
## 2) Statevector-Referenced Geometry Survival of a Four-Qubit ZZ Quantum Kernel on IBM Quantum Hardware: A Fixed-Subset Diagnostic Across Three Execution Configurations
- **Authors:** Rostyslav Sipakov
- **arXiv:** [2607.20377](https://arxiv.org/abs/2607.20377v1) · [pdf](https://arxiv.org/pdf/2607.20377v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.20377v1))
- **Categories:** quant-ph, cs.LG

### Abstract
> Quantum-kernel methods encode a dataset's geometry in a Gram matrix, so learning claims on hardware kernels assume the intended geometry survives execution. We measure that survival for one frozen four-qubit ZZ feature-map kernel on $N=24$ real indoor air-quality windows, reconstructed on ibm_fez (1024 shots per circuit) under baseline, dynamical decoupling alone, and gate twirling alone, each a single non-interleaved job. Every configuration returned a complete, finite, positive-semidefinite Gram matrix and preserved the centered statevector geometry to a substantial but incomplete descriptive degree (full-matrix centered kernel alignment, CKA, 0.933-0.989). Gate twirling was most faithful on every reported geometry axis, with the only jackknife-resolved improvement over baseline (persisted Spearman, mean absolute error, and full-matrix CKA diagnostics); dynamical decoupling alone was not separated from baseline at the frozen-window scale. Residual hardware distortion, not finite sampling, dominates the discrepancy. Yet fidelity and label alignment were reversed: the most faithful configuration had the lowest centered kernel-target alignment, which sits at or below label-permutation references for statevector and hardware alike. We read the small hardware uplift as a normalization property of the non-affine distortion, not captured signal. These are descriptive results for single jobs on one backend, not causal mitigation-efficacy estimates; no quantum-advantage, hardware-classifier-superiority, or forecasting claim is made. Implementation fidelity and task relevance are distinct axes; hardware quantum machine-learning studies should report both.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: N=24

* Equation: N=24
* Symbols: N
* Why it matters: This equation represents the number of real indoor air-quality windows used in the dataset.

### Equation 2: x ↦ |φ(x)⟩

* Equation: x ↦ |φ(x)⟩
* Symbols: x, |φ(x)⟩
* Why it matters: This equation represents the mapping from input data x to a quantum state |φ(x)⟩.

### Equation 3: K(x_i, x_j) = ||⟨φ(x_i) | φ(x_j)⟩||^2

* Equation: K(x_i, x_j) = ||⟨φ(x_i) | φ(x_j)⟩||^2
* Symbols: x_i, x_j, K(x_i, x_j), |φ(x_i)⟩, |φ(x_j)⟩
* Why it matters: This equation represents the Gram matrix K, which encodes the geometry of the dataset.

### Equation 4: [0, π]

* Equation: [0, π]
* Symbols: [0, π]
* Why it matters: This equation represents the range of values for the quantum state |φ(x)⟩.

### Equation 5: Not found in extracted context

**Method Summary**
================

* The authors used a four-qubit ZZ feature-map kernel to encode the geometry of the dataset.
* The dataset consists of real indoor air-quality monitoring data with a 30-minute window stride and a one-hour prediction horizon.
* The authors performed a fixed-subset diagnostic across three execution configurations: baseline, dynamical decoupling alone, and gate twirling alone.

**Experimental Overview**
=====================

* Tasks/Datasets: Binary event-onset forecasting on real indoor air-quality monitoring data.
* Baselines/Comparisons: Baseline, dynamical decoupling alone, and gate twirling alone.
* Main claimed findings: The authors measured the survival of the four-qubit ZZ feature-map kernel on IBM Quantum hardware across three execution configurations, with gate twirling being the most faithful on every reported geometry axis.

**What to Verify in the PDF**
==========================

* The authors' implementation fidelity and task relevance are distinct axes, and hardware quantum machine-learning studies should report both.
* The discrepancy between the most faithful configuration and the lowest centered kernel-target alignment is due to residual hardware distortion, not finite sampling.
* The authors' results are descriptive, not causal mitigation-efficacy estimates, and no quantum-advantage, hardware-classifier-superiority, or forecasting claim is made.
{% endraw %}

{% raw %}
## 3) Online Variance Reduction for Domain Adaptation on Streaming Data
- **Authors:** Andrea Napoli
- **arXiv:** [2607.20374](https://arxiv.org/abs/2607.20374v1) · [pdf](https://arxiv.org/pdf/2607.20374v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.20374v1))
- **Categories:** cs.LG

### Abstract
> This paper studies the problem of stochastic variance reduction (SVR) for the maximum mean discrepancy (MMD) and correlation alignment (CORAL) loss functions. Although various offline SVR algorithms for these losses have been proposed, these are incompatible with online, distributed, or incremental learning settings. This paper presents Adaptive vaRiance Reduction via Online reWeighting (ARROW), the first online SVR algorithm for the MMD and CORAL for streamed data. The method maintains moving average references of the alignment statistics, and adaptively reweights incoming minibatches so that the minibatch and reference statistics are aligned. Further, we propose a relaxed reweighting scheme so that the ensuing weight-optimisation problem is tractable. In experiments and simulations, we show that ARROW performs competitively with offline algorithms in terms of runtime, degree of variance reduction achieved, and target domain accuracy.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `x_{s},y_{s} x_{s},y_{s}`
* Equation: Not explicitly defined in the context
* Symbols: `x_{s}`, `y_{s}`
* Why it matters: Not found in extracted context.

### Equation 2: `x_{t} x_{t}`
* Equation: Not explicitly defined in the context
* Symbols: `x_{t}`
* Why it matters: Not found in extracted context.

### Equation 3: `h=g\circ f h=g\circ f`
* Equation: Not explicitly defined in the context
* Symbols: `h`, `g`, `f`
* Why it matters: Not found in extracted context.

### Equation 4: `z_{s}=f\left(x_{s}\right),\ \ z_{t}=f\left(x_{t}\right) z_{s}=f\left(x_{s}\right),\ \ z_{t}=f\left(x_{t}\right)`
* Equation: Not explicitly defined in the context
* Symbols: `z_{s}`, `z_{t}`, `f`, `x_{s}`, `x_{t}`
* Why it matters: Not found in extracted context.

### Equation 5: `L=L_{\mathrm{task}}\left(h\left(x_{s}\right),y_{s}\right)+\lambda L_{\mathrm{disc}}\left(z_{s},z_{t}\right), L=L_{\mathrm{task}}\left(h\left(x_{s}\right),y_{s}\right)+\lambda L_{\mathrm{disc}}\left(z_{s},z_{t}\right)`
* Equation: Maximum mean discrepancy (MMD) loss function
* Symbols: `L`, `L_{\mathrm{task}}`, `L_{\mathrm{disc}}`, `h`, `x_{s}`, `y_{s}`, `z_{s}`, `z_{t}`, `λ`
* Why it matters: This is the loss function used for domain adaptation, which is the main objective of the paper.

### Equation 6: `\lambda>0 λ>0`
* Equation: Trade-off parameter for the distribution-matching regulariser
* Symbols: `λ`
* Why it matters: This parameter controls the balance between the task loss and the distribution-matching regulariser.

### Equation 7: `L_{\mathrm{disc}} L_{\mathrm{disc}}`
* Equation: Distribution-matching regulariser
* Symbols: `L_{\mathrm{disc}}`
* Why it matters: This regulariser is used to align the feature distributions between the source and target domains.

### Equation 8: `L_{\operatorname{MMD}}=\left\|\mu_{s}-\mu_{t}\right\|_{\mathcal{H}}^{2} L_{\operatorname{MMD}}=\left\|\mu_{s}-\mu_{t}\right\|_{\mathcal{H}}^{2}`
* Equation: Maximum mean discrepancy (MMD) loss function (simplified)
* Symbols: `L_{\operatorname{MMD}}`, `μ_{s}`, `μ_{t}`, `∥⋅∥_{\mathcal{H}}`
* Why it matters: This is a simplified version of the MMD loss function, which measures the difference between the mean of the source and target distributions.

**Method Summary**
================

* The paper proposes Adaptive Variance Reduction via Online reWeighting (ARROW), an online stochastic variance reduction (SVR) algorithm for the maximum mean discrepancy (MMD) and correlation alignment (CORAL) loss functions.
* ARROW maintains moving average references of the alignment statistics and adaptively reweights incoming minibatches to align the minibatch and reference statistics.
* The method uses a relaxed reweighting scheme to make the weight-optimisation problem tractable.

**Experimental Overview**
=====================

* The paper evaluates ARROW on three criteria: degree of variance reduction achieved, target domain accuracy, and training speed.
* The experiments use Monte Carlo simulations to compare the estimator variance for different SVR methods across different values of k.
* The datasets used are 2D standard normal data with n_{s}=n_{t}=4,000 samples.
* The baselines compared are uniform random sampling, diverse sampling using k-means++ (Arthur and Vassilvitskii, 2007), stratified sampling (VaRDASS), order-aware sampling (ORDERED), and paired sampling (PSDA).

**What to Verify in the PDF**
==========================

* The implementation details of the ARROW algorithm, including the choice of hyperparameters and the optimization procedure.
* The theoretical analysis of the ARROW algorithm, including the convergence rate and the variance reduction bound.
* The results of the experiments, including the degree of variance reduction achieved, target domain accuracy, and training speed, for different values of k and datasets.
{% endraw %}

{% raw %}
## 4) Local minimizers in $\mathbb{R}^n$ of vector Allen-Cahn with an $(n+1)$-junction
- **Authors:** Abhishek Adimurthi
- **arXiv:** [2607.20369](https://arxiv.org/abs/2607.20369v1) · [pdf](https://arxiv.org/pdf/2607.20369v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.20369v1))
- **Categories:** math.AP, math.OC

### Abstract
> For a domain $Ω$ that is a deformation of a unit ball in $\mathbb{R}^n$, we establish the existence of a sequence of local minimizers for the vector Allen-Cahn energy having $n+1$ wells. This sequence converges in the $L^1$ topology to a partition of $Ω$ whose skeleton is given by a simplex cone that contains an $(n+1)$-junction point. This is accomplished by proving that the partition is an isolated local minimizer of a weighted perimeter problem arising as the associated $Γ$-limit of the sequence of Allen-Cahn functionals. The results established in this article generalize those in the author's earlier article with Peter Sternberg (MR5033050), which dealt with the case $n=3$. We also weaken the one crucial assumption from the author's earlier article with Peter Sternberg (MR5033050).
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathbb{R}^{n}$

* Equation: $\mathbb{R}^{n}$
* Symbols: None
* Why it matters: This is the domain space where the problem is defined.

### Equation 2: $(n+1)$

* Equation: $(n+1)$
* Symbols: None
* Why it matters: This represents the number of wells in the vector Allen-Cahn energy.

### Equation 3: $\Omega$

* Equation: $\Omega$
* Symbols: None
* Why it matters: This is the domain where the partition is constructed.

### Equation 4: $L^{1}$

* Equation: $L^{1}$
* Symbols: None
* Why it matters: This is the topology used to measure the distance between the partition and the minimizer.

### Equation 5: $\Gamma$

* Equation: $\Gamma$
* Symbols: None
* Why it matters: This represents the limit of the sequence of Allen-Cahn functionals.

**Method Summary**
==================

* The authors construct a domain $\Omega$ and a partition $\mathcal{S}$ of $\Omega$ into $n+1$ regions such that the interior weighted surface area is minimized in the $L^{1}$ topology.
* The partition is constructed using a simplex cone with an $(n+1)$-junction point.
* The authors use the machinery of $\Gamma$-convergence to establish the existence of a local minimizer of the associated weighted perimeter problem.

**Experimental Overview**
=========================

* Tasks: Construct a domain $\Omega$ and a partition $\mathcal{S}$ of $\Omega$ into $n+1$ regions such that the interior weighted surface area is minimized in the $L^{1}$ topology.
* Datasets: None
* Baselines: None
* Main claimed findings: The authors establish the existence of a local minimizer of the associated weighted perimeter problem, which converges in the $L^{1}$ topology to a partition of $\Omega$ whose skeleton is given by a simplex cone with an $(n+1)$-junction point.

**What to Verify in the PDF**
=============================

* The authors' construction of the domain $\Omega$ and the partition $\mathcal{S}$ of $\Omega$ into $n+1$ regions.
* The minimization of the interior weighted surface area in the $L^{1}$ topology.
* The convergence of the sequence of Allen-Cahn functionals to a local minimizer of the associated weighted perimeter problem.
{% endraw %}

{% raw %}
## 5) Variance-reduced Domain Adaptation using Paired Sampling
- **Authors:** Andrea Napoli
- **arXiv:** [2607.20367](https://arxiv.org/abs/2607.20367v1) · [pdf](https://arxiv.org/pdf/2607.20367v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.20367v1))
- **Categories:** cs.LG

### Abstract
> Correlation alignment and the maximum mean discrepancy are two widely used distribution-matching frameworks for unsupervised domain adaptation (UDA). However, high variance in these losses has been shown to undermine their effectiveness in minibatch optimisation settings. Furthermore, the losses lack finite-sum structure, which renders them incompatible with classical stochastic variance reduction (SVR) methods. This paper proposes Paired Sampling for Domain Adaptation (PSDA), a novel SVR technique tailored to such objectives. PSDA pairs observations both within and across domains, to form quadruplets that are always sampled together during training. The pairings are designed to minimise expected gradient variance, and reduce to solving a set of linear assignment problems. Our simulations demonstrate reduced variance compared to related methods, and experiments on three domain shift datasets show improved target domain accuracy.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Dataset Definitions
```markdown
\mathcal{D}_{s}=\left\{\left(x_{i}^{s},y_{i}^{s}\right)\right\}_{i=1}^{n_{s}}
```
* Equation: Definition of the source dataset `D_s`
* Symbols: `x_i^s`, `y_i^s`, `n_s`
* Why it matters: Defines the source dataset, which is used for supervised task loss and distribution-matching regularizer.

### Equation 2: Target Dataset Definition
```markdown
\mathcal{D}_{t}=\left\{x_{j}^{t}\right\}_{j=1}^{n_{t}}
```
* Equation: Definition of the target dataset `D_t`
* Symbols: `x_j^t`, `n_t`
* Why it matters: Defines the target dataset, which is used for distribution-matching regularizer.

### Equation 3: Model Composition
```markdown
h=g\circ f
```
* Equation: Composition of the model `h` and feature extractor `f`
* Symbols: `h`, `g`, `f`
* Why it matters: Defines the overall model architecture, where `g` is the prediction head and `f` is the feature extractor.

### Equation 4: Feature Representations
```markdown
z_{i}^{s}=f\left(x_{i}^{s}\right),\ \ z_{i}^{t}=f\left(x_{j}^{t}\right)
```
* Equation: Feature representations `z_i^s` and `z_i^t` for source and target datasets
* Symbols: `z_i^s`, `z_i^t`, `x_i^s`, `x_j^t`, `f`
* Why it matters: Defines the feature representations used for distribution-matching regularizer.

### Equation 5: Task Loss
```markdown
L_{\mathrm{task}}\left(h\left(x^{s}\right),y^{s}\right)
```
* Equation: Task loss function for supervised task
* Symbols: `L_task`, `h`, `x^s`, `y^s`
* Why it matters: Defines the supervised task loss function, which is optimized on the source dataset.

**Method Summary**
==================

* The proposed method, Paired Sampling for Domain Adaptation (PSDA), uses paired sampling to minimize expected gradient variance.
* PSDA pairs observations both within and across domains to form quadruplets that are always sampled together during training.
* The pairings are designed to minimize expected gradient variance and reduce to solving a set of linear assignment problems.
* PSDA considers two specific options for the distribution-matching regularizer: MMD and CORAL.

**Experimental Overview**
==========================

* The proposed method, PSDA, is evaluated on three domain shift datasets.
* The evaluation criteria include degree of variance reduction achieved, target domain accuracy, and training speed.
* PSDA is compared to two variants: "Paired sampling" and "Double-paired", which perform only Stage 1 and both Stage 1 and Stage 2 matching, respectively.
* The baselines for comparison include uniform random sampling, diverse sampling using k-means++, stratified sampling (VaRDASS), and order-aware sampling (ORDERED).

**What to Verify in the PDF**
=============================

* The mathematical formulation of the expected gradient variance minimization problem.
* The linear assignment problem formulation and its solution.
* The experimental results for the three domain shift datasets, including the degree of variance reduction achieved, target domain accuracy, and training speed.
* The comparison of PSDA with the baselines, including the results for "Paired sampling" and "Double-paired" variants.
{% endraw %}
