---
layout: post
title: "Daily arXiv Digest — 2026-05-29 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching
- **Authors:** Alaa Khamis, Alaa Maalouf
- **arXiv:** [2605.30337](https://arxiv.org/abs/2605.30337v1) · [pdf](https://arxiv.org/pdf/2605.30337v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.30337v1))
- **Categories:** cs.LG

### Abstract
> Test-time finetuning (TTFT) is a rapidly evolving paradigm that adapts a language model to each prompt by retrieving related sequences, updating the model on them, and then evaluating the prompt. However, TTFT is only practical if it is fast: selection and finetuning both happen per query, making each a direct bottleneck. Existing methods trade speed for quality: fast retrieval is often redundant, while stronger diversity-aware selection adds prohibitive per-query cost. We introduce HullFT, a geometric approach to TTFT that addresses both bottlenecks. Given a query, HullFT first represents the query embedding as a sparse convex combination of few training sequences, using efficient projection-free Frank-Wolfe optimization. This yields a support set that is inherently relevant and diverse. We then convert the fractional convex weights into an exact integer multiset for finetuning through a geometric integerization procedure. The resulting multiplicities naturally create repeated examples, which we exploit with Gradient Reuse to amortize forward-backward computation across repeated finetuning steps. Our experiments show that HullFT improves the quality-efficiency tradeoff over current state-of-the-art TTFT methods, achieving lower bits-per-byte at substantially lower total runtime.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: ε

* Equation: ε
* Symbols: ε (tolerance)
* Why it matters: The Frank-Wolfe tolerance ε is a hyperparameter that controls the trade-off between the quality of the support set and the computational cost of finding it.

### Equation 2: ℓ2

* Equation: ℓ2
* Symbols: ℓ2 (squared loss)
* Why it matters: The ℓ2 loss is used as the objective function in the Frank-Wolfe algorithm, which is a classical method for solving convex optimization problems.

### Equation 3: O(1/ε)

* Equation: O(1/ε)
* Symbols: O(1/ε) (big O notation)
* Why it matters: This equation shows that the computational complexity of the Frank-Wolfe algorithm decreases as the tolerance ε decreases, which is a desirable property for efficient optimization.

### Equation 4: ℝd

* Equation: ℝd
* Symbols: ℝd (real numbers)
* Why it matters: This equation represents the dimensionality of the embedding space, which is a crucial aspect of the problem formulation.

### Equation 5: d+1

* Equation: d+1
* Symbols: d+1 (dimensionality)
* Why it matters: This equation represents the number of parameters in the model, which is an important consideration in the context of optimization and finetuning.

**Method Summary**
================

* The HullFT method uses a geometric approach to test-time finetuning, which involves representing the query embedding as a sparse convex combination of few training sequences.
* The method uses efficient projection-free Frank-Wolfe optimization to find a support set that is inherently relevant and diverse.
* The support set is then converted into an exact integer multiset for finetuning, which creates repeated examples that can be exploited with Gradient Reuse to amortize forward-backward computation.

**Experimental Overview**
=====================

* The experiments evaluate HullFT on 12 subsets of The Pile using GPT-2 as the base model.
* The evaluation protocol involves averaging the results over 150 test queries per subset, with a total-runtime budget ranging from 1 to 50 seconds.
* The method is compared against SIFT and kNN, which are state-of-the-art methods for test-time finetuning.
* The main claimed findings include:
	+ HullFT achieves a strictly lower Bits-Per-Byte (BPB%) than both SIFT and kNN across every total-runtime budget.
	+ The gap over the best baseline is largest at tight budgets, with HullFT dominating the strongest competing baseline for every T ≲ 4.5 seconds.

**What to Verify in the PDF**
==========================

* The pseudocode for the core procedures, algorithmic variants, and baselines referenced in Sec. 3.
* The experimental protocol details, including the evaluation style, retrieval pools, and runtime measurements.
* The ablation results, which isolate the effect of individual design choices on the performance of HullFT.
{% endraw %}

{% raw %}
## 2) Fairness-Aware Federated Learning with Trajectory Shapley Value
- **Authors:** Daniel Kuznetsov, Ziqi Wang
- **arXiv:** [2605.30336](https://arxiv.org/abs/2605.30336v1) · [pdf](https://arxiv.org/pdf/2605.30336v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.30336v1))
- **Categories:** cs.LG

### Abstract
> Federated learning is an emerging distributed paradigm that addresses the challenges posed by heterogeneous, privacy-sensitive data. It enables multiple clients to train a model collaboratively by aggregating their local updates at a server. However, conventional aggregation schemes typically use fixed weights that fail to reflect unequal and time-varying client contributions, leading to biased and unstable learning. To improve fairness and stability, we propose the Trajectory Shapley Value (TSV), a contribution metric that evaluates how each client influences the optimization trajectory of the global model using a validation-based, temporally consistent utility. Building on TSV, we design FedTSV, an adaptive aggregation method that converts per-round evaluations into dynamic client weights, allowing the server to respond to heterogeneous and adversarial participation in real time. Experiments on benchmark datasets show that FedTSV accelerates convergence, improves robustness, and yields more equitable contribution assessments, thereby providing a principled foundation for fairness-aware federated optimization.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{D}$

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 2: $\mathcal{N}:=\{1,2,\dots,n\}$

* Equation: $\mathcal{N}:=\{1,2,\dots,n\}$
* Symbols: $\mathcal{N}$, $n$
* Why it matters: Defines a set of indices $\mathcal{N}$, which is used to index clients in the federated learning setting.

### Equation 3: $i\in\mathcal{N}$

* Equation: Not provided
* Symbols: $i$, $\mathcal{N}$
* Why it matters: Indicates that $i$ is an element of the set $\mathcal{N}$, which represents the indices of clients.

### Equation 4: $\mathcal{D}_{i}$

* Equation: Not provided
* Symbols: $\mathcal{D}_{i}$
* Why it matters: Represents the local dataset of client $i$.

### Equation 5: $F_{i}(\cdot;\mathcal{D}_{i})$

* Equation: $F_{i}(\cdot;\mathcal{D}_{i})$
* Symbols: $F_{i}$, $\mathcal{D}_{i}$
* Why it matters: Represents the loss function of client $i$ on its local dataset $\mathcal{D}_{i}$.

### Equation 6: $\theta\in\mathbb{R}^{d}$

* Equation: $\theta\in\mathbb{R}^{d}$
* Symbols: $\theta$, $d$
* Why it matters: Represents the model parameters of the federated learning system, with $d$ being the dimensionality of the parameters.

### Equation 7: $\min_{\theta\in\mathbb{R}^{d}}\;F(\theta;\mathcal{D})\coloneqq\sum_{i\in\mathcal{N}}\alpha_{i}\,F_{i}(\theta;\mathcal{D}_{i})$

* Equation: $\min_{\theta\in\mathbb{R}^{d}}\;F(\theta;\mathcal{D})\coloneqq\sum_{i\in\mathcal{N}}\alpha_{i}\,F_{i}(\theta;\mathcal{D}_{i})$
* Symbols: $F$, $\mathcal{D}$, $\alpha_{i}$, $F_{i}$, $\mathcal{D}_{i}$
* Why it matters: Represents the global loss function of the federated learning system, which is the minimum of the loss functions of all clients weighted by their respective weights $\alpha_{i}$.

### Equation 8: $\alpha_{i}\geq 0$

* Equation: $\alpha_{i}\geq 0$
* Symbols: $\alpha_{i}$
* Why it matters: Ensures that the weights $\alpha_{i}$ are non-negative, which is a necessary condition for the global loss function to be well-defined.

**Method Summary**
==================

* The proposed method, FedTSV, adapts client aggregation weights according to estimated contributions using the Trajectory Shapley Value (TSV) metric.
* FedTSV uses a validation-based, temporally consistent utility to evaluate the contributions of each client.
* The method assigns higher importance to clients with high-quality data while down-weighting potentially malicious participants.
* FedTSV achieves higher accuracy and robustness compared to baselines such as FedAvg and LOO.

**Experimental Overview**
========================

* Tasks: Federated learning on MNIST and CIFAR-10 datasets.
* Datasets: 100 clients, with 70 benign clients holding IID data, 10 benign clients holding non-IID data, and 20 malicious clients.
* Baselines: FedAvg, LOO, and CGSV.
* Main claimed findings: FedTSV achieves higher accuracy and robustness compared to baselines, and improves the fairness and stability of federated learning.

**What to Verify in the PDF**
=============================

* The mathematical derivation of the Trajectory Shapley Value (TSV) metric and its application to federated learning.
* The experimental results for the MNIST and CIFAR-10 datasets, including the accuracy and robustness of FedTSV compared to baselines.
* The analysis of the Byzantine clients and their impact on the federated learning system.
{% endraw %}

{% raw %}
## 3) When, why, and how do diffusion posterior samplers fail? A finite-sample lens
- **Authors:** Benjamin A. Burns, Sara Fridovich-Keil
- **arXiv:** [2605.30330](https://arxiv.org/abs/2605.30330v1) · [pdf](https://arxiv.org/pdf/2605.30330v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG

### Abstract
> Diffusion models have excellent capacity to model complex distributions of natural data, which has made them a popular and effective choice for posterior sampling in imaging inverse problems. Existing methods can incorporate any measurement model at inference time but must use an inexact approximation for the likelihood at intermediate timesteps for computational tractability. Although these approximations can often work well empirically, their downstream effect on the sampled posterior is poorly understood and can result in unexplained failures. To understand when, why, and how these likelihood approximations propagate to erroneous posterior distributions, we introduce a finite-sample perspective on posterior sampling that approximates the posterior to arbitrary precision as training set size tends towards infinity, for any forward model and prior distribution. Using this finite-sample lens, we observe that popular posterior sampling approximations tend to under- or over-estimate the spread of the posterior at intermediate timesteps, causing downstream consequences including sensitivity to early stopping time, inaccurate relative weighting of posterior modes, and hallucination, both of prior modes that are not in the posterior and likelihood modes that are not supported by the prior. Moreover, we find that the cause of these posterior errors requires neither a nonlinear measurement model nor a multimodal posterior, but can arise solely due to a multimodal prior and inaccurate posterior spread at intermediate sampling times. Our finite-sample posterior sampling approach is agnostic to the type of likelihood approximation and the type of (linear or nonlinear) forward model, and can thus serve as a drop-in diagnostic to evaluate the accuracy and failure modes of existing and future posterior samplers.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough

Unfortunately, the extracted context does not provide any mathematical formulas to walkthrough.

### Method Summary

* The authors introduce a finite-sample perspective on posterior sampling that approximates the posterior to arbitrary precision as training set size tends towards infinity.
* The approach is agnostic to the type of likelihood approximation and the type of (linear or nonlinear) forward model.
* The authors aim to evaluate the accuracy and failure modes of existing and future posterior samplers.
* The method can be used to diagnose posterior errors caused by inaccurate posterior spread at intermediate sampling times.
* The approach can be applied to any forward model and prior distribution.

### Experimental Overview

* Tasks/Datasets: Not specified in the extracted context.
* Baselines/Comparisons: Not specified in the extracted context.
* Main Claimed Findings: The authors observe that popular posterior sampling approximations tend to under- or over-estimate the spread of the posterior at intermediate timesteps, causing downstream consequences.

### What to Verify in the PDF

* The specific tasks and datasets used in the experiments.
* The details of the likelihood approximations used in the existing methods.
* The results of the experiments, including the specific posterior errors and failure modes observed.
{% endraw %}

{% raw %}
## 4) SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?
- **Authors:** Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang
- **arXiv:** [2605.30329](https://arxiv.org/abs/2605.30329v1) · [pdf](https://arxiv.org/pdf/2605.30329v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.30329v1))
- **Categories:** cs.LG

### Abstract
> Autonomous AI research agents aim to accelerate scientific discovery by automating the research pipeline, from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamental bottleneck: whether Large Language Models can judge the methodological viability of a research idea before expending time and computational resources. We introduce SoundnessBench, a curated benchmark of 1,099 machine-learning research proposals reconstructed from ICLR submissions, labeled with reviewer soundness sub-scores, and audited against source papers. SoundnessBench should be interpreted as a benchmark for recoverable proposal-stage soundness rather than exact prediction of full-paper review outcomes. Across 12 frontier LLMs, we find a pervasive optimism bias: under standard prompting, models frequently rate low-soundness proposals as sound, while aggressive prompting largely shifts errors from false positives to false negatives. Additional controls for public-corpus contamination, paper-identifying phrases, surface features, and human audit quality suggest that this behavior is not explained by a single confounder. Our results indicate that current LLMs are not yet reliable as standalone first-gate evaluators for scientific rigor.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: S ≤ 2

* Equation: S ≤ 2
* Symbols: S (soundness score)
* Why it matters: This equation represents the condition for a proposal to be considered low soundness. The soundness score S is compared to 2, indicating that proposals with a score less than or equal to 2 are classified as low soundness.

### Equation 2: = 1.77

* Equation: = 1.77
* Symbols: (soundness score)
* Why it matters: This equation represents the soundness score assigned to a proposal. The value of 1.77 is a specific score that corresponds to a particular level of soundness.

### Equation 3: S ≥ 3

* Equation: S ≥ 3
* Symbols: S (soundness score)
* Why it matters: This equation represents the condition for a proposal to be considered high soundness. The soundness score S is compared to 3, indicating that proposals with a score greater than or equal to 3 are classified as high soundness.

### Equation 4: = 3.22

* Equation: = 3.22
* Symbols: (soundness score)
* Why it matters: This equation represents the soundness score assigned to a proposal. The value of 3.22 is a specific score that corresponds to a particular level of soundness.

### Equation 5: ≥ 3

* Equation: ≥ 3
* Symbols: (soundness score)
* Why it matters: This equation represents the condition for a proposal to be considered high soundness. The soundness score is compared to 3, indicating that proposals with a score greater than or equal to 3 are classified as high soundness.

### Equation 6: ≤ 2

* Equation: ≤ 2
* Symbols: (soundness score)
* Why it matters: This equation represents the condition for a proposal to be considered low soundness. The soundness score is compared to 2, indicating that proposals with a score less than or equal to 2 are classified as low soundness.

### Equation 7: τ = 0.7

* Equation: τ = 0.7
* Symbols: τ (tau)
* Why it matters: This equation represents the threshold for soundness judgment. The value of 0.7 is a specific threshold that corresponds to a particular level of soundness.

### Equation 8: ℓ = 3000

* Equation: ℓ = 3000
* Symbols: ℓ (length)
* Why it matters: This equation represents the length of the proposal text. The value of 3000 is a specific length that corresponds to a particular proposal.

**Method Summary**
==================

* The authors introduce SoundnessBench, a benchmark for evaluating the soundness of machine learning research proposals.
* The benchmark is built from real ML research submissions and targets recoverable proposal-stage methodological soundness rather than exact full-paper review prediction.
* The authors evaluate a diverse set of 12 frontier models on SoundnessBench, including GPT models, Claude models, Gemini models, Qwen models, a LLaMA model, and a Kimi model.
* The evaluation protocol involves providing a results-masked research proposal to an LLM with a fixed evaluation prompt and asking the model to classify the proposal as high or low soundness and provide a justification.

**Experimental Overview**
========================

* Tasks/Datasets: SoundnessBench, a benchmark for evaluating the soundness of machine learning research proposals.
* Baselines/Comparisons: The authors evaluate a diverse set of 12 frontier models on SoundnessBench.
* Main Claimed Findings: The authors observe a pervasive optimism bias in scientific judgment, where models frequently rate proposals with low reviewer-derived soundness labels as sound.

**What to Verify in the PDF**
=============================

* The authors report that 92.3% of leakage checks match the expected "No" answer and 84.6% of label-validity checks match the expected "Yes" answer in the preliminary human audit of extraction quality and label validity.
* The authors also report that GPT-5.4's approval rate drops from 77.0% on the original proposals to 1.0% after injection of targeted flaws into 100 high-soundness proposals.
* The authors provide representative false-positive and true-positive examples, together with concrete model responses, in Supplementary Sec. B.9.
{% endraw %}

{% raw %}
## 5) Reasoning with Sampling: Cutting at Decision Points
- **Authors:** Felix Zhou, Anay Mehrotra, Quanquan C. Liu
- **arXiv:** [2605.30327](https://arxiv.org/abs/2605.30327v1) · [pdf](https://arxiv.org/pdf/2605.30327v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.AI, cs.CL, math.ST, stat.ML

### Abstract
> Frontier reasoning models are produced by posttraining base language models with reinforcement learning. Recent work has challenged this by showing that sampling from a sharpened version of the base model's distribution, a so-called power distribution, elicits comparable reasoning without additional training, curated datasets, or verifiers. However, making this method practical requires efficiently sampling from the power distribution. A sampler needs to "mix" to the power distribution, which necessitates moving between modes of the target distribution; intuitively, e.g., trying different reasoning strategies. The samplers proposed in prior works repeatedly select a "cut" position in the current reasoning trace uniformly at random and resample the suffix from that position onward. However, reasoning traces typically contain a few consequential decisions (e.g., the choice of proof strategy or algorithm), and we observe that a uniformly chosen cut tends to rewrite local details rather than revisit decision points. We introduce an algorithm (Entropy-Cut Metropolis-Hastings) that uses the base model's next-token entropy as a proxy to identify key decision points and resample from those positions. We empirically verify that entropy jumps are a useful proxy for decision points and, in a stylized model of reasoning, prove that our method's mixing time scales with the number of decisions in a trace rather than with the number of tokens, which can be much larger. Across MATH500, HumanEval, GPQA Diamond, and AIME26, our method consistently improves over baselines and RL-trained models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Uniformly chosen cut
Not found in extracted context.

### 2. Entropy-Cut Metropolis-Hastings algorithm
Not found in extracted context.

### 3. Next-token entropy
Not found in extracted context.

### 4. Power distribution
Not found in extracted context.

### 5. Decision points
Not found in extracted context.

**Method Summary**
==================

* The authors introduce an algorithm called Entropy-Cut Metropolis-Hastings to efficiently sample from the power distribution.
* The algorithm uses the base model's next-token entropy as a proxy to identify key decision points.
* The method "mixes" to the power distribution by resampling from these identified decision points.
* The algorithm is designed to improve upon prior samplers that uniformly select a "cut" position in the current reasoning trace.

**Experimental Overview**
========================

* Tasks/Datasets:
	+ MATH500
	+ HumanEval
	+ GPQA Diamond
	+ AIME26
* Baselines/Comparisons:
	+ Prior samplers that uniformly select a "cut" position
	+ RL-trained models
* Main Claimed Findings:
	+ The Entropy-Cut Metropolis-Hastings algorithm consistently improves over baselines and RL-trained models across the mentioned datasets.

**What to Verify in the PDF**
=============================

* The mathematical formulation of the Entropy-Cut Metropolis-Hastings algorithm.
* The empirical results and analysis of the algorithm's performance on the mentioned datasets.
* The proof that the algorithm's mixing time scales with the number of decisions in a trace rather than with the number of tokens.
{% endraw %}
