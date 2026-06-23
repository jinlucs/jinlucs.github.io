---
layout: post
title: "Daily arXiv Digest — 2026-06-23 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Open Problem: Is AdamW Effective Under Heavy-Tailed Noise?
- **Authors:** Dingzhi Yu, Hongyi Tao, Yuanyu Wan, Luo Luo, Lijun Zhang
- **arXiv:** [2606.23676](https://arxiv.org/abs/2606.23676v1) · [pdf](https://arxiv.org/pdf/2606.23676v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.23676v1))
- **Categories:** cs.LG, cs.AI, math.OC, stat.ML

### Abstract
> AdamW is the de facto optimizer for training large language models (LLMs), yet the theory behind it still lives mostly in finite-variance regimes. This is increasingly unsatisfying, as empirical evidence indicates that stochastic gradient noise in LLM pretraining is typically heavy-tailed. Recent work shows that sign-based optimizers such as Lion and Muon achieve sharp heavy-tailed rates, and that AdaGrad can also converge under heavy-tailed noise. However, no rigorous convergence theory for AdamW has yet been established in this regime. Can AdamW converge under the same heavy-tailed assumptions, or does its second-moment accumulator create a genuine obstruction? We formulate this as an open problem, prove a positive weighted-metric benchmark, and give a corridor lower-bound mechanism showing how denominator memory can hide large gradients.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: p ∈ (1, 2]
```math
p \in (1, 2]
```
* Symbols: `p` (a variable representing a parameter)
* Why it matters: This equation represents the range of values for the parameter `p`, which is used to analyze the convergence rate of AdamW under heavy-tailed noise.

### Equation 2: O(T^{-(p-1)/(3p-2)})
```math
O(T^{-(p-1)/(3p-2)})
```
* Symbols: `T` (a variable representing the number of iterations), `p` (a variable representing a parameter)
* Why it matters: This equation represents the convergence rate of sign-based methods under heavy-tailed noise, which serves as a comparison target for AdamW.

### Equation 3: O(√d/T^{1/4})
```math
O(\sqrt{d}/T^{1/4})
```
* Symbols: `d` (a variable representing the dimensionality of the data), `T` (a variable representing the number of iterations)
* Why it matters: This equation represents a lower bound on the convergence rate of AdamW under heavy-tailed noise.

### Equation 4: ℓ1
```math
\ell_{1}
```
* Symbols: `ℓ1` (a notation representing the L1 norm)
* Why it matters: This equation represents the L1 norm, which is used to analyze the convergence rate of AdamW under heavy-tailed noise.

### Equation 5: ∏[\mathbb{E}[\left|\mathbf{g}_{t,i}\right|^{p}] < ∞]
```math
\mathbb{E}[\left|\mathbf{g}_{t,i}\right|^{p}] < \infty
```
* Symbols: `∏` (a notation representing the expectation), `t` (a variable representing the iteration number), `i` (a variable representing the index), `p` (a variable representing a parameter), `ℵ` (a notation representing the expectation)
* Why it matters: This equation represents a condition on the expectation of the L1 norm of the gradient, which is used to analyze the convergence rate of AdamW under heavy-tailed noise.

**Method Summary**
==================

* AdamW is a popular optimizer for training large language models.
* The authors formulate an open problem: Can AdamW converge under heavy-tailed noise?
* The authors compare AdamW to sign-based optimizers, which have been shown to achieve sharp heavy-tailed rates.
* The authors propose a nonasymptotic ℓ1-stationarity upper bound for AdamW under heavy-tailed noise.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors do not specify a particular task or dataset.
* Baselines/Comparisons: The authors compare AdamW to sign-based optimizers.
* Main Claimed Findings: The authors claim that AdamW does not converge under heavy-tailed noise, but provide a lower-bound instance showing that no such guarantee is possible.

**What to Verify in the PDF**
=============================

* The authors provide a clean specialization of the model, which may not be representative of the full paper.
* The authors use a nonasymptotic ℓ1-stationarity upper bound, which may not be sufficient to prove convergence under heavy-tailed noise.
* The authors do not provide a detailed analysis of the convergence rate of AdamW under heavy-tailed noise.
{% endraw %}

{% raw %}
## 2) CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation
- **Authors:** Sikai Li, Shuning Li, Zhenyu Wei, Yunchao Yao, Chenran Li, Mingyu Ding
- **arXiv:** [2606.23680](https://arxiv.org/abs/2606.23680v1) · [pdf](https://arxiv.org/pdf/2606.23680v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.23680v1))
- **Categories:** cs.RO, cs.AI, cs.LG

### Abstract
> Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexterous hand control into coordinated latent residual control, enabling high-DoF dexterous loco-manipulation on the move. Starting from simulated whole-body and hand demonstrations, CoorDex trains privileged motion tracking teachers for the humanoid body and dexterous hand, distills them into proprioception-conditioned latent priors, and uses the frozen priors as the action space for downstream residual reinforcement learning. A coordinated latent residual policy composes these priors through shared task context and separate body-hand residual heads, preserving natural whole-body motion while improving finger-level contact reliability. CoorDex enables a Unitree G1 humanoid with a 20-DoF WUJI hand to execute dexterous manipulation while in motion, including non-stop bottle grasping and carrying, fridge door opening on the move, and cube pick-and-turn. Ablations on the walk-grasp-carry task show that joint-space PPO, joint-space hand control, and monolithic latent prediction all fail under the same reward budget, while the latent-prior interface and coordinated residual structure make high-dimensional contact-rich loco-manipulation trainable. Project Page: https://skevinci.github.io/coordex/
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{D}(\mathcal{R},\mathcal{O})$

* Equation: $\mathcal{D}(\mathcal{R},\mathcal{O})$
* Symbols: $\mathcal{D}$, $\mathcal{R}$, $\mathcal{O}$
* Why it matters: Not found in extracted context.

### Equation 2: $x \in \{b, h\}$

* Equation: $x \in \{b, h\}$
* Symbols: $x$, $b$, $h$
* Why it matters: Denotes the body or hand subsystem.

### Equation 3: $\pi_{T}^{b}$

* Equation: $\pi_{T}^{b}$
* Symbols: $\pi_{T}^{b}$
* Why it matters: Represents the body prior.

### Equation 4: $\mathbf{s}^{b,p}_{t}$

* Equation: $\mathbf{s}^{b,p}_{t}$
* Symbols: $\mathbf{s}^{b,p}_{t}$
* Why it matters: Represents the proprioceptive state of the body.

### Equation 5: $\mathbf{s}^{b,g}_{t}$

* Equation: $\mathbf{s}^{b,g}_{t}$
* Symbols: $\mathbf{s}^{b,g}_{t}$
* Why it matters: Represents the goal state of the body.

**Method Summary**
==================

* CoorDex is a modular pipeline that maps high-dimensional humanoid locomotion and dexterous hand control to coordinated latent residual control.
* The pipeline builds separate body and hand priors and trains a downstream residual RL policy to coordinate them.
* The method consists of three main components: prior construction via teacher tracking and proprioceptive distillation, coordinated latent residual policy, and residual PPO training and environment design.

**Experimental Overview**
========================

* Tasks: Three dexterous humanoid loco-manipulation tasks: WalkGrab, OpenFridge, and WalkPickTurn.
* Baselines: Joint-space PPO, joint-space hand control, and monolithic latent prediction.
* Main claimed findings: CoorDex enables high-dimensional contact-rich loco-manipulation trainable, while the latent-prior interface and coordinated residual structure make it trainable.

**What to Verify in the PDF**
=============================

* The construction of the body and hand priors, including the teacher tracking and proprioceptive distillation pipeline.
* The details of the coordinated latent residual policy, including the shared task context and separate body-hand residual heads.
* The evaluation metrics used to assess the performance of CoorDex, including task success, fall rate, and drop rate.
{% endraw %}

{% raw %}
## 3) Semantic Browsing: Controllable Diversity for Image Generation
- **Authors:** Sara Dorfman, Maya Vishnevsky, Omer Dahary, Or Patashnik, Daniel Cohen-Or
- **arXiv:** [2606.23679](https://arxiv.org/abs/2606.23679v1) · [pdf](https://arxiv.org/pdf/2606.23679v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.23679v1))
- **Categories:** cs.CV, cs.AI, cs.GR, cs.LG

### Abstract
> Modern text-to-image models excel in visual fidelity and prompt adherence. However, this strict adherence comes at the cost of diversity: generated samples tend to collapse into a single visual interpretation. Existing methods to improve diversity produce outputs driven by incidental variations rather than meaningful design choices. This motivates a new variant of the diversity task where structure is enforced on the generated samples. We introduce a method for controlled diversity that enables Semantic Browsing, where users can navigate structured image galleries and experience creative exploration through a systematic traversal of meaningful, interpretable axes of variation. Achieving this level of semantic control requires a deep understanding of the scene. We exploit the fact that recent text-to-image models are trained on elaborated captions, effectively decoupling semantic decision-making from pixel generation. This enables a paradigm shift: instead of relying on stochastic variation within the text-to-image model, we induce diversity directly at the text level. By leveraging rich textual representations, we allow a Vision Language Model (VLM) to operate on the full scene context. To overcome the generic outputs typical of standard VLMs, we employ an agentic workflow that explicitly enforces structured variation attuned to the original prompt. We demonstrate that our method produces diverse and navigable design spaces where every variation corresponds to a specific, user-understandable semantic decision.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\mathcal{S}$

* Equation: $\mathcal{S}$
* Symbols: None
* Why it matters: This equation represents the structured scene space, which is the space of fully specified scene interpretations.

### Equation 2: $s_{0} \in \mathcal{S}$

* Equation: $s_{0} \in \mathcal{S}$
* Symbols: $s_{0}$, $\mathcal{S}$
* Why it matters: This equation represents the initial scene interpretation $s_{0}$, which is a fully specified scene interpretation within the structured scene space $\mathcal{S}$.

### Equation 3: $(V, E)$

* Equation: $(V, E)$
* Symbols: $V$, $E$
* Why it matters: This equation represents the rooted tree $(V, E)$, where $V$ is the set of scene interpretations and $E$ is the set of edges between nodes.

### Equation 4: $s \in V \subset \mathcal{S}$

* Equation: $s \in V \subset \mathcal{S}$
* Symbols: $s$, $V$, $\mathcal{S}$
* Why it matters: This equation represents a scene interpretation $s$ that is a subset of the set of scene interpretations $V$ within the structured scene space $\mathcal{S}$.

### Equation 5: $(s_{1}, s_{2}) \in E$

* Equation: $(s_{1}, s_{2}) \in E$
* Symbols: $s_{1}$, $s_{2}$, $E$
* Why it matters: This equation represents an edge between two scene interpretations $s_{1}$ and $s_{2}$ in the rooted tree $(V, E)$.

**Method Summary**
================

* The method formalizes the generation process as the construction of a hierarchical interpretative tree within a structured scene space.
* The method operates within the space $\mathcal{S}$ of fully specified scene interpretations, encoded as structured JSONs.
* The output of the method is a rooted tree $(V, E)$, where each node is a scene interpretation $s \in V \subset \mathcal{S}$.

**Experimental Overview**
=====================

* Tasks/Datasets: The method is evaluated on a subset of 50 prompts randomly sampled from the MS-COCO dataset.
* Baselines/Comparisons: The method is compared to established baselines designed to maximize diversity.
* Main Claimed Findings: The method significantly enhances output diversity without compromising image quality or prompt alignment.

**What to Verify in the PDF**
==========================

* Additional details regarding the agent configuration and system prompts.
* The scaling ablation across tree depth and branching factor (Appendix F).
* The sensitivity study of VLM choice (Appendix E).
{% endraw %}

{% raw %}
## 4) Diffusion Models Adapt to Low-Dimensional Structure Under Flexible Coefficient Choices
- **Authors:** Changxiao Cai, Yuchen Jiao, Gen Li
- **arXiv:** [2606.23627](https://arxiv.org/abs/2606.23627v1) · [pdf](https://arxiv.org/pdf/2606.23627v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.23627v1))
- **Categories:** stat.ML, cs.LG, math.ST

### Abstract
> Diffusion models are known to exploit unknown low-dimensional structure to accelerate sampling. However, existing convergence theory under low-dimensional data structure has largely focused on update rules with narrowly prescribed coefficient choices. This raises a fundamental question: is adaptation to low-dimensional structure sensitive to the precise choice of update coefficients? In this paper, we show that such adaptation is a robust property of diffusion models. For a broad class of update coefficients, we prove that $\widetilde{O}(k/\varepsilon)$ iterations suffice to generate an $\varepsilon$-accurate sample in total variation (TV) distance, independently of the ambient dimension. Our framework substantially broadens the class of diffusion samplers known to enjoy low dimensional adaptation and applies to several commonly used methods in practice. These results provide a theoretical justification for the empirical effectiveness of diffusion samplers across different coefficient choices when applied to structured, high-dimensional data.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\widetilde{O}(k/\varepsilon)$

* Equation: $\widetilde{O}(k/\varepsilon)$
* Symbols: $\widetilde{O}$, $k$, $\varepsilon$
* Why it matters: This notation represents the time complexity of the algorithm, indicating that the number of iterations required to achieve a certain level of accuracy grows linearly with the number of dimensions $k$ and inversely proportional to the desired accuracy $\varepsilon$.

### Equation 2: $\varepsilon$

* Equation: $\varepsilon$
* Symbols: $\varepsilon$
* Why it matters: This represents the desired accuracy or tolerance in the sampling process. A smaller value of $\varepsilon$ requires more iterations to achieve the same level of accuracy.

### Equation 3: $\{s_{t}(\cdot)\}_{t=1}^{T}$

* Equation: $\{s_{t}(\cdot)\}_{t=1}^{T}$
* Symbols: $s_{t}(\cdot)$, $T$
* Why it matters: This represents the sequence of score functions used in the diffusion process. Each score function $s_{t}(\cdot)$ is used to compute the noise schedule $(\alpha_{t})_{t=1}^{T}$.

### Equation 4: $Y_{T}\sim\mathcal{N}(0,I_{d})$ and $Y_{t-1}=\frac{1}{\sqrt{\alpha_{t}}}\big(Y_{t}+\eta_{t}s_{t}(Y_{t})+\sigma_{t}Z_{t}\big)$

* Equation: $Y_{T}\sim\mathcal{N}(0,I_{d})$ and $Y_{t-1}=\frac{1}{\sqrt{\alpha_{t}}}\big(Y_{t}+\eta_{t}s_{t}(Y_{t})+\sigma_{t}Z_{t}\big)$
* Symbols: $Y_{T}$, $Y_{t-1}$, $\alpha_{t}$, $\eta_{t}$, $s_{t}(\cdot)$, $\sigma_{t}$, $Z_{t}$
* Why it matters: This represents the forward process of the diffusion model, where $Y_{T}$ is a Gaussian random vector with zero mean and identity covariance matrix, and $Y_{t-1}$ is computed using the score function $s_{t}(\cdot)$ and the noise schedule $(\alpha_{t})_{t=1}^{T}$.

### Equation 5: $Z_{t}\overset{\mathsf{i.i.d.}}{\sim}\mathcal{N}(0,I_{d})$

* Equation: $Z_{t}\overset{\mathsf{i.i.d.}}{\sim}\mathcal{N}(0,I_{d})$
* Symbols: $Z_{t}$
* Why it matters: This represents the independent and identically distributed (i.i.d.) Gaussian random vectors used to compute the noise schedule $(\alpha_{t})_{t=1}^{T}$.

### Equation 6: $(\alpha_{t})_{t=1}^{T}$

* Equation: $(\alpha_{t})_{t=1}^{T}$
* Symbols: $(\alpha_{t})_{t=1}^{T}$
* Why it matters: This represents the sequence of noise schedules used in the diffusion process.

### Equation 7: $(\eta_{t},\sigma_{t}^{2})_{t=1}^{T}$

* Equation: $(\eta_{t},\sigma_{t}^{2})_{t=1}^{T}$
* Symbols: $(\eta_{t},\sigma_{t}^{2})_{t=1}^{T}$
* Why it matters: This represents the sequence of parameters used to compute the noise schedule $(\alpha_{t})_{t=1}^{T}$.

### Equation 8: $(\eta_{t},\sigma_{t}^{2})$

* Equation: $(\eta_{t},\sigma_{t}^{2})$
* Symbols: $(\eta_{t},\sigma_{t}^{2})$
* Why it matters: This represents the sequence of parameters used to compute the noise schedule $(\alpha_{t})_{t=1}^{T}$.

**Method Summary**
==================

* The diffusion model uses a sequence of score functions $s_{t}(\cdot)$ to compute the noise schedule $(\alpha_{t})_{t=1}^{T}$.
* The forward process involves computing $Y_{t-1}$ using the score function $s_{t}(\cdot)$ and the noise schedule $(\alpha_{t})_{t=1}^{T}$.
* The diffusion model uses i.i.d. Gaussian random vectors $Z_{t}$ to compute the noise schedule $(\alpha_{t})_{t=1}^{T}$.
* The model is designed to adapt to low-dimensional structure under flexible coefficient choices.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors use a Gaussian distribution to validate their theoretical findings.
* Baselines/Comparisons: The authors compare their results with a baseline model that does not adapt to low-dimensional structure.
* Main Claimed Findings: The authors demonstrate that the diffusion model adapts to low-dimensional structure under flexible coefficient choices, and that this adaptation is robust to changes in the ambient dimension.

**What to Verify in the PDF**
=============================

* The authors claim that the diffusion model adapts to low-dimensional structure under flexible coefficient choices. Verify that this claim is supported by the experimental results.
* The authors use a Gaussian distribution to validate their theoretical findings. Verify that the results are consistent with the theoretical analysis.
* The authors compare their results with a baseline model that does not adapt to low-dimensional structure. Verify that the diffusion model outperforms the baseline model in terms of accuracy and efficiency.
{% endraw %}

{% raw %}
## 5) DiT-Reward: Generative Representations for Text-to-Image Reward Modeling
- **Authors:** Yuanming Yang, Guoqing Ma, Bo Wang, Yuan Zhang, Wei Tang, Chenyi Li, Haoyang Huang, Nan Duan
- **arXiv:** [2606.23626](https://arxiv.org/abs/2606.23626v1) · [pdf](https://arxiv.org/pdf/2606.23626v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.23626v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Can representations learned for image generation also support the evaluation of generated images? We study text-to-image reward prediction as a downstream task of generative representation learning. To this end, we introduce DiT-Reward, which converts a pretrained text-to-image Diffusion Transformer into a reward model by processing near-clean image latents and aggregating text-conditioned image representations across transformer layers. Under the same training data mixture as HPSv3, DiT-Reward outperforms HPSv3 on all four evaluated preference benchmarks, reaching 85.6% on HPDv2 and 77.6% on HPDv3. When the generative backbone is frozen, a lightweight learned head can still extract meaningful preference predictions from its representations. Probing across depth further reveals that downstream reward performance is strongest in the middle-to-late layers and benefits from combining representations across different stages. We also observe consistent positive scaling with generative backbone capacity. Finally, when used to optimize Stable Diffusion 3.5 Large with Flow-GRPO, DiT-Reward outperforms HPSv3 along the matched training trajectory, with particularly clear gains in realism. Direct latent scoring also achieves a 1.65x inference speedup over HPSv3 with comparable peak memory. These results show that pretrained generative DiTs provide transferable representations for reward modeling and policy optimization.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 1.65 ×

* Equation: Not explicitly defined, but appears as a scaling factor in the text.
* Symbols: Not found in extracted context.
* Why it matters: This equation is used to describe the inference speedup of Direct Latent Scoring over HPSv3.

### Equation 2: (x^{+}, x^{-})

* Equation: Not explicitly defined, but appears as a pair of images in the text.
* Symbols: x^{+} and x^{-} represent the preferred and rejected images, respectively.
* Why it matters: This equation represents the pair of images used to train the reward model.

### Equation 3: x^{+}

* Equation: Not explicitly defined, but appears as a representation of the preferred image.
* Symbols: x^{+} represents the preferred image.
* Why it matters: This equation represents the preferred image used to train the reward model.

### Equation 4: x^{-}

* Equation: Not explicitly defined, but appears as a representation of the rejected image.
* Symbols: x^{-} represents the rejected image.
* Why it matters: This equation represents the rejected image used to train the reward model.

### Equation 5: r_{\theta}(x, p)

* Equation: Not explicitly defined, but appears as a reward function.
* Symbols: r_{\theta} represents the reward function, x represents the input image, and p represents the text prompt.
* Why it matters: This equation represents the reward function used to train the reward model.

**Method Summary**
==================

* The authors propose DiT-Reward, a reward model that converts a pretrained text-to-image Diffusion Transformer into a reward model.
* DiT-Reward uses the pretrained text-to-image generator itself as the reward backbone, reusing its internal representations for reward prediction.
* The authors train DiT-Reward with the standard Bradley-Terry preference objective, which increases the reward margin between human-preferred and rejected images.

**Experimental Overview**
========================

* Tasks/Datasets: The authors evaluate DiT-Reward on four preference benchmarks: HPDv2, HPDv3, ImageReward, and PickScore.
* Baselines/Comparisons: The authors compare DiT-Reward with HPSv3, a representative reward model.
* Main Claimed Findings: DiT-Reward outperforms HPSv3 on all four benchmarks, achieving the best performance on HPDv3 and HPDv2.

**What to Verify in the PDF**
=============================

* The authors mention that the training mixture includes HPDv3 pairwise data, a filtered golden subset from HPDv2, sampled Pick-A-Pic data, sampled ImageReward data, and Midjourney user-choice data. Verify the details of this training mixture.
* The authors also mention that the reward head is a lightweight MLP. Verify the architecture of the reward head and its implementation.
* The authors claim that DiT-Reward outperforms HPSv3 on all four benchmarks. Verify the results and the implementation details of the experiments.
{% endraw %}
