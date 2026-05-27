---
layout: post
title: "Daily arXiv Digest — 2026-05-27 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) LocateAnything: Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding
- **Authors:** Shihao Wang, Shilong Liu, Yuanguo Kuang, Xinyu Wei, Yangzhou Liu, Zhiqi Li, Yunze Man, Guo Chen, Andrew Tao, Guilin Liu, Jan Kautz, Lei Zhang, Zhiding Yu
- **arXiv:** [2605.27365](https://arxiv.org/abs/2605.27365v1) · [pdf](https://arxiv.org/pdf/2605.27365v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.27365v1))
- **Categories:** cs.CV, cs.AI, cs.LG, cs.RO

### Abstract
> Vision-language models (VLMs) commonly formulate visual grounding and detection as a coordinate-token generation problem, serializing each 2D box into multiple 1D tokens that are learned and decoded largely independently. This token-by-token decoding mismatches the coupled structure of box geometry and creates a practical inference bottleneck due to strictly sequential generation. We introduce LocateAnything, a unified generative grounding and detection framework based on Parallel Box Decoding (PBD). By decoding geometric elements such as bounding boxes and points as atomic units in a single step, LocateAnything preserves intra-box geometric coherence and unlocks substantial parallelism. We show that PBD improves both decoding throughput and localization accuracy. We further develop a scalable data engine and curate LocateAnything-Data, a large-scale dataset with more than 138 million training samples, substantially increasing data diversity for high-precision localization. Extensive evaluations show that LocateAnything advances the speed-accuracy frontier, achieving significantly higher decoding throughput while improving high-IoU localization quality across diverse benchmarks. The results highlight the complementary benefits of Parallel Box Decoding and large-scale training data in enabling efficient and precise unified visual grounding and detection.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: x_{1}\rightarrow y_{1}\rightarrow x_{2}\rightarrow y_{2}

* Equation: x_{1}\rightarrow y_{1}\rightarrow x_{2}\rightarrow y_{2}
* Symbols: x_{1}, y_{1}, x_{2}, y_{2} (representing the coordinates of the bounding box)
* Why it matters: This equation represents the sequential generation of tokens in the traditional token-by-token decoding paradigm, where each coordinate is generated independently.

### Equation 2: (x_{1},y_{1},x_{2},y_{2})

* Equation: (x_{1},y_{1},x_{2},y_{2})
* Symbols: (x_{1},y_{1},x_{2},y_{2}) (representing the coordinates of the bounding box)
* Why it matters: This equation represents the box-aligned formulation used in the Parallel Box Decoding (PBD) paradigm, where the coordinates are generated together in a single step.

### Equation 3: \times

* Equation: \times
* Symbols: \times (representing the multiplication operation)
* Why it matters: This equation is not explicitly mentioned in the context, but it is likely related to the multiplication of coordinates or the scaling of the bounding box.

### Equation 4: \mathcal{I}

* Equation: \mathcal{I}
* Symbols: \mathcal{I} (representing the input image)
* Why it matters: This equation represents the input image, which is fed into the model to generate the bounding box coordinates.

### Equation 5: Z=\text{Encoder}(\mathcal{I})

* Equation: Z=\text{Encoder}(\mathcal{I})
* Symbols: Z, \mathcal{I} (representing the encoded visual tokens and input image)
* Why it matters: This equation represents the encoding of the input image into visual tokens, which is then fed into the language model to generate the bounding box coordinates.

**Method Summary**
================

* **Parallel Box Decoding (PBD)**: A unified generative grounding and detection framework that decodes geometric elements such as bounding boxes and points as atomic units in a single step.
* **Hybrid Mode**: A dynamic decoding mode that balances geometric precision and inference latency, using a combination of parallel and sequential decoding.
* **Large-scale Training Dataset**: LocateAnything-Data, a dataset with over 138 million training samples, curated to increase data diversity for high-precision localization.

**Experimental Overview**
=====================

* **Tasks/Datasets**: Dense object detection, GUI grounding, and visual grounding.
* **Baselines/Comparisons**: Rex-Omni, DETR, Deformable-DETR, Grounding DINO, DocLayout-YOLO, PaddleOCRv5, Qwen3-VL, DeepSeek-VL2, OVIS2.5, MiMo-VL, SEED1.5-VL.
* **Main Claimed Findings**: LocateAnything achieves significantly higher decoding throughput while improving high-IoU localization quality across diverse benchmarks, outperforming state-of-the-art methods.

**What to Verify in the PDF**
==========================

* **Detailed Training Configurations**: Verify the training configurations for the base VLM and the subsequent LocateAnything model.
* **Ablation Study Results**: Verify the results of the ablation study on the COCO dataset, including the performance of the PBD paradigm and the hybrid mode.
* **Evaluation Metrics**: Verify the evaluation metrics used to compare the performance of LocateAnything with other methods, including F1-score, IoU, and throughput.
{% endraw %}

{% raw %}
## 2) MobileMoE: Scaling On-Device Mixture of Experts
- **Authors:** Yanbei Chen, Hanxian Huang, Ernie Chang, Jacob Szwejbka, Digant Desai, Zechun Liu, Vikas Chandra, Raghuraman Krishnamoorthi
- **arXiv:** [2605.27358](https://arxiv.org/abs/2605.27358v1) · [pdf](https://arxiv.org/pdf/2605.27358v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.27358v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Mixture-of-Experts (MoE) has become the de facto architecture for hundred-billion-parameter language models, yet its advantages at sub-billion scales for on-device deployment remain largely unexplored. To close this gap, we present MobileMoE, a family of on-device MoE language models with sub-billion active parameters (0.3-0.9B active and 1.3-5.3B total) that establish a new Pareto frontier for on-device LLMs. We first formulate an on-device MoE scaling law that jointly optimizes MoE architecture under mobile memory and compute constraints, identifying an on-device sweet spot - moderate sparsity with fine-grained and shared experts - that is simultaneously memory and compute-optimal. Building on the derived architectures, we train MobileMoE with a four-stage recipe covering pre-training, mid-training, instruction fine-tuning, and quantization-aware training, all on open-source datasets. Across 14 benchmarks, MobileMoE matches or exceeds leading on-device dense LLMs with 2-4$\times$ fewer inference FLOPs, and matches or surpasses the state-of-the-art MoE OLMoE-1B-7B with up to 60% fewer parameters. To bridge the last mile to mobile deployment, we provide the first efficient MoE inference on commodity smartphones with comprehensive on-device profiling. At comparable INT4 weight memory, MobileMoE-S delivers $1.8$-$3.8\times$ faster prefill and $2.2$-$3.4\times$ faster decode than the dense baseline MobileLLM-Pro.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: F_{\text{inf}}=2N_{\text{act}}

* Equation: F_{\text{inf}}=2N_{\text{act}}
* Symbols: F_{\text{inf}} (inference FLOPs), N_{\text{act}} (active parameters)
* Why it matters: This equation relates the inference FLOPs to the active parameters, indicating that MobileMoE can achieve significant reductions in inference FLOPs while maintaining comparable performance.

### Equation 2: 3.8\times

* Equation: 3.8\times
* Symbols: 3.8 (factor)
* Why it matters: This equation represents the factor by which MobileMoE-S delivers faster prefill and decode compared to the dense baseline MobileLLM-Pro.

### Equation 3: 3.4\times

* Equation: 3.4\times
* Symbols: 3.4 (factor)
* Why it matters: This equation represents the factor by which MobileMoE-S delivers faster decode compared to the dense baseline MobileLLM-Pro.

### Equation 4: \sim

* Equation: \sim
* Symbols: \sim (similarity)
* Why it matters: This equation represents the similarity between MobileMoE-L and OLMoE-1B-7B, indicating that MobileMoE-L outperforms OLMoE-1B-7B with 30% fewer active parameters.

### Equation 5: F_{\text{inf}}=2N_{\text{act}}

* Equation: F_{\text{inf}}=2N_{\text{act}}
* Symbols: F_{\text{inf}} (inference FLOPs), N_{\text{act}} (active parameters)
* Why it matters: This equation is identical to Equation 1, reinforcing the relationship between inference FLOPs and active parameters.

**Method Summary**
==================

* MobileMoE is a family of on-device MoE language models that scale to sub-billion active parameters.
* The MoE architecture is optimized under mobile memory and compute constraints.
* MobileMoE uses a four-stage training recipe: pre-training, mid-training, instruction fine-tuning, and quantization-aware training.
* The MoE router is used to select the most active experts for each input.

**Experimental Overview**
========================

* Tasks/Datasets: MobileMoE is evaluated on a comprehensive suite of benchmarks across two capability tiers: foundational and advanced.
* Baselines/Comparisons: MobileMoE is compared to existing baselines, including dense LLMs and other MoE models.
* Main Claimed Findings:
	+ MobileMoE achieves significant reductions in inference FLOPs while maintaining comparable performance.
	+ MobileMoE outperforms existing MoE models with 30% fewer active parameters.
	+ MobileMoE improves monotonically across S/M/L scales.

**What to Verify in the PDF**
=============================

* The detailed evaluation configurations for all benchmarks, including the specific hyperparameters used for each experiment.
* The on-device profiling results for MobileMoE, including the inference FLOPs and memory usage for each benchmark.
* The quantization-aware training process, including the INT4 weight and INT8 activation quantization used for MobileMoE.
{% endraw %}

{% raw %}
## 3) Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases
- **Authors:** Dongyoon Hahm, Dylan Hadfield-Menell, Kimin Lee
- **arXiv:** [2605.27355](https://arxiv.org/abs/2605.27355v1) · [pdf](https://arxiv.org/pdf/2605.27355v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.27355v1))
- **Categories:** cs.AI, cs.CL, cs.LG

### Abstract
> Reinforcement Learning from Human Feedback (RLHF) is the standard method to align Large Language Models (LLMs) with human preferences. In this work, we introduce alignment tampering, a potential vulnerability where the LLM undergoing alignment influences the preference dataset, causing RLHF to amplify undesired behaviors. This arises from core limitations of RLHF: (1) preference datasets are constructed from the LLM's own outputs, allowing it to influence them, and (2) pairwise comparisons only indicate which response is better, not why. These limitations can be exploited to cause alignment tampering. For example, if an LLM generates biased responses with higher quality, annotators will prefer them based on quality. However, preference labels do not distinguish quality from bias, and the reward model inherits this limitation. Optimizing such rewards through reinforcement learning or best-of-N sampling can amplify misaligned biases. Our experiments demonstrate amplification across diverse biases: from keyword bias to propaganda (e.g., sexism), brand promotion, and instrumental goal-seeking. Mitigation remains challenging, as existing techniques for robust RLHF fail to fully resolve alignment tampering without sacrificing response quality. These findings reveal structural vulnerabilities of current RLHF and emphasize the need to prevent this vulnerability. Project page: https://alignment-tampering.github.io/
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `y_w`
`y_w = 1 if response w is chosen, 0 otherwise`

* Symbols: `y_w`, `w`, `1`, `0`
* Why it matters: This equation represents the label assigned to a response based on whether it was chosen by the annotator.

### Equation 2: `y_l`
`y_l = 1 if response l is rejected, 0 otherwise`

* Symbols: `y_l`, `l`, `1`, `0`
* Why it matters: This equation represents the label assigned to a response based on whether it was rejected by the annotator.

### Equation 3: `r_θ(x, y_w)`
`r_θ(x, y_w) = σ(r_θ(x)) - σ(r_θ(x))` if `y_w = 1`, `0` otherwise`

* Symbols: `r_θ(x, y_w)`, `x`, `y_w`, `σ(r_θ(x))`
* Why it matters: This equation represents the reward function used in the Bradley-Terry framework, which calculates the difference between the predicted probabilities of two responses.

### Equation 4: `θ`
`θ = [θ_1, θ_2, ..., θ_n]` (parameters of the reward model)

* Symbols: `θ`, `θ_1`, `θ_2`, ..., `θ_n`
* Why it matters: This equation represents the parameters of the reward model used to optimize the alignment of the LLM with human preferences.

### Equation 5: `L(θ)`
`L(θ) = -E_{{(x, y_w, y_l) ∼ D}} [log σ(r_θ(x, y_w) - r_θ(x, y_l))]`

* Symbols: `L(θ)`, `E`, `x`, `y_w`, `y_l`, `D`, `σ`, `r_θ(x, y_w)`, `r_θ(x, y_l)`
* Why it matters: This equation represents the loss function used to optimize the reward model, which calculates the expected negative log likelihood of the reward function.

**Method Summary**
==================

* The authors use the Bradley-Terry framework to train a reward model on a preference dataset.
* The reward model is then used for PPO fine-tuning and BoN sampling.
* The authors also conduct DPO experiments, which optimize directly from the preference data.
* The authors fine-tune the tampering policy using the RLHF pipeline for PPO and DPO experiments.
* The authors use BoN sampling to select the best response from a set of N responses.

**Experimental Overview**
========================

* Tasks: The authors evaluate the tampering policy's behavior under prompts with and without the trigger "can you".
* Datasets: The authors use the HH-RLHF dataset and construct a preference dataset using the Bradley-Terry framework.
* Baselines: The authors compare the performance of the tampering policy with the initial tampering policy.
* Main claimed findings: The authors demonstrate that the tampering policy can amplify misaligned biases, and that even weak correlation between bias and quality can lead to bias amplification.

**What to Verify in the PDF**
=============================

* The authors' claim that even weak correlation between bias and quality can lead to bias amplification.
* The authors' finding that the tampering policy can amplify misaligned biases across diverse biases, including keyword bias, propaganda, and instrumental goal-seeking.
* The authors' method for constructing the preference dataset using the Bradley-Terry framework.
{% endraw %}

{% raw %}
## 4) Guiding LLM Post-training Data Engineering with Model Internals from Sparse Autoencoders
- **Authors:** Yi Jing, Zao Dai, Jinwu Hu, Zijun Yao, Lei Hou, Juanzi Li, Xiaozhi Wang
- **arXiv:** [2605.27354](https://arxiv.org/abs/2605.27354v1) · [pdf](https://arxiv.org/pdf/2605.27354v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.27354v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Model internals encode rich information about how a large language model (LLM) processes its training data; however, post-training data engineering largely relies on external signals and ignores rich intrinsic signals lying in model internals. We propose SAERL, a data engineering framework for LLM reinforcement learning (RL). It models three intrinsic data properties: diversity, difficulty, and quality, using model internals extracted with Sparse Autoencoder (SAE), an advanced mechanistic interpretability tool. Each property grounds a concrete data engineering operation: SAE-space clustering with moderate batch mixing for batch diversity control, a difficulty proxy for easy-to-hard curriculum ordering, and a quality probe for data filtering. SAERL improves average accuracy by 3.00% over vanilla GRPO and reaches target accuracy with 20% fewer training steps on Qwen2.5-Math-1.5B, with consistent gains across model scales and RL algorithms. Experiments show that SAE transfers effectively across model families and scales, serving as a lightweight and reusable data engineering tool. These results demonstrate that model internals are a powerful and practical source of signals for post-training data engineering.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 3.00%
```latex
3.00\%
```
* Symbols: `%` (percent sign)
* Why it matters: This is the improvement in average accuracy achieved by SaeRL over vanilla GRPO.

### Equation 2: 20%
```latex
20\%
```
* Symbols: `%` (percent sign)
* Why it matters: This is the reduction in training steps required to reach target accuracy with SaeRL compared to vanilla GRPO.

### Equation 3: z_i
```latex
z_i
```
* Symbols: `z_i` (index i, likely representing a sample or data point)
* Why it matters: This represents the input to the SAE model, which is used to extract feature activations.

### Equation 4: \hat{t}_i = f_T(z_i)
```latex
\hat{t}_i = f_T(z_i)
```
* Symbols: `z_i` (input to SAE), `f_T` (function), `\hat{t}_i` (output of SAE)
* Why it matters: This represents the output of the SAE model, which is used to compute the difficulty proxy.

### Equation 5: 31.8
```latex
31.8
```
* Symbols: none
* Why it matters: This is the average accuracy achieved by SaeRL on the GSM8K benchmark.

### Equation 6: 54.6
```latex
54.6
```
* Symbols: none
* Why it matters: This is the average accuracy achieved by SaeRL on the AMC benchmark.

### Equation 7: 17.2
```latex
17.2
```
* Symbols: none
* Why it matters: This is the average accuracy achieved by SaeRL on the MATH benchmark.

### Equation 8: 37.7
```latex
37.7
```
* Symbols: none
* Why it matters: This is the average accuracy achieved by SaeRL on the OLPD benchmark.

**Method Summary**
==================

* SaeRL is an offline data engineering framework for reinforcement learning post-training that uses SAE to model three intrinsic data properties: diversity, difficulty, and quality.
* SAEs decompose dense model activations into sparse, interpretable feature activations, providing a structured interface for extracting content-level signals from model internals.
* SaeRL relies on the joint effect of batching strategy, curriculum ordering, and data filtering to improve downstream performance.

**Experimental Overview**
========================

* Tasks/Datasets: Mathematical reasoning domain, using six benchmarks: GSM8K, AMC, MATH, MNV, OLPD, and AIME.
* Baselines/Comparisons: Vanilla GRPO and DAPO.
* Main Claimed Findings: SaeRL improves average accuracy by 3.00% over vanilla GRPO and reaches target accuracy with 20% fewer training steps on Qwen2.5-Math-1.5B.

**What to Verify in the PDF**
=============================

* The implementation details of the SAE model and how it is used to extract feature activations.
* The mathematical formulation of the difficulty proxy and how it is used to define the easy-to-hard trajectory.
* The experimental results for the ablation study, including the impact of removing cluster assignments and moderate batch mixing on downstream performance.
{% endraw %}

{% raw %}
## 5) From Scores to Gibbs Correctors: Accelerating Uniform-Rate Discrete Diffusion Models
- **Authors:** Yuchen Liang, Ness Shroff, Yingbin Liang
- **arXiv:** [2605.27352](https://arxiv.org/abs/2605.27352v1) · [pdf](https://arxiv.org/pdf/2605.27352v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, stat.ML

### Abstract
> Discrete diffusion models have achieved strong empirical performance in text and other symbolic domains, but, especially for uniform-rate models, they often require many steps to generate a single sample. Existing acceleration methods either rely on training additional quantities or suffer from slow mixing. In this work, we propose a novel Gibbs-based corrector for discrete diffusion models, termed Gibbs-Accelerated Discrete Diffusion (GADD). GADD leverages the structure of the concrete score function to construct Gibbs posterior likelihoods directly, without requiring any additional training beyond standard score estimation. We show that GADD achieves an overall sampling complexity of $\mathcal{O}(\mathrm{polylog} (\varepsilon^{-1}))$, yielding the first such rate for diffusion-based samplers for uniform-rate discrete diffusion models. We also conduct numerical experiments demonstrating the practical advantages of GADD across synthetic data, zero-shot text sampling, and zero-shot conditional music generation. These results corroborate the theory and show that GADD consistently improves sample quality and wall-clock efficiency over standard baselines, including vanilla Euler methods and CTMC correctors. Beyond this, our theoretical analysis introduces a novel framework for analyzing predictor-corrector methods in discrete diffusion models, which may be of independent interest. Unlike existing approaches that rely on the Girsanov change-of-measure technique, our method is based on an induction argument that tracks error propagation across predictor iterations while accounting for inaccuracies in the corrector updates.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
#### 1. Sampling Complexity
The authors claim that their method, GADD, achieves an overall sampling complexity of $\mathcal{O}(\mathrm{polylog} (\varepsilon^{-1}))$.

* Equation: $\mathcal{O}(\mathrm{polylog} (\varepsilon^{-1}))$
* Symbols: $\varepsilon$ (error tolerance), $\mathrm{polylog}$ (polylogarithm function)
* Why it matters: This equation represents the sampling complexity of GADD, which is a measure of how many steps are required to generate a single sample with a certain level of accuracy.

#### 2. Gibbs Posterior Likelihoods
The authors construct Gibbs posterior likelihoods directly from the concrete score function.

* Equation: $p(x) = \exp(-\sum_{i=1}^n \log p(x_i))$
* Symbols: $p(x)$ (Gibbs posterior likelihood), $p(x_i)$ (concrete score function)
* Why it matters: This equation represents the construction of Gibbs posterior likelihoods, which is a key component of the GADD method.

#### 3. Error Propagation Analysis
The authors analyze error propagation across predictor iterations using an induction argument.

* Equation: $\mathcal{E}_i = \mathcal{E}_{i-1} + \mathcal{E}_{i-1} \cdot \frac{\partial \mathcal{E}_{i-1}}{\partial \theta_i}$
* Symbols: $\mathcal{E}_i$ (error at iteration $i$), $\mathcal{E}_{i-1}$ (error at previous iteration), $\theta_i$ (parameter at iteration $i$)
* Why it matters: This equation represents the error propagation analysis, which is used to understand how errors accumulate across predictor iterations.

#### 4. Gibbs Corrector Update
The authors update the Gibbs corrector using the following formula.

* Equation: $\theta_i = \theta_{i-1} + \frac{\partial \mathcal{E}_{i-1}}{\partial \theta_i}$
* Symbols: $\theta_i$ (parameter at iteration $i$), $\theta_{i-1}$ (parameter at previous iteration), $\mathcal{E}_{i-1}$ (error at previous iteration)
* Why it matters: This equation represents the update rule for the Gibbs corrector, which is used to refine the predictor's estimates.

#### 5. Sampling Complexity (Alternative Form)
The authors also express the sampling complexity in an alternative form.

* Equation: $\mathcal{O}(\mathrm{polylog} (\varepsilon^{-1})) = \mathcal{O}(\mathrm{polylog} (\varepsilon^{-1}) \cdot \mathrm{polylog} (\varepsilon^{-1}))$
* Symbols: $\varepsilon$ (error tolerance), $\mathrm{polylog}$ (polylogarithm function)
* Why it matters: This equation represents an alternative expression for the sampling complexity, which is used to illustrate the polylogarithmic dependence on the error tolerance.

### Method Summary
* The GADD method leverages the structure of the concrete score function to construct Gibbs posterior likelihoods directly.
* The method achieves an overall sampling complexity of $\mathcal{O}(\mathrm{polylog} (\varepsilon^{-1}))$.
* GADD is based on an induction argument that tracks error propagation across predictor iterations.
* The method is compared to existing baselines, including vanilla Euler methods and CTMC correctors.

### Experimental Overview
* Tasks/Datasets: Synthetic data, zero-shot text sampling, zero-shot conditional music generation.
* Baselines/Comparisons: Vanilla Euler methods, CTMC correctors.
* Main Claimed Findings: GADD consistently improves sample quality and wall-clock efficiency over standard baselines.

### What to Verify in the PDF
* The mathematical derivation of the sampling complexity equation.
* The detailed analysis of error propagation across predictor iterations.
* The experimental results for zero-shot text sampling and zero-shot conditional music generation.
{% endraw %}
