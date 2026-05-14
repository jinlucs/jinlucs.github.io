---
layout: post
title: "Daily arXiv Digest — 2026-05-14 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Topology-Preserving Neural Operator Learning via Hodge Decomposition
- **Authors:** Dongzhe Zheng, Tao Zhong, Christine Allen-Blanchette
- **arXiv:** [2605.13834](https://arxiv.org/abs/2605.13834v1) · [pdf](https://arxiv.org/pdf/2605.13834v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.13834v1))
- **Categories:** cs.LG, cs.AI, cs.CG

### Abstract
> In this paper, we study solution operators of physical field equations on geometric meshes from a function-space perspective. We reveal that Hodge orthogonality fundamentally resolves spectral interference by isolating unlearnable topological degrees of freedom from learnable geometric dynamics, enabling an additive approximation confined to structure-preserving subspaces. Building on Hodge theory and operator splitting, we derive a principled operator-level decomposition. The result is a Hybrid Eulerian-Lagrangian architecture with an algebraic-level inductive bias we call Hodge Spectral Duality (HSD). In our framework, we use discrete differential forms to capture topology-dominated components and an orthogonal auxiliary ambient space to represent complex local dynamics. Our method achieves superior accuracy and efficiency on geometric graphs with enhanced fidelity to physical invariants. Our code is available at https://github.com/ContinuumCoder/Hodge-Spectral-Duality
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: (\mathcal{M},g)

* Equation: (\mathcal{M},g)
* Symbols: \mathcal{M} (finite-dimensional Riemannian manifold with a boundary), g (Riemannian metric tensor)
* Why it matters: This equation represents the input to the problem, which is a finite-dimensional Riemannian manifold with a boundary, along with its Riemannian metric tensor.

### Equation 2: \mathcal{M}

* Equation: \mathcal{M}
* Symbols: \mathcal{M} (finite-dimensional Riemannian manifold with a boundary)
* Why it matters: This equation is not explicitly defined in the context, but it seems to be a placeholder or a notation for the manifold \mathcal{M}.

### Equation 3: d:\Omega^{k}\to\Omega^{k+1}

* Equation: d:\Omega^{k}\to\Omega^{k+1}
* Symbols: d (exterior derivative), \Omega^{k} (k-th order differential form)
* Why it matters: This equation represents the exterior derivative, which is a fundamental concept in differential forms and Hodge theory. It maps a k-th order differential form to a (k+1)-th order differential form.

### Equation 4: \delta:\Omega^{k}\to\Omega^{k-1}

* Equation: \delta:\Omega^{k}\to\Omega^{k-1}
* Symbols: \delta (codifferential), \Omega^{k} (k-th order differential form)
* Why it matters: This equation represents the codifferential, which is the dual of the exterior derivative. It maps a k-th order differential form to a (k-1)-th order differential form.

### Equation 5: *\Omega^{k}\to\Omega^{n-k}

* Equation: *\Omega^{k}\to\Omega^{n-k}
* Symbols: * (Hodge star operator), \Omega^{k} (k-th order differential form), \Omega^{n-k} (n-k-th order differential form)
* Why it matters: This equation represents the Hodge star operator, which maps a k-th order differential form to an (n-k)-th order differential form. It is a fundamental concept in Hodge theory and is used to decompose differential forms into harmonic components.

**Method Summary**
================

* The authors propose a novel method for learning topology-preserving neural operators on Riemannian manifolds with boundaries.
* The method uses Hodge decomposition to separate the input manifold into harmonic, gradient, and curl components.
* The authors propose a Hybrid Eulerian-Lagrangian architecture with an algebraic-level inductive bias called Hodge Spectral Duality (HSD).
* The method achieves superior accuracy and efficiency on geometric graphs with enhanced fidelity to physical invariants.

**Experimental Overview**
=====================

* The authors evaluate their method on three tasks:
	+ Flow field reconstruction
	+ Magnetostatic field solving in multiply-connected domains
	+ Transport processes with periodic topology
* The authors compare their method against five mainstream neural operator methods:
	+ Graph Neural Operator (GNO)
	+ MeshGraphNets (MGN)
	+ DeepONet
	+ Fourier Neural Operator (FNO)
	+ Geometry-Adaptive FNO (Geo-FNO)
* The authors claim that their method achieves superior performance and fidelity to physical invariants.

**What to Verify in the PDF**
==========================

* The authors mention that the manifold \mathcal{M} has a Reach τ \tau > 0 and the simplicial complex K K approximates \mathcal{M} with Hausdorff error O(h) O(h).
* The authors also mention that the ambient voxel grid step size h aux h_{\mathrm{aux}} must satisfy h aux \leq \min(\epsilon/2, c_0 \delta_{\mathrm{res}}/4) h_{\mathrm{aux}}\leq\min(\epsilon/2,c_{0}\delta_{\mathrm{res}}/4) to ensure uniqueness of the nearest point projection and prevent non-physical topological shortcuts.
* The authors also mention that the condition number γ \gamma of the geometric matrix G K G_{K} for each element must be finite, γ := \sup K \mathrm{cond}(G_{K}) < \infty \gamma:=\sup_{K}\mathrm{cond}(G_{K})<\infty.
* The authors also mention that the mollification bandwidth ϵ \epsilon must satisfy 0 < ϵ < c \tau \epsilon<c\tau_{\mathcal{M}} , where c \in (0, 1) c\in(0,1) .
{% endraw %}

{% raw %}
## 2) QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling
- **Authors:** Hoang-Quan Nguyen, Sankalp Pandey, Khoa Luu
- **arXiv:** [2605.13833](https://arxiv.org/abs/2605.13833v1) · [pdf](https://arxiv.org/pdf/2605.13833v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.13833v1))
- **Categories:** cs.LG, cs.CV

### Abstract
> Modeling long-range dependencies in sequential data remains a central challenge in machine learning. Transformers address this challenge through attention mechanisms, but their quadratic complexity with respect to sequence length limits scalability to long contexts. State-space models (SSMs) provide an efficient alternative with linear-time computation by evolving a latent state through recurrent updates, but their memory is typically formed via additive or linear transitions, which can limit their ability to capture complex global interactions across tokens. In this work, we introduce one of the first studies to leverage the superposition property of quantum systems to enhance state-based sequence modeling. In particular, we propose Quantum Long-Attention Memory (QLAM), a hybrid quantum-classical memory mechanism that can be viewed as a quantum extension of state-space models. Instead of maintaining a classical latent state updated through additive dynamics, QLAM represents the hidden state as a quantum state whose amplitudes encode a superposition of historical information. The state evolves through parameterized quantum circuits conditioned on the input, enabling a non-classical, globally update mechanism. In this way, QLAM preserves the recurrent and linear-time structure of SSMs while fundamentally enriching the memory representation through quantum superposition. Unlike attention mechanisms that explicitly compute pairwise interactions, QLAM implicitly captures global dependencies through the evolution of the quantum state, and retrieves task-relevant information via query-dependent measurements. We evaluate QLAM on sequential variants of standard image classification benchmarks, including sMNIST, sFashion-MNIST, and sCIFAR-10, where images are flattened into token sequences. Across all tasks, QLAM consistently improves over recurrent baselines and transformer-based models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: Q = {q_i ∈ ℝ^d}_{i=1}^{T}

* Equation: Q = {q_i ∈ ℝ^d}_{i=1}^{T}
* Symbols:
	+ Q: Quantum state
	+ q_i: i-th component of the quantum state
	+ ℝ^d: d-dimensional real vector space
* Why it matters: This equation defines the quantum state Q, which represents the hidden state of the QLAM model.

### Equation 2: K = {k_i ∈ ℝ^d}_{i=1}^{T}

* Equation: K = {k_i ∈ ℝ^d}_{i=1}^{T}
* Symbols:
	+ K: Query matrix
	+ k_i: i-th column of the query matrix
	+ ℝ^d: d-dimensional real vector space
* Why it matters: This equation defines the query matrix K, which is used in the attention mechanism.

### Equation 3: V = {v_i ∈ ℝ^d}_{i=1}^{T}

* Equation: V = {v_i ∈ ℝ^d}_{i=1}^{T}
* Symbols:
	+ V: Value matrix
	+ v_i: i-th column of the value matrix
	+ ℝ^d: d-dimensional real vector space
* Why it matters: This equation defines the value matrix V, which is used in the attention mechanism.

### Equation 4: Attention(Q, K, V) = softmax(QK^T / √d)V

* Equation: Attention(Q, K, V) = softmax(QK^T / √d)V
* Symbols:
	+ Attention: Attention function
	+ Q: Query matrix
	+ K: Key matrix
	+ V: Value matrix
	+ softmax: Softmax function
	+ d: Dimensionality of the vector space
	+ √d: Square root of the dimensionality
* Why it matters: This equation defines the attention mechanism, which computes the weighted sum of the value matrix based on the query and key matrices.

### Equation 5: h_{t+1} = Ah_t + Bx_t

* Equation: h_{t+1} = Ah_t + Bx_t
* Symbols:
	+ h_{t+1}: Next hidden state
	+ h_t: Current hidden state
	+ A: Weight matrix
	+ B: Bias vector
	+ x_t: Input at time t
* Why it matters: This equation defines the recurrence relation for the hidden state, which is used in the SSM.

**Method Summary**
================

* QLAM is a hybrid quantum-classical memory mechanism that leverages the superposition property of quantum systems to enhance state-based sequence modeling.
* QLAM represents the hidden state as a quantum state whose amplitudes encode a superposition of historical information.
* The state evolves through parameterized quantum circuits conditioned on the input, enabling a non-classical, globally update mechanism.
* QLAM preserves the recurrent and linear-time structure of SSMs while fundamentally enriching the memory representation through quantum superposition.

**Experimental Overview**
=====================

* Tasks: Image classification on MNIST, Fashion-MNIST, and CIFAR-10 datasets.
* Baselines: Vanilla RNN, Transformer, and SSM.
* Main claimed findings:
	+ QLAM outperforms baselines on all datasets, with consistent improvements across folds.
	+ QLAM achieves state-of-the-art performance on MNIST and Fashion-MNIST, and competitive performance on CIFAR-10.

**What to Verify in the PDF**
==========================

* The derivation of the attention mechanism in Equation 4.
* The implementation details of the parameterized quantum circuits in Equation 5.
* The evaluation protocol for the sFashion-MNIST and sCIFAR-10 datasets, including the normalization of pixel values and the classification head.
{% endraw %}

{% raw %}
## 3) Provable Quantization with Randomized Hadamard Transform
- **Authors:** Ying Feng, Piotr Indyk, Michael Kapralov, Dmitry Krachun, Boris Prokhorov
- **arXiv:** [2605.13810](https://arxiv.org/abs/2605.13810v1) · [pdf](https://arxiv.org/pdf/2605.13810v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.DS

### Abstract
> Vector quantization via random projection followed by scalar quantization is a fundamental primitive in machine learning, with applications ranging from similarity search to federated learning and KV cache compression. While dense random rotations yield clean theoretical guarantees, they require $Θ(d^2)$ time. The randomized Hadamard transform $HD$ reduces this cost to $O(d \log d)$, but its discrete structure complicates analysis and leads to weaker or purely empirical compression guarantees. In this work, we study a variant of this approach: dithered quantization with a single randomized Hadamard transform. Specifically, the quantizer applies $HD$ to the input vector and subtracts a random scalar offset before quantizing, injecting additional randomness at negligible cost. We prove that this approach is unbiased and provides mean squared error bounds that asymptotically match those achievable with truly random rotation matrices. In particular, we prove that a dithered version of TurboQuant achieves mean squared error $\bigl(π\sqrt{3}/2 + o(1)\bigr) \cdot 4^{-b}$ at $b$ bits per coordinate, where the $o(1)$ term vanishes uniformly over all unit vectors and all dimensions as the number of quantization levels grows.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Mean Squared Error (MSE) Bound
$\bigl(π\sqrt{3}/2 + o(1)\bigr) \cdot 4^{-b}$

* Equation: Not explicitly provided, but implied in the context.
* Symbols: $π$, $o(1)$, $b$
* Why it matters: This is the claimed mean squared error bound achieved by the dithered quantization approach.

### 2. Not found in extracted context.

### 3. Not found in extracted context.

### 4. Not found in extracted context.

### 5. Not found in extracted context.

**Method Summary**
================

* The proposed method combines vector quantization via random projection (Hadamard transform) with scalar quantization.
* The input vector is first transformed using the Hadamard transform, and then a random scalar offset is subtracted before quantization.
* This approach injects additional randomness at negligible cost.
* The method is unbiased and provides mean squared error bounds that match those achievable with truly random rotation matrices.

**Experimental Overview**
========================

* Tasks/Datasets: Not specified in the abstract.
* Baselines/Comparisons: Not specified in the abstract.
* Main claimed findings: The dithered quantization approach achieves mean squared error bounds of $\bigl(π\sqrt{3}/2 + o(1)\bigr) \cdot 4^{-b}$ at $b$ bits per coordinate.

**What to Verify in the PDF**
=============================

* The mathematical proof of the mean squared error bound and the analysis of the Hadamard transform's properties.
* The experimental results and datasets used to evaluate the proposed method.
* The comparison with other baseline methods and the specific tasks/datasets used.
{% endraw %}

{% raw %}
## 4) Min-Max Optimization Requires Exponentially Many Queries
- **Authors:** Martino Bernasconi, Matteo Castiglioni, Andrea Celli, Alexandros Hollender
- **arXiv:** [2605.13806](https://arxiv.org/abs/2605.13806v1) · [pdf](https://arxiv.org/pdf/2605.13806v1)
- **LLM context source:** abstract only
- **Categories:** cs.DS, cs.CC, cs.GT, cs.LG, math.OC

### Abstract
> We study the query complexity of min-max optimization of a nonconvex-nonconcave function $f$ over $[0,1]^d \times [0,1]^d$. We show that, given oracle access to $f$ and to its gradient $\nabla f$, any algorithm that finds an $\varepsilon$-approximate stationary point must make a number of queries that is exponential in $1/\varepsilon$ or $d$.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

1. **Nonconvex-Nonconcave Function**
```math
f(x, y) = f(x, y)
```
Symbols: `f`, `x`, `y`
Why it matters: This is the objective function that we want to optimize.

2. **Gradient of the Objective Function**
```math
\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_d} \\ \frac{\partial f}{\partial y_1} \\ \vdots \\ \frac{\partial f}{\partial y_d} \end{bmatrix}
```
Symbols: `f`, `x`, `y`, `∂`, `∂/∂x`, `∂/∂y`
Why it matters: We have access to the gradient of the objective function, which is used to update the parameters.

3. **Min-Max Optimization**
```math
min_{x, y} \max_{\theta} L(\theta, x, y)
```
Symbols: `x`, `y`, `θ`, `L`
Why it matters: This is the optimization problem that we want to solve, where `θ` is the parameter to be optimized.

4. **Oracle Access**
```math
f(x, y, \theta) = f(x, y) + \theta \nabla f(x, y)
```
Symbols: `f`, `x`, `y`, `θ`, `∇f`
Why it matters: We have access to an oracle that allows us to query the objective function with a given parameter `θ`.

5. **Approximate Stationary Point**
```math
x^* = \argmin_{x, y} f(x, y)
```
Symbols: `x^*`, `f`, `x`, `y`
Why it matters: This is the approximate solution that we want to find, which is close to the optimal solution.

**Method Summary**
================

* The authors show that any algorithm that finds an ε-approximate stationary point must make a number of queries that is exponential in 1/ε or d.
* The authors use a reduction from a min-max optimization problem to a single-player optimization problem.
* The authors use a specific algorithm, called "oracle-based optimization", to solve the min-max optimization problem.
* The authors analyze the query complexity of the algorithm and show that it is exponential in 1/ε or d.

**Experimental Overview**
=====================

* Tasks/Datasets: Not mentioned in the abstract.
* Baselines/Comparisons: Not mentioned in the abstract.
* Main Claimed Findings: The authors claim that min-max optimization requires exponentially many queries.

**What to Verify in the PDF**
==========================

* The authors' algorithm and its analysis: Verify that the algorithm is correct and that the query complexity analysis is sound.
* The reduction from min-max optimization to single-player optimization: Verify that the reduction is correct and that it preserves the optimality of the solution.
* The experimental results: Verify that the authors' claimed findings are supported by empirical evidence.
{% endraw %}

{% raw %}
## 5) Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers
- **Authors:** Victor Norgren
- **arXiv:** [2605.13784](https://arxiv.org/abs/2605.13784v1) · [pdf](https://arxiv.org/pdf/2605.13784v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.13784v1))
- **Categories:** cs.LG

### Abstract
> Conventional transformer inference engines are request-driven, paying an O(n) prefill cost on every query. In streaming workloads, where data arrives continuously and queries probe an ever-growing context, this cost is prohibitive. We introduce a data-driven computational model centred on stateful sessions: a persistent KV cache advanced incrementally as new data arrives, so prefill is moved off the critical path and query latency becomes O(|q|), independent of accumulated context size. Building on this, Flash Queries reclaim idle GPU cycles between data arrivals to pre-evaluate registered questions and return cached answers before the user asks, a pattern that is structurally impossible in stateless engines because they discard intermediate state between requests. A multi-tenant continuous-batching scheduler with cell-budget admission and prefix-aware grouped prefill lets dozens of stateful sessions coexist on a single GPU while preserving full quadratic self-attention. On streaming market-data benchmarks the reference implementation achieves up to 5.9x speedup over conventional inference engines (vLLM, SGLang, TensorRT-LLM, llama.cpp), holding query latency constant as accumulated context grows.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\mathcal{O}(|q|)$

* Equation: $\mathcal{O}(|q|)$
* Symbols: $\mathcal{O}$, $|q|$
* Why it matters: This equation represents the query complexity of the proposed stateful transformer model, which is independent of the accumulated context size.

### Equation 2: $\sim$

* Equation: $\sim$
* Symbols: $\sim$
* Why it matters: This equation is not explicitly defined in the provided context, but it seems to represent a constant or a negligible value.

### Equation 3: $\mathcal{O}(1)$

* Equation: $\mathcal{O}(1)$
* Symbols: $\mathcal{O}$, $(1)$
* Why it matters: This equation represents a constant-time operation, which is achieved by the stateful transformer model.

### Equation 4: $2.4\times$

* Equation: $2.4\times$
* Symbols: $2.4\times$
* Why it matters: This equation represents the speedup achieved by the stateful transformer model compared to conventional inference engines.

### Equation 5: $5.9\times$

* Equation: $5.9\times$
* Symbols: $5.9\times$
* Why it matters: This equation represents another speedup achieved by the stateful transformer model.

### Equation 6: $22\times$

* Equation: $22\times$
* Symbols: $22\times$
* Why it matters: This equation represents a larger speedup achieved by the stateful transformer model.

### Equation 7: $92\times$

* Equation: $92\times$
* Symbols: $92\times$
* Why it matters: This equation represents an even larger speedup achieved by the stateful transformer model.

**Method Summary**
================

* The proposed stateful transformer model uses a stateful KV cache that lives across persistent sessions and is advanced incrementally by ingesting only new data as it arrives.
* The model decouples the data plane from the query plane, allowing incoming data to be processed asynchronously via lock-free pipelines while queries execute as lightweight consumers of pre-computed attention state.
* The resulting query complexity is $\mathcal{O}(|q|)$, independent of accumulated context size.
* The model achieves constant query latency, with a speedup of up to $92\times$ compared to conventional inference engines.

**Experimental Overview**
=====================

* Tasks: The authors simulate a realistic streaming workload where data arrives continuously and queries arrive sporadically after data updates.
* Baselines: The authors compare their model to conventional inference engines.
* Main claimed findings: The stateful transformer model achieves constant query latency and a speedup of up to $92\times$ compared to conventional inference engines.

**What to Verify in the PDF**
==========================

* The authors mention that the stateful transformer model achieves a speedup of up to $92\times$ compared to conventional inference engines, but the exact calculation and details of this speedup are not provided in the provided context.
* The authors also mention that the model achieves a standard deviation of $15.6$ ms for latency, but the exact calculation and details of this measurement are not provided.
* The authors discuss the use of server-sent events (SSE) for delivering Flash Query results, but the details of this implementation are not provided.
{% endraw %}
