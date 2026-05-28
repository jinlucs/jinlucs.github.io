---
layout: post
title: "Daily arXiv Digest — 2026-05-28 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) AREA: Attribute Extraction and Aggregation for CLIP-Based Class-Incremental Learning
- **Authors:** Zhen-Hao Xie, Yu-Cheng Shi, Da-Wei Zhou
- **arXiv:** [2605.28809](https://arxiv.org/abs/2605.28809v1) · [pdf](https://arxiv.org/pdf/2605.28809v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.28809v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> Class-Incremental Learning (CIL) is important in building real-world learning systems. In CLIP-based CIL, the model performs classification by comparing similarity between visual and textual embeddings obtained from template prompts, e.g., ``a photo of a [CLASS]''. This seemingly monolithic matching process can be decomposed into two conceptually distinct stages: attribute extraction and attribute aggregation. For example, a model may recognize cat using attributes such as fur texture and whiskers. When learning a new class like car, the model must extract additional attributes like wheels and adjust how they are aggregated in the shared representation space. However, since only data from the current task is available, incremental updates can bias both attribute extraction and aggregation toward new classes, leading to catastrophic forgetting. Therefore, we propose AREA for attribute extraction and aggregation in CLIP-based CIL. To stabilize extraction, we anchor class-level visual and textual attributes on the hyperspherical embedding space via principal geodesic analysis. To stabilize aggregation, we learn lightweight task-specific experts with scoring and residual refinement, regularized by a variational information bottleneck objective. During inference, we perform routing over task attribute manifolds via optimal transport for more concise prediction. Experiments show that AREA consistently outperforms SOTA methods. Code is available at https://github.com/LAMDA-CL/ICML2026-AREA.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Set of datasets
\[\{\mathcal{D}^{1},\mathcal{D}^{2},\ldots,\mathcal{D}^{B}\}\]

* Symbols: \(\mathcal{D}^{b}\) (dataset \(b\)), \(B\) (number of datasets)
* Why it matters: This equation represents the set of datasets used for training and testing the model.

### Equation 2: Dataset definition
\[\mathcal{D}^{b}=\{(\mathbf{x}_{i},y_{i})\}_{i=1}^{n_{b}}\]

* Symbols: \(\mathbf{x}_{i}\) (input feature), \(y_{i}\) (label), \(n_{b}\) (number of samples in dataset \(b\))
* Why it matters: This equation defines a dataset as a collection of input features and their corresponding labels.

### Equation 3: Number of samples in a dataset
\[n_{b}\]

* Symbols: \(n_{b}\) (number of samples in dataset \(b\))
* Why it matters: This equation represents the number of samples in a dataset.

### Equation 4: Input feature dimension
\[\mathbf{x}_{i}\in\mathbb{R}^{D}\]

* Symbols: \(\mathbf{x}_{i}\) (input feature), \(D\) (dimensionality of input features)
* Why it matters: This equation specifies the dimensionality of the input features.

### Equation 5: Label space
\[y_{i}\in\mathcal{Y}_{b}\]

* Symbols: \(y_{i}\) (label), \(\mathcal{Y}_{b}\) (label space of dataset \(b\))
* Why it matters: This equation defines the label space of a dataset.

### Equation 6: Label space uniqueness
\[\mathcal{Y}_{b}\cap\mathcal{Y}_{b^{\prime}}=\varnothing\]

* Symbols: \(\mathcal{Y}_{b}\) (label space of dataset \(b\)), \(\mathcal{Y}_{b^{\prime}}\) (label space of dataset \(b^{\prime}\))
* Why it matters: This equation ensures that the label spaces of different datasets are disjoint.

### Equation 7: Dataset index uniqueness
\[b\neq b^{\prime}\]

* Symbols: \(b\) (dataset index), \(b^{\prime}\) (dataset index)
* Why it matters: This equation ensures that the dataset indices are unique.

### Equation 8: Regularized transport cost
\[\mathcal{D}^{b}=\sum_{j=1}^{N_{b}}w_{j}\delta_{\mathbf{v}_{j}}\]

* Symbols: \(\mathcal{D}^{b}\) (regularized transport cost), \(w_{j}\) (weight), \(\delta_{\mathbf{v}_{j}}\) (Dirac delta function), \(\mathbf{v}_{j}\) (attribute atom)
* Why it matters: This equation defines the regularized transport cost as a weighted sum of Dirac delta functions.

**Method Summary**
==================

* **Geometry-Aware Anchoring**: Anchor class-level visual and textual attributes on the hypersphere via Principal Geodesic Analysis (PGA) to prevent extraction drift.
* **Robust Evidence Aggregation**: Aggregate anchored attributes using scoring and residual refinement, regularized by a variational information bottleneck objective for stable and generalizable evidence.
* **Distributional Task Routing**: Perform soft routing over task manifolds to select compatible task experts under cross-task overlap.
* **Hyperparameter Robustness**: Evaluate the stability of A rea against key hyperparameters, including the intervention loss weight and the compression loss weight.

**Experimental Overview**
========================

* **Tasks/Datasets**: Evaluate A rea on nine benchmark datasets, including CIFAR100, CUB200, ObjectNet, ImageNet-R, FGVCAircraft, StanfordCars, Food101, SUN397, and UCF101.
* **Baselines/Comparisons**: Compare A rea against a broad set of state-of-the-art continual learning baselines, including SOTA methods.
* **Main Claimed Findings**: A rea consistently achieves superior performance, outperforming most prior methods by more than 5% in both average accuracy and last-task accuracy.

**What to Verify in the PDF**
=============================

* **Derivation of Lipschitz Continuity**: Verify the derivation of the Lipschitz continuity of the Sinkhorn distance.
* **Theoretical Analysis**: Verify the theoretical analysis of the Sinkhorn distance and its properties.
* **Experimental Results**: Verify the experimental results, including the performance curves and accuracy values.
{% endraw %}

{% raw %}
## 2) Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation
- **Authors:** Jiahe Pan, Stelian Coros, Jitendra Malik, Toru Lin
- **arXiv:** [2605.28812](https://arxiv.org/abs/2605.28812v1) · [pdf](https://arxiv.org/pdf/2605.28812v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.28812v1))
- **Categories:** cs.RO, cs.AI, cs.LG

### Abstract
> A primary bottleneck in contact-rich manipulation is the difficulty of collecting real-world data. Sim-to-real reinforcement learning offers a scalable alternative, but the simulation-reality gap prevents information-dense modalities like touch from being effectively used. Existing sim-to-real methods often mitigate this gap by simplifying tactile data into coarse low-dimensional features -- sacrificing the richness required for complex manipulation. In this work, we introduce Center-of-Pressure (CoP), an effective tactile representation grounded in physical principles that preserves dense contact information while maintaining robustness for sim-to-real transfer. To support this representation, we propose a sensor calibration scheme based on differentiable dynamics, enabling the estimation of taxel orientations without requiring ground-truth force measurements. We evaluate CoP on two blind, challenging contact-rich manipulation tasks: peg-in-hole insertion and ball balancing. Across both tasks, policies conditioned on CoP achieve zero-shot sim-to-real transfer on a multi-fingered hand, and outperform both coarse binary-contact and raw-taxel baselines. Analysis of learned policy states further suggests that CoP-conditioned policies encode task-relevant physical properties, such as object mass, as an emergent byproduct of control.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `{^{\mathcal{S}}f_{\rm{cop}}\in\mathbb{R}^{3}}`

* Equation: `{^{\mathcal{S}}f_{\rm{cop}}\in\mathbb{R}^{3}}`
* Symbols: `{^{\mathcal{S}}f_{\rm{cop}}}`, `{^{\mathcal{S}}}`, `\mathbb{R}^{3}`
* Why it matters: This equation represents the Center-of-Pressure (CoP) force vector in the sensor frame `{^{\mathcal{S}}}`, which is a compact local contact descriptor.

### Equation 2: `{^{\mathcal{S}}p_{\rm{cop}}\in\mathbb{R}^{3}}`

* Equation: `{^{\mathcal{S}}p_{\rm{cop}}\in\mathbb{R}^{3}}`
* Symbols: `{^{\mathcal{S}}p_{\rm{cop}}}`, `{^{\mathcal{S}}}`, `\mathbb{R}^{3}`
* Why it matters: This equation represents the Center-of-Pressure (CoP) contact position in the sensor frame `{^{\mathcal{S}}}`, which is a compact local contact descriptor.

### Equation 3: `\mathcal{S}`

* Equation: `\mathcal{S}`
* Symbols: `\mathcal{S}`
* Why it matters: This equation represents the sensor frame, which is used to express the CoP force vector and contact position.

### Equation 4: `f_{cop}`

* Equation: `f_{cop}`
* Symbols: `f_{cop}`, `{^{\mathcal{S}}}`, `\mathbb{R}^{3}`
* Why it matters: This equation represents the CoP force vector, which is a compact local contact descriptor.

### Equation 5: `p_{cop}`

* Equation: `p_{cop}`
* Symbols: `p_{cop}`, `{^{\mathcal{S}}}`, `\mathbb{R}^{3}`
* Why it matters: This equation represents the CoP contact position, which is a compact local contact descriptor.

**Method Summary**
==================

* The authors propose a physics-aware contact representation called Center-of-Pressure (CoP) to enable sim-to-real transfer of learned policies.
* CoP is a compact local contact descriptor that preserves dense contact information while maintaining robustness for sim-to-real transfer.
* The authors also propose a sensor calibration scheme based on differentiable dynamics to estimate taxel orientations without requiring ground-truth force measurements.

**Experimental Overview**
========================

* Tasks:
	+ Peg-in-hole insertion
	+ Ball balancing
* Baselines:
	+ Proprioception (base)
	+ Binary contact per sensing array (binary)
	+ CoP force magnitude (mag)
	+ Force vector-only (vec)
	+ Contact position-only (pos)
	+ Raw taxel forces (taxel)
	+ Expert human (human)
* Main claimed findings:
	+ CoP-conditioned policies achieve zero-shot sim-to-real transfer on a multi-fingered hand.
	+ CoP-conditioned policies outperform baselines on both tasks.

**What to Verify in the PDF**
=============================

* The authors claim that the CoP representation preserves dense contact information while maintaining robustness for sim-to-real transfer. Verify this claim by analyzing the mathematical formulation of CoP and its properties.
* The authors propose a sensor calibration scheme based on differentiable dynamics to estimate taxel orientations. Verify the effectiveness of this scheme by analyzing the results of the sensor calibration experiment.
* The authors claim that the CoP-conditioned policies achieve zero-shot sim-to-real transfer on a multi-fingered hand. Verify this claim by analyzing the results of the sim-to-real transfer experiment.
{% endraw %}

{% raw %}
## 3) Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization
- **Authors:** Audrey Chan, Aaron Labbé, Jacob Lavoie, Jordan Bannister, Arsène Fansi Tchango, Guillaume Lajoie, Laurent Charlin
- **arXiv:** [2605.28810](https://arxiv.org/abs/2605.28810v1) · [pdf](https://arxiv.org/pdf/2605.28810v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.28810v1))
- **Categories:** cs.LG, cs.IR, cs.SD

### Abstract
> Functional music applications, from consumer focus and sleep aids to clinical interventions, share a distinctive recommendation problem: success is defined by the listener's affective state, but online experimentation on emotion is ethically constrained, particularly for clinical populations who cannot reliably skip a song or report distress. We describe AMRS, the Affective Music Recommendation System deployed on LUCID's health-and-wellness platforms, which serve clinical users (primarily older adults with neurocognitive conditions) and consumer-wellness users across energize, focus, calm, and sleep modes. AMRS is built around a rollout-based world model: a causal transformer trained on logged listening data to jointly predict engagement, binary rating, and self-reported valence and arousal. The world model serves both as an in-silico simulator for offline policy training and as a stress-testing tool before deployment. A recommender policy initialized by behaviour cloning is fine-tuned offline with Direct Preference Optimization (DPO) against a configurable multi-objective utility function. Under a strict cold-start protocol, the world model predicts both behavioural and affective signals with usable fidelity; DPO improves predicted valence and arousal over the cloned baseline while maintaining a similar diversity profile and avoiding the distributional collapse produced by greedy optimization. We position the work as an early deployed validation of a methodology for affective recommendation when online experimentation is ethically untenable.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: (\hat{e},\hat{r},\hat{v},\hat{a})

* Equation: (\hat{e},\hat{r},\hat{v},\hat{a})
* Symbols: \hat{e}, \hat{r}, \hat{v}, \hat{a} (predicted engagement rate, rating, valence, and arousal)
* Why it matters: This equation represents the predicted feedback signals given a user history and a candidate next song.

### Equation 2: \mathcal{H}_{t}

* Equation: \mathcal{H}_{t}
* Symbols: \mathcal{H}_{t} (user's listening history at time t)
* Why it matters: This equation represents the state of the Markov Decision Process at time t, which is the user's listening history.

### Equation 3: e\in[0,1]

* Equation: e\in[0,1]
* Symbols: e (engagement rate)
* Why it matters: This equation represents the range of values for the engagement rate, which is a continuous signal.

### Equation 4: v\in[0,1]

* Equation: v\in[0,1]
* Symbols: v (valence)
* Why it matters: This equation represents the range of values for the valence, which is a continuous signal.

### Equation 5: a\in[0,1]

* Equation: a\in[0,1]
* Symbols: a (arousal)
* Why it matters: This equation represents the range of values for the arousal, which is a continuous signal.

**Method Summary**
==================

* The authors build a rollout-based world model, a causal transformer trained on logged listening data, to predict all four feedback signals given a user history and a candidate next song.
* The recommender policy is first initialized by behaviour cloning the production policy, then fine-tuned with Direct Preference Optimization (DPO) against a configurable multi-objective utility function.
* The world model serves as an in-silico simulator for offline policy training and as a stress-testing tool before deployment.

**Experimental Overview**
=========================

* Tasks: The authors evaluate the Affective Music Recommendation System (AMRS) on a proprietary dataset drawn from LUCID's deployed platform.
* Datasets: The dataset is split 80/10/10 by user ID using MCCV with 10 random splits.
* Baselines: The authors compare AMRS with Copycat, DPO, and Random/Greedy baselines.
* Main claimed findings: The authors report that DPO improves predicted valence and arousal over the cloned baseline while maintaining a similar diversity profile and avoiding the distributional collapse produced by greedy optimization.

**What to Verify in the PDF**
=============================

* The authors claim that the world model predicts both behavioural and affective signals with usable fidelity under a strict cold-start protocol. Verify this claim by checking the results of the rollout-based world model.
* The authors report that DPO improves predicted valence and arousal over the cloned baseline while maintaining a similar diversity profile. Verify this claim by checking the results of the DPO fine-tuning process.
* The authors mention that the dataset is pooled from the clinical and consumer-wellness applications. Verify this claim by checking the dataset description or the authors' discussion of the dataset.
{% endraw %}

{% raw %}
## 4) Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling
- **Authors:** Xinyu Wang, Mingze Li, Sicheng Lyu, Dongxiu Liu, Kaicheng Yang, Ziyu Zhao, Yufei Cui, Xiao-Wen Chang, Peng Lu
- **arXiv:** [2605.28803](https://arxiv.org/abs/2605.28803v1) · [pdf](https://arxiv.org/pdf/2605.28803v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.28803v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We challenge this assumption with Omega-QVLA, the first training-free post-training quantization framework that compresses both the language backbone and the entire diffusion action head of a VLA model to a uniform W4A4 precision, eliminating the need for mixed-precision allocation. Omega-QVLA combines a composite SVD-Hadamard rotation that equalizes per-channel weight energy while diffusing residual activation outliers with per-step DiT activation scaling quantization that absorbs dynamic-range drift across denoising steps. On LIBERO, Omega-QVLA compresses Pi 0.5 and GR00T N1.5 to W4A4 with 98.0% and 87.8% task success rates, matching or exceeding their FP16 references of 97.1% and 87.0%, while reducing the static memory footprint by 71.3%. Real-world manipulation experiments further confirm smooth, accurate manipulation where prior methods fail. Code is available at https://github.com/UCMP13753/Omega-QVLA.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Ω

* Equation: Ω
* Symbols: Ω, W, X, R
* Why it matters: This equation represents the proposed composite rotation method for equalizing per-channel weight energy while diffusing residual activation outliers. The composite rotation method combines the effects of SVD and Hadamard rotation to improve the statistical properties of the rotated space.

### Equation 2: 

* Equation: 
* Symbols: , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
{% endraw %}

{% raw %}
## 5) CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models
- **Authors:** Abhilash Durgam, Nyle Siddiqui, Jeffrey A. Chan-Santiago, Qiushi Fu, Elakkat D. Gireesh, Mubarak Shah
- **arXiv:** [2605.28792](https://arxiv.org/abs/2605.28792v1) · [pdf](https://arxiv.org/pdf/2605.28792v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.28792v1))
- **Categories:** cs.AI, cs.HC, cs.LG

### Abstract
> Electroencephalography (EEG) is a critical, non-invasive method to monitor electrical brain activity. EEGs can span anywhere from a couple seconds to multiple hours, posing a major hurdle for existing deep learning methods due to two major factors: (1) existing EEG models are predominantly built upon the attention mechanism, incurring quadratic scaling as the sequence length increases, and (2) raw EEG signals must be processed in a sliding-window fashion due to fixed-length input requirements, preventing global understanding of the entire signal. To this extent, we propose CaMBRAIN - the first Causal, Mamba-based state space model (SSM) capable of real-time inference of EEG signals, arguing that bidirectional approaches are needlessly expensive given the causal, unidirectional nature of EEG. However, training such a model is non-trivial, as crucial EEG events can be extremely brief - within fractions of a second - yet separated by long intervals spanning minutes. Current EEG methods use self-supervised objectives that optimize for signal reconstruction, but these are not well suited for streaming SSMs; they fail to explicitly train the hidden state to retain the salient long-range context needed for streaming inference. We therefore introduce a multi-stage self-supervised training pipeline specifically tailored to encourage long-range memory retention and strong performance on EEG signals, while preserving the linear-time complexity of state space models. CaMBRAIN achieves state-of-the-art (SOTA) results across 3 different EEG datasets with >10x higher throughput than existing models, enabling the first model capable of long-range, continuous inference of variable-length EEG signals.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 
\[ \times \]

Symbols: 
- 
- 

Why it matters: Not found in extracted context.

### Equation 2: 
\[ X\in\mathbb{R}^{C\times T} \]

Symbols: 
- 
- 
- 
- 

Why it matters: Represents an EEG segment as a multichannel time series.

### Equation 3: 
\[ G_{T}=\lfloor T/P\rfloor \]

Symbols: 
- 
- 
- 
- 

Why it matters: Calculates the number of patches in an EEG segment.

### Equation 4: 
\[ \mathbf{X}=\{x_{1},\ldots,x_{G_{T}}\} \]

Symbols: 
- 
- 
- 

Why it matters: Represents EEG tokens, which are embedded EEG patches.

### Equation 5: 
\[ x_{t}\in\mathbb{R}^{d} \]

Symbols: 
- 
- 
- 

Why it matters: Represents the EEG content at temporal index t across all channels.

### Equation 6: 
\[ x(t)\in\mathbb{R}^{L} \]

Symbols: 
- 
- 
- 

Why it matters: Not found in extracted context.

### Equation 7: 
\[ h(t)\in\mathbb{R}^{N} \]

Symbols: 
- 
- 
- 

Why it matters: Not found in extracted context.

### Equation 8: 
\[ y(t)\in\mathbb{R}^{L} \]

Symbols: 
- 
- 
- 

Why it matters: Not found in extracted context.

**Method Summary**
==================

* CaMBRAIN is a causal EEG foundation model for continuous streaming inference.
* It operates in a unidirectional, forward-only manner and prioritizes learning representations rather than reconstructing signals.
* The method is built on two key principles: causal, linear-time sequence modeling and representation-level self-supervised learning.
* CaMBRAIN uses a transformer-based embedding for EEG tokens and a state space model for EEG understanding.

**Experimental Overview**
========================

* CaMBRAIN is evaluated on a diverse set of EEG benchmarks, including TUAR, TUAB, MAT, and CHB-MIT.
* The method achieves competitive or superior performance across all benchmarks, with the best AUROC on TUAR and CHB-MIT.
* The results suggest that persistent-state streaming and representation-level training provide strong cross-task EEG representations.

**What to Verify in the PDF**
=============================

* The details of the transformer-based embedding for EEG tokens.
* The implementation of the state space model for EEG understanding.
* The evaluation of the method on out-of-distribution (OOD) scenarios.
{% endraw %}
