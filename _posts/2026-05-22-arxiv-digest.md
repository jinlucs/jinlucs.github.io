---
layout: post
title: "Daily arXiv Digest — 2026-05-22 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Integrable Elasticity via Neural Demand Potentials
- **Authors:** Carlos Heredia, Daniel Roncel
- **arXiv:** [2605.22820](https://arxiv.org/abs/2605.22820v1) · [pdf](https://arxiv.org/pdf/2605.22820v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.22820v1))
- **Categories:** cs.LG

### Abstract
> We propose the Integrable Context-Dependent Demand Network (ICDN), a demand-first neural model for multiproduct retail demand. The model learns log-demand as a smooth, context-conditioned function of log-prices, allowing elasticities to be derived exactly from the learned demand surface. On the Dominick's beer dataset, ICDN improves out-of-sample generalization over a directed log-log benchmark and yields more stable, economically plausible elasticity estimates, especially for weakly identified cross-price effects.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\beta_{ii}(x)u_{i}$

* Equation: $\beta_{ii}(x)u_{i}$
* Symbols: $\beta_{ii}(x)$, $u_{i}$
* Why it matters: This equation represents the own-price elasticity of demand for product $i$ at price $x$. The coefficient $\beta_{ii}(x)$ is a function of the log-price $x$ and the demand for product $i$.

### Equation 2: $w_{ii}(x)^{\top}B_{i}(u_{i})$

* Equation: $w_{ii}(x)^{\top}B_{i}(u_{i})$
* Symbols: $w_{ii}(x)$, $B_{i}(u_{i})$
* Why it matters: This equation represents the demand for product $i$ at price $x$, conditioned on the demand for product $i$. The term $B_{i}(u_{i})$ is a function of the demand for product $i$.

### Equation 3: $\beta_{ij}(x)u_{j}$

* Equation: $\beta_{ij}(x)u_{j}$
* Symbols: $\beta_{ij}(x)$, $u_{j}$
* Why it matters: This equation represents the cross-price elasticity of demand for product $i$ with respect to product $j$ at price $x$. The coefficient $\beta_{ij}(x)$ is a function of the log-price $x$ and the demand for product $j$.

### Equation 4: $w_{ij}(x)^{\top}B_{j}(u_{j})$

* Equation: $w_{ij}(x)^{\top}B_{j}(u_{j})$
* Symbols: $w_{ij}(x)$, $B_{j}(u_{j})$
* Why it matters: This equation represents the demand for product $j$ at price $x$, conditioned on the demand for product $j$. The term $B_{j}(u_{j})$ is a function of the demand for product $j$.

### Equation 5: $B_{i}(u_{i})^{\top}U^{(ij)}(x)B_{j}(u_{j})$

* Equation: $B_{i}(u_{i})^{\top}U^{(ij)}(x)B_{j}(u_{j})$
* Symbols: $B_{i}(u_{i})$, $U^{(ij)}(x)$, $B_{j}(u_{j})$
* Why it matters: This equation represents the elasticity of demand for product $i$ with respect to product $j$ at price $x$. The term $U^{(ij)}(x)$ is a function of the log-price $x$ and the demand for product $j$.

**Method Summary**
================

* The ICDN model learns a context-conditioned demand surface $g_{\theta}(u,x)$, where $u$ is the log-price and $x$ is the context.
* The model-implied elasticity matrix is the Jacobian of the fitted log-demand surface with respect to log-prices.
* The ICDN model is trained with a composite objective that balances predictive accuracy, smoothness of the fitted demand surface, and business plausibility of the implied elasticity matrix.

**Experimental Overview**
=====================

* Tasks: Evaluate ICDN on the Dominick's Finer Foods (DFF) scanner dataset for the beer category.
* Datasets: DFF scanner dataset for the beer category.
* Baselines/Comparisons: Directed log-log benchmark.
* Main claimed findings: ICDN improves out-of-sample generalization and yields more stable model-implied elasticity estimates than the log-log benchmark.

**What to Verify in the PDF**
==========================

* The derivation of the ICDN model's elasticity matrix.
* The evaluation of the ICDN model's performance on the DFF scanner dataset.
* The comparison of the ICDN model's results with the log-log benchmark.
{% endraw %}

{% raw %}
## 2) Vector Policy Optimization: Training for Diversity Improves Test-Time Search
- **Authors:** Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani, Sebastian Risi, Omar Khattab, Zhang-Wei Hong, Pulkit Agrawal
- **arXiv:** [2605.22817](https://arxiv.org/abs/2605.22817v1) · [pdf](https://arxiv.org/pdf/2605.22817v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.22817v1))
- **Categories:** cs.LG, cs.AI, cs.CL, cs.NE

### Abstract
> Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Policy Optimization (VPO), an RL algorithm that explicitly trains policies to anticipate diverse downstream reward functions and to produce diverse solutions. VPO exploits that rewards are often vector-valued in practice, like per-test-case correctness in code generation or, say, multiple different user personas or reward models. VPO is essentially a drop-in replacement for the GRPO advantage estimator, but it trains the LLM to output a set of solutions where individual solutions specialize to different trade-offs in the vector reward space. Across four tasks, VPO matches or beats the strongest scalar RL baselines on test-time search (e.g. pass@k and best@k), with the gap widening as the search budget grows. For evolutionary search, VPO models unlock problems that GRPO models cannot solve at all. As test-time search becomes more standardized, optimizing for diversity may need to become the default post-training objective.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: πθ(⋅|x)

πθ(⋅|x) represents the policy output for a given input x, parameterized by θ.

* Equation: πθ(⋅|x)
* Symbols: πθ, ⋅, |, x, θ
* Why it matters: This equation represents the output of the policy network, which is crucial for making decisions in the environment.

### Equation 2: r(x,y) = [r1(x,y), ..., rd(x,y)] ∈ ℝd

r(x,y) represents the reward function for a given state x and action y, which is a vector-valued function.

* Equation: r(x,y) = [r1(x,y), ..., rd(x,y)]
* Symbols: r, x, y, d, ℝd
* Why it matters: This equation represents the reward function, which is used to evaluate the performance of the policy.

### Equation 3: ri

ri represents the individual components of the reward function.

* Equation: ri
* Symbols: ri
* Why it matters: This equation represents the individual components of the reward function, which are used to compute the overall reward.

### Equation 4: w ∈ Δd-1

w represents a distribution over the individual components of the reward function.

* Equation: w ∈ Δd-1
* Symbols: w, d, Δd-1
* Why it matters: This equation represents a distribution over the individual components of the reward function, which is used to compute the weighted sum of the rewards.

### Equation 5: w⊙r(x,y)

w⊙r(x,y) represents the weighted sum of the rewards.

* Equation: w⊙r(x,y)
* Symbols: w, r, x, y
* Why it matters: This equation represents the weighted sum of the rewards, which is used to compute the overall reward.

**Method Summary**
==================

* **Vector Policy Optimization (VPO)**: VPO is an RL algorithm that explicitly trains policies to anticipate diverse downstream reward functions and to produce diverse solutions.
* **Two key components**: (1) training a model to generate multiple candidate completions per prompt within a single autoregressive rollout, and (2) replacing a fixed reward weighting with a distribution over weights.
* **Set-level objective**: VPO defines a set-level objective that rewards the model for producing diverse, high-quality solutions.

**Experimental Overview**
=========================

* **Tasks/Datasets**: Four domains chosen to span distinct shapes of multi-objective structure: (i) binary vs. continuous reward components, and (ii) hand-crafted vs. metric-based reward shapes.
* **Baselines/Comparisons**: Scalar GRPO and best@k.
* **Main Claimed Findings**: VPO consistently improves best@k relative to scalar baselines, while GRPO quickly saturates as k increases.

**What to Verify in the PDF**
=============================

* **Detailed reward function**: Verify the detailed reward function used in the experiments, including the reward components and the distribution over weights.
* **Autoregressive rollout**: Verify the details of the autoregressive rollout used to generate candidate completions.
* **Search procedure**: Verify the details of the search procedure used to evaluate the performance of the policies, including the best@k metric.
{% endraw %}

{% raw %}
## 3) Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration
- **Authors:** Lily Goli, Justin Kerr, Daniele Reda, Alec Jacobson, Andrea Tagliasacchi, Angjoo Kanazawa
- **arXiv:** [2605.22814](https://arxiv.org/abs/2605.22814v1) · [pdf](https://arxiv.org/pdf/2605.22814v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.22814v1))
- **Categories:** cs.LG

### Abstract
> Exploration is a prerequisite for learning useful behaviors in sparse-reward, long-horizon tasks, particularly within 3D environments. Curiosity-driven reinforcement learning addresses this via intrinsic rewards derived from the mismatch between the agent's predictive model of the world and reality. However, translating this intrinsic motivation to complex, photorealistic environments remains difficult, as agents can become trapped in local loops and receive fresh rewards for revisiting forgotten states. In this work, we demonstrate that this failure stems from a lack of spatial persistence and episodic context. We show that effective curiosity requires a model of the world that is persistent and continuously updated, paired with an agent that maintains an episodic trajectory history to navigate toward novel regions. We achieve this using an online 3D reconstruction as a persistent model of the world, while the agent policy is parameterized as a sequence model over RGB observations to maintain episodic context. This design enables effective exploration during training while allowing the agent to navigate using solely RGB frames at deployment. Trained purely via curiosity on HM3D, our agent outperforms RL-based active mapping baselines and generalizes zero-shot to Gibson and AI-generated worlds. Our end-to-end policy enables efficient adaptation to downstream tasks, such as apple picking and image-goal navigation, outperforming from-scratch baselines. Please see video results at https://recuriosity.github.io/.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 1{<}t{<}N

* Equation: 1{<}t{<}N
* Symbols: t, N
* Why it matters: This equation represents the time step t and the total number of time steps N. It is likely used to define the scope of the exploration process.

### Equation 2: a_{t}

* Equation: a_{t}
* Symbols: a_{t}, t
* Why it matters: This equation represents the action taken by the agent at time step t. It is likely used to define the agent's behavior in the 3D environment.

### Equation 3: \mathcal{E}

* Equation: \mathcal{E}
* Symbols: \mathcal{E}
* Why it matters: This equation represents the environment or the 3D scene that the agent is interacting with. It is likely used to define the agent's interaction with the environment.

### Equation 4: o_{t+1}

* Equation: o_{t+1}
* Symbols: o_{t+1}, t
* Why it matters: This equation represents the new observation or state of the environment at time step t+1. It is likely used to define the agent's perception of the environment.

### Equation 5: \tilde{o}_{t+1}

* Equation: \tilde{o}_{t+1}
* Symbols: \tilde{o}_{t+1}, t
* Why it matters: This equation represents the augmented observation or privileged sensory information at training time. It is likely used to define the agent's access to additional information during training.

**Method Summary**
==================

* Our method consists of two key parts: a long-context transformer-based agent architecture and a curiosity module based on 3D reconstruction.
* The agent takes in a stream of RGB observations from the 3D environment and outputs local camera motion per-timestep.
* The curiosity module builds a photorealistic 3D scene reconstruction from the agent's stream of observations and uses the disagreement between novel view renders and ground truth observation as reward.
* The agent maintains internal memory long enough to enable it to discover exploration strategies like backtracking.

**Experimental Overview**
========================

* Tasks: We perform an experimental analysis of our curiosity-driven exploration on two tasks: indoor scene exploration and downstream navigation tasks (apple-picking and image-goal navigation).
* Datasets: We use the HM3D evaluation dataset.
* Baselines: We compare our agent to active-mapping baselines (OccAnt-RGBD and ANS-depth).
* Main claimed findings: Our agent achieves greater 3D completeness faster than all baselines, while requiring only RGB input at test time.

**What to Verify in the PDF**
=============================

* The implementation details of the 3D reconstruction and the curiosity module.
* The effect of memory capacity variations on the agent's exploration behavior.
* The results of the ablation study on the necessity of the agent's episodic memory and world persistence.
{% endraw %}

{% raw %}
## 4) The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning
- **Authors:** Vishal Rajput
- **arXiv:** [2605.22800](https://arxiv.org/abs/2605.22800v1) · [pdf](https://arxiv.org/pdf/2605.22800v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.22800v1))
- **Categories:** cs.LG, cs.AI, stat.ML

### Abstract
> Robustness, domain adaptation, photometric and occlusion invariance, compositional generalisation, temporal robustness, alignment safety, and classical anisotropic regularisation are usually treated as separate problems with separate method families. This paper argues that much of their shared structure is one statistical problem: estimate the covariance of label-preserving deployment nuisance, then regularise the encoder Jacobian along a matrix whose range covers that covariance (the matching principle). CORAL, adversarial training, IRM, augmentation, metric learning, Jacobian penalties, and alignment-style constraints are different estimators of that object, not independent robustness tricks. In the linear-Gaussian model we prove closed-form optimality (Theorem A), including cube-root water-filling within the matched range; necessity of range coverage for quadratic Jacobian penalties (Theorem G); the same range dichotomy at deep global minima; and two falsification controls (Lemma C; Corollaries E), with seven conditional consistency lemmas (D1-D7) for estimation under standard identifiability assumptions. We introduce the Trajectory Deviation Index (TDI), a label-free probe of embedding sensitivity when task accuracy or Jacobian Frobenius norm is insufficient. Thirteen pre-registered blocks from classical ML through Qwen2.5-7B test the predicted matched, then isotropic, then wrong-W ordering on geometry and deployment drift; twelve pass, and the sole exception (Office-31) is an eigengap failure named before the run. At 7B scale, matched style-PMH improves selective honesty and preserves Style TDI where standard DPO degrades it. The contribution is naming the deployment nuisance covariance, stating what the regulariser must do, and supplying a closed-form falsifiable theory once that object is identified, not universality on every leaderboard.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Σtask = CovQn(n)

* Equation: Σtask = CovQn(n)
* Symbols: Σtask (covariance of label-preserving deployment nuisance), CovQn(n) (covariance of label-preserving deployment nuisance)
* Why it matters: This equation represents the covariance of the label-preserving deployment nuisance, which is the statistical problem that the matching principle aims to solve.

### Equation 2: Σ′

* Equation: Σ′
* Symbols: Σ′ (matrix whose range covers the range of Σtask)
* Why it matters: This equation represents the matrix whose range covers the range of Σtask, which is used to regularize the encoder Jacobian.

### Equation 3: range(Σtask)

* Equation: range(Σtask)
* Symbols: range(Σtask) (range of Σtask)
* Why it matters: This equation represents the range of Σtask, which is the set of all possible values that Σtask can take.

### Equation 4: {}∗global

* Equation: {}∗global
* Symbols: {}∗global (global minimum of the encoder Jacobian)
* Why it matters: This equation represents the global minimum of the encoder Jacobian, which is used to evaluate the performance of the matching principle.

### Equation 5: ‖J‖F

* Equation: ‖J‖F
* Symbols: ‖J‖F (Frobenius norm of the encoder Jacobian)
* Why it matters: This equation represents the Frobenius norm of the encoder Jacobian, which is used to evaluate the performance of the matching principle.

**Method Summary**
================

* The matching principle is a geometric theory of loss functions for nuisance-robust representation learning.
* It identifies the common population object that methods are estimating and regularizes the encoder Jacobian along a matrix Σ′ whose range covers the range of Σtask.
* The matching principle unifies various methods, including CORAL, adversarial training, IRM, augmentation, metric learning, and Jacobian penalties.
* It provides a closed-form, falsifiable theory for estimating the covariance of the label-preserving deployment nuisance.

**Experimental Overview**
=====================

* The authors use the Perturbation Matching Hypothesis (PMH) framework to evaluate the performance of the matching principle.
* They report results on 13 pre-registered blocks from classical ML through Qwen2.5-7B.
* The main claimed findings include:
	+ The matching principle improves selective honesty and preserves Style tdi in a controlled alignment regime.
	+ Standard dpo degrades it, but the matching principle improves it.
	+ The authors report diagnostic results from the experiment, including task metrics and diagnostic results.

**What to Verify in the PDF**
==========================

* The authors claim that the matching principle improves selective honesty and preserves Style tdi in a controlled alignment regime. Verify this claim by examining the results of the experiment and the diagnostic results.
* The authors report that standard dpo degrades the performance of the matching principle. Verify this claim by examining the results of the experiment and the diagnostic results.
* The authors claim that the matching principle provides a closed-form, falsifiable theory for estimating the covariance of the label-preserving deployment nuisance. Verify this claim by examining the mathematical derivations and the experimental results.
{% endraw %}

{% raw %}
## 5) Finite-Particle Convergence Rates for Conservative and Non-Conservative Drifting Models
- **Authors:** Krishnakumar Balasubramanian
- **arXiv:** [2605.22795](https://arxiv.org/abs/2605.22795v1) · [pdf](https://arxiv.org/pdf/2605.22795v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.22795v1))
- **Categories:** stat.ML, cs.AI, cs.LG, math.ST

### Abstract
> We propose and analyze a conservative drifting method for one-step generative modeling. The method replaces the original displacement-based drifting velocity by a kernel density estimator (KDE)-gradient velocity, namely the difference of the kernel-smoothed data score and the kernel-smoothed model score. This velocity is a gradient field, addressing the non-conservatism issue identified for general displacement-based drifting fields. We prove continuous-time finite-particle convergence bounds for the conservative method on $\R^d$: a joint-entropy identity yields bounds for the empirical Stein drift, the smoothed Fisher discrepancy of the KDE, and the squared center velocity. The main finite-particle correction is a reciprocal-KDE self-interaction term, and we give deterministic and high-probability local-occupancy conditions under which this term is controlled. We keep the quadrature constants explicit and track their possible bandwidth dependence: the root residual-velocity rate $N^{-1/(d+4)}$ holds under an additional $h$-uniform quadrature regularity condition, while a more general growth condition yields the optimized root rate $N^{-(2-β)/(2(d+4-β))}$, where $0\le β<2$. We also analyze the non-conservative drifting method with Laplace kernel, corresponding to the original displacement-based velocity proposed in~\cite{deng2026drifting}. For this method, a sharp companion kernel decomposes the velocity into a positive scalar preconditioning of a sharp-score mismatch plus a Laplace scale-mismatch residual, producing an analogous finite-particle rate with an unavoidable residual term. Finally, we explain how the continuous-time residual-velocity bounds translate into one-step generation guarantees through the explicit drift size $η$.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: ℝ^{d}

* Equation: ℝ^{d}
* Symbols: None
* Why it matters: This is the notation for the d-dimensional Euclidean space, which is used to describe the setting of the paper.

### Equation 2: N^{-1/(d+4)}

* Equation: N^{-1/(d+4)}
* Symbols: N (quadrature constant), d (dimensionality)
* Why it matters: This is a rate bound for the conservative drifting method, which depends on the quadrature constant N and the dimensionality d.

### Equation 3: N^{-(2-\beta)/(2(d+4-\beta))}

* Equation: N^{-(2-\beta)/(2(d+4-\beta))}
* Symbols: N (quadrature constant), d (dimensionality), β (parameter)
* Why it matters: This is another rate bound for the conservative drifting method, which depends on the quadrature constant N, dimensionality d, and a parameter β.

### Equation 4: 0 ≤ β < 2

* Equation: 0 ≤ β < 2
* Symbols: β (parameter)
* Why it matters: This is a constraint on the parameter β, which is used to bound the rate of convergence of the conservative drifting method.

### Equation 5: η

* Equation: η
* Symbols: η (drift size)
* Why it matters: This is the drift size, which is a measure of the distance between the target and model distributions.

### Equation 6: K_{h}

* Equation: K_{h}
* Symbols: h (bandwidth), K (kernel)
* Why it matters: This is the kernel density estimator (KDE) with bandwidth h, which is used to smooth the data and model distributions.

### Equation 7: α

* Equation: α
* Symbols: α (probability measure)
* Why it matters: This is a probability measure on ℝ^{d}, which is used to define the Laplace KDE.

**Method Summary**
==================

* The paper proposes a conservative drifting method for one-step generative modeling, which replaces the original displacement-based drifting velocity with a kernel density estimator (KDE)-gradient velocity.
* The method is analyzed using a joint-entropy identity, which yields bounds for the empirical Stein drift, the smoothed Fisher discrepancy of the KDE, and the squared center velocity.
* The main finite-particle correction is a reciprocal-KDE self-interaction term, which is controlled under deterministic and high-probability local-occupancy conditions.
* The paper also analyzes the non-conservative drifting method with Laplace kernel, which is shown to have a similar finite-particle rate with an additional scale-mismatch residual.

**Experimental Overview**
=========================

* Tasks/Datasets: The paper does not specify a particular task or dataset, but it mentions that the leave-one-out Laplace theorem has a different bandwidth tradeoff from the conservative theorem.
* Baselines/Comparisons: The paper compares the conservative and non-conservative drifting methods, but it does not provide a specific baseline.
* Main Claimed Findings: The paper claims to have established finite-particle convergence bounds for the conservative and non-conservative drifting methods, which depend on the quadrature constant N, dimensionality d, and a parameter β.

**What to Verify in the PDF**
=============================

* The proof of the finite-particle convergence bounds for the conservative drifting method, which appears to involve a joint-entropy identity and a reciprocal-KDE self-interaction term.
* The analysis of the non-conservative drifting method with Laplace kernel, which involves a sharp companion kernel decomposition and a scale-mismatch residual.
* The bandwidth and step-size choices for the non-conservative drifting method with Laplace kernel, which appear to involve a leave-one-out Laplace theorem and a quadrature error bound.
{% endraw %}
