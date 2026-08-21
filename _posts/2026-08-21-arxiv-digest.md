---
layout: post
title: "Daily arXiv Digest — 2026-08-21 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement
- **Authors:** Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na
- **arXiv:** [2608.20318](https://arxiv.org/abs/2608.20318v1) · [pdf](https://arxiv.org/pdf/2608.20318v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.20318v1))
- **Categories:** cs.AI, cs.CL, cs.LG

### Abstract
> Recursive self-improvement (RSI) asks whether an AI system can improve the process that produces AI systems, so that the next system inherits the improvement. That process is the training algorithm: a better objective or update rule improves the compute\mbox{-}capability exchange rate for every subsequent run, including the one that produces the next agent. Whether RSI is feasible therefore turns on whether an agent can design training algorithms. No benchmark isolates that ability: existing suites are won by collecting data or by tuning hyperparameters, and none tells a change to how a run is executed apart from a change to how the model learns. We present AI4AI\mbox{-}Bench, 10 frozen research repositories spanning 10 training algorithm families. In each task, an agent has 4 hours on one B300 to rewrite the training algorithm; its code is then rerun from scratch for up to 12 hours and scored by a fixed evaluator hidden from the agent, against the repository's original algorithm under the same procedure. Because the 10 metrics are incommensurable, every task is mapped onto one scale on which $0$ is an uninformative model, $0.1$ is the algorithm the repository ships, and $1.0$ is the task optimum. Across 29 configurations of 6 systems on all 10 tasks the mean score is $0.166$, and the best system reaches $0.250$: even the strongest closes under a fifth of the distance between the algorithm that was already there and the optimum. The submissions show where that distance went: most never change how the model learns at all, and the minority that do average $0.226$ against $0.126$ for the rest. More reasoning effort mostly buys the willingness to go there, taking that minority from $8\%$ of submissions to $64\%$ and the mean score from $0.094$ to $0.196$. We release the task suite, the evaluators and every scored submission, so that the measurement can be repeated as these systems change.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Mean Score
```markdown
0.166
```
* Symbols: None
* Why it matters: The mean score represents the average performance of all submissions across all tasks.

### Equation 2: Strongest System's Average Score
```markdown
0.250
```
* Symbols: None
* Why it matters: This score represents the highest average performance achieved by any system across all tasks.

### Equation 3: Mean Score of Submissions that Reached the Algorithmic Layer
```markdown
0.226
```
* Symbols: None
* Why it matters: This score represents the average performance of submissions that successfully designed and implemented new training algorithms.

### Equation 4: Baseline Score
```markdown
0.126
```
* Symbols: None
* Why it matters: This score represents the performance of the original algorithm implemented by each repository.

### Equation 5: Percentage of Submissions that Improved the Baseline
```markdown
64%
```
* Symbols: None
* Why it matters: This percentage represents the proportion of submissions that improved the performance of the original algorithm.

**Method Summary**
==================

* The AI4AI-Bench suite consists of 10 frozen research repositories, each representing a different family of training algorithms.
* Each repository is evaluated using a fixed evaluator, which scores the submissions based on their performance.
* The submissions are compared to the original algorithm implemented by each repository, and the results are used to determine the effectiveness of the new training algorithms.

**Experimental Overview**
========================

* **Tasks/Datasets**: The AI4AI-Bench suite consists of 10 tasks, each representing a different family of training algorithms.
* **Baselines/Comparisons**: The original algorithm implemented by each repository serves as the baseline for comparison.
* **Main Claimed Findings**: The study demonstrates that most submissions fail to improve the performance of the original algorithm, with only a small proportion of submissions achieving significant improvements.

**What to Verify in the PDF**
=============================

* The detailed analysis of the three submissions that successfully designed and implemented new training algorithms.
* The results of the experiments, including the scores and rankings of the different systems.
* The evaluation of the performance of the strongest system, including its average score and the distance it achieves from the task optimum.
{% endraw %}

{% raw %}
## 2) $TCP_α$: Margin-Controlled Confidence estimation for reliable Music Information Retrieval
- **Authors:** Parampreet Singh, Anushka Singh, Sumit Kumar, Vipul Arora
- **arXiv:** [2608.20326](https://arxiv.org/abs/2608.20326v1) · [pdf](https://arxiv.org/pdf/2608.20326v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.20326v1))
- **Categories:** eess.AS, cs.LG

### Abstract
> Deep neural networks are often overconfident, assigning high confidence even to incorrect predictions. Consequently, users lack a reliable signal for deciding when a prediction can be trusted. Post-hoc confidence estimation addresses this by training a lightweight auxiliary head over a frozen classifier. Existing targets, however, suffer from inherent ambiguity: they assign overlapping confidence values to correct and incorrect predictions, while errors near the decision boundary receive confidence scores indistinguishable from correct predictions. In this work, we propose $TCP_α$, a novel confidence target that resolves these limitations by introducing a margin-controlled penalty for misclassified samples. We prove that $TCP_α$ guarantees complete separation between the target values of correct and incorrect predictions, with a separation margin that is independent of the number of classes and increases monotonically with the penalty parameter. Since accurate classifiers naturally produce very few errors, learning these targets results in a severely imbalanced regression problem. We therefore present a systematic study of training strategies for learning under this imbalance and identify an effective training configuration through extensive ablation studies. We evaluate the proposed approach on rāga identification, investigate its robustness under domain shift, and further validate it on frame-wise ornamentation detection without modifying the selected configuration. Across all settings, $TCP_α$ consistently outperforms existing confidence targets for failure prediction. Rejecting only the least-confident 8\% of predictions improves the base model's macro-F1 from 0.89 to 0.98, while fine-tuning the confidence head with only 5\% labeled samples from a new corpus effectively restores performance under domain shift.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: TCP_{\alpha}
```math
TCP_{\alpha} = \frac{p^{*} + \alpha}{p^{*} + \alpha + p(\hat{y} \neq y^{*})}
```
Symbols:
- `TCP_{\alpha}`: proposed confidence target
- `p^{*}`: probability assigned to the ground-truth class
- `p`: probability assigned to the predicted class
- `y^{*}`: ground-truth class
- `y`: predicted class
- `α`: penalty hyperparameter

Why it matters: This equation defines the proposed confidence target, which modifies the traditional TCP target by introducing a penalty term for misclassified samples.

### Equation 2: TCP_{n}
```math
TCP_{n} = \frac{p^{*}}{p^{*} + p(\hat{y} \neq y^{*})}
```
Symbols:
- `TCP_{n}`: traditional TCP target
- `p^{*}`: probability assigned to the ground-truth class
- `p`: probability assigned to the predicted class
- `y^{*}`: ground-truth class
- `y`: predicted class

Why it matters: This equation defines the traditional TCP target, which assigns a confidence value to each sample without considering the penalty term.

### Equation 3: \mathrm{TCP}_{\alpha}
```math
\mathrm{TCP}_{\alpha} = \frac{p^{*} + \alpha}{p^{*} + \alpha + p(\hat{y} \neq y^{*})} \cdot \frac{1}{1 + \alpha}
```
Symbols:
- `\mathrm{TCP}_{\alpha}`: modified TCP target with penalty
- `p^{*}`: probability assigned to the ground-truth class
- `p`: probability assigned to the predicted class
- `y^{*}`: ground-truth class
- `y`: predicted class
- `α`: penalty hyperparameter

Why it matters: This equation defines the modified TCP target with the penalty term, which is used to push error targets away from the success region.

### Equation 4: \alpha
```math
\alpha \geq 0
```
Symbols:
- `α`: penalty hyperparameter

Why it matters: This equation defines the constraint on the penalty hyperparameter, which must be non-negative.

### Equation 5: Not found in extracted context
No additional equations were found in the extracted context.

**Method Summary**
==================

* The proposed method, TCP_{\alpha}, uses a margin-controlled penalty to push error targets away from the success region.
* The method is designed to address the limitations of traditional confidence targets, which assign overlapping confidence values to correct and incorrect predictions.
* The proposed method is trained using an imbalance-aware strategy to learn the confidence head under the highly imbalanced TCP_{\alpha} target distribution.

**Experimental Overview**
==========================

* Tasks:
	+ Rāga identification
	+ Frame-wise ornamentation detection
* Datasets:
	+ Prasar Bharati Indian Music (PIM) dataset
	+ Saraga-Hindustani dataset
	+ Rāga Ornamentation Detection corpus
* Baselines:
	+ Traditional TCP target
	+ Label Distribution Smoothing (LDS)
	+ Feature Distribution Smoothing (FDS)
	+ Error upsampling
* Main claimed findings:
	+ TCP_{\alpha} consistently outperforms existing confidence targets for failure prediction.
	+ Rejecting only the least-confident 8% of predictions improves the base model's macro-F1 from 0.89 to 0.98.
	+ Fine-tuning the confidence head with only 5% labeled samples from a new corpus effectively restores performance under domain shift.

**What to Verify in the PDF**
=============================

* The detailed derivation of the proposed confidence target, TCP_{\alpha}.
* The experimental results for the Rāga Ornamentation Detection corpus.
* The analysis of the effect of the penalty hyperparameter, α, on the performance of the proposed method.
{% endraw %}

{% raw %}
## 3) Explainable Transformer Models for Clinical Prediction Tasks on Structured Electronic Health Records
- **Authors:** Jun Ni Du, Lukas Adamek, Maxim Kryukov, Flavio Dormont, Ziv Bar-Joseph, Sven Jager, Brandon Rufino
- **arXiv:** [2608.20315](https://arxiv.org/abs/2608.20315v1) · [pdf](https://arxiv.org/pdf/2608.20315v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.20315v1))
- **Categories:** cs.LG

### Abstract
> Predictive models over structured electronic health records (EHRs) remain central to machine learning for healthcare, but few have jointly emphasized quantitative laboratory information and interpretability with respect to input medical events. We present BERT-LER, a BERT-style model for coded EHR timelines pretrained and fine-tuned from a de-identified EHR dataset of 75 million patients, that encodes laboratory test results as discrete tokens while retaining graded information through percentile-based binning, paired with Integrated Gradients for token-level attributions grounded in the input EHR sequence. We benchmark our approach on the public EHRShot benchmark suite and on an asthma severity progression study based on real-world data. This addresses a methodological gap in EHR foundation-style modeling by unifying laboratory value representation and explainability in a single framework, while assessing whether both predictive performance and explanations generalize beyond standard clinical prediction tasks. Across EHRShot and asthma tasks, BERT-LER achieves predictive performance that is competitive with, and on laboratory-related tasks often exceeds, publicly available benchmark models, and provides attributions that align with clinically known risk factors. Our architecture and explainability approach can be applied to many therapeutic areas and prediction tasks using language models trained on structured EHRs.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: IG_{i}(x)
\[ IG_{i}(x) = (x_{i} - x^{\prime}_{i}) \int_{\alpha=0}^{1} \frac{\partial F(x^{\prime} + \alpha(x - x^{\prime}))}{\partial x_{i}} d\alpha \]

* Equation: IG_{i}(x)
* Symbols: IG_{i}(x), x_{i}, x^{\prime}_{i}, F(x^{\prime} + \alpha(x - x^{\prime})) 
* Why it matters: This equation represents the Integrated Gradients (IG) method for attributing the contribution of input feature x_{i} to the output of a model F(x).

### Equation 2: x^{\prime} + \alpha(x - x^{\prime})
\[ x^{\prime} + \alpha(x - x^{\prime}) \]

* Equation: x^{\prime} + \alpha(x - x^{\prime})
* Symbols: x^{\prime}, \alpha, x
* Why it matters: This equation is used to compute the partial derivative of F(x) with respect to x_{i} in the IG method.

### Equation 3: \alpha
\[ \alpha = \frac{k}{m} \text{ for } k = 1, \ldots, m \]

* Equation: \alpha
* Symbols: \alpha, k, m
* Why it matters: This equation represents the step size parameter \alpha used in the IG method.

### Equation 4: \frac{\partial F(x)}{\partial x_{i}}
\[ \frac{\partial F(x)}{\partial x_{i}} \]

* Equation: \frac{\partial F(x)}{\partial x_{i}}
* Symbols: F(x), x_{i}
* Why it matters: This equation represents the partial derivative of the model F(x) with respect to input feature x_{i}.

### Equation 5: F(x)
\[ F(x) \]

* Equation: F(x)
* Symbols: F(x)
* Why it matters: This equation represents the output of the model F(x).

**Method Summary**
==================

* The authors propose a BERT-style model called BERT-LER for clinical prediction tasks on structured electronic health records (EHRs).
* The model is pre-trained on a de-identified EHR dataset of 75 million patients and fine-tuned for specific tasks.
* The model incorporates laboratory test results as discrete tokens while retaining graded information through percentile-based binning.
* The authors use Integrated Gradients to provide token-level attributions grounded in the input EHR sequence.

**Experimental Overview**
========================

* The authors evaluate BERT-LER on two datasets: EHRShot and asthma severity progression tasks.
* The EHRShot dataset is used as a standard multi-task benchmark, and the asthma severity progression tasks are used as an external application check beyond public leaderboards.
* The authors compare BERT-LER to several baselines, including CLMBR, RETAIN, and Med-BERT.
* The main claimed findings are that BERT-LER achieves competitive predictive performance with, and often exceeds, publicly available benchmark models.

**What to Verify in the PDF**
=============================

* The authors' approach to handling outliers and missing values in the EHR dataset.
* The details of the cohort construction and study design for the asthma severity progression tasks.
* The implementation of the Integrated Gradients method for attributing the contribution of input features to the model output.
{% endraw %}

{% raw %}
## 4) Worst-Case Probability Bounds for Finite-Horizon Safety under Moment Uncertainty
- **Authors:** Renato Loureiro, Torbjørn Cunis
- **arXiv:** [2608.20121](https://arxiv.org/abs/2608.20121v1) · [pdf](https://arxiv.org/pdf/2608.20121v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.20121v1))
- **Categories:** math.OC

### Abstract
> This paper addresses the problem of estimating upper bounds on the probability that a dynamical system will enter an undesirable region at some point within a finite time horizon. The primary source of uncertainty lies in the system's initial state, for which only a finite set of moments is known or within a prescribed interval. To tackle this problem, we formulate a measure-based program and propose its relaxation using the moment-sum-of-squares (moment-SOS) framework. The corresponding dual problem is introduced as a functional program, which is subsequently strengthened into a sum-of-squares (SOS) program. Notably, this dual formulation bears a structural resemblance to classical barrier function techniques for certifying system safety, with the key distinction that it yields a probabilistic certificate. The effectiveness of the proposed approach is demonstrated through multiple case studies, including a case involving an object in orbit.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{S}$

* Equation: $\mathcal{S}$
* Symbols: $\mathcal{S}$ (set of undesirable regions)
* Why it matters: This equation represents the set of undesirable regions that the system should avoid entering.

### Equation 2: $\mathbb{N}$

* Equation: $\mathbb{N}$
* Symbols: $\mathbb{N}$ (natural numbers)
* Why it matters: This equation is used to index the set of undesirable regions.

### Equation 3: $\mathbb{R}$

* Equation: $\mathbb{R}$
* Symbols: $\mathbb{R}$ (real numbers)
* Why it matters: This equation is used to represent the state space of the system.

### Equation 4: $n\in\mathbb{N}$

* Equation: $n\in\mathbb{N}$
* Symbols: $n$ (natural number), $\mathbb{N}$ (natural numbers)
* Why it matters: This equation is used to index the set of undesirable regions.

### Equation 5: $\mathbb{N}^{n}$

* Equation: $\mathbb{N}^{n}$
* Symbols: $\mathbb{N}^{n}$ (set of natural numbers to the power of n)
* Why it matters: This equation is used to represent the set of undesirable regions.

**Method Summary**
==================

* The authors propose a measure-based program to estimate upper bounds on the probability that a dynamical system will enter an undesirable region at some point within a finite time horizon.
* The program is relaxed using the moment-sum-of-squares (moment-SOS) framework.
* The corresponding dual problem is introduced as a functional program, which is subsequently strengthened into a sum-of-squares (SOS) program.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors demonstrate the effectiveness of their approach on multiple case studies, including a case involving an object in-orbit.
* Baselines/Comparisons: The authors compare their approach with classical barrier function techniques for certifying system safety.
* Main Claimed Findings: The authors claim that their approach provides a probabilistic certificate for system safety, which is more conservative than classical barrier function techniques.

**What to Verify in the PDF**
=============================

* The authors claim that their approach is robust to the true initial distribution, but it is unclear how they verify this claim.
* The authors mention that their approach is based on the moment-SOS framework, but it is unclear how they relax the program using this framework.
* The authors claim that their approach is effective on multiple case studies, but it is unclear how they evaluate the performance of their approach on these cases.
{% endraw %}

{% raw %}
## 5) Orthogonal JEPA: Factorized Predictive States for Latent World Models
- **Authors:** Taoyong Cui, Pheng Ann Heng, Wanli Ouyang
- **arXiv:** [2608.20065](https://arxiv.org/abs/2608.20065v1) · [pdf](https://arxiv.org/pdf/2608.20065v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.20065v1))
- **Categories:** cs.LG

### Abstract
> World models construct latent states that support prediction, planning, and reasoning about an underlying system. Joint-embedding predictive architectures (JEPAs) offer a direct way to learn such states by predicting targets in representation space instead of reconstructing every detail of the observation. Standard JEPAs, however, organize all predictable content through one target embedding and one prediction pathway. In complex systems, this monolithic state can allocate redundant capacity to dominant signals while providing weak or conflicting gradients to less dominant predictive structure. We introduce \method, a latent world-modeling framework based on orthogonal predictive factorization. Learned basis matrices analyze each target state into multiple components, and a dedicated prediction branch estimates each component from a shared context representation. Predictive regression preserves the factor magnitudes required for state synthesis, an orthogonality objective discourages repeated directions, factor-activity regularization maintains variation in projected targets, and online variance regularization discourages coordinate-wise encoder collapse. Predicted components are synthesized into a complete latent state that can be used by a readout, decoder, planner, or autoregressive rollout. The same predictive-state mechanism applies when the target is temporally future, spatially hidden, or another partial observation of the same system. Experiments on controlled vision, single-cell transcriptomics, longitudinal health records, continuous control, and molecular dynamics evaluate representation quality, forecasting, planning, and long-horizon stability.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\delta$
```markdown
δ
```
* Symbols: $\delta$
* Why it matters: $\delta$ is an index that denotes a domain.

### Equation 2: $x \sim \mathcal{D}_{\delta}$
```markdown
x ∼ 𝒟 δ
```
* Symbols: $x$, $\delta$, $\mathcal{D}_{\delta}$
* Why it matters: This equation represents a raw observation $x$ sampled from a distribution $\mathcal{D}_{\delta}$ in a specific domain $\delta$.

### Equation 3: $\mathcal{A}_{\delta}$
```markdown
\mathcal{A}_{\delta}
```
* Symbols: $\mathcal{A}_{\delta}$
* Why it matters: $\mathcal{A}_{\delta}$ is a domain adapter that maps a raw observation $x$ to content tokens $H$ and optional structural descriptors $S$ in a specific domain $\delta$.

### Equation 4: $H = \{h_i\}_{i \in \Omega}$
```markdown
H = { h i } i ∈ Ω
```
* Symbols: $H$, $h_i$, $\Omega$
* Why it matters: $H$ is a set of content tokens that encode information about the raw observation $x$ in a specific domain $\delta$.

### Equation 5: $S = \{s_i\}_{i \in \Omega}$
```markdown
S = { s i } i ∈ Ω
```
* Symbols: $S$, $s_i$, $\Omega$
* Why it matters: $S$ is a set of optional structural descriptors that encode additional information about the raw observation $x$ in a specific domain $\delta$.

**Method Summary**
==================

* Orthogonal JEPA is a factorized predictive-state architecture that constructs latent states for latent world models.
* The architecture consists of a domain adapter, an online encoder, and a target encoder.
* The domain adapter maps a raw observation to content tokens and optional structural descriptors.
* The online encoder produces a context representation from the content tokens and structural descriptors.
* The target encoder produces a target representation from the content tokens and structural descriptors.
* The target parameters are updated using exponential moving average.

**Experimental Overview**
========================

* Orthogonal JEPA is evaluated on five systems: hidden-state completion, temporal forecasting, planning, and autoregressive rollout.
* The primary change is the monolithic versus factorized JEPA target.
* The experiment compares the performance of Orthogonal JEPA with a frozen baseline and standard JEPA.
* The tasks and datasets used are not specified in the provided context.

**What to Verify in the PDF**
=============================

* The definition of a latent world model and its role in predictive-state architectures.
* The mathematical formulation of the online and target encoders.
* The optimization procedure used to update the target parameters.
* The experimental results and comparison with baselines.
{% endraw %}
