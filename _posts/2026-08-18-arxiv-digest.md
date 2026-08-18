---
layout: post
title: "Daily arXiv Digest — 2026-08-18 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) AutoSR: Automatic Symbolic Regression by Searching Research States
- **Authors:** Kejia Zhang, Youran Sun, Xinyu Ren, Chugang Yi, Haizhao Yang
- **arXiv:** [2608.16876](https://arxiv.org/abs/2608.16876v1) · [pdf](https://arxiv.org/pdf/2608.16876v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.16876v1))
- **Categories:** cs.SC, cs.AI, cs.LG, math.NA

### Abstract
> We introduce Automatic Symbolic Regression (AutoSR), a fully automated system that instantiates Research-Space Symbolic Regression by searching persistent scientific investigations rather than isolated equations. Finite, noisy data often yield numerically competitive expressions that imply very different behavior outside the observed regime, making numerical fit and syntactic complexity insufficient measures of scientific credibility. Existing approaches largely focus on improving expressions, yet the search typically retains little beyond the resulting formula and score, losing the scientific record, such as motivations and probes, that inform what to try next. AutoSR preserves this record in a \textbf{Research State}, coupling each candidate equation with the reasoning, computational evidence, and independent review developed along its branch. Proposer--reviewer agents develop these states under progressive-widening Monte Carlo tree search (PW-MCTS), which allocates computation across competing investigations, while the accumulated research record is ultimately synthesized into a final report that explains the leading relation and the basis for its selection. Across nine selected challenges from two benchmark suites, AutoSR recovers algebraically equivalent relations in every case, including three cp3-bench problems that no published system recovers and six structurally diverse LSR-Transform problems. Overall, AutoSR extends symbolic regression from equation-level search toward automated scientific investigation, allowing scientific knowledge and accumulated evidence to shape both what is explored and how the resulting equation is justified.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: \mathcal{P}

* Equation: \mathcal{P}
* Symbols: \mathcal{P} (problem specification)
* Why it matters: The problem specification defines the scientific question, observed data, variable meanings, supporting evidence, evaluation criterion, and requirements for an acceptable relation.

### Equation 2: (\mathcal{P},B)

* Equation: (\mathcal{P},B)
* Symbols: \mathcal{P} (problem specification), B (computation budget)
* Why it matters: The system receives a problem specification and a computation budget, and returns a leading relation and a final report that connects this relation to its evidence and limitations.

### Equation 3: \hat{f}

* Equation: \hat{f}
* Symbols: \hat{f} (leading relation)
* Why it matters: The system returns a leading relation that represents the best solution to the problem.

### Equation 4: \mathcal{R}_{\mathrm{final}}

* Equation: \mathcal{R}_{\mathrm{final}}
* Symbols: \mathcal{R}_{\mathrm{final}} (final report)
* Why it matters: The system returns a final report that connects the leading relation to its evidence, limitations, research history, and credible alternatives.

### Equation 5: \operatorname{AutoSR}(\mathcal{P},B)\longrightarrow(\hat{f},\mathcal{R}_{\mathrm{final}})

* Equation: \operatorname{AutoSR}(\mathcal{P},B)\longrightarrow(\hat{f},\mathcal{R}_{\mathrm{final}})
* Symbols: \operatorname{AutoSR} (AutoSR system), \mathcal{P} (problem specification), B (computation budget), \hat{f} (leading relation), \mathcal{R}_{\mathrm{final}} (final report)
* Why it matters: This equation represents the overall process of the AutoSR system, which receives a problem specification and a computation budget, and returns a leading relation and a final report.

### Equation 6: \mathcal{S}_{i}=(f_{i},m_{i},\mathcal{A}_{i},\rho_{i},s_{i};p_{i})

* Equation: \mathcal{S}_{i}=(f_{i},m_{i},\mathcal{A}_{i},\rho_{i},s_{i};p_{i})
* Symbols: \mathcal{S}_{i} (Research State), f_{i} (function), m_{i} (mean), \mathcal{A}_{i} (action), \rho_{i} (reward), s_{i} (state), p_{i} (proposer)
* Why it matters: This equation represents a Research State, which is a persistent scientific investigation that includes a function, mean, action, reward, state, and proposer.

**Method Summary**
==================

* The AutoSR system receives a problem specification and a computation budget, and returns a leading relation and a final report that connects this relation to its evidence and limitations.
* The system uses a Monte Carlo tree search (PW-MCTS) to allocate computation across competing investigations.
* The system preserves the scientific record, including motivations, probes, and independent review, in a Research State.
* The system extends symbolic regression from equation-level search toward automated scientific investigation.

**Experimental Overview**
=========================

* The experiments evaluate the AutoSR system on nine selected challenge cases from two benchmark suites.
* The challenge cases cover dependent input features, a single expression that unifies cusp and core density profiles, and a strongly oscillatory gravitational-wave signal with an additional mass parameter.
* The system is compared to existing symbolic-regression systems on the cp3-bench and LSR-Transform datasets.
* The main claimed findings are that the AutoSR system recovers exact relations on selected equations, including three cp3-bench problems that no published system recovers.

**What to Verify in the PDF**
=============================

* The details of the Monte Carlo tree search (PW-MCTS) algorithm used by the AutoSR system.
* The implementation of the Research State data structure and how it is used to preserve the scientific record.
* The evaluation protocol used to compare the AutoSR system to existing symbolic-regression systems on the cp3-bench and LSR-Transform datasets.
{% endraw %}

{% raw %}
## 2) An Analytical-Prior Framework for Data-Efficient Prediction of Sound-Reduction Frequencies in Rectangular Side-Branch Helmholtz Resonators
- **Authors:** Jiaming Li
- **arXiv:** [2608.16873](https://arxiv.org/abs/2608.16873v1) · [pdf](https://arxiv.org/pdf/2608.16873v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG

### Abstract
> High-fidelity finite-element simulations can provide accurate numerical predictions for side-branch resonators, but large simulation datasets are expensive to generate and purely data-driven surrogates may become unreliable when simulation-labelled data are scarce. This study develops an analytical-prior learning framework that reuses a low-cost analytical model to improve data efficiency under limited high-fidelity simulation budgets. Two complementary routes are considered. When the analytical model remains available at inference, it is retained as an explicit baseline and the simulation data are used to learn only the analytical-to-simulation discrepancy. When a self-contained predictor is required, the analytical mapping is first distilled from abundant low-cost evaluations into a learned prior and then calibrated with the limited simulation data. The framework is evaluated on rectangular side-branch Helmholtz resonators using 86 simulation-labelled geometries and 8,998 non-overlapping analytical-only geometries. The analytical model achieved a mean absolute error (MAE) of 1.333 Hz. Direct support vector regression (SVR) achieved 3.375 Hz, while residual SVR reduced the MAE to 0.426 Hz. A direct multilayer perceptron (MLP) achieved 1.109 Hz, whereas analytical-prior pretraining reduced the error to 0.556 Hz with frozen-prior residual adaptation and 0.371 Hz with full-model fine-tuning. Across training budgets of 20 to 70 simulation-labelled cases, both analytical correction and analytical-prior pretraining consistently improved data efficiency relative to direct learning. These results show that analytical prior information can substantially improve high-fidelity prediction when simulation data are scarce, with explicit correction and prior distillation serving complementary deployment needs.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Mean Absolute Error (MAE)
```markdown
MAE = (1/n) * ∑|y_true - y_pred|
```
Symbols: `MAE` (Mean Absolute Error), `y_true` (true values), `y_pred` (predicted values), `n` (number of samples)

Why it matters: MAE is a measure of the average difference between predicted and true values, used to evaluate the performance of the proposed framework.

### 2. Direct Support Vector Regression (SVR)
```markdown
SVR(y) = ∑w_i * x_i + b
```
Symbols: `SVR(y)` (SVR prediction), `w_i` (weights), `x_i` (features), `b` (bias)

Why it matters: SVR is a regression algorithm used as a baseline for comparison with the proposed framework.

### 3. Residual SVR
```markdown
Residual SVR(y) = SVR(y) - f(x)
```
Symbols: `Residual SVR(y)` (residual SVR prediction), `f(x)` (analytical model prediction)

Why it matters: Residual SVR is a modified version of SVR that uses the analytical model as an additional feature to improve performance.

### 4. Multilayer Perceptron (MLP)
```markdown
MLP(y) = σ(W * x + b)
```
Symbols: `MLP(y)` (MLP prediction), `W` (weights), `x` (features), `b` (bias), `σ` (activation function)

Why it matters: MLP is a neural network used as a baseline for comparison with the proposed framework.

### 5. Analytical-Prior Pretraining
```markdown
f(x) = σ(W * x + b)
```
Symbols: `f(x)` (analytical model prediction), `W` (weights), `x` (features), `b` (bias), `σ` (activation function)

Why it matters: The analytical model is used as a starting point for pretraining, which improves the performance of the framework.

**Method Summary**
==================

* The proposed framework combines an analytical model with a learning algorithm to improve data efficiency.
* Two complementary routes are considered: (1) using the analytical model as an explicit baseline, and (2) distilling the analytical model into a learned prior and calibrating it with limited simulation data.
* The framework is evaluated using 86 simulation-labelled geometries and 8,998 non-overlapping analytical-only geometries.

**Experimental Overview**
========================

* Tasks: prediction of sound-reduction frequencies in rectangular side-branch Helmholtz resonators.
* Datasets: 86 simulation-labelled geometries and 8,998 non-overlapping analytical-only geometries.
* Baselines: Direct SVR, Residual SVR, Direct MLP, and Analytical-Prior Pretraining.
* Main claimed findings: The proposed framework consistently improves data efficiency relative to direct learning, with explicit correction and prior distillation serving complementary deployment needs.

**What to Verify in the PDF**
=============================

* The mathematical derivations of the analytical model and the learning algorithm.
* The details of the simulation setup and the evaluation metrics used.
* The results of the ablation study to understand the impact of different hyperparameters and model architectures.
{% endraw %}

{% raw %}
## 3) Data-Efficient and Interpretable Classification of Circulating Tumor Cell Phenotypes in Microfluidic Devices via Deep Learning
- **Authors:** Serena Su, Yifan Wang, Senwei Liang
- **arXiv:** [2608.16870](https://arxiv.org/abs/2608.16870v1) · [pdf](https://arxiv.org/pdf/2608.16870v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.16870v1))
- **Categories:** cs.LG

### Abstract
> Accurate classification of circulating tumor cell (CTC) phenotypes can provide valuable information for assessing metastatic potential. Label free microfluidic devices provide a hydrodynamic obstacle course that transforms subtle biophysical characteristics of CTCs, including size and deformability, into distinct kinematic trajectories. However, the highly nonlinear fluid structure interactions governing these trajectories make the inverse problem of inferring cellular phenotype from trajectory data analytically intractable. While deep neural networks (DNNs) have emerged as a powerful approach for addressing this inverse problem, their effectiveness is constrained by the limited availability of trajectory data and the lack of physical interpretability. To address these challenges, we propose an interpretable and data efficient DNN framework for trajectory based CTC classification. To mitigate the scarcity of data, we develop Subsequence (SubSeq), a targeted augmentation strategy that randomly extracts informative local trajectory segments during training to promote learning from localized patterns. We further apply Gradient Weighted Class Activation Mapping to identify the trajectory features and physical regions of the microfluidic device that drive model predictions. Experimental results demonstrate that SubSeq improves classification accuracy over the evaluated baseline and augmentation methods. Furthermore, interpretability analysis suggests that localized trajectory segments contain substantial biophysical information relevant to accurate classification. This provides justification for SubSeq and also highlights the redundancy of full-length trajectories. More broadly, the proposed framework views microfluidic geometries as physical encoders of cellular mechanical properties, providing mechanistic insights that may inform the future design of diagnostic devices.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Data Set Definition
```math
\mathcal{D}=\{(\mathbf{X}^{(i)},p^{(i)})\}_{i=1}^{N}
```
* Equation: Data set definition
* Symbols:
	+ $\mathcal{D}$: Data set
	+ $\mathbf{X}^{(i)}$: Feature vector for the $i^{th}$ data point
	+ $p^{(i)}$: Label for the $i^{th}$ data point
* Why it matters: This equation defines the data set used for training and testing the model.

### Equation 2: Trajectory Representation
```math
\mathbf{X}^{(i)}=\left\{(x_{t}^{(i)},y_{t}^{(i)},z_{t}^{(i)},v_{x,t}^{(i)},v_{y,t}^{(i)},v_{z,t}^{(i)})\right\}_{t=1}^{T}
```
* Equation: Trajectory representation
* Symbols:
	+ $\mathbf{X}^{(i)}$: Feature vector for the $i^{th}$ data point
	+ $x_{t}^{(i)}$, $y_{t}^{(i)}$, $z_{t}^{(i)}$: Position coordinates at time $t$
	+ $v_{x,t}^{(i)}$, $v_{y,t}^{(i)}$, $v_{z,t}^{(i)}$: Velocity components at time $t$
* Why it matters: This equation represents the feature vector for each data point, which includes position and velocity coordinates.

### Equation 3: Label Definition
```math
p^{(i)}\in\{0,1\}
```
* Equation: Label definition
* Symbols:
	+ $p^{(i)}$: Label for the $i^{th}$ data point
* Why it matters: This equation defines the possible labels for each data point, which is either 0 or 1.

### Equation 4: Trajectory Representation (Alternative)
```math
\mathbf{X}^{(i)}
```
* Equation: Trajectory representation (alternative)
* Symbols:
	+ $\mathbf{X}^{(i)}$: Feature vector for the $i^{th}$ data point
* Why it matters: This equation is an alternative representation of the feature vector, which is not explicitly defined in the original equation.

### Equation 5: Trajectory Representation (Alternative)
```math
(x_{t},y_{t},z_{t})_{t=1}^{T}
```
* Equation: Trajectory representation (alternative)
* Symbols:
	+ $(x_{t},y_{t},z_{t})_{t=1}^{T}$: Position coordinates at each time step
* Why it matters: This equation represents the position coordinates at each time step, which is an alternative representation of the feature vector.

**Method Summary**
================

* The proposed method uses a convolutional neural network (CNN) to classify circulating tumor cell (CTC) phenotypes based on their trajectories in a microfluidic device.
* The method employs a data augmentation technique called SubSeq, which randomly selects temporal segments of the trajectory data to train the model.
* The method also uses Grad-CAM analysis to interpret the trained models and identify salient features of CTC trajectories.

**Experimental Overview**
=====================

* Tasks/Datasets:
	+ Classify CTC phenotypes based on their trajectories in a microfluidic device
	+ Evaluate the performance of the proposed method using a dataset of 516 CTC trajectories
* Baselines/Comparisons:
	+ Compare the performance of the proposed method with other data augmentation techniques, such as Cutout and Mixup
* Main Claimed Findings:
	+ The proposed method achieves comparable performance to other data augmentation techniques, but with a more consistent and stable performance across different data regimes.

**What to Verify in the PDF**
==========================

* The implementation details of the SubSeq data augmentation technique, including the parameters used and the evaluation metrics used to compare its performance with other techniques.
* The results of the Grad-CAM analysis, including the identified salient features of CTC trajectories and their contributions to the classification decisions.
* The evaluation of the model's performance across different data regimes, including the data-rich and data-scarce scenarios.
{% endraw %}

{% raw %}
## 4) Non-Crossing Deep Quantile Regression for Distributional Survival Prediction
- **Authors:** Shuai Huang, Zhe Qu, Zhaowei Hua, Guohao Shen, Rui Tang, Hongtu Zhu
- **arXiv:** [2608.16864](https://arxiv.org/abs/2608.16864v1) · [pdf](https://arxiv.org/pdf/2608.16864v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.16864v1))
- **Categories:** stat.ML, cs.LG, stat.AP

### Abstract
> In survival analysis the way covariates act on the risk of an event often differs between early and late failure times, yet hazard- and mean-based summaries collapse this variation into a single number. Quantile-based modeling instead describes the full conditional distribution on the original time scale, but existing censored-data methods are either inflexible or produce logically inconsistent crossing quantile curves. We propose a Censored Non-crossing Quantile (CNQ) framework for right-censored data that jointly estimates several conditional survival quantiles and guarantees valid ordering by construction, with flexibility supplied by Kolmogorov-Arnold and Transformer backbones, and we establish a finite-sample excess-risk bound holding jointly across all fitted quantile levels. Across 27 simulation settings and six cohorts the framework attains lower pinball loss than quantile-, hazard- and tree-based competitors whenever the conditional distribution is asymmetric, with interval coverage closer to nominal on all six. In two clinical case studies (METABRIC, breast cancer; FLCHAIN, population mortality) it recovers covariate effects that vary across the survival distribution and would be hidden by a single hazard ratio, and yields coherent individualized quantile milestones. Code: https://github.com/BIG-S2/deepcnq
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: {N/\log N}^{-\beta/(2\beta+p)}

* Equation: `{N/\log N}^{-\beta/(2\beta+p)}`
* Symbols: `N`, `\log N`, `\beta`, `p`
* Why it matters: This equation is used to calculate the learning rate for the AdamW optimizer. The learning rate is a hyperparameter that controls how quickly the model learns from the data.

### Equation 2: \beta

* Equation: `\beta`
* Symbols: `\beta`
* Why it matters: This equation is used to calculate the quantile regression coefficients. The coefficients are used to estimate the conditional distribution of the event time given the covariates.

### Equation 3: n=500

* Equation: `n=500`
* Symbols: `n`
* Why it matters: This equation is used to specify the sample size for the simulation study. The sample size is an important hyperparameter that controls the amount of data used to train and evaluate the model.

### Equation 4: n=144

* Equation: `n=144`
* Symbols: `n`
* Why it matters: This equation is used to specify the sample size for the real-world datasets. The sample size is an important hyperparameter that controls the amount of data used to train and evaluate the model.

### Equation 5: n=8{,}873

* Equation: `n=8{,}873`
* Symbols: `n`
* Why it matters: This equation is used to specify the sample size for the real-world datasets. The sample size is an important hyperparameter that controls the amount of data used to train and evaluate the model.

**Method Summary**
==================

* The proposed method, CNQ, is a non-crossing quantile regression framework that jointly estimates several conditional survival quantiles.
* CNQ uses a Kolmogorov–Arnold backbone and a Transformer backbone to estimate the conditional distribution of the event time given the covariates.
* The method is designed to handle right-censored data and provides a flexible way to estimate the conditional distribution of the event time.
* CNQ is compared to several baselines, including quantile regression, hazard regression, and tree-based methods.

**Experimental Overview**
=========================

* Tasks/Datasets: The proposed method is evaluated on 27 simulation settings and six real-world cohorts.
* Baselines/Comparisons: The method is compared to several baselines, including quantile regression, hazard regression, and tree-based methods.
* Main Claimed Findings: The method attains lower pinball loss than the baselines whenever the conditional distribution is asymmetric, and provides coherent individualized quantile milestones.

**What to Verify in the PDF**
=============================

* The implementation details of the proposed method, including the choice of hyperparameters and the optimization algorithm used.
* The results of the sensitivity analysis, which is used to evaluate the robustness of the method to different hyperparameters and data distributions.
* The results of the case studies, which are used to evaluate the performance of the method on real-world datasets.
{% endraw %}

{% raw %}
## 5) Proteus: Incremental Memory Activation for Long-Context Sequence Modeling
- **Authors:** Reza Bayat, Ali Behrouz, Vahab Mirrokni, Aaron Courville
- **arXiv:** [2608.16844](https://arxiv.org/abs/2608.16844v1) · [pdf](https://arxiv.org/pdf/2608.16844v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.16844v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> The quadratic cost of attention-based sequence models for long contexts has motivated a growing line of research on memory-based models that can compress context into a compact state. However, most existing memory models expose a static memory throughout the entire sequence. Because early tokens face no compression pressure, they occupy too many degrees of freedom and "pollute" the memory state, leaving little capacity for later context and increasing interference between what is stored and what arrives next. We study a new paradigm of incremental memory activation, where the effective capacity of memory is progressively expanded as the context grows. Imposing an early bottleneck forces the model to compress history more effectively, while unlocking fresh capacity over time reduces interference and improves retention of later context. We instantiate this paradigm in Proteus, a straightforward mechanism that can be incorporated into a broad class of neural memory architectures at no additional cost. We apply Proteus to state-of-the-art models, including SWLA, Comba, Titans, and Hope-Attention, and observe consistent improvements on standard language modeling and reasoning, as well as on long-context retrieval and understanding, with gains that grow at longer context lengths. Overall, our results show that static memory is suboptimal and that scheduling effective capacity is a simple and broadly applicable tool for sequence modeling.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1) Formula Walkthrough**
### Equation 1
`{^{{}^{{}^{\dagger}}}}`

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2
`{^{{}^{{}^{\ddagger}}}}`

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

**2) Method Summary**
* Proteus is a mechanism that can be incorporated into a broad class of neural memory architectures at no additional cost.
* Proteus imposes an early bottleneck to compress history more effectively, while unlocking fresh capacity over time.
* The effective capacity of memory is progressively expanded as the context grows.
* Proteus is applied to state-of-the-art models, including SWLA, Comba, Titans, and Hope-Attention.

**3) Experimental Overview**
* Tasks/Datasets: Language modeling, reasoning, long-context retrieval, and understanding.
* Baselines/Comparisons: State-of-the-art models, including SWLA, Comba, Titans, and Hope-Attention.
* Main Claimed Findings: Adding Proteus consistently improves average downstream accuracy over the corresponding base model, and lowers perplexity in nearly all settings.

**4) What to Verify in the PDF**
* The effect of the number of partition blocks (E) on the performance of Proteus.
* The mechanism by which Proteus unlocks fresh capacity over time.
* The impact of the number of partition blocks on the non-monotonicity of perplexity improvement.
{% endraw %}
