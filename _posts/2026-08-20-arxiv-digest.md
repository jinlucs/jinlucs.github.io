---
layout: post
title: "Daily arXiv Digest — 2026-08-20 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Lévy Attention: Single-Pass Predictive Uncertainty for Continuous-Time Attention
- **Authors:** Sotirios P. Chatzis, Loukas Papadoulas
- **arXiv:** [2608.19171](https://arxiv.org/abs/2608.19171v1) · [pdf](https://arxiv.org/pdf/2608.19171v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.19171v1))
- **Categories:** cs.LG

### Abstract
> Deep models for irregularly-sampled time series answer queries at arbitrary continuous timestamps, yet report nothing about how far each answer should be trusted. We show the attention layer itself can close that gap: with the right stochastic formulation, the pass that makes each prediction also reports, in closed form and at no extra cost, how far it should be trusted. We introduce Lévy Attention, a cross-attention operator whose output is a stochastic integral against an inhomogeneous Poisson random measure: query-key compatibilities assemble an intensity over a continuous (time x channel) index space, the measure scatters atoms under it, and the output averages an interpolated value field at those atoms. In expectation it reduces to a mollified cosine-kernel attention, so it replaces a softmax layer and trains with exact gradients. What softmax discards, the Poisson construction preserves in closed form: the evidence $Λ_q$ (total compatibility mass) and the disagreement $\mathrm{tr}\,Σ_V(q)$ (value spread). An exact variance identity makes their combination $\hatσ(q)=\sqrt{\mathrm{tr}\,Σ_V(q)\,\varphi(Λ_q)}$ the root-mean-square deviation of the sampled operator, emitted by the deterministic pass with no trained head. Empirically, disagreement carries the signal, while the evidence factor swings from uninformative on dense data to strongly informative on sparse. On t-PatchGNN the operator swap costs at most 5.6% accuracy against a matched control and nothing on the sparsest dataset. The free disagreement signal improves on 20-pass MC dropout across matched five-seed suites, and $\hatσ$ scales a calibrated Gaussian whose zero-sample CRPS beats a fifty-draw sampler; a split-conformal wrapper reaches nominal coverage at every level, and one pass ranks 3,383 unseen patients by trust in 1.4 seconds.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: \times

* Equation: \times
* Symbols: \times (index space), \times (channel)
* Why it matters: This equation represents the index space for the cross-attention operator. It is a product of two indices, one for time and one for channel.

### Equation 2: \Lambda_{q}

* Equation: \Lambda_{q}
* Symbols: \Lambda_{q} (evidence), q (query)
* Why it matters: This equation represents the evidence, which is the total compatibility mass found by the query-key compatibilities.

### Equation 3: \tr\bm{\Sigma}_{V}(q)

* Equation: \tr\bm{\Sigma}_{V}(q)
* Symbols: \tr (trace), \bm{\Sigma}_{V}(q) (disagreement)
* Why it matters: This equation represents the disagreement, which is the spread of the attended values.

### Equation 4: \hat{\sigma}(q)=\sqrt{\smash[b]{\tr\bm{\Sigma}_{V}(q)\,\varphi(\Lambda_{q})}}

* Equation: \hat{\sigma}(q)=\sqrt{\smash[b]{\tr\bm{\Sigma}_{V}(q)\,\varphi(\Lambda_{q})}}
* Symbols: \hat{\sigma}(q) (root-mean-square deviation), \tr (trace), \bm{\Sigma}_{V}(q) (disagreement), \varphi (function)
* Why it matters: This equation represents the root-mean-square deviation of the sampled operator, which is a measure of the uncertainty.

### Equation 5: 5.6%

* Equation: 5.6%
* Symbols: 5.6% (accuracy loss)
* Why it matters: This equation represents the accuracy loss of the Lévy attention operator compared to the softmax attention operator.

**Method Summary**
==================

* The Lévy attention operator is a cross-attention operator that takes into account the evidence and disagreement in the attention mechanism.
* The operator is trained using a deterministic mean path and a sampling path for on-demand error bars.
* The method is based on the idea of stochastic integration against a Poisson random measure on a (time × \times channel) index space.
* The operator is compared to the softmax attention operator in terms of accuracy and uncertainty.

**Experimental Overview**
=========================

* The experiments are conducted on the t-PatchGNN benchmark and the PhysioNet dataset.
* The tasks are to evaluate the accuracy and uncertainty of the Lévy attention operator compared to the softmax attention operator.
* The main claimed findings are:
	+ The Lévy attention operator has a lower accuracy loss compared to the softmax attention operator.
	+ The Lévy attention operator has a better uncertainty representation compared to the softmax attention operator.
	+ The operator is scalable and can be applied to large datasets.

**What to Verify in the PDF**
=============================

* The derivation of the Lévy attention operator and its properties.
* The experimental setup and results for the t-PatchGNN benchmark and the PhysioNet dataset.
* The theoretical analysis of the uncertainty representation and its relation to the evidence and disagreement.
* The comparison of the Lévy attention operator with other attention mechanisms.
{% endraw %}

{% raw %}
## 2) Constrained minmax density transportation for linear parabolic PDEs: a numerical optimal control perspective
- **Authors:** Siddhartha Ganguly, Vaibhav Upadhyay, Kenji Kashima, Debasish Chatterjee
- **arXiv:** [2608.19170](https://arxiv.org/abs/2608.19170v1) · [pdf](https://arxiv.org/pdf/2608.19170v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.19170v1))
- **Categories:** math.OC, eess.SY

### Abstract
> This article introduces a numerical optimal control framework for minmax constrained density control for a class of noisy linear parabolic partial differential equations (PDEs), in particular the noisy heat equation. The goal is to transport an initial density to a target density while minimizing a specified cost with respect to control actions and maximizing it with respect to disturbances, all within a fixed time horizon while satisfying given convex path constraints. To address this, the spatial derivatives in the PDE are discretized using finite-difference approximations, transforming the problem into a system of ordinary differential equations in time. The admissible space of control and disturbance trajectories is then finitely parametrized, and the resulting optimal control problem is formulated as a convex semi-infinite program (SIP) under mild assumptions. By leveraging new numerical tools from convex SIP theory, we establish guarantees for exact solutions that account for constraint satisfaction under an infinite family of disturbance realizations, and we establish an optimization-based computationally efficient algorithm to recover these solutions. Comprehensive numerical examples to demonstrate and validate our findings are included.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: u^{\ast}(\cdot)
* Equation: u^{\ast}(\cdot) = \mathcal{H}(\mathcal{T},\mathcal{B};\bar{z})
* Symbols: u^{\ast}(\cdot) - optimal control trajectory, \mathcal{H}(\mathcal{T},\mathcal{B};\bar{z}) - cost function
* Why it matters: This equation represents the optimal control trajectory that minimizes the cost function.

### Equation 2: x_{\mathrm{init}}\in\mathbb{R}^{d}
* Equation: x_{\mathrm{init}}\in\mathbb{R}^{d} - initial state
* Symbols: x_{\mathrm{init}} - initial state, \mathbb{R}^{d} - d-dimensional Euclidean space
* Why it matters: This equation represents the initial state of the system.

### Equation 3: x_{\mathrm{target}}\in\mathbb{R}^{d}
* Equation: x_{\mathrm{target}}\in\mathbb{R}^{d} - target state
* Symbols: x_{\mathrm{target}} - target state, \mathbb{R}^{d} - d-dimensional Euclidean space
* Why it matters: This equation represents the target state of the system.

### Equation 4: y(\cdot)
* Equation: y(\cdot) = cy_{xx}(x,t)
* Symbols: y(\cdot) - disturbance, c - constant, y_{xx}(x,t) - second derivative of y with respect to x
* Why it matters: This equation represents the disturbance that affects the system.

### Equation 5: y_{\Omega}(\cdot)
* Equation: y_{\Omega}(\cdot) - disturbance on the boundary
* Symbols: y_{\Omega}(\cdot) - disturbance on the boundary, \Omega - boundary of the domain
* Why it matters: This equation represents the disturbance on the boundary of the domain.

### Equation 6: y_{t}(x,t)=cy_{xx}(x,t)
* Equation: y_{t}(x,t)=cy_{xx}(x,t) - heat equation
* Symbols: y_{t}(x,t) - partial derivative of y with respect to t, c - constant, y_{xx}(x,t) - second derivative of y with respect to x
* Why it matters: This equation represents the heat equation that governs the system.

### Equation 7: y(0,t)=0
* Equation: y(0,t)=0 - initial condition
* Symbols: y(0,t) - disturbance at time t, 0 - initial condition
* Why it matters: This equation represents the initial condition of the disturbance.

### Equation 8: y(1,t)=v(t)+w(t)
* Equation: y(1,t)=v(t)+w(t) - boundary condition
* Symbols: y(1,t) - disturbance at time t, v(t) - control input, w(t) - disturbance
* Why it matters: This equation represents the boundary condition of the disturbance.

**Method Summary**
==================

* The authors propose a numerical optimal control framework for minmax constrained density control of linear parabolic PDEs.
* The framework uses a convex semi-infinite program (SIP) to solve the optimal control problem.
* The authors leverage new numerical tools from convex SIP theory to establish guarantees for exact solutions.
* The framework is designed to account for constraint satisfaction under an infinite family of disturbance realizations.

**Experimental Overview**
========================

* Tasks/Datasets: The authors test their framework on a heat equation problem with Dirichlet boundary conditions.
* Baselines/Comparisons: The authors compare their framework with a baseline method that uses a finite-dimensional optimization approach.
* Main Claimed Findings: The authors claim that their framework can recover exact solutions to the SIP problem, which accounts for constraint satisfaction under an infinite family of disturbance realizations.

**What to Verify in the PDF**
=============================

* The authors claim that their framework can recover exact solutions to the SIP problem, which accounts for constraint satisfaction under an infinite family of disturbance realizations.
* The authors use a finite-dimensional optimization approach as a baseline method for comparison.
* The authors provide numerical results to illustrate the performance of their framework.
* The authors discuss the implications of their results for real-world applications.
{% endraw %}

{% raw %}
## 3) Learned, Then Lost: A Measured Single-Example Counterfactual in Pre-training
- **Authors:** Zachary Speck, Asa Shepard
- **arXiv:** [2608.19168](https://arxiv.org/abs/2608.19168v1) · [pdf](https://arxiv.org/pdf/2608.19168v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.19168v1))
- **Categories:** cs.LG

### Abstract
> A single training example's contribution to a finished model is normally estimated rather than measured, because measuring it takes two expensive full pre-training runs that differ in one row of one batch. We ran that counterfactual 24 times at a small scale. We trained 32 GPT-2 models at 124M parameters from scratch on OpenWebText, over four conditions and eight seeds. At step 200 of 9,536, at peak learning rate, we replaced one row of a 256-row batch with a fixed context injection carrying a 194-token passage. The three injected conditions are: 1. fluent prose with a corpus-attested subject, 2. fluent prose with a fabricated subject matched to it within 0.14% on full-batch gradient delta, and 3. random keyboard characters. The fourth condition is an uninjected twin. The passage is learned from one exposure and then decays. Fifty steps after injection, the arm that saw a passage predicts it better than the arm that did not by 0.039 and 0.044 nats of cross-entropy on the passage, at eight of eight seeds with p < $10^{-4}$. At the final step we do not detect that difference for either passage, at p = 0.25 and p = 0.71, against minimum detectable effects of 0.025 and 0.079 nats, nor between the two passages, at p=0.54. Every geometric measure we report is taken after that decay. Our pre-registered contrast on interpolation loss barrier is +0.0068 with p = 0.509, against a minimum detectable effect of 0.032 barrier units. Held-out cross-entropy is $-0.00044$ with p = 0.310. Per-layer centered kernel alignment does not detectably separate any condition at any layer. Weight displacement reaches 44.1% of the seed-to-seed Euclidean distance and is 92% settled by the midpoint of training, while the barrier reaches 3.0% of the seed-to-seed barrier. Those two figures sit roughly 15 times apart, and that is a lower bound. The injection relocates the model within its basin without moving it out.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

Here's a walkthrough of up to 5 equations extracted from the context:

### Equation 1: p<10^{-4}
```python
p < 10^{-4}
```
* Symbols: `p` (probability)
* Why it matters: This equation represents the significance level for the t-test, indicating that the observed difference is statistically significant.

### Equation 2: p=0.25
```python
p = 0.25
```
* Symbols: `p` (probability)
* Why it matters: This equation represents the p-value for the t-test, indicating the probability of observing the difference by chance.

### Equation 3: p=0.71
```python
p = 0.71
```
* Symbols: `p` (probability)
* Why it matters: This equation represents the p-value for the t-test, indicating the probability of observing the difference by chance.

### Equation 4: p=0.54
```python
p = 0.54
```
* Symbols: `p` (probability)
* Why it matters: This equation represents the p-value for the t-test, indicating the probability of observing the difference by chance.

### Equation 5: +0.0068
```python
+0.0068
```
* Symbols: `+` (addition)
* Why it matters: This equation represents the mean difference between fluent-fabricated and fluent-attested on the interpolation loss barrier.

**Method Summary**
==================

Here's a summary of the method in 3-5 bullets:

* The authors use GPT-2 at 124M parameters and train it from an initialization of random weights (dictated by the seed).
* They use a corpus of 2,499,805,184 training tokens and 10,485,760 held-out, both from OpenWebText.
* The authors inject a fixed 194-token context into one row of the 256-row batch at step 200 of 9,536, and compare the performance of the injected model against its seed-matched twin.

**Experimental Overview**
=========================

Here's an overview of the experiment in 2-4 bullets:

* Tasks/Datasets: The authors train GPT-2 on OpenWebText and inject a fixed 194-token context into one row of the 256-row batch.
* Baselines/Comparisons: The authors compare the performance of the injected model against its seed-matched twin, as well as against a random-chars condition and a fluent-attested condition.
* Main Claimed Findings: The authors claim that the injected model performs better than its seed-matched twin on the interpolation loss barrier, but not on the held-out cross-entropy.

**What to Verify in the PDF**
=============================

Here are 2-4 bullets on details that still need the full paper:

* The authors mention that the injection point is step 200 in one row of the 256-row batch, but it's unclear why this specific step was chosen.
* The authors report that the mean difference between fluent-fabricated and fluent-attested is 0.00680 with respect to the interpolation loss barrier, but it's unclear what this means in practice.
* The authors mention that the barrier displacement and Euclidean distance dissociation are each expressed as a fraction of the seed-alone quantity, but it's unclear what this means in terms of the underlying mechanics of the model.
{% endraw %}

{% raw %}
## 4) Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions
- **Authors:** Tomasz R. Bielecki, Thibaut Mastrolia, Haoze Yan
- **arXiv:** [2608.19151](https://arxiv.org/abs/2608.19151v1) · [pdf](https://arxiv.org/pdf/2608.19151v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.19151v1))
- **Categories:** cs.LG, math.OC, stat.ML

### Abstract
> We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting. Due to the path dependence of the memory of the Hawkes intensity, this problem does not fall within classical stochastic control theory outside particular Markovian kernels. We first develop a finite-dimensional Markovianization procedure and algorithm to approximate multivariate Hawkes processes with mixtures of exponential kernels. We prove the convergence of the Markovianized approximation of the Hawkes process, its intensity, and the value of the problem to the original non-Markovian processes and the value of the primal problem. We then formulate continuous-time deterministic policy gradient learning on the Markovianized approximation of the problem, called Hawkes-CT DDPG. We propose a model-free algorithm to solve the non-Markovian Hawkes-driven optimization by observing only the event times of the process, the realization of the solution to the SDE, and a chosen set of decay filters, while the Hawkes kernel coefficients remain unknown. We compare our continuous time reinforcement learning Hawkes-CT DDPG method with discrete time reinforcement learning techniques under three different types of kernels: simple exponential, Erlang, and power-law kernels.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: λ
λ
- Symbols: λ (lambda)
- Why it matters: The intensity of the Hawkes process.

### Equation 2: λ_t = μ∞(t) + ∫[0,t-] Φ(t-s) dN_s
λ_t = μ∞(t) + ∫[0,t-] Φ(t-s) dN_s
- Symbols: λ_t (intensity at time t), μ∞(t) (limiting intensity), Φ(t-s) (Hawkes kernel), dN_s (jump size at time s)
- Why it matters: The Hawkes intensity at time t is the sum of the limiting intensity and the integral of the Hawkes kernel up to time t.

### Equation 3: μ∞
μ∞
- Symbols: μ∞ (limiting intensity)
- Why it matters: The limiting intensity of the Hawkes process.

### Equation 4: Φ
Φ
- Symbols: Φ (Hawkes kernel)
- Why it matters: The kernel that determines the memory of the Hawkes process.

### Equation 5: dX_t = b(t,X_t,a_t) dt + σ(t,X_t,a_t) dW_t + ∑[i=1]^m γ_i(t,X_t-1,a_t) dN_t^i
dX_t = b(t,X_t,a_t) dt + σ(t,X_t,a_t) dW_t + ∑[i=1]^m γ_i(t,X_t-1,a_t) dN_t^i
- Symbols: dX_t (differential of the state), b(t,X_t,a_t) (drift term), σ(t,X_t,a_t) (diffusion term), dW_t (Wiener process), dN_t^i (jump at time t for component i), γ_i(t,X_t-1,a_t) (jump intensity)
- Why it matters: The stochastic differential equation that describes the dynamics of the Hawkes process.

**Method Summary**
================

* The authors propose a continuous-time reinforcement learning method for controlling Hawkes-driven stochastic differential equations.
* The method uses a Markovianization procedure to approximate the Hawkes process with a mixture of exponential kernels.
* The authors prove the convergence of the Markovianized approximation to the original non-Markovian process.
* The method is implemented using a deterministic policy gradient algorithm, called Hawkes-CT DDPG.

**Experimental Overview**
=====================

* The authors compare the performance of Hawkes-CT DDPG with discrete-time reinforcement learning methods on three different types of kernels: simple exponential, Erlang, and power-law.
* The experiments are designed to test the ability of the method to learn from limited data and to handle non-Markovian dynamics.
* The authors report that Hawkes-CT DDPG achieves the lowest mean cost in both experiments, indicating its effectiveness in controlling Hawkes-driven systems.

**What to Verify in the PDF**
==========================

* The derivation of the Markovianization procedure and the proof of convergence.
* The implementation details of the Hawkes-CT DDPG algorithm, including the choice of hyperparameters and the optimization procedure.
* The results of the experiments, including the mean cost and the policy performance, and the comparison with baseline methods.
{% endraw %}

{% raw %}
## 5) Geometric Iterative Retrieval for Neural Audio Codec Resynthesis
- **Authors:** Leo Schmidt-Traub, Frédéric Berdoz, Luca A. Lanzendörfer, Roger Wattenhofer
- **arXiv:** [2608.19141](https://arxiv.org/abs/2608.19141v1) · [pdf](https://arxiv.org/pdf/2608.19141v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.19141v1))
- **Categories:** cs.SD, cs.LG

### Abstract
> Neural audio codecs based on Residual Vector Quantization (RVQ) have become the dominant discrete representation for token-based general audio generation, yet resynthesizing high-quality audio from coarse codec tokens remains an open problem and bounds the fidelity of every system that generates them. Prior work has framed resynthesis as a choice between discrete token prediction and continuous regression. We argue that this dichotomy is incomplete and introduce geometric iterative retrieval, a paradigm that uses the RVQ layer hierarchy itself as a natural iterative decomposition in continuous codebook space. Rather than classifying over discrete vocabularies or regressing to a single target vector, our method performs contrastive retrieval in the codebook's geometric space. We evaluate our method on codec restoration tasks across speech and music, and show improvements over both single-pass token prediction and one-step regression baselines.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: D{-}1

\[ D{-}1 = \sum_{k=1}^{D} \mathbf{e}_{k} \]

Symbols:
- \( D \): number of layers
- \( \mathbf{e}_{k} \): codebook vector at layer \( k \)
- \( \mathbf{e}_{k} \in \mathcal{C}_{k} = \{\mathbf{c}_{k}^{(1)},\dots,\mathbf{c}_{k}^{(V)}\} \): codebook vector at layer \( k \) with \( V \) possible values

Why it matters: This equation represents the sum of all codebook vectors across all layers.

### Equation 2: \mathbf{z} \in \mathbb{R}^{d}

Symbols:
- \( \mathbf{z} \): latent vector
- \( d \): dimension of the latent space

Why it matters: This equation defines the dimensionality of the latent space used for prediction.

### Equation 3: \mathbf{e}_{k} \in \mathcal{C}_{k} = \{\mathbf{c}_{k}^{(1)},\dots,\mathbf{c}_{k}^{(V)}\}

Symbols:
- \( \mathbf{e}_{k} \): codebook vector at layer \( k \)
- \( \mathcal{C}_{k} \): set of codebook vectors at layer \( k \)
- \( V \): number of possible values for each codebook vector

Why it matters: This equation defines the set of possible codebook vectors at each layer.

### Equation 4: \hat{\mathbf{z}} = \sum_{k=1}^{D} \mathbf{e}_{k}

Symbols:
- \( \hat{\mathbf{z}} \): predicted latent vector
- \( \mathbf{e}_{k} \): codebook vector at layer \( k \)

Why it matters: This equation represents the predicted latent vector as the sum of all codebook vectors.

### Equation 5: \mathbf{z}

Symbols:
- \( \mathbf{z} \): latent vector
- \( d \): dimension of the latent space

Why it matters: This equation is a placeholder for the latent vector used for prediction.

**Method Summary**
==================

* Geometric iterative retrieval is a paradigm that uses the RVQ layer hierarchy itself as a natural iterative decomposition in continuous codebook space.
* The method performs contrastive retrieval in the codebook's geometric space, rather than classifying over discrete vocabularies or regressing to a single target vector.
* The approach is implemented as a layer-wise prediction model over DAC's RVQ stack, trained with a contrastive retrieval objective and a self-attention aggregator.

**Experimental Overview**
=========================

* Tasks/Datasets: Codec restoration tasks across speech and music using the 44.1 kHz Descript Audio Codec.
* Baselines/Comparisons: Naive first-layer decode, CE token-prediction baseline, MSE one-step baseline, OSR (cosine-similarity) baseline.
* Main claimed findings: Geometric iterative retrieval outperforms all baselines on LSD, and beats the CE token-prediction baseline and the MSE one-step baseline on all three metrics.

**What to Verify in the PDF**
=============================

* The training objective and loss function used in the paper.
* The implementation details of the self-attention aggregator and DeBERTa-v3 encoder.
* The evaluation protocol used to compare the proposed method with the baselines.
{% endraw %}
