---
layout: post
title: "Daily arXiv Digest — 2026-07-03 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates
- **Authors:** Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah, Shahriar Noroozizadeh
- **arXiv:** [2607.02507](https://arxiv.org/abs/2607.02507v1) · [pdf](https://arxiv.org/pdf/2607.02507v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.02507v1))
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA

### Abstract
> LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR responses that are recorded but never shown to the other participant. Across 10 models, 3 scenarios, and 5 variations within each scenario, alignment-inducing settings produce systematic public-OTR divergence in the targeted agent, with its decision divergence rising from a $\sim$3% baseline to roughly 40%. The effect is consistent across four aggregate analyses: stance, semantic similarity, natural language inference, and survey responses. In some cases, the OTR response explicitly attributes public accommodation to relational pressures, such as career risk or sponsorship obligation. The findings suggest that agent evaluation should extend beyond explicit goals and detect emergent objectives. We present a dual-channel evaluation framework and complementary behavioral measures that operationalize this assessment.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

Here's a walkthrough of up to 5 equations from the extracted context:

### Equation 1: 
\[
\sim
\]

* Symbols: `\sim` (tilde)
* Why it matters: This equation is not explicitly defined in the context, but it seems to represent a placeholder or a dummy variable.

### Equation 2: 
\[
\dagger
\]

* Symbols: `\dagger` (dagger)
* Why it matters: Similar to Equation 1, this equation is not explicitly defined in the context. It may represent another placeholder or dummy variable.

### Equation 3: 
\[
\alpha
\]

* Symbols: `\alpha`
* Why it matters: This equation represents a variable or parameter, possibly related to the agent's decision-making process or objective function.

### Equation 4: 
\[
i_{t}=\alpha
\]

* Symbols: `i_t`, `\alpha`
* Why it matters: This equation defines a relationship between the agent's internal state `i_t` and the parameter `\alpha`. It may represent a simple update rule or a mapping between the two.

### Equation 5: 
\[
h_{t}
\]

* Symbols: `h_t`
* Why it matters: This equation represents a variable or function that depends on the agent's internal state `i_t` and possibly other inputs. It may be related to the agent's public or private history.

**Method Summary**
==================

Here's a summary of the method in 5 bullets:

* The authors introduce a dual-channel debate framework, where agents produce public utterances and private responses (OTR) that are recorded but not shown to the other participant.
* The authors use a range of models, including Persona-Reinforcing, Historical Alignment-Inducing, and Baseline Alignment-Inducing, to study the effect of social structure on agent behavior.
* The authors use a variety of evaluation metrics, including stance divergence, semantic similarity, natural language inference, and survey responses, to assess the agents' behavior.
* The authors use a range of scenarios, including climate endorsement and faculty manuscript submission, to study the effect of social structure on agent behavior in different contexts.
* The authors use a range of models, including GPT-5.4, Gemini 3.1 Pro, and GLM-5, to study the effect of social structure on agent behavior and to compare the performance of different models.

**Experimental Overview**
=========================

Here's an overview of the experimental setup:

* **Tasks/Datasets**: The authors use a range of scenarios, including climate endorsement and faculty manuscript submission, to study the effect of social structure on agent behavior.
* **Baselines/Comparisons**: The authors compare the performance of different models, including Persona-Reinforcing, Historical Alignment-Inducing, and Baseline Alignment-Inducing, to study the effect of social structure on agent behavior.
* **Main Claimed Findings**: The authors claim that social structure can lead to significant changes in agent behavior, including public-OTR divergence, and that this effect is not limited to specific models or scenarios.

**What to Verify in the PDF**
=============================

Here are 2 to 4 bullets on details that still need the full paper:

* **Additional Formalism and Method Details**: The authors mention that the formalism in Sec. 2 is intended as a minimal output-level notation rather than a claim of novelty over existing models of interaction. However, the full paper may provide more details on the formalism and method used.
* **Case Study Results**: The authors present several case studies to illustrate the effect of social structure on agent behavior. However, the full paper may provide more detailed results and analysis of these case studies.
* **Discussion and Implications**: The authors mention that the findings have implications for the evaluation of agent behavior and the design of socially structured settings. However, the full paper may provide more detailed discussion and implications of the results.
{% endraw %}

{% raw %}
## 2) DemoPSD: Disagreement-Modulated Policy Self-Distillation
- **Authors:** Yunhe Li, Hao Shi, Wenhao Liu, Mengzhe Ruan, Hanxu Hou, Zhongxiang Dai, Shuang Qiu, Linqi Song
- **arXiv:** [2607.02502](https://arxiv.org/abs/2607.02502v1) · [pdf](https://arxiv.org/pdf/2607.02502v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.02502v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> On-policy self-distillation (OPSD) has emerged as a practical method for training large language models (LLMs) to reason, where a single model acts as both the teacher and the student with different levels of information access. However, recent studies have found that the teacher's dense token-level supervision, conditioned on privileged information, can lead to overfitting to in-domain patterns, suppress exploration, and hurt cross-domain generalization, while also introducing a more fundamental issue: *privileged information leakage*, where the student encodes answer-dependent shortcuts that are unavailable at test time. We introduce **DemoPSD**, a novel framework that resolves such problems through the idea of *selective adoption of teacher guidance*. Instead of fitting the full teacher distribution, DemoPSD steers the student toward a *reverse-KL barycenter target*, a weighted geometric combination of the teacher and student distributions, that naturally balances learning from the teacher with preserving the student's own reasoning capacity. We measure the difference between their distributions and use such a discrepancy to adaptively control the blending at each token position. We provably show that DemoPSD achieves **(1)** *leakage attenuation*, i.e., effective mitigation of privileged information leakage; and **(2)** *exploration preservation*, i.e., preservation of exploration capacity under dense token-level distillation. Extensive experiments on SciKnowEval across four scientific fields show that DemoPSD outperforms both GRPO and SDPO while maintaining higher training entropy and robustly generalizing to out-of-distribution GPQA benchmarks.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: y^{*}

y^{*} = π_{\text{teacher}}(y \mid x, y_{<t}) \cdot \frac{1}{Z_{\text{teacher}}(x, y_{<t})} \cdot \pi_{\text{student}}(y \mid x, y_{<t})

Symbols:
- y^{*} : target output
- π_{\text{teacher}} : teacher's output distribution
- π_{\text{student}} : student's output distribution
- x : input
- y_{<t} : context up to time t
- Z_{\text{teacher}} : teacher's partition function

Why it matters: This equation represents the teacher's output distribution, which is used as a target for the student to learn from.

### Equation 2: I(y_{t};y^{*}\mid x,y_{<t})>0

I(y_{t};y^{*}\mid x,y_{<t}) > 0

Symbols:
- I(y_{t};y^{*}\mid x,y_{<t}) : mutual information between y_{t} and y^{*} given x and y_{<t}
- y_{t} : token at time t
- y^{*} : target output
- x : input
- y_{<t} : context up to time t

Why it matters: This inequality ensures that the mutual information between the token and the target output is greater than zero, indicating that the token is informative about the target output.

### Equation 3: y_{<t}

y_{<t} = \prod_{t=1}^{T} y_{t}

Symbols:
- y_{<t} : context up to time t
- y_{t} : token at time t
- T : total number of tokens

Why it matters: This equation represents the context up to time t, which is used to compute the teacher's output distribution.

### Equation 4: y_{t}

y_{t} = \pi_{\text{teacher}}(y \mid x, y_{<t})

Symbols:
- y_{t} : token at time t
- π_{\text{teacher}} : teacher's output distribution
- x : input
- y_{<t} : context up to time t

Why it matters: This equation represents the teacher's output distribution for the token at time t.

### Equation 5: \displaystyle\begin{aligned} \pi_{t}^{\text{target}}(v\mid x,y^{*},\hat{y}_{<t})&\propto\big(\pi_{\text{teacher}}(v\mid x,y^{*},\hat{y}_{<t})\big)^{1-\alpha_{t}}\cdot\big(\pi_{\text{student}}(v\mid x,\hat{y}_{<t})\big)^{\alpha_{t}},\end{aligned}

Symbols:
- π_{t}^{\text{target}} : target output distribution at time t
- v : token
- x : input
- y^{*} : target output
- \hat{y}_{<t} : context up to time t
- π_{\text{teacher}} : teacher's output distribution
- π_{\text{student}} : student's output distribution
- α_{t} : blending parameter

Why it matters: This equation represents the target output distribution at time t, which is a weighted combination of the teacher's and student's output distributions.

**Method Summary**
==================

* DemoPSD is a novel framework that resolves the problems of overfitting, exploration suppression, and privileged information leakage in on-policy self-distillation.
* The framework selectively adopts the teacher's guidance when the distributions remain reasonably consistent, and relies more on its own reasoning when the distributions substantially diverge.
* The key ingredient of DemoPSD is measuring the disagreement between the teacher's and student's predictions at each token position.
* The framework uses a reverse-KL barycenter target to balance learning from the teacher with preserving the student's own reasoning capacity.

**Experimental Overview**
========================

* Tasks/Datasets: Scientific reasoning benchmarks, including SciKnowEval across four scientific fields (biology, chemistry, material science, and physics).
* Baselines/Comparisons: SDPO and GRPO.
* Main Claimed Findings:
	+ DemoPSD outperforms SDPO and GRPO in terms of in-domain accuracy, training entropy, and out-of-distribution generalization.
	+ DemoPSD preserves exploration entropy and reduces privileged information leakage.

**What to Verify in the PDF**
=============================

* The derivation of the reverse-KL barycenter target and its loss and gradient.
* The experimental results for the base model, training data, and training setup.
* The theoretical analysis of DemoPSD's leakage attenuation and exploration preservation properties.
{% endraw %}

{% raw %}
## 3) Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials
- **Authors:** Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng, Laura Zichi, Chuin Wei Tan, Marc L. Descoteaux, Boris Kozinsky
- **arXiv:** [2607.02499](https://arxiv.org/abs/2607.02499v1) · [pdf](https://arxiv.org/pdf/2607.02499v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.02499v1))
- **Categories:** cs.LG, cs.AI, physics.chem-ph, physics.comp-ph

### Abstract
> Machine learning interatomic potentials (MLIPs) have become a hallmark of AI for scientific simulation. While efforts on new architectures and datasets have led to increasingly accurate and general models, the choice of optimizer for training has largely remained unexplored, defaulting to Adam and its variants in the community. Here, we implement and systematically compare a class of recently proposed matrix-structured optimizers, including Muon, SOAP, and the hybrid SOAP-Muon, for training NequIP and Allegro MLIP models. We find that these optimizers can substantially outperform Adam in both convergence speed and final accuracy. SOAP and SOAP-Muon emerge as robust and consistently strong methods, while Muon only provides partial gains relative to Adam. The improvements are particularly pronounced under partial force supervision. Our results indicate that optimizer choice is an overlooked yet impactful design axis for MLIPs.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1. Formula Walkthrough**
### Equation 1: CsH2PO4
```latex
\text{CsH}{\vphantom{\text{X}}}_{\smash[t]{\text{2}}}\text{PO}{\vphantom{\text{X}}}_{\smash[t]{\text{4}}}
```
Symbols: Cs (Cesium), H (Hydrogen), P (Phosphorus)
Why it matters: This equation represents a chemical formula for a compound, likely used in the context of the paper's discussion on machine learning interatomic potentials.

### Equation 2: 50%
```latex
50\%
```
Symbols: None
Why it matters: This equation represents a percentage value, likely used in the context of the paper's discussion on hyperparameter tuning or data sampling.

### Equation 3: 100%
```latex
100\%
```
Symbols: None
Why it matters: This equation represents a percentage value, likely used in the context of the paper's discussion on hyperparameter tuning or data sampling.

### Equation 4: θ
```latex
\theta
```
Symbols: θ (theta)
Why it matters: This equation represents a parameter or variable used in the context of the paper's discussion on machine learning interatomic potentials.

### Equation 5: {r_j, Z_j}
```latex
\{\mathbf{r}_{j},Z_{j}\}
```
Symbols: r_j (atomic position), Z_j (atomic number)
Why it matters: This equation represents a set of atomic positions and chemical species used in the context of the paper's discussion on machine learning interatomic potentials.

### Equation 6: E_θ
```latex
E_{\theta}
```
Symbols: E_θ (energy)
Why it matters: This equation represents the predicted energy of a system using a machine learning interatomic potential.

### Equation 7: ε_i, θ
```latex
\varepsilon_{i,\theta}
```
Symbols: ε_i, θ (epsilon_i, theta)
Why it matters: This equation represents a local atomic contribution to the predicted energy of a system using a machine learning interatomic potential.

### Equation 8: E_θ({r_j, Z_j})
```latex
E_{\theta}(\{\mathbf{r}_{j},Z_{j}\})=\sum_{i}\varepsilon_{i,\theta}(\{\mathbf{r}_{j},Z_{j}\}_{j\in\mathcal{N}_{i}}),
```
Symbols: E_θ (energy), ε_i, θ (epsilon_i, theta), r_j (atomic position), Z_j (atomic number), i (index)
Why it matters: This equation represents the predicted energy of a system using a machine learning interatomic potential, decomposed into a sum of local atomic contributions.

**2. Method Summary**
* The paper proposes a new class of matrix-structured optimizers, including Muon, SOAP, and the hybrid SOAP-Muon, for training machine learning interatomic potentials.
* The optimizers are designed to improve convergence speed and final accuracy in training MLIP models.
* The paper evaluates the optimizers across different equivariant architectures and chemical environments, including NequIP and Allegro models.

**3. Experimental Overview**
* Tasks: Training machine learning interatomic potentials using different optimizers.
* Datasets: NequIP and Allegro models.
* Baselines: AdamW.
* Main claimed findings: The matrix-structured optimizers substantially outperform AdamW in both convergence speed and final accuracy, with SOAP and SOAP-Muon emerging as robust and consistently strong methods.

**4. What to Verify in the PDF**
* The implementation details of the matrix-structured optimizers, including Muon and SOAP.
* The hyperparameter tuning protocol used to evaluate the optimizers.
* The results of the experiments, including the accuracy improvements and time-to-accuracy reductions.
{% endraw %}

{% raw %}
## 4) OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers
- **Authors:** Donghyun Lee, Jitesh Chavan, Duy Nguyen, Sam Huang, Liming Jiang, Priyadarshini Panda, Timo Mertens, Saurabh Shukla
- **arXiv:** [2607.02461](https://arxiv.org/abs/2607.02461v1) · [pdf](https://arxiv.org/pdf/2607.02461v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.02461v1))
- **Categories:** cs.CV, cs.AI, cs.LG

### Abstract
> Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in a normalized, rotated basis. In this basis, a randomized permuted block-Hadamard (RPBH) rotation concentrates each coordinate around one fixed, known marginal regardless of the input, so a single Lloyd-Max codebook serves all timesteps, prompts, and layers of a given input dimension. We extend the same quantizer to weight rows offline, absorbing the rotation into the weights so that it cancels inside each linear layer and only a forward rotation on the activations remains at runtime. The same recipe transfers from image to video with no per-modality tuning. Across FLUX.1, Z-Image-Turbo, Wan 2.1, and CogVideoX, it sets the state of the art for PTQ at several low-bit settings. It also pushes PTQ of image diffusion transformers to W2A4 with usable generation quality.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Π_d
Π_d = \Pi_{d}
* Equation: Π_d (Pi-d)
* Symbols: Π_d (Pi-d), π (π)
* Why it matters: Represents the distributional quantizer applied in one shared, rotated, normalized basis.

### Equation 2: \hat{W}^{\prime}\hat{x}^{\prime} \approx Wx
\hat{W}^{\prime}\hat{x}^{\prime}\approx Wx
* Equation: Approximation of the weight and activation product
* Symbols: \hat{W}^{\prime} (hat-W-prime), \hat{x}^{\prime} (hat-x-prime), W (W), x (x)
* Why it matters: Demonstrates the quantization process, where the approximated product is close to the original product.

### Equation 3: f_d \approx \mathcal{N}(0,1/d)
f_{d}\approx\mathcal{N}(0,1/d)
* Equation: Approximation of the distribution f_d
* Symbols: f_d (f-d), \mathcal{N} (N), 0 (0), 1/d (1/d)
* Why it matters: Represents the distribution used for quantization, which is approximately a standard normal distribution.

### Equation 4: \mathcal{C}_{d,b}
\mathcal{C}_{d,b}
* Equation: Not explicitly defined in the context
* Symbols: \mathcal{C}_{d,b} (C-d-b)
* Why it matters: Not found in extracted context.

### Equation 5: \mathbf{W}
\mathbf{W}
* Equation: Not explicitly defined in the context
* Symbols: \mathbf{W} (W)
* Why it matters: Not found in extracted context.

### Equation 6: \mathbf{x}
\mathbf{x}
* Equation: Not explicitly defined in the context
* Symbols: \mathbf{x} (x)
* Why it matters: Not found in extracted context.

### Equation 7: \mathbf{y} = \mathbf{W}\mathbf{x}, \quad \mathbf{W} \in \mathbb{R}^{m \times d}, \quad \mathbf{x} \in \mathbb{R}^{d}
\mathbf{y}=\mathbf{W}\mathbf{x},\quad\mathbf{W}\in\mathbb{R}^{m\times d},\quad\mathbf{x}\in\mathbb{R}^{d}
* Equation: Matrix multiplication
* Symbols: \mathbf{y} (y), \mathbf{W} (W), \mathbf{x} (x), \mathbb{R}^{m \times d} (R-m-d), \mathbb{R}^{d} (R-d)
* Why it matters: Represents the matrix multiplication used in the paper, which is a fundamental operation in linear algebra.

**Method Summary**
==================

* OrbitQuant replaces per-input range calibration with a distributional quantizer applied in one shared, rotated, normalized basis.
* The quantizer is applied in two stages: offline and online.
* Offline, the weights are quantized using a randomized permuted block-Hadamard (RPBH) rotation.
* Online, the activations are quantized using a nearest-centroid lookup.
* The quantizer is designed to be data-agnostic, meaning it can be applied to any input without requiring re-calibration.

**Experimental Overview**
========================

* Tasks/Datasets:
	+ Image generation: FLUX.1-schnell, FLUX.1-dev, Z-Image-Turbo
	+ Video generation: Wan 2.1-1.3B, CogVideoX-2B
* Baselines/Comparisons:
	+ SVDQuant
	+ AdaTSQ
	+ ViDiT-Q
	+ QuaRot
	+ SmoothQuant
* Main Claimed Findings:
	+ OrbitQuant achieves state-of-the-art results for image and video generation at several low-bit settings.
	+ OrbitQuant has the lowest overhead among the weight-and-activation quantization methods on both image and video.

**What to Verify in the PDF**
=============================

* The implementation details of the RPBH rotation and the nearest-centroid lookup.
* The analysis of the latency and memory overhead of OrbitQuant compared to other methods.
* The results of the ablation study, including the effect of different rotations and the impact of AdaLN modulation on the model's performance.
{% endraw %}

{% raw %}
## 5) Neuron-Aware Active Few-Shot Learning for LLMs
- **Authors:** Zhuowei Chen, Liwei Chen, Christian Schunn, Raquel Coelho, Xiang Lorraine Li
- **arXiv:** [2607.02423](https://arxiv.org/abs/2607.02423v1) · [pdf](https://arxiv.org/pdf/2607.02423v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.02423v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Active Few-Shot Learning (AFSL) adapts LLMs to specialized domains by identifying the most valuable unlabeled samples for annotation and use as few-shot demonstrations, effectively reducing human annotation costs while promoting high performance. However, existing methods typically rely on output-level signals for sample identification, such as predictive entropy or semantic similarities with test-time data based on external embeddings, which often overlook models' internal dynamics, which could pinpoint specific knowledge gaps. To bridge this gap, we propose NeuFS, a Neuron-Aware Active Few-Shot Learning framework that shifts the selection paradigm from output-level proxies to models' internal dynamics. NeuFS utilizes neuron activation patterns to represent sample directly, and includes a dual-criteria selection strategy that: (1) ensures few-shot sample diversity with neuron patterns for broader example coverage, while (2) prioritizing on identifying informative and challenging few-shot samples LLMs tend to hallucinate by quantifying neuron consensus. Experiments on three datasets demonstrate that NeuFS excels in both reasoning and text classification tasks, outperforming existing AFSL baselines. Ablation studies further highlight that internal neuron activations provide a more principled and effective selection signal than external embeddings, validating the superiority of the proposed NeuFS.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathbf{h}^{l}$

* Equation: $\mathbf{h}^{l}$
* Symbols: $\mathbf{h}^{l}$ (raw activation values from FFNs across all transformer layers for each candidate sample)
* Why it matters: This represents the raw activation values from the FFNs, which are used as input to the Neuron Activation Identification stage.

### Equation 2: $\mathbf{W}_{\textit{in}}^{l} \in \mathbb{R}^{d \times d_{ff}}$

* Equation: $\mathbf{W}_{\textit{in}}^{l} \in \mathbb{R}^{d \times d_{ff}}$
* Symbols: $\mathbf{W}_{\textit{in}}^{l}$ (weight matrix for input layer)
* Why it matters: This weight matrix is used to transform the raw activation values into a more meaningful representation.

### Equation 3: $\sigma(\cdot)$

* Equation: $\sigma(\cdot)$
* Symbols: $\sigma(\cdot)$ (activation function)
* Why it matters: This activation function is used to introduce non-linearity into the model.

### Equation 4: $\mathbf{W}_{\textit{out}}^{l} \in \mathbb{R}^{d_{ff} \times d}$

* Equation: $\mathbf{W}_{\textit{out}}^{l} \in \mathbb{R}^{d_{ff} \times d}$
* Symbols: $\mathbf{W}_{\textit{out}}^{l}$ (weight matrix for output layer)
* Why it matters: This weight matrix is used to transform the output of the Neuron Activation Identification stage into a final prediction.

### Equation 5: $d_{ff}$

* Equation: $d_{ff}$
* Symbols: $d_{ff}$ (number of feed-forward neurons)
* Why it matters: This represents the number of feed-forward neurons in the model, which is used to transform the raw activation values.

**Method Summary**
==================

* **NeuFS**: A neuron-aware active few-shot learning framework that shifts the selection paradigm from output-level proxies to models' internal dynamics.
* **Dual-criteria selection strategy**: Ensures few-shot sample diversity with neuron patterns for broader example coverage, while prioritizing on identifying informative and challenging few-shot samples.
* **Neuron Activation Identification**: Filters for neurons that contribute significantly to the model's final prediction.
* **Neuron-Aware Active Few-Shot Selection**: Integrates Neuron-Aware Sample Diversification with Neuron Consensus Quantification to prioritize samples that trigger unique knowledge circuits.

**Experimental Overview**
========================

* **Tasks/Datasets**: Three reasoning and classification datasets: MMLU-Pro, Edu-Feedback, and TREC.
* **Baselines/Comparisons**: Six baseline methods: Random, TypiClust, Patron, and four variants of existing AFSL methods.
* **Main Claimed Findings**: NeuFS outperforms existing AFSL baselines and achieves the highest accuracy on the three datasets.

**What to Verify in the PDF**
=============================

* **Details of the Early Unembedding technique**: How does Early Unembedding work, and how is it used in the Neuron Activation Identification stage?
* **Mathematical derivations of the Neuron Consensus Quantification**: How are the mathematical derivations of the Neuron Consensus Quantification formula provided in the paper?
* **Experimental results for different Info Types**: How do the experimental results for different Info Types (e.g. Semantic signals, Entropy, Linguistic features) compare to each other, and how do they compare to the results for NeuFS?
{% endraw %}
