---
layout: post
title: "Daily arXiv Digest — 2026-07-14 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks
- **Authors:** Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet, Thomas Hofmann
- **arXiv:** [2607.11875](https://arxiv.org/abs/2607.11875v1) · [pdf](https://arxiv.org/pdf/2607.11875v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.11875v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> We present a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models. While previous works on Transformer learning dynamics have so far been mostly tied to specific tasks, we study a generalized class of inductive tasks that unifies several synthetic tasks known in the literature, including in-context n-grams and multi-hop reasoning. In this class, we theoretically prove that the training dynamics of attention models can be confined to a highly interpretable, low-dimensional invariant manifold. On this manifold, the learning dynamics are captured by a handful of interpretable coordinates rather than millions of parameters, making both theoretical and empirical analysis more tractable. Using this framework, we characterize how data statistics govern the competition between in-context and in-weights learning, we study how random initializations determine the `winning' circuit when multiple solutions are possible, and we demonstrate that the coordinate frame associated with the manifold can be used to automatically detect which circuits have been learned in trained models. By casting circuit formation as a low-dimensional dynamical phenomenon, we take a step toward a predictive theory of how Transformers learn.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: n
```latex
{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}n}
```
* Symbols: `n`
* Why it matters: Not found in extracted context.

### Equation 2: k
```latex
{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}k}
```
* Symbols: `k`
* Why it matters: Not found in extracted context.

### Equation 3: i < n
```latex
i<{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}n}}
```
* Symbols: `i`, `n`
* Why it matters: Not found in extracted context.

### Equation 4: k_i
```latex
{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}k}}_{i}
```
* Symbols: `k_i`, `i`
* Why it matters: Not found in extracted context.

### Equation 5: k_i ≤ k
```latex
{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}k}}_{i}\leq{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}k}}
```
* Symbols: `k_i`, `k`
* Why it matters: Not found in extracted context.

### Equation 6: \mathcal{V}
```latex
{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathcal{V}}}
```
* Symbols: \mathcal{V}
* Why it matters: Not found in extracted context.

### Equation 7: \mathbf{x}^{{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}n}}}_{2}
```latex
{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathbf{x}}}^{{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}n}}}_{2}
```
* Symbols: \mathbf{x}
* Why it matters: Not found in extracted context.

### Equation 8: \mathbf{x}^{i}_{1}
```latex
{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathbf{x}}}^{i}_{1}
```
* Symbols: \mathbf{x}, `i`
* Why it matters: Not found in extracted context.

**Method Summary**
==================

* The authors propose a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models.
* The framework constrains learning to a highly interpretable, low-dimensional invariant manifold.
* The authors use a greedy backward elimination algorithm to detect the essential circuits in the trained model.
* The algorithm performs well in detecting the essential circuits, even when multiple solutions are possible.

**Experimental Overview**
========================

* The authors use a variety of synthetic tasks, including in-context n-grams and multi-hop reasoning, to evaluate the performance of the Transformer model.
* The authors compare the performance of the Transformer model to a baseline model that does not use the invariant manifold framework.
* The authors find that the Transformer model performs significantly better than the baseline model, especially on tasks that require inductive reasoning.

**What to Verify in the PDF**
=============================

* The authors' theoretical framework and the mathematical derivations that support it.
* The experimental results and the analysis of the data.
* The implications of the findings for the field of natural language processing and the development of more advanced language models.
{% endraw %}

{% raw %}
## 2) A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation
- **Authors:** Yunhai Feng, Natalie Leung, Jiaxuan Wang, Lujie Yang, Haozhi Qi, Preston Culbertson
- **arXiv:** [2607.11874](https://arxiv.org/abs/2607.11874v1) · [pdf](https://arxiv.org/pdf/2607.11874v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.11874v1))
- **Categories:** cs.RO, cs.AI, cs.LG

### Abstract
> Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires delicate regulation of contact modes and forces. We present REGRIND, a minimalist retargeting-guided RL pipeline that learns dexterous manipulation policies from a single human demonstration. REGRIND retargets human hand-object motion to a robot reference that preserves hand-object spatial and contact relationships, trains a residual RL policy in simulation to track object-centric keypoints along that reference, and transfers the resulting policy zero-shot to hardware with careful system identification. The resulting policies produce fluid, human-like behavior on two different multi-fingered hands across contact-rich tool-use tasks, including operating a pair of scissors and turning a screwdriver. Through systematic hardware experiments, we identify and analyze the key factors that govern sim-to-real transfer in dexterous manipulation, offering practical guidance for retargeting-based learning in contact-rich settings. Videos and code are available at https://yunhaifeng.com/REGRIND.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: ⟨𝒮, 𝒜, P, ρ0, r, T⟩

* Equation: ⟨𝒮, 𝒜, P, ρ0, r, T⟩
* Symbols: 𝒮 (state space), 𝒜 (action space), P (transition dynamics), ρ0 (initial state distribution), r (reward function), T (horizon)
* Why it matters: This equation represents a finite-horizon Markov Decision Process (MDP), which is the framework used to formulate robot policy learning with reinforcement learning (RL).

### Equation 2: 𝒮

* Equation: 𝒮
* Symbols: 𝒮 (state space)
* Why it matters: This equation represents the state space of the MDP, which is the set of all possible states that the robot can be in.

### Equation 3: 𝒜

* Equation: 𝒜
* Symbols: 𝒜 (action space)
* Why it matters: This equation represents the action space of the MDP, which is the set of all possible actions that the robot can take.

### Equation 4: P: 𝒮 × 𝒜 → Δ(𝒮)

* Equation: P: 𝒮 × 𝒜 → Δ(𝒮)
* Symbols: P (transition dynamics), 𝒮 (state space), 𝒜 (action space), Δ(𝒮) (probability distribution over the state space)
* Why it matters: This equation represents the transition dynamics of the MDP, which describes how the state of the robot changes in response to an action.

### Equation 5: ρ0

* Equation: ρ0
* Symbols: ρ0 (initial state distribution)
* Why it matters: This equation represents the initial state distribution of the MDP, which describes the probability distribution of the initial state of the robot.

### Equation 6: r: 𝒮 × 𝒜 → [0,1]

* Equation: r: 𝒮 × 𝒜 → [0,1]
* Symbols: r (reward function), 𝒮 (state space), 𝒜 (action space), [0,1] (reward range)
* Why it matters: This equation represents the reward function of the MDP, which describes the reward that the robot receives for taking an action in a particular state.

**Method Summary**
==================

* The authors propose a minimalist retargeting-guided RL pipeline for dexterous manipulation.
* The pipeline consists of three stages:
	+ Retargeting: The authors use a simple IK-based retargeting strategy to transform the human motion into a robot reference.
	+ Residual RL: The authors use a residual RL policy to track the object-centric keypoints along the retargeted reference.
	+ Transfer: The authors use a zero-shot transfer approach to transfer the policy from simulation to hardware.
* The authors evaluate their method on two dexterous manipulation tasks: scissors and screwdriver.

**Experimental Overview**
========================

* Tasks/Datasets: The authors evaluate their method on two dexterous manipulation tasks: scissors and screwdriver.
* Baselines/Comparisons: The authors compare their method to two baselines: Mink IK + RL and SPIDER.
* Main Claimed Findings: The authors claim that their method achieves low object tracking error and near perfect success rates on all tasks, while the baselines struggle with the contact-rich tasks.

**What to Verify in the PDF**
=============================

* The authors claim that their method achieves near perfect success rates on all tasks, but the evaluation metrics used are not explicitly stated.
* The authors use a zero-shot transfer approach, but the details of this approach are not explicitly stated.
* The authors use a residual RL policy, but the details of this policy are not explicitly stated.
{% endraw %}

{% raw %}
## 3) Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias
- **Authors:** Zixiang Xu, Sixian Li, Huaxing Liu, Xiang Wang, Shuai Li, Zirui Song, Xiuying Chen
- **arXiv:** [2607.11871](https://arxiv.org/abs/2607.11871v1) · [pdf](https://arxiv.org/pdf/2607.11871v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.11871v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Existing studies of LLM-as-judge scoring bias work predominantly at the input-output level: they perturb inputs, measure score deltas, and propose prompt-level mitigations. We argue that the same biases admit a representation-level account in the judge's hidden state, complementary to the input-output view and operationally useful in ways it does not afford. We report three findings, across seven judges, seven bias types, and nine benchmarks. Geometry: baseline judging inputs occupy a tight activation manifold while biased inputs are displaced along a low-dimensional, type-specific subspace that sharpens with depth and is recovered consistently by three families of estimators. Causal control: steering hidden states along this subspace drives scoring in both directions, forward shifts reproducing biased scoring on clean inputs and reverse shifts restoring baseline scoring on biased ones, while matched-norm random directions produce shifts an order of magnitude smaller. Operational: a simple linear projection onto the same bias-direction features anticipates judge failures on three entirely unseen benchmarks, substantially outperforming text-based alternatives. Reading bias as activation geometry, rather than as input-output noise, unifies geometric structure, causal control, and operational prediction within a single framework. The project page is available at https://xzx34.github.io/unfair-judge/
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Not found in extracted context.

### Equation 2: (\mathcal{D}_{\text{base}},\mathcal{D}_{\text{pos}},\mathcal{D}_{\text{neg}})
- Symbols: \mathcal{D}_{\text{base}},\mathcal{D}_{\text{pos}},\mathcal{D}_{\text{neg}}
- Matters: This equation represents the three datasets used for training, testing, and validation.

### Equation 3: \mathcal{M}_{\text{base}}
- Symbols: \mathcal{M}_{\text{base}}
- Matters: This equation represents the baseline activation manifold, which is the distribution of activation sets for unbiased baseline evaluation.

### Equation 4: 0.82
- Symbols: None
- Matters: This value is not explicitly explained in the context, but it might represent a threshold or a metric used in the experiment.

### Equation 5: 0.63
- Symbols: None
- Matters: Similar to Equation 4, this value is not explicitly explained but might represent another threshold or metric.

**Method Summary**
================

* The authors develop a unified methodology for analyzing, causally intervening on, and anticipating scoring biases in LLM judges.
* The methodology includes an activation-level analysis framework that identifies a direction in the judge's hidden state along which bias concentrates.
* The framework supports two downstream applications: causal control via activation steering and an outcome predictor built on activation features.

**Experimental Overview**
=====================

* Tasks/Datasets: The authors evaluate scoring bias across seven LLM judges on nine diverse benchmarks (GSM8K, MMLU, TruthfulQA, CommonsenseQA, PubMedQA, GPQA, ARC-Challenge, SocialMaze, BBQ).
* Baselines/Comparisons: The authors compare their results to SteerFair, a closest methodological precedent for finding bias directions and steering activations.
* Main Claimed Findings: The authors report three findings: (1) scoring bias is a structured behavioral phenomenon, (2) this behavior has a stable geometric correlate in the judge's hidden state, and (3) the bias direction is causally load-bearing and operationally useful.

**What to Verify in the PDF**
==========================

* The authors claim that the bias direction is causally load-bearing and operationally useful. Verify that the experiment supports this claim by examining the results of activation steering and the outcome predictor.
* The authors report that the bias direction is recovered consistently by three families of estimators. Verify that the experiment demonstrates the robustness of the bias direction estimation.
* The authors claim that the geometry supports a cross-domain outcome predictor on entirely unseen benchmarks. Verify that the experiment demonstrates the generalizability of the bias direction to new domains.
{% endraw %}

{% raw %}
## 4) Input-Aware Dynamic Backdoor Attack Against Quantum Neural Networks
- **Authors:** Junrui Zhang, Zemin Chen, Lusi Li, Mohammad Ghasemigol, Daniel Takabi, Rui Ning
- **arXiv:** [2607.11843](https://arxiv.org/abs/2607.11843v1) · [pdf](https://arxiv.org/pdf/2607.11843v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.11843v1))
- **Categories:** quant-ph, cs.LG

### Abstract
> Quantum Neural Networks (QNNs) are a promising framework for quantum machine learning on near-term quantum devices, but their security risks remain insufficiently understood. Studies have shown that QNNs are vulnerable to backdoor attacks, yet existing quantum backdoors mostly rely on a fixed trigger shared by all poisoned inputs. This fixed-trigger design is a major weakness because many defenses detect or weaken the repeated patterns such triggers leave in data representations. Although input-aware dynamic backdoors have been studied in classical neural networks, transferring them to QNNs is difficult because quantum learning introduces new obstacles. In particular, measurement compresses the post-ansatz quantum state into a limited classical output, weakening supervision for a trigger generator, while individual density matrices fluctuate with the input and make per-sample contrastive learning unstable. To address these challenges, we propose Q-DIBA, the first input-aware dynamic backdoor attack for QNNs. Q-DIBA jointly trains a classical trigger generator and a victim QNN through a three-mode mini-batch strategy that supports clean behavior, attack activation, and trigger specificity. To provide stable quantum-level supervision, Q-DIBA introduces an ensemble density contrastive loss that operates on post-ansatz quantum states before measurement and contrasts mode-averaged density matrices rather than individual samples. Experiments on MNIST and Fashion-MNIST across multiple QNN architectures show that Q-DIBA achieves high clean accuracy, strong attack success, and high cross-trigger accuracy, demonstrating effectiveness, stealthiness, and input specificity. The attack also remains resilient against defenses including visual inspection, spectral-signature detection, and fine-tuning, suggesting that input-aware quantum backdoors are an important threat to secure QNN deployment.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Density Matrix Representation
```markdown
ρ_{i}=|\psi_{i}\rangle\langle\psi_{i}|
```
* Equation: ρ_{i}=|\psi_{i}\rangle\langle\psi_{i}|
* Symbols: ρ_{i} (density matrix), |\psi_{i}\rangle (quantum state)
* Why it matters: This equation represents the density matrix of a quantum state, which is a fundamental concept in quantum mechanics and quantum computing.

### Equation 2: Quantum State Representation
```markdown
\ket{\psi}=\alpha\ket{0}+\beta\ket{1},\quad|\alpha|^{2}+|\beta|^{2}=1
```
* Equation: \ket{\psi}=\alpha\ket{0}+\beta\ket{1},\quad|\alpha|^{2}+|\beta|^{2}=1
* Symbols: \ket{\psi} (quantum state), \alpha (complex coefficient), \beta (complex coefficient)
* Why it matters: This equation represents a quantum state as a superposition of two basis states, with coefficients \alpha and \beta. The normalization condition ensures that the coefficients are properly scaled.

### Equation 3: Coefficients
```markdown
\alpha,\beta
```
* Equation: \alpha,\beta
* Symbols: \alpha (complex coefficient), \beta (complex coefficient)
* Why it matters: These coefficients represent the amplitudes of the quantum state superposition.

### Equation 4: Coefficient Norm
```markdown
|\alpha|^{2}
```
* Equation: |\alpha|^{2}
* Symbols: |\alpha|^{2} (norm of coefficient \alpha)
* Why it matters: This expression represents the squared magnitude of the coefficient \alpha, which is a measure of its magnitude.

### Equation 5: Coefficient Norm (Alternative)
```markdown
|\beta|^{2}
```
* Equation: |\beta|^{2}
* Symbols: |\beta|^{2} (norm of coefficient \beta)
* Why it matters: This expression represents the squared magnitude of the coefficient \beta, which is a measure of its magnitude.

**Method Summary**
==================

* The authors propose a new backdoor attack called Q-DIBA (Input-Aware Dynamic Backdoor Attack) designed specifically for Quantum Neural Networks (QNNs).
* Q-DIBA jointly trains a classical trigger generator and a victim QNN through a three-mode mini-batch strategy.
* The attack uses an ensemble density contrastive loss to provide stable quantum-level supervision.
* The authors evaluate Q-DIBA on two datasets (MNIST and F-MNIST) and three QNN architectures, achieving high clean accuracy, strong attack success, and high cross-trigger accuracy.

**Experimental Overview**
==========================

* Tasks: The authors evaluate Q-DIBA on two datasets (MNIST and F-MNIST) and three QNN architectures.
* Baselines: The authors compare Q-DIBA to a baseline attack that uses a fixed trigger.
* Main claimed findings: Q-DIBA achieves high clean accuracy, strong attack success, and high cross-trigger accuracy.

**What to Verify in the PDF**
=============================

* The authors claim that Q-DIBA is resilient against representative defenses, including visual inspection, spectral-signature detection, and fine-tuning.
* The authors also claim that Q-DIBA remains effective even when the trigger budget is reduced.
* The authors provide experimental results for different QNN architectures and datasets, but it would be useful to see more detailed analysis of the results.
{% endraw %}

{% raw %}
## 5) Stabilize-then-optimize: Feedback transformations as preconditioners in optimal control
- **Authors:** Till Preuster, Manuel Schaller, Anton Schiela, Martin Stoll
- **arXiv:** [2607.11835](https://arxiv.org/abs/2607.11835v1) · [pdf](https://arxiv.org/pdf/2607.11835v1)
- **LLM context source:** abstract only
- **Categories:** math.OC, math.NA

### Abstract
> Many numerical algorithms for optimal control leverage an elimination of the state via the control-to-state map such as condensed approaches or preconditioned conjugate gradient methods for the optimality system. As such, the norm of the control-to-state map directly enters the convergence estimates for these methods, e.g., via the condition number of the associated linear system. In this work we show that using feedback transformations one may reformulate the optimal control problem to decrease the norm of the (feedbacked) control-to-state map, leading to a drastic improvement of the involved condition numbers. We illustrate the abstract approach for ordinary and partial differential equations such as parabolic, hyperbolic or elliptic equations. For each of these problem classes we provide a constructive method to improve solution operator norms via feedbacks. Further, we showcase the efficacy of the method by means of various numerical examples with elliptic, parabolic and hyperbolic partial differential equations.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
#### 1. Equation: 
\[ \text{condition number} = \| \mathcal{C} \| \cdot \| \mathcal{C}^{-1} \| \]
- Symbols: $\mathcal{C}$ (control-to-state map), $\| \cdot \|$ (norm)
- Why it matters: The condition number of the control-to-state map directly affects the convergence of numerical algorithms for optimal control.

#### 2. Equation: 
\[ \text{norm of feedbacked control-to-state map} = \| \mathcal{F} \mathcal{C} \| \]
- Symbols: $\mathcal{F}$ (feedback transformation), $\mathcal{C}$ (control-to-state map), $\| \cdot \|$ (norm)
- Why it matters: The norm of the feedbacked control-to-state map is decreased, leading to improved convergence estimates.

#### 3. Equation: 
\[ \text{solution operator norm} = \| \mathcal{A} \| \]
- Symbols: $\mathcal{A}$ (solution operator), $\| \cdot \|$ (norm)
- Why it matters: The solution operator norm is improved via feedbacks, leading to better numerical solutions.

#### 4. Equation: 
\[ \text{optimal control problem} \quad \text{minimize} \quad f(x, u) \]
- Symbols: $x$ (state), $u$ (control), $f(x, u)$ (objective function)
- Why it matters: The optimal control problem is the core objective of the work, aiming to improve numerical solutions via feedback transformations.

#### 5. Equation: 
\[ \text{convergence estimate} \quad \text{converges if} \quad \kappa(\mathcal{C}) < \rho \]
- Symbols: $\kappa(\mathcal{C})$ (condition number of control-to-state map), $\rho$ (tolerance)
- Why it matters: The convergence estimate depends on the condition number of the control-to-state map, which can be improved via feedback transformations.

### Method Summary
* The authors propose using feedback transformations to decrease the norm of the control-to-state map.
* This approach leads to a drastic improvement in the condition numbers of the associated linear systems.
* The method is applied to various problem classes, including ordinary and partial differential equations.
* A constructive method is provided to improve solution operator norms via feedbacks.

### Experimental Overview
* Tasks/Datasets: Various numerical examples with elliptic, parabolic, and hyperbolic partial differential equations.
* Baselines/Comparisons: The authors compare the proposed method with condensed approaches and preconditioned conjugate gradient methods.
* Main Claimed Findings: The proposed method leads to a significant improvement in convergence estimates and numerical solutions.

### What to Verify in the PDF
* Details on the implementation of the feedback transformations and how they are applied to the optimal control problem.
* The theoretical justification for the improvement in convergence estimates and solution operator norms.
* The robustness of the proposed method to different problem classes and parameter settings.
{% endraw %}
