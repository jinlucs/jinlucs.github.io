---
layout: post
title: "Daily arXiv Digest — 2026-04-15 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Classical and Quantum Speedups for Non-Convex Optimization via Energy Conserving Descent
- **Authors:** Yihang Sun, Huaijin Wang, Patrick Hayden, Jose Blanchet
- **arXiv:** [2604.13022](https://arxiv.org/abs/2604.13022v1) · [pdf](https://arxiv.org/pdf/2604.13022v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.13022v1))
- **Categories:** quant-ph, cs.LG, math.OC, stat.ML

### Abstract
> The Energy Conserving Descent (ECD) algorithm was recently proposed (De Luca & Silverstein, 2022) as a global non-convex optimization method. Unlike gradient descent, appropriately configured ECD dynamics escape strict local minima and converge to a global minimum, making it appealing for machine learning optimization. We present the first analytical study of ECD, focusing on the one-dimensional setting for this first installment. We formalize a stochastic ECD dynamics (sECD) with energy-preserving noise, as well as a quantum analog of the ECD Hamiltonian (qECD), providing the foundation for a quantum algorithm through Hamiltonian simulation. For positive double-well objectives, we compute the expected hitting time from a local to the global minimum. We prove that both sECD and qECD yield exponential speedup over respective gradient descent baselines--stochastic gradient descent and its quantization. For objectives with tall barriers, qECD achieves a further speedup over sECD.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: V(Θ) = ω^2(Θ^2 - a^2)^2 / (8a^2) + V0

* Equation: V(Θ) = ω^2(Θ^2 - a^2)^2 / (8a^2) + V0
* Symbols:
	+ V(Θ): potential energy
	+ ω: a parameter
	+ Θ: variable
	+ a: a parameter
	+ V0: initial potential energy
* Why it matters: This equation defines the potential energy function V(Θ) used in the Energy Conserving Descent (ECD) algorithm.

### Equation 2: V0 > 0

* Equation: V0 > 0
* Symbols:
	+ V0: initial potential energy
* Why it matters: This inequality ensures that the initial potential energy V0 is positive, which is a necessary condition for the ECD algorithm to work.

### Equation 3: β = V(0) = a^2ω^2 / 8

* Equation: β = V(0) = a^2ω^2 / 8
* Symbols:
	+ β: a parameter
	+ a: a parameter
	+ ω: a parameter
	+ V(0): potential energy at time 0
* Why it matters: This equation defines the parameter β in terms of the initial potential energy V(0) and the parameters a and ω.

### Equation 4: s, h, E, λc, λq

* Equation: s, h, E, λc, λq
* Symbols:
	+ s: a parameter
	+ h: a parameter
	+ E: energy
	+ λc: a parameter
	+ λq: a parameter
* Why it matters: These symbols are used to represent various quantities in the context of the ECD algorithm, but their specific meanings are not explicitly defined in the provided context.

### Equation 5: β → ∞

* Equation: β → ∞
* Symbols:
	+ β: a parameter
* Why it matters: This equation indicates that the parameter β approaches infinity, which is likely used to analyze the behavior of the ECD algorithm as the parameter β increases.

### Equation 6: ≈ √s / (aω^3) exp(ω^2a^2 / s)

* Equation: ≈ √s / (aω^3) exp(ω^2a^2 / s)
* Symbols:
	+ s: a parameter
	+ a: a parameter
	+ ω: a parameter
* Why it matters: This equation provides an approximation for the expected hitting time in the under-guessing regime, which is a key quantity in the ECD algorithm.

### Equation 7: ≈ 1 / (aω^3/2 √h) exp(a^2ω / h)

* Equation: ≈ 1 / (aω^3/2 √h) exp(a^2ω / h)
* Symbols:
	+ h: a parameter
	+ a: a parameter
	+ ω: a parameter
* Why it matters: This equation provides another approximation for the expected hitting time in the under-guessing regime, which is used to compare with the classical case.

### Equation 8: V0 ≥ β

* Equation: V0 ≥ β
* Symbols:
	+ V0: initial potential energy
	+ β: a parameter
* Why it matters: This inequality ensures that the initial potential energy V0 is greater than or equal to the parameter β, which is used to analyze the behavior of the ECD algorithm.

**Method Summary**
================

* The Energy Conserving Descent (ECD) algorithm is a global non-convex optimization method that uses energy-conserving dynamics to escape local minima.
* The algorithm requires an a priori guess F0 for the global minimum, which defines the potential V(Θ) = F(Θ) - F0.
* The ECD algorithm can be applied to both classical and quantum systems, with different dynamics and potential functions.
* The algorithm is analyzed using energy-domain and time-domain approaches, which provide insights into the behavior of the algorithm.

**Experimental Overview**
=====================

* Tasks/Datasets: The authors study the performance of the ECD algorithm on one-dimensional double-well objectives in the under-guessing regime.
* Baselines/Comparisons: The authors compare the performance of the ECD algorithm with classical gradient descent and other optimization methods.
* Main Claimed Findings: The authors demonstrate that the ECD algorithm can achieve faster convergence rates than classical gradient descent in the under-guessing regime.

**What to Verify in the PDF**
==========================

* The authors claim that the ECD algorithm can achieve faster convergence rates than classical gradient descent in the under-guessing regime. Verify this claim by analyzing the expected hitting times and comparing the results with classical gradient descent.
* The authors use a specific double-well potential function F(Θ) = ω^2(Θ^2 - a^2)^2 / (8a^2) to study the behavior of the ECD algorithm. Verify that the potential function satisfies the assumptions made in the paper.
* The authors analyze the behavior of the ECD algorithm using energy-domain and time-domain approaches. Verify that the results are consistent with the theoretical analysis and provide insights into the behavior of the algorithm.
{% endraw %}

{% raw %}
## 2) Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe
- **Authors:** Yaxuan Li, Yuxin Zuo, Bingxiang He, Jinqian Zhang, Chaojun Xiao, Cheng Qian, Tianyu Yu, Huan-ang Gao, Wenkai Yang, Zhiyuan Liu, Ning Ding
- **arXiv:** [2604.13016](https://arxiv.org/abs/2604.13016v1) · [pdf](https://arxiv.org/pdf/2604.13016v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.13016v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> On-policy distillation (OPD) has become a core technique in the post-training of large language models, yet its training dynamics remain poorly understood. This paper provides a systematic investigation of OPD dynamics and mechanisms. We first identify that two conditions govern whether OPD succeeds or fails: (i) the student and teacher should share compatible thinking patterns; and (ii) even with consistent thinking patterns and higher scores, the teacher must offer genuinely new capabilities beyond what the student has seen during training. We validate these findings through weak-to-strong reverse distillation, showing that same-family 1.5B and 7B teachers are distributionally indistinguishable from the student's perspective. Probing into the token-level mechanism, we show that successful OPD is characterized by progressive alignment on high-probability tokens at student-visited states, a small shared token set that concentrates most of the probability mass (97%-99%). We further propose two practical strategies to recover failing OPD: off-policy cold start and teacher-aligned prompt selection. Finally, we show that OPD's apparent free lunch of dense token-level reward comes at a cost, raising the question of whether OPD can scale to long-horizon distillation.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 
\[
\mathcal{L}_{\text{distill}} = \frac{1}{N} \sum_{i=1}^{N} \left( \mathcal{L}_{\text{student}}(x_i) + \lambda \mathcal{L}_{\text{teacher}}(x_i) \right)
\]

* Symbols: $\mathcal{L}_{\text{distill}}$ (distillation loss), $\mathcal{L}_{\text{student}}$ (student loss), $\mathcal{L}_{\text{teacher}}$ (teacher loss), $N$ (batch size), $\lambda$ (weight for teacher loss)
* Why it matters: This equation represents the loss function used for on-policy distillation, which combines the student's loss and the teacher's loss with a weight $\lambda$.

### Equation 2: 
\[
\pi_{\theta} = \mathcal{L}_{\text{student}}(x) + \lambda \mathcal{L}_{\text{teacher}}(x)
\]

* Symbols: $\pi_{\theta}$ (student policy), $\mathcal{L}_{\text{student}}$ (student loss), $\mathcal{L}_{\text{teacher}}$ (teacher loss), $x$ (input)
* Why it matters: This equation represents the student's policy, which is a weighted sum of the student's loss and the teacher's loss.

### Equation 3: 
\[
x = (x_1, \ldots, x_n)
\]

* Symbols: $x$ (input), $x_i$ (input i)
* Why it matters: This equation represents the input to the model, which is a sequence of tokens.

### Equation 4: 
\[
y = (y_1, \ldots, y_m)
\]

* Symbols: $y$ (output), $y_i$ (output i)
* Why it matters: This equation represents the output of the model, which is a sequence of tokens.

### Equation 5: 
\[
y_{<t} \triangleq (y_1, \ldots, y_{t-1})
\]

* Symbols: $y_{<t}$ (prefix of output), $y_i$ (output i)
* Why it matters: This equation represents the prefix of the output, which is used to compute the overlap between the student and teacher.

**Method Summary**
================

* The authors investigate on-policy distillation (OPD) of large language models.
* They identify two conditions for OPD to succeed: (1) the student and teacher should share compatible thinking patterns, and (2) the teacher should offer genuinely new capabilities beyond what the student has seen during training.
* The authors propose two practical strategies to recover failing OPD: off-policy cold start and teacher-aligned prompt selection.
* They also propose a new evaluation metric, the gap recovery rate, to measure the effectiveness of OPD.

**Experimental Overview**
=========================

* The authors use the Qwen3-1.7B-Base model as the student and compare it with two teachers: Qwen3-4B (Non-thinking) and Qwen3-4B-Base-GRPO.
* The authors conduct two OPD experiments using the DAPO-Math-17k dataset and evaluate the performance of the student and teachers on AIME 2024, AIME 2025, and AMC 2023.
* The authors also conduct controlled comparisons across model families, using DeepSeek-R1-Distill-Qwen-1.5B and Skywork-OR1-Math-7B as students and comparing them with their respective post-trained teachers.

**What to Verify in the PDF**
=============================

* The authors claim that the overlap ratio dynamic is stable and consistent throughout training. Verify that this is indeed the case by examining the plots in Figure 21.
* The authors propose a new evaluation metric, the gap recovery rate. Verify that this metric is a reliable measure of OPD effectiveness by comparing it with other evaluation metrics.
* The authors claim that the additional capabilities acquired by the post-trained teachers are more transferable through OPD. Verify this by analyzing the performance of the post-trained teachers on different tasks and datasets.
* The authors propose two practical strategies to recover failing OPD. Verify that these strategies are effective by comparing their performance with the baseline and other methods.
{% endraw %}

{% raw %}
## 3) Causal Diffusion Models for Counterfactual Outcome Distributions in Longitudinal Data
- **Authors:** Farbod Alinezhad, Jianfei Cao, Gary J. Young, Brady Post
- **arXiv:** [2604.12992](https://arxiv.org/abs/2604.12992v1) · [pdf](https://arxiv.org/pdf/2604.12992v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.12992v1))
- **Categories:** stat.ML, cs.LG, econ.EM

### Abstract
> Predicting counterfactual outcomes in longitudinal data, where sequential treatment decisions heavily depend on evolving patient states, is critical yet notoriously challenging due to complex time-dependent confounding and inadequate uncertainty quantification in existing methods. We introduce the Causal Diffusion Model (CDM), the first denoising diffusion probabilistic approach explicitly designed to generate full probabilistic distributions of counterfactual outcomes under sequential interventions. CDM employs a novel residual denoising architecture with relational self-attention, capturing intricate temporal dependencies and multimodal outcome trajectories without requiring explicit adjustments (e.g., inverse-probability weighting or adversarial balancing) for confounding. In rigorous evaluation on a pharmacokinetic-pharmacodynamic tumor-growth simulator widely adopted in prior work, CDM consistently outperforms state-of-the-art longitudinal causal inference methods, achieving a 15-30% relative improvement in distributional accuracy (1-Wasserstein distance) while maintaining competitive or superior point-estimate accuracy (RMSE) under high-confounding regimes. By unifying uncertainty quantification and robust counterfactual prediction in complex, sequentially confounded settings, without tailored deconfounding, CDM offers a flexible, high-impact tool for decision support in medicine, policy evaluation, and other longitudinal domains.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `t=1,2,\dots,T`

* Equation: `t=1,2,\dots,T`
* Symbols: `t` (time step), `T` (total number of time steps)
* Why it matters: This equation represents the range of time steps considered in the model.

### Equation 2: `X_{i,t}`

* Equation: `X_{i,t}`
* Symbols: `X_{i,t}` (feature vector at time step `t` for individual `i`)
* Why it matters: This equation represents the feature vector observed at time step `t` for individual `i`.

### Equation 3: `A_{i,t}`

* Equation: `A_{i,t}`
* Symbols: `A_{i,t}` (treatment administered at time step `t` for individual `i`)
* Why it matters: This equation represents the treatment administered at time step `t` for individual `i`.

### Equation 4: `Y_{i,t}`

* Equation: `Y_{i,t}`
* Symbols: `Y_{i,t}` (outcome of interest at time step `t` for individual `i`)
* Why it matters: This equation represents the outcome of interest at time step `t` for individual `i`.

### Equation 5: `t_{0}`

* Equation: `t_{0}`
* Symbols: `t_{0}` (baseline time step)
* Why it matters: This equation represents the baseline time step, which is used to define the history of individual `i` up to time `t_{0}`.

**Method Summary**
================

* The Causal Diffusion Model (CDM) is a denoising diffusion probabilistic approach designed to generate full probabilistic distributions of counterfactual outcomes under sequential interventions.
* The model employs a novel residual denoising architecture with relational self-attention, capturing intricate temporal dependencies and multimodal outcome trajectories without requiring explicit adjustments for confounding.
* The model is trained on "factual" patient trajectories and generates counterfactual outcomes by simulating the next time step for each patient under all possible treatment choices.

**Experimental Overview**
=====================

* Tasks: Counterfactual outcome prediction in longitudinal data
* Datasets: Simulated data using the pharmacokinetic-pharmacodynamic (PK-PD) tumor growth simulator
* Baselines: R-MSN, CRN, GNet, and Causal Transformer (CT)
* Main claimed findings: CDM consistently outperforms baselines in terms of distribution fidelity and achieves the lowest Wasserstein distance for every level of confounding.

**What to Verify in the PDF**
==========================

* The details of the PK-PD tumor growth simulator and its simulation procedure.
* The implementation of the Relational Self-Attention (RSA) architecture and its effects on the model's performance.
* The hyperparameter tuning process and the impact of different learning rates and embedding sizes on the model's performance.
{% endraw %}

{% raw %}
## 4) Parcae: Scaling Laws For Stable Looped Language Models
- **Authors:** Hayden Prairie, Zachary Novack, Taylor Berg-Kirkpatrick, Daniel Y. Fu
- **arXiv:** [2604.12946](https://arxiv.org/abs/2604.12946v1) · [pdf](https://arxiv.org/pdf/2604.12946v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.12946v1))
- **Categories:** cs.LG

### Abstract
> Traditional fixed-depth architectures scale quality by increasing training FLOPs, typically through increased parameterization, at the expense of a higher memory footprint, or data. A potential alternative is looped architectures, which instead increase FLOPs by sending activations through a block of layers in a loop. While promising, existing recipes for training looped architectures can be unstable, suffering from residual explosion and loss spikes. We address these challenges by recasting looping as a nonlinear time-variant dynamical system over the residual stream. Via a linear approximation to this system, we find that instability occurs in existing looped architectures as a result of large spectral norms in their injection parameters. To address these instability issues, we propose Parcae, a novel stable, looped architecture that constrains the spectral norm of the injection parameters via discretization of a negative diagonal parameterization. As a result, Parcae achieves up to 6.3% lower validation perplexity over prior large-scale looped models. Using our stable looped architecture, we investigate the scaling properties of looping as a medium to improve quality by increasing FLOPs in training and test-time. For training, we derive predictable power laws to scale FLOPs while keeping parameter count fixed. Our initial scaling laws suggest that looping and data should be increased in tandem, given a fixed FLOP budget. At test-time, we find that Parcae can use looping to scale compute, following a predictable, saturating exponential decay. When scaled up to 1.3B parameters, we find that Parcae improves CORE and Core-Extended quality by 2.99 and 1.18 points when compared to strong Transformer baselines under a fixed parameter and data budget, achieving a relative quality of up to 87.5% a Transformer twice the size.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\overline{\bm{A}}$

* Equation: $\overline{\bm{A}} = W_1$
* Symbols: $\overline{\bm{A}}$, $W_1$
* Why it matters: $\overline{\bm{A}}$ is the linearized version of the injection parameters, which is used to represent the recurrent update rule in the dynamical system.

### Equation 2: $h_t$

* Equation: $h_t$
* Symbols: $h_t$
* Why it matters: $h_t$ represents the state of the recurrent model at time step $t$.

### Equation 3: $h_{t+1} = \overline{\bm{A}}h_t + \overline{\bm{B}}e + \overline{\mathcal{R}}(h_t, e)$

* Equation: $h_{t+1} = \overline{\bm{A}}h_t + \overline{\bm{B}}e + \overline{\mathcal{R}}(h_t, e)$
* Symbols: $h_{t+1}$, $\overline{\bm{A}}$, $\overline{\bm{B}}$, $\overline{\mathcal{R}}$, $h_t$, $e$
* Why it matters: This equation represents the recurrent update rule in the dynamical system, which is a key component of the looped architecture.

### Equation 4: $\overline{\bm{B}}$

* Equation: $\overline{\bm{B}} = W_2$
* Symbols: $\overline{\bm{B}}$, $W_2$
* Why it matters: $\overline{\bm{B}}$ is the linearized version of the embedding parameters, which is used to represent the input to the recurrent update rule.

### Equation 5: $\overline{\mathcal{R}}$

* Equation: $\overline{\mathcal{R}} = \overline{\mathcal{R}}(W_1h_t + W_2e) - (W_1h_t + W_2e)$
* Symbols: $\overline{\mathcal{R}}$, $W_1$, $W_2$, $h_t$, $e$
* Why it matters: $\overline{\mathcal{R}}$ represents the residual term in the recurrent update rule, which is used to capture the non-linear dynamics of the system.

**Method Summary**
==================

* **Stable Training Algorithms for Parcae**: The authors propose a stable training algorithm for Parcae, which involves adjusting the training objective to reduce loss spikes and improve convergence.
* **Per-sequence Depth Sampling**: The authors introduce a per-sequence depth sampling algorithm to stabilize the training process and improve test-time scaling.
* **Discretization of Negative Diagonal Parameterization**: The authors propose discretizing the negative diagonal parameterization to constrain the spectral norm of the injection parameters and improve stability.

**Experimental Overview**
========================

* **Tasks/Datasets**: The authors evaluate Parcae on end-to-end quality, training FLOP scaling, and test-time scaling.
* **Baselines/Comparisons**: The authors compare Parcae to parameter- and data-matched RDMs and Transformers.
* **Main Claimed Findings**: Parcae outperforms both parameter- and data-matched RDMs and Transformers, and achieves predictable power laws for scaling.

**What to Verify in the PDF**
==========================

* **Details of the dynamical system**: The authors mention that the recurrent update rule can be exactly formulated as a non-linear time-variant dynamical system, but the details of this formulation are not provided.
* **Derivation of instability conditions**: The authors mention that instability occurs in existing looped architectures due to large spectral norms in their injection parameters, but the derivation of these conditions is not provided.
* **Details of the per-sequence depth sampling algorithm**: The authors mention that the algorithm is used to stabilize the training process and improve test-time scaling, but the details of the algorithm are not provided.
{% endraw %}

{% raw %}
## 5) Variable Bregman Majorization-Minimization algorithms for nonconvex nonsmooth optimization, with application to Poisson imaging
- **Authors:** Maxence Adly, Alix Chazottes, Emilie Chouzenoux, Jean-Christophe Pesquet, Florent Sureau
- **arXiv:** [2604.12829](https://arxiv.org/abs/2604.12829v1) · [pdf](https://arxiv.org/pdf/2604.12829v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.12829v1))
- **Categories:** math.OC

### Abstract
> In this work, we introduce a unifying Bregman-based majorization-minimization (MM) framework for solving nonconvex nonsmooth optimization problems. The proposed approach leverages Bregman divergences, possibly varying across iterations, to construct tailored surrogate functions that majorize the objective. We establish the convergence of the iterates of the resulting variable Bregman MM algorithm to critical points under the Kurdyka-Lojasiewicz property, relaxing standard assumptions such as the Lipschitz smoothness of the nonconvex objective function. We derive a constructive methodology to build a broad class of variable Bregman majorants with tractable minimizers. Our study encapsulates various existing majorization techniques, in particular those derived for Poisson data fidelity terms in imaging inverse problems. Numerical experiments on Positron Emission Tomography (PET) image reconstruction with a nonconvex regularizer showcase the practical feasibility of the proposed scheme.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\Gamma_{0}(\mathbb{R}^{N})$

* Equation: $\Gamma_{0}(\mathbb{R}^{N})$
* Symbols: $\Gamma_{0}$, $\mathbb{R}^{N}$
* Why it matters: This equation is likely a notation for a function or a set, but its exact meaning is not clear from the context. It may represent a Bregman divergence or a majorization function.

### Equation 2: $f:\mathbb{R}^{N}\to\mathbb{R}\cup\{+\infty\}$

* Equation: $f:\mathbb{R}^{N}\to\mathbb{R}\cup\{+\infty\}$
* Symbols: $f$, $\mathbb{R}^{N}$
* Why it matters: This equation defines a function $f$ that takes a vector in $\mathbb{R}^{N}$ and returns a real value, possibly including infinity. This function is likely the objective function being optimized.

### Equation 3: $\mathbb{R}^{N}$

* Equation: $\mathbb{R}^{N}$
* Symbols: $\mathbb{R}^{N}$
* Why it matters: This equation represents the set of all $N$-dimensional real vectors.

### Equation 4: $f(x)<+\infty$

* Equation: $f(x)<+\infty$
* Symbols: $f$, $x$
* Why it matters: This equation states that the function $f$ takes a value less than infinity at $x$. This is likely a property of the function being optimized.

### Equation 5: $\operatorname{dom}(f)$

* Equation: $\operatorname{dom}(f)$
* Symbols: $\operatorname{dom}$, $f$
* Why it matters: This equation represents the domain of the function $f$, which is the set of all input values for which $f$ is defined.

### Equation 6: $(x,f(x))$

* Equation: $(x,f(x))$
* Symbols: $x$, $f(x)$
* Why it matters: This equation represents a pair consisting of a vector $x$ and the value of the function $f$ at $x$.

### Equation 7: $x\in\mathbb{R}^{N}$

* Equation: $x\in\mathbb{R}^{N}$
* Symbols: $x$, $\mathbb{R}^{N}$
* Why it matters: This equation states that $x$ is an element of the set of all $N$-dimensional real vectors.

### Equation 8: $\operatorname{graph}(f)$

* Equation: $\operatorname{graph}(f)$
* Symbols: $\operatorname{graph}$, $f$
* Why it matters: This equation represents the graph of the function $f$, which is the set of all pairs $(x,f(x))$.

**Method Summary**
================

* The proposed algorithm uses a Bregman majorization-minimization framework to solve nonconvex nonsmooth optimization problems.
* The algorithm iteratively defines the next iterate as the minimizer of a Bregman majorant approximation to the objective function.
* The algorithm is designed to work with a broad class of functions, including those with varying Bregman divergences.
* The algorithm is shown to converge to a single critical point under certain assumptions.

**Experimental Overview**
=====================

* Tasks: The algorithm is tested on a 2D slice of a brain phantom using real PET data.
* Datasets: The algorithm is compared to a baseline (ML-EM) and other majorization-based methods.
* Main claimed findings: The algorithm outperforms the baseline and other methods in terms of detail preservation and contrast in low-dose regions.

**What to Verify in the PDF**
=========================

* The mathematical proof of the convergence result, which relies on the Kurdyka-Łojasiewicz property.
* The construction of the Bregman majorants and their properties.
* The numerical stability of the algorithm, particularly the use of Taylor expansions to evaluate the curvature of the majorants.
{% endraw %}
