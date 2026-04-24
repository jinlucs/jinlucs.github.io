---
layout: post
title: "Daily arXiv Digest — 2026-04-24 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Fine-Tuning Regimes Define Distinct Continual Learning Problems
- **Authors:** Paul-Tiberiu Iordache, Elena Burceanu
- **arXiv:** [2604.21927](https://arxiv.org/abs/2604.21927v1) · [pdf](https://arxiv.org/pdf/2604.21927v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.21927v1))
- **Categories:** cs.LG

### Abstract
> Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: \mathcal{T}_{1},\dots,\mathcal{T}_{T}

* Equation: A sequence of tasks \mathcal{T}_{1},\dots,\mathcal{T}_{T} .
* Symbols: \mathcal{T}_{t} represents a task at time t.
* Why it matters: This equation represents the sequence of tasks that the model is trained on.

### Equation 2: \theta\in\mathbb{R}^{d}

* Equation: The model's parameters θ are in ℝ ^{d} .
* Symbols: θ represents the model's parameters, d is the dimensionality of the parameter space.
* Why it matters: This equation specifies the space in which the model's parameters reside.

### Equation 3: \mathcal{J}_{t}(\theta)=\mathcal{L}_{t}(\theta)+\lambda\,\Omega_{t}(\theta;\theta_{1:t-1})

* Equation: The loss function \mathcal{J}_{t}(\theta) is composed of two terms: the current-task loss \mathcal{L}_{t}(\theta) and the method-specific term \lambda\,\Omega_{t}(\theta;\theta_{1:t-1}).
* Symbols: \mathcal{J}_{t}(\theta) represents the loss function at time t, \mathcal{L}_{t}(\theta) is the current-task loss, \lambda is a hyperparameter, \Omega_{t}(\theta;\theta_{1:t-1}) is the method-specific term, and \theta_{1:t-1} represents the previous parameters.
* Why it matters: This equation represents the objective function that the model is optimized to minimize at each time step.

### Equation 4: \mathcal{L}_{t}

* Equation: The current-task loss \mathcal{L}_{t}(\theta) is not explicitly defined in the provided context.
* Symbols: \mathcal{L}_{t}(\theta) represents the loss function for the current task.
* Why it matters: This equation is not fully specified, but it is likely a function of the model's parameters θ and the task-specific data.

### Equation 5: \Omega_{t}

* Equation: The method-specific term \Omega_{t}(\theta;\theta_{1:t-1}) is not explicitly defined in the provided context.
* Symbols: \Omega_{t}(\theta;\theta_{1:t-1}) represents the term used to preserve previously acquired knowledge.
* Why it matters: This equation is not fully specified, but it is likely a function of the model's parameters θ and the previous parameters θ_{1:t-1}.

### Equation 6: S\subseteq\{1,\dots,d\}

* Equation: S is a subset of the indices {1,\dots,d} .
* Symbols: S represents a subset of the model's parameters.
* Why it matters: This equation specifies the subset of parameters that are kept trainable.

### Equation 7: P_{S}

* Equation: P_{S} is not explicitly defined in the provided context.
* Symbols: P_{S} represents a probability distribution over the subset S.
* Why it matters: This equation is not fully specified, but it is likely related to the method-specific term \Omega_{t}(\theta;\theta_{1:t-1}).

### Equation 8: \eta>0

* Equation: \eta is a positive scalar.
* Symbols: \eta represents a hyperparameter.
* Why it matters: This equation specifies a hyperparameter that controls the trade-off between fitting the current task and preserving previously acquired knowledge.

**Method Summary**
================

* The authors propose a new approach to continual learning by considering the fine-tuning regime as a key evaluation variable.
* The fine-tuning regime is defined by the subset of trainable parameters S \subseteq \{1,\dots,d} .
* The authors argue that changing the fine-tuning regime can alter the effective update signal and affect the relative ranking of methods.
* The authors propose a new evaluation protocol that treats the fine-tuning regime as a first-class variable.

**Experimental Overview**
=====================

* The authors evaluate the proposed approach on five benchmark datasets (MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100).
* The authors compare the proposed approach with four standard methods (online EWC, LwF, SI, and GEM).
* The authors test the robustness of the proposed approach to different task orders and fine-tuning regimes.

**What to Verify in the PDF**
==========================

* The authors mention that the task boundaries are assumed to be known throughout training, but it is unclear how this assumption is justified.
* The authors do not provide a clear definition of the method-specific term \Omega_{t}(\theta;\theta_{1:t-1}).
* The authors mention that the authors use a shared backbone together with a global T × C T\times C classifier, but it is unclear how this architecture is related to the fine-tuning regime.
* The authors do not provide a clear explanation of how the authors handle the case where the task boundaries are not known at training time.
{% endraw %}

{% raw %}
## 2) The Sample Complexity of Multicalibration
- **Authors:** Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
- **arXiv:** [2604.21923](https://arxiv.org/abs/2604.21923v1) · [pdf](https://arxiv.org/pdf/2604.21923v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.21923v1))
- **Categories:** cs.LG, math.ST, stat.ML

### Abstract
> We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\varepsilon$

* Equation: $\varepsilon$
* Symbols: $\varepsilon$
* Why it matters: This is the error tolerance parameter that the multicalibration algorithm aims to achieve.

### Equation 2: $\kappa > 0$

* Equation: $\kappa > 0$
* Symbols: $\kappa$
* Why it matters: This is a parameter that controls the trade-off between the sample complexity and the desired calibration error.

### Equation 3: $|G| \leq \varepsilon^{-\kappa}$

* Equation: $|G| \leq \varepsilon^{-\kappa}$
* Symbols: $|G|$, $\varepsilon$, $\kappa$
* Why it matters: This is the condition under which the sample complexity of multicalibration is analyzed.

### Equation 4: $\widetilde{\Theta}(\varepsilon^{-3})$

* Equation: $\widetilde{\Theta}(\varepsilon^{-3})$
* Symbols: $\widetilde{\Theta}$
* Why it matters: This is the asymptotic complexity bound for the sample complexity of multicalibration.

### Equation 5: $\widetilde{\Theta}(\varepsilon^{-2})$

* Equation: $\widetilde{\Theta}(\varepsilon^{-2})$
* Symbols: $\widetilde{\Theta}$
* Why it matters: This is the asymptotic complexity bound for the sample complexity of marginal calibration.

### Equation 6: $\kappa = 0$

* Equation: $\kappa = 0$
* Symbols: $\kappa$
* Why it matters: This is a special case that separates the sample complexity of multicalibration from that of marginal calibration.

### Equation 7: $L_p$

* Equation: $L_p$
* Symbols: $L_p$
* Why it matters: This is a property class that is relevant to the weighted $L_p$ multicalibration.

**Method Summary**
==================

* The authors study the sample complexity of multicalibration in the batch setting.
* They prove that for every fixed $\kappa > 0$, the sample complexity of multicalibration is $\Theta(\varepsilon^{-3})$ in the regime $|G| \leq \varepsilon^{-\kappa}$.
* The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction.
* The authors also show that the sample complexity of multicalibration is $\Theta(\varepsilon^{-2})$ for $\kappa = 0$.

**Experimental Overview**
=======================

* The authors do not provide any experimental details in the provided context.
* However, they mention that their results are relevant to concrete property classes such as quantiles and expectiles.

**What to Verify in the PDF**
==========================

* The authors' lower-bound constructions use only polylogarithmically many groups, which implies that the sharp lower bounds $\Omega(\varepsilon^{-3})$ for mean ECE and $\Omega(\varepsilon^{-3/p})$ for weighted $L_p$ already fit every polynomial budget $|G| \leq \varepsilon^{-\kappa}$ with fixed $\kappa > 0$.
* The authors' results characterize the minimax dependence on $\varepsilon$ for mean ECE and weighted $L_p$ multicalibration throughout the entire regime of polynomial group growth.
* The authors also discuss the possibility of derandomization and whether deterministic predictors can match the randomized minimax rates in full generality.
{% endraw %}

{% raw %}
## 3) When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs
- **Authors:** Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny, Mustafa Shukor, Alasdair Newson, Matthieu Cord
- **arXiv:** [2604.21911](https://arxiv.org/abs/2604.21911v1) · [pdf](https://arxiv.org/pdf/2604.21911v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.21911v1))
- **Categories:** cs.CV, cs.AI, cs.CL, cs.LG

### Abstract
> Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\mathcal{O}_{\text{present}}$

* Equation: $\mathcal{O}_{\text{present}}$
* Symbols: $\mathcal{O}_{\text{present}}$ (object presence)
* Why it matters: This equation represents the presence of an object in the image, which is used to evaluate the model's performance on object recognition tasks.

### Equation 2: $\mathcal{O}_{\text{random}}$

* Equation: $\mathcal{O}_{\text{random}}$
* Symbols: $\mathcal{O}_{\text{random}}$ (object absence)
* Why it matters: This equation represents the absence of an object in the image, which is used to evaluate the model's performance on object recognition tasks.

### Equation 3: $\mathcal{O}_{\text{adversarial}}$

* Equation: $\mathcal{O}_{\text{adversarial}}$
* Symbols: $\mathcal{O}_{\text{adversarial}}$ (adversarial object)
* Why it matters: This equation represents an object that is contextually credible but visually absent, which is used to evaluate the model's performance on hallucination tasks.

**Method Summary**
================

* The authors propose HalluScope, a benchmark to study the impact of textual priors on hallucinations in LVLMs.
* HalluScope consists of a diverse set of images with semantically diverse captions and object annotations.
* The authors propose HalluVL-DPO, a framework for fine-tuning LVLMs to mitigate hallucinations induced by textual instruction priors.
* HalluVL-DPO uses preference optimization to guide the model to prefer grounded responses over hallucinated ones.

**Experimental Overview**
=====================

* Tasks: Object recognition, adversarial recognition, and hallucination tasks.
* Datasets: HalluScope, POPE, CP-Bench, HallusionBench, CHAIR, MME, and ScienceQA.
* Baselines: Original model, VCD, DPO-fine-tuned model, and HalluVL-DPO.
* Main claimed findings: HalluVL-DPO effectively mitigates hallucinations induced by textual instruction priors while preserving or improving performance on other hallucination benchmarks and visual capability evaluations.

**What to Verify in the PDF**
==========================

* The authors' claim that visual backbones are generally good enough to identify present objects and random absent objects, with accuracies above 85%.
* The effectiveness of HalluVL-DPO in mitigating hallucinations induced by textual instruction priors.
* The impact of reweighting samples during training on the performance of HalluVL-DPO.
{% endraw %}

{% raw %}
## 4) Low-Rank Adaptation Redux for Large Models
- **Authors:** Bingcong Li, Yilang Zhang, Georgios B. Giannakis
- **arXiv:** [2604.21905](https://arxiv.org/abs/2604.21905v1) · [pdf](https://arxiv.org/pdf/2604.21905v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.21905v1))
- **Categories:** cs.LG, eess.SP

### Abstract
> Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `× 10^{18}`

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not provided

### Equation 2: `∼`

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not provided

### Equation 3: `X Y^{\top}`

* Equation: Not provided
* Symbols: `X`, `Y`, `^{\top}`
* Why it matters: This equation represents the matrix product of `X` and `Y`, which is a fundamental operation in linear algebra.

### Equation 4: `X`

* Equation: Not provided
* Symbols: `X`
* Why it matters: This equation is likely a reference to the matrix `X` being discussed in the context of low-rank adaptation.

### Equation 5: `Y`

* Equation: Not provided
* Symbols: `Y`
* Why it matters: This equation is likely a reference to the matrix `Y` being discussed in the context of low-rank adaptation.

### Equation 6: `100 ×`

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not provided

### Equation 7: `∼ 1%-2%`

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not provided

### Equation 8: `a`

* Equation: Not provided
* Symbols: `a`
* Why it matters: Not provided

**Method Summary**
==================

* Low-rank adaptation (LoRA) is a parameter-efficient fine-tuning method for large models.
* LoRA uses a low-rank matrix factorization to adapt the model parameters.
* LoRA is compared to other fine-tuning methods, including prompt and prefix tuning.
* LoRA is shown to be more efficient and effective than other methods in certain scenarios.

**Experimental Overview**
=========================

* Tasks/Datasets: Not specified
* Baselines/Comparisons: LoRA is compared to other fine-tuning methods, including prompt and prefix tuning.
* Main claimed findings: LoRA is shown to be more efficient and effective than other methods in certain scenarios.

**What to Verify in the PDF**
=============================

* The mathematical derivations of the LoRA algorithm.
* The experimental results and comparisons with other methods.
* The theoretical guarantees and limitations of LoRA.
{% endraw %}

{% raw %}
## 5) Fairness under uncertainty in sequential decisions
- **Authors:** Michelle Seng Ah Lee, Kirtan Padh, David Watson, Niki Kilbertus, Jatinder Singh
- **arXiv:** [2604.21711](https://arxiv.org/abs/2604.21711v1) · [pdf](https://arxiv.org/pdf/2604.21711v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.21711v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Fair machine learning (ML) methods help identify and mitigate the risk that algorithms encode or automate social injustices. Algorithmic approaches alone cannot resolve structural inequalities, but they can support socio-technical decision systems by surfacing discriminatory biases, clarifying trade-offs, and enabling governance. Although fairness is well studied in supervised learning, many real ML applications are online and sequential, with prior decisions informing future ones. Each decision is taken under uncertainty due to unobserved counterfactuals and finite samples, with dire consequences for under-represented groups, systematically under-observed due to historical exclusion and selective feedback. A bank cannot know whether a denied loan would have been repaid, and may have less data on marginalized populations. This paper introduces a taxonomy of uncertainty in sequential decision-making -- model, feedback, and prediction uncertainty -- providing shared vocabulary for assessing systems where uncertainty is unevenly distributed across groups. We formalize model and feedback uncertainty via counterfactual logic and reinforcement learning, and illustrate harms to decision makers (unrealized gains/losses) and subjects (compounding exclusion, reduced access) of policies that ignore the unobserved space. Algorithmic examples show it is possible to reduce outcome variance for disadvantaged groups while preserving institutional objectives (e.g. expected utility). Experiments on data simulated with varying bias show how unequal uncertainty and selective feedback produce disparities, and how uncertainty-aware exploration alters fairness metrics. The framework equips practitioners to diagnose, audit, and govern fairness risks. Where uncertainty drives unfairness rather than incidental noise, accounting for it is essential to fair and effective decision-making.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `t=50`

* Equation: `t=50`
* Symbols: `t` (no specific symbols)
* Why it matters: This equation is not explicitly used in the paper, but it seems to be a placeholder or a variable name. It might be related to the experiment or simulation setup.

### Equation 2: `t∈ℕ`

* Equation: `t∈ℕ`
* Symbols: `t` (variable), `ℕ` (set of natural numbers)
* Why it matters: This equation defines the domain of `t`, which is the set of natural numbers. It indicates that `t` can take any positive integer value.

### Equation 3: `x_t`

* Equation: `x_t`
* Symbols: `x` (variable), `t` (variable)
* Why it matters: This equation represents a variable `x` at time `t`. It is likely a feature or input variable in the machine learning model.

### Equation 4: `A ∈ {0, 1}`

* Equation: `A ∈ {0, 1}`
* Symbols: `A` (variable), `{0, 1}` (set of binary values)
* Why it matters: This equation defines a binary sensitive attribute `A`, which can take values 0 or 1. It is likely used to represent a categorical or binary feature in the dataset.

### Equation 5: `S = X × G × L × C`

* Equation: `S = X × G × L × C`
* Symbols: `S` (set), `X` (set), `G` (set), `L` (set), `C` (set)
* Why it matters: This equation defines a set `S` as the Cartesian product of sets `X`, `G`, `L`, and `C`. It represents the possible combinations of values from these sets.

**Method Summary**
================

* The authors propose a framework to mitigate fairness issues in sequential decisions under uncertainty.
* They use a pipeline to simulate different types and magnitudes of bias in binary decision problems.
* The framework accommodates historical bias, measurement bias, representation bias, and omitted variable bias.
* The authors evaluate the performance of different methods using fairness metrics such as selection rate and profit.

**Experimental Overview**
=====================

* Tasks: The authors use a synthetic dataset to evaluate the performance of different methods in mitigating fairness issues.
* Datasets: The authors use a custom-generated dataset to simulate different magnitudes and types of bias.
* Baselines/Comparisons: The authors compare the performance of different methods using fairness metrics such as selection rate and profit.
* Main claimed findings: The authors demonstrate that even minimal uncertainty-aware adjustments can shift fairness outcomes without sacrificing utility, and that no single method dominates; the appropriate uncertainty-aware strategy depends on the structure of the bias present.

**What to Verify in the PDF**
==========================

* The authors mention that existing datasets commonly used in the Fair ML literature, such as Adult and German Credit, would not have allowed for this type of experiment.
* The authors use a custom-generated dataset to simulate different magnitudes and types of bias, but it would be interesting to see how the results would generalize to real-world datasets.
* The authors mention that the taxonomy of bias types and their interactions is not fully explored, and it would be interesting to see more details on this topic.
* The authors also mention that the authors' approach is not intended as fairness guarantees or production-ready solutions, but rather as a foundation for developing more robust approaches.
{% endraw %}
