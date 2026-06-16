---
layout: post
title: "Daily arXiv Digest — 2026-06-16 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Hierarchical Advantage Weighting for Online RL Fine-Tuning of VLAs from Sparse Episode Outcomes
- **Authors:** Tongyan Fang, Siyuan Huang, Naiyu Fang, Ganlong Zhao, Zhongjin Luo, Jianbo Liu, Xiaogang Wang, Ying Dong, Hongsheng Li
- **arXiv:** [2606.17043](https://arxiv.org/abs/2606.17043v1) · [pdf](https://arxiv.org/pdf/2606.17043v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.17043v1))
- **Categories:** cs.RO, cs.LG

### Abstract
> When pretrained VLA policies are fine-tuned through online RL, each rollout episode produces only a single binary outcome (success or failure), yet the actor update requires per-transition supervision. Existing approaches commonly reduce this sparse outcome to a single scalar reward or advantage signal, which conflates distinct forms of transition-level feedback and provides limited guidance once basic task success becomes achievable. First, a single scalar signal conflates the two objectives of viability and efficiency; once basic success is achieved, the binary label provides no gradient to distinguish efficient completions from slow ones. Second, real-world rollouts mix autonomous and intervention segments; naively assigning episode outcomes across these boundaries introduces incorrect credit assignment. To address these issues, we propose Hierarchical Advantage-Weighted Behavior Cloning (HABC), which trains separate critic heads for these two objectives on different data subsets and combines their outputs with a state-adaptive balance. A state-adaptive gate $g_t$ merges their one-step advantages, prioritizing viability when success is uncertain and shifting to efficiency only when viability is high, and converts the result into per-transition weights on the actor loss. Intervention-aware credit assignment further restricts outcome labels to segments executed by the current policy, preventing supervision from leaking across intervention boundaries. In real-robot experiments on three contact-rich bimanual tasks, HABC raises success from supervised fine-tuning (SFT) baselines of 36%, 44%, and 12% to 92%, 88%, and 38%.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1
^{2{\,\scalebox{0.75}{\Letter}}}

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 2
^{1,3{\,\scalebox{0.75}{\Letter}}}

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 3
^{{\scalebox{0.75}{\Letter}}}

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 4
g_{t}

* Equation: Not provided
* Symbols: g_{t}
* Why it matters: Represents the state-adaptive gate that merges the one-step advantages from the viability and efficiency heads.

### Equation 5
V_{v}

* Equation: Not provided
* Symbols: V_{v}
* Why it matters: Represents the viability value used to derive the scalar weight w_{i}.

### Equation 6
V_{e}

* Equation: Not provided
* Symbols: V_{e}
* Why it matters: Represents the efficiency value used to derive the scalar weight w_{i}.

### Equation 7
A_{v}

* Equation: Not provided
* Symbols: A_{v}
* Why it matters: Represents the one-step advantage from the viability head.

### Equation 8
A_{e}

* Equation: Not provided
* Symbols: A_{e}
* Why it matters: Represents the one-step advantage from the efficiency head.

**Method Summary**
================

* The proposed method, Hierarchical Advantage-Weighted Behavior Cloning (HABC), trains separate critic heads for viability and efficiency on different data subsets.
* The state-adaptive gate g_{t} merges the one-step advantages from the viability and efficiency heads to produce per-transition weights on the actor loss.
* The method uses a flow-matching VLA actor trained with a weighted flow-matching loss, which extracts viability and efficiency from sparse outcomes.
* The core design question is how to set the scalar weight w_{i} so that viability and efficiency are extracted from sparse outcomes and routed to the correct data.

**Experimental Overview**
=====================

* Tasks: The proposed method is evaluated on three real-robot dual-arm manipulation tasks: Pencil Pouch, Paper Bag, and Snack Bag.
* Baselines: The method is compared to supervised fine-tuning (SFT) and imit-DAgger baselines.
* Main claimed findings: The proposed method achieves the highest success rate on all three tasks and reduces trajectory length compared to the viability-only variant and imit-DAgger baseline.

**What to Verify in the PDF**
==========================

* The implementation details of the flow-matching VLA actor and the weighted flow-matching loss.
* The hyperparameter tuning process for the proposed method.
* The evaluation metrics used to measure success rate and trajectory length.
{% endraw %}

{% raw %}
## 2) The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers
- **Authors:** Alper Yıldırım
- **arXiv:** [2606.17037](https://arxiv.org/abs/2606.17037v1) · [pdf](https://arxiv.org/pdf/2606.17037v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.17037v1))
- **Categories:** cs.CV, cs.AI, cs.LG

### Abstract
> Oppenheim and Lim (1981) showed that natural images stay recognizable when reconstructed from their Fourier phase alone, while the magnitude carries little of their identity. We ask whether trained image classifiers reproduce this asymmetry inside their hidden layers, and we test it causally: given two images, we transplant the phase of one onto the magnitude of the other at a chosen layer and record which image the prediction follows. In PRISM2D, GFNet, and ViT-B/16 the prediction follows the phase or sign donor, and deleting all image-specific magnitude barely moves accuracy, so identity rides on phase while image-specific magnitude is largely dispensable to the readout. ResNet-50 at first seems to break the pattern, because transplanting sign after its ReLUs does nothing; a fair intervention before the ReLU reveals a strong latent sign code in the late blocks, and a DC-only control shows the readout consumes a channel-wise spatial average. Controls rule out the trivial case in which magnitude simply stops depending on the image. The architectures therefore share a phase/sign identity code but expose it in different bases, set by rectification and readout geometry, which gives a mechanistic account of the texture--shape gap between CNNs and attention models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `(x_{A},x_{B})`

* Equation: `(x_{A},x_{B})`
* Symbols: `x_{A}`, `x_{B}`
* Why it matters: This equation represents the input image pairs used for the experiment. The authors sample pairs of different classes and shuffle the validation set to create a fixed seed.

### Equation 2: `y_{A}\neq y_{B}`

* Equation: `y_{A}\neq y_{B}`
* Symbols: `y_{A}`, `y_{B}`
* Why it matters: This equation represents the condition for selecting image pairs for the experiment. Only pairs where the class labels are different are used.

### Equation 3: `h^{(\ell)}(x)`

* Equation: `h^{(\ell)}(x)`
* Symbols: `h^{(\ell)}`, `x`
* Why it matters: This equation represents the hidden layer output of the neural network. The authors transplant the phase of one image onto the magnitude of another at a chosen layer.

### Equation 4: `\ell`

* Equation: `\ell`
* Symbols: `\ell`
* Why it matters: This equation represents the layer number at which the phase transplantation is performed. The authors sweep the intervention layer to record how often the prediction follows the phase or sign donor.

### Equation 5: `\phi(h)`

* Equation: `\phi(h)`
* Symbols: `\phi`, `h`
* Why it matters: This equation represents the phase function applied to the hidden layer output. The authors use the phase function to transplant the phase of one image onto the magnitude of another.

**Method Summary**
================

* The authors evaluate four trained classifiers on the same protocol: PRISM2D, GFNet, ResNet-50, and ViT-B/16.
* The classifiers are trained on the ImageNet-100 dataset with 100 classes, 126,689 training images, and 5,000 validation images.
* The authors apply the phase transplantation intervention at inference only and record how often the prediction follows the phase or sign donor.
* The experiment is performed on four architecture families: complex, real spectral, convolutional, and attention.

**Experimental Overview**
=====================

* Tasks/Datasets: The authors evaluate four trained classifiers on the ImageNet-100 dataset.
* Baselines/Comparisons: The authors compare the performance of the four classifiers on the same protocol.
* Main Claimed Findings: The authors find that by the time of readout, the phase or sign of the features decides the class. The shared endpoint is the main finding of the experiment.

**What to Verify in the PDF**
==========================

* The authors mention that the forward pass runs in bfloat16 autocast, while every Fourier transform and phase operation is computed in single precision. Verify that this is indeed the case.
* The authors mention that the phase transplantation intervention is applied at inference only. Verify that this is the case and that the authors do not apply the intervention during training.
* The authors mention that the phase code is something the models build, not something inherited from the pixels. Verify that this is indeed the case and that the authors provide evidence for this claim.
{% endraw %}

{% raw %}
## 3) Your Privacy My Cloak: Backdoor Attacks on Differentially Private Federated Learning
- **Authors:** Xiaolin Li, Ning Wang, Ninghui Li, Wenhai Sun
- **arXiv:** [2606.17035](https://arxiv.org/abs/2606.17035v1) · [pdf](https://arxiv.org/pdf/2606.17035v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.17035v1))
- **Categories:** cs.LG, cs.CR

### Abstract
> Prior research suggests that differential privacy (DP) inherently enhances the robustness of federated learning (FL) against backdoor attacks. In this paper, we challenge this assumption. Through an empirical analysis of two baseline attack strategies, we uncover a fundamental tension in DP-FL: while bypassing DP allows state-of-the-art defenses to detect and filter malicious updates, complying with DP inadvertently masks their distinguishing statistical characteristics. Consequently, existing defenses become ineffective as DP reduces the raw backdoor signal. Building on this masking effect, we propose RING, a novel attack that explicitly exploits DP to conceal malicious contributions while maximizing attack impact. By collaboratively crafting adversarial perturbations, compromised clients reconstruct a strong backdoor signal during aggregation without triggering anomaly detection. RING operates as a perturbation layer that is agnostic to the underlying backdoor technique, making it broadly applicable and composable with existing attacks -- a property that significantly amplifies the threat it poses to DP-FL. Extensive evaluations across four image and text datasets under non-iid distributions show that RING achieves an average attack success rate of 90.3% against six state-of-the-art defenses under a moderate privacy budget, an improvement of up to 26.08x over baseline strategies. Finally, we evaluate potential countermeasures and find that mitigating this threat incurs significant utility trade-offs, exposing a fundamental security gap in the deployment of differentially private FL.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 90.3%
```latex
90.3\%
```
* Symbols: `%` (percent sign)
* Why it matters: This is the average attack success rate of Ring against six state-of-the-art defenses under a moderate privacy budget.

### Equation 2: 26.08 ×
```latex
26.08\times
```
* Symbols: `×` (multiplication symbol)
* Why it matters: This is the improvement in attack success rate of Ring over baseline strategies.

### Equation 3: ε = 1
```latex
\epsilon=1
```
* Symbols: `ε` (epsilon), `=`
* Why it matters: This represents the privacy budget used in the experiments.

### Equation 4: (ε, δ)
```latex
(\epsilon,\delta)
```
* Symbols: `ε` (epsilon), `δ` (delta)
* Why it matters: This represents the privacy budget and sensitivity parameter used in differential privacy.

### Equation 5: D1
```latex
D_{1}
```
* Symbols: `D1` (no specific meaning given in the context)
* Why it matters: This represents the aggregate noise error under varying `f` and subgroup configurations.

**Method Summary**
==================

* Ring is a novel attack that exploits differential privacy to conceal malicious contributions while maximizing attack impact.
* The attack operates as a perturbation layer that is agnostic to the underlying backdoor technique.
* Ring achieves an average attack success rate of 90.3% against six state-of-the-art defenses under a moderate privacy budget.

**Experimental Overview**
=========================

* Tasks/Datasets: Four image and text datasets (MNIST, CIFAR-10, CIFAR-100, Sentiment-140) with three non-iid data distributions (probability-based, non-iid, and iid).
* Baselines/Comparisons: DP-opt-in and DP-opt-out baselines, six state-of-the-art defenses.
* Main Claimed Findings: Ring substantially outperforms both DP-opt-in and DP-opt-out baselines in ASR and evades existing defenses in most cases.
{% endraw %}

{% raw %}
## 4) HAMON: Passive Optical Sequence Mixing for Long-Horizon Forecasting
- **Authors:** Alper Yıldırım
- **arXiv:** [2606.17028](https://arxiv.org/abs/2606.17028v1) · [pdf](https://arxiv.org/pdf/2606.17028v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.17028v1))
- **Categories:** cs.LG, cs.AI, cs.AR

### Abstract
> Simple linear and frequency-domain models remain surprisingly competitive in long-horizon time-series forecasting, and recent mechanistic evidence suggests that standard forecasting benchmarks may not require the dense superposed representations that make transformers powerful in other domains. This raises a substrate-level question: if the core forecasting operator is often low-complexity and approximately linear, does it need to be implemented as learned digital temporal mixing? We introduce HAMON, a passive diffractive optical forecasting core in which historical values are encoded onto an optical aperture, future positions are left dark, and cascaded trainable phase masks with free-space diffraction shape the forecast directly in the output field. At inference, prediction is performed by a single passive optical propagation pass with no trainable digital sequence-mixing layer. Across standard benchmarks, HAMON outperforms the strongest digital baselines considered on ETTm2 at all horizons and on ETTh2 at all but the longest horizon, improving MSE by up to 14\% and doing so consistently across horizons rather than at isolated points. It is competitive on Weather and trails the strongest baselines on the remaining ETT settings and on the high-channel-count Traffic and Electricity datasets. Phase encoding, intensity-compatible readout, and phase-scrambling ablations, together with a TorchOptics cross-simulator check, indicate that the forecasts arise from the data-bearing optical field rather than from a digital forecasting head. Because the passive core uses standard Fourier optics, HAMON defines a concrete target for optical hardware and for passive physical sequence mixing.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `x ∈ ℝ^{L × C}`

* Equation: `x ∈ ℝ^{L × C}`
* Symbols: `x`, `L`, `C`
* Why it matters: This equation represents the input data `x` as a matrix of shape `(L, C)`, where `L` is the number of time steps and `C` is the number of features.

### Equation 2: `y ∈ ℝ^{H × C}`

* Equation: `y ∈ ℝ^{H × C}`
* Symbols: `y`, `H`, `C`
* Why it matters: This equation represents the predicted output `y` as a matrix of shape `(H, C)`, where `H` is the number of future time steps and `C` is the number of features.

### Equation 3: `U_{0} ∈ ℂ^{G}`

* Equation: `U_{0} ∈ ℂ^{G}`
* Symbols: `U_{0}`, `G`
* Why it matters: This equation represents the initial optical aperture `U_{0}` as a complex-valued matrix of shape `(G, G)`, where `G` is the number of input aperture positions.

### Equation 4: `ℓ`

* Equation: `ℓ`
* Symbols: `ℓ`
* Why it matters: This equation represents the lookback length, which is not explicitly defined in the context. However, it is mentioned that the lookback length is used to determine the number of input aperture positions.

### Equation 5: `φ_{ℓ} ∈ ℝ^{G}`

* Equation: `φ_{ℓ} ∈ ℝ^{G}`
* Symbols: `φ_{ℓ}`, `G`
* Why it matters: This equation represents the phase mask `φ_{ℓ}` as a real-valued matrix of shape `(G,)`, where `G` is the number of input aperture positions. The phase mask is used to shape the forecast directly in the output field.

**Method Summary**
==================

* The HAMON model uses a passive optical sequence mixing approach to forecast future values.
* The input data `x` is encoded onto an optical aperture, and future positions are left dark.
* The cascaded trainable phase masks with free-space diffraction shape the forecast directly in the output field.
* The model uses reversible instance normalization (RevIN) to stabilize the input scale.

**Experimental Overview**
=========================

* Tasks/Datasets: The HAMON model is evaluated on the standard long-term forecasting protocol using prediction horizons `H ∈ {96, 192, 336, 720}`.
* Baselines/Comparisons: The model is compared against representative digital forecasting models using baseline MSE values reported by Xu et al. (2024).
* Main Claimed Findings: The HAMON model achieves competitive forecasting behavior when the sequence-mixing computation is moved into passive propagation.

**What to Verify in the PDF**
=============================

* The implementation details of the RevIN normalization layer.
* The mathematical derivation of the phase mask `φ_{ℓ}` and its effect on the forecast.
* The experimental results for the different prediction horizons and phase mask configurations.
{% endraw %}

{% raw %}
## 5) ExpRL: Exploratory RL for LLM Mid-Training
- **Authors:** Violet Xiang, Amrith Setlur, Chase Blagden, Nick Haber, Aviral Kumar
- **arXiv:** [2606.17024](https://arxiv.org/abs/2606.17024v1) · [pdf](https://arxiv.org/pdf/2606.17024v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.17024v1))
- **Categories:** cs.LG

### Abstract
> Sparse reward reinforcement learning (RL) has become a standard tool for improving LLM reasoning, but its success depends critically on the coverage present in the base model. In practice, models are often primed for RL through \emph{mid-training} on curated reasoning traces that teach useful primitive skills such as decomposition, verification, or self-correction. Although effective, this strategy requires manually specifying what the model should learn, and it remains unclear whether such primitive coverage is enough for much harder problems, which require combining these skills into broader solution strategies. We study a more automated approach: \emph{RL-based mid-training} using large corpora of human-written question-answer data. Rather than treating reference solutions as targets to imitate, our method, ExpRL, uses them as \emph{reward scaffolds}: references are hidden from the policy and used only to construct problem-specific grading rubrics for judging on-policy reasoning traces. The policy samples from the original problem prompt, while an LLM judge compares the sampled reasoning trace against the reference solution and assigns outcome-level or process-level dense rewards. This lets ExpRL reinforce partial progress, useful intermediate reductions, and productive reasoning behaviors that sparse final-answer rewards often fail to upweight. On challenging math reasoning tasks, ExpRL yields stronger RL priming than SFT, sparse-reward GRPO, and self-distillation, and provides a better initialization for subsequent sparse-reward RL. Additional mixed-domain experiments further suggest that ExpRL can extend beyond the original math-only setting.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{D}_{\text{mid}}=\{(\mathbf{x}_{i},\mathbf{y}_{i}^{\star})\}_{i=1}^{N}$

* Equation: $\mathcal{D}_{\text{mid}}$
* Symbols: $\mathcal{D}_{\text{mid}}$ (dataset for mid-training), $\mathbf{x}_{i}$ (input prompts), $\mathbf{y}_{i}^{\star}$ (reference solutions)
* Why it matters: This equation represents the dataset used for mid-training, which consists of input prompts and their corresponding reference solutions.

### Equation 2: $\mathbf{x}_{i}$

* Equation: $\mathbf{x}_{i}$
* Symbols: $\mathbf{x}_{i}$ (input prompts)
* Why it matters: This equation represents the input prompts used for mid-training.

### Equation 3: $\mathbf{y}_{i}^{\star}$

* Equation: $\mathbf{y}_{i}^{\star}$
* Symbols: $\mathbf{y}_{i}^{\star}$ (reference solutions)
* Why it matters: This equation represents the reference solutions used for mid-training.

### Equation 4: $\pi_{\theta}$

* Equation: $\pi_{\theta}$
* Symbols: $\pi_{\theta}$ (policy)
* Why it matters: This equation represents the policy used for mid-training.

### Equation 5: $\theta$

* Equation: $\theta$
* Symbols: $\theta$ (model parameters)
* Why it matters: This equation represents the model parameters used for mid-training.

**Method Summary**
==================

* The authors propose a new method called ExpRL, which uses large corpora of human-written question-answer data to automate the mid-training process for reinforcement learning (RL) models.
* ExpRL uses a policy to sample from the input prompts, and an LLM judge to compare the sampled reasoning traces against the reference solutions and assign outcome-level or process-level dense rewards.
* The authors evaluate ExpRL on challenging math reasoning tasks and compare it to alternative mid-training procedures, including sparse-reward RL and self-distillation.

**Experimental Overview**
========================

* Tasks/Datasets: The authors evaluate ExpRL on challenging math reasoning tasks using a dataset of hard question and reference answer pairs from recent works.
* Baselines/Comparisons: The authors compare ExpRL to alternative mid-training procedures, including sparse-reward RL and self-distillation.
* Main Claimed Findings: ExpRL yields stronger RL priming than SFT, sparse-reward GRPO, and self-distillation, and provides a better initialization for subsequent sparse-reward RL.

**What to Verify in the PDF**
=============================

* The authors mention that ExpRL can also work when a smaller reference-conditioned judge provides rewards for a larger policy. Verify the details of this experiment in the PDF.
* The authors also mention that ExpRL can extend beyond the original math-only setting. Verify the results of the mixed-domain experiments in the PDF.
* The authors use a dataset combining hard question and reference answer pairs from recent works. Verify the details of the dataset and the data preprocessing steps in the PDF.
{% endraw %}
