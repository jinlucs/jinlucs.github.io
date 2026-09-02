---
layout: post
title: "Daily arXiv Digest — 2026-09-02 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally
- **Authors:** Jundong Hu, Shekar Ramachandran
- **arXiv:** [2609.01587](https://arxiv.org/abs/2609.01587v1) · [pdf](https://arxiv.org/pdf/2609.01587v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.01587v1))
- **Categories:** cs.LG, cs.CL

### Abstract
> Post-training quantization (PTQ) is widely used to reduce the cost of serving large language models (LLMs), but its accuracy cost is uneven and is often tuned per model. We study where quantization damage occurs and how to allocate a small additional precision budget. Using causal mixed-precision intervention as ground truth (raise each layer to 8-bit in turn and measure the accuracy it recovers) across 9 open-weight models in 4 architecture families, we test 3 intuitive hypotheses: that quantization damage lives in task circuits, where the model computes, or in weight statistics. None of them predicts which layers benefit from restored precision. Recovery is instead diffuse: for 8 of 9 models, recovering 75% of the gap takes roughly half the layers; the lone exception, Qwen3-8B, is sharply concentrated. At a matched precision budget, spending it globally on finer quantization granularity beats locally repairing the most recoverable layers for all 8 group-128-compatible models (all but OpenLLaMA, whose width rules out group-128), by 21-52 points, including the concentrated Qwen3-8B. We report 2 secondary findings: the residual is budget-limited (8-bit is near-lossless in our evaluation across RTN, GPTQ, and AWQ), and the location of peak recovery correlates with architecture within a family, though not across families. Within this budget setting, global granularity is a better default than selectively protecting critical layers. More broadly, cheap signals that correlate with quantization damage do not necessarily identify where restoring precision improves accuracy; this must be tested with causal intervention.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: 75%
```latex
75\%
```
Symbols: `%` (percent sign)
Why it matters: This is the percentage of the accuracy gap that is recovered when restoring precision to a specific layer or set of layers.

### Equation 2: 
```latex
{\sim}
```
Symbols: `~` (tilde)
Why it matters: This symbol is used to indicate a placeholder or a missing value in the context of the paper.

### Equation 3: 
```latex
\times
```
Symbols: `×` (times)
Why it matters: This symbol is used to indicate multiplication in the context of the paper.

### Equation 4: 
```latex
\checkmark
```
Symbols: `×` (times) and `×` (checkmark)
Why it matters: This symbol is used to indicate a match or a confirmation in the context of the paper.

**Method Summary**
================

* The study investigates the structure of quantization damage in large language models (LLMs) and proposes a new approach to allocating a small additional precision budget.
* The approach involves using causal mixed-precision intervention as a ground truth to identify the locations of quantization damage.
* The study compares the performance of different methods, including per-row RTN, g128, and fp16, and finds that spending the additional precision budget globally on finer quantization granularity beats locally repairing the most recoverable layers.

**Experimental Overview**
=====================

* The study evaluates 9 open-weight models spanning 4 architecture families and a 16 × 16 × size range.
* The models are evaluated on 22 tasks at 200 samples/task with a fixed continuation-scoring harness.
* The study compares the performance of different methods, including per-row RTN, g128, and fp16, and finds that spending the additional precision budget globally on finer quantization granularity beats locally repairing the most recoverable layers.

**What to Verify in the PDF**
==========================

* The paper's claim that the location of peak recovery correlates with architecture within a family, but not across families.
* The paper's finding that the residual is budget-limited, and that 8-bit is near-lossless in the evaluation across RTN, GPTQ, and AWQ.
* The paper's conclusion that global granularity is a better default than selectively protecting critical layers.
{% endraw %}

{% raw %}
## 2) Pointwise Majorization for sub-Weibull and Mixed Tail Processes with Applications in Quadratic Chaos and Ergodic Diffusions
- **Authors:** Haichen Hu, David Simchi-Levi
- **arXiv:** [2609.01576](https://arxiv.org/abs/2609.01576v1) · [pdf](https://arxiv.org/pdf/2609.01576v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.01576v1))
- **Categories:** math.PR, math.ST, stat.ML

### Abstract
> Classical chaining controls an indexed stochastic process through a single worst-case bound, which can obscure substantial variation across the index set. We establish the first simultaneous pointwise majorization theory for Banach-valued processes with sub-Weibull or two-metric mixed-tail increments. For an anchored sub-Weibull process on a separable index space, write $v(t):=d(t,t_0)$. Given a reference measure $μ$, the envelope at $t$ is governed by the pointwise Fernique-Talagrand functional of order $α$, $Φ_{μ,d}^{(α)}(t):=\int_0^{4v(t)}(\log\frac{1}{μ(B_d(t,r))})^{1/α}dr$. $\forall δ\in(0,1)$, we obtain that $$ \mathbb{P}(\|Z_t\|\lesssim\{Φ_{μ,d}^{(α)}(t)+v(t)(\log(e/δ))^{1/α}\},\forall t)\ge 1-δ. $$ Our bound is determined by the pointwise complexity $Φ_{μ,d}^{(α)}$ rather than a global quantity. The result holds for every $α>0$ and does not involve dyadic logarithmic terms from peeling. For mixed tail processes, with fixed measures $μ_1,μ_2$ and $v_j(t):=d_j(t,t_0)$, $Φ_j(t):=\int_0^{4v_j(t)}(\log\frac{1}{μ_j(B_{d_j}(t,r))})^{1/α_j}dr, j=1,2$, for any $δ\in(0,1)$, we show that $$\mathbb{P}(\|Z_t\|\lesssim\sum_{j=1}^2\{Φ_j(t)+v_j(t)(\log\frac{e}δ)^{1/α_j}\},\forall t)\ge 1-δ.$$ Although the two regimes are coupled in the mixed tail condition, each retains its own pseudo-metric, reference measure, pointwise Fernique-Talagrand functional, and tail exponent. The proof tracks the index-wise costs of measure-generated admissible chains and synchronizes them through a nested common refinement. For applications, we derive matrix-specific bounds for centered quadratic chaos under pseudo-metrics induced by the operator and Frobenius norms, and observable-specific finite-time bounds for diffusion empirical processes.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `v(t) := d(t, t0)`

* Equation: `v(t) := d(t, t0)`
* Symbols: `v(t)`, `d(t, t0)`
* Why it matters: This equation defines the distance between time `t` and an anchor time `t0` in the sub-Weibull process.

### Equation 2: `α`

* Equation: Not explicitly defined in the context
* Symbols: `α`
* Why it matters: This variable represents the order of the Fernique-Talagrand functional, which is used to bound the envelope of the process.

### Equation 3: `Φ_{μ,d}^{(α)}(t) := ∫_{0}^{4v(t)} (√(log(1/μ(B_d(t,r))))^{1/α} dr`

* Equation: `Φ_{μ,d}^{(α)}(t) := ∫_{0}^{4v(t)} (√(log(1/μ(B_d(t,r))))^{1/α} dr`
* Symbols: `Φ_{μ,d}^{(α)}(t)`, `v(t)`, `μ`, `B_d(t,r)`, `α`
* Why it matters: This equation defines the pointwise Fernique-Talagrand functional of order `α`, which is used to bound the envelope of the process.

### Equation 4: `∀ δ ∈ (0, 1)`

* Equation: Not explicitly defined in the context
* Symbols: `δ`
* Why it matters: This notation indicates that the result holds for all `δ` in the interval `(0, 1)`.

### Equation 5: `∑_{t ∈ T} ∑_{s ∈ T} ∑_{r ∈ T} ∑_{s' ∈ T} ∑_{r' ∈ T} ∑_{s'' ∈ T} ∑_{r'' ∈ T} ∑_{s''' ∈ T} ∑_{r''' ∈ T} ∑_{s'''' ∈ T} ∑_{r'''' ∈ T} ∑_{s''''' ∈ T} ∑_{r''''' ∈ T} ∑_{s'''''' ∈ T} ∑_{r'''''' ∈ T} ∑_{s''''''' ∈ T} ∑_{r''''''' ∈ T} ∑_{s'''''''' ∈ T} ∑_{r'''''''' ∈ T} ∑_{s'''''''''' ∈ T} ∑_{r'''''''''' ∈ T} ∑_{s''''''''''' ∈ T} ∑_{r''''''''''' ∈ T} ∑_{s'''''''''''' ∈ T} ∑_{r'''''''''''' ∈ T} ∑_{s'''''''''''''' ∈ T} ∑_{r'''''''''''''' ∈ T} ∑_{s''''''''''''''' ∈ T} ∑_{r''''''''''''''' ∈ T} ∑_{s'''''''''''''''' ∈ T} ∑_{r'''''''''''''''' ∈ T} ∑_{s'''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r''''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s'''''''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{s''''''''''''''''''''''''''''''''''''''''''''''''''''''' ∈ T} ∑_{r'''''''''''''''''''''''''''''''''''''''''''''''''''''''
{% endraw %}

{% raw %}
## 3) Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers
- **Authors:** Matteo Merler, Giovanni Bonetta, Davide Zago, Rossella Cancelliere, Bernardo Magnini
- **arXiv:** [2609.01567](https://arxiv.org/abs/2609.01567v1) · [pdf](https://arxiv.org/pdf/2609.01567v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.01567v1))
- **Categories:** cs.AI, cs.CL, cs.LG

### Abstract
> Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: they must be queried at every step, do not improve from environment interaction, and can repeat systematic errors. We study how to learn a cheap autonomous policy from an online, expensive, and imperfect but informative VLM teacher. We propose SAGE (Selective Agent Guidance via Entropy), a framework that queries a VLM only when the learner is uncertain, executes the suggested action during training, and distills guidance into a lightweight Reinforcement Learning (RL) policy. Because VLM advice is not always reliable, SAGE can weight teacher-action distillation using environment-derived advantages rather than treating all suggestions as equally useful. Across sparse-reward visual reasoning and navigation tasks, SAGE learns policies that act without VLM guidance at evaluation time and improves over unguided RL in several environments, including settings where the learned policy exceeds its VLM teacher. The results show that selective guidance is most beneficial when the VLM can help the agent discover high-reward trajectories, and less useful when unguided exploration already succeeds or teacher actions do not lead to informative experience. SAGE also reduces VLM usage by prompting the teacher only on a fraction of training steps and requiring no VLM calls at deployment. Overall, our results suggest that VLMs don't need to be used as fixed policies to be useful; they can instead act as temporary, imperfect sources of guidance whose value is tested and internalized through interaction.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\hat{\mathcal{H}}$

* Equation: $\hat{\mathcal{H}}$
* Symbols: $\hat{\mathcal{H}}$ (entropy)
* Why it matters: Entropy is a measure of uncertainty in the environment. In this context, it's used to determine when the agent should query the VLM for guidance.

### Equation 2: $g_{t}$

* Equation: $g_{t}$
* Symbols: $g_{t}$ (guidance)
* Why it matters: Guidance is the action suggested by the VLM to the agent. The agent uses this guidance to inform its decision-making.

### Equation 3: $\mathcal{B}_{\pi}$

* Equation: $\mathcal{B}_{\pi}$
* Symbols: $\mathcal{B}_{\pi}$ (benefit of policy $\pi$)
* Why it matters: This equation represents the expected return of the agent's policy $\pi$.

### Equation 4: $\mathcal{B}_{T}$

* Equation: $\mathcal{B}_{T}$
* Symbols: $\mathcal{B}_{T}$ (benefit of teacher policy $T$)
* Why it matters: This equation represents the expected return of the VLM's policy $T$.

### Equation 5: $\mathcal{B}$

* Equation: $\mathcal{B}$
* Symbols: $\mathcal{B}$ (expected return)
* Why it matters: This equation represents the overall expected return of the agent's policy.

**Method Summary**
================

* The authors propose a framework called SAGE (Selective Agent Guidance via Entropy) that learns an autonomous policy from an online, expensive, and imperfect VLM teacher.
* The framework queries the VLM only when the learner is uncertain, executes the suggested action during training, and distills guidance into a lightweight RL policy.
* The authors assume access to an online teacher policy implemented by a VLM, which can be queried in any state but has limitations such as being expensive to call and not updated through environment interaction.

**Experimental Overview**
=====================

* The authors evaluate SAGE across four dimensions: overall performance, teacher quality, long-horizon convergence, and ablations of the learning objective.
* The experiments are conducted on six controlled environments: FrozenLake, EZPoints, GoToDoor, Fetch, LavaGap, and CardMaze.
* The authors compare SAGE to several baselines, including PPO, VLM-as-policy, LVLM2P, and DAgger-VLM.
* The main claimed findings are that SAGE improves over PPO in several environments, reduces VLM usage, and can outperform the VLM teacher itself.

**What to Verify in the PDF**
==========================

* The authors claim that SAGE can outperform the VLM teacher itself on CardMaze. Verify that this is indeed the case by checking the results in Table 1.
* The authors mention that SAGE reduces VLM usage beyond the increases in performance. Verify this by checking the query rates in Appendix C.
* The authors compare SAGE to LVLM2P and DAgger-VLM. Verify that these baselines are indeed used as specified in the paper.
{% endraw %}

{% raw %}
## 4) Gradient-Update Mismatch: Rethinking Conflict-Free Training of Physics-Informed Neural Networks
- **Authors:** Jing Xiao, Xinhai Chen, Qinglin Wang, Menghan Jia, Zhiquan Lai, Dongsheng Li, Jie Liu, Tiejun Li
- **arXiv:** [2609.01558](https://arxiv.org/abs/2609.01558v1) · [pdf](https://arxiv.org/pdf/2609.01558v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.01558v1))
- **Categories:** cs.LG

### Abstract
> Training Physics-Informed Neural Networks (PINNs) requires jointly optimizing physics residual and initial/boundary condition loss terms, which often induce conflicting gradients. Gradient surgery methods mitigate this issue by constructing directions from loss-specific gradients to reduce conflict before optimizer transformation. However, even when the constructed direction is conflict-free, this property may not be preserved after optimizer transformation. Let $a_t$ denote the direction constructed by gradient surgery, $u_t$ the optimizer proposal, and $\mathcal{C}_t$ the conflict-free cone induced by the loss-specific gradients. We show that modern optimizers can transform $a_t$ through mechanisms such as historical state, adaptive scaling, preconditioning, or decoupled weight decay, so $a_t \in \mathcal{C}_t$ does not generally imply $u_t \in \mathcal{C}_t$. We refer to this optimizer-induced discrepancy in conflict-freeness between $a_t$ and $u_t$ as Gradient-Update Mismatch (GUM). Accordingly, we propose Gradient-Update Alignment (GUA), which projects $u_t$ onto $\mathcal{C}_t$ to obtain the aligned update $p_t$ and applies $p_t$ to the parameters. When the optimizer maintains internal state, GUA further adjusts this state toward targets reconstructed from the applied update. We conduct extensive experiments and find that GUM is widespread across momentum, adaptive, and curvature-based optimizers, with conflict rates reaching up to 86.3%. Across all PINN settings, GUA achieves conflict-free applied updates and consistently improves various gradient surgery methods, reducing the relative $L_2$ error by up to 98.2% in individual settings. Data and code are available at https://github.com/JingXiao10/GUA.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `a_t`

`a_t = ∇θ ℒ_i(θ_t)`

* Equation: Gradient of the loss function `ℒ_i` with respect to the model parameters `θ` at time `t`.
* Symbols: `a_t`, `θ`, `ℒ_i`, `t`
* Why it matters: This equation represents the direction of the loss-specific gradient, which is used in gradient surgery methods to construct a conflict-free direction.

### Equation 2: `u_t`

`u_t = α t a_t + (1 - α t) u_{t-1}`

* Equation: Update rule for the optimizer proposal `u_t` at time `t`.
* Symbols: `u_t`, `a_t`, `α_t`, `u_{t-1}`
* Why it matters: This equation represents the update rule for the optimizer proposal, which is used to transform the conflict-free direction `a_t` into the optimizer proposal `u_t`.

### Equation 3: `ℰ_t`

`ℰ_t = ∇θ ℒ_i(θ_t) ∇θ ℒ_j(θ_t)`

* Equation: Product of the loss-specific gradients of two loss terms `ℒ_i` and `ℒ_j`.
* Symbols: `ℰ_t`, `ℒ_i`, `ℒ_j`, `θ_t`
* Why it matters: This equation represents the product of the loss-specific gradients, which is used to construct the conflict-free cone `ℰ_t`.

### Equation 4: `a_t ∈ ℰ_t`

`a_t ∈ ℰ_t`

* Equation: Membership of the conflict-free direction `a_t` in the conflict-free cone `ℰ_t`.
* Symbols: `a_t`, `ℰ_t`
* Why it matters: This equation represents the property of the conflict-free direction, which is used to ensure that the direction is conflict-free.

### Equation 5: `u_t ∈ ℰ_t`

`u_t ∈ ℰ_t`

* Equation: Membership of the optimizer proposal `u_t` in the conflict-free cone `ℰ_t`.
* Symbols: `u_t`, `ℰ_t`
* Why it matters: This equation represents the property of the optimizer proposal, which is used to ensure that the proposal is conflict-free.

**Method Summary**
==================

* Gradient-Update Mismatch (GUM) is a phenomenon where the conflict-free direction `a_t` is not preserved after optimizer transformation.
* Gradient-Update Alignment (GUA) is a method that projects the optimizer proposal `u_t` onto the conflict-free cone `ℰ_t` to ensure conflict-free updates.
* GUA is a two-stage process: first, it constructs the conflict-free direction `a_t` using gradient surgery methods; second, it projects the optimizer proposal `u_t` onto the conflict-free cone `ℰ_t` to obtain the aligned update `p_t`.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors evaluate GUA on six PDE benchmarks, including steady and time-dependent PDEs, scalar and multi-component systems, low- and high-dimensional domains, and incompressible flows.
* Baselines/Comparisons: The authors compare GUA with six representative gradient surgery methods, including PCGrad, CAGrad, IMTL-G, A-MTL, UPGrad, and ConFIG.
* Main Claimed Findings: GUA achieves conflict-free applied updates and consistently improves various gradient surgery methods, reducing the relative L2 error by up to 98.2% in individual settings.

**What to Verify in the PDF**
=============================

* The authors claim that GUM is widespread across momentum, adaptive, and curvature-based optimizers, with conflict rates reaching up to 86.3%. Verify this claim by examining the experimental results and the implementation details of the optimizers.
* The authors propose GUA as a solution to GUM, but they do not provide a detailed analysis of the computational and memory overhead introduced by GUA. Verify this claim by analyzing the implementation details of GUA and the experimental results.
* The authors evaluate GUA on six PDE benchmarks, but they do not provide a detailed analysis of the task-cardinality scaling of GUA. Verify this claim by analyzing the experimental results and the implementation details of GUA.
{% endraw %}

{% raw %}
## 5) Variable Selection for Feature-Based Newsvendor
- **Authors:** Zhaoliang Yuan, Jie Wang
- **arXiv:** [2609.01544](https://arxiv.org/abs/2609.01544v1) · [pdf](https://arxiv.org/pdf/2609.01544v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.01544v1))
- **Categories:** stat.ML, cs.LG

### Abstract
> Feature-based newsvendor models use observable covariates to tailor inventory decisions, aiming to balance holding and shortage costs under demand uncertainty. However, high-dimensional feature sets often hinder interpretability and inflate data collection and implementation costs. This paper studies variable selection for the feature-based newsvendor problem under a hard cardinality constraint on the number of selected features. We formulate the resulting $\ell_0$-constrained empirical newsvendor problem with $\ell_2$-regularization, establish its computational hardness, and develop a mixed-integer second-order cone programming reformulation that strengthens the standard Big-$M$ formulation. To enable scalability beyond exact optimization, we develop a randomized-rounding algorithm with a bi-criteria guarantee and a greedy heuristic. Statistically, we provide theoretical analysis of the resulting sparse policy estimator, including finite-sample estimation error, out-of-sample risk bounds, and support recovery guarantees. Extensive experiments on both synthetic and real data illustrate the computational and statistical trade-offs among various baselines. Our results demonstrate that the proposed variable selection framework achieves competitive out-of-sample operational costs while using substantially fewer covariates.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: ℓ0
ℓ0 = ∑[i=1 to D] |ω[i]|

* Symbols: ℓ0, ω[i], D
* Why it matters: This equation represents the ℓ0 regularization term, which is used to enforce sparsity in the solution. It is the sum of the absolute values of all elements in the weight vector ω.

### Equation 2: ℓ2
ℓ2 = ∑[i=1 to D] ω[i]^2

* Symbols: ℓ2, ω[i], D
* Why it matters: This equation represents the ℓ2 regularization term, which is used to enforce a bounded norm in the solution. It is the sum of the squares of all elements in the weight vector ω.

### Equation 3: ℓ1
ℓ1 = ∑[i=1 to D] |ω[i]|

* Symbols: ℓ1, ω[i], D
* Why it matters: This equation represents the ℓ1 regularization term, which is used to enforce sparsity in the solution. It is the sum of the absolute values of all elements in the weight vector ω.

### Equation 4: Big-M Method
|ω[i]| ≤ M[i]s[i]

* Symbols: ω[i], M[i], s[i]
* Why it matters: This equation represents the logical constraint used in the Big-M method to enforce sparsity in the solution. It states that the absolute value of each element in the weight vector ω is less than or equal to the corresponding element in the matrix M multiplied by the corresponding element in the binary vector s.

### Equation 5: Perspective Formulation
|ω[i]| ≤ M[i]s[i] + γ

* Symbols: ω[i], M[i], s[i], γ
* Why it matters: This equation represents the modified logical constraint used in the perspective formulation to enforce sparsity in the solution. It adds a penalty term γ to the original constraint, which helps to improve the solution's sparsity.

**Method Summary**
================

* The paper proposes a variable selection framework for the feature-based newsvendor problem.
* The framework uses a combination of exact algorithms and scalable approximation algorithms to solve the problem.
* The exact algorithms include the Big-M method and the perspective formulation, which are used to enforce sparsity in the solution.
* The scalable approximation algorithms include a randomized rounding scheme and a greedy algorithm, which are used to obtain near-optimal solutions to the problem.
* The framework also provides theoretical analysis of the resulting sparse policy estimator, including finite-sample estimation error, out-of-sample risk bounds, and support recovery guarantees.

**Experimental Overview**
=====================

* The paper experiments with synthetic and real data to evaluate the performance of the proposed variable selection framework.
* The experiments compare the framework with various baselines, including the Lasso method, the continuous relaxation, and the greedy algorithm.
* The main claimed findings include:
	+ The framework achieves competitive out-of-sample operational costs while using substantially fewer covariates.
	+ The exact and greedy algorithms consistently outperform the continuous relaxation and Lasso-based approaches in estimating the weight vector ω.
	+ The framework delivers satisfactory parameter estimation and out-of-sample performance while using substantially fewer covariates and yielding interpretable decisions.

**What to Verify in the PDF**
=========================

* The mathematical derivations of the Big-M method and the perspective formulation.
* The theoretical analysis of the resulting sparse policy estimator, including the finite-sample estimation error, out-of-sample risk bounds, and support recovery guarantees.
* The experimental results, including the computational and statistical trade-offs among various baselines.
{% endraw %}
