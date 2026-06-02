---
layout: post
title: "Daily arXiv Digest — 2026-06-02 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) A No-Regret Framework for Adaptive Incentive Design
- **Authors:** Georgios Vasileiou, Lantian Zhang, Silun Zhang
- **arXiv:** [2606.02529](https://arxiv.org/abs/2606.02529v1) · [pdf](https://arxiv.org/pdf/2606.02529v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.02529v1))
- **Categories:** math.OC, cs.GT, cs.MA, eess.SY

### Abstract
> Incentive design studies how a central authority can influence strategic agents through payments, subsidies, or taxes, so that individual objectives align with collective welfare. This paper introduces a No-Regret Adaptive Incentive Design (RAID) framework for nonlinear games with continuous action spaces and private agent costs. In this framework, the authority (planner) designs incentives that regulate the Nash equilibrium toward a socially optimal action profile, while simultaneously learning agents' unknown preferences from repeated strategic responses. We formulate the RAID problem and construct a least-squares estimator whose strong consistency requires only diminishing excitation. Leveraging this weak excitation requirement, we propose a switching incentive policy that alternates between probing (exploration) and estimate-based (exploitation) incentives. The resulting policy achieves an $O(t^{-0.5})$ parameter estimation rate and accumulates $O(t^{0.5}\log t)$ squared social-cost regret, almost surely. We further extend the framework to an endogenous-noise response model, where standard least-squares estimation is biased due to an error-in-variables correlation between the noise and agent responses. We utilize a repeated-sampling estimator and corresponding switching policy that retain the same almost-sure convergence and regret rates. Numerical experiments validate the effectiveness and predicted convergence rates of the method.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: O(t^{-0.5})

* Equation: O(t^{-0.5})
* Symbols: O, t
* Why it matters: This equation represents the parameter estimation rate of the switching incentive policy. The O notation indicates the rate of convergence, and the exponent -0.5 indicates that the policy achieves a sublinear convergence rate.

### Equation 2: O(t^{0.5}\log t)

* Equation: O(t^{0.5}\log t)
* Symbols: O, t
* Why it matters: This equation represents the squared social-cost regret accumulated by the switching incentive policy. The O notation indicates the rate of convergence, and the exponent 0.5 and the logarithmic term indicate that the policy achieves a sublinear convergence rate with a logarithmic factor.

### Equation 3: n\in\mathbb{N}

* Equation: n\in\mathbb{N}
* Symbols: n
* Why it matters: This equation represents the set of natural numbers, which is used to index the agents in the incentivized game.

### Equation 4: [n]=\{1,2,\ldots,n\}

* Equation: [n]=\{1,2,\ldots,n\}
* Symbols: [n], \{1,2,\ldots,n\}
* Why it matters: This equation represents the set of indices for the agents in the incentivized game. The square brackets indicate that the set contains the integers from 1 to n.

### Equation 5: x\in\mathbb{R}^{n}

* Equation: x\in\mathbb{R}^{n}
* Symbols: x, \mathbb{R}^{n}
* Why it matters: This equation represents the set of all n-dimensional real vectors, which is used to index the strategies of the agents in the incentivized game.

### Equation 6: \|x\|_{2}

* Equation: \|x\|_{2}
* Symbols: x, \|\cdot\|_{2}
* Why it matters: This equation represents the Euclidean norm of the vector x, which is used to measure the length of the vector.

**Method Summary**
==================

* The authors propose a No-Regret Adaptive Incentive Design (RAID) framework for nonlinear games with continuous action spaces and private agent costs.
* The framework consists of a least-squares estimator that learns the agents' marginal nominal costs and a switching incentive policy that alternates between probing and estimate-based incentives.
* The policy achieves an O(t^{-0.5}) parameter estimation rate and accumulates O(t^{0.5}\log t) squared social-cost regret, almost surely.
* The authors extend the framework to an endogenous-noise response model, where standard least-squares estimation is biased due to an error-in-variables correlation between the noise and agent responses.

**Experimental Overview**
=========================

* The authors conduct numerical experiments to validate the effectiveness and predicted convergence rates of the method.
* The experiments involve a set of agents playing a nonlinear game with continuous action spaces and private agent costs.
* The authors compare the performance of the RAID framework with a baseline policy that uses a fixed incentive.
* The main claimed findings are that the RAID framework achieves a faster parameter estimation rate and accumulates less squared social-cost regret than the baseline policy.

**What to Verify in the PDF**
=============================

* The authors claim that the least-squares estimator is strongly consistent, but the proof is not provided in the abstract.
* The authors also claim that the switching incentive policy achieves an O(t^{-0.5}) parameter estimation rate, but the proof is not provided in the abstract.
* The authors mention that the policy accumulates O(t^{0.5}\log t) squared social-cost regret, but the proof is not provided in the abstract.
* The authors also mention that the framework can be extended to an endogenous-noise response model, but the proof is not provided in the abstract.
{% endraw %}

{% raw %}
## 2) IntraShuffler: A Privacy Preserving Framework for Heterogeneous DP Federated Learning
- **Authors:** Farhin Farhad Riya, Olivera Kotevska, Jinyuan Stella Sun
- **arXiv:** [2606.02563](https://arxiv.org/abs/2606.02563v1) · [pdf](https://arxiv.org/pdf/2606.02563v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.02563v1))
- **Categories:** cs.LG, cs.CR, cs.DC

### Abstract
> Heterogeneous Differential Privacy (HDP) in Federated Learning (FL) allows clients to select individual privacy budgets ($\varepsilon_i$) according to institutional policies and data sensitivity. In practice, many HDP-FL systems employ $\varepsilon$-aware server aggregation to improve model utility by re-weighting client updates according to their declared privacy budgets. However, gradient updates in FL retain structural patterns induced by non-independent and identically-distributed (non-IID) data, and these additional signals exposed by $\varepsilon$-aware aggregation create new opportunities for inference by an honest-but-curious server. In this work, we first show that a server equipped with gradient denoising and surrogate modeling can mount a \emph{Privacy Inference Attack} that infers distributional attributes of clients and links updates from the same client across training rounds, measured via surrogate inference accuracy and linkage success, under realistic knowledge constraints. The Shuffle-Model has been widely studied as a defense against such inference risks by anonymizing update sources, but it is fundamentally incompatible with HDP-FL $\varepsilon$-aware aggregation. To address this challenge, we propose \textbf{IntraShuffler}, a middleware defense framework designed for HDP-FL systems. IntraShuffler introduces a privacy-aware shuffling mechanism that groups clients into privacy-compatible buckets and performs parameter-level shuffling within each bucket to disrupt persistent gradient structure while preserving $\varepsilon$-aware aggregation. Experiments across four different datasets show that IntraShuffler reduces gradient recoverability by over 60% and decreases surrogate inference accuracy from 0.78 to 0.33 while maintaining comparable model utility across multiple FL aggregation rules.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Privacy Budget
```markdown
\varepsilon_{i}
```
* Equation: Not explicitly defined in the context.
* Symbols: εi, which represents the privacy budget for client i.
* Why it matters: The privacy budget is a crucial parameter in Heterogeneous Differential Privacy (HDP) that determines the level of noise added to client updates.

### Equation 2: Privacy Budget (continued)
```markdown
\varepsilon
```
* Equation: Not explicitly defined in the context.
* Symbols: ε, which represents the overall privacy budget for the entire system.
* Why it matters: The overall privacy budget is used to determine the level of noise added to client updates and is a key parameter in HDP.

### Equation 3: Denoising Loss
```markdown
\ell_{2}
```
* Equation: Not explicitly defined in the context.
* Symbols: ℓ2, which represents the L2 loss function.
* Why it matters: The L2 loss function is used to train the ε-aware learned denoiser fθ(g, ε).

### Equation 4: Cosine Similarity
```markdown
\cos(\theta)
```
* Equation: Not explicitly defined in the context.
* Symbols: θ, which represents the angle between two vectors.
* Why it matters: The cosine similarity is used to measure the similarity between denoised gradients and is used to evaluate the effectiveness of IntraShuffler in disrupting client-specific gradient structure.

### Equation 5: RMSE
```markdown
RMSE
```
* Equation: Not explicitly defined in the context.
* Symbols: RMSE, which represents the root mean squared error.
* Why it matters: The RMSE is used to evaluate the performance of different aggregation rules and privacy mechanisms in IntraShuffler.

**Method Summary**
==================

* IntraShuffler is a privacy-preserving framework for Heterogeneous DP Federated Learning (FL) that disrupts client-specific gradient structure to prevent distributional inference and cross-round linkage.
* The framework uses ε-aware learned denoising to partially restore distribution-dependent structural patterns in client updates.
* IntraShuffler achieves near-random source inference accuracy across datasets and rounds by shuffling parameters within privacy-compatible buckets.
* The framework preserves model utility and convergence under heterogeneous privacy budgets, comparable to Shuffle-DP.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Household-level load forecasting datasets (London Household Electricity, Pecan Street Electricity)
	+ Large-scale ComStock dataset
	+ CIFAR-10 vision dataset
* Baselines/Comparisons:
	+ Non-shuffled FL
	+ Shuffle-DP
	+ Plain FL-DP
* Main Claimed Findings:
	+ IntraShuffler effectively eliminates long-term client linkability in HDP-based FL.
	+ IntraShuffler preserves model utility and convergence under heterogeneous privacy budgets.
	+ IntraShuffler achieves near-random source inference accuracy across datasets and rounds.

**What to Verify in the PDF**
=============================

* The implementation details of the ε-aware learned denoiser fθ(g, ε) and its training procedure.
* The evaluation of the role of bucketing in IntraShuffler across different datasets and models.
* The results of the IID vs non-IID ablation study, including the impact of client heterogeneity on gradient-based inference.
{% endraw %}

{% raw %}
## 3) Permissive Safety Through Trusted Inference: Verifiable Belief-Space Neural Safety Filters for Assured Interactive Robotics
- **Authors:** Haimin Hu
- **arXiv:** [2606.02562](https://arxiv.org/abs/2606.02562v1) · [pdf](https://arxiv.org/pdf/2606.02562v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.02562v1))
- **Categories:** cs.RO, cs.AI, cs.LG, eess.SY

### Abstract
> Autonomous robots that interact with people must make safe and efficient decisions under human-induced uncertainty, such as their preferences, goals, competency, and willingness to cooperate. Safety filters are a popular approach for ensuring safety in interactive robotics, since their modular design separates safety from performance, allowing robots to operate safely around people with minimal impact on task efficiency. While traditional safety filters typically operate only in the physical space, neglecting the robot's ability to learn and adapt online, the recently proposed belief-space safety filter (BeliefSF) reasons about robot safety in closed-loop with runtime inference that actively reduces the robot's uncertainty online, thereby reducing conservativeness in filtering. However, providing formal safety guarantees for robots deploying BeliefSF remains a significant challenge due to errors in runtime inference and neural approximation of safety filters required to handle the high dimensionality of belief spaces. In this paper, we propose an algorithmic approach to certify high-probability safety of BeliefSF using conformal prediction, while explicitly accounting for the reliability of the robot's runtime inference module. Our method leverages the structure of belief-space safety filtering by focusing verification on a region where inference is expected to be reliable. It preserves the simplicity and sample complexity of standard conformal prediction, yet can certify a substantially less conservative safety filter. Through a simulated human-vehicle interaction benchmark, we show that our approach verifies a significantly more permissive belief-space safety filter than a standard conformal prediction baseline.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: {x}_{t+1}={f}({x}_{t},{u}^{e}_{t},{u}^{o}_{t})

* Equation: `{x}_{t+1}={f}({x}_{t},{u}^{e}_{t},{u}^{o}_{t})`
* Symbols:
	+ `{x}_{t+1}`: The next state vector of the ego robot.
	+ `{x}_{t}`: The current state vector of the ego robot.
	+ `{u}^{e}_{t}`: The control vector of the ego robot.
	+ `{u}^{o}_{t}`: The control vector of the opponent.
	+ `f`: The physical interaction function.
* Why it matters: This equation describes the dynamics of the ego robot and the opponent, and how the ego robot's control inputs affect the state of both agents.

### Equation 2: {x}_{t}=({x}^{e}_{t},{x}^{o}_{t})\in\mathcal{X}\subseteq\mathbb{R}^{{n_{x}}}

* Equation: `{x}_{t}=({x}^{e}_{t},{x}^{o}_{t})\in\mathcal{X}\subseteq\mathbb{R}^{{n_{x}}}`
* Symbols:
	+ `{x}_{t}`: The current state vector of the ego robot.
	+ `{x}^{e}_{t}`: The ego part of the state vector.
	+ `{x}^{o}_{t}`: The opponent part of the state vector.
	+ `\mathcal{X}`: The state space.
	+ `\mathbb{R}^{{n_{x}}}`: The real vector space of dimension `n_x`.
* Why it matters: This equation defines the state space of the ego robot and the opponent, and how the state vector is composed of both.

### Equation 3: {u}^{e}_{t}\in{\mathcal{U}}^{e}\subset\mathbb{R}^{{m_{e}}}

* Equation: `{u}^{e}_{t}\in{\mathcal{U}}^{e}\subset\mathbb{R}^{{m_{e}}}`
* Symbols:
	+ `{u}^{e}_{t}`: The control vector of the ego robot at time `t`.
	+ `\mathcal{U}^{e}`: The control space of the ego robot.
	+ `\mathbb{R}^{{m_{e}}}`: The real vector space of dimension `m_e`.
* Why it matters: This equation defines the control space of the ego robot, and how the control vector is a vector in this space.

### Equation 4: {u}^{o}_{t}\in{\mathcal{U}}^{o}\subset\mathbb{R}^{{m_{o}}}

* Equation: `{u}^{o}_{t}\in{\mathcal{U}}^{o}\subset\mathbb{R}^{{m_{o}}}`
* Symbols:
	+ `{u}^{o}_{t}`: The control vector of the opponent at time `t`.
	+ `\mathcal{U}^{o}`: The control space of the opponent.
	+ `\mathbb{R}^{{m_{o}}}`: The real vector space of dimension `m_o`.
* Why it matters: This equation defines the control space of the opponent, and how the control vector is a vector in this space.

### Equation 5: f:\mathcal{X}\times{\mathcal{U}}^{e}\times{\mathcal{U}}^{o}\to\mathcal{X}

* Equation: `f:\mathcal{X}\times{\mathcal{U}}^{e}\times{\mathcal{U}}^{o}\to\mathcal{X}`
* Symbols:
	+ `f`: The physical interaction function.
	+ `\mathcal{X}`: The state space.
	+ `\mathcal{U}^{e}`: The control space of the ego robot.
	+ `\mathcal{U}^{o}`: The control space of the opponent.
	+ `\mathcal{X}`: The output space.
* Why it matters: This equation defines the physical interaction function, which maps the state space, control space of the ego robot, and control space of the opponent to the state space.

### Equation 6: \coloneq{x}\in{\mathcal{X}}\mid g({x})<0

* Equation: `\coloneq{x}\in{\mathcal{X}}\mid g({x})<0`
* Symbols:
	+ `\coloneq`: The set notation.
	+ `{x}`: The state vector.
	+ `{x}\in{\mathcal{X}}`: The state vector is in the state space.
	+ `g({x})<0`: The function `g` evaluated at the state vector is less than 0.
* Why it matters: This equation defines the failure set, which is the set of states where the safety condition is not met.

### Equation 7: g:{\mathcal{X}}\rightarrow\mathbb{R}

* Equation: `g:{\mathcal{X}}\rightarrow\mathbb{R}`
* Symbols:
	+ `g`: The safety function.
	+ `{x}`: The state vector.
	+ `\mathbb{R}`: The real numbers.
* Why it matters: This equation defines the safety function, which maps the state space to the real numbers.

### Equation 8: {{\Omega}}

* Equation: `{{\Omega}}`
* Symbols:
	+ `{{\Omega}}`: The set of catastrophic safety events.
* Why it matters: This equation defines the set of catastrophic safety events, which are the events that can lead to a safety failure.

**Method Summary**
==================

* The proposed method uses conformal prediction to verify the safety of the belief-space safety filter.
* The method takes into account the reliability of the robot's runtime inference module.
* The method focuses on a region where inference is expected to be reliable.
* The method preserves the simplicity and sample complexity of standard conformal prediction.
* The method can certify a substantially less conservative safety filter than a standard conformal prediction baseline.

**Experimental Overview**
========================

* The experiment is a simulated human-vehicle interaction benchmark.
* The experiment compares the proposed method with a standard conformal prediction baseline.
* The experiment evaluates whether the proposed method can certify a more permissive belief-space safety filter than the baseline.
* The experiment focuses on two questions:
	+ Whether the proposed method yields a tighter safety coverage parameter than the baseline.
	+ Whether the proposed method can certify a more permissive safety filter than the baseline.

**What to Verify in the PDF**
=============================

* The PDF provides more details on the simulation setup and the opponent modeling.
* The PDF provides more details on the training of the inference score function `h_L`.
* The PDF provides more details on the evaluation of the proposed method and the baseline.
* The PDF provides more details on the results of the experiment, including the safety coverage parameter and the permissiveness of the safety filter.
{% endraw %}

{% raw %}
## 4) A No-Regret Framework for Adaptive Incentive Design
- **Authors:** Georgios Vasileiou, Lantian Zhang, Silun Zhang
- **arXiv:** [2606.02529](https://arxiv.org/abs/2606.02529v1) · [pdf](https://arxiv.org/pdf/2606.02529v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.02529v1))
- **Categories:** math.OC, cs.GT, cs.MA, eess.SY

### Abstract
> Incentive design studies how a central authority can influence strategic agents through payments, subsidies, or taxes, so that individual objectives align with collective welfare. This paper introduces a No-Regret Adaptive Incentive Design (RAID) framework for nonlinear games with continuous action spaces and private agent costs. In this framework, the authority (planner) designs incentives that regulate the Nash equilibrium toward a socially optimal action profile, while simultaneously learning agents' unknown preferences from repeated strategic responses. We formulate the RAID problem and construct a least-squares estimator whose strong consistency requires only diminishing excitation. Leveraging this weak excitation requirement, we propose a switching incentive policy that alternates between probing (exploration) and estimate-based (exploitation) incentives. The resulting policy achieves an $O(t^{-0.5})$ parameter estimation rate and accumulates $O(t^{0.5}\log t)$ squared social-cost regret, almost surely. We further extend the framework to an endogenous-noise response model, where standard least-squares estimation is biased due to an error-in-variables correlation between the noise and agent responses. We utilize a repeated-sampling estimator and corresponding switching policy that retain the same almost-sure convergence and regret rates. Numerical experiments validate the effectiveness and predicted convergence rates of the method.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: O(t^{-0.5})
```math
O(t^{-0.5})
```
Symbols: `O`, `t`, `-0.5`
Why it matters: This equation represents the parameter estimation rate of the switching incentive policy.

### Equation 2: O(t^{0.5}\log t)
```math
O(t^{0.5}\log t)
```
Symbols: `O`, `t`, `0.5`, `\log t`
Why it matters: This equation represents the accumulated social-cost regret of the switching incentive policy.

### Equation 3: n\in\mathbb{N}
```math
n\in\mathbb{N}
```
Symbols: `n`, `\mathbb{N}`
Why it matters: This equation represents the set of natural numbers, which is used to index the agents.

### Equation 4: [n]=\{1,2,\ldots,n\}
```math
[n]=\{1,2,\ldots,n\}
```
Symbols: `[n]`, `{1,2,\ldots,n}`
Why it matters: This equation represents the set of indices for the agents, which is used to index the strategies.

### Equation 5: x\in\mathbb{R}^{n}
```math
x\in\mathbb{R}^{n}
```
Symbols: `x`, `\mathbb{R}^{n}`
Why it matters: This equation represents the strategy space of the agents, which is a vector of length `n` in `R`.

### Equation 6: \|x\|_{2}
```math
\|x\|_{2}
```
Symbols: `x`, `\|x\|_{2}`
Why it matters: This equation represents the Euclidean norm of the strategy vector `x`.

**Method Summary**
==================

* The authors propose a No-Regret Adaptive Incentive Design (RAID) framework for nonlinear games with continuous action spaces and private agent costs.
* The framework involves a least-squares estimator that learns agents' preferences from repeated strategic responses.
* The authors propose a switching incentive policy that alternates between probing (exploration) and estimate-based (exploitation) incentives.
* The policy achieves an O(t^{-0.5}) parameter estimation rate and accumulates O(t^{0.5}\log t) squared social-cost regret, almost surely.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors do not specify the exact tasks or datasets used in the experiments.
* Baselines/Comparisons: The authors compare their proposed RAID framework with existing baselines, but do not specify the exact baselines or comparison metrics.
* Main Claimed Findings: The authors claim that their proposed RAID framework achieves an O(t^{-0.5}) parameter estimation rate and accumulates O(t^{0.5}\log t) squared social-cost regret, almost surely.

**What to Verify in the PDF**
=============================

* The authors mention an error-in-variables bias in the least-squares estimator, but do not provide a detailed analysis of this bias.
* The authors propose a repeated-sampling estimator to address the error-in-variables bias, but do not provide a detailed analysis of this estimator.
* The authors claim that their proposed RAID framework achieves a certain parameter estimation rate and accumulates a certain squared social-cost regret, but do not provide a detailed proof of these claims.
{% endraw %}

{% raw %}
## 5) Drifting Preference Optimization for One-Step Generative Models
- **Authors:** Zhou Jiang, Yandong Wen, Zhen Liu
- **arXiv:** [2606.02521](https://arxiv.org/abs/2606.02521v1) · [pdf](https://arxiv.org/pdf/2606.02521v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.02521v1))
- **Categories:** cs.LG, cs.CV

### Abstract
> One-step text-to-image generators are attractive for deployment because they generate an image with a single forward pass, but preference finetuning them remains difficult: standard alignment methods often rely on policy likelihoods, denoising trajectories, differentiable reward gradients, or test-time optimization. We propose Drifting Preference Optimization (DrPO), an online preference-finetuning method for deterministic one-step generators. For each prompt, DrPO samples candidates from the current generator, ranks them with a target reward, and uses high- and low-scoring samples to synthesize a feature-space update direction. The update is a non-parametric dipole preference field plus a reference drift estimated from the frozen base generator, and is optimized through a detached feature-space regression target. The target reward is used only for ranking, so DrPO can train with large, black-box, or non-differentiable rewards while inference remains a single generator call. We evaluate DrPO on SD-Turbo and SDXL-Turbo with multiple target rewards and benchmarks, including HPSv3 and GenEval. DrPO improves alignment over reward-gradient-free one-step preference baselines and reduces HPSv3 training computation by $3.51\times$ under the matched effective-batch setting by removing reward-model backpropagation. Initial offline experiments suggest that sample-based gradient synthesis can also be used beyond online reward ranking.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: 3.51 ×

* Equation: 3.51 × 3.51
* Symbols: None
* Why it matters: This equation is used to calculate the reduction in training computation by removing reward-model backpropagation.

### Equation 2: p_{\theta}

* Equation: p_{\theta} = ...
* Symbols: p_{\theta}, \theta
* Why it matters: This equation is not explicitly defined in the context, but it is likely related to the probability distribution of the generator.

### Equation 3: p_{\text{ref}}

* Equation: p_{\text{ref}} = ...
* Symbols: p_{\text{ref}}
* Why it matters: This equation is not explicitly defined in the context, but it is likely related to the reference distribution.

### Equation 4: z^{*}

* Equation: z^{*} = ...
* Symbols: z^{*}
* Why it matters: This equation is not explicitly defined in the context, but it is likely related to the optimal feature-space update direction.

### Equation 5: \epsilon

* Equation: \epsilon = ...
* Symbols: \epsilon
* Why it matters: This equation is not explicitly defined in the context, but it is likely related to the input noise.

### Equation 6: y_{\theta}=G_{\theta}(\epsilon,c)

* Equation: y_{\theta}=G_{\theta}(\epsilon,c)
* Symbols: y_{\theta}, G_{\theta}, \epsilon, c
* Why it matters: This equation defines the generator output as a function of the input noise and the feature extractor.

### Equation 7: f_{\theta}(\epsilon,c)

* Equation: f_{\theta}(\epsilon,c) = ...
* Symbols: f_{\theta}, \epsilon, c
* Why it matters: This equation is not explicitly defined in the context, but it is likely related to the feature-space update direction.

### Equation 8: \mathbf{V}_{\nu^{+},\nu^{-}}(x)

* Equation: \mathbf{V}_{\nu^{+},\nu^{-}}(x) = \mathbb{E}_{b^{+}\sim\nu^{+}}\!\left[k(x,b^{+})(b^{+}-x)\right] - \mathbb{E}_{b^{-}\sim\nu^{-}}\!\left[k(x,b^{-})(b^{-}-x)\right]
* Symbols: \mathbf{V}_{\nu^{+},\nu^{-}}(x), \nu^{+}, \nu^{-}, k, x
* Why it matters: This equation defines the non-parametric reward in feature space as the difference between the expected values of the feature-space kernel applied to the positive and negative samples.

**Method Summary**
================

* Drifting Preference Optimization (DrPO) is an online preference-finetuning method for deterministic one-step generators.
* DrPO samples candidates from the current generator, ranks them with a target reward, and uses high- and low-scoring samples to synthesize a feature-space update direction.
* The update is a non-parametric dipole preference field plus a reference drift estimated from the frozen base generator.
* DrPO can train with large, black-box, or non-differentiable rewards while inference remains a single generator call.

**Experimental Overview**
=====================

* Tasks/Datasets: SD-Turbo and SDXL-Turbo one-step text-to-image generators, Pick-a-Pic v2 and Parti-Prompts.
* Baselines/Comparisons: Reward-gradient-free one-step preference methods, direct reward-gradient methods.
* Main Claimed Findings: DrPO improves alignment over reward-gradient-free one-step preference baselines and reduces training computation by removing reward-model backpropagation.

**What to Verify in the PDF**
==========================

* The implementation details of the DrPO algorithm, including the choice of target reward and the optimization procedure.
* The evaluation metrics used to measure the performance of the DrPO method, including the PickScore, AES, and ImageReward metrics.
* The results of the offline experiments, including the sample-based gradient synthesis results.
{% endraw %}
