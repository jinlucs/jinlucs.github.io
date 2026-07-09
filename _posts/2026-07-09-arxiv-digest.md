---
layout: post
title: "Daily arXiv Digest — 2026-07-09 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) The Key to Going Linear: Analysis-Driven Transformer Linearization
- **Authors:** Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi
- **arXiv:** [2607.07706](https://arxiv.org/abs/2607.07706v1) · [pdf](https://arxiv.org/pdf/2607.07706v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.07706v1))
- **Categories:** cs.LG

### Abstract
> The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of approximation errors and introduce structural interventions, specifically sink tokens, short convolutions, and fixed-budget cache routing, which reduces the remaining gap. We scale this linearization approach across LLaMA and Qwen models up to 32B parameters, outperforming prior post hoc baselines on MMLU and matching the long-context retrieval of complex adaptive-caching frameworks.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: W_{q}
```math
W_{q}
```
Symbols: `W_{q}`, `q`
Why it matters: This equation represents the query weights in the transformer model.

### Equation 2: W_{k}
```math
W_{k}
```
Symbols: `W_{k}`, `k`
Why it matters: This equation represents the key weights in the transformer model.

### Equation 3: W_{v}
```math
W_{v}
```
Symbols: `W_{v}`, `v`
Why it matters: This equation represents the value weights in the transformer model.

### Equation 4: \varphi
```math
\varphi
```
Symbols: `\varphi`
Why it matters: This equation represents the softmax function used in the transformer model.

### Equation 5: \alpha_{i}
```math
\alpha_{i}
```
Symbols: `\alpha_{i}`, `i`
Why it matters: This equation represents the attention weights in the transformer model.

**Method Summary**
==================

* The authors propose an analysis-driven transformer linearization approach to reduce the quadratic cost of causal self-attention.
* The approach involves identifying the effect of state update design in a strict frozen-backbone regime and introducing structural interventions to reduce the remaining gap.
* The authors use sink tokens, short convolutions, and fixed-budget cache routing to achieve this goal.
* The approach is evaluated on LLaMA and Qwen models up to 32B parameters and compared to prior post hoc baselines.

**Experimental Overview**
========================

* Tasks/Datasets: The authors evaluate their approach on the DCLM-Edu dataset for 10M tokens.
* Baselines/Comparisons: The authors compare their approach to prior post hoc baselines, including LoLCaT and Liger-GLA.
* Main Claimed Findings: The authors claim that their approach outperforms prior baselines on MMLU and matches the long-context retrieval of complex adaptive-caching frameworks.

**What to Verify in the PDF**
=============================

* The authors mention that training Hedgehog takes approximately 8 hours due to the absence of a Triton implementation. It would be interesting to verify this claim and understand the implications of this limitation.
* The authors also mention that the state-based mechanisms (GLA/kGLA/GDN) substantially outperform the kernelized Hedgehog replacement. It would be interesting to verify this claim and understand the underlying reasons for this difference.
* The authors propose adding short convolutions to enhance representational capacity. It would be interesting to verify the effectiveness of this addition and understand its impact on the overall performance of the model.
{% endraw %}

{% raw %}
## 2) Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF
- **Authors:** Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay
- **arXiv:** [2607.07693](https://arxiv.org/abs/2607.07693v1) · [pdf](https://arxiv.org/pdf/2607.07693v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.07693v1))
- **Categories:** cs.LG, cs.AI, cs.CV

### Abstract
> Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that substantially improve the feedback efficiency of diffusion RLHF while preserving generalization to unseen prompts. Our key observation is that reward information in diffusion trajectories is unevenly distributed: not all denoising timesteps or trajectories contribute equally to learning from a reward signal. By emphasizing informative timesteps and trajectories during optimization, we obtain more effective gradient updates. First, we introduce a per-timestep weighting scheme that reweights denoising steps during policy optimization. We theoretically connect this weighting to the optimal convergence properties of proximal policy optimization (PPO) and approximate the resulting weighting trend empirically. Second, we introduce a replay mechanism that prioritizes informative trajectories, enabling the model to reuse past samples instead of repeatedly querying new rewards. Together, these strategies significantly improve the feedback efficiency of diffusion RLHF. Under identical hyperparameter settings, our approach achieves up to a 6$\times$ improvement in sample efficiency compared to widely used diffusion RLHF baselines.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 6 ×
```markdown
6 ×
```
* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: ×
```markdown
×
```
* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 3: (S,A,P,R,γ)
```markdown
(S,A,P,R,γ)
```
* Equation: Not explicitly defined in the context.
* Symbols:
	+ S: State
	+ A: Action
	+ P: Policy
	+ R: Reward
	+ γ: Discount factor
* Why it matters: Represents a common reinforcement learning setting.

### Equation 4: P(s^{\prime}|s,a)
```markdown
P(s^{\prime}|s,a)
```
* Equation: Not explicitly defined in the context.
* Symbols:
	+ P: Probability
	+ s^{\prime}: Next state
	+ s: Current state
	+ a: Action
* Why it matters: Represents the policy's probability of transitioning from one state to another given an action.

### Equation 5: s^{\prime}
```markdown
s^{\prime}
```
* Equation: Not explicitly defined in the context.
* Symbols:
	+ s^{\prime}: Next state
* Why it matters: Represents the next state in a sequence.

### Equation 6: R(s,a)
```markdown
R(s,a)
```
* Equation: Not explicitly defined in the context.
* Symbols:
	+ R: Reward
	+ s: State
	+ a: Action
* Why it matters: Represents the reward received for taking an action in a state.

### Equation 7: γ
```markdown
γ
```
* Equation: Not explicitly defined in the context.
* Symbols:
	+ γ: Discount factor
* Why it matters: Represents the discount factor used in reinforcement learning.

**Method Summary**
==================

* The proposed method combines selective timestep weighting and advantage-based replay to improve the feedback efficiency of diffusion RLHF.
* The method addresses the credit assignment problem by introducing a timestep-dependent weighting scheme.
* The method also introduces a replay mechanism that prioritizes informative trajectories.
* The proposed method is highly applicable to existing diffusion RLHF frameworks.

**Experimental Overview**
========================

* Tasks/Datasets: The proposed method is tested on 5 reward functions, including JPEG compressibility, JPEG incompressibility, aesthetic score, HPS v2, and image reward.
* Baselines/Comparisons: The proposed method is compared to existing diffusion RLHF baselines, including DDPO, DPOK, and B2-DiffuRL.
* Main Claimed Findings: The proposed method achieves up to a 6 × 6 × improvement in sample efficiency compared to existing diffusion RLHF baselines.

**What to Verify in the PDF**
=============================

* The mathematical derivation of the timestep-dependent weighting scheme.
* The empirical results for the different reward functions.
* The analysis of the replay mechanism's impact on sample efficiency.
{% endraw %}

{% raw %}
## 3) Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning
- **Authors:** Vladislav Beliaev
- **arXiv:** [2607.07690](https://arxiv.org/abs/2607.07690v1) · [pdf](https://arxiv.org/pdf/2607.07690v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.07690v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating roles, one drafts a solution and the other reads it while solving, and each is rewarded for out-solving the other. To win, a model must out-reason a rival that has seen its work, so reasoning is judged implicitly during training, with no process labels and no reward model. Because both models are optimized, each faces a progressively stronger rival, which single-model RL cannot provide. The two need only be comparably strong and behaviorally different. At inference the pair deploys as it trains, a two-stage cascade in which one model drafts and the other answers after reading the draft. On the hard split of DeepMath with Qwen3, this doubles GRPO's pass@1, roughly eight times the gain of an untrained Mixture-of-Agents pass over the same base. The ordering replicates on competitive-programming code and across model families (Qwen3.5, Gemma 4). For now the models talk in text; the next step is to let them reason together in latent space.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 2 ×

* Equation: 2 ×
* Symbols: None explicitly mentioned
* Why it matters: Not explicitly mentioned in the context, but it seems to be a placeholder for a formula that will be explained later.

### Equation 2: 1.8 ×

* Equation: 1.8 ×
* Symbols: None explicitly mentioned
* Why it matters: Not explicitly mentioned in the context, but it seems to be a placeholder for a formula that will be explained later.

### Equation 3: ≈ 2%

* Equation: ≈ 2%
* Symbols: ≈
* Why it matters: This equation is mentioned in the context of comparing the performance of Agon and GRPO. The ≈ symbol indicates that the value is an approximation.

### Equation 4: 2 × 2

* Equation: 2 × 2
* Symbols: ×
* Why it matters: This equation is mentioned in the context of comparing the performance of Agon and GRPO. The × symbol indicates multiplication.

### Equation 5: ×

* Equation: ×
* Symbols: ×
* Why it matters: This equation is mentioned in the context of defining the reward function r(x,y) ∈ {0,1}. The × symbol indicates multiplication.

**Method Summary**
==================

* Agon trains two policies, A and B, head-to-head on the same problems.
* The design has four parts: a draft-and-challenge rollout, a competitive reward, a compute-parity accounting, and an efficient instantiation of the two policies as divergent adapters over a shared base.
* Post-training RL is self-improvement, where the gradient is computed from rollouts produced by the policy itself.
* The two policies are optimized to face a progressively stronger rival, which single-model RL cannot provide.

**Experimental Overview**
==========================

* Tasks/Datasets: DeepMath-103K (difficulty 8, binary-answer questions removed)
* Baselines/Comparisons:
	+ Vanilla GRPO
	+ Untrained MoA control
	+ Self-refinement
	+ Cooperative exchange
	+ Competition
* Main Claimed Findings:
	+ Agon lifts GRPO by +31 pp, roughly eight times the gain of untrained MoA control.
	+ Agon reaches roughly twice vanilla GRPO's held-out pass@1 while shortening final-stage traces.

**What to Verify in the PDF**
=============================

* The implementation details of the two-stage cascade and the competitive reward.
* The theoretical justification for the compute-parity accounting and the efficient instantiation of the two policies as divergent adapters.
* The results of the second-domain study on CodeContests and the implications for the performance of Agon on different domains.
{% endraw %}

{% raw %}
## 4) Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization
- **Authors:** Xiangming Huang, Guannan Zhang, Lu Lu, Raphaël Pestourie
- **arXiv:** [2607.07682](https://arxiv.org/abs/2607.07682v1) · [pdf](https://arxiv.org/pdf/2607.07682v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.07682v1))
- **Categories:** cs.LG

### Abstract
> The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust but struggle in high-dimensional spaces. This paper introduces a Neural Operator-enabled Topology-informed Evolutionary Strategy (NOTES) that integrates dimensionality reduction, representation learning, and evolutionary optimization for efficient and transferable inverse design. NOTES couples a DeepONet-based neural operator with the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to perform global optimization in a compact latent space that encodes topology-aware priors while discovering high-performance designs for unseen operating conditions. Applied to nanophotonic beam-deflector inverse design governed by Maxwell's equations, NOTES reduces the design dimensionality from 256 to 25 and consistently achieves over 95 percent efficiency, outperforming CMA-ES, topology optimization, and other baselines. Applied to structural optimization, NOTES discovers designs that achieve compliance down to 246. By decoupling topology learning of a DeepONet from the governing physics in a PDE solver, NOTES provides a flexible and transferable framework for the inverse design of physical systems.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: \(\lambda\)

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: \(\theta\)

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 3: \(\displaystyle\min_{\mathbf{v}\in\mathcal{C}}-\mathrm{FOM}(\mathbf{x};\mathbf{v})\quad\text{s.t.}\quad\mathcal{F}(\mathbf{x};\mathbf{v})=0\)

* Equation: Not found in extracted context.
* Symbols:
	+ \(\mathbf{v}\): design variable
	+ \(\mathcal{C}\): feasible space
	+ \(\mathrm{FOM}\): figure of merit
	+ \(\mathbf{x}\): PDE solution
	+ \(\mathcal{F}\): PDE operator
* Why it matters: This equation represents the optimization problem for inverse design, where the goal is to minimize the negative of the figure of merit while satisfying the PDE constraints.

### Equation 4: \(\mathrm{FOM}\)

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 5: \(\mathcal{F}\)

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 6: \(\mathcal{C}\)

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 7: \(\mathbf{x}\)

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 8: \(\mathbf{v}\)

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

**Method Summary**
==================

* The proposed framework, NOTES, integrates dimensionality reduction, representation learning, and evolutionary optimization for efficient and transferable inverse design.
* NOTES couples a DeepONet-based neural operator with the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to perform global optimization in a compact latent space that encodes topology-aware priors.
* The framework is applied to two PDE-constrained inverse design applications with fundamentally different governing physics and geometric structures.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Nanophotonic beam-deflector inverse design governed by Maxwell's equations.
	+ Structural optimization.
* Baselines/Comparisons:
	+ Topology optimization.
	+ GLOnet.
	+ CMA-ES.
	+ L-BFGS + DeepONet.
* Main Claimed Findings:
	+ NOTES consistently achieves over 95% efficiency in the nanophotonic application.
	+ NOTES discovers designs that achieve compliance down to 246 in the structural optimization application.

**What to Verify in the PDF**
=============================

* The mathematical formulation of the DeepONet-based neural operator and its coupling with CMA-ES.
* The implementation details of the Meent PDE solver used to evaluate the objective.
* The results of the principal components analysis (PCA) on the generated designs to understand the aspect ratio distribution.
{% endraw %}

{% raw %}
## 5) Does Bielik Know What It Doesn't Know? Activation Dispersion Separates Entity Familiarity from Factual Reliability Across Model Scale
- **Authors:** Grzegorz Brzezinka
- **arXiv:** [2607.07670](https://arxiv.org/abs/2607.07670v1) · [pdf](https://arxiv.org/pdf/2607.07670v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.07670v1))
- **Categories:** cs.CL, cs.LG

### Abstract
> Large language models hallucinate most about entities they have never seen. We ask whether a model's activations betray entity familiarity before a single answer token is generated, and whether that signal predicts the factual reliability of the answers. On four Polish Bielik models (1.5B-11B parameters), we probe four entity domains (athletes, cities, writers, musicians), each with 42 well-known, 42 obscure-but-real, and 42 fabricated entities addressed by a one-sentence question (504 prompts per model). Two unsupervised, single-forward-pass dispersion measures over post-SwiGLU MLP activations, inverse participation ratio and spectral entropy, separate known from fabricated entities at AUROC 0.95-1.00 across all domains and scales; a supervised linear probe reaches 0.99-1.00. Both clear selection-aware permutation floors of about 0.70-0.74 (empirical p<=1e-3), survive held-out layer selection (0.93-0.99), and persist on real names (known vs. obscure-but-real: 0.96-1.00). The signal transfers across entity types (mean off-diagonal AUROC 0.92-0.99); a matched-template counterfactual shows the only large drops are template-caused, not entity-type effects, and the signal is diffuse across heads. This representational signal is already at ceiling at 1.5B, whereas behavioral factual reliability scales sharply: 0, 2, 10, and 19 of 42 known athletes are answered fully correctly by the 1.5B, 4.5B, 7B, and 11B models under a strict judge. Within known entities, separating correct from hallucinated answers is much harder (probe 0.93; dispersion no better than a first-token-entropy baseline). A five-sample semantic-entropy baseline reaches only 0.71-0.83 at 5x the inference cost. Despite this internal awareness, the models almost never abstain: an audit of 2,520 answers finds 2 refusals and 1 hedge. Entity familiarity and factual reliability are distinct phenomena on different scaling curves.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: p ≤ 10^(-3)

* Equation: p ≤ 10^(-3)
* Symbols: p (probability)
* Why it matters: This equation represents the empirical p-value, which is used to determine the significance of the observed effect. A p-value of 10^(-3) or lower indicates that the observed effect is statistically significant.

### Equation 2: ≈

* Equation: ≈
* Symbols: ≈ (approximation symbol)
* Why it matters: This equation represents the approximation of the activation dispersion measures. The ≈ symbol indicates that the measures are approximating the true dispersion values.

### Equation 3: →

* Equation: →
* Symbols: → (arrow symbol)
* Why it matters: This equation represents the direction of the relationship between entity familiarity and factual reliability. The arrow symbol indicates that the relationship is directional, with entity familiarity leading to factual reliability.

**Method Summary**
==================

* The authors construct a dataset in four entity domains (athletes, cities, writers, and musicians) with 126 entities per domain and 504 prompts per model.
* The authors train four Polish Bielik models with 1.5B, 4.5B, 7B, and 11B parameters.
* The authors use two unsupervised dispersion measures (inverse participation ratio and spectral entropy) and a supervised linear probe to evaluate the model's ability to separate known from fabricated entities.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors use a dataset with 504 prompts per model, each with 42 well-known, 42 obscure-but-real, and 42 fabricated entities.
* Baselines/Comparisons: The authors compare their results with a first-token-entropy baseline and a five-sample semantic-entropy baseline.
* Main Claimed Findings: The authors claim that the unsupervised dispersion measures and the supervised linear probe can separate known from fabricated entities with high accuracy, and that the signal is diffuse rather than carried by a small fixed set of heads.

**What to Verify in the PDF**
=============================

* The authors report that the behavioral factual reliability scales sharply with model size, but the representational awareness does not improve with scale. Verify that this is true for all four entity domains.
* The authors report that the models almost never hold back, but the authors do not provide a clear explanation for this phenomenon. Verify that the authors provide a clear explanation for why the models do not hold back.
* The authors report that the signal transfers across entity types, but the authors do not provide a clear explanation for why this is the case. Verify that the authors provide a clear explanation for why the signal is able to transfer across entity types.
{% endraw %}
