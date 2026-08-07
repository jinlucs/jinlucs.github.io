---
layout: post
title: "Daily arXiv Digest — 2026-08-07 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games
- **Authors:** Boning Li, Yu Chen, Longbo Huang
- **arXiv:** [2608.06362](https://arxiv.org/abs/2608.06362v1) · [pdf](https://arxiv.org/pdf/2608.06362v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.06362v1))
- **Categories:** cs.GT, cs.AI, cs.CL, cs.LG, cs.MA

### Abstract
> Deciding which of two agents is stronger means playing games until skill outweighs luck, and every game costs money, model inference, or expert time. Since the number of games needed is unknown, fixed-budget evaluations either keep paying after the result is settled or stop before the agents can be told apart, while naive optional stopping with an ordinary confidence interval invalidates the stated level. We make such an evaluation stop as soon as its evidence suffices, with the guarantee intact. The Action-Informed Value Assessment Tool (AIVAT) reduces variance in imperfect-information games through conditional mean-zero corrections, by a median $54\times$ across 15 LLM agent configurations spanning 71,439 paired Heads-Up No-Limit Hold'em (HUNL) hands, but does not say when to stop. We combine AIVAT with continuously monitored Confidence Sequences (CSs) into anytime-valid AIVAT (AV-AIVAT), whose online value model learns only from past games so that no game scores its own correction. At the nominal 95\% level and a target precision of $\pm1$ Big Blind, raw outcomes need a median $74\times$ as many hands as AIVAT-corrected outcomes to stop under the Asymptotic CS (AsympCS). Exact finite-sample certification uses the Empirical-Bernstein CS (EB-CS), which needs an independently justified bound on corrected payoffs. We establish such a bound structurally for Leduc hold'em and characterize a width floor set by the CS's bet cap and that bound, which governs how much of a variance gain becomes earlier stopping; the descriptive HUNL EB-CS runs show a median $1.37\times$ stopping-time ratio. AV-AIVAT turns variance reduction into efficient, auditable early stopping while separating asymptotic screening from exact certification, so an evaluation can stop the moment its evidence suffices and hand a third party everything needed to recheck the verdict at that very stopping time.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 74 ×
```markdown
74 ×
```
* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 2: 54 ×
```markdown
54 ×
```
* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Reduces variance in imperfect-information games by a median 54 × 54 across 15 LLM agent configurations

### Equation 3: ± 1
```markdown
± 1
```
* Equation: Not explicitly defined in the context
* Symbols: ± (plus-minus) and 1
* Why it matters: Represents the target precision of ± 1 Big Blind (BB) in the nominal 95% level

### Equation 4: 1.37 ×
```markdown
1.37 ×
```
* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Represents the median stopping-time ratio of the descriptive HUNL EB-CS runs

### Equation 5: 99.98%
```markdown
99.98%
```
* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 6: v_t
```markdown
v_t
```
* Equation: Not explicitly defined in the context
* Symbols: v_t (not found in extracted context)
* Why it matters: Not found in extracted context

### Equation 7: 1:t-1
```markdown
1{:}t{-}1
```
* Equation: Not explicitly defined in the context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

**Method Summary**
==================

* The authors propose AV-AIVAT, a method that combines AIVAT with Confidence Sequences (CSs) to reduce variance in imperfect-information games.
* AV-AIVAT uses a predictable interface to update the value function from an adaptively growing evaluation stream.
* The method provides a certified anytime-valid stopping criterion, allowing for early stopping while maintaining the guarantee of the stated level.
* AV-AIVAT reduces variance by a median 54 × 54 across 15 LLM agent configurations.

**Experimental Overview**
=========================

* Tasks/Datasets: Heads-Up No-Limit Hold'em (HUNL) games
* Baselines/Comparisons: AIVAT, Confidence Sequences (CSs), and baseline control variates
* Main Claimed Findings: AV-AIVAT reduces variance by a median 54 × 54 across 15 LLM agent configurations, and achieves a median 74 × 74 × reduction in raw outcomes needed to stop under the Asymptotic CS (AsympCS) setting.

**What to Verify in the PDF**
=============================

* The derivation and boundary of the design proxy (Section B.3)
* The analysis status and common settings (Section D.1)
* The experimental settings and results (e.g., the number of games played, the target precision, and the stopping criterion)
{% endraw %}

{% raw %}
## 2) CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks
- **Authors:** Fanzhe Meng, Guoxin Chen, Jiale Zhao, Shuang Sun, Zhiyu Lin, Wayne Xin Zhao, Ruihua Song, Ji-Rong Wen, Kai Jia
- **arXiv:** [2608.06352](https://arxiv.org/abs/2608.06352v1) · [pdf](https://arxiv.org/pdf/2608.06352v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.06352v1))
- **Categories:** cs.LG, cs.CL

### Abstract
> Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting. In this paper, we present CalibForge, an autonomous terminal-task synthesis system that uses verified solver behavior to revise candidate tasks through adversarial solver calibration. Multi-solver calibration targets disagreement within a heterogeneous solver pool, whereas contrastive solver calibration targets a designated strong-pass/weak-fail relation; both operationalize a solver-relative learnable zone anchored in demonstrated solvability. Using CalibForge, we construct 5,431 calibrated terminal tasks. Our ablations show that both strategies yield more effective supervision than authoring and validation alone or ordinary single-solver feedback. Models trained on the full collection achieve 32.58% and 47.57% on Terminal-Bench 2.0. The largest improvements over the corresponding base model reach 24.71 percentage points on Terminal-Bench 2.0, 27.68 points on SWE-bench Pro, and 30.04 points on Doc2Repo. Together, these results support solver-relative learnability as a practical target for constructing effective and transferable agent training data.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: τ

* Equation: τ
* Symbols: τ (unknown variable)
* Why it matters: τ represents a candidate terminal task, which is the input to the CalibForge system.

### Equation 2: V(τ)

* Equation: V(τ) = V(\tau)
* Symbols: V(τ) (verification function), τ (candidate terminal task)
* Why it matters: V(τ) indicates whether the candidate task τ is valid and solvable.

### Equation 3: γ

* Equation: γ
* Symbols: γ (calibration specification)
* Why it matters: γ defines the solver setting and behavioral retention criterion for the author-solver loop.

### Equation 4: C γ

* Equation: C γ
* Symbols: C γ (calibration criterion)
* Why it matters: C γ is the retention criterion that determines whether a task is retained or discarded.

### Equation 5: R max

* Equation: R max = 50
* Symbols: R max (maximum number of calibration rounds)
* Why it matters: R max limits the number of calibration rounds for each candidate task.

**Method Summary**
================

* CalibForge uses an autonomous terminal-task synthesis system to generate calibrated terminal tasks.
* The system consists of an authoring agent and a solver pool, which are used to revise and validate candidate tasks.
* The authoring agent constructs candidate tasks, validates their structure, and attempts to solve them.
* The solver pool provides feedback on the candidate tasks, which is used to revise and revalidate the tasks.
* The system uses adversarial solver calibration to target disagreement within the solver pool.

**Experimental Overview**
=====================

* Tasks/Datasets: CalibForge generates 5,431 calibrated terminal tasks using a combination of multi-solver calibration and contrastive solver calibration.
* Baselines/Comparisons: The authors compare the performance of CalibForge with baseline task sets and evaluate the effectiveness of the synthesized data.
* Main Claimed Findings: CalibForge achieves state-of-the-art performance on Terminal-Bench 2.0 and improves over baseline models on SWE-bench Pro and Doc2Repo.

**What to Verify in the PDF**
==========================

* The implementation details of the authoring agent and the solver pool.
* The evaluation protocol for the synthesized data, including the choice of evaluation metrics and the selection of tasks for evaluation.
* The results of the failure analysis of trained models, including the identification of distinct failure mechanisms and the analysis of trajectory inspection results.
{% endraw %}

{% raw %}
## 3) Scalable estimation of VARMA models
- **Authors:** Daniel Paulin, Victor Elvira
- **arXiv:** [2608.06340](https://arxiv.org/abs/2608.06340v1) · [pdf](https://arxiv.org/pdf/2608.06340v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.06340v1))
- **Categories:** stat.ML, cs.LG, math.ST

### Abstract
> Vector autoregressive moving-average (VARMA) models have long been considered impractical beyond moderate dimensions: the likelihood is non-convex, the parametrization is identified only up to equivalence, and every evaluation costs a pass over the entire series. Yet their moving-average term captures with a few parameters what a pure autoregression matches only with many lags. We introduce an estimation framework that removes this computational barrier: each optimization iteration is independent of the series length $T$. The framework combines a partial-autocorrelation reparametrization that guarantees stationarity and invertibility by construction, Gaussian priors on the reparametrized coefficients with separate scales for diagonal and off-diagonal entries, and losses that depend on the data only through fixed-size sufficient statistics, evaluated by a Parseval (Fourier) identity at near-linear cost in the truncation length. This yields two point estimators: a regularized least-squares fit and a covariance-marginalized maximum-a-posteriori estimator. We prove that both recover the infinite-autoregressive representation of the true process at a near-parametric rate in fixed dimension, so the truncation introduces no asymptotic bias. The same machinery extends, at the same leading cost, to seasonal dynamics, exogenous regressors (VARMAX), and rolling-window refits. Empirically, the estimators stay close to the oracle forecast error from $d=10$ to $d=40$ (where classical conditional MLE returns non-invertible fits whose forecasts diverge) and match or beat VAR, Bayesian-VAR, component-wise ARMA, and sparse-VARMA baselines on retail-demand, meteorological, and air-quality data. This brings likelihood-based VARMA estimation, at a per-iteration cost independent of the series length, to the problem sizes where practitioners have so far relied on VAR models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1. Formula Walkthrough**
### Equation 1: d=10
\[ d = 10 \]
Symbols: \( d \) (series length)
Why it matters: This equation represents the series length for a specific experiment.

### Equation 2: d=40
\[ d = 40 \]
Symbols: \( d \) (series length)
Why it matters: This equation represents the series length for another specific experiment.

### Equation 3: (p,q)
\[ (p, q) \]
Symbols: \( p \) (number of autoregressive terms), \( q \) (number of moving-average terms)
Why it matters: This equation represents the parameters of a VARMA model.

### Equation 4: O(T)
\[ O(T) \]
Symbols: \( T \) (series length)
Why it matters: This equation represents the computational complexity of the recursive evaluation of the conditional likelihood.

### Equation 5: \boldsymbol{S}_{2}
\[ \boldsymbol{S}_{2} \]
Symbols: \( \boldsymbol{S}_{2} \) (second-moment block)
Why it matters: This equation represents a block of the materialised second-moment tensor.

**2. Method Summary**
* The authors introduce a scalable estimation framework for dense VARMA models.
* The framework combines a partial-autocorrelation reparametrization, penalized least-squares, and covariance-marginalized losses.
* The authors prove that both estimators recover the infinite-autoregressive representation of the true process at a near-parametric rate in fixed dimension.
* The framework is extended to seasonal dynamics, exogenous regressors, and rolling-window refits.

**3. Experimental Overview**
* Tasks: The authors evaluate their framework on retail-demand, meteorological, and air-quality data.
* Baselines: The authors compare their framework with VAR, Bayesian-VAR, component-wise ARMA, and sparse-VARMA baselines.
* Main claimed findings: The authors claim that their framework outperforms the baselines in terms of forecast error and scalability.

**4. What to Verify in the PDF**
* The authors claim that the sufficient statistics drive the nonlinear VARMA problem as well. Verify this claim in the PDF.
* The authors prove that both estimators recover the infinite-VAR representation at a near-parametric rate in fixed dimension. Verify this proof in the PDF.
* The authors discuss the identifiability issues that they do not address. Verify this discussion in the PDF.
{% endraw %}

{% raw %}
## 4) RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction
- **Authors:** Chenglong Wang, Ziming Zhu, Yifu Huo, Bei Li, Qiaozhi He, Yan Ding, Xiaoyang Hao, Yuxin Gao, Tianhua Zhou, Xiaojia Chang, Tongran Liu, Jingbo Zhu
- **arXiv:** [2608.06310](https://arxiv.org/abs/2608.06310v1) · [pdf](https://arxiv.org/pdf/2608.06310v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.06310v1))
- **Categories:** cs.LG, cs.CL

### Abstract
> Recent advances in reward modeling show a paradigm shift from discriminative reward models to generative reward models. However, despite their strong capabilities in response ranking, generative reward models have not realized their potential in reinforcement learning (RL). Our analysis reveals that this limitation arises from a mismatch between the comparative nature of generative reward modeling and the scalar scoring paradigm adopted by existing RL algorithms. To bridge this gap, we propose a Ranking-based Reward Construction (RRC) approach, which enables generative reward models to provide more effective RL learning signals by deriving rewards from relative preference rankings. RRC introduces two complementary strategies: self-competitive ranking, which exploits comparisons among sampled responses, and anchor-guided ranking, which enables scalable ranking-based reward construction with a small set of reference responses. Experiments across open-ended chat and reasoning benchmarks demonstrate that RRC substantially improves RL training with generative reward models, achieving consistent gains over existing reward construction approaches. Our code can be found at https://github.com/wangclnlp/RRC.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Not found in extracted context.

### Equation 2: 
\[ \mathcal{O}(m\cdot\log m) \]
Symbols: \( m \), \( \mathcal{O} \) (Big O notation)
Why it matters: This equation represents the time complexity of the self-competitive ranking (SCR) approach, indicating that the time required grows linearly with the number of votes.

### Equation 3: 
\[ \mathcal{O}(m\cdot n) \]
Symbols: \( m \), \( n \), \( \mathcal{O} \) (Big O notation)
Why it matters: This equation represents the time complexity of the anchor-guided ranking (AGR) approach, indicating that the time required grows linearly with the number of anchors.

### Equation 4: 
\[ r_{\phi}(x,y) \]
Symbols: \( r_{\phi} \), \( x \), \( y \), \( \phi \)
Why it matters: This equation represents the reward function \( r_{\phi} \) that takes in input \( x \) and response \( y \) and is parameterized by \( \phi \), indicating how rewards are constructed from generative reward models.

**Method Summary**
================

* The proposed RRC approach leverages the comparative strengths of generative reward models in RL by deriving rewards from relative preference rankings.
* The approach consists of two complementary strategies: self-competitive ranking (SCR) and anchor-guided ranking (AGR).
* SCR exploits comparisons among sampled responses, while AGR enables scalable ranking-based reward construction with a small set of reference responses.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Open-ended chat benchmarks: AlpacaEval2, ArenaHardV2, WildBench
	+ Knowledge and math reasoning benchmarks: MMLU-Redux, MATH-500
* Baselines/Comparisons:
	+ Discriminative reward models (DRM)
	+ Generative reward models with probability-based reward construction (GRM w/ PRC)
* Main Claimed Findings:
	+ RRC approaches consistently outperform all baselines by a clear margin.
	+ Constructing rewards from rankings rather than token probabilities is substantially more effective for generative reward models in RL.
	+ Majority voting mechanism further boosts performance.

**What to Verify in the PDF**
=============================

* The implementation details of the self-competitive ranking (SCR) and anchor-guided ranking (AGR) approaches.
* The evaluation of the proposed RRC approach on different benchmark datasets and comparison to existing baselines.
* The analysis of the trade-off between computational cost and performance in the RRC approach.
{% endraw %}

{% raw %}
## 5) Surv-IPTB: An Attention-Based Model for Estimating Individual Probability of Treatment Benefit with Survival Data
- **Authors:** Lev V. Utkin, Stanislav K. Kogan, Andrei V. Konstantinov
- **arXiv:** [2608.06288](https://arxiv.org/abs/2608.06288v1) · [pdf](https://arxiv.org/pdf/2608.06288v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.06288v1))
- **Categories:** cs.LG, stat.ML

### Abstract
> This work presents a novel attention-based framework for estimating the Individual Probability of Treatment Benefit (IPTB) in survival analysis contexts. The proposed model, called Surv-IPTB, directly quantifies the probability that a specific patient will experience extended survival time under treatment versus control. We reformulate IPTB estimation as a binary classification problem, leveraging pairwise patient comparisons across treatment and control cohorts. The framework incorporates a principled handling of right-censored observations through imprecise probability representations, where uncertain treatment effects are characterized by interval-valued probabilities. An attention mechanism with learnable query-key transformations enables flexible, data-driven aggregation of pairwise comparisons, while simultaneously learning soft class probabilities for censored cases. Through extensive experiments on synthetic datasets with complex nonlinear structures, including spiral, bell-shaped, and circular feature spaces, we demonstrate that our approach maintains robust performance across varying censoring rates and treatment effect strengths. The model consistently outperforms meta-learner baselines (T-learner and S-learner) equipped with random survival forests, Cox proportional hazards, and Beran estimators, particularly in challenging nonlinear scenarios where conventional methods exhibit significant degradation. The results establish the proposed attention-based framework as a scalable and statistically principled solution for personalized treatment benefit assessment in survival settings. The code implementing the model is publicly available.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: X = \mathbf{x}

* Equation: X = \mathbf{x}
* Symbols: X (potential outcome under control), \mathbf{x} (covariate vector)
* Why it matters: This equation represents the potential outcome under control, which is the true latent survival time under treatment.

### Equation 2: \rho(\mathbf{x}) = \Pr\{H>Y \mid X=\mathbf{x}\} = \Pr\{\Delta>0 \mid X=\mathbf{x}\}

* Equation: \rho(\mathbf{x}) = \Pr\{H>Y \mid X=\mathbf{x}\} = \Pr\{\Delta>0 \mid X=\mathbf{x}\}
* Symbols: \rho(\mathbf{x}) (probability of treatment benefit), H (potential outcome under treatment), Y (potential outcome under control), \mathbf{x} (covariate vector), \Delta (treatment effect)
* Why it matters: This equation represents the probability of treatment benefit, which is the probability that a patient will experience extended survival time under treatment versus control.

### Equation 3: \Delta = H - Y

* Equation: \Delta = H - Y
* Symbols: \Delta (treatment effect), H (potential outcome under treatment), Y (potential outcome under control)
* Why it matters: This equation represents the treatment effect, which is the difference between the potential outcomes under treatment and control.

### Equation 4: \Pr\{\Delta>0 \mid X=\mathbf{x}\}

* Equation: \Pr\{\Delta>0 \mid X=\mathbf{x}\}
* Symbols: \Pr\{\Delta>0 \mid X=\mathbf{x}\} (probability of treatment benefit given covariate vector \mathbf{x})
* Why it matters: This equation represents the probability of treatment benefit given a specific covariate vector, which is used to estimate the individual probability of treatment benefit.

### Equation 5: (h_i, y_j)

* Equation: (h_i, y_j)
* Symbols: h_i (observed outcome under treatment), y_j (observed outcome under control)
* Why it matters: This equation represents the observed outcomes under treatment and control, which are used to estimate the treatment effect.

**Method Summary**
==================

* The proposed model, Surv-IPTB, is an attention-based framework for estimating the individual probability of treatment benefit with survival data.
* The model reformulates IPTB estimation as a binary classification problem, leveraging pairwise patient comparisons across treatment and control cohorts.
* The framework incorporates a principled handling of right-censored observations through imprecise probability representations.
* An attention mechanism with learnable query-key transformations enables flexible, data-driven aggregation of pairwise comparisons.
* The model is evaluated on synthetic datasets with complex nonlinear structures, including spiral, bell-shaped, and circular feature spaces.

**Experimental Overview**
=========================

* Tasks/Datasets: The experiments evaluate model performance on synthetic datasets with complex nonlinear structures.
* Baselines/Comparisons: The model is compared to six distinct baselines, including T-learner, S-learner, Random Survival Forests, Cox proportional hazards model, and Beran estimator with Gaussian kernels.
* Main Claimed Findings: The model consistently outperforms the baselines, particularly in challenging nonlinear scenarios where conventional methods exhibit significant degradation.

**What to Verify in the PDF**
=============================

* The implementation details of the attention mechanism and imprecise probability representations.
* The evaluation of the model on real-world datasets, including the dataset used for the experiments.
* The theoretical guarantees of the model, including the convergence of the optimization algorithm and the accuracy of the estimated treatment effect.
{% endraw %}
