---
layout: post
title: "Daily arXiv Digest — 2026-08-19 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) The concentration game: Bayesian updating, regret, and information
- **Authors:** Akshay Balsubramani
- **arXiv:** [2608.18061](https://arxiv.org/abs/2608.18061v1) · [pdf](https://arxiv.org/pdf/2608.18061v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.18061v1))
- **Categories:** cs.LG, cs.GT, math.PR, math.ST

### Abstract
> We give a two-player zero-sum repeated game between a learner and nature whose value identity generates Bayesian updating and an exact accounting of exponential-weights regret at once, and supplies the comparator-class variational form that a wide class of concentration phenomena share. The terminal payoff is the most a comparator can gain at fixed relative entropy from the prior, and the one-step constraint is an information budget on nature's move under the learner's mixed action. With the learner's move otherwise unrestricted, Gibbs/Bayes weights emerge as its unique Bellman equalizer -- the mixed action that makes the per-round loss independent of which direction nature moves -- with log-partition functions playing the role of value functions. The regret decomposes exactly into three parts: a per-round information loss reflecting the variation in observed outcomes, an additive retempering drift that accounts exactly for any change of measurement scale between rounds, and the information the comparator carries relative to the prior. The variance and bounded-range proxies that drive standard regret bounds are looser relaxations of this decomposition, which holds generally and governs them all. Both players' strategies are read off from the decomposition term by term, and repeated play yields an information-theoretic ledger of self-play in place of the usual quadratic-variation surrogate. The same comparator-class geometry accounts for the classical large-deviation bounds, and methods across bandits, posterior sampling, aggregation, and boosting are specializations of the one regret decomposition.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: [K] := {1, …, K}

* Equation: [K] := {1, …, K}
* Symbols: [K] (set of actions)
* Why it matters: Defines the set of possible actions in the concentration game.

### Equation 2: Γ ≥ 0

* Equation: Γ ≥ 0
* Symbols: Γ (comparator complexity budget)
* Why it matters: Represents the maximum allowed relative entropy from the prior.

### Equation 3: (ηt, qt)t=1T

* Equation: (ηt, qt)t=1T
* Symbols: (ηt, qt) (schedule of measurement scales and per-round information budgets)
* Why it matters: Specifies the measurement scales and information budgets for each round.

### Equation 4: Γ

* Equation: Γ
* Symbols: Γ (comparator complexity budget)
* Why it matters: Same as Equation 2, represents the maximum allowed relative entropy from the prior.

### Equation 5: S_t-1 := ∑s<tz_s

* Equation: S_t-1 := ∑s<tz_s
* Symbols: S_t-1 (cumulative centered score)
* Why it matters: Represents the cumulative score of nature's past moves.

**Method Summary**
==================

* The concentration game is a two-player zero-sum repeated game that unifies several research communities' separate formalisms for information accounting problems.
* The game's value identity accounts for Bayesian updating, exponential-weights regret, concentration of measure, and large-deviation theory.
* The main result is that the decomposition holds with equality at every horizon, for every comparator, and for every predictable schedule.
* The decomposition is composed across rounds, and each of the three terms is a sum of per-round contributions.

**Experimental Overview**
=========================

* Tasks/Datasets: The paper does not specify a particular dataset, but it discusses the concentration game as a unifying framework for various information accounting problems.
* Baselines/Comparisons: The paper does not provide a comparison to existing baselines, but it discusses the decomposition as a unifying framework for various information accounting problems.
* Main Claimed Findings: The main result is that the decomposition holds with equality at every horizon, for every comparator, and for every predictable schedule.

**What to Verify in the PDF**
=============================

* The proof of Theorem 4.3, which states that the decomposition holds with equality at every horizon, for every comparator, and for every predictable schedule.
* The derivation of the closed-form loss from changing measurement scale between rounds (Proposition C.1).
* The bound Val_tη, Γ(S) ≤ U_t(S), which states that the value-to-go is bounded by the Bellman relaxation.
{% endraw %}

{% raw %}
## 2) Primitive Representation Learning for Unsupervised Dynamic Contrast Enhanced MRI Reconstruction
- **Authors:** Veronika Spieker, Wenqi Huang, Cemre Ariyurek, Liam Timms, Daniel Rueckert, Onur Afacan, Julia A. Schnabel, Sila Kurugol
- **arXiv:** [2608.18055](https://arxiv.org/abs/2608.18055v1) · [pdf](https://arxiv.org/pdf/2608.18055v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.18055v1))
- **Categories:** eess.IV, cs.CV, cs.LG, eess.SP, physics.med-ph

### Abstract
> Reliable quantitative analysis of dynamic contrast-enhanced MRI requires high-quality spatiotemporal reconstructions at high undersampling rates. Scan-specific reconstructions using Gaussian and Gabor primitives have shown promising results without the need for large training datasets, but have not addressed the additional dimension of dynamic contrast. We propose a multi-dimensional, primitive based framework for dynamic contrast-enhanced MRI reconstruction that disentangles the underlying anatomy, the dynamic contrast enhancement, and residual motion into separate temporal basis functions, thereby enabling a geometrical interpretation of the representation. We show that this architecture achieves performance competitive with conventional reconstruction methods, both in reconstruction quality and in the accuracy of extracted aorta and kidney enhancement curves. The modular tier design extends naturally to additional dynamic factors and higher acceleration rates. Code available at https://github.com/compai-lab/ 2026-GaborDCE-spieker.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `x_{t}(\vec{r})=\sum_{n=1}^{N}w_{n,t}\,P_{n}\!\bigl(\vec{r};\;\vec{\mu}_{n,t},\,\vec{s}_{n,t},\theta_{n,t},\vec{\xi}_{n,t}\bigr)`

* Equation: `x_{t}(\vec{r})=\sum_{n=1}^{N}w_{n,t}\,P_{n}\!\bigl(\vec{r};\;\vec{\mu}_{n,t},\,\vec{s}_{n,t},\theta_{n,t},\vec{\xi}_{n,t}\bigr)`
* Symbols:
	+ `x_{t}(\vec{r})`: the reconstructed image at time `t` and location `r`
	+ `w_{n,t}`: the complex weight of the `n`-th primitive at time `t`
	+ `P_{n}\!\bigl(\vec{r};\;\vec{\mu}_{n,t},\,\vec{s}_{n,t},\theta_{n,t},\vec{\xi}_{n,t}\bigr)`: the `n`-th primitive at location `r` with parameters `μ_{n,t}`, `s_{n,t}`, `θ_{n,t}`, and `ξ_{n,t}`
* Why it matters: This equation represents the reconstruction of the image at time `t` as a sum of `N` primitives, each with its own weight and parameters.

### Equation 2: `w_{n,t}\in\mathbb{C}`

* Equation: `w_{n,t}\in\mathbb{C}`
* Symbols: `w_{n,t}`
* Why it matters: This equation specifies that the complex weights `w_{n,t}` are elements of the complex numbers.

### Equation 3: `P_{n}\!\bigl(\vec{r};\,\vec{\mu},\,\vec{s},\,\theta,\,\vec{\xi}\bigr)`

* Equation: `P_{n}\!\bigl(\vec{r};\,\vec{\mu},\,\vec{s},\,\theta,\,\vec{\xi}\bigr)`
* Symbols:
	+ `P_{n}\!\bigl(\vec{r};\,\vec{\mu},\,\vec{s},\,\theta,\,\vec{\xi}\bigr)`: the `n`-th primitive at location `r` with parameters `μ`, `s`, `θ`, and `ξ`
* Why it matters: This equation represents the `n`-th primitive at location `r` with its corresponding parameters.

### Equation 4: `\vec{\mu}_{n,t}`

* Equation: `\vec{\mu}_{n,t}`
* Symbols: `\vec{\mu}_{n,t}`
* Why it matters: This equation specifies the parameters `μ_{n,t}` of the `n`-th primitive at time `t`.

### Equation 5: `\vec{s}_{n,t}`

* Equation: `\vec{s}_{n,t}`
* Symbols: `\vec{s}_{n,t}`
* Why it matters: This equation specifies the parameters `s_{n,t}` of the `n`-th primitive at time `t`.

### Equation 6: `\theta_{n,t}`

* Equation: `\theta_{n,t}`
* Symbols: `\theta_{n,t}`
* Why it matters: This equation specifies the parameters `θ_{n,t}` of the `n`-th primitive at time `t`.

### Equation 7: `\vec{\xi}_{n,t}`

* Equation: `\vec{\xi}_{n,t}`
* Symbols: `\vec{\xi}_{n,t}`
* Why it matters: This equation specifies the parameters `ξ_{n,t}` of the `n`-th primitive at time `t`.

### Equation 8: `w_{n,t}`

* Equation: `w_{n,t}`
* Symbols: `w_{n,t}`
* Why it matters: This equation specifies the complex weights `w_{n,t}` of the `n`-th primitive at time `t`.

**Method Summary**
==================

* The authors propose a multi-dimensional, primitive-based framework for dynamic contrast-enhanced MRI reconstruction.
* The framework disentangles the underlying anatomy, dynamic contrast enhancement, and residual motion into separate temporal basis functions.
* The authors use a modular tier design to extend the framework to additional dynamic factors and higher acceleration rates.
* The authors compare their method to conventional reconstruction methods, including GRASP, L+S, and Hash-INR.
* The authors evaluate their method on a dataset of pediatric MRI acquisitions and report competitive reconstruction quality and accuracy of extracted aorta and kidney enhancement curves.

**Experimental Overview**
=========================

* Tasks:
	+ Evaluate the proposed method on a dataset of pediatric MRI acquisitions.
	+ Compare the proposed method to conventional reconstruction methods, including GRASP, L+S, and Hash-INR.
* Datasets:
	+ Pediatric MRI acquisitions with a golden angle stack-of-stars 3D FLASH prototype sequence.
	+ A dataset of 5 in-house pediatric MRI acquisitions.
* Baselines/Comparisons:
	+ GRASP: a clinical standard for dynamic contrast-enhanced MRI reconstruction.
	+ L+S: a conventional decomposition-based method for dynamic contrast-enhanced MRI reconstruction.
	+ Hash-INR: an alternative scan-specific learning-based method for dynamic contrast-enhanced MRI reconstruction.
* Main claimed findings:
	+ The proposed method achieves competitive reconstruction quality and accuracy of extracted aorta and kidney enhancement curves.
	+ The proposed method is more robust to noise and artifacts than conventional reconstruction methods.
{% endraw %}

{% raw %}
## 3) Optimize Your Sampling: Tuned Diffusion Sampling with Bayesian Optimization
- **Authors:** Travis Zhang, Christian Belardi, Justin Lovelace, Jin Peng Zhou, Saebyeol Shin, Carla P. Gomes, Kilian Q. Weinberger
- **arXiv:** [2608.18040](https://arxiv.org/abs/2608.18040v1) · [pdf](https://arxiv.org/pdf/2608.18040v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.18040v1))
- **Categories:** cs.LG, cs.CV

### Abstract
> Sampling from a diffusion model typically requires many forward passes through a large neural network, making generation computationally expensive. While much work has focused on efficient solvers and samplers, comparatively little attention has been paid to selecting the sampling timesteps themselves. A recent line of work optimizes theoretically derived surrogates for sample quality rather than the quality metric itself. We propose Optimizing Your Sampling (OYS), which instead treats timestep selection as a black-box optimization problem, optimizing the target metric directly with Bayesian optimization. OYS outperforms both the default schedules and those of Align Your Steps on text-to-image generation, and improves over the default schedules on inpainting and other image tasks, in both quantitative and human evaluations. OYS requires no additional training, is applicable even to distilled models, and improves both simple and sophisticated samplers such as Euler and DPM-Solver++. A 5-step OYS schedule retains 89%-94% of the quality of a 50-step schedule while reducing inference cost by 10x.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\sigma_{\min}$

* Equation: $\sigma_{\min}$
* Symbols: $\sigma_{\min}$ (minimum signal-to-noise ratio)
* Why it matters: This equation represents the minimum signal-to-noise ratio, which is a unified representation of noise levels across models.

### Equation 2: $\sigma_{\max}$

* Equation: $\sigma_{\max}$
* Symbols: $\sigma_{\max}$ (maximum signal-to-noise ratio)
* Why it matters: This equation represents the maximum signal-to-noise ratio, which is a unified representation of noise levels across models.

### Equation 3: $\rho$

* Equation: $\rho$
* Symbols: $\rho$ (noise level)
* Why it matters: This equation represents the noise level, which is a key factor in determining the quality of generated samples.

### Equation 4: $\mathcal{X}$

* Equation: $\mathcal{X}$
* Symbols: $\mathcal{X}$ (sample space)
* Why it matters: This equation represents the sample space, which is the set of all possible samples generated by the diffusion model.

### Equation 5: $\mathbf{p} = \{p_{1}, \dots, p_{M}\}$

* Equation: $\mathbf{p} = \{p_{1}, \dots, p_{M}\}$
* Symbols: $\mathbf{p}$ (probability distribution), $p_{k}$ (probability of each timestep)
* Why it matters: This equation represents the probability distribution of the timesteps, which is used to select the optimal sampling schedule.

**Method Summary**
==================

* The proposed method, Optimizing Your Sampling (OYS), treats timestep selection as a black-box optimization problem, optimizing the target metric directly with Bayesian optimization.
* OYS outperforms both the default schedules and those of Align Your Steps on text-to-image generation, and improves over the default schedules on inpainting and other image tasks.
* OYS requires no additional training, is applicable even to distilled models, and improves both simple and sophisticated samplers such as Euler and DPM-Solver++.

**Experimental Overview**
========================

* Tasks/Datasets: Text-to-image generation, inpainting, and prompt diffusion tasks.
* Baselines/Comparisons: Default schedules, Align Your Steps, and SDXL-Turbo.
* Main Claimed Findings: OYS outperforms the default schedules and Align Your Steps on text-to-image generation, and improves over the default schedules on inpainting and other image tasks.

**What to Verify in the PDF**
=============================

* The human preference score calculation for the Human Preference Dataset v2 (HPD v2) and the fine-tuned CLIP model.
* The zero-shot FID results on MSCOCO and the evaluation of OYS on the validation split of COCO Captions.
* The detailed results for SDXL-Turbo in Table 5, including the mean HPS and win rates for different baselines.
{% endraw %}

{% raw %}
## 4) Harnessing Magnitude-Only and Complex Measurements for Improved Dynamic MRI Reconstruction with Learned Priors
- **Authors:** Mahdi Saberi, Yaşar Utku Alçalar, Merve Gülle, Chetan Shenoy, Mehmet Akçakaya
- **arXiv:** [2608.18036](https://arxiv.org/abs/2608.18036v1) · [pdf](https://arxiv.org/pdf/2608.18036v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.18036v1))
- **Categories:** eess.IV, cs.AI, cs.CV, cs.LG, physics.med-ph

### Abstract
> MRI reconstruction methods for undersampled k-space data naturally utilize complex-valued measurements. Parallel developments in sparse phase retrieval have shown that magnitude-only measurements may provide complementary information for signal recovery. However, their use in MRI reconstruction remains largely unexplored, due to lack of practical settings where informative magnitude measurements can be obtained without additional scan time. In this work, we investigate the use of auxiliary k-space magnitude information for accelerated steady-state dynamic MRI reconstruction, and demonstrate strong consistency of k-space magnitudes across time-frames. Building on this observation, we propose $\mathbb{C}+\text{Mag}$, a magnitude-informed physics-driven deep learning reconstruction method. The proposed method employs an ADMM-based unrolling framework with a novel magnitude-aware data-fidelity formulation, where quadratically smoothed optimization and momentum-based updates are introduced to address the non-differentiability and non-convexity of the magnitude constraints. Experiments on retrospectively undersampled cine MRI and phase-contrast flow MRI datasets, as well as prospectively undersampled real-time cine MRI acquisitions, demonstrate improved artifact suppression, sharper anatomical recovery, and better preservation of phase information compared to conventional PD-DL methods, which is further supported through blinded expert reader evaluations.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: ℂ + Mag

* Equation: ℂ + Mag
* Symbols: ℂ (complex-valued measurements), Mag (magnitude-only measurements)
* Why it matters: This equation represents the proposed reconstruction framework that jointly enforces consistency with both complex-valued and magnitude-only measurements.

### Equation 2: Optimization Problem

* Equation: \arg\min_{\mathbf{x}}\|\mathbf{y}_{\Omega}-\mathbf{E}_{\Omega}\mathbf{x}\|_{2}^{2}+\mathcal{R}(\mathbf{x})
* Symbols: \mathbf{x} (reconstructed image), \mathbf{y}_{\Omega} (complex-valued measurements), \mathbf{E}_{\Omega} (forward operator), \mathcal{R}(\mathbf{x}) (regularization term)
* Why it matters: This equation represents the optimization problem used to reconstruct the image, which minimizes the difference between the measured data and the reconstructed image, subject to a regularization term that enforces consistency with the auxiliary magnitude constraints.

### Equation 3: Complex-Valued Measurements

* Equation: \mathbf{y}_{\Omega}\in{\mathbb{C}}^{m}
* Symbols: \mathbf{y}_{\Omega} (complex-valued measurements), m (number of measurements)
* Why it matters: This equation represents the definition of complex-valued measurements, which are used as input to the reconstruction framework.

### Equation 4: Sampling Pattern

* Equation: \Omega
* Symbols: \Omega (sampling pattern)
* Why it matters: This equation represents the sampling pattern used to acquire the complex-valued measurements, which is used to determine the locations of the measurements in the k-space.

### Equation 5: Forward Operator

* Equation: \mathbf{E}_{\Omega}:{\mathbb{C}}^{n}\to{\mathbb{C}}^{m}
* Symbols: \mathbf{E}_{\Omega} (forward operator), n (number of image pixels), m (number of measurements)
* Why it matters: This equation represents the forward operator used to relate the image to the complex-valued measurements, which is used to compute the reconstruction error.

**Method Summary**
================

* The proposed method uses a combination of complex-valued and magnitude-only measurements to improve dynamic MRI reconstruction.
* The method employs an ADMM-based unrolling framework with a novel magnitude-aware data-fidelity formulation.
* The framework jointly enforces consistency with both complex-valued and magnitude-only measurements, which improves the reconstruction accuracy.
* The method is compared to conventional PD-DL methods, which use only complex-valued measurements.

**Experimental Overview**
=====================

* The proposed method is evaluated on two datasets: retrospectively undersampled cine MRI and phase-contrast flow MRI datasets, as well as prospectively undersampled real-time cine MRI acquisitions.
* The method is compared to conventional PD-DL methods, which use only complex-valued measurements.
* The main claimed findings are:
	+ Improved artifact suppression and sharper anatomical recovery compared to conventional PD-DL methods.
	+ Better preservation of phase information compared to conventional PD-DL methods.
	+ Excellent agreement with the corresponding baseline acquisitions for all cardiac function parameters.

**What to Verify in the PDF**
==========================

* The implementation details of the proposed method, including the choice of hyperparameters and the optimization algorithm used.
* The results of the ablation study, which examines the impact of different components of the proposed method on the reconstruction accuracy.
* The detailed analysis of the qualitative expert evaluation, which assesses the image quality and artifacts in the reconstructed images.
{% endraw %}

{% raw %}
## 5) Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents
- **Authors:** Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba
- **arXiv:** [2608.18008](https://arxiv.org/abs/2608.18008v1) · [pdf](https://arxiv.org/pdf/2608.18008v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.18008v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-planner and RL-controller architecture as a Goal-Augmented Markov Decision Process and show that when the LLM per-state progress score is used as a bounded potential function, the resulting shaping term preserves the optimal policy set even when the LLM scores are inaccurate. This guarantee is stronger than what general LLM-as-reward approaches provide. We verify the result numerically on a small MDP under four potential configurations, including an adversarial one scaled to twenty times the base reward magnitude.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $20 \times$
* Equation: $20 \times$
* Symbols: None
* Why it matters: This equation is not explicitly defined in the context, but it seems to be related to the reward magnitude in the MiniGrid-DoorKey-6x6-v0 environment.

### Equation 2: $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \rho_0)$
* Equation: $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \rho_0)$
* Symbols:
	+ $\mathcal{M}$: Goal-Augmented Markov Decision Process
	+ $\mathcal{S}$: State space
	+ $\mathcal{A}$: Action space
	+ $P$: Transition model
	+ $R$: Reward function
	+ $\gamma$: Discount factor
	+ $\rho_0$: Initial state distribution
* Why it matters: This equation defines the structure of the Goal-Augmented Markov Decision Process, which is used to formalize the hybrid LLM-planner + RL-controller architecture.

### Equation 3: $s_t \in \mathcal{S}$
* Equation: $s_t \in \mathcal{S}$
* Symbols:
	+ $s_t$: State at time $t$
	+ $\mathcal{S}$: State space
* Why it matters: This equation specifies that the state at time $t$ belongs to the state space.

### Equation 4: $a_t \in \mathcal{A}$
* Equation: $a_t \in \mathcal{A}$
* Symbols:
	+ $a_t$: Action at time $t$
	+ $\mathcal{A}$: Action space
* Why it matters: This equation specifies that the action at time $t$ belongs to the action space.

### Equation 5: $s_{t+1} \sim P(\cdot \mid s_t, a_t)$
* Equation: $s_{t+1} \sim P(\cdot \mid s_t, a_t)$
* Symbols:
	+ $s_{t+1}$: State at time $t+1$
	+ $P$: Transition model
	+ $s_t$: State at time $t$
	+ $a_t$: Action at time $t$
* Why it matters: This equation specifies the transition model, which describes the probability distribution over the next state given the current state and action.

**Method Summary**
================

* The proposed framework combines large language models (LLMs) with reinforcement learning (RL) to create a hybrid LLM-planner + RL-controller architecture.
* The framework uses a Goal-Augmented Markov Decision Process (GA-MDP) to formalize the hybrid architecture.
* The LLM's per-state progress score is used as a bounded potential function in the sense of Ng, Harada, Russell (1999).
* The induced reward-shaping term does not alter the set of optimal policies of the augmented MDP regardless of how wrong the LLM's scores are at individual states.

**Experimental Overview**
=====================

* Tasks/Datasets: MiniGrid-DoorKey-6x6-v0
* Baselines/Comparisons: PPO baseline
* Main claimed findings: The hybrid agent using Qwen-2.5:14b achieves a success rate of 28.1% with a wide confidence interval, while the PPO baseline achieves a success rate of 28.1% with a wide confidence interval.

**What to Verify in the PDF**
==========================

* The mathematical proof of the guarantee that the induced reward-shaping term does not alter the set of optimal policies of the augmented MDP.
* The numerical results for the four potential configurations, including the adversarial one.
* The details of the transition model and the reward function used in the experiments.
{% endraw %}
