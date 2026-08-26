---
layout: post
title: "Daily arXiv Digest — 2026-08-26 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Bellman Calibration for Marginalized Importance Weighting in Offline Reinforcement Learning
- **Authors:** Lars van der Laan, Nathan Kallus
- **arXiv:** [2608.24858](https://arxiv.org/abs/2608.24858v1) · [pdf](https://arxiv.org/pdf/2608.24858v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.24858v1))
- **Categories:** cs.LG, stat.ML

### Abstract
> Marginalized importance weighting evaluates a target policy by reweighting offline state-action samples with its discounted occupancy ratio, characterized by an adjoint Bellman equation. Existing minimax, primal-dual, and fitted fixed-point estimators can leave residual occupancy-balance violations because of function-class approximation, regularization, or incomplete optimization. These violations are difficult to diagnose and reduce because the objectives generally lack a direct supervised validation loss for hyperparameter tuning, model selection, and early stopping. We introduce isotonic Bellman calibration, a one-dimensional, model-agnostic post-processing method that reduces these violations while preserving the ranking information in any initial occupancy-ratio estimate. The method corrects the estimate's scale and shape by applying fitted occupancy-ratio evaluation (FORE) over a one-dimensional class of nondecreasing transformations. We characterize Bellman calibration as a conditional fixed-point property equivalent to occupancy-balance against every test function of the calibrated ratio. More generally, we derive a calibration-refinement bound showing that any fitted ratio with small calibration error performs nearly as well as the best post-processing based on its fitted values. For isotonic Bellman calibration, we establish finite-sample calibration guarantees and a KL oracle inequality relative to the best monotone transformation of the initial estimate. Consequently, isotonic Bellman calibration achieves small calibration error and KL risk within statistical error of the best monotone correction, with guarantees for downstream target-occupancy functionals, including policy-value estimation.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: Not found in extracted context.

### Equation 2: γ=0
* Equation: γ=0
* Symbols: γ (discount factor)
* Why it matters: The discount factor is a hyperparameter that determines the importance of future rewards. Setting γ=0 implies that future rewards are not considered.

### Equation 3: (\mathcal{S},\mathcal{A},P,\gamma)
* Equation: (\mathcal{S},\mathcal{A},P,\gamma)
* Symbols: \mathcal{S} (state space), \mathcal{A} (action space), P (transition model), γ (discount factor)
* Why it matters: This equation represents the Markov decision process (MDP) that is used to define the problem.

### Equation 4: \mathcal{S}
* Equation: \mathcal{S}
* Symbols: \mathcal{S} (state space)
* Why it matters: The state space represents the possible states that the agent can be in.

### Equation 5: \mathcal{A}
* Equation: \mathcal{A}
* Symbols: \mathcal{A} (action space)
* Why it matters: The action space represents the possible actions that the agent can take.

### Equation 6: P(\cdot\mid s,a)
* Equation: P(\cdot\mid s,a)
* Symbols: P (transition model), s (state), a (action)
* Why it matters: This equation represents the probability of transitioning from state s to state s' given action a.

### Equation 7: \gamma\in[0,1)
* Equation: \gamma\in[0,1)
* Symbols: γ (discount factor)
* Why it matters: The discount factor should be between 0 and 1, where 0 implies no discounting and 1 implies infinite discounting.

### Equation 8: X=(S,A)\in\mathcal{X}:=\mathcal{S}\times\mathcal{A}
* Equation: X=(S,A)\in\mathcal{X}:=\mathcal{S}\times\mathcal{A}
* Symbols: X (state-action pair), \mathcal{X} (state-action space)
* Why it matters: This equation represents the state-action space, which is the set of all possible state-action pairs.

**Method Summary**
================

* The authors propose a method called Bellman calibration for marginalized importance weighting in offline reinforcement learning.
* The method uses a one-dimensional, model-agnostic post-processing technique to reduce residual occupancy-balance violations.
* The method corrects the estimate's scale and shape by applying fitted occupancy-ratio evaluation (FORE) over a one-dimensional class of nondecreasing transformations.
* The authors derive a calibration-refinement bound showing that any fitted ratio with small calibration error performs nearly as well as the best post-processing based on its fitted values.

**Experimental Overview**
=====================

* The authors evaluate the proposed method on two tasks: D4RL MuJoCo and InfiniteCartPole.
* The tasks are chosen because they are representative of real-world reinforcement learning problems.
* The authors compare the proposed method to three baselines: neural FORE, DualDICE, and SCOPE-RL minimax weight learning.
* The main claimed finding is that the proposed method improves out-of-sample Bellman balance and off-policy value estimation.

**What to Verify in the PDF**
==========================

* The authors claim that the proposed method achieves small calibration error and KL risk within statistical error of the best monotone correction.
* To verify this claim, the authors should provide more details on the statistical error and the best monotone correction.
* The authors should also provide more details on the experimental design, including the choice of hyperparameters and the evaluation metrics.
* Additionally, the authors should provide more details on the theoretical guarantees of the proposed method, including the calibration-refinement bound.
{% endraw %}

{% raw %}
## 2) BioKERN: Biological Kernel Regularization for Histology-to-Transcriptomics Neighborhood Retrieval
- **Authors:** Seungik Cho, Betul Orcan-Ekmekci
- **arXiv:** [2608.24823](https://arxiv.org/abs/2608.24823v1) · [pdf](https://arxiv.org/pdf/2608.24823v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.24823v1))
- **Categories:** cs.LG, q-bio.QM

### Abstract
> Spatially resolved biology requires representations that preserve biological neighborhood structure rather than only exact cross-modal correspondences. Existing histology--transcriptomics objectives can emphasize instance-level matching even when non-paired spots share molecular or spatial context. We introduce BioKERN, a multimodal spatial representation-learning framework that incorporates biological structure as an explicit, learnable inductive bias. BioKERN constructs a training-time biological kernel by combining transcriptomic similarity and spatial proximity, then uses it to provide graded neighborhood supervision and regularize embedding geometry. Evaluation uses a fixed, model-independent biological neighborhood definition shared by all methods. Across Mouse Brain Visium and Human Liver GSE240429, BioKERN consistently improves biological-neighborhood retrieval over BLEEP in both single- and multi-scale settings. Controlled shared-architecture experiments show that most of the improvement arises from biological-kernel regularization rather than increased model capacity. These results support explicit biological geometry as an interpretable inductive bias for multimodal learning in spatial biology.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `(x_i, g_i, s_i)`

* Equation: `(x_i, g_i, s_i)`
* Symbols: `x_i`, `g_i`, `s_i`
* Why it matters: This equation represents the input data for the BioKERN framework, consisting of a spatial-transcriptomics spot, where `x_i` is the H&E image patch, `g_i` is the corresponding gene-expression profile, and `s_i` is the tissue coordinate.

### Equation 2: `x_i`

* Equation: `x_i`
* Symbols: `x_i`
* Why it matters: This equation represents the H&E image patch centered at spot `i`.

### Equation 3: `g_i`

* Equation: `g_i`
* Symbols: `g_i`
* Why it matters: This equation represents the corresponding gene-expression profile for spot `i`.

### Equation 4: `s_i ∈ ℝ^2`

* Equation: `s_i ∈ ℝ^2`
* Symbols: `s_i`
* Why it matters: This equation represents the spatial coordinate of spot `i` in 2D space.

### Equation 5: `d = 128`

* Equation: `d = 128`
* Symbols: `d`
* Why it matters: This equation represents the dimensionality of the embedding space, which is set to 128.

**Method Summary**
==================

* BioKERN learns a multimodal spatial representation that incorporates both cross-modal similarity and biological neighborhood structure.
* The framework consists of multimodal representation learning, construction of a learnable biological reference kernel, and kernel-regularized neighborhood supervision.
* The use of a frozen PLIP pathology encoder extracts morphology features, while gene expression is normalized, log-transformed, standardized, and reduced with PCA.
* Lightweight ResidualAdapters project both modalities into a shared d = 128 dimensional ℓ2 -normalized embedding space.

**Experimental Overview**
========================

* Tasks: Histology-to-Transcriptomics Neighborhood Retrieval
* Datasets: Mouse Brain Visium and Human Liver GSE240429
* Baselines: CCA, Ridge regression, naive PLIP zero-shot lower bound, PLIP linear, BLEEP
* Main claimed findings: BioKERN consistently improves biological-neighborhood retrieval over BLEEP in both single- and multi-scale settings.

**What to Verify in the PDF**
=============================

* The evaluation kernel `K_eval` used for Bio-mAP, which combines gene and spatial similarity with equal weights.
* The details of the Leiden clustering at resolution 0.5 used to produce 10 evaluation domains.
* The gene preprocessing steps used for the Human Liver GSE240429 dataset, including the union of the top 1,000 highly variable genes from the training slices.
{% endraw %}

{% raw %}
## 3) A Geometric Theory of Robust Fairness Audits
- **Authors:** Binita Maity
- **arXiv:** [2608.24818](https://arxiv.org/abs/2608.24818v1) · [pdf](https://arxiv.org/pdf/2608.24818v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.24818v1))
- **Categories:** cs.LG

### Abstract
> Neighborhood-based fairness audits evaluate individual fairness by comparing predictions among similar individuals in feature space. Despite their widespread use, little is known about the robustness of the auditing procedure itself. Because these audits rely on nearest neighbor relationships, small perturbations in feature space can alter local neighborhoods and produce different fairness assessments even when model predictions remain unchanged. We develop a geometric framework for analyzing the robustness of neighborhood-based fairness audits under bounded perturbations. Our analysis establishes sufficient conditions for neighborhood invariance, quantifies how neighborhood replacement propagates to audit instability, and introduces audit volatility, a measure of the expected sensitivity of fairness audits under repeated perturbations. Experiments on benchmark datasets support the theoretical analysis and show that the proposed framework explains the observed stability of neighborhood-based fairness audits.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: X=\{x_{1},\ldots,x_{n}\}\subseteq(\mathcal{M},d)

* Equation: X=\{x_{1},\ldots,x_{n}\}\subseteq(\mathcal{M},d)
* Symbols: X (set of data points), x_i (individual data points), \mathcal{M} (feature space), d (distance metric)
* Why it matters: This equation defines the set of data points X, which is a subset of the feature space \mathcal{M} with a given distance metric d.

### Equation 2: (\mathcal{M},d)

* Equation: (\mathcal{M},d)
* Symbols: \mathcal{M} (feature space), d (distance metric)
* Why it matters: This equation is a placeholder for the feature space \mathcal{M} with a given distance metric d, which is used to define the set of data points X.

### Equation 3: f:X\rightarrow\mathcal{Y}

* Equation: f:X\rightarrow\mathcal{Y}
* Symbols: f (model), X (set of data points), \mathcal{Y} (output space)
* Why it matters: This equation defines the model f, which takes in data points X and outputs values in the output space \mathcal{Y}.

### Equation 4: x_{i}

* Equation: x_{i}
* Symbols: x_i (individual data points)
* Why it matters: This equation represents an individual data point x_i, which is a member of the set of data points X.

### Equation 5: N_{k}(i)

* Equation: N_{k}(i)
* Symbols: N_k(i) (k-nearest neighbors), i (individual data point), k (number of nearest neighbors)
* Why it matters: This equation defines the k-nearest neighbors N_k(i) of an individual data point i, which are the k data points closest to i in the feature space.

**Method Summary**
================

* Neighborhood-based fairness audits evaluate individual fairness by comparing predictions among similar individuals in feature space.
* The proposed geometric framework analyzes the robustness of neighborhood-based fairness audits under bounded perturbations.
* The framework establishes sufficient conditions for neighborhood invariance, quantifies how neighborhood replacement propagates to audit instability, and introduces audit volatility, a measure of the expected sensitivity of fairness audits under repeated perturbations.

**Experimental Overview**
=====================

* Tasks/Datasets: The proposed framework is evaluated on the Adult Income, Bank Marketing, and COMPAS datasets obtained through the AI Fairness 360 toolkit and UCI.
* Baselines/Comparisons: The framework is compared to nearest neighbor consistency measures and FaiTH, which evaluate fairness by aggregating pairwise prediction comparisons over local neighborhoods.
* Main Claimed Findings: The proposed framework accurately explains the robustness of neighborhood-based fairness audits under feature perturbations, and provides informative and reliable robustness guarantees in practice.

**What to Verify in the PDF**
==========================

* The mathematical derivations of Theorem 8 and Corollary 7, which provide the theoretical bounds for audit volatility.
* The experimental results for the largest perturbation radius considered in the experiments (ρ = 0.20), which provide additional empirical validation of the proposed framework.
* The dependence of audit volatility on the expected amount of neighborhood replacement, which is quantified by the proposed framework.
{% endraw %}

{% raw %}
## 4) Effective Learning Rate Governs Loss Dynamics in Language Model Pretraining
- **Authors:** Zihan Liu, Ruiheng Zheng, Shaobo Zhang, Changxin Tian, Kunlong Chen, Zhiqiang Zhang, Lei Wu
- **arXiv:** [2608.24814](https://arxiv.org/abs/2608.24814v1) · [pdf](https://arxiv.org/pdf/2608.24814v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.24814v1))
- **Categories:** cs.LG

### Abstract
> We uncover ELR collapse in language model pretraining: learning rate (LR) and parameter norm govern loss dynamics primarily through their ratio, the effective learning rate (ELR). When ELR is matched across runs, their loss trajectories collapse throughout training despite substantially different LRs and parameter norms. Across optimizers, architectures, datasets, and model scales, mean collapse errors are typically a few x 10^-3, below the seed-to-seed variation measured in a representative configuration. Systematic ablations identify normalization design and the timescale of LR-norm variation as key determinants of collapse precision. Controlled interventions further show that weight decay and Hyperball shape loss dynamics primarily through the ELR schedules they induce. Replacing LR with ELR enables a fitted functional scaling law (FSL) to transfer across norm-control methods. The resulting ELR-based FSL also explains delayed acceleration, a recurring effect of norm control. Together, these results establish ELR as a common coordinate linking LR scheduling, norm control, and loss dynamics.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 3: Effective Learning Rate (ELR)
\[
\eta_{k}^{\mathrm{eff}}\mathrel{:=}\eta_{k}/\|\mathbf{W}_{k}\|_{F}
\]
Symbols:
- \(\eta_{k}\): learning rate at step \(k\)
- \(\|\mathbf{W}_{k}\|_{F}\): Frobenius norm of the weight matrix at step \(k\)

Why it matters: This equation defines the effective learning rate, which is the ratio of the actual learning rate to the norm of the weight matrix. It's a key concept in understanding how learning rates interact with weight norms.

### Equation 5: Update Rule for Language Model
\[
\mathbf{h}^{\ell+1}=\mathbf{h}^{\ell}+\operatorname{FFN}\!\left(\operatorname{Norm}(\mathbf{h}^{\ell})\right)
\]
Symbols:
- \(\mathbf{h}^{\ell}\): hidden state at step \(\ell\)
- \(\operatorname{FFN}\!\left(\operatorname{Norm}(\mathbf{h}^{\ell})\right)\): feed-forward network applied to the normalized hidden state

Why it matters: This equation describes the update rule for the language model, where the hidden state is updated by applying a feed-forward network to the normalized hidden state.

### Equation 6: Hidden State
\[
\mathbf{h}^{\ell}
\]
Symbols:
- \(\mathbf{h}^{\ell}\): hidden state at step \(\ell\)

Why it matters: This equation simply represents the hidden state at a given step.

### Equation 7: Learning Rate Schedules
\[
4.8\times 10^{-3}
\]
Symbols:
- \(4.8\times 10^{-3}\): learning rate schedule value

Why it matters: This equation represents a specific learning rate schedule value, which is used in the experiments.

### Equation 10: RMSE
\[
10^{-3}
\]
Symbols:
- \(10^{-3}\): RMSE value

Why it matters: This equation represents the root mean squared error (RMSE) value, which is used to evaluate the performance of the language model.

**Method Summary**
==================

* The authors train a 124M-parameter Llama model on FineWeb using various optimizers, architectures, datasets, and model scales.
* They use a combination of weight decay and Hyperball to control the norm of the weights.
* The authors also experiment with different learning rate schedules and compare their performance.

**Experimental Overview**
=========================

* Tasks/Datasets: Language model pretraining on FineWeb.
* Baselines/Comparisons: The authors compare their results with different optimizers, architectures, datasets, and model scales.
* Main Claimed Findings: The authors claim that the effective learning rate (ELR) is a key factor in controlling the loss dynamics of the language model, and that it can be used to transfer across norm-control methods.

**What to Verify in the PDF**
=============================

* The authors use a combination of weight decay and Hyperball to control the norm of the weights. Verify how these methods are implemented and their effects on the loss dynamics.
* The authors experiment with different learning rate schedules and compare their performance. Verify the specific learning rate schedules used and their effects on the loss dynamics.
* The authors use a 124M-parameter Llama model on FineWeb. Verify the details of the model architecture, training procedure, and hyperparameters used.
{% endraw %}

{% raw %}
## 5) MDTE: Minority-Aware Diffusion over Temporal Edge Events for Imbalanced Node Classification
- **Authors:** Zhou Zelong, Zhang Tianming, Yang Zhengyi, Tang Yifu, Hou Chenyu, Cao Bin, Fan Jing
- **arXiv:** [2608.24812](https://arxiv.org/abs/2608.24812v1) · [pdf](https://arxiv.org/pdf/2608.24812v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.24812v1))
- **Categories:** cs.LG

### Abstract
> Class-imbalanced node classification on temporal graphs is challenging because majority-dominated temporal propagation progressively assimilates minority representations, while conventional node and neighborhood information provides insufficient discriminative evidence for minority classes. To address these issues, we propose MDTE, a minority-aware diffusion framework that reconstructs stable and discriminative temporal edge-event representations through conditional diffusion denoising. Specifically, MDTE introduces Distribution-Aware Selective Propagation, which combines Local Outlier Factor (LOF)-based propagation filtering with cluster-aware low-frequency propagation. The module preserves informative neighborhood dependencies while mitigating harmful propagation and majority-class information assimilation. It further develops Multi-View Discriminative Fusion, which exploits feature reconstruction and topology prediction to characterize class-wise differences in distribution learning and extracts complementary discriminability signals to guide denoising. Experiments on five real-world datasets demonstrate that MDTE consistently achieves the best performance on minority-class-oriented metrics, improving minority-class recall by up to 23.53 percentage points, minority-class F1 by 8.68 percentage points, and AUPRC by 2.67 percentage points over the strongest baselines.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{G}^{T}=(\mathcal{V}^{T},\mathcal{E}^{T},\mathbf{A}^{T},\mathbf{H})$

* Equation: $\mathcal{G}^{T}=(\mathcal{V}^{T},\mathcal{E}^{T},\mathbf{A}^{T},\mathbf{H})$
* Symbols: $\mathcal{G}^{T}$ (temporal graph), $\mathcal{V}^{T}$ (node set), $\mathcal{E}^{T}$ (edge set), $\mathbf{A}^{T}$ (adjacency matrix), $\mathbf{H}$ (node features)
* Why it matters: This equation represents the temporal graph $\mathcal{G}^{T}$, which consists of nodes $\mathcal{V}^{T}$, edges $\mathcal{E}^{T}$, adjacency matrix $\mathbf{A}^{T}$, and node features $\mathbf{H}$.

### Equation 2: $\mathcal{V}^{T}=\{v_{1},v_{2},\ldots,v_{N}\}$

* Equation: $\mathcal{V}^{T}=\{v_{1},v_{2},\ldots,v_{N}\}$
* Symbols: $\mathcal{V}^{T}$ (node set), $v_{i}$ (node $i$)
* Why it matters: This equation defines the node set $\mathcal{V}^{T}$, which consists of $N$ nodes $v_{i}$.

### Equation 3: $N=|\mathcal{V}^{T}|$

* Equation: $N=|\mathcal{V}^{T}|$
* Symbols: $N$ (number of nodes), $|\mathcal{V}^{T}|$ (number of nodes in $\mathcal{V}^{T}$)
* Why it matters: This equation states that the number of nodes $N$ is equal to the number of nodes in the node set $\mathcal{V}^{T}$.

### Equation 4: $\mathcal{E}^{T}=\{e_{ij}^{t}=(v_{i},v_{j},t)\mid v_{i},v_{j}\in\mathcal{V}^{T},\,t\leq T\}$

* Equation: $\mathcal{E}^{T}=\{e_{ij}^{t}=(v_{i},v_{j},t)\mid v_{i},v_{j}\in\mathcal{V}^{T},\,t\leq T\}$
* Symbols: $\mathcal{E}^{T}$ (edge set), $e_{ij}^{t}$ (edge $(i,j)$ at time $t$), $v_{i}$ (node $i$), $v_{j}$ (node $j$), $t$ (time)
* Why it matters: This equation defines the edge set $\mathcal{E}^{T}$, which consists of edges $e_{ij}^{t}$ between nodes $v_{i}$ and $v_{j}$ at time $t$, where $t\leq T$.

### Equation 5: $e_{ij}^{t}$

* Equation: $e_{ij}^{t}$
* Symbols: $e_{ij}^{t}$ (edge $(i,j)$ at time $t$)
* Why it matters: This equation represents an individual edge $e_{ij}^{t}$ in the edge set $\mathcal{E}^{T}$.

### Equation 6: $v_{i}$

* Equation: $v_{i}$
* Symbols: $v_{i}$ (node $i$)
* Why it matters: This equation represents an individual node $v_{i}$ in the node set $\mathcal{V}^{T}$.

### Equation 7: $v_{j}$

* Equation: $v_{j}$
* Symbols: $v_{j}$ (node $j$)
* Why it matters: This equation represents an individual node $v_{j}$ in the node set $\mathcal{V}^{T}$.

### Equation 8: $\mathbf{A}^{T}$

* Equation: $\mathbf{A}^{T}$
* Symbols: $\mathbf{A}^{T}$ (adjacency matrix)
* Why it matters: This equation represents the adjacency matrix $\mathbf{A}^{T}$ of the temporal graph $\mathcal{G}^{T}$.

**Method Summary**
==================

* MDTE is a minority-aware diffusion framework for imbalanced node classification on temporal graphs.
* It consists of four stages: Temporal Edge-Event Construction, Minority-Aware Temporal Edge-Event Diffusion, Edge-to-Node Aggregation, and Debiased Contrastive Learning.
* The second stage proceeds through Forward Diffusion, Denoising Condition Construction, and Conditional Reverse Process.
* The denoising condition is constructed by two key modules: Distribution-Aware Selective Propagation and Multi-View Discriminative Fusion.

**Experimental Overview**
========================

* Tasks: Imbalanced node classification on temporal graphs.
* Datasets: Five financial transaction graph datasets (DGraph-Fin, Elliptic, Elliptic++ Transactions and Actors, Ethereum).
* Baselines: Thirteen baselines from four categories (temporal graph methods, static graph autoencoder methods, imbalanced graph methods, graph diffusion methods).
* Main claimed findings: MDTE achieves the best performance on minority-class-oriented metrics, improving minority-class recall by up to 23.53 percentage points, minority-class F1 by 8.68 percentage points, and AUPRC by 2.67 percentage points over the strongest baselines.

**What to Verify in the PDF**
=============================

* Details of the Distribution-Aware Selective Propagation and Multi-View Discriminative Fusion modules.
* The mathematical formulation of the Forward Diffusion, Denoising Condition Construction, and Conditional Reverse Process stages.
* The experimental results for each dataset, including the performance metrics and the comparison with baselines.
{% endraw %}
