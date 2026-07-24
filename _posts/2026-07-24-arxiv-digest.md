---
layout: post
title: "Daily arXiv Digest — 2026-07-24 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Expanding Flow Maps
- **Authors:** Sophia Tang, Pranam Chatterjee
- **arXiv:** [2607.21585](https://arxiv.org/abs/2607.21585v1) · [pdf](https://arxiv.org/pdf/2607.21585v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG

### Abstract
> Flow-based generative models have enabled remarkable progress in fast and controllable generation across continuous and discrete state spaces, yet existing parameterizations are constrained to fixed dimensions or fixed sequence lengths. Here, we introduce Expanding Generative Flows (EFlows), which define flows between distributions of increasing dimensionality along an expanding interpolant that grows the state by augmenting it with conditional noise. Building on this construction, we propose Expanding Flow Maps (EFMs), a new class of flow maps that distill the expanding interpolant into efficient few-step generative models. Each EFM factors the map between any two timesteps into two learnable operations: an expand operator, which augments the state space with new coordinates or tokens conditioned on the current state, and a transport map, which pushes the expanded state forward along the interpolant. Composing these operators yields a single map that jointly expands and denoises the state, recovering existing fixed-canvas flows and flow maps as the special case in which the expand operator is the identity. We further extend the framework to the discrete simplex, enabling variable-size graph generation and variable-length sequence generation. Across both continuous and discrete modalities, we establish EFlows and EFMs as a principled framework for settings in which output size is itself a learned, controllable degree of freedom.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Expanding Interpolant Construction

Not found in extracted context.

### 2. Expand Operator

Not found in extracted context.

### 3. Transport Map

Not found in extracted context.

### 4. EFM Composition

Not found in extracted context.

### 5. Fixed-Canvas Flows and Flow Maps

Not found in extracted context.

**Method Summary**
==================

* Expanding Generative Flows (EFlows) define flows between distributions of increasing dimensionality along an expanding interpolant.
* Expanding Flow Maps (EFMs) distill the expanding interpolant into efficient few-step generative models.
* Each EFM factors the map between any two timesteps into two learnable operations: an expand operator and a transport map.
* The expand operator augments the state space with new coordinates or tokens conditioned on the current state.
* The transport map pushes the expanded state forward along the interpolant.

**Experimental Overview**
========================

* Tasks/Datasets: Not found in extracted context.
* Baselines/Comparisons: Not found in extracted context.
* Main Claimed Findings: EFlows and EFMs enable variable-size graph generation and variable-length sequence generation across both continuous and discrete modalities.

**What to Verify in the PDF**
=============================

* Details on the Expanding Interpolant Construction, including the mathematical formulation of the expanding interpolant.
* The mathematical formulation of the expand operator and transport map.
* Experimental results and details on the tasks/datasets, baselines, and comparisons used to evaluate EFlows and EFMs.
{% endraw %}

{% raw %}
## 2) Synthetic data generation framework for quality control automation in gravure printing
- **Authors:** Korota Arsène Coulibaly, Mohamed Hamlich, Khalid Hmali, Andrea Trombin
- **arXiv:** [2607.21577](https://arxiv.org/abs/2607.21577v1) · [pdf](https://arxiv.org/pdf/2607.21577v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.21577v1))
- **Categories:** cs.CV, cs.AI, cs.LG, eess.IV

### Abstract
> Quality control in printing, particularly in rotogravure printing, still depends on slow, costly, and subjective manual inspection. Automated surface defect detection is critical for maintaining high-quality standards in rotogravure printing. Deep learning models give prospects for automation. However, training robust deep learning models, such as YOLO or Vision Transformers, is heavily hindered by the extreme scarcity of real-world industrial defects images. To overcome this limitation, this paper introduces a novel synthetic data generation framework tailored for rotogravure printing quality control. The proposed pipeline automatically generates high-fidelity images of specific printing defects (creases, streaks, misregistration, etc.) and outputs corresponding bounding boxes and annotations. To validate the framework, a synthetic dataset of 7533 images was generated and used to train the state-of-the-art object-detection model RFDETR. Experimental results demonstrate that the model trained on our synthetic data achieves a Mean Average Precision (mAP) of 80.9\% on real industrial testing samples. This framework provides a zero-cost, rapid-deployment solution for automating defect inspection in printing lines without requiring massive manual data collection.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: D_{clean}
\[ D_{clean} \]
Symbols: \( D_{clean} \)
Why it matters: This equation represents the set of clean images used to train the model.

### Equation 2: F_{defects}
\[ F_{defects} \]
Symbols: \( F_{defects} \)
Why it matters: This equation represents the set of defects (e.g., creases, streaks, misregistration) used to generate synthetic images.

### Equation 3: \{f_{1},f_{2},...,f_{k}\}
\[ \{f_{1},f_{2},...,f_{k}\} \]
Symbols: \( f_{i} \) (i = 1 to k)
Why it matters: This equation represents the set of simulation functions (e.g., crease, shift) used to apply defects to images.

### Equation 4: N_{max}
\[ N_{max} \]
Symbols: \( N_{max} \)
Why it matters: This equation represents the maximum number of defects that can be applied to an image.

### Equation 5: D_{defective}
\[ D_{defective} \]
Symbols: \( D_{defective} \)
Why it matters: This equation represents the set of defective images generated using the synthetic data framework.

**Method Summary**
==================

* The proposed framework is applied in the field of rotogravure printing or roll-to-roll printing.
* The framework generates high-fidelity images of specific printing defects (creases, streaks, misregistration, etc.) and outputs corresponding bounding boxes and annotations.
* The framework uses a simulation function to apply defects to healthy images, ensuring diversity in the generated synthetic data.

**Experimental Overview**
========================

* Tasks: The framework is used to train the state-of-the-art object-detection model RFDETR on a synthetic dataset of 7533 images.
* Datasets: The synthetic dataset is generated using the proposed framework.
* Baselines/Comparisons: The model trained on the synthetic data achieves a Mean Average Precision (mAP) of 80.9% on real industrial testing samples.
* Main claimed findings: The framework provides a zero-cost, rapid-deployment solution for automating defect inspection in printing lines without requiring massive manual data collection.

**What to Verify in the PDF**
=============================

* The implementation details of the simulation function and the generation of synthetic images.
* The evaluation metrics used to measure the performance of the model trained on the synthetic data.
* The comparison of the proposed framework with other state-of-the-art methods for defect detection in printing.
{% endraw %}

{% raw %}
## 3) X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment
- **Authors:** Dongjie Fu, Di Cao, Xize Cheng, Zihan Zhang, Wenxu Jia, Yifu Chen, Shengpeng Ji, Yu Zhang, Tao Jin
- **arXiv:** [2607.21550](https://arxiv.org/abs/2607.21550v1) · [pdf](https://arxiv.org/pdf/2607.21550v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.21550v1))
- **Categories:** cs.LG

### Abstract
> While large audio-language models have achieved remarkable progress in auditory perception, they still lag behind text-based large language models in deep logical reasoning, primarily due to the scarcity of high-quality audio reasoning data. To bridge this gap, we propose X$^3$-OPD, a cross-modal on-policy distillation framework that transfers reasoning capabilities from a powerful text teacher to an audio-language student. During training, the student generates reasoning trajectories conditioned on its own acoustic perception, while the teacher provides token-level guidance using matched textual inputs and verified answers. We further construct a three-tier symmetric corpus covering textual reasoning rendered into speech, audio-event reasoning grounded in complex acoustic scenes, and spoken-dialogue reasoning involving paralinguistic cues. This design extends cross-modal distillation beyond textually recoverable content to reasoning grounded in non-linguistic events, prosody, and conversational context. Experiments on MMSU, MMAU, BIG Bench Audio, and MMAR demonstrate that X$^3$-OPD substantially improves audio-grounded reasoning and chain-of-thought quality while largely preserving the model's existing capabilities under domain shift.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: (x_{t},x_{a},q,a^{\star})

* Equation: (x_{t},x_{a},q,a^{\star})
* Symbols: x_{t} (text input), x_{a} (acoustic input), q (question), a^{\star} (ground truth answer)
* Why it matters: This equation represents a symmetric sample, which is a tuple containing the text input, acoustic input, question, and ground truth answer. This sample is used to train the model.

### Equation 2: x_{a}

* Equation: x_{a}
* Symbols: x_{a} (acoustic input)
* Why it matters: This equation represents the acoustic input, which is used as input to the audio student model.

### Equation 3: x_{t}

* Equation: x_{t}
* Symbols: x_{t} (text input)
* Why it matters: This equation represents the text input, which is used as input to the text teacher model.

### Equation 4: \pi_{T}(\cdot\mid x_{t},q,a^{\star};\theta_{T})

* Equation: \pi_{T}(\cdot\mid x_{t},q,a^{\star};\theta_{T})
* Symbols: \pi_{T} (frozen text teacher), x_{t} (text input), q (question), a^{\star} (ground truth answer), \theta_{T} (parameters of the text teacher)
* Why it matters: This equation represents the probability distribution of the text teacher model, which is used to generate the text output.

### Equation 5: \theta_{T}

* Equation: \theta_{T}
* Symbols: \theta_{T} (parameters of the text teacher)
* Why it matters: This equation represents the parameters of the text teacher model, which are used to train the model.

**Method Summary**
==================

* The proposed framework consists of three components: a three-tier modality-paired corpus, a cross-modal on-policy distillation objective, and a training recipe.
* The three-tier corpus establishes a uniform schema across textual reasoning, audio-event reasoning, and spoken dialogue.
* The cross-modal on-policy distillation objective scores student rollouts under the matched text input.
* The training recipe combines a brief offline warm-start with on-policy optimization.

**Experimental Overview**
========================

* Tasks/Datasets:
	+ Three-tier corpus containing 27.8K Tier-1, 32K Tier-2, and 12K Tier-3 instances.
	+ Evaluation benchmarks: MMSU, MMAU, BIG Bench Audio, and MMAR.
* Baselines/Comparisons:
	+ Qwen3-Omni-Thinking baseline.
	+ State-of-the-art closed- and open-source systems.
	+ Controlled in-house baselines.
* Main Claimed Findings:
	+ X 3 -OPD demonstrates substantial improvements in complex audio-grounded reasoning.
	+ X 3 -OPD achieves solid gains in semantic and acoustic event understanding.

**What to Verify in the PDF**
=============================

* The construction of the three-tier corpus and the filtering process for Tier-1, Tier-2, and Tier-3 instances.
* The details of the offline warm-start SFT pass and its impact on the model's logical reasoning format and sensitivity to paralinguistic cues.
* The evaluation of the model's performance on the held-out MMAR benchmark and the CoT-quality metrics, Rubrics and CRS.
{% endraw %}

{% raw %}
## 4) Zero-Flow Two-Sample Tests
- **Authors:** Yakun Wang, Leyang Wang, Song Liu, Taiji Suzuki
- **arXiv:** [2607.21542](https://arxiv.org/abs/2607.21542v1) · [pdf](https://arxiv.org/pdf/2607.21542v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.21542v1))
- **Categories:** cs.LG, stat.ML

### Abstract
> We propose a new approach to two-sample testing for deciding whether two sets of samples are drawn from the same distribution. The test is built on a statistical discrepancy based on the zero-flow criterion, termed zero-flow discrepancy (ZFD). We prove the validity of ZFD and propose a practical testing procedure, termed the zero-flow two-sample test (ZF2ST). The key idea is to learn how samples from the two distributions are locally misaligned and use the resulting directional pattern as evidence of distributional difference. By separating witness learning from hypothesis evaluation, ZF2ST can use flexible neural networks while maintaining valid statistical calibration. We develop both regression-based and power-maximized approaches for learning the witness. Experiments on synthetic and image datasets demonstrate that ZF2ST can achieve strong testing power for structured distributional changes while maintaining well-calibrated type-I error.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathbb{R}^{d}$

* Equation: $\mathbb{R}^{d}$
* Symbols: $\mathbb{R}^{d}$ (Euclidean space of dimension $d$)
* Why it matters: This equation represents the sample space, which is a fundamental concept in statistics and machine learning.

### Equation 2: $S_{X}=\{\mathbf{x}_{i}\}_{i=1}^{n}\overset{\mathrm{i.i.d.}}{\sim}P$

* Equation: $S_{X}=\{\mathbf{x}_{i}\}_{i=1}^{n}\overset{\mathrm{i.i.d.}}{\sim}P$
* Symbols: $S_{X}$ (sample space of $X$), $\{\mathbf{x}_{i}\}_{i=1}^{n}$ (set of $n$ samples from $X$), $\overset{\mathrm{i.i.d.}}{\sim}$ (independently and identically distributed)
* Why it matters: This equation represents the training data for the two-sample test, which is drawn from a distribution $P$.

### Equation 3: $S_{Y}=\{\mathbf{y}_{j}\}_{j=1}^{m}\overset{\mathrm{i.i.d.}}{\sim}Q$

* Equation: $S_{Y}=\{\mathbf{y}_{j}\}_{j=1}^{m}\overset{\mathrm{i.i.d.}}{\sim}Q$
* Symbols: $S_{Y}$ (sample space of $Y$), $\{\mathbf{y}_{j}\}_{j=1}^{m}$ (set of $m$ samples from $Y$), $\overset{\mathrm{i.i.d.}}{\sim}$ (independently and identically distributed)
* Why it matters: This equation represents the testing data for the two-sample test, which is drawn from a distribution $Q$.

### Equation 4: $H_{0}:P=Q$

* Equation: $H_{0}:P=Q$
* Symbols: $H_{0}$ (null hypothesis), $P$ (distribution of $X$), $Q$ (distribution of $Y$)
* Why it matters: This equation represents the null hypothesis of the two-sample test, which assumes that the two distributions are the same.

### Equation 5: $H_{1}:P\neq Q$

* Equation: $H_{1}:P\neq Q$
* Symbols: $H_{1}$ (alternative hypothesis), $P$ (distribution of $X$), $Q$ (distribution of $Y$)
* Why it matters: This equation represents the alternative hypothesis of the two-sample test, which assumes that the two distributions are different.

**Method Summary**
==================

* The proposed method, Zero-Flow Two-Sample Tests (ZF2ST), uses a statistical discrepancy based on the zero-flow criterion to test whether two sets of samples are drawn from the same distribution.
* The method learns a directional pattern in the data to detect distributional differences.
* Two approaches are proposed for learning the witness: least-square regression and power-maximized approaches.
* The method is validated using synthetic and image datasets.

**Experimental Overview**
========================

* Tasks/Datasets: Synthetic and image datasets are used to evaluate the performance of ZF2ST.
* Baselines/Comparisons: The following baselines are compared to ZF2ST:
	+ MMD-D (Liu et al., 2020)
	+ C2ST (Lopez-Paz and Oquab, 2016)
	+ C2ST-L (Cheng and Cloninger, 2022)
	+ MMD-O (Sutherland et al., 2016)
* Main Claimed Findings: ZF2ST achieves strong testing power for structured distributional changes while maintaining well-calibrated type-I error.

**What to Verify in the PDF**
=============================

* The dynamic pairing strategy introduced in Appendix C.1.
* The power analysis and type-I error results for the different approaches to learning the witness.
* The evaluation protocol and configuration details in Appendix D.
* The visualization of synthetic datasets in Figure ˜ 4.
{% endraw %}

{% raw %}
## 5) Test-Time Scaling via Error Localization
- **Authors:** Rajiv Shailesh Chitale, Rahul Madhavan, Taneesh Gupta, Deepanway Ghosal, Aravindan Raghuveer
- **arXiv:** [2607.21453](https://arxiv.org/abs/2607.21453v1) · [pdf](https://arxiv.org/pdf/2607.21453v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.21453v1))
- **Categories:** cs.LG

### Abstract
> Scaling inference-time computation has emerged as a reliable method to improve the performance of large language models on complex reasoning and programming tasks. However, standard approaches such as independent sampling and sequential multi-turn refinement operate without token-level credit assignment, resulting in computational inefficiency, since valid reasoning prefixes are frequently discarded. In this work, we introduce Test-Time Scaling via Error Localization (TTEL), an inference-time algorithm that utilizes fixed or environment feedback to perform token-level error localization. By comparing conditional probabilities under informed feedback against a null-context baseline, TTEL isolates the step at which an error occurred. The algorithm then truncates the trajectory and branches a new generation, maximally reusing the valid prefix. Extensive evaluations demonstrate that TTEL establishes strictly dominating Pareto frontiers across sequential reasoning domains, measured by pass-at-k vs. generated-token cost. With Qwen3-8B on LiveCodeBench, TTEL attains a pass@64 of 71.0% while generating approximately half as many tokens as independent sampling (360.4k vs. 735.0k). Generalizing to math benchmarks AIME-2025 and HMMT-2025, TTEL cleanly outperforms competing test-time baselines across both Qwen3-8B and Qwen3-4B-Thinking-2507.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: π_{\theta}(\cdot\mid x)/\pi_{\theta}(\cdot\mid x,f)

* Equation: π_{\theta}(\cdot\mid x)/\pi_{\theta}(\cdot\mid x,f)
* Symbols: π_{\theta} (theta), x (problem prompt), f (feedback)
* Why it matters: This equation represents the token-level divergence signal used to detect errors in the generated trajectory.

### Equation 2: π_{\theta}

* Equation: π_{\theta}
* Symbols: π_{\theta} (theta)
* Why it matters: This equation is not explicitly defined in the context, but it seems to represent the pre-trained autoregressive language model.

### Equation 3: \mathcal{V}

* Equation: \mathcal{V}
* Symbols: \mathcal{V} (vocabulary)
* Why it matters: This equation is not explicitly defined in the context, but it seems to represent the vocabulary of the language model.

### Equation 4: y = (y_{1}, \dots, y_{N})

* Equation: y = (y_{1}, \dots, y_{N})
* Symbols: y (trajectory), N (number of tokens)
* Why it matters: This equation represents the generated trajectory of tokens.

### Equation 5: p_{t}^{(S)} := \pi_{\theta}(y_{t} \mid x, y_{<t})

* Equation: p_{t}^{(S)} := \pi_{\theta}(y_{t} \mid x, y_{<t})
* Symbols: p_{t}^{(S)} (student token probability), \pi_{\theta} (theta), y_{t} (token), x (problem prompt), y_{<t} (prefix)
* Why it matters: This equation represents the student token probability at time t, which is used to detect errors in the generated trajectory.

**Method Summary**
==================

* The proposed method, Test-Time Scaling via Error Localization (TTEL), operates on a single pre-trained language model π_{\theta} that serves as both the generator and the evaluator of its own outputs.
* TTEL uses fixed or environment feedback to perform token-level error localization, which involves detecting and filtering token-level error signals (spikes) and utilizing those signals to guide a search and branching strategy over candidate solutions.
* The algorithm performs token-level spike detection by re-scoring the same trajectory under two alternative contexts: a feedback-conditioned context using the actual feedback f and a null-feedback context using a non-diagnostic message f_{\varnothing}.
* The filtered spike score is used to prune and branch an inference-time search tree, which is then used to generate a fresh attempt from the context without anchoring.

**Experimental Overview**
========================

* Tasks/Datasets: The proposed method is evaluated on two challenging domains: complex mathematical reasoning and code generation.
* Baselines/Comparisons: The method is compared to standard multi-turn paradigms, including independent sampling and sequential multi-turn refinement.
* Main Claimed Findings: The proposed method establishes strictly dominating Pareto frontiers across sequential reasoning domains, measured by pass-at-k vs. generated-token cost.

**What to Verify in the PDF**
=============================

* The experimental results, including the compute-optimal scaling capabilities of TTEL across domains and the detailed ablations dissecting how structural context and filtering using a non-diagnostic feedback baseline drive its error localization precision.
* The theoretical analysis, including the formalization of the algorithm and the analysis of the search and branching strategy.
* The evaluation of the method on the AIME-2025 and HMMT-2025 datasets, including the results on pass@k and generated-token cost.
{% endraw %}
