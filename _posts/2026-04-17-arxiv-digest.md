---
layout: post
title: "Daily arXiv Digest — 2026-04-17 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Structural interpretability in SVMs with truncated orthogonal polynomial kernels
- **Authors:** Víctor Soto-Larrosa, Nuria Torrado, Edmundo J. Huertas
- **arXiv:** [2604.15285](https://arxiv.org/abs/2604.15285v1) · [pdf](https://arxiv.org/pdf/2604.15285v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.15285v1))
- **Categories:** stat.ML, cs.LG, math.ST

### Abstract
> We study post-training interpretability for Support Vector Machines (SVMs) built from truncated orthogonal polynomial kernels. Since the associated reproducing kernel Hilbert space is finite-dimensional and admits an explicit tensor-product orthonormal basis, the fitted decision function can be expanded exactly in intrinsic RKHS coordinates. This leads to Orthogonal Representation Contribution Analysis (ORCA), a diagnostic framework based on normalized Orthogonal Kernel Contribution (OKC) indices. These indices quantify how the squared RKHS norm of the classifier is distributed across interaction orders, total polynomial degrees, marginal coordinate effects, and pairwise contributions. The methodology is fully post-training and requires neither surrogate models nor retraining. We illustrate its diagnostic value on a synthetic double-spiral problem and on a real five-dimensional echocardiogram dataset. The results show that the proposed indices reveal structural aspects of model complexity that are not captured by predictive accuracy alone.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{X}\subseteq\mathbb{R}^{d}$

* Equation: $\mathcal{X}\subseteq\mathbb{R}^{d}$
* Symbols: $\mathcal{X}$, $\mathbb{R}^{d}$
* Why it matters: This equation defines the input space $\mathcal{X}$ as a subset of $\mathbb{R}^{d}$, which is the space of all $d$-dimensional real vectors.

### Equation 2: $\{(\mathbf{x}_{i},y_{i})_{i=1}^{m},\qquad\mathbf{x}_{i}\in\mathcal{X},\qquad y_{i}\in\{-1,+1\}$

* Equation: $\{(\mathbf{x}_{i},y_{i})_{i=1}^{m},\qquad\mathbf{x}_{i}\in\mathcal{X},\qquad y_{i}\in\{-1,+1\}$
* Symbols: $\mathbf{x}_{i}$, $y_{i}$, $\mathcal{X}$, $m$
* Why it matters: This equation defines the dataset $\{(\mathbf{x}_{i},y_{i})_{i=1}^{m}\}$, where each data point is a pair $(\mathbf{x}_{i},y_{i})$ with $\mathbf{x}_{i}\in\mathcal{X}$ and $y_{i}\in\{-1,+1\}$.

### Equation 3: $\mathbf{x}$

* Equation: $\mathbf{x}$
* Symbols: $\mathbf{x}$
* Why it matters: This equation is likely a placeholder for a vector $\mathbf{x}$, which is a common notation in machine learning and linear algebra.

### Equation 4: $\mathbf{z}$

* Equation: $\mathbf{z}$
* Symbols: $\mathbf{z}$
* Why it matters: This equation is likely a placeholder for another vector $\mathbf{z}$, which is another common notation in machine learning and linear algebra.

### Equation 5: $\mathcal{X}$

* Equation: $\mathcal{X}$
* Symbols: $\mathcal{X}$
* Why it matters: This equation is the same as Equation 1, defining the input space $\mathcal{X}$ as a subset of $\mathbb{R}^{d}$.

### Equation 6: $y_{i}$

* Equation: $y_{i}$
* Symbols: $y_{i}$
* Why it matters: This equation defines the labels $y_{i}$, which are either $-1$ or $+1$.

### Equation 7: $\alpha_{i}$

* Equation: $\alpha_{i}$
* Symbols: $\alpha_{i}$
* Why it matters: This equation is likely a placeholder for a scalar $\alpha_{i}$, which is a common notation in machine learning and linear algebra.

### Equation 8: $K:\mathcal{X}\times\mathcal{X}\to\mathbb{R},\qquad K(\mathbf{x},\mathbf{z})=K(\mathbf{z},\mathbf{x})$

* Equation: $K:\mathcal{X}\times\mathcal{X}\to\mathbb{R},\qquad K(\mathbf{x},\mathbf{z})=K(\mathbf{z},\mathbf{x})$
* Symbols: $K$, $\mathcal{X}$, $\mathbb{R}$
* Why it matters: This equation defines the kernel function $K$, which maps pairs of input vectors $\mathbf{x}$ and $\mathbf{z}$ to real numbers in $\mathbb{R}$. The kernel is symmetric, meaning $K(\mathbf{x},\mathbf{z})=K(\mathbf{z},\mathbf{x})$.

**Method Summary**
================

* The authors propose a post-training interpretability method for Support Vector Machines (SVMs) built from truncated orthogonal polynomial kernels.
* The method, called Orthogonal Representation Contribution Analysis (ORCA), provides a principled decomposition of the model into contributions associated with different interaction orders and total polynomial degrees.
* ORCA uses the orthogonality of the underlying polynomial basis to decompose the squared RKHS norm of the trained component into interaction orders, marginal coordinate effects, and pairwise contributions.
* The authors illustrate the diagnostic value of ORCA on a synthetic double-spiral problem and a real five-dimensional echocardiogram dataset.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Synthetic double-spiral dataset
	+ Real five-dimensional echocardiogram dataset
* Baselines/Comparisons:
	+ Not mentioned in the extracted context
* Main Claimed Findings:
	+ ORCA provides a principled decomposition of the model into contributions associated with different interaction orders and total polynomial degrees.
	+ The proposed method reveals structural aspects of model complexity that are not captured by predictive accuracy alone.

**What to Verify in the PDF**
==========================

* The authors mention that the kernel design is based on Jacobi tensor-product kernels, but the details of this are not provided in the extracted context.
* The authors also mention that the regularisation parameter $C$ is reported alongside each configuration, but the exact values are not provided.
* The authors mention that the OKC indices are normalized, but the normalization process is not described in detail.
* The authors mention that the ORCA framework is fully post-training and requires neither surrogate models nor retraining, but the details of this are not provided.
{% endraw %}

{% raw %}
## 2) How Embeddings Shape Graph Neural Networks: Classical vs Quantum-Oriented Node Representations
- **Authors:** Nouhaila Innan, Antonello Rosato, Alberto Marchisio, Muhammad Shafique
- **arXiv:** [2604.15273](https://arxiv.org/abs/2604.15273v1) · [pdf](https://arxiv.org/pdf/2604.15273v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.15273v1))
- **Categories:** cs.LG, quant-ph

### Abstract
> Node embeddings act as the information interface for graph neural networks, yet their empirical impact is often reported under mismatched backbones, splits, and training budgets. This paper provides a controlled benchmark of embedding choices for graph classification, comparing classical baselines with quantum-oriented node representations under a unified pipeline. We evaluate two classical baselines alongside quantum-oriented alternatives, including a circuit-defined variational embedding and quantum-inspired embeddings computed via graph operators and linear-algebraic constructions. All variants are trained and tested with the same backbone, stratified splits, identical optimization and early stopping, and consistent metrics. Experiments on five different TU datasets and on QM9 converted to classification via target binning show clear dataset dependence: quantum-oriented embeddings yield the most consistent gains on structure-driven benchmarks, while social graphs with limited node attributes remain well served by classical baselines. The study highlights practical trade-offs between inductive bias, trainability, and stability under a fixed training budget, and offers a reproducible reference point for selecting quantum-oriented embeddings in graph learning.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `G = (V, E)`
#### Symbols:
- `G`: graph
- `V`: set of nodes
- `E`: set of edges

#### Why it matters:
This equation represents the basic structure of a graph, which is a fundamental input for graph neural networks.

### Equation 2: `ϕ θ (⋅) = 𝐙 ∈ ℝ |V| × d`
#### Symbols:
- `ϕ θ (⋅)`: node-embedding module
- `θ`: model parameters
- `⋅`: input node
- `𝐙`: node embedding
- `|V|`: number of nodes
- `d`: dimensionality of node embeddings

#### Why it matters:
This equation describes the node-embedding module, which is responsible for generating node representations that are fed into the downstream classifier.

### Equation 3: `𝐙 ∈ ℝ |V| × d`
#### Symbols:
- `𝐙`: node embedding
- `|V|`: number of nodes
- `d`: dimensionality of node embeddings

#### Why it matters:
This equation specifies the output of the node-embedding module, which is a matrix of size `|V| × d` representing the node representations.

### Equation 4: `G_v`
#### Symbols:
- `G_v`: subgraph induced by node `v`
- `v`: node

#### Why it matters:
This notation is used to refer to the subgraph induced by a specific node `v`, which is relevant in the context of graph neural networks.

### Equation 5: `H_v`
#### Symbols:
- `H_v`: set of neighbors of node `v`
- `v`: node

#### Why it matters:
This notation refers to the set of neighbors of a node `v`, which is an important aspect of graph structure that is used in graph neural networks.

**Method Summary**
================

* The authors evaluate classical and quantum-oriented node representations in a controlled graph-classification pipeline.
* The node-embedding module is the only variable being compared across different methods.
* The downstream classifier is fixed (GIN backbone) and the same for all methods.
* The authors aim to isolate the effect of node representations on graph-level prediction.

**Experimental Overview**
=====================

* Tasks: graph classification
* Datasets: five different TU datasets and QM9 converted to classification via target binning
* Baselines: two classical baselines (Fixed and MLP), four quantum-oriented embeddings (Angle-VQC, QuOp, QWalkVec, and QPE)
* Main claimed findings: quantum-oriented embeddings provide improvements over strong classical baselines on structure-driven benchmarks, but not on social graphs with limited node attributes.

**What to Verify in the PDF**
==========================

* The details of the quantum-inspired constructions (QuOp, QWalkVec, and QPE) and how they are computed from graph operators and linear-algebraic transformations.
* The specific implementation of the Angle-VQC embedding and how it is parameterized using PennyLane's default.qubit simulator.
* The evaluation setup, including the specific hyperparameters and optimization settings used for each method.
{% endraw %}

{% raw %}
## 3) Prism: Symbolic Superoptimization of Tensor Programs
- **Authors:** Mengdi Wu, Xiaoyu Jiang, Oded Padon, Zhihao Jia
- **arXiv:** [2604.15272](https://arxiv.org/abs/2604.15272v1) · [pdf](https://arxiv.org/pdf/2604.15272v1)
- **LLM context source:** abstract only
- **Categories:** cs.PL, cs.AI, cs.LG

### Abstract
> This paper presents Prism, the first symbolic superoptimizer for tensor programs. The key idea is sGraph, a symbolic, hierarchical representation that compactly encodes large classes of tensor programs by symbolically representing some execution parameters. Prism organizes optimization as a two-level search: it constructs symbolic graphs that represent families of programs, and then instantiates them into concrete implementations. This formulation enables structured pruning of provably suboptimal regions of the search space using symbolic reasoning over operator semantics, algebraic identities, and hardware constraints. We develop techniques for efficient symbolic graph generation, equivalence verification via e-graph rewriting, and parameter instantiation through auto-tuning. Together, these components allow Prism to bridge the rigor of exhaustive search with the scalability required for modern ML workloads. Evaluation on five commonly used LLM workloads shows that Prism achieves up to $2.2\times$ speedup over best superoptimizers and $4.9\times$ over best compiler-based approaches, while reducing end-to-end optimization time by up to $3.4\times$.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

Unfortunately, the extracted context does not provide any mathematical equations to walkthrough.

**Method Summary**
================

* Prism organizes optimization as a two-level search: constructing symbolic graphs that represent families of programs and then instantiating them into concrete implementations.
* The symbolic graphs are generated using techniques for efficient symbolic graph generation.
* Equivalence verification is performed via e-graph rewriting.
* Parameter instantiation is achieved through auto-tuning.
* The approach enables structured pruning of provably suboptimal regions of the search space using symbolic reasoning over operator semantics, algebraic identities, and hardware constraints.

**Experimental Overview**
=======================

* Tasks/Datasets: Five commonly used LLM workloads.
* Baselines/Comparisons: Best superoptimizers and best compiler-based approaches.
* Main Claimed Findings:
	+ Prism achieves up to $2.2\times$ speedup over best superoptimizers.
	+ Prism achieves up to $4.9\times$ speedup over best compiler-based approaches.
	+ Prism reduces end-to-end optimization time by up to $3.4\times$.

**What to Verify in the PDF**
==========================

* Details on the e-graph rewriting technique used for equivalence verification.
* The specific algebraic identities and hardware constraints used for symbolic reasoning.
* The auto-tuning approach used for parameter instantiation.
{% endraw %}

{% raw %}
## 4) Stability and Generalization in Looped Transformers
- **Authors:** Asher Labovich
- **arXiv:** [2604.15259](https://arxiv.org/abs/2604.15259v1) · [pdf](https://arxiv.org/pdf/2604.15259v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.AI

### Abstract
> Looped transformers promise test-time compute scaling by spending more iterations on harder problems, but it remains unclear which architectural choices let them extrapolate to harder problems at test time rather than memorize training-specific solutions. We introduce a fixed-point based framework for analyzing looped architectures along three axes of stability -- reachability, input-dependence, and geometry -- and use it to characterize when fixed-point iteration yields meaningful predictions. Theoretically, we prove that looped networks without recall have countable fixed points and cannot achieve strong input-dependence at any spectral regime, while recall combined with outer normalization reliably produces a regime in which fixed points are simultaneously reachable, locally smooth in the input, and supported by stable backpropagation. Empirically, we train single-layer looped transformers on chess, sudoku, and prefix-sums and find that downstream performance tracks the framework's predictions across tasks and architectural configurations. We additionally introduce internal recall, a novel recall placement variant, and show that it becomes competitive with -- and on sudoku, substantially better than -- standard recall placement once outer normalization is applied.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### 1. Theoretical Analysis of Fixed Points

The paper introduces a fixed-point based framework for analyzing looped architectures. The first equation is not explicitly provided, but it is mentioned that looped networks without recall have countable fixed points.

* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation is crucial in understanding the theoretical stability of looped networks without recall.

### 2. Reachability of Fixed Points

The paper proves that looped networks without recall have countable fixed points and cannot achieve strong input-dependence at any spectral regime.

* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation highlights the limitations of looped networks without recall in achieving strong input-dependence.

### 3. Geometry of Fixed Points

The paper introduces a framework for analyzing the geometry of fixed points. However, the specific equation is not provided.

* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation is essential in understanding the geometric properties of fixed points in looped networks.

### 4. Outer Normalization

The paper discusses the importance of outer normalization in achieving stable backpropagation.

* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation is crucial in understanding the role of outer normalization in stabilizing backpropagation.

### 5. Internal Recall Placement

The paper introduces internal recall placement, a novel recall placement variant.

* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation is essential in understanding the performance of internal recall placement in achieving competitive results.

**Method Summary**
================

* The paper introduces a fixed-point based framework for analyzing looped architectures along three axes of stability: reachability, input-dependence, and geometry.
* The framework is used to characterize when fixed-point iteration yields meaningful predictions.
* The authors prove that looped networks without recall have countable fixed points and cannot achieve strong input-dependence at any spectral regime.
* The authors empirically train single-layer looped transformers on chess, sudoku, and prefix-sums and find that downstream performance tracks the framework's predictions.
* The authors introduce internal recall, a novel recall placement variant, and show that it becomes competitive with -- and on sudoku, substantially better than -- standard recall placement once outer normalization is applied.

**Experimental Overview**
=====================

* Tasks/Datasets: Chess, sudoku, and prefix-sums
* Baselines/Comparisons: Standard recall placement and internal recall placement
* Main claimed findings: Downstream performance tracks the framework's predictions, internal recall placement becomes competitive with standard recall placement once outer normalization is applied.

**What to Verify in the PDF**
=========================

* The mathematical derivations of the theoretical analysis of fixed points, reachability, geometry, and outer normalization.
* The empirical results of the experiments, including the performance of internal recall placement and its comparison to standard recall placement.
* The detailed explanation of the fixed-point based framework and its application to looped architectures.
{% endraw %}

{% raw %}
## 5) Lightweight Real-Time ALADIN for Distributed Optimization
- **Authors:** Yifei Wang, Xuhui Feng, Shimin Pan, Liangfan Zhu, Xu Du, Apostolos I. Rikos
- **arXiv:** [2604.15176](https://arxiv.org/abs/2604.15176v1) · [pdf](https://arxiv.org/pdf/2604.15176v1)
- **LLM context source:** abstract only
- **Categories:** math.OC

### Abstract
> This paper presents a real-time computational framework for multi-node distributed optimization by extending the Augmented Lagrangian Alternating Direction Inexact Newton (ALADIN) algorithm. Our approach integrates adjoint sequential quadratic programming (SQP) techniques to enable efficient approximation of Jacobian information within the ALADIN embedded quadratic program, thereby reducing communication overhead. Furthermore, to decrease computational complexity, we design an event-triggered update strategy that avoids updating Hessian and Jacobian matrices at every iteration. The proposed method achieves local convergence and enhanced communication efficiency, making it well suited for time-critical applications. Numerical experiments demonstrate that our approach achieves competitive performance while exhibiting superior computational efficiency in real-time scenarios, validating its practical applicability for time-sensitive distributed optimization challenges.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Augmented Lagrangian Alternating Direction Inexact Newton (ALADIN) algorithm

Not found in extracted context.

### 2. Adjoint Sequential Quadratic Programming (SQP) techniques

Not found in extracted context.

### 3. Event-triggered update strategy

Not found in extracted context.

### 4. Hessian and Jacobian matrices

Not found in extracted context.

### 5. Local convergence

Not found in extracted context.

**Method Summary**
==================

* The authors extend the ALADIN algorithm to enable efficient approximation of Jacobian information using adjoint SQP techniques.
* The approach integrates SQP into the ALADIN algorithm to reduce communication overhead.
* An event-triggered update strategy is designed to avoid updating Hessian and Jacobian matrices at every iteration.
* The method achieves local convergence and enhanced communication efficiency.

**Experimental Overview**
=======================

* Tasks/Datasets: Not found in extracted context.
* Baselines/Comparisons: Not found in extracted context.
* Main claimed findings: The proposed approach achieves competitive performance while exhibiting superior computational efficiency in real-time scenarios.

**What to Verify in the PDF**
==========================

* Details on the adjoint SQP techniques used to approximate Jacobian information.
* The mathematical formulation of the event-triggered update strategy.
* Experimental results on specific tasks/datasets and baselines.
{% endraw %}
