---
layout: post
title: "Daily arXiv Digest — 2026-08-04 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning
- **Authors:** Zhaoxin Yu, Qi Shen, Hengli Li, Zhaowei Zhang, Song-Chun Zhu, Chi Zhang, Zilong Zheng
- **arXiv:** [2608.02585](https://arxiv.org/abs/2608.02585v1) · [pdf](https://arxiv.org/pdf/2608.02585v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.02585v1))
- **Categories:** cs.LG, cs.CL

### Abstract
> Optimization-based latent reasoning improves large language model outputs by optimizing instance-specific continuous states at test time while keeping model parameters frozen. Existing methods, however, typically connect these states to the reasoning trajectory through decoded tokens, making sequence-level credit assignment indirect and obscuring how latent updates shape subsequent reasoning. We introduce GradCuit (gradient through circuit), which inserts optimizable latent states at a selected Transformer layer between the hidden representations of the prompt and the generated continuation. Causal self-attention provides every continuation-token log-probability with a differentiable path to every preceding latent state through the remaining Transformer blocks, enabling reward-weighted gradients from the entire continuation to be assigned directly to the latents. Across five instruction-tuned backbones, three reasoning benchmarks, and two answer formats, GradCuit achieves an average accuracy of 64.5%, outperforming chain-of-thought prompting by 6.6 percentage points and the strongest competing method by 2.4 points. GradCuit also demonstrates greater robustness: across seven learning-rate settings, it consistently outperforms LatentSeek while reducing the standard deviation of accuracy from 1.53 to 0.82, and even its random-walk variant remains competitive with LatentSeek. For interpretability, token-level gradient attribution reveals that latent influence concentrates on reasoning-connector tokens, while layer analysis identifies early-to-middle Transformer layers as the most effective optimization space. By directly optimizing internal reasoning from outcome feedback, GradCuit opens a new axis of robust and interpretable test-time scaling, where LLMs adapt how they reason rather than merely regenerate, sample, or rerank outputs.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
===============

### Equation 1
```math
{}^{\,1,2\,*}
```
Symbols: `*` denotes a placeholder for variables or unknown values.
Why it matters: This equation is not explicitly defined in the context, but it appears to be a notation for a specific mathematical operation or a placeholder for variables.

### Equation 2
```math
{}^{\,1,3\,*}
```
Symbols: `*` denotes a placeholder for variables or unknown values.
Why it matters: Similar to Equation 1, this equation is not explicitly defined, but it may represent a mathematical operation or a placeholder for variables.

### Equation 3
```math
{}^{\,1,4\,*\,\dagger}
```
Symbols: `*` denotes a placeholder for variables or unknown values, `\dagger` denotes a dagger symbol, which is often used to indicate a footnote or a reference.
Why it matters: This equation is not explicitly defined, but it may represent a mathematical operation or a placeholder for variables.

### Equation 4
```math
{}^{\,1,4\,}
```
Symbols: `*` denotes a placeholder for variables or unknown values.
Why it matters: This equation is not explicitly defined, but it may represent a mathematical operation or a placeholder for variables.

### Equation 5
```math
{}^{\,1\,}
```
Symbols: `*` denotes a placeholder for variables or unknown values.
Why it matters: This equation is not explicitly defined, but it may represent a mathematical operation or a placeholder for variables.

### Equation 6
```math
{}^{1\,}
```
Symbols: `*` denotes a placeholder for variables or unknown values.
Why it matters: This equation is not explicitly defined, but it may represent a mathematical operation or a placeholder for variables.

### Equation 7
```math
{}^{2\,}
```
Symbols: `*` denotes a placeholder for variables or unknown values.
Why it matters: This equation is not explicitly defined, but it may represent a mathematical operation or a placeholder for variables.

### Equation 8
```math
{}^{3\,}
```
Symbols: `*` denotes a placeholder for variables or unknown values.
Why it matters: This equation is not explicitly defined, but it may represent a mathematical operation or a placeholder for variables.

**Method Summary**
================

* GradCuit is a method for credit-assigned gradient flow that enables robust and interpretable test-time latent reasoning.
* It inserts optimizable latent states at a selected Transformer layer between the hidden representations of the prompt and the generated continuation.
* The method uses causal self-attention to provide a differentiable path to every preceding latent state through the remaining Transformer blocks.
* GradCuit achieves an average accuracy of 64.5% across five instruction-tuned backbones, three reasoning benchmarks, and two answer formats.

**Experimental Overview**
=====================

* Tasks/Datasets: GPQA-Diamond, GSM8K, and MATH-500
* Baselines/Comparisons: CoT, Self-Reflection, Self-Consistency, Self-Scored Best-of-N (BoN), LatentSeek
* Main Claimed Findings: GradCuit achieves an average accuracy of 64.5% across all settings, outperforming CoT by 6.6 points and the strongest competing method by 2.4 points.

**What to Verify in the PDF**
==========================

* The implementation details of the GradCuit method, including the specific Transformer layers and attention mechanisms used.
* The results of the ablation study, including the performance of the full GradCuit and its variants.
* The analysis of the token-level gradient attribution, including the results of the Boxed answer format analysis.
{% endraw %}

{% raw %}
## 2) CoWAM: Coordination Contracts for Selective Policy Intervention with WAMs
- **Authors:** Shuaijun Liu, Qifu Wen, Shuyang Hao, Qi Luo, Chenglong Zhang, Feiyang You, Chengyu Wu, Ningxin Su
- **arXiv:** [2608.02578](https://arxiv.org/abs/2608.02578v1) · [pdf](https://arxiv.org/pdf/2608.02578v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.02578v1))
- **Categories:** cs.RO, cs.AI, cs.LG

### Abstract
> World Action Models (WAMs) augment robot policies with action-conditioned predicted futures, but a plausible future alone does not justify changing the action that a bimanual policy would execute. We present CoWAM, a selective intervention layer that expresses synchronization, role compatibility, and collision convergence as coordination contracts. Each contract combines typed admissibility checks with event-conditioned verification and calibrated intervention gates. CoWAM preserves the nominal action unless an alternative satisfies every active obligation and provides a clear, low-risk improvement; when the nominal action is also inadmissible, it invokes a predefined abstention fallback. To separate selector quality from proposal quality, all methods operate on identical candidate pools and commit their decisions before shared oracle labeling. Across eight simulated bimanual tasks, CoWAM improves coordination-valid selection by 16.7 percentage points over the contract-only variant and raises closed-loop success by 9.6 percentage points over the strongest selective baseline, while keeping harmful interventions below 1%. Together, these results establish coordination contracts as an effective interface for conservative policy intervention with predicted world-action evidence across coordination-rich bimanual tasks.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Candidate Pool

\[ \mathcal{P}_{t} = \{(\mathbf{a}_{i}, \hat{\mathbf{z}}_{i})\}_{i=0}^{K-1} \]

* Equation: \( \mathcal{P}_{t} \) represents the set of candidate pairs at time \( t \).
* Symbols:
	+ \( \mathcal{P}_{t} \): set of candidate pairs
	+ \( \mathbf{a}_{i} \): action \( i \)
	+ \( \hat{\mathbf{z}}_{i} \): predicted world trajectory for action \( i \)
	+ \( i \): index of the action
	+ \( K \): number of candidate pairs
* Why it matters: This equation defines the set of candidate pairs that will be considered for intervention.

### Equation 2: Action

\[ \mathbf{a}_{i} \]

* Equation: \( \mathbf{a}_{i} \) represents the action \( i \).
* Symbols:
	+ \( \mathbf{a}_{i} \): action \( i \)
* Why it matters: This equation represents the action that will be considered for intervention.

### Equation 3: Predicted World Trajectory

\[ \hat{\mathbf{z}}_{i} \]

* Equation: \( \hat{\mathbf{z}}_{i} \) represents the predicted world trajectory for action \( i \).
* Symbols:
	+ \( \hat{\mathbf{z}}_{i} \): predicted world trajectory for action \( i \)
* Why it matters: This equation represents the predicted future state of the world given the action.

### Equation 4: Event Set

\[ \mathcal{E} \]

* Equation: \( \mathcal{E} \) represents the set of events.
* Symbols:
	+ \( \mathcal{E} \): set of events
* Why it matters: This equation defines the set of events that will be considered for intervention.

### Equation 7: Intervention Gate

\[ g_{i} = \prod_{e \in \mathcal{E}} (1 - m_{t,e} + m_{t,e} c_{i,e}) \]

* Equation: \( g_{i} \) represents the intervention gate for action \( i \).
* Symbols:
	+ \( g_{i} \): intervention gate for action \( i \)
	+ \( m_{t,e} \): mask for event \( e \) at time \( t \)
	+ \( c_{i,e} \): calibration for action \( i \) and event \( e \)
	+ \( e \): event
	+ \( t \): time
* Why it matters: This equation determines whether the action should be intervened upon.

**Method Summary**
==================

* CoWAM is a selective intervention layer that expresses synchronization, role compatibility, and collision convergence as coordination contracts.
* Each contract combines typed admissibility checks with event-conditioned verification and calibrated intervention gates.
* CoWAM preserves the nominal action unless an alternative satisfies every active obligation and provides a clear, low-risk improvement.
* The method operates on identical candidate pools and commits decisions before shared oracle labeling.

**Experimental Overview**
=========================

* Tasks/Datasets: RoboTwin 2.0 on eight bimanual tasks.
* Baselines/Comparisons:
	+ Policy Top-1
	+ Future-Consensus
	+ Static collision gate
	+ RGB-D selector
	+ Selective Control baseline
* Main Claimed Findings:
	+ CoWAM improves coordination-valid selection by 16.7 percentage points over the contract-only variant.
	+ CoWAM raises closed-loop success by 9.6 percentage points over the strongest selective baseline.
	+ CoWAM limits false and harmful interventions to 3.3% and 0.4%, respectively.

**What to Verify in the PDF**
=============================

* The appendix reports the complete task and event decompositions, sequential horizons, proposer regimes, modality and threshold ablations, risk-coverage analysis, runtime, failure labels, and denominator ledger.
* The oracle upper bound succeeds on 176 of 240 pools, and CoWAM closes 55 of the 80-success gap between the nominal policy and this proposal ceiling.
* The full paper provides more details on the ablation study, including the results of the no-depth variant and the shuffling predicted futures experiment.
{% endraw %}

{% raw %}
## 3) Smooth Reparameterizations of Functions on Simplicial Product Spaces: Applications to Probabilistic Tensor Decomposition and Functional Data Registration
- **Authors:** Shashwat Kumar, Arafat Rahman, Anuj Srivastava, P. -A. Absil
- **arXiv:** [2608.02576](https://arxiv.org/abs/2608.02576v1) · [pdf](https://arxiv.org/pdf/2608.02576v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.02576v1))
- **Categories:** cs.LG

### Abstract
> We consider optimization problems defined on product spaces of simplices. Examples of this class of problems include learning low-rank discrete multivariate probability distributions via simplex constrained tensor decomposition and performing functional data registration under the Square Root Velocity Function (SRVF) representation. In this work, we demonstrate the feasibility of replacing the product simplex with a smooth, elementwise strictly convex reparameterization, resulting in an unconstrained optimization problem on a manifold. We show that performing such a reparameterization results in the second order Karush-Kuhn-Tucker (KKT) points on the smooth manifold being mapped to the weak second order KKT points on the product simplex. This leads to a Riemannian Gradient Descent (RGD) algorithm for solving the reparameterized problem, which outperforms Projected Gradient Descent (PGD), and provides a more faithful representation of the original function shapes while performing curve registration.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Minimization Problem on Simplicial Product Space

\[ \min_{v\in\mathcal{F}_{\mathrm{simplex}}}f(v), \]
\[ \mathcal{F}_{\mathrm{simplex}}=\Delta^{n_{1}}\times\cdots\times\Delta^{n_{L}}\times\mathbb{R}^{n_{L+1}}\times\cdots\times\mathbb{R}^{n_{L+Q}}. \]

*   **Equation**: Minimization problem on a simplicial product space.
*   **Symbols**: \(v\), \(\mathcal{F}_{\mathrm{simplex}}\), \(f(v)\).
*   **Why it matters**: This equation defines the objective function to be minimized, which is a key component of the optimization problem.

### Equation 2: Not Found in Extracted Context

### Equation 3: Definition of Simplicial Product Space

\[ \Delta^{n}=\{x\in\mathbb{R}^{n}\mid x\geq 0,\textbf{1}^{T}x=1\}. \]

*   **Equation**: Definition of a simplicial product space.
*   **Symbols**: \(x\), \(n\), \(\Delta^{n}\).
*   **Why it matters**: This equation provides a mathematical definition of the simplicial product space, which is used throughout the paper.

### Equation 4: Not Found in Extracted Context

### Equation 5: Not Found in Extracted Context

### Equation 6: Not Found in Extracted Context

### Equation 7: Minimization Problem on Smooth Reparameterization

\[ \min_{\theta\in\mathcal{F}_{\mathrm{smooth}}}f(\varphi(\theta)), \]

*   **Equation**: Minimization problem on a smooth reparameterization.
*   **Symbols**: \(\theta\), \(\mathcal{F}_{\mathrm{smooth}}\), \(f(\varphi(\theta))\).
*   **Why it matters**: This equation defines the objective function to be minimized on the smooth reparameterization space.

**Method Summary**
==================

*   The paper proposes a smooth reparameterization framework for optimization problems on simplicial product spaces.
*   The framework replaces the product simplex with a smooth, element-wise strictly convex reparameterization, resulting in an unconstrained optimization problem on a manifold.
*   The paper demonstrates the feasibility of this approach and shows that it outperforms Projected Gradient Descent (PGD) in certain applications.

**Experimental Overview**
=========================

*   **Tasks/Datasets**: The paper benchmarks the smooth reparameterization framework on a variety of tasks, including low-rank discrete multivariate probability distributions and functional data registration.
*   **Baselines/Comparisons**: The paper compares the smooth reparameterization framework to Projected Gradient Descent (PGD) and other baselines.
*   **Main Claimed Findings**: The paper claims that the smooth reparameterization framework outperforms PGD in certain applications and provides a more faithful representation of the original function shapes.

**What to Verify in the PDF**
=============================

*   **Details of the Smooth Reparameterization Framework**: The paper provides a high-level overview of the smooth reparameterization framework, but it would be useful to verify the mathematical details of the framework, including the construction of the Lagrangians and the derivation of the first-order KKT conditions.
*   **Numerical Results**: The paper presents numerical results for the smooth reparameterization framework, but it would be useful to verify the accuracy of these results and to explore the limitations of the framework.
*   **Theoretical Guarantees**: The paper claims that the smooth reparameterization framework has certain theoretical guarantees, such as convergence and optimality. It would be useful to verify these guarantees and to explore the conditions under which they hold.
{% endraw %}

{% raw %}
## 4) Pseudorandom Streams within Diffusion Models Act as Learnable Inputs That Affect Generation Quality
- **Authors:** Shengzhi Deng, Chenqi Ye, Yanze Guo
- **arXiv:** [2608.02575](https://arxiv.org/abs/2608.02575v1) · [pdf](https://arxiv.org/pdf/2608.02575v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.02575v1))
- **Categories:** cs.LG, stat.ML

### Abstract
> Diffusion models rely on stochastic inputs, yet on finite-precision hardware, the "randomness" they consume is realized as deterministic numerical orbits generated by pseudorandom rules. Accessible orbit structure can become a learnable input and affect both training and generation because the realized loss and its gradient depend on the concrete pseudorandom values consumed at each optimization step. A small multilayer perceptron predicts the next value of an orbit from its recent history, measuring general sequence predictability. A diffusion probe replaces real images with online random tensors while preserving the diffusion architecture and training objective, measuring whether the target system can exploit orbit structure. After controlling marginal statistics and screening out clear dynamical and finite-precision failures, the remaining orbits still produce markedly different diffusion losses and generation quality on MNIST and CIFAR-10. Both measures show strong rank correlations with macroscopic generation degradation, although their local rankings differ. After normalization by the IID baseline, the probe loss and the real-data diffusion loss approximately follow an empirical power law, with different exponents on the two datasets. These results suggest that a pseudorandom source is not only a distributional choice, but also a model-dependent structured input.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Objective Function
\mathcal{L}(\theta;D)

* Symbols: \mathcal{L} (objective function), \theta (model parameters), D (training data)
* Why it matters: This equation represents the objective function of the model, which is a function of the model parameters and the training data.

### Equation 2: Model Parameters
\theta

* Symbols: \theta (model parameters)
* Why it matters: This equation represents the model parameters, which are learned during training.

### Equation 3: Expected Objective Function
\mathcal{L}(\theta;D)=\mathbb{E}_{R}\left[\widehat{\mathcal{L}}(\theta;D,R)\right]

* Symbols: \mathcal{L} (objective function), \theta (model parameters), D (training data), R (random variables)
* Why it matters: This equation represents the expected objective function, which takes into account the random variables involved in data ordering, diffusion-timestep selection, training noise, and other stochastic operations.

### Equation 4: Random Variables
R_{t}

* Symbols: R_{t} (random variables at time t)
* Why it matters: This equation represents the random variables involved in data ordering, diffusion-timestep selection, training noise, and other stochastic operations.

### Equation 5: Objective Function with Random Variables
\widehat{\mathcal{L}}_{t}(\theta_{t};D,R_{t})

* Symbols: \widehat{\mathcal{L}}_{t} (approximate objective function at time t), \theta_{t} (model parameters at time t), D (training data), R_{t} (random variables at time t)
* Why it matters: This equation represents the approximate objective function at time t, which is used to compute the gradient of the objective function with respect to the model parameters.

**Method Summary**
================

* The authors use a diffusion model with a pseudorandom stream as the input, which is generated by a multilayer perceptron that predicts the next value of the orbit from its recent history.
* The authors control the marginal statistics of the pseudorandom stream and screen out clear dynamical and finite-precision failures.
* The authors use a diffusion probe to replace real images with online random tensors while preserving the diffusion architecture and training objective.
* The authors compare the performance of the diffusion model with different pseudorandom streams and show that the pseudorandom stream can affect both training and generation quality.

**Experimental Overview**
=====================

* Tasks/Datasets: The authors test the diffusion model on MNIST and CIFAR-10 datasets.
* Baselines/Comparisons: The authors compare the performance of the diffusion model with different pseudorandom streams, including an IID reference and four types of deterministic orbits: Logistic, finite-memory Markov-type, Sine, and ShiftedSine.
* Main Claimed Findings: The authors show that the pseudorandom stream can affect both training and generation quality, and that the pseudorandom stream can be used as a learnable input that affects generation quality.

**What to Verify in the PDF**
==========================

* The authors mention that the pseudorandom stream can be used as a learnable input that affects generation quality, but they do not provide a detailed explanation of how this works.
* The authors also mention that the pseudorandom stream can be controlled to have different marginal statistics and that this can affect the performance of the diffusion model.
* The authors provide some experimental results, but they do not provide a detailed analysis of the results or a discussion of the implications of the findings.
{% endraw %}

{% raw %}
## 5) Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection
- **Authors:** Anusha Madan Gopal, Aras Pirbadian, Kristofor D. Carlson, M Anthony Lewis, Jonathan Tapson
- **arXiv:** [2608.02560](https://arxiv.org/abs/2608.02560v1) · [pdf](https://arxiv.org/pdf/2608.02560v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.02560v1))
- **Categories:** cs.LG, cs.AI, cs.IR

### Abstract
> Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query. We introduce PRECOG (Pre-Computed Context Injection), a retrieval mechanism that exploits a property unique to SSMs: the fixed-size, position-agnostic recurrent hidden state is a complete summary of everything the model has read. PRECOG pre-encodes document corpora offline as SSM hidden states and injects the best-matching state directly at query time, bypassing in-context re-ingestion entirely. The same state-injection mechanism enables SMC (Structured Memory Consolidation): a hierarchical persistent memory with cognitive-domain clustering, an adjustable fidelity-vs-storage dial, and $O(1)$ session initialization, which consolidates short-term episodic states into long-term semantic memory and fuses both with retrieved corpus states at query time. We demonstrate the system on TENNs-LLM, a 1.2B-parameter gated-SSM language model with a 192 KB hidden state. PRECOG matches in-context RAG answer quality, reducing prefill latency from $\sim$27 s to $<$6 ms on edge hardware -- a $\sim$4500$\times$ speedup that crosses the threshold from unusable to interactive. The mechanism is architecturally impossible for Transformer KV-caches, which are position-entangled and grow linearly with context length.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: O(L_{\text{context}})
```latex
O(L_{\text{context}})
```
Symbols: `O` (Big O notation), `L_{\text{context}}` (context length)
Why it matters: This equation represents the prefilled cost of retrieval-augmented generation (RAG) models, which grows linearly with the context length.

### Equation 2: O(1)
```latex
O(1)
```
Symbols: `O` (Big O notation)
Why it matters: This equation represents the prefilled cost of State-Space Models (SSMs), which is constant and independent of the context length.

### Equation 3: \sim
```latex
\sim
```
Symbols: `\sim` (approximately equal to)
Why it matters: This equation represents the speedup achieved by using PRECOG, which reduces the prefill latency from approximately 27 seconds to less than 6 milliseconds.

### Equation 4: \times
```latex
\times
```
Symbols: `\times` (multiplication)
Why it matters: This equation represents the ratio of the storage advantage of PRECOG to the chunk artifact, which is approximately 85 times.

### Equation 5: O(d\cdot N)
```latex
O(d\cdot N)
```
Symbols: `O` (Big O notation), `d` (dimensionality), `N` (number of dimensions)
Why it matters: This equation represents the storage and bandwidth requirements of the PRECOG system, which is proportional to the dimensionality of the hidden state and the number of dimensions.

**Method Summary**
==================

* The PRECOG system uses a State-Space Model (SSM) to capture the persistent context and corpus retrieval.
* The system partitions the knowledge base into chunks, each of which is run through the SSM in inference mode.
* The chunk boundaries can follow any strategy, and the SSM produces a fixed-size hidden state regardless of input length.
* The system uses a lightweight sentence encoder to produce the retrieval key, which is persisted to flash storage.
* The system uses FAISS for nearest-neighbor search and demand-loads the corresponding states from flash into DRAM at query time.

**Experimental Overview**
=========================

* The PRECOG system is evaluated on the SQuAD v1.1 development set, which consists of 10,570 question-paragraph pairs over 2,067 distinct paragraphs.
* The system is compared to three baselines: in-context RAG, PRECOG top-1, and PRECOG top-3.
* The main claimed findings are:
	+ PRECOG matches in-context RAG to within 0.2 F1 and 0.2 EM on the SQuAD v1.1 dev split.
	+ PRECOG reduces the prefill latency from approximately 27 seconds to less than 6 milliseconds on edge hardware.
	+ The system achieves a speedup of approximately 4500 times compared to the baseline.

**What to Verify in the PDF**
=============================

* The storage and bandwidth requirements of the PRECOG system, including the dimensionality of the hidden state and the number of dimensions.
* The FAISS implementation and its impact on the system's performance.
* The memory horizon analysis and its implications for the system's performance.
* The roofline analysis and its comparison across deployment platforms.
{% endraw %}
