---
layout: post
title: "Daily arXiv Digest — 2026-07-01 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) AdaJEPA: An Adaptive Latent World Model
- **Authors:** Ying Wang, Oumayma Bounou, Yann LeCun, Mengye Ren
- **arXiv:** [2606.32026](https://arxiv.org/abs/2606.32026v1) · [pdf](https://arxiv.org/pdf/2606.32026v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.32026v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes the first action chunk, uses the observed next-state transition as a self-supervised adaptation signal, and replans with the updated model. This closed-loop update continuously recalibrates the world model without additional expert demonstrations. Across a range of goal-reaching tasks, AdaJEPA substantially improves planning success with as few as one gradient step per MPC replanning step.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1. Formula Walkthrough**
### Equation 1: a_{t}
\[ a_{t} \]
Symbols: \( a_{t} \) (action at time t)
Why it matters: This equation represents the action taken at time t by the model.

### Equation 2: o_{t+1}
\[ o_{t+1} \]
Symbols: \( o_{t+1} \) (observation at time t+1)
Why it matters: This equation represents the observation at time t+1, which is used to update the model.

### Equation 3: \{o_{t},a_{t},o_{t+1}\}
\[ \{o_{t},a_{t},o_{t+1}\} \]
Symbols: \( \{o_{t},a_{t},o_{t+1}\} \) (tuple of observation, action, and next observation)
Why it matters: This equation represents the data used to update the model, consisting of the observation at time t, the action taken at time t, and the next observation.

### Equation 4: o_{t} \in \mathbb{R}^{n_{o}}
\[ o_{t} \in \mathbb{R}^{n_{o}} \]
Symbols: \( o_{t} \) (observation at time t), \( n_{o} \) (dimensionality of observation space)
Why it matters: This equation specifies the dimensionality of the observation space, which is used to represent the observation at time t.

### Equation 5: a_{t} \in \mathbb{R}^{n_{a}}
\[ a_{t} \in \mathbb{R}^{n_{a}} \]
Symbols: \( a_{t} \) (action at time t), \( n_{a} \) (dimensionality of action space)
Why it matters: This equation specifies the dimensionality of the action space, which is used to represent the action taken at time t.

**2. Method Summary**
* AdaJEPA is an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC).
* The model consists of an encoder and a predictor, which are trained jointly by minimizing a latent prediction objective over reward-free offline trajectories.
* The model adapts to the test environment by replanning with the updated model after each execution, using the observed next-state transition as a self-supervised adaptation signal.
* The adaptation process is performed with a single gradient step per MPC replanning step, and the model is updated using a replay buffer.

**3. Experimental Overview**
* Tasks/Datasets: PushT and PointMaze benchmarks
* Baselines/Comparisons: Frozen model, MPC planner with JEPAs, and other baselines
* Main Claimed Findings: AdaJEPA improves planning performance on unseen in-distribution and out-of-distribution test environments, with significant gains in robustness to visual and layout shifts.

**4. What to Verify in the PDF**
* Details on the data generation process for the PushT and PointMaze benchmarks, including the specific shapes and layouts used for training and testing.
* The mathematical formulation of the latent prediction objective used to train the JEPAs, including the specific loss function and optimization algorithm used.
* The implementation details of the MPC planner, including the specific MPC algorithm used and the hyperparameters tuned for each experiment.
{% endraw %}

{% raw %}
## 2) SemRF: A Semantic Reference Frame for Residual-Stream Dynamics in Language Models
- **Authors:** Jian Gu, Aldeida Aleti, Chunyang Chen, Hongyu Zhang
- **arXiv:** [2606.32022](https://arxiv.org/abs/2606.32022v1) · [pdf](https://arxiv.org/pdf/2606.32022v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.32022v1))
- **Categories:** cs.LG, cs.CL

### Abstract
> Residual-stream analysis asks how language-model computation evolves across depth, but intermediate decoding requires comparable readout coordinates across layers. If embedding anchors and unembedding readout disagree on the chosen span, apparent motion may reflect measurement drift rather than computation. We introduce \emph{Semantic Reference Frames} (SemRF), an anchor-based formalism separating semantic measurement from residual dynamics. A SemRF fixes anchors and measures states against them. Pseudo-inverse tying gives exact synchronization; under restricted bi-invertibility, SemRF yields stable semantic-basis coordinates, distortion bounds, and near-identity changes. With the frame fixed, residual computation becomes a depthwise semantic trajectory. The anchors induce a semantic Voronoi diagram: distance, or evidence such as logits, assigns each layer to a coarse cell, while coordinates retain within-cell motion and margins. We define layerwise steps, contribution profiles, and imbalance diagnostics, then use the Voronoi trace to define a margin-relaxed tube. The canonical trace is the minimum-action path inside this tube; when nonempty with positive quadratic weight, it is unique and obeys a discrete spline equation away from active constraints. Excess action controls step, curvature, and profile mismatch. Low curvature implies piecewise-linear compressibility and local knowledge density: lower trace complexity means fewer semantic knots. Through the parameter-to-trajectory map, this gives a conditional link to parameter efficiency: among admissible settings fitting data, lower-action and lower-complexity traces use fewer semantic degrees of freedom. The guarantees require controlled interface error and small projection residual under explicit tube constraints.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\theta\mapsto z_{0:L}(x;\theta)$

* Equation: $\theta\mapsto z_{0:L}(x;\theta)$
* Symbols: $\theta$ (model parameters), $z_{0:L}(x;\theta)$ (output)
* Why it matters: This equation represents the output of the model as a function of the input $x$ and model parameters $\theta$.

### Equation 2: $h_{\ell,t}\in\mathbb{R}^{d}$

* Equation: $h_{\ell,t}\in\mathbb{R}^{d}$
* Symbols: $h_{\ell,t}$ (hidden state), $d$ (dimensionality)
* Why it matters: This equation represents the hidden state of the model at layer $\ell$ and time step $t$.

### Equation 3: $\ell\in\{0,\dots,L\}$

* Equation: $\ell\in\{0,\dots,L\}$
* Symbols: $\ell$ (layer index), $L$ (number of layers)
* Why it matters: This equation represents the layer index, which ranges from 0 to $L$.

### Equation 4: $h_{\ell+1,t}=h_{\ell,t}+u_{\ell,t}(h_{\ell,t})$

* Equation: $h_{\ell+1,t}=h_{\ell,t}+u_{\ell,t}(h_{\ell,t})$
* Symbols: $h_{\ell+1,t}$ (hidden state at next layer), $h_{\ell,t}$ (hidden state at current layer), $u_{\ell,t}(h_{\ell,t})$ (update function)
* Why it matters: This equation represents the update rule for the hidden state at the next layer, which is a function of the current hidden state.

### Equation 5: $\Delta h_{\ell,t}:=u_{\ell,t}(h_{\ell,t})$

* Equation: $\Delta h_{\ell,t}:=u_{\ell,t}(h_{\ell,t})$
* Symbols: $\Delta h_{\ell,t}$ (change in hidden state), $u_{\ell,t}(h_{\ell,t})$ (update function)
* Why it matters: This equation represents the change in the hidden state at the current layer, which is a function of the current hidden state.

**Method Summary**
================

* **Semantic Reference Frames (SemRF)**: An anchor-based formalism for separating measurement from dynamics in language models.
* **Restricted bi-invertibility**: A structural assumption that ensures stable semantic coordinates and explicit distortion bounds.
* **Pseudo-inverse tying**: A technique that supplies an exact anchor-synchronization case.
* **Semantic Voronoi diagram**: A diagram that assigns each layer to a coarse cell based on semantic distance.

**Experimental Overview**
=====================

* **Tasks/Datasets**: Not specified in the provided context.
* **Baselines/Comparisons**: Not specified in the provided context.
* **Main Claimed Findings**: SemRF provides a stable semantic-basis coordinates, distortion bounds, and controlled near-identity frame changes, which enables a depthwise semantic trajectory.

**What to Verify in the PDF**
==========================

* **Detailed explanation of the pseudo-inverse tying technique**: Understand how this technique supplies an exact anchor-synchronization case.
* **Derivation of the distortion bounds**: Verify the mathematical derivation of the distortion bounds and their implications.
* **Experimental results**: Review the experimental results to understand how SemRF compares to other methods in terms of semantic motion and computation.
{% endraw %}

{% raw %}
## 3) TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning
- **Authors:** Yuanda Xu, Zhengze Zhou, Hejian Sang, Xiaomin Li, Jiaxin Zhang, Xinchen Du, Zhipeng Wang, Alborz Geramifard
- **arXiv:** [2606.32017](https://arxiv.org/abs/2606.32017v1) · [pdf](https://arxiv.org/pdf/2606.32017v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.32017v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Agentic reinforcement learning requires assigning credit to environment-facing actions such as searches, clicks, edits, navigation commands, and object interactions. Standard GRPO uses the final verifier outcome as a uniform advantage over all action tokens. This outcome signal is useful but structurally incomplete: it punishes useful exploration in failed rollouts and reinforces redundant or regressive actions in successful rollouts. We propose TRIAGE, a role-typed credit assignment framework that adds a semantic role axis to outcome credit. A structured judge classifies each segment as decisive progress, useful exploration, no-progress infrastructure, or regression, and a fixed role-conditioned rule maps these labels to bounded segment-level process rewards. This keeps verifier outcomes as the source of optimization direction while correcting the two main blind spots of outcome-only credit. We further show that role-conditioned credit is the optimal segment-level correction expressible from role labels alone -- a projection of the per-segment advantage residual onto the role variable -- so that the fixed role constants reduce advantage estimation error whenever the judge is reliable, and we connect this to lower-variance policy gradients. Across ALFWorld, Search-QA, and WebShop, TRIAGE improves success rates over GRPO for two policy models and outperforms both a scalar judge-derived process reward and an outcome-supervised shared-backbone value baseline. Ablations show that the gain comes from role typing rather than merely adding dense rewards: reliable detection of regression inside successful trajectories is the dominant contributor, while exploration credit provides a consistent secondary gain; on completed ALFWorld and WebShop rollouts, TRIAGE also reduces environment-facing turns by an additional $10.4\%$ and $14.8\%$ relative to GRPO.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `10.4%`

* Equation: `10.4%`
* Symbols: `%` (percentage symbol)
* Why it matters: This is the relative reduction in environment-facing turns by TRIAGE compared to GRPO in ALFWorld and WebShop.

### Equation 2: `14.8%`

* Equation: `14.8%`
* Symbols: `%` (percentage symbol)
* Why it matters: This is the relative reduction in environment-facing turns by TRIAGE compared to GRPO in ALFWorld and WebShop.

### Equation 3: `r_{i}=V(\tau_{i})\in\{0,1\}`

* Equation: `r_{i}=V(\tau_{i})\in\{0,1\}`
* Symbols: `r_{i}`, `V`, `\tau_{i}`, `{0,1}`
* Why it matters: This equation defines the verifier reward `r_{i}` as a binary value (0 or 1) based on the outcome of the trajectory `V(\tau_{i})`.

### Equation 4: `A_{i}^{\mathrm{GRPO}}=(r_{i}-\bar{r})/(\sigma_{r}+\epsilon)`

* Equation: `A_{i}^{\mathrm{GRPO}}=(r_{i}-\bar{r})/(\sigma_{r}+\epsilon)`
* Symbols: `A_{i}^{\mathrm{GRPO}}`, `r_{i}`, `\bar{r}`, `\sigma_{r}`, `\epsilon`
* Why it matters: This equation defines the group-normalized advantage `A_{i}^{\mathrm{GRPO}}` assigned by GRPO to each segment of the trajectory.

### Equation 5: `r_{i}\in\{0,1\}`

* Equation: `r_{i}\in\{0,1\}`
* Symbols: `r_{i}`
* Why it matters: This equation defines the verifier reward `r_{i}` as a binary value (0 or 1) for use in calculating the group-normalized advantage.

**Method Summary**
==================

* TRIAGE proposes a role-typed credit assignment framework for agentic reinforcement learning.
* The framework adds a semantic role axis to outcome credit, using a structured judge to classify each segment as decisive progress, useful exploration, no-progress infrastructure, or regression.
* The role-conditioned rule maps these labels to bounded segment-level process rewards.
* TRIAGE improves success rates over GRPO for two policy models and outperforms both a scalar judge-derived process reward and an outcome-supervised shared-backbone value baseline.

**Experimental Overview**
=========================

* Tasks/Datasets: ALFWorld, Search-QA, and WebShop.
* Baselines/Comparisons: GRPO, scalar judge-derived process reward, and outcome-supervised shared-backbone value baseline.
* Main Claimed Findings: TRIAGE improves success rates over GRPO and outperforms baselines in all three environments.

**What to Verify in the PDF**
=============================

* The role-conditioned rule and how it maps labels to process rewards.
* The reliability of the structured judge and its impact on the performance of TRIAGE.
* The theoretical justification for the optimal segment-level correction expressible from role labels alone.
{% endraw %}

{% raw %}
## 4) Freeform Preference Learning for Robotic Manipulation
- **Authors:** Marcel Torne, Anubha Mahajan, Abhijnya Bhat, Chelsea Finn
- **arXiv:** [2606.32027](https://arxiv.org/abs/2606.32027v1) · [pdf](https://arxiv.org/pdf/2606.32027v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.32027v1))
- **Categories:** cs.RO, cs.AI, cs.LG

### Abstract
> Reward design remains a central bottleneck for autonomous robot policy improvement, especially in long-horizon manipulation tasks where sparse success labels provide too little signal and binary preferences collapse many competing notions of quality into one ambiguous signal. We introduce Freeform Preference Learning (FPL), a method for learning robot policies from freeform human preferences. Rather than asking annotators which of two trajectories is better overall, FPL lets them define natural-language preference axes, such as speed, safety, quality of placement, or carefulness, and provide pairwise preferences along each axis. These annotations are used to learn a language-conditioned reward model that maps a trajectory and preference label to an axis-specific reward. We use this model to train a reward-conditioned policy that optimizes across the multiple human-specified dimensions. Across four real-world and two simulated long-horizon manipulation tasks, FPL improves over sparse-reward and binary-preference methods by 38 percentage points. Beyond improved performance, FPL learns dense progress signals without explicit subtask segmentation, shows compositionality of behavior not present in the data, and allows users to steer the policy towards different behaviors at test time without retraining. Blog post with videos available at https://freeform-pl.github.io/fpl.website/
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $(s_{i},s_{j})$

* Equation: $(s_{i},s_{j})$
* Symbols: $s_{i}$ and $s_{j}$ (states)
* Why it matters: This equation represents the interaction between two states in the environment.

### Equation 2: $y\in\{0,1\}$

* Equation: $y\in\{0,1\}$
* Symbols: $y$ (label)
* Why it matters: This equation represents the binary label assigned to a state, indicating whether it is a success or failure.

### Equation 3: $s_{i}$

* Equation: $s_{i}$
* Symbols: $s_{i}$ (state)
* Why it matters: This equation represents a single state in the environment.

### Equation 4: $s_{j}$

* Equation: $s_{j}$
* Symbols: $s_{j}$ (state)
* Why it matters: This equation represents another single state in the environment.

### Equation 5: $\mathcal{P}$

* Equation: $\mathcal{P}$
* Symbols: $\mathcal{P}$ (policy)
* Why it matters: This equation represents the policy learned by the algorithm.

**Method Summary**
==================

* The authors propose Freeform Preference Learning (FPL), a method for learning robot policies from freeform human preferences.
* FPL allows humans to define natural-language preference axes and provide pairwise preferences along each axis.
* The algorithm learns a language-conditioned reward model that maps a trajectory and preference label to an axis-specific reward.
* The reward model is used to train a reward-conditioned policy that optimizes across multiple human-specified dimensions.

**Experimental Overview**
========================

* The authors evaluate FPL on four real-world manipulation tasks and two simulated long-horizon manipulation tasks.
* The tasks are:
	+ Real-world: Put cube into target bowl, Fold shorts, Plate toast, Set up the table
	+ Simulation: Two tasks with varying levels of complexity
* The authors compare FPL to five baselines:
	+ Single Preferences
	+ Advantage Conditioning
	+ Weighted Regression
	+ Filtered BC
	+ BC
* The main claimed findings are:
	+ FPL improves over sparse-reward and binary-preference methods by 38 percentage points.
	+ FPL learns dense progress signals without explicit subtask segmentation.
	+ FPL exhibits steerability of rewards at test time.

**What to Verify in the PDF**
=============================

* The authors claim that FPL learns performant policies from freeform human preferences. Verify this claim by examining the results of the experiments.
* The authors mention that FPL provides axis-specific supervision, allowing the policy to improve both task completion and qualitative aspects of behavior. Verify this claim by examining the reward models learned by FPL.
* The authors mention that FPL allows users to steer the policy towards different behaviors at test time without retraining. Verify this claim by examining the results of the experiments.
{% endraw %}

{% raw %}
## 5) PolicyGuard: From Organizational Policies to Neuro-SymbolicCompliance Review Engines
- **Authors:** Sameer Malik, Ayush Singh, Amar Prakash Azad
- **arXiv:** [2606.32004](https://arxiv.org/abs/2606.32004v1) · [pdf](https://arxiv.org/pdf/2606.32004v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.32004v1))
- **Categories:** cs.AI, cs.LG, cs.LO, cs.SC

### Abstract
> Policy-grounded document review requires determining whether a target document complies with organization-specific policies, guidelines, or playbooks. While large language models can assist with policy interpretation and document analysis, end-to-end prompting leaves the applied policy logic implicit, making compliance decisions difficult to inspect, update, and test. We present PolicyGuard, a neuro-symbolic framework for policy-grounded document compliance review. PolicyGuard converts organizational policy guidance into an executable review engine consisting of typed relational logic rules and atom-level extraction questions. During review, LLMs answer these local questions using retrieved document evidence, and a symbolic evaluator applies the formal rules to detect non-compliance. We instantiate and evaluate PolicyGuard on company-specific NDA compliance review, where contract clauses must be checked against organization-specific negotiation policies. By separating policy formalization, local document interpretation, and symbolic compliance evaluation, PolicyGuard makes document review more explicit, maintainable, and systematically testable.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Precision-Recall Analysis by Contract

Equation:
\[
\mathrm{pass}^k = \mathbb{E}_{\mathrm{task}}\left[\frac{\binom{c}{k}}{\binom{n}{k}}\right]
\]

Symbols:
- $\mathrm{pass}^k$: probability of correct pass at $k$-th step
- $\mathbb{E}_{\mathrm{task}}$: expected value over the task
- $c$: number of correct predictions
- $n$: total number of predictions
- $\binom{c}{k}$: number of combinations of $c$ items taken $k$ at a time
- $\binom{n}{k}$: number of combinations of $n$ items taken $k$ at a time

Why it matters: This equation calculates the expected probability of correct pass at each step, which is used to evaluate the performance of the model.

### Equation 2: Precision-Recall Analysis by Contract (continued)

Not found in extracted context.

### Equation 3: Precision-Recall Analysis by Contract (continued)

Not found in extracted context.

### Equation 4: Precision-Recall Analysis by Contract (continued)

Not found in extracted context.

### Equation 5: Precision-Recall Analysis by Contract (continued)

Not found in extracted context.

### Equation 6: Precision-Recall Analysis by Contract (continued)

Not found in extracted context.

### Equation 7: Precision-Recall Analysis by Contract (continued)

Not found in extracted context.

### Equation 8: Precision-Recall Analysis by Contract (continued)

Not found in extracted context.

**Method Summary**
==================

* PolicyGuard is a neuro-symbolic framework that converts organizational policy guidance into an executable review engine.
* The framework consists of typed relational logic rules and atom-level extraction questions.
* PolicyGuard uses large language models to answer local questions and a symbolic evaluator to apply formal rules and detect non-compliance.
* The framework separates policy formalization, local document interpretation, and symbolic compliance evaluation, making document review more explicit, maintainable, and systematically testable.

**Experimental Overview**
=========================

* Tasks/Datasets: Company-specific NDA compliance review using 95 guidelines from an internal playbook and five NDA contracts.
* Baselines/Comparisons: Four zero-shot prompting baselines (Direct Prompting, Chain-of-Thought, Legal Reasoning, and Legal Syllogism) and a Majority Class baseline.
* Main Claimed Findings: PolicyGuard substantially outperforms all zero-shot baselines, improving non-compliance-class F1 by 30.8 points over the best prompting method.

**What to Verify in the PDF**
=============================

* The detailed implementation of the PolicyGuard framework, including the typed relational logic rules and atom-level extraction questions.
* The evaluation of the framework on a larger dataset and with more diverse policies and contracts.
* The analysis of the impact of the symbolic layer on auditability and the potential for human-in-the-loop refinement.
{% endraw %}
