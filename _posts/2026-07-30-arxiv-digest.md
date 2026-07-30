---
layout: post
title: "Daily arXiv Digest — 2026-07-30 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes
- **Authors:** Lennon J. Shikhman, Michael Galarnyk, Aadi Dash, Nicholas A. Welsh
- **arXiv:** [2607.27188](https://arxiv.org/abs/2607.27188v1) · [pdf](https://arxiv.org/pdf/2607.27188v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.27188v1))
- **Categories:** cs.LG, q-fin.CP, q-fin.PR, q-fin.ST

### Abstract
> Accurate option prices do not imply accurate recovery of the latent risk-neutral density. We study this distinction with two complementary benchmarks. A controlled benchmark exposes simulator-truth densities for latent evaluation, while a chronological NIFTY benchmark tests only held-out market prices. A two-component lognormal mixture has the lowest aggregate price, $L^1$, Wasserstein, and fixed-tail errors on the synthetic benchmark. Learned operators retain narrower strengths: DeepONet reduces 1% quantile and variance error by 39.0% and 34.6% relative to the mixture, and a quote transformer reduces $L^1$ by 16.4% on the structurally misspecified Merton family. A numerical conditioning analysis explains why these rankings can differ: after enforcing mass and forward constraints, 95 of 126 pricing directions are numerically null, and two densities separated by $L^1 = 0.061$ produce identical prices on the covered strikes. On 524 held-out NIFTY calls, validation-selected test-time adaptation reduces DeepONet RMSE by 28.3%, but per-expiry mixture and SVI fits remain much more accurate. The evidence supports target-dependent inductive bias, not a universal winner.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: L^{1}

L^{1} = \sum_{i=1}^{n} |x_i - y_i|

* Equation: L^{1} is the L1 loss function, which calculates the sum of absolute differences between predicted and actual values.
* Symbols: x_i represents the predicted values, y_i represents the actual values, and n is the number of data points.
* Why it matters: The L1 loss function is used to evaluate the performance of the models in terms of mean absolute error.

### Equation 2: 39.0\%

* Equation: This is the relative reduction in 1% quantile error achieved by DeepONet compared to the mixture baseline.
* Symbols: 39.0% is the percentage reduction in error.
* Why it matters: This equation shows the improvement in performance of DeepONet over the mixture baseline.

### Equation 3: 34.6\%

* Equation: This is the relative reduction in variance error achieved by DeepONet compared to the mixture baseline.
* Symbols: 34.6% is the percentage reduction in error.
* Why it matters: This equation shows the improvement in performance of DeepONet over the mixture baseline.

### Equation 4: 16.4\%

* Equation: This is the relative reduction in L1 loss achieved by the quote transformer compared to the mixture baseline.
* Symbols: 16.4% is the percentage reduction in error.
* Why it matters: This equation shows the improvement in performance of the quote transformer over the mixture baseline.

### Equation 5: L^{1}=0.061

* Equation: This is the L1 loss value for two densities that produce identical prices on the covered strikes.
* Symbols: L^{1}=0.061 represents the L1 loss value.
* Why it matters: This equation shows the similarity between two densities that produce identical prices.

### Equation 6: 28.3\%

* Equation: This is the relative reduction in RMSE achieved by validation-selected test-time adaptation on DeepONet.
* Symbols: 28.3% is the percentage reduction in error.
* Why it matters: This equation shows the improvement in performance of validation-selected test-time adaptation on DeepONet.

### Equation 7: \tau

* Equation: This represents the maturity parameter.
* Symbols: \tau represents the maturity parameter.
* Why it matters: This equation is used to define the forward price and normalized log terminal price.

**Method Summary**
==================

* The primary protocol uses supervised density MSE as the objective function.
* The objective ablation compares density MSE with combinations of observed-quote MSE, forward-moment penalty, and H1-style grid roughness penalty.
* The learned models are compared to a direct mixture baseline.
* The quote transformer has the lowest stable learned L1 loss and W1 loss, while DeepONet has the best learned fixed-tail, 1% quantile, variance, and price errors.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Synthetic benchmark: 3,000 examples with a 70/15/15 split, 128-node strike grid, and 16 maturities.
	+ Real NIFTY held-out evaluation: 6,191 calls, 295 dates, and 19 expiries.
* Baselines/Comparisons:
	+ Mixture baseline
	+ DeepONet
	+ Quote transformer
	+ FNO
* Main Claimed Findings:
	+ The quote transformer has the lowest stable learned L1 loss and W1 loss.
	+ DeepONet has the best learned fixed-tail, 1% quantile, variance, and price errors.
	+ Validation-selected test-time adaptation improves performance on DeepONet.

**What to Verify in the PDF**
=============================

* The exact implementation details of the models, including the architecture and hyperparameters.
* The results of the objective ablation, including the comparison of density MSE with combinations of observed-quote MSE, forward-moment penalty, and H1-style grid roughness penalty.
* The results of the chronological NIFTY held-out evaluation, including the comparison of the quote transformer and DeepONet with the mixture baseline.
{% endraw %}

{% raw %}
## 2) From Classification to Regression: Using a Fruitfly to Solve Equations
- **Authors:** Shady E. Ahmed, Panos Stinis
- **arXiv:** [2607.27196](https://arxiv.org/abs/2607.27196v1) · [pdf](https://arxiv.org/pdf/2607.27196v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.27196v1))
- **Categories:** cs.LG, math.NA

### Abstract
> We present a novel approach to regression tasks using classification which is motivated by the mechanism used by fruitflies to sense their environment. Specifically, we formulate a general framework for learning nonlinear input-output relationships by replacing complex global surrogate models with a finite library of representative local patterns. Since scientific data often occupy limited and recurring regions of the input space, we generate predictions by measuring similarities between a query and stored patterns, then combining their associated responses through weighted reconstruction. We apply this approach to nonlinear dynamical systems, data-driven regression, and physics-informed learning using suitable embeddings and similarity measures. For dynamical systems, our offline-online workflow extracts patterns from data or governing equations during the offline phase, while online prediction requires only similarity evaluation and response aggregation. This structure helps us reduce computational and memory demands while providing explicit control over the trade-off among accuracy, storage, and inference cost.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: \frac{du}{dt}=f(u)

* Equation: \frac{du}{dt}=f(u)
* Symbols: u (state variable), f (function)
* Why it matters: This equation represents the time derivative of the state variable u, which is a fundamental concept in dynamical systems.

### Equation 2: \frac{du}{dt}=f(u)

* Equation: \frac{du}{dt}=f(u)
* Symbols: u (state variable), f (function)
* Why it matters: This equation is identical to Equation 1, but it's repeated for emphasis. It still represents the time derivative of the state variable u.

### Equation 3: u(t+\Delta t)=\mathcal{M}(u(t))

* Equation: u(t+\Delta t)=\mathcal{M}(u(t))
* Symbols: u (state variable), \mathcal{M} (map or function)
* Why it matters: This equation represents the evolution of the state variable u over a time step \Delta t, using a map or function \mathcal{M}.

### Equation 4: u\in\mathbb{R}^{n}

* Equation: u\in\mathbb{R}^{n}
* Symbols: u (state variable), n (dimensionality)
* Why it matters: This equation specifies the domain of the state variable u as a vector space of dimension n, which is a common representation in dynamical systems.

### Equation 5: \frac{du}{dt}=f(u)

* Equation: \frac{du}{dt}=f(u)
* Symbols: u (state variable), f (function)
* Why it matters: This equation is identical to Equation 1 and Equation 2, but it's repeated again for emphasis. It still represents the time derivative of the state variable u.

**Method Summary**
==================

* The proposed framework reformulates regression as a classification problem by interpreting class activations as input-dependent reconstruction coefficients.
* The model learns a collection of representative local patterns together with their associated responses.
* Prediction proceeds by associating the current input to these representative patterns and reconstructing the desired output through their weighted combination.
* The framework is motivated by the mechanism used by fruitflies to sense their environment, where similarities between a query and stored patterns are measured and combined to produce a response.

**Experimental Overview**
=========================

* Tasks/Datasets: The proposed framework is applied to nonlinear dynamical systems, data-driven regression, and physics-informed learning.
* Baselines/Comparisons: The authors compare the proposed framework to existing methods such as reduced-order models, kernel methods, Gaussian processes, and deep neural networks.
* Main Claimed Findings: The proposed framework achieves competitive performance with existing methods while requiring substantially fewer floating-point operations and memory accesses.

**What to Verify in the PDF**
=============================

* The authors claim that the proposed framework can be extended to general regression problems through an appropriate choice of input embedding. Verify that this is indeed the case and explore the implications of this extension.
* The authors mention that the framework can be used for physics-informed learning. Verify that this is the case and explore the benefits and limitations of this application.
* The authors discuss the trade-off between accuracy, storage, and inference cost. Verify that the proposed framework can achieve competitive performance while reducing the inference cost and explore the implications of this trade-off.
{% endraw %}

{% raw %}
## 3) Can AI agents conduct open-ended AI research? Early evidence from two case studies
- **Authors:** Peter Kirgis, Sayash Kapoor, Andrew Schwartz, Stephan Rabanser, David Africa, Konstantinos Voudouris, Viet Nguyen, Toby Pilditch, Magda Dubois, Harry Coppock, Cozmin Ududec, Nitya Nadgir, Matilda Orona, Tilman Bayer, Derrick Chan-Sew, Yue Ling, Abhishek Shetty, Helen Toner, Gillian Hadfield, Seth Lazar, Steve Newman, Shoshannah Tekofsky, Rishi Bommasani, Arvind Narayanan
- **arXiv:** [2607.27191](https://arxiv.org/abs/2607.27191v1) · [pdf](https://arxiv.org/pdf/2607.27191v1)
- **LLM context source:** abstract only
- **Categories:** cs.AI, cs.CY, cs.LG

### Abstract
> Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on narrow, verifiable tasks, which excludes open-ended research, or submit AI-generated papers to blind peer review, which is overstretched, stochastic, and suffers from poor review quality. We introduce a third way to measure progress towards AI R\&D automation. An agent takes on the central, open-ended research question of a high-quality unpublished paper, and the paper's original authors grade its output. We call these shadow evaluations. We ran shadow evaluations on two unpublished NeurIPS 2026 submissions, giving frontier agents six days and thousands of dollars of compute. The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions. As a result, both papers were unambiguously rejected by the authors. We identify five recurring failure modes: poor judgment about the bar for publishable research, uncreative responses to shortcomings in the research design, ineffective backtracking from dead ends, poor resource awareness, and instruction drift. A robustness check with a second model and scaffold reproduced these failures. We release the expert reviews, survey responses, agent repositories, and logs. Our results provide early evidence that today's agents can do the engineering of AI research, but struggle with critical parts of the research lifecycle.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough

Unfortunately, no equations were found in the extracted context.

### Method Summary

* The authors introduce a new method called "shadow evaluations" to measure progress towards AI R&D automation.
* They use this method to evaluate two unpublished NeurIPS 2026 submissions.
* The authors provide a robustness check with a second model and scaffold to reproduce the failures.
* The method involves giving frontier agents a central, open-ended research question and grading their output based on expert reviews.

### Experimental Overview

* Tasks/Datasets: Unpublished NeurIPS 2026 submissions
* Baselines/Comparisons: None mentioned in the abstract
* Main Claimed Findings: Agents can complete the engineering of AI research, but struggle with critical parts of the research lifecycle.

### What to Verify in the PDF

* The expert reviews, survey responses, agent repositories, and logs mentioned in the abstract.
* The details of the two unpublished NeurIPS 2026 submissions that were used for the shadow evaluations.
* The five recurring failure modes identified in the paper, including poor judgment about the bar for publishable research and ineffective backtracking from dead ends.
{% endraw %}

{% raw %}
## 4) Skillful forecasting of offshore winds from satellite scatterometer constellations
- **Authors:** Francesco Pinto, Luca Lanzilao, Paco Lopez Dekker, Angela Meyer
- **arXiv:** [2607.27152](https://arxiv.org/abs/2607.27152v1) · [pdf](https://arxiv.org/pdf/2607.27152v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.27152v1))
- **Categories:** cs.LG

### Abstract
> Accurate intraday forecasts of offshore wind are becoming increasingly important for power system operation and the integration of growing shares of offshore wind energy. Operational forecasts rely predominantly on numerical weather prediction (NWP), which is not optimized for lead times of minutes to hours, where initial-condition accuracy dominates forecast skill. Although satellite scatterometer observations are routinely assimilated into NWP, they have not previously been used directly for forecasting. Here we present WindCastNet, the first satellite-based nowcasting framework for offshore wind speed and direction, introducing a new paradigm for intraday forecasting that learns from spatiotemporally irregular satellite observations. WindCastNet predicts offshore wind fields from observations acquired by satellite scatterometer constellations. WindCastNet employs a partial convolutional long short-term memory network that exploits microwave radar observations from the European, Chinese, and Indian scatterometers despite their irregular spatial coverage, asynchronous sampling, and variable revisit times. Spatial observation masks and inter-observation intervals are encoded, while a continuous temporal representation enables forecasts at arbitrary lead times. Evaluated over the North Sea, WindCastNet reduces the root-mean-square error by 23% and 7% relative to the HARMONIE MEPS model at lead times of 1 and 2 h, respectively, and outperforms persistence by 9-15% during the first three forecast hours. Forecast skill decreases under strong-wind conditions and spatially non-uniform flow. These results demonstrate that satellite scatterometer constellations can provide an independent and competitive source of short-term offshore wind forecasts, opening new opportunities for renewable energy forecasting but also broader marine weather applications, including tropical cyclone nowcasting.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 0.01

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: 25 × 25

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 3: 1300

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 4: 1400

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 5: 15%

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 6: 19630

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 7: 13223

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

**Method Summary**
==================

* The authors propose a new framework for offshore wind speed and direction forecasting using satellite scatterometer constellations.
* The framework, called WindCastNet, uses a partial convolutional long short-term memory network to exploit microwave radar observations from multiple satellites.
* The network is designed to handle spatiotemporally irregular satellite observations and can generate forecasts at arbitrary lead times.
* The authors evaluate the performance of WindCastNet using a benchmark model, HARMONIE-AROME MEPS, and find that it reduces the root-mean-square error by 23% and 7% at lead times of 1 and 2 hours, respectively.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors evaluate the performance of WindCastNet using a test set of over 4.4 million observations across the study domain.
* Baselines/Comparisons: The authors compare the performance of WindCastNet with the HARMONIE-AROME MEPS model.
* Main Claimed Findings: WindCastNet reduces the root-mean-square error by 23% and 7% at lead times of 1 and 2 hours, respectively, and outperforms HARMONIE-AROME MEPS for lead times up to 2.5 hours.

**What to Verify in the PDF**
=============================

* The authors mention that the model is trained with a partial-convolution reconstruction loss adapted from [pconvlstm](https://arxiv.org/abs/2006.10923). Verify the details of this loss function and its implementation.
* The authors also mention that the model is evaluated using a Pearson correlation coefficient of approximately r = 0.95. Verify the calculation of this coefficient and its significance.
* The authors provide a histogram showing the amount of grid cells observed at each timestamp. Verify the details of this histogram and its interpretation.
{% endraw %}

{% raw %}
## 5) MindForge: Teaching Small Language Models Whole-Life-Cycle Software Engineering via Source-Free Program Synthesis
- **Authors:** Yihao Chen, Shi Chang, Khaled Chawa, Feng Lin, Boyuan Chen, Shaowei Wang, Ahmed E. Hassan
- **arXiv:** [2607.27146](https://arxiv.org/abs/2607.27146v1) · [pdf](https://arxiv.org/pdf/2607.27146v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.27146v1))
- **Categories:** cs.SE, cs.CL, cs.LG

### Abstract
> Coding agents have made substantial progress on software engineering tasks that modify existing codebases, including bug fixing and feature implementation. However, constructing a complete program from scratch remains a major challenge: even the frontier models evaluated on ProgramBench fully resolve fewer than 1% of tasks. One obstacle is the lack of scalable training environments for this from-scratch setting, spanning the whole software engineering life cycle, as existing environment-construction frameworks focus only on a single phase in software development. To address this gap, we introduce MindForge, an automated pipeline that converts open-source command-line programs into source-free environments that expose only a compiled reference executable and its documentation. Using MindForge, we construct training environments from repositories disjoint from those in ProgramBench, and curate a high-quality data recipe consisting of program synthesis trajectories using GLM-5.2 as the teacher agent. Fine-tuning Qwen3.6-27B on these trajectories increases its ProgramBench average test pass rate from 37.98% to 49.51%, achieving performance comparable to substantially larger frontier models. Moreover, the fine-tuned model consistently improves over the base model across all seven unseen software engineering benchmarks, spanning long-horizon repository generation and translation, bug fixing, feature implementation, and cross-language issue resolution, with absolute gains of 31.00 points on RepoZero-C2Rust, 14.16 on DeepSWE, 10.70/4.56 on NL2Repo-Bench (with/without tests), 5.04 on SWE-bench Verified, 5.93 on SWE-bench Pro, 5.22 on SWE-bench Multilingual, and 4.94 on FeatBench.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\beta_{1}=0.9$

* Equation: $\beta_{1}=0.9$
* Symbols: $\beta_{1}$ (learning rate for the first moment)
* Why it matters: This is the learning rate for the first moment, which is used in the AdamW optimization algorithm.

### Equation 2: $\beta_{2}=0.98$

* Equation: $\beta_{2}=0.98$
* Symbols: $\beta_{2}$ (learning rate for the second moment)
* Why it matters: This is the learning rate for the second moment, which is also used in the AdamW optimization algorithm.

### Equation 3: $0.04$

* Equation: $0.04$
* Symbols: None
* Why it matters: This is the weight decay value, which is used to prevent overfitting in the AdamW optimization algorithm.

### Equation 4: $4\times 10^{-5}$

* Equation: $4\times 10^{-5}$
* Symbols: None
* Why it matters: This is the initial learning rate, which is used in the AdamW optimization algorithm.

### Equation 5: $4\times 10^{-6}$

* Equation: $4\times 10^{-6}$
* Symbols: None
* Why it matters: This is the final learning rate, which is used in the AdamW optimization algorithm.

**Method Summary**
================

* The authors introduce MindForge, an automated pipeline that converts open-source command-line programs into source-free environments.
* The pipeline uses a combination of program synthesis and reinforcement learning to generate a high-quality data recipe.
* The authors fine-tune a language model (Qwen3.6-27B) on this data recipe and evaluate its performance on a range of software engineering benchmarks.
* The authors also analyze the behavior of the model and its teacher model on a set of tasks.

**Experimental Overview**
=====================

* Tasks/Datasets: The authors evaluate the performance of the fine-tuned model on a range of software engineering benchmarks, including ProgramBench, DeepSWE, NL2Repo, and RepoZero.
* Baselines/Comparisons: The authors compare the performance of the fine-tuned model to a range of baselines, including the teacher model and a range of smaller language models.
* Main Claimed Findings: The authors claim that the fine-tuned model achieves state-of-the-art performance on a range of software engineering benchmarks, with improvements of up to 49.51% on ProgramBench.

**What to Verify in the PDF**
==========================

* The authors claim that the fine-tuned model achieves state-of-the-art performance on a range of software engineering benchmarks, but the details of the evaluation protocol and the specific metrics used are not provided in the abstract.
* The authors also claim that the model is able to generalize to a range of tasks and datasets, but the results of the evaluation on these tasks are not provided in the abstract.
* The authors also mention that the model is able to improve over the base model across all seven unseen software engineering benchmarks, but the specific results of these evaluations are not provided in the abstract.
{% endraw %}
