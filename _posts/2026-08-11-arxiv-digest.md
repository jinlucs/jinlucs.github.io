---
layout: post
title: "Daily arXiv Digest — 2026-08-11 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Competitive mediator games and urban CAV routing markets
- **Authors:** Grzegorz Jamróz
- **arXiv:** [2608.09894](https://arxiv.org/abs/2608.09894v1) · [pdf](https://arxiv.org/pdf/2608.09894v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.09894v1))
- **Categories:** cs.GT, cs.MA, econ.TH, math.OC

### Abstract
> Inspired by possible future markets of autonomous routing and driving (ARAD), we introduce competitive mediator games and their equilibria which generalize the (coarse) correlated equilibria, which have become a popular research area recently as they not only can be more socially efficient than Nash equilibria but also are limits of algorithmic no-regret multi-agent learning dynamics. We discuss the basic properties of competitive mediator games and prove that in the generic setting of anonymous congestion(routing) games with market-share maximizing mediators all competitive mediator equilibria are monopolies whenever one of the mediators is weakly preferred to other mediators by all users. We apply and interpret these results in the context of new markets of competing ARAD service providers. We also provide a comprehensive overview of these markets and discuss the future mechanism design thereof.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 0.5*15=7.5

* Equation: 0.5*15=7.5
* Symbols: None
* Why it matters: Not found in extracted context.

### Equation 2: A=\{a1,a2,\dots,\}

* Equation: A=\{a1,a2,\dots,\}
* Symbols: A, a1, a2, ...
* Why it matters: Represents the set of actions available to a user in a standard game.

### Equation 3: A=\{r1,r2\}

* Equation: A=\{r1,r2\}
* Symbols: A, r1, r2
* Why it matters: Represents the set of actions available to a user in a mediated game, where A is the set of routes and F is the set of mediators.

### Equation 4: r1,r2

* Equation: r1,r2
* Symbols: r1, r2
* Why it matters: Not found in extracted context.

### Equation 5: a1,a2,\dots

* Equation: a1,a2,\dots
* Symbols: a1, a2, ...
* Why it matters: Represents the set of actions available to a user in a mediated game, where a1, a2, ... are the routes chosen by the mediator.

**Method Summary**
==================

* The authors introduce competitive mediator games and their equilibria, which generalize correlated equilibria.
* The authors discuss the basic properties of competitive mediator games and prove that in the generic setting of anonymous congestion(routing) games with market-share maximizing mediators, all competitive mediator equilibria are monopolies whenever one of the mediators is weakly preferred to other mediators by all users.
* The authors apply and interpret these results in the context of new markets of competing ARAD service providers.
* The authors provide a comprehensive overview of these markets and discuss the future mechanism design thereof.

**Experimental Overview**
========================

* Tasks/Datasets: Not found in extracted context.
* Baselines/Comparisons: Not found in extracted context.
* Main Claimed Findings: Not found in extracted context.

**What to Verify in the PDF**
=============================

* The authors' formal framework for competitive mediator games and their equilibria.
* The proof that in the generic setting of anonymous congestion(routing) games with market-share maximizing mediators, all competitive mediator equilibria are monopolies whenever one of the mediators is weakly preferred to other mediators by all users.
* The authors' application and interpretation of these results in the context of new markets of competing ARAD service providers.
{% endraw %}

{% raw %}
## 2) BDH-CQ: In-Context Learning with Recurrent Latent Reasoning
- **Authors:** Björn Engdahl, Adrian Kosowski, Jan Chorowski, Zuzanna Stamirowska, Przemysław Uznański, Junlin Jiang, Rohan Phadke, Remigiusz Kinas, Richard Zhong
- **arXiv:** [2608.09888](https://arxiv.org/abs/2608.09888v1) · [pdf](https://arxiv.org/pdf/2608.09888v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.09888v1))
- **Categories:** cs.NE, cs.AI, cs.LG, stat.ML

### Abstract
> We introduce BDH-CQ, a reasoning model that combines in-context learning with recurrent latent reasoning. Inputs presented at inference time continuously update the model's recurrent memory; the model then solves a query through iterative computation in a high-dimensional latent space, without verbalizing its intermediate reasoning. We evaluate the model on the public ARC-AGI-1 evaluation set and use controlled ARC-like interventions to study what it learns from demonstrations, how consistently it applies an inferred transformation, and which concepts remain difficult. A 150M-parameter configuration reaches 29.5% pass@2 at a computed inference cost of \$0.0007 per task. This operating point breaks through the previously reported ARC-AGI-1 cost-accuracy Pareto frontier, establishing a new state of the art in benchmark cost efficiency.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: D=\{(x_{t},y_{t})\}_{t=1}^{K}

* Equation: D=\{(x_{t},y_{t})\}_{t=1}^{K}
* Symbols: D (dataset), x_t (input), y_t (output), K (number of tasks)
* Why it matters: This equation represents the dataset used for training and testing the model.

### Equation 2: x^{\star}

* Equation: x^{\star}
* Symbols: x^{\star} (query or target input)
* Why it matters: This equation represents the input that the model needs to solve or query.

### Equation 3: S_{t}=U_{\theta}(S_{t-1},D_{t})

* Equation: S_{t}=U_{\theta}(S_{t-1},D_{t})
* Symbols: S_t (state or memory), U_{\theta} (update function), S_{t-1} (previous state), D_t (new data)
* Why it matters: This equation represents the update of the model's memory or state using the new data and the previous state.

### Equation 4: D_{t}

* Equation: D_{t}
* Symbols: D_t (new data)
* Why it matters: This equation represents the new data that is added to the model's memory at each time step.

### Equation 5: \theta

* Equation: \theta
* Symbols: \theta (model parameters)
* Why it matters: This equation represents the model's parameters that are updated during training.

**Method Summary**
==================

* The model uses in-context learning with recurrent latent reasoning to solve tasks.
* The model updates its memory or state using the new data and the previous state.
* The model is trained on a dataset of demonstration pairs and test pairs.
* The model is evaluated on the public ARC-AGI-1 evaluation set and other datasets.

**Experimental Overview**
=========================

* Tasks/Datasets: The model is evaluated on the public ARC-AGI-1 evaluation set and other datasets such as ConceptARC.
* Baselines/Comparisons: The model is compared to other models such as GPT 5.6 Luna.
* Main Claimed Findings: The model achieves a pass@2 accuracy of 29.5% on the public ARC-AGI-1 evaluation set at a cost of $0.0007 per task, which is less than one-tenth of a cent.

**What to Verify in the PDF**
=============================

* The training data and objective used to train the model.
* The evaluation metrics used to evaluate the model's performance.
* The results of the independent black-box audit conducted by co-authors from Bielik and New York University.
{% endraw %}

{% raw %}
## 3) Financial Numerical Prediction and Allocation as Token Generation
- **Authors:** Xu Ouyang, Moontae Lee
- **arXiv:** [2608.09880](https://arxiv.org/abs/2608.09880v1) · [pdf](https://arxiv.org/pdf/2608.09880v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.09880v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> Financial prediction typically relies on task-specific regression, ranking, or policy heads, separating the language model from the numerical object ultimately evaluated. We investigate whether a causal language model can instead represent forecasts and decisions directly through constrained token generation. FinATOM introduces a unified, head-free interface for three-step stock-return forecasting and dynamic five-ETF allocation. The forecasting model autoregressively emits volatility-standardized return tokens and is trained with ordinal and ranking supervision followed by a one-epoch token-level policy stage. The allocation model generates normalized long-only weights; supervised fine-tuning imitates a causal mean--variance anchor, and DAPO-augmented GRPO optimizes realized 21-day Sharpe subject to anchor consistency. In 2023--2025 ETF tests, the allocation policy improves pooled gross Sharpe from 1.428 to 1.529 and net Sharpe under a 5-bp transaction-cost model from 1.394 to 1.494. The multimodal allocation input attains the highest three-period mean Sharpe of 1.540, with its clearest advantage in 2025. On FinTexTS, the SFT and policy strategies achieve 73.52\%/2.68 and 73.72\%/2.69 cumulative-return/Sharpe, respectively. These results support the feasibility of direct language-model token generation for financial numerical prediction and decision-making, while motivating broader tests across assets, regimes, and random seeds.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `x_{t}`

* Equation: Not explicitly defined in the context
* Symbols: `x_{t}` (input at time `t`)
* Why it matters: Not found in extracted context.

### Equation 2: `y_{t}=(y_{t,1},\ldots,y_{t,L})`

* Equation: Not explicitly defined in the context
* Symbols: `y_{t}` (output at time `t`), `y_{t,1},\ldots,y_{t,L}` (components of `y_{t}`)
* Why it matters: Not found in extracted context.

### Equation 3: `p_{\theta}(y_{t}\mid x_{t})=\prod_{\ell=1}^{L}p_{\theta}(y_{t,\ell}\mid x_{t},y_{t,<\ell})`

* Equation: Conditional probability of `y_{t}` given `x_{t}`
* Symbols: `p_{\theta}(y_{t}\mid x_{t})` (conditional probability), `p_{\theta}(y_{t,\ell}\mid x_{t},y_{t,<\ell})` (conditional probability of component `y_{t,\ell}`)
* Why it matters: Describes the probability model used by the language model.

### Equation 4: `R_{t}\in\mathbb{R}^{20\times 5}`

* Equation: Not explicitly defined in the context
* Symbols: `R_{t}` (return matrix at time `t`)
* Why it matters: Not found in extracted context.

### Equation 5: `\mu_{t}`

* Equation: Not explicitly defined in the context
* Symbols: `\mu_{t}` (mean at time `t`)
* Why it matters: Not found in extracted context.

### Equation 6: `\Sigma_{t}`

* Equation: Not explicitly defined in the context
* Symbols: `\Sigma_{t}` (covariance matrix at time `t`)
* Why it matters: Not found in extracted context.

### Equation 7: `\displaystyle\widetilde{\boldsymbol{w}}_{t}=\arg\min_{\boldsymbol{w}\in\mathcal{W}}\;\sqrt{252\,\boldsymbol{w}^{\top}\Sigma_{t}\boldsymbol{w}}-0.05(252\mu_{t})^{\top}\boldsymbol{w}`

* Equation: Optimization problem for weight vector `\boldsymbol{w}`
* Symbols: `\boldsymbol{w}` (weight vector), `\Sigma_{t}` (covariance matrix), `\mu_{t}` (mean)
* Why it matters: Describes the optimization objective used to find the optimal weight vector.

### Equation 8: `\displaystyle\sqrt{252\,\boldsymbol{w}^{\top}\Sigma_{t}\boldsymbol{w}}-0.05(252\mu_{t})^{\top}\boldsymbol{w}`

* Equation: Objective function for optimization problem
* Symbols: `\boldsymbol{w}` (weight vector), `\Sigma_{t}` (covariance matrix), `\mu_{t}` (mean)
* Why it matters: Describes the objective function used to optimize the weight vector.

**Method Summary**
==================

* The authors propose a unified, head-free interface for financial numerical prediction and allocation using a causal language model.
* The model uses a shared token-native design, where the backbone models are LoRA-adapted Llama 3.2 1B architectures with tied vocabulary projection.
* The policy stage is trained using ordinal and ranking supervision, and the allocation model generates normalized long-only weights.
* The authors evaluate the performance of the model using various metrics, including Sharpe ratio, annual return, and volatility.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Financial numerical prediction and allocation
	+ Stock forecasting using FinTexTS
	+ Portfolio allocation using a daily multimodal dataset
* Baselines/Comparisons:
	+ FinTexTS row
	+ Causal teacher
	+ Equal weighting
* Main Claimed Findings:
	+ The policy stage improves the return-risk tradeoff rather than exploiting extra trading intensity.
	+ The allocation model achieves the highest pooled Sharpe among the learned policies.

**What to Verify in the PDF**
=============================

* The authors claim that the policy stage mainly improves the return-risk tradeoff rather than exploiting extra trading intensity. Verify this claim by examining the results of the pooled comparison in Table 3.
* The authors also claim that the allocation model achieves the highest pooled Sharpe among the learned policies. Verify this claim by examining the results of Table 2.
* The authors use a daily multimodal dataset for five liquid ETFs. Verify the composition of the dataset and the construction of the dataset.
* The authors use FinTexTS for stock forecasting. Verify the composition of FinTexTS and the construction of the stock forecasting experiment.
{% endraw %}

{% raw %}
## 4) Logarithmic-Free Moment and Generalization Bounds for Uniformly Stable Algorithms
- **Authors:** Thanh Nguyen-Cung, Binh T. Nguyen
- **arXiv:** [2608.09870](https://arxiv.org/abs/2608.09870v1) · [pdf](https://arxiv.org/pdf/2608.09870v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.09870v1))
- **Categories:** stat.ML, cs.LG, math.PR, math.ST

### Abstract
> Uniform stability is a classical tool for controlling the generalization error of a learning algorithm. Bousquet, Klochkov, and Zhivotovskiy (2020) showed that the problem can be reduced to a moment inequality for a sum of weakly interacting functions of independent random variables. Their bound contains an additional factor $\log n$, and they asked whether this factor can be removed. We answer this upper-bound question affirmatively. More specifically, let $Z=(Z_1,\ldots,Z_n)$ have independent coordinates and let $g_i(Z)$ satisfy $$ \mathbb E[g_i(Z)\mid Z_{-i}]=0, \qquad \left| \mathbb E[g_i(Z)\mid Z_i]\right|\le M, \qquad \forall i = \overline{1, n} $$ while changing any coordinate $Z_j$, $j\neq i$, changes $g_i$ by at most $β$ and $Z_{-i}$ denotes all coordinates except $Z_i$. We prove that, for every $p\ge2$, $$ \left\| \sum_{i=1}^n g_i(Z)\right\|_p \le 16pnβ+M\sqrt{2pn}. $$ This removes the $\log n$ factor from the previous bound and matches the lower bound of Bousquet, Klochkov, and Zhivotovskiy up to universal constants in the range covered by their construction. Our proof first establishes the required estimate on the Rademacher cube, then transfers it to arbitrary product distributions by a two-copy randomization argument.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\log n$

* Equation: $\log n$
* Symbols: $\log n$ (natural logarithm)
* Why it matters: This equation is not explicitly used in the paper, but it is mentioned in the abstract as a factor that needs to be removed.

### Equation 2: $Z = (Z_1, \ldots, Z_n)$

* Equation: $Z = (Z_1, \ldots, Z_n)$
* Symbols: $Z$ (product space), $Z_i$ (coordinate)
* Why it matters: This equation defines the product space, which is used throughout the paper.

### Equation 3: $g_i(Z)$

* Equation: $g_i(Z)$
* Symbols: $g_i$ (function), $Z$ (product space)
* Why it matters: This equation defines the function $g_i$ that is used in the moment inequality.

### Equation 4: $\mathbb{E}[g_i(Z) \mid Z_{-i}] = 0$, $\left|\mathbb{E}[g_i(Z) \mid Z_i]\right| \leq M$, $\forall i = \overline{1, n}$

* Equation: $\mathbb{E}[g_i(Z) \mid Z_{-i}] = 0$, $\left|\mathbb{E}[g_i(Z) \mid Z_i]\right| \leq M$, $\forall i = \overline{1, n}$
* Symbols: $\mathbb{E}[g_i(Z) \mid Z_{-i}]$ (conditional expectation), $\left|\mathbb{E}[g_i(Z) \mid Z_i]\right|$ (absolute value of conditional expectation), $M$ (bound on the absolute value of the conditional expectation), $i$ (index)
* Why it matters: This equation states the assumptions on the functions $g_i$ that are used in the moment inequality.

### Equation 5: $Z_j$

* Equation: $Z_j$
* Symbols: $Z_j$ (coordinate)
* Why it matters: This equation is not explicitly used in the paper, but it is part of the definition of the product space.

### Equation 6: $j \neq i$

* Equation: $j \neq i$
* Symbols: $j$ (index), $i$ (index)
* Why it matters: This equation is used to define the function $g_i$.

### Equation 7: $g_i$

* Equation: $g_i$
* Symbols: $g_i$ (function)
* Why it matters: This equation is not explicitly used in the paper, but it is part of the definition of the function $g_i$.

### Equation 8: $\beta$

* Equation: $\beta$
* Symbols: $\beta$ (parameter)
* Why it matters: This equation is not explicitly used in the paper, but it is part of the definition of the parameter $\beta$.

**Method Summary**
================

* The paper proves a logarithmic-free moment and generalization bounds for uniformly stable algorithms.
* The algorithm is defined as $\gamma$-uniformly stable, where $\gamma$ is a parameter that controls the stability of the algorithm.
* The loss function is assumed to be bounded by $L$, and the algorithm is shown to have a generalization error that is bounded by a function of the parameter $\beta$ and the number of samples $n$.

**Experimental Overview**
=====================

* The paper does not provide any experimental results or datasets.
* The authors compare their algorithm to the baseline algorithm of Bousquet et al. [2], which has a logarithmic factor in its bound.
* The main claimed finding is that the authors' algorithm has a logarithmic-free bound, which is more efficient than the baseline algorithm.

**What to Verify in the PDF**
==========================

* The assumptions on the functions $g_i$ and the parameter $\beta$ are not explicitly stated in the abstract.
* The proof of the logarithmic-free bound is not provided in the abstract.
* The experimental results and datasets are not provided in the abstract.
{% endraw %}

{% raw %}
## 5) Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation
- **Authors:** Yubo Jiang, Fengying Xie, Zhiguo Jiang, Haopeng Zhang
- **arXiv:** [2608.09826](https://arxiv.org/abs/2608.09826v1) · [pdf](https://arxiv.org/pdf/2608.09826v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.09826v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Reinforcement learning with verifiable rewards yields no group-relative signal when rollout groups are uniformly correct or uniformly wrong, which account for 63.0-68.0% of groups in our experiments. We propose SKALD (Skill-Anchored Latent Distillation), an on-policy self-distillation framework that uses two context views of the same Qwen3-Base model: a question-only student and a teacher conditioned on an abstract, explicit-answer-filtered skill card. The student is trained on its own prefixes, transferring the skill-induced advantage into shared parameters without privileged input at test time. To stabilize context-induced distribution mismatch, SKALD employs an annealed exponentially tilted objective that downweights teacher-preferred tokens with very low student likelihood; as the tilt vanishes, it converges to teacher cross-entropy and recovers the forward-KL student gradient. An empirical gate activates distillation only when verified rollouts estimate a positive teacher advantage. Across five held-out mathematics benchmarks, SKALD improves overall avg@8 over GRPO by +2.46, +4.85, and +12.01 at 0.6B, 1.7B, and 4B, respectively. At 1.7B, zero-variance-only distillation recovers 84.7% of the full gain, while SKALD remains +4.06 above FLOP-matched GRPO and exceeds contextual skill exposure by +3.77. These results show that abstract skills provide dense supervision where group-relative rewards become uninformative.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 
^{1,3~\dagger}

* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: 
63.0

* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Refers to the percentage of rollout groups that are uniformly correct or uniformly wrong.

### Equation 3: 
68.0\%

* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Refers to the percentage of rollout groups that are uniformly wrong.

### Equation 4: 
+2.46

* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Refers to the mean gain of SKALD over GRPO at scale 0.6B.

### Equation 5: 
+4.85

* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Refers to the mean gain of SKALD over GRPO at scale 1.7B.

### Equation 6: 
+12.01

* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Refers to the mean gain of SKALD over GRPO at scale 4B.

### Equation 7: 
84.7\%

* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Refers to the percentage of full gain recovered by zero-variance-only distillation at scale 1.7B.

### Equation 8: 
+4.06

* Equation: Not explicitly defined in the context.
* Symbols: Not found in extracted context.
* Why it matters: Refers to the gain of SKALD over GRPO at scale 1.7B.

**Method Summary**
================

* SKALD trains a single model through two context views, eliminating the costs of external teachers.
* The student sees only the problem, while the self-teacher sees an abstract skill.
* The empirical gate activates distillation only when verified rollouts estimate a positive teacher advantage.
* The annealed exponentially tilted objective downweights teacher-preferred tokens with very low student likelihood.

**Experimental Overview**
=====================

* Tasks/Datasets: MATH500, AMC23, AIME24, AIME25, and Minerva.
* Baselines/Comparisons: GRPO (group-normalized REINFORCE).
* Main Claimed Findings: SKALD attains the best overall avg@8 and pass@8 at all three tested scales, with mean gains over GRPO of +2.46, +4.85, and +12.01.
{% endraw %}
