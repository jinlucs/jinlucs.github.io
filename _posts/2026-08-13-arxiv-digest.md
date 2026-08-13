---
layout: post
title: "Daily arXiv Digest — 2026-08-13 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Earth observation embeddings are effective sub-grid descriptors for probabilistic weather downscaling
- **Authors:** Pedro Sousa, Will Tebbutt, Sadiq Jaffer, Robin Young, Anil Madhavapeddy, Richard E. Turner
- **arXiv:** [2608.12271](https://arxiv.org/abs/2608.12271v1) · [pdf](https://arxiv.org/pdf/2608.12271v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.12271v1))
- **Categories:** cs.LG, physics.ao-ph

### Abstract
> Global weather reanalyses and forecasts resolve the evolving atmospheric state on coarse grids, but site-specific applications require predictions at arbitrary locations where near-surface conditions also depend on unresolved terrain and land-surface properties. Existing probabilistic downscalers address this gap using hand-crafted topographic descriptors. We ask instead whether Earth observation foundation models can provide transferable sub-grid surface representations for probabilistic weather downscaling. We augment a convolutional conditional neural process that downscales coarse ERA5 reanalysis fields at ~25 km resolution with a learned local surface descriptor, obtained by compressing a patch of TESSERA embeddings at 10 m resolution. Although these embeddings summarise surface conditions over annual timescales, they improve downscaling of instantaneous 2 m temperature and 10 m wind speed by encoding persistent surface properties that capture a location's departure from the coarse-grid atmospheric state. Across five climatically diverse regions, the embedding improves point and probabilistic skill at stations held out in both space and time, overall improving CRPS skill by 11.5% for 2 m temperature and 6.2% for 10 m wind speed. We further analyse how its contribution differs by variable, finding that topography explains more of temperature's sub-grid structure, while TESSERA provides additional surface information for wind speed. These improvements persist when the coarse input is changed from ERA5 to forecasts from the Aurora AI forecasting model, and when predicting at newly deployed stations with no regional history. To our knowledge, this is the first evidence that long-timescale Earth-observation embeddings can support short-timescale weather downscaling where sub-grid departures are systematically structured by persistent surface properties.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1
{\sim}25

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 2
11.5\%

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 3
6.2\%

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 4
3\,^{\circ}

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 5
8\,^{\circ}

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 6
{\sim}23\%

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 7
0.25^{\circ}

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 8
\sim 25

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

**Method Summary**
==================

* The authors use a ConvCNP downscaling framework to predict weather at arbitrary locations.
* The framework uses a Tessera surface descriptor to construct sub-grid representations.
* The authors train the model on ERA5 reanalysis data and evaluate its performance on Aurora forecast grids.
* The model is trained using a conditional neural process formulation and a mean squared error loss function.
* The authors use a model output statistics approach to adapt the model to lead-dependent forecast errors.

**Experimental Overview**
=========================

* Tasks: The authors evaluate the performance of the Tessera embedding on downscaling performance across complementary spatial and operational settings.
* Datasets: The authors use ERA5 reanalysis data and Aurora forecast grids.
* Baselines/Comparisons: The authors compare the performance of the Tessera embedding to a baseline ConvCNP model.
* Main claimed findings: The authors claim that the Tessera embedding improves downscaling performance across all metrics and regions.

**What to Verify in the PDF**
=============================

* The authors claim that the Tessera embedding reduces the risk of posterior collapse. Verify this claim by examining the KL weight annealing schedule and the posterior log-variance.
* The authors mention that the embedding changes the fine-scale structure of dense downscaled fields. Verify this claim by examining the results of Section 3.2.
* The authors claim that the embedding is sample-efficient. Verify this claim by examining the results of Section 3.5.
{% endraw %}

{% raw %}
## 2) Redistribution-based Cost Inference Improves Sparse Safe Offline RL
- **Authors:** Ebenezer Gelo, Geraud Nangue Tasse, Steven James, Benjamin Rosman
- **arXiv:** [2608.12306](https://arxiv.org/abs/2608.12306v1) · [pdf](https://arxiv.org/pdf/2608.12306v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.12306v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Safe offline RL typically assumes access to dense per-step cost annotations, but in practice supervisors provide only trajectory-level stop-feedback: a binary signal at the first unsafe transition, with no per-step attribution. We frame this as a temporal credit assignment problem and propose the Redistribution-based Cost Inference (RCI) framework, which converts sparse stop-feedback into dense per-step costs via return decomposition, then trains a constrained offline policy on the augmented dataset. We show that return-equivalent redistribution preserves the feasible policy set and the optimal Lagrangian in a CMDP, establishing that the transformation is lossless in theory while yielding better-conditioned cost critic learning in practice. Experiments on highway driving and robotic manipulation demonstrate substantially lower violation rates than sparse and classifier-based baselines, with robustness to heterogeneous dataset compositions and label noise.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: (\mathcal{S},\mathcal{A},P,r,\gamma)

* Equation: (\mathcal{S},\mathcal{A},P,r,\gamma)
* Symbols: \(\mathcal{S}\) (state space), \(\mathcal{A}\) (action space), \(P\) (transition model), \(r\) (reward function), \(\gamma\) (discount factor)
* Why it matters: This equation represents the Markov Decision Process (MDP) framework, which is the foundation for many reinforcement learning algorithms.

### Equation 2: \mathcal{S}

* Equation: \mathcal{S}
* Symbols: \(\mathcal{S}\) (state space)
* Why it matters: This equation represents the state space, which is a set of all possible states in the environment.

### Equation 3: \mathcal{A}

* Equation: \mathcal{A}
* Symbols: \(\mathcal{A}\) (action space)
* Why it matters: This equation represents the action space, which is a set of all possible actions in the environment.

### Equation 4: P(s^{\prime}|s,a)

* Equation: P(s^{\prime}|s,a)
* Symbols: \(P\) (transition model), \(s^{\prime}\) (next state), \(s\) (current state), \(a\) (action)
* Why it matters: This equation represents the transition model, which describes the probability of transitioning from one state to another given the current state and action.

### Equation 5: r(s,a)

* Equation: r(s,a)
* Symbols: \(r\) (reward function), \(s\) (state), \(a\) (action)
* Why it matters: This equation represents the reward function, which assigns a reward to each state-action pair based on the agent's performance.

**Method Summary**
==================

* The Redistribution-based Cost Inference (RCI) framework converts sparse stop-feedback into dense per-step costs via return decomposition.
* RCI trains a constrained offline policy on the augmented dataset, which preserves the feasible policy set and the optimal Lagrangian in a CMDP.
* The transformation is lossless in theory, but yields better-conditioned cost critic learning in practice.

**Experimental Overview**
========================

* Tasks/Datasets:
	+ HighwayEnv: an ego vehicle navigates highway traffic while avoiding collisions.
	+ Safe-FetchReach: a 7-DOF robotic arm reaches target positions while avoiding a spherical hazard region.
* Baselines/Comparisons:
	+ Reward-Only: ignores safety costs and sets the budget to infinity.
	+ Sparse: uses the raw terminal cost label without redistribution.
	+ Hazard: a two-head binary classifier predicts whether a state-action pair appears in any unsafe trajectory.
* Main Claimed Findings:
	+ RCI substantially lowers violation rates compared to sparse and classifier-based baselines.
	+ RCI is robust to heterogeneous dataset compositions and label noise.

**What to Verify in the PDF**
=============================

* The formal statements and proofs for the return-equivalence property (Appendix A).
* The qualitative analysis in Appendix B, including the visualization of spatial cost landscapes and policy trajectories.
* The experimental details in Appendix C, including the annotation protocol and task definitions.
{% endraw %}

{% raw %}
## 3) A Framework for Designing Reward Functions: From Objectives to Features to Human-Aligned Reward Functions
- **Authors:** Di Yang Shi, W. Bradley Knox
- **arXiv:** [2608.12302](https://arxiv.org/abs/2608.12302v1) · [pdf](https://arxiv.org/pdf/2608.12302v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.12302v1))
- **Categories:** cs.LG

### Abstract
> We present a formal process to enable non-experts to instantiate and iterate on human-aligned reward functions, i.e. reward functions that adhere to a given preference ordering over trajectories. Given a task described in natural language, our process produces a linear reward function in three steps: distill the task's objectives into a set of fundamental objectives and derive measurable outcome variables that capture those fundamental objectives, select a causally representative subset of outcome variables as the reward terms, and fit weights to those reward terms via preference elicitation. Our contributions describe the first step and formalize the latter two steps. The first is a guided workflow for deriving outcome variables. The second is a reduction of reward term selection to minimum-cost partial cover on a causal DAG, solved in polynomial time via max-flow. The third is a geometric framing of weight fitting as a convex feasibility problem iteratively narrowed by preference queries, solved by existing separation oracle methods. To the best of our knowledge, this is the first reward-design method that maintains a deterministically conflict-free feasible weight region, narrowed to a desired tolerance via a separation oracle with O(n log κ) preference queries.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: O(n\log\kappa)

* Equation: O(n\log\kappa)
* Symbols: n, \kappa
* Why it matters: This equation represents the time complexity of the algorithm for solving the minimum-cost partial cover problem on a causal DAG. The algorithm is said to have a polynomial time complexity of O(n\log\kappa), which is efficient.

### Equation 2: m/s^{2}

* Equation: m/s^{2}
* Symbols: m, s
* Why it matters: This equation is not explicitly mentioned in the context as a formula derived from the paper, but it appears to be a notation for acceleration (m/s^{2} = acceleration in m/s^{2}).

### Equation 3: m/s^{3}

* Equation: m/s^{3}
* Symbols: m, s
* Why it matters: Similar to Equation 2, this equation is not explicitly mentioned in the context as a formula derived from the paper, but it appears to be a notation for jerk (m/s^{3} = jerk in m/s^{3}).

### Equation 4: a\rightarrow b

* Equation: a\rightarrow b
* Symbols: a, b
* Why it matters: This equation represents a causal relationship between two nodes in a causal DAG. It indicates that node a has a causal effect on node b.

### Equation 5: G=(V,E)

* Equation: G=(V,E)
* Symbols: G, V, E
* Why it matters: This equation represents a directed graph G, where V is the set of vertices and E is the set of edges. It is used to denote the causal DAG of outcome variables.

**Method Summary**
==================

* The proposed framework consists of three steps:
	+ Distill the task description into a set of fundamental objectives and derive measurable outcome variables that capture those fundamental objectives.
	+ Select a causally representative, low-cost subset of outcome variables as the reward terms.
	+ Fit weights to those reward terms via preference elicitation.
* The first step involves an iterative procedure to distill task objectives into fundamental objectives.
* The second step involves selecting outcome variables based on their causal relationships and costs.
* The third step involves fitting weights to the selected outcome variables using preference elicitation.

**Experimental Overview**
=========================

* Tasks/Datasets: Not explicitly mentioned in the context.
* Baselines/Comparisons: Not explicitly mentioned in the context.
* Main Claimed Findings: The proposed framework produces a human-aligned linear reward function that is efficient and effective in obtaining policies that behave as desired.

**What to Verify in the PDF**
=============================

* The details of the iterative procedure for distilling task objectives into fundamental objectives.
* The mathematical formulation of the minimum-cost partial cover problem on a causal DAG.
* The experimental results and comparisons with baselines.
{% endraw %}

{% raw %}
## 4) Earth observation embeddings are effective sub-grid descriptors for probabilistic weather downscaling
- **Authors:** Pedro Sousa, Will Tebbutt, Sadiq Jaffer, Robin Young, Anil Madhavapeddy, Richard E. Turner
- **arXiv:** [2608.12271](https://arxiv.org/abs/2608.12271v1) · [pdf](https://arxiv.org/pdf/2608.12271v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.12271v1))
- **Categories:** cs.LG, physics.ao-ph

### Abstract
> Global weather reanalyses and forecasts resolve the evolving atmospheric state on coarse grids, but site-specific applications require predictions at arbitrary locations where near-surface conditions also depend on unresolved terrain and land-surface properties. Existing probabilistic downscalers address this gap using hand-crafted topographic descriptors. We ask instead whether Earth observation foundation models can provide transferable sub-grid surface representations for probabilistic weather downscaling. We augment a convolutional conditional neural process that downscales coarse ERA5 reanalysis fields at ~25 km resolution with a learned local surface descriptor, obtained by compressing a patch of TESSERA embeddings at 10 m resolution. Although these embeddings summarise surface conditions over annual timescales, they improve downscaling of instantaneous 2 m temperature and 10 m wind speed by encoding persistent surface properties that capture a location's departure from the coarse-grid atmospheric state. Across five climatically diverse regions, the embedding improves point and probabilistic skill at stations held out in both space and time, overall improving CRPS skill by 11.5% for 2 m temperature and 6.2% for 10 m wind speed. We further analyse how its contribution differs by variable, finding that topography explains more of temperature's sub-grid structure, while TESSERA provides additional surface information for wind speed. These improvements persist when the coarse input is changed from ERA5 to forecasts from the Aurora AI forecasting model, and when predicting at newly deployed stations with no regional history. To our knowledge, this is the first evidence that long-timescale Earth-observation embeddings can support short-timescale weather downscaling where sub-grid departures are systematically structured by persistent surface properties.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1

* Equation: `{\sim}25`
* Symbols: `{\sim}` (tilde) and `25`
* Why it matters: This equation is not explicitly defined in the context, but it seems to represent a threshold or a value. It is used in the context of downscaling performance evaluation.

### Equation 2

* Equation: `11.5\%`
* Symbols: `%` (percent sign)
* Why it matters: This equation represents a percentage value, likely used to evaluate the performance of the downscaling model.

### Equation 3

* Equation: `6.2\%`
* Symbols: `%` (percent sign)
* Why it matters: This equation represents another percentage value, likely used to evaluate the performance of the downscaling model.

### Equation 4

* Equation: `3\,^{\circ}`
* Symbols: `\,^{\circ}` (degree symbol)
* Why it matters: This equation represents a value in degrees, likely used to represent spatial resolution or grid size.

### Equation 5

* Equation: `8\,^{\circ}`
* Symbols: `\,^{\circ}` (degree symbol)
* Why it matters: This equation represents another value in degrees, likely used to represent spatial resolution or grid size.

**Method Summary**
==================

* The authors use a ConvCNP downscaling framework to predict weather conditions at arbitrary locations.
* The framework uses a Tessera surface descriptor to construct a sub-grid representation of the terrain and land-surface properties.
* The authors train the model on ERA5 reanalysis data and evaluate its performance using various metrics, including mean absolute error (MAE) and root mean squared error (RMSE).
* The authors also evaluate the model's performance using Aurora forecast grids as input.

**Experimental Overview**
=========================

* Tasks:
	+ Downscaling weather conditions at arbitrary locations using a ConvCNP framework.
	+ Evaluating the performance of the downscaling model using various metrics.
* Datasets:
	+ ERA5 reanalysis data.
	+ Aurora forecast grids.
* Baselines/Comparisons:
	+ Hand-crafted topographic descriptors.
	+ Existing probabilistic downscalers.
* Main claimed findings:
	+ The Tessera surface descriptor improves the performance of the downscaling model.
	+ The model achieves better performance than existing probabilistic downscalers.

**What to Verify in the PDF**
=============================

* The authors claim that the Tessera surface descriptor improves the performance of the downscaling model. Verify this claim by examining the results of the experiments and the metrics used to evaluate the model's performance.
* The authors also claim that the model achieves better performance than existing probabilistic downscalers. Verify this claim by comparing the results of the experiments with those of existing downscaling models.
* The authors mention that the model's performance is evaluated using various metrics, including MAE and RMSE. Verify that these metrics are indeed used to evaluate the model's performance and that the results are presented in a clear and transparent manner.
{% endraw %}

{% raw %}
## 5) Calibration Bets on the Past: Post-Training Quantization for Financial Time-Series Forecasting
- **Authors:** Junyi Ye, Ivy Gateri Wanjiku
- **arXiv:** [2608.12259](https://arxiv.org/abs/2608.12259v1) · [pdf](https://arxiv.org/pdf/2608.12259v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.12259v1))
- **Categories:** cs.LG, q-fin.ST

### Abstract
> Financial forecasting models are typically developed in full precision, yet production deployment often requires low-precision inference to reduce memory and computational cost. Post-training quantization (PTQ) enables such deployment without retraining. However, reliable activation quantization requires calibration: activation ranges are estimated from historical data before deployment and then remain fixed during future inference. The importance of this deployment choice for financial forecasting remains poorly understood. We present a systematic study of activation calibration for PTQ in cross-sectional volatility forecasting on the S&P 500. Our evaluation covers seven representative neural architectures, eight walk-forward test years (2018-2025), and 560 trained models. We find that activation calibration has little effect at 8 bits but becomes the primary determinant of predictive performance at 4 bits. Under default absolute-maximum (abs-max) calibration, static 4-bit quantization of both weights and activations removes 11-62% of the full-precision mean information coefficient in affected architectures. Replacing abs-max with percentile calibration recovers 53-94% of this degradation in the four most affected architectures. The preferred activation range also varies across market periods. Narrow ranges improve resolution under typical market conditions but lose part of their advantage when test-period market dispersion exceeds the calibration history. These findings show that activation calibration is a first-class deployment decision for reliable 4-bit PTQ in financial forecasting. When substantial degradation remains, 8-bit activations or weight-only 4-bit quantization provide more robust deployment choices.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\hat{x}$

* Equation: $\hat{x}$
* Symbols: $\hat{x}$ (estimated output)
* Why it matters: This equation represents the estimated output of the neural network.

### Equation 2: $[-A, A]$

* Equation: $[-A, A]$
* Symbols: $[-A, A]$ (range of activation values)
* Why it matters: This equation represents the range of activation values that can be used for quantization.

### Equation 3: $\hat{x} = s \cdot \mathrm{round}\left(\frac{\mathrm{clip}(x, -A, A)}{s}\right)$

* Equation: $\hat{x} = s \cdot \mathrm{round}\left(\frac{\mathrm{clip}(x, -A, A)}{s}\right)$
* Symbols: $\hat{x}$ (estimated output), $s$ (scale factor), $x$ (input), $A$ (activation range)
* Why it matters: This equation represents the quantized output of the neural network. It scales the input activation values to the range $[-A, A]$ and then rounds them to the nearest integer.

### Equation 4: $s = \frac{A}{7}$

* Equation: $s = \frac{A}{7}$
* Symbols: $s$ (scale factor), $A$ (activation range)
* Why it matters: This equation represents the scale factor used to scale the input activation values to the range $[-A, A]$.

### Equation 5: $\mathcal{C}$

* Equation: $\mathcal{C}$
* Symbols: $\mathcal{C}$ (set of input values)
* Why it matters: This equation represents the set of input values used to estimate the activation range.

**Method Summary**
==================

* Post-training quantization (PTQ) converts a trained full-precision neural network into a low-precision model without retraining.
* PTQ approximates weights and activations using a small set of discrete values to reduce memory usage and inference cost.
* The reduction in precision becomes particularly significant at low bit widths, and selecting the activation range is a central design decision for reliable low-bit activation quantization.

**Experimental Overview**
========================

* Tasks/Datasets: Daily simple returns are computed from Yahoo Finance adjusted close prices for the S&P 500 constituents from June 2008 through December 2025.
* Baselines/Comparisons: HAR (Holdout Average Rate) and persistence provide classical forecasting baselines to interpret the practical magnitude of the observed IC losses.
* Main Claimed Findings: Activation calibration has little effect at 8 bits but becomes the primary determinant of predictive performance at 4 bits.

**What to Verify in the PDF**
=============================

* The authors' claim that activation calibration has little effect at 8 bits but becomes the primary determinant of predictive performance at 4 bits.
* The results of the walk-forward test years (2018–2025) and the 560 trained models.
* The effect of different activation-calibration strategies on the predictive performance of the models.
{% endraw %}
