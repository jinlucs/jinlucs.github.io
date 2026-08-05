---
layout: post
title: "Daily arXiv Digest — 2026-08-05 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Information-Geometric Forward Policy Training in GFlowNets
- **Authors:** Yordan Raykov, Rodrigo Veiga
- **arXiv:** [2608.03967](https://arxiv.org/abs/2608.03967v1) · [pdf](https://arxiv.org/pdf/2608.03967v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.03967v1))
- **Categories:** stat.ML, cs.LG

### Abstract
> Generative Flow Networks (GFlowNets) have emerged as a flexible framework for amortised inference over discrete and mixed discrete-continuous objects, requiring only an unnormalised target density specified through a reward. In this work, we formulate forward-policy training in GFlowNets through the information geometry of the induced trajectory sampler. Treating the forward policy as an induced trajectory sampler, we show that its intrinsic first-order geometry is given by the Fisher-Rao metric of the trajectory family, and that the associated natural gradient provides the canonical local update whenever the corresponding Fisher information is computable or accurately approximable. We derive an exact decomposition of the trajectory Fisher into per-step conditional second moments, which clarifies when temporal score interactions vanish and when dense couplings remain under shared parameterisation. This leads to three computational regimes: settings with tractable exact Fisher information, settings where Monte Carlo estimators of the expected Fisher are sufficient, and structure-exploitable settings in which target locality or factorisation yields accurate approximations of the Fisher expectation. In the latter case, graphical-model tools such as exact marginalisation, separator methods, and belief propagation provide principled surrogates for natural-gradient updates. The resulting framework turns target structure into optimisation geometry and yields a tractable route to structure-aware forward-policy training in GFlowNets. We illustrate the framework empirically through examples comparing convergence and exploration behaviour under Riemannian and Euclidean optimisation.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: R(x)

* Equation: R(x)
* Symbols: R(x) (not explicitly defined in the context)
* Why it matters: Not found in extracted context.

### Equation 2: θ

* Equation: θ
* Symbols: θ
* Why it matters: θ is the parameter of the forward policy, but its definition is not provided in the extracted context.

### Equation 3: π_{θ}

* Equation: π_{θ}
* Symbols: π_{θ} (π_{θ} is the forward policy)
* Why it matters: π_{θ} is the forward policy, which is the main object of study in the paper.

### Equation 4: q_{θ}(\tau) = \prod_{t=0}^{T-1} \pi_{\theta}(a_{t} | s_{t})

* Equation: q_{θ}(\tau) = \prod_{t=0}^{T-1} \pi_{\theta}(a_{t} | s_{t})
* Symbols: q_{θ}(\tau), π_{θ}(a_{t} | s_{t}) (π_{θ} is the forward policy)
* Why it matters: This equation represents the forward policy as a product of conditional probabilities, which is a key concept in the paper.

### Equation 5: \tau

* Equation: \tau
* Symbols: \tau
* Why it matters: \tau is the trajectory, which is the output of the forward policy.

### Equation 6: s_{t}

* Equation: s_{t}
* Symbols: s_{t}
* Why it matters: s_{t} is the state at time t, which is a key component of the trajectory.

### Equation 7: a_{t}

* Equation: a_{t}
* Symbols: a_{t}
* Why it matters: a_{t} is the action taken at time t, which is a key component of the trajectory.

**Method Summary**
==================

* The authors propose a method for training forward policies in GFlowNets using information-geometric forward policy training.
* The method is based on the Fisher-Rao metric and the natural gradient.
* The authors derive an exact decomposition of the trajectory Fisher into per-step conditional second moments.
* The method has three computational regimes: settings with tractable exact Fisher information, settings where Monte Carlo estimators of the expected Fisher are sufficient, and structure-exploitable settings in which target locality or factorisation yields accurate approximations of the Fisher expectation.

**Experimental Overview**
=========================

* The authors evaluate their method on two benchmark datasets: the 8-Gaussians and Rings lazy-random-walk benchmarks.
* The 8-Gaussians benchmark is a standard benchmark for evaluating the performance of trajectory-balance methods.
* The Rings benchmark is a more challenging benchmark that requires the method to recover a larger number of modes.
* The authors compare their method to three baselines: Euclidean TB, Wasserstein TB, and ACE/DTB.
* The authors report that their method achieves a negative reward gap, indicating that the learned distribution over-weights high-reward ring cells relative to the target distribution.

**What to Verify in the PDF**
=============================

* The authors mention that the factorised natural-gradient approximation matches the full-Fisher variants at a fraction of the per-step cost. Verify this claim by examining the implementation details of the factorised natural-gradient approximation.
* The authors report that the learned distribution over-weights high-reward ring cells relative to the target distribution. Verify this claim by examining the learned distribution and the target distribution.
* The authors mention that the method has three computational regimes. Verify this claim by examining the implementation details of the method and the conditions under which each regime is applicable.
{% endraw %}

{% raw %}
## 2) Muon Meets Mamba: Spectral Optimization for State Space Models
- **Authors:** Arslan Battalov, Karim Kramin, Alexander Markotenko, Sofia Sinitsina
- **arXiv:** [2608.03941](https://arxiv.org/abs/2608.03941v1) · [pdf](https://arxiv.org/pdf/2608.03941v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.03941v1))
- **Categories:** cs.LG

### Abstract
> Muon is a recent optimizer that orthogonalizes the update to each weight matrix with a Newton-Schulz iteration, which performs steepest descent under the spectral norm. Almost all the evidence for it comes from Transformer models, and its behavior on state-space models is largely unreported. We compare Muon with AdamW on Mamba-2 130M under a controlled protocol that varies only which weight groups are trained with Muon. The benefit is localized. Muon on the output projection alone beats Muon on the input projection or on both. The advantage is mainly one of token efficiency. It holds on two corpora and two token budgets, and persists when training continues well past the compute-optimal point. Conditioning does not explain the gain. Muon lowers the condition number of whichever projection it trains, but the better-conditioned input projection is not the one that helps.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $10^{9}$

* Equation: $10^{9}$
* Symbols: None
* Why it matters: Not found in extracted context.

### Equation 2: $2.6 \times 10^{9}$

* Equation: $2.6 \times 10^{9}$
* Symbols: None
* Why it matters: Not found in extracted context.

### Equation 3: $5 \times 10^{10}$

* Equation: $5 \times 10^{10}$
* Symbols: None
* Why it matters: Not found in extracted context.

### Equation 4: $\mathcal{G}_{\mathrm{in}}$

* Equation: $\mathcal{G}_{\mathrm{in}}$
* Symbols: $\mathcal{G}_{\mathrm{in}}$
* Why it matters: Represents the input projection group.

### Equation 5: $\mathcal{G}_{\mathrm{out}}$

* Equation: $\mathcal{G}_{\mathrm{out}}$
* Symbols: $\mathcal{G}_{\mathrm{out}}$
* Why it matters: Represents the output projection group.

### Equation 6: $\mathcal{G}_{\mathrm{in}} \cup \mathcal{G}_{\mathrm{out}}$

* Equation: $\mathcal{G}_{\mathrm{in}} \cup \mathcal{G}_{\mathrm{out}}$
* Symbols: $\mathcal{G}_{\mathrm{in}}$, $\mathcal{G}_{\mathrm{out}}$
* Why it matters: Represents the union of the input and output projection groups.

**Method Summary**
==================

* The authors compare Muon with AdamW on Mamba-2 130M under a controlled protocol.
* The benefit of Muon is localized to the output projection.
* Muon reduces the condition number of the projection it trains.
* The authors evaluate Muon on two corpora (OpenWebText and FineWeb-Edu) and two token budgets (10^9 and 2.6 × 10^9).

**Experimental Overview**
=========================

* Tasks: Autoregressive language modeling.
* Datasets: OpenWebText and FineWeb-Edu.
* Baselines: AdamW.
* Comparisons: Muon on different projection groups (input, output, and both).
* Main claimed findings:
	+ Muon reduces final validation loss relative to AdamW.
	+ Muon achieves the lowest final loss on the output projection group.
	+ Muon is robust across corpora and token budgets.

**What to Verify in the PDF**
=============================

* The authors' analysis of the condition number of the projection groups.
* The impact of conditioning on the performance of Muon.
* The robustness of Muon across different token budgets and corpora.
{% endraw %}

{% raw %}
## 3) Logic Before Language: Pre-pretraining on Formal Derivations Fosters Skill Acquisition and Compressibility
- **Authors:** Jo-Ku Cheng, Nikolaos Aletras, Marco Valentino
- **arXiv:** [2608.03930](https://arxiv.org/abs/2608.03930v1) · [pdf](https://arxiv.org/pdf/2608.03930v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.03930v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> Pre-pretraining language models (LMs) on symbolic data can accelerate and improve natural language acquisition. However, existing pre-pretraining tasks, such as Dyck and procedural algorithms, rely on narrow primitives that fail to capture the expressive capacity of natural language. Moreover, prior studies remain restricted to relatively small token budgets, offering limited insight into skill emergence and representational dynamics. To address these limitations, we propose logic pre-pretraining (Logic-PPT) as a principled initialization strategy, leveraging formal derivations to impart richer structural and linguistic biases. Formal derivations require abstract mechanisms that are central to natural language, simultaneously binding variables, connecting quantifiers and relational dependencies, and composing predicate-argument structures over long contexts. Scaling our evaluation to a 100B-token regime, logic pre-pretraining substantially accelerates skill acquisition in LMs, achieving 80\% accuracy on linguistic tasks with 36B fewer tokens than standard initialization, and outperforming alternative pre-pretraining baselines. Mechanistically, formal derivations induce persistent structural reorganization, distinctively characterized by a lower-rank, spectrally concentrated representation space. Crucially, we show that this internal geometry enables improved model compressibility via pruning, matching the dense baseline performance even at $\approx$33\% sparsity.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 
\[
\mathcal{A} \rightarrow \mathcal{R} \rightarrow \varphi
\]

* Equation: A logical derivation sequence
* Symbols:
	+ \(\mathcal{A}\): set of logical axioms
	+ \(\mathcal{R}\): set of inference rules
	+ \(\varphi\): final goal formula
* Why it matters: This equation represents the structure of a formal logical derivation, which is used to generate the target step in the Logic Pre-Pretraining (Logic-PPT) framework.

### Equation 2: 
\[
\Theta_{\text{logic}}^{*} = \{\ \Theta_{\text{backbone}}^{\text{logic}},\mathbf{E}_{\text{logic}}^{*},\mathbf{H}_{\text{logic}}^{*}\}
\]

* Equation: Definition of the resulting parameters after Logic-PPT
* Symbols:
	+ \(\Theta_{\text{logic}}^{*}\): resulting parameters after Logic-PPT
	+ \(\Theta_{\text{backbone}}^{\text{logic}}\): backbone parameters
	+ \(\mathbf{E}_{\text{logic}}^{*}\): embedding parameters
	+ \(\mathbf{H}_{\text{logic}}^{*}\): hidden state parameters
* Why it matters: This equation shows how the resulting parameters are defined after Logic-PPT, which is used to evaluate the performance of the model.

### Equation 3: 
\[
\Gamma = \{\alpha_i\}_{i=1}^{L}
\]

* Equation: Definition of the premise set
* Symbols:
	+ \(\Gamma\): premise set
	+ \(\alpha_i\): intermediate formulas
	+ \(L\): number of steps
* Why it matters: This equation represents the premise set generated by the derivation tree, which is used to evaluate the performance of the model.

### Equation 4: 
\[
\varphi = \mathcal{A} \cup \mathcal{R} \cup \Gamma
\]

* Equation: Definition of the final goal formula
* Symbols:
	+ \(\varphi\): final goal formula
	+ \(\mathcal{A}\): set of logical axioms
	+ \(\mathcal{R}\): set of inference rules
	+ \(\Gamma\): premise set
* Why it matters: This equation shows how the final goal formula is defined, which is used to evaluate the performance of the model.

### Equation 5: 
\[
\mathcal{R} = \{\rho_1, \rho_2, ..., \rho_n\}
\]

* Equation: Definition of the set of inference rules
* Symbols:
	+ \(\mathcal{R}\): set of inference rules
	+ \(\rho_i\): inference rule
	+ \(n\): number of inference rules
* Why it matters: This equation represents the set of inference rules used in the Logic-PPT framework, which is used to generate the target step.

**Method Summary**
==================

* The Logic Pre-Pretraining (Logic-PPT) framework is proposed to accelerate and improve natural language acquisition.
* The framework consists of two main stages: Logic Pre-Pretraining and Natural Language Pretraining via backbone transfer.
* The Logic Pre-Pretraining stage uses formal logical derivations to impart richer structural and linguistic biases to the model.
* The Natural Language Pretraining stage uses the resulting parameters from Logic Pre-Pretraining to fine-tune the model on natural language data.

**Experimental Overview**
=========================

* The experiment uses a 14-layer Qwen3 architecture as the Transformer backbone.
* The model is trained on a 100B-token regime and compared to a randomly initialized baseline undergoing only language pretraining.
* The experiment evaluates the performance of the model on linguistic tasks and analyzes the representation geometry and pruning robustness.

**What to Verify in the PDF**
=============================

* The evaluation scope of the paper, including the evaluation of the benefits of Logic-PPT on downstream tasks.
* The details of the derivation-tree generation process, including the library of derivation schemata and the backward chaining algorithm.
* The results of the pruning robustness analysis, including the effect of sparsity on the model's performance.
{% endraw %}

{% raw %}
## 4) Latent Reward Registers for Diffusion Preference Alignment
- **Authors:** Yuanshen Guan, Zipeng Feng, Zhiwei Xiong, Peiqin Sun
- **arXiv:** [2608.03929](https://arxiv.org/abs/2608.03929v1) · [pdf](https://arxiv.org/pdf/2608.03929v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.03929v1))
- **Categories:** cs.LG, cs.CV

### Abstract
> Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents by prepending learnable, position-free register tokens to the input sequence of a frozen Diffusion Transformer (DiT). This independent readout mechanism extracts latent reward evidence without altering the generator's hidden states or velocity field. The resulting dense, differentiable reward signal throughout the full denoising process facilitates two alignment strategies. For training, Reward-Gradient On-Policy Distillation (RG-OPD) distills reward-guided updates along on-policy trajectories, bypassing the computationally expensive rollouts of standard policy gradients. For inference, Reward-Guided Sampling (RGS) steers trajectories via magnitude-matched reward gradients without parameter updates. Empirically, at high noise levels (u = 0.8), the registers reach the highest pairwise accuracy among the evaluated latent reward models. Furthermore, RG-OPD outperforms online reinforcement learning baselines while reducing GPU hours by up to 33x, and RGS establishes a new state-of-the-art among training-free methods, strictly enhancing both alignment and perceptual metrics. Code and weights are available at https://github.com/Guanys-dar/latent-reward-register
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `u{=}0.8`

* Equation: `u{=}0.8`
* Symbols: `u` (noise level)
* Why it matters: This equation represents the noise level used in the experiment, which is set to 0.8. This value is used to evaluate the performance of the latent reward models.

### Equation 2: `33\times`

* Equation: `33\times`
* Symbols: `33` (factor)
* Why it matters: This equation represents the factor by which the training efficiency of RG-OPD is improved compared to online reinforcement learning baselines.

### Equation 3: `z_{t}`

* Equation: `z_{t}`
* Symbols: `z_{t}` (latent state)
* Why it matters: This equation represents the latent state at time `t`, which is used to compute the reward signal.

### Equation 4: `\nabla R`

* Equation: `\nabla R`
* Symbols: `\nabla R` (reward gradient)
* Why it matters: This equation represents the gradient of the reward signal with respect to the latent state.

### Equation 5: `z_{i}`

* Equation: `z_{i}`
* Symbols: `z_{i}` (latent state)
* Why it matters: This equation represents the latent state at position `i`, which is used to compute the reward signal.

**Method Summary**
================

* The proposed framework consists of three core components:
	+ Latent Reward Registers: a lightweight mechanism that predicts the expected terminal preference using learnable register tokens and frozen DiT features.
	+ Reward-Gradient On-Policy Distillation (RG-OPD): a training strategy that distills reward-guided updates along on-policy trajectories.
	+ Reward-Guided Sampling (RGS): an inference strategy that steers trajectories via magnitude-matched reward gradients.

**Experimental Overview**
=====================

* Tasks/Datasets: The experiment is performed on four benchmarks: ImageReward, HPDv2, HPDv3, and GenAI-Bench.
* Baselines/Comparisons: The proposed framework is compared to five latent reward baselines: LRM, PAVRM, Diffusion Probe, DiNa-LRM, and online reinforcement learning baselines.
* Main Claimed Findings: The proposed framework outperforms all latent baselines on three of the four benchmarks and remains highly competitive on the fourth, despite evaluating heavily corrupted latents.

**What to Verify in the PDF**
==========================

* The implementation details of the Latent Reward Registers mechanism, including the architecture and training procedure.
* The evaluation protocol for the RG-OPD and RGS strategies, including the choice of hyperparameters and metrics used.
* The results of the ablation study, including the impact of different register designs and noise levels on the performance of the proposed framework.
{% endraw %}

{% raw %}
## 5) Sparse Weight Decomposition for Efficient Circuit Extraction
- **Authors:** Chuanhao Yan, Xuhan Huang, Yawen Duan, Zhenfei Yin, Hang Zhao, Bryan Dai, Jie Fu
- **arXiv:** [2608.03913](https://arxiv.org/abs/2608.03913v1) · [pdf](https://arxiv.org/pdf/2608.03913v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.03913v1))
- **Categories:** cs.LG, cs.CL

### Abstract
> Dense pretrained transformers do not naturally expose interpretable units for circuit extraction. Existing approaches obtain such units by learning auxiliary sparse representations or training sparse models, incurring substantial additional computation while potentially introducing a fidelity gap between the representation being analyzed and the original pretrained model. We propose Sparse Weight Decomposition (SWD), which reparameterizes pretrained linear projections by factorizing each weight matrix into two sparse factors whose shared intermediate coordinates serve as individually addressable circuit units. Without training a separate replacement network, this parametric representation supports the same scoring, selection, and ablation circuit extraction workflow used for methods that learn sparse features. Across single-matrix replacements, SWD matches the held-out fidelity achieved by Transcoder and other strong baselines while using less than 1% of the data that those baselines use to train their replacements. For matched replacement fidelity, SWD reaches the same circuit sufficiency and necessity targets with fewer active read/write edges and selected units across tasks on GPT-2, Qwen2.5, and Qwen3.5-27B. We further show that SWD remains effective for full-model replacement of all attention and MLP weight matrices after fine-tuning the nonzero factor values. Finally, SWD also features a zero-data variant, allowing broader use of mechanistic interpretability analysis (e.g., per-step analysis).
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: {\bm{W}}
```markdown
{\bm{W}} ∈ ℝ d in × d out
```
Symbols: `{\bm{W}}`, `d in`, `d out`
Why it matters: This is the dense matrix representing the weight of the model.

### Equation 2: {\bm{W}} ≈ {\bm{A}}{\bm{B}}
```markdown
{\bm{W}} ≈ {\bm{A}}{\bm{B}}
```
Symbols: `{\bm{W}}`, `{\bm{A}}`, `{\bm{B}}`
Why it matters: This equation represents the approximation of the dense weight matrix using the sparse product of two matrices.

### Equation 3: {\bm{A}}_{:,i}
```markdown
{\bm{A}}_{:,i}
```
Symbols: `{\bm{A}}`, `:,`, `i`
Why it matters: This represents the `i`-th column of the sparse matrix `{\bm{A}}`.

### Equation 4: {\bm{B}}_{i,:}
```markdown
{\bm{B}}_{i,:}
```
Symbols: `{\bm{B}}`, `i`, `:`
Why it matters: This represents the `i`-th row of the sparse matrix `{\bm{B}}`.

### Equation 5: {\bm{A}}_{:,i}{\bm{B}}_{i,:}
```markdown
{\bm{A}}_{:,i}{\bm{B}}_{i,:}
```
Symbols: `{\bm{A}}`, `{\bm{B}}`, `:,`, `i`, `:`
Why it matters: This represents the product of the `i`-th column of `{\bm{A}}` and the `i`-th row of `{\bm{B}}`.

**Method Summary**
==================

* The authors propose Sparse Weight Decomposition (SWD), a method for efficient circuit extraction using sparse weight decomposition.
* SWD reparameterizes the dense weight matrix using factorization into two sparse matrices.
* The method is designed to preserve the same scoring, selection, and ablation workflow as existing approaches.
* SWD achieves the same replacement fidelity as strong baselines while using less than 1% of the data required.

**Experimental Overview**
==========================

* The authors evaluate SWD on three datasets: GPT-2 Small, Qwen2.5, and Qwen3.5-27B.
* The evaluation protocol includes replacement fidelity, circuit cost-quality tradeoff, and circuit extraction.
* The authors compare SWD with three baselines: Transcoder, VPD, and sparse-pretrained models.
* The main claimed findings include:
	+ SWD achieves the same replacement fidelity as strong baselines while using less data.
	+ SWD reduces circuit cost-quality tradeoff.
	+ SWD extracts meaningful units with semantic interpretations.

**What to Verify in the PDF**
=============================

* The construction of the sparse product and its relation to the dense weight matrix.
* The optimization objective and its relation to the Frobenius norm.
* The evaluation protocol and its relation to the task-based circuit-discovery setup.
* The results of the zero-data variant and its implications for mechanistic interpretability analysis.
{% endraw %}
