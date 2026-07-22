---
layout: post
title: "Daily arXiv Digest — 2026-07-22 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Provable diffusion-based posterior sampling for linear inverse problems via DDIM
- **Authors:** Yuchen Jiao, Na Li, Changxiao Cai, Yuxin Chen, Gen Li
- **arXiv:** [2607.19333](https://arxiv.org/abs/2607.19333v1) · [pdf](https://arxiv.org/pdf/2607.19333v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.AI, stat.ML

### Abstract
> Diffusion-based methods have achieved remarkable empirical success in solving inverse problems. However, many existing posterior samplers either lack rigorous theoretical guarantees or incur substantial computational overhead. We propose a simple and efficient algorithm, called \pddim, for solving linear inverse problems with diffusion priors via a DDIM-type sampler. Our method requires only lightweight, coordinate-wise modifications to the standard DDIM update, while explicitly incorporating the measurement model. The key idea is to perform posterior sampling separately along each singular direction of the measurement operator: for each direction, the sampler follows the learned diffusion prior when the observation signal-to-noise ratio (SNR) is below the corresponding diffusion SNR, and switches to a calibrated measurement-based predictor otherwise. We prove that the proposed sampler converges to the Bayesian posterior conditioned on the measurements. Empirical results show that the proposed sampler performs favorably against existing diffusion-based posterior samplers across a range of image restoration tasks, achieving the best performance on the majority of evaluation metrics considered. Overall, our results convert posterior sampling for noisy linear inverse problems to simple coordinate-wise DDIM updates, yielding an efficient, easy-to-implement algorithm with provable posterior consistency.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
#### 1. Measurement Operator
Not found in extracted context.

#### 2. Diffusion SNR
Not found in extracted context.

#### 3. Bayesian Posterior
Not found in extracted context.

#### 4. Coordinate-wise Modifications
Not found in extracted context.

#### 5. Standard DDIM Update
Not found in extracted context.

### Method Summary
* The proposed algorithm, \pddim, uses a DDIM-type sampler for linear inverse problems with diffusion priors.
* The sampler performs posterior sampling separately along each singular direction of the measurement operator.
* For each direction, the sampler follows the learned diffusion prior when the observation signal-to-noise ratio (SNR) is below the corresponding diffusion SNR, and switches to a calibrated measurement-based predictor otherwise.
* The method requires only lightweight, coordinate-wise modifications to the standard DDIM update.

### Experimental Overview
* Tasks/Datasets: Image restoration tasks
* Baselines/Comparisons: Existing diffusion-based posterior samplers
* Main Claimed Findings: The proposed sampler performs favorably against existing diffusion-based posterior samplers across a range of image restoration tasks, achieving the best performance on the majority of evaluation metrics considered.

### What to Verify in the PDF
* Details about the measurement model and its incorporation into the sampler.
* Proofs of the convergence of the proposed sampler to the Bayesian posterior conditioned on the measurements.
* Empirical results and evaluation metrics used to compare the performance of the proposed sampler with existing diffusion-based posterior samplers.
{% endraw %}

{% raw %}
## 2) ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling
- **Authors:** Chirag Vashist, Ke Li
- **arXiv:** [2607.19332](https://arxiv.org/abs/2607.19332v1) · [pdf](https://arxiv.org/pdf/2607.19332v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.CV

### Abstract
> Generative models have undergone many generations of evolution, from VAEs/GANs to diffusion/flow matching. Along the way, the underlying techniques have become more complicated and various beliefs about what drives strong empirical performance have taken hold. Due to the success of diffusion models and flow matching, one of the more common beliefs is the importance of transforming the noise distribution to the data distribution gradually through many small transformations. We ask whether this is truly necessary, and take a minimalist approach to designing a competitive generative model. We start with the bare-bones essentials, namely just a training objective and a model. We purposefully make both simple. For the training objective, we choose Implicit Maximum Likelihood Estimation (IMLE), and eschew more complicated alternatives such as variational inference, adversarial training and numerical integration. For the model, we eschew transformers and instead choose a moderately sized convolutional network. Then we judiciously added elements that are truly essential, which surprisingly do not include iterative denoising. The result is a single-step parameter-efficient generative model that produces high quality samples at fast speed: it achieves an FID of 2.56 on ImageNet 256 and simultaneously attains good precision and recall.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Implicit Maximum Likelihood Estimation (IMLE) Objective
```math
L = \mathbb{E}_{x \sim p(x)} \left[ \log p(x) \right]
```
Symbols: `L`, `x`, `p(x)`, `p(x)` (note: `p(x)` is repeated, likely a typo)
Why it matters: This is the training objective used in the ROMS-IMLE model, which aims to maximize the likelihood of the data distribution.

### 2. No explicit mention of the convolutional network architecture
No equation to explain.

### 3. No explicit mention of the diffusion or flow matching models
No equation to explain.

### 4. No explicit mention of the FID score calculation
No equation to explain.

### 5. No explicit mention of the precision and recall calculation
No equation to explain.

**Method Summary**
==================

* The ROMS-IMLE model uses Implicit Maximum Likelihood Estimation (IMLE) as the training objective.
* The model architecture consists of a moderately sized convolutional network.
* The model does not employ iterative denoising.
* The model is designed to be single-step and parameter-efficient.

**Experimental Overview**
=========================

* Tasks/Datasets: ImageNet 256
* Baselines/Comparisons: Not mentioned in the abstract
* Main claimed findings: The ROMS-IMLE model achieves an FID of 2.56 on ImageNet 256 and produces high-quality samples at fast speed.

**What to Verify in the PDF**
=============================

* The exact architecture of the convolutional network used in the ROMS-IMLE model.
* The implementation details of the Implicit Maximum Likelihood Estimation (IMLE) objective.
* The evaluation metrics used to measure the performance of the ROMS-IMLE model (e.g. precision, recall, FID score).
* The computational speedup achieved by the single-step parameter-efficient design of the ROMS-IMLE model.
{% endraw %}

{% raw %}
## 3) ISO: An RLVR-Native Optimization Stack
- **Authors:** Hanqing Zhu, Wenyan Cong, Zhizhou Sha, Sagnik Mukherjee, Xinyuan Song, David González-Martínez, Xiaoxia Wu, Yuandong Tian, Shiwei Liu, David Z. Pan, Zhangyang "Atlas" Wang
- **arXiv:** [2607.19331](https://arxiv.org/abs/2607.19331v1) · [pdf](https://arxiv.org/pdf/2607.19331v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.19331v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Reinforcement learning with verifiable rewards (RLVR) is rapidly advancing the reasoning capabilities of language models, yet the optimization layer that converts reward feedback into weight-space updates remains poorly understood. Building on our prior analysis (Zhu et al., 2025), we study this missing layer through the singular structure of model weights and identify spectral inheritance: RLVR can reuse the base model's weight spectra while acquiring new behavior through changes in the associated input and output singular frames. We operationalize spectral inheritance as Isospectral Optimization (ISO), an RLVR-native, fixed-spectrum optimization framework with complementary offline and online instantiations. Offline, ISO-Merger combines the frame changes of shared-base specialists into a single fixed-spectrum model, requiring no post-merge data, rollouts, gradient updates, or on-policy distillation (OPD). It recovers complementary specialist capabilities and achieves the strongest aggregate performance among the compared data-free merging methods. Online, ISO-Optimizer applies a chosen base optimizer, including AdamW and Muon, to the frame variables while keeping the base spectra fixed. Across reasoning and coding tasks ranging from 1.5B to 8B parameters, ISO-Optimizer improves accuracy in the reported runs and reaches matched scores with substantially fewer training steps. On Qwen3-8B-Base, AdamW reaches an aggregate accuracy of 0.495 after 270 training steps. ISO-AdamW reaches the same accuracy after only 100 training steps and improves further to 0.509 after 210 training steps. Together, ISO offers a concrete answer to RLVR's missing optimization layer: rather than inheriting pre-training optimization wholesale, design post-training around the structure of reward-driven adaptation: inherit the spectrum, optimize the frames.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 0.495

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: 0.509

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 3: \Sigma_{0}

* Equation: Σ (sigma) notation for a sum.
* Symbols: Σ, 0
* Why it matters: Represents the base model's weight spectra.

### Equation 4: \alpha

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 5: (U,V)

* Equation: Not found in extracted context.
* Symbols: U, V
* Why it matters: Represents the induced weight motion for infinitesimal Stiefel-factor changes.

**Method Summary**
==================

* The ISO (ISO-Merger) algorithm composes multiple RLVR (Reinforcement Learning with Verifiable Rewards) specialists from a shared base without post-merge data, rollouts, or distillation.
* ISO retains each expert's learned frames (U, V) while reusing the shared base spectrum Σ0.
* The algorithm is designed for two instantiations: ISO-Merger and ISO-Optimizer.
* ISO-Merger is tested in two expert-composition settings, comparing against representative training-free merging baselines.

**Experimental Overview**
=========================

* Tasks/Datasets: Two-stage vision-language-action RL pipeline, Qwen2.5-VL-3B-Instruct.
* Baselines/Comparisons: Task Arithmetic, TIES, TSV-Merge, RAM, OrthoMerge-G-TIES.
* Main claimed findings:
	+ Both frames must remain adaptable for optimal remix within both incoming subspaces.
	+ Retaining only the incoming output or input subspace leaves substantial residual updates.
	+ Retaining the incoming spectrum while adapting both frames leaves a low residual update.

**What to Verify in the PDF**
=============================

* The full benchmark protocols, decoding settings, baseline hyperparameters, and best@4/worst@4 results in Appendix F.
* The implementation details of the ISO-Merger algorithm, including the full procedure summarized in Algorithm 1.
* The evaluation of ISO-Optimizer's improvement in RLVR convergence when applied to base optimizers such as AdamW and Muon.
{% endraw %}

{% raw %}
## 4) CircuitKIT : Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability
- **Authors:** Pratinav Seth, Hem Gosalia, Aditya Kasliwal, Vinay Kumar Sankarapu
- **arXiv:** [2607.19317](https://arxiv.org/abs/2607.19317v1) · [pdf](https://arxiv.org/pdf/2607.19317v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.CL, cs.ET

### Abstract
> Circuit analysis can support not only model explanation but also downstream interventions such as pruning, editing, steering, and selective fine-tuning. However, conducting such analyses currently requires stitching together separate implementations for discovery, evaluation, and intervention, as well as hand-authoring the contrastive prompts required by many discovery methods. This fragmentation makes methods difficult to compare and limits their application beyond canonical tasks. We introduce CircuitKIT, a source-available library that connects the circuit-analysis workflow through a typed, serializable representation. CircuitKIT provides a suite of discovery algorithms, declarative interfaces for mapping structured data into discovery tasks, complementary circuit diagnostics, and downstream application modules. Together, these components provide common infrastructure for conducting and comparing circuit analyses. The library, examples, notebooks, and documentation are released at https://github.com/Lexsi-Labs/CircuitKIT .
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
No formulas are explicitly mentioned in the extracted context.

### Method Summary
* CircuitKIT provides a suite of discovery algorithms for circuit analysis.
* The library offers a typed, serializable representation for connecting the circuit-analysis workflow.
* CircuitKIT includes declarative interfaces for mapping structured data into discovery tasks.
* The library provides complementary circuit diagnostics and downstream application modules.
* CircuitKIT aims to support not only model explanation but also downstream interventions such as pruning, editing, steering, and selective fine-tuning.

### Experimental Overview
* Tasks/Datasets: Not explicitly mentioned in the extracted context.
* Baselines/Comparisons: Not mentioned in the extracted context.
* Main Claimed Findings: CircuitKIT provides a common infrastructure for conducting and comparing circuit analyses.

### What to Verify in the PDF
* Details about the specific tasks and datasets used in the experiments.
* The comparison with existing baselines and the results of the experiments.
* The specific downstream interventions supported by CircuitKIT and the results of the evaluation.
{% endraw %}

{% raw %}
## 5) Off-Context GRPO: Learning to Reason on Hard Problems using Privileged Information
- **Authors:** Priyank Agrawal, Ankur Samanta, Shervin Ghasemlou, Jalaj Bhandari, Kavosh Asadi, Daniel Jiang, Aditya Modi
- **arXiv:** [2607.19313](https://arxiv.org/abs/2607.19313v1) · [pdf](https://arxiv.org/pdf/2607.19313v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.19313v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Reinforcement learning with verifiable rewards (RLVR) improves reasoning in large language models. Yet, typical RLVR approaches fail on difficult problems: when a model cannot generate any correct solutions, it receives \textit{zero} learning signal. Providing privileged guidance during training, such as solution prefixes, can help overcome this learning cliff by steering the model towards {correct solutions with non-zero reward}. {We call these rollouts \textit{off-context}: they are generated from a training prompt that contains privileged guidance, while the target objective is defined by the original prompt without that guidance.} {We introduce} Off-Context GRPO (OC-GRPO), a minimally modified variant of GRPO that uses guided rollouts but applies an importance-corrected objective to steer the update back toward the original unguided objective, avoiding the mismatch that destabilizes uncorrected guided training. Empirically, our algorithm achieves a 3.9\% absolute improvement (13.8\% relative gain) over vanilla GRPO on average across standard mathematical reasoning benchmarks with negligible additional cost.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================================

### Equation 1: y_{1}\quad r=0

* Equation: y_{1}\quad r=0
* Symbols: y_{1}, r
* Why it matters: This equation represents a scenario where the model receives a reward of 0, indicating that it has not generated a correct solution.

### Equation 2: y_{2}\quad r=0

* Equation: y_{2}\quad r=0
* Symbols: y_{2}, r
* Why it matters: Similar to Equation 1, this equation represents another scenario where the model receives a reward of 0.

### Equation 3: y_{3}\quad r=0

* Equation: y_{3}\quad r=0
* Symbols: y_{3}, r
* Why it matters: This equation represents yet another scenario where the model receives a reward of 0.

### Equation 4: y_{4}\quad r=0

* Equation: y_{4}\quad r=0
* Symbols: y_{4}, r
* Why it matters: This equation represents a scenario where the model receives a reward of 0.

### Equation 5: y_{1}\quad r=1

* Equation: y_{1}\quad r=1
* Symbols: y_{1}, r
* Why it matters: This equation represents a scenario where the model receives a reward of 1, indicating that it has generated a correct solution.

**Method Summary**
=====================

* The authors propose Off-Context GRPO (OC-GRPO), a variant of GRPO that uses guided rollouts but applies an importance-corrected objective to steer the update back toward the original unguided objective.
* OC-GRPO is designed to overcome the learning cliff problem in RLVR, where a model cannot generate any correct solutions and receives zero learning signal.
* The authors use a minimally modified variant of GRPO, which uses guided rollouts but applies an importance-corrected objective to steer the update back toward the original unguided objective.

**Experimental Overview**
==========================

* Tasks/Datasets: The authors evaluate OC-GRPO on standard mathematical reasoning benchmarks, including MATH, AIME, Gaokao2023, and OmniMath.
* Baselines/Comparisons: The authors compare OC-GRPO against four baselines: vanilla GRPO, POPE*, PrefixRL*, and BREAD*.
* Main Claimed Findings: OC-GRPO achieves a 3.9% absolute improvement (13.8% relative gain) over vanilla GRPO on average across standard mathematical reasoning benchmarks.

**What to Verify in the PDF**
=============================

* The authors claim that OC-GRPO is a minimally modified variant of GRPO, but the PDF does not provide a detailed explanation of the modifications made to GRPO.
* The authors also claim that OC-GRPO is designed to overcome the learning cliff problem in RLVR, but the PDF does not provide a detailed explanation of how OC-GRPO addresses this problem.
* The authors provide experimental results for OC-GRPO on various benchmarks, but the PDF does not provide a detailed explanation of the experimental setup or the evaluation protocol used.
{% endraw %}
