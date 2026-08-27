---
layout: post
title: "Daily arXiv Digest — 2026-08-27 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Finding and using interpretable latents in a neutrino foundation model with sparse autoencoders
- **Authors:** Raphaël Bonnet-Guerrini, Johann Ioannou-Nikolaides, Inar Timiryasov, Vincenzo Piuri
- **arXiv:** [2608.26090](https://arxiv.org/abs/2608.26090v1) · [pdf](https://arxiv.org/pdf/2608.26090v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.26090v1))
- **Categories:** astro-ph.HE, cs.AI, cs.LG, hep-ex

### Abstract
> We present a first application of sparse-autoencoder-based mechanistic interpretability to particle physics. Studying a neutrino foundation model pretrained on IceCube data and fine-tuned for direction reconstruction, we identify a validated atlas of physical concepts in the model representation, using a strict validation protocol consisting of held-out tests, matched nuisance controls, and replication across independent dictionary trainings. Causal interventions show that the direction head barely draws on this atlas. Motivated by this underused information, we train an uncertainty head on the same event-level representation to predict the model's angular reconstruction error. Unlike the direction head, it depends causally on quality and brightness features from the atlas. At $20\%$ selection efficiency, this interpretable estimator improves the median angular resolution from $20.2^\circ$ to $3.2^\circ$. These results suggest that mechanistic interpretability can reveal learned latent physics encoded within a model's internal representation and help design downstream tasks that exploit it.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 20%
#### Equation
20%
#### Symbols
- None
#### Why it matters
This equation is likely a percentage value representing the selection efficiency of the model. It is mentioned in the context of training an uncertainty head on the same event-level representation to predict the model's angular reconstruction error.

### Equation 2: 20.2°
#### Equation
20.2°
#### Symbols
- None
#### Why it matters
This equation represents the median angular resolution before the improvement. It is compared to the final result of 3.2°, indicating the improvement achieved by the interpretable estimator.

### Equation 3: 3.2°
#### Equation
3.2°
#### Symbols
- None
#### Why it matters
This equation represents the median angular resolution after the improvement. It shows the significant reduction in angular resolution achieved by the interpretable estimator.

### Equation 4: 1μs
#### Equation
1μs
#### Symbols
- None
#### Why it matters
This equation is not explicitly mentioned in the context, but it might be related to the time resolution of the model. It is possible that this value is used in the validation protocol or as a baseline.

### Equation 5: L=127
#### Equation
L=127
#### Symbols
- L ( likely representing a dimension or length)
- 127
#### Why it matters
This equation is not explicitly explained in the context, but it might be related to the architecture of the model or the number of layers in the transformer. It is possible that this value is used to define the number of blocks in the transformer.

**Method Summary**
================

* The main reconstruction loss is the mean squared error in normalized activation space.
* To avoid dead latents, an AuxK revival loss is added to the training objective.
* The sparse dictionaries are trained on the frozen PolarBERT representation.
* The validation protocol separates readable features, validated physical read-outs, and causal features.

**Experimental Overview**
========================

* Tasks/Datasets: Neutrino direction reconstruction using IceCube data.
* Baselines/Comparisons: The authors compare their results to the original PolarBERT model and other baselines.
* Main Claimed Findings: The interpretable estimator improves the median angular resolution from 20.2° to 3.2° at 20% selection efficiency.

**What to Verify in the PDF**
=============================

* The details of the AuxK revival loss and its implementation.
* The validation protocol used to separate readable features, validated physical read-outs, and causal features.
* The results of the additional atlas results reported in Appendix B, including the leading clean-trigger coordinates and the auxiliary contrast.
{% endraw %}

{% raw %}
## 2) Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent Data Selection and Foundation Model Embeddings
- **Authors:** Evelyn Ma, Rama Kumar Pasumarthi, Kishwar Shafin, Mandar Sharma, Mimi Sun, Hamed Sadeghi, Dav M. Ebengo, Mbulayi Onesime, Rouslan Solomakhin, John Wamburu, William Ogallo, Aisha Walcott-Bryant, Sanxing Chen, Arbaaz Muslim, Yael Mayer, Ronald Ho, Roy Lee, Ruth Alcantara, Abdoulaye Diack, Monica Bharel, Lambert Rosique, Jeremy Amez-Droz, Christopher Haire, James Manyika, Yossi Matias, Niv Efron, Gautam Prasad, Shravya Shetty
- **arXiv:** [2608.26088](https://arxiv.org/abs/2608.26088v1) · [pdf](https://arxiv.org/pdf/2608.26088v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.26088v1))
- **Categories:** cs.AI, cs.LG

### Abstract
> Addressing critical global challenges, from food security and disaster risk to disease outbreaks and socio-economic vulnerability, demands high-fidelity geospatial modeling. However, building predictive planetary models remains bottlenecked by a fragmented data ecosystem, requiring manual data retrieval, multimodal data curation and fusion along with iterative model selection. We present the Planetary Prediction Engine (PPE), an autonomous AI system that executes this end-to-end workflow directly from natural-language queries. PPE synthesizes multimodal datasets on the fly, retrieving spatiotemporally relevant covariates across open-web and Earth observation platforms (Data Commons, Google Earth Engine) and fusing them with geospatial foundation model embeddings (PDFM, AlphaEarth). Simultaneously, it searches over task-tailored model architecture families with automated overfitting guards. Across diverse tasks, geographies, and scientific domains, PPE consistently outperforms state-of-the-art or manually tuned expert baselines. For US spatial regression, PPE improves mean $R^2$ across 21 CDC health indicators (76.8% vs. 60.0%), FEMA national risk indices (64.9% vs. 60.0%), and the Social Vulnerability Index (66.2% vs. 58.6%). For spatial downscaling in data-scarce settings, PPE integrates localized proxies to double baseline accuracy in Nigerian food security indicators ($R^2$ of 66.1% vs. 31.5%). For epidemiological nowcasting of the 2026 DRC Bundibugyo Ebola outbreak, PPE achieves a Recall@10 of 83.3% (identifying 15 of 18 newly invaded health zones across five weekly forecasts), a +10.3 percentage-point improvement over the public state-of-the-art modeling (~73%). By combining autonomous multimodal planetary data discovery with targeted model optimization, PPE lowers the technical barrier to planetary-scale analytics, enabling rapid, customized, expert-level deployment.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: R^2

* Equation: `R^2 = 1 - (1 / (n - 1)) * Σ (y_i - ŷ_i)^2`
* Symbols:
	+ `R^2`: Coefficient of Determination
	+ `n`: Number of data points
	+ `y_i`: Actual value
	+ `ŷ_i`: Predicted value
* Why it matters: `R^2` measures the proportion of the variance in the dependent variable that is predictable from the independent variable(s). A higher value indicates a better fit of the model to the data.

### Equation 2: ~

* Equation: `~ = 10.3`
* Symbols: None
* Why it matters: This equation is used to represent a specific value, but its meaning is not explicitly explained in the context. It appears to be a percentage point improvement over a baseline model.

### Equation 3: ×

* Equation: `X_i = [X_i^cov, X_i^emb]`
* Symbols:
	+ `X_i`: Feature vector for location `i`
	+ `X_i^cov`: Covariates for location `i`
	+ `X_i^emb`: Location-based embedding signals for location `i`
* Why it matters: This equation represents the construction of a feature vector `X_i` by combining covariates `X_i^cov` and location-based embedding signals `X_i^emb`.

**Method Summary**
================

* The Planetary Prediction Engine (PPE) is an autonomous AI system that executes an end-to-end workflow directly from natural-language queries.
* PPE synthesizes multimodal datasets on the fly, retrieving spatiotemporally relevant covariates across open-web and Earth observation platforms.
* The system fuses geospatial foundation model embeddings with automatically selected geospatial covariates to construct a feature vector.
* PPE searches over task-tailored model architecture families with automated overfitting guards.

**Experimental Overview**
=====================

* Tasks/Datasets:
	+ Mechanistic Nowcasting: Simulates the spatiotemporal trajectory of the May–July 2026 DRC Ebola Outbreak across all 519 health zones in DRC.
	+ Super-Resolution Downscaling: Integrates localized proxies to double baseline accuracy in Nigerian food security indicators.
	+ Spatial Regression: Evaluates the system's performance on US spatial regression tasks, including CDC health indicators and FEMA national risk indices.
* Baselines/Comparisons:
	+ State-of-the-art or manually tuned expert baselines.
* Main Claimed Findings:
	+ PPE consistently outperforms state-of-the-art or manually tuned expert baselines across diverse tasks, geographies, and scientific domains.

**What to Verify in the PDF**
==========================

* Detailed benchmark specifications for the Nowcasting paradigm, including technical specifications, spatial granularities, and evaluation partitions.
* Full ablation results for the system's performance across different tasks and datasets.
* Explanation of the five-dimension scoring rubric utilized by the Intelligent Data Selection stage.
{% endraw %}

{% raw %}
## 3) TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development
- **Authors:** Jiarui Yan, Weiwei Sun, Sijie Li, Wenhan Li, Yiming Yang
- **arXiv:** [2608.26086](https://arxiv.org/abs/2608.26086v1) · [pdf](https://arxiv.org/pdf/2608.26086v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.26086v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Large language models write correct code for isolated problems but remain far weaker at autonomous machine-learning development, where an agent must revise data pipelines, models, and validation over hours of feedback, and on most competitions still finishes below strong human competitors. Outcome-based benchmarks record this gap but not its cause, because they grade the final submission and discard the development process behind it. We introduce TraceML, which pairs human and agent work on the same competitions under one version-level schema: 4,465 human Kaggle trajectories across 134 competitions, seven of which are also worked by two agent scaffolds, giving 430 paired human and 207 agent trajectories. Every code version carries its score, its timestamp, and labels for the action taken, its intent, the edit size, and the score effect. Read this way, the gap becomes concrete. Experts alternate data work, validation, model changes, and ensembling, and return to approaches they had set aside. Each agent scaffold instead collapses into a narrow loop: Codex spends its steps re-weighting ensembles and tuning submissions, MLEvolve mutates its model in place, and neither pivots at the human rate nor reopens abandoned work. A short planning prompt distilled from human practice moves the behaviors it names toward the human profile and lifts scores, but the effort profile stays agent-shaped: instruction closes only the part of the gap that reduces to instructions. We release the corpus, the schema, the labelers, and the extraction pipeline at https://huggingface.co/datasets/jerryyan/TraceML.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\log_{2}$
* Equation: $\log_{2}$
* Symbols: $\log_{2}$ (base-2 logarithm)
* Why it matters: This equation is used to describe the gap between human and agent performance in machine learning development.

### Equation 2: $0.09$
* Equation: $0.09$
* Symbols: None
* Why it matters: This value represents the percentage of human returns that end above the version they went back to.

### Equation 3: $0.12$
* Equation: $0.12$
* Symbols: None
* Why it matters: This value represents the percentage of human returns that end above the version they went back to.

### Equation 4: $25\%$
* Equation: $25\%$
* Symbols: None
* Why it matters: This value represents the percentage of human returns that end above the version they went back to.

### Equation 5: $58\%$
* Equation: $58\%$
* Symbols: None
* Why it matters: This value represents the percentage of human returns that end above the version they went back to.

**Method Summary**
================

* The authors introduce TraceML, a framework for analyzing human-agent planning in machine learning development.
* The framework pairs human and agent work on the same competitions under one version-level schema.
* The authors use a paired subset of 430 human and 207 agent trajectories to analyze the gap between human and agent performance.
* The authors find that humans return to earlier work, while agents effectively never do.
* The authors conclude that what the agents lack is memory, not recovery.

**Experimental Overview**
=====================

* Tasks/Datasets: The authors use a paired subset of 430 human and 207 agent trajectories on 7 Kaggle competitions.
* Baselines/Comparisons: The authors compare the performance of Codex and MLEvolve agents to human performance on the same competitions.
* Main Claimed Findings: The authors find that humans return to earlier work, while agents effectively never do, and that what the agents lack is memory, not recovery.

**What to Verify in the PDF**
==========================

* The authors mention that the harness experiment adds the intervention and ablation arms on the same 7 competitions, but it is unclear what these arms represent.
* The authors also mention that the study covers all 7 paired competitions at the same 12-hour budget, but it is unclear how the budget is allocated between the human and agent runs.
* The authors mention that the study uses a repeated same-condition runs to bound the noise at roughly 0.01 in each competition's metric, but it is unclear how this is done.
{% endraw %}

{% raw %}
## 4) ICON Decomposition: Multivariate Concept-Level Explanations of Deep Representations for Model Auditing
- **Authors:** Roshan Prakash Rane, Marco Simnacher, Manuel Pfeuffer, Marc-Andre Schulz, Nys Tjade Siegel, Maximilian Dreyer, Frederik Pahde, Wojciech Samek, Sonja Greven, Kerstin Ritter
- **arXiv:** [2608.26083](https://arxiv.org/abs/2608.26083v1) · [pdf](https://arxiv.org/pdf/2608.26083v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.26083v1))
- **Categories:** cs.LG, cs.AI, cs.CV, stat.ML

### Abstract
> Deep neural networks often exploit spurious associations in their training data, a failure known as shortcut learning. Concept-based explainability methods screen for shortcuts by testing whether concepts such as a patient's sex or scanner settings can be decoded from a network layer. Because each concept is evaluated in isolation, these methods can mistake correlations between concepts as evidence that the model uses them. We introduce ICON decomposition, which instead quantifies how much of a layer's variance each concept explains after accounting for all other concepts and the outcome. On synthetic data with known ground truth, ICON recovers concept importance more accurately than seven alternative baseline methods. On skin-lesion and brain-imaging models, it isolates the concepts on which a model genuinely relies, quantifies the representation unexplained by any of the supplied concepts, and yields sparse explanations that we validate by retraining and out-of-distribution testing.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: κ
κ = ∑[i=1 to q] (|c_i| / (1 + |c_i|)) \* (|H_l| / (1 + |H_l|))

* Equation: A weighted sum of normalized concept importance and representation importance.
* Symbols:
	+ κ: concept importance score
	+ c_i: concept i
	+ H_l: representation importance at layer l
	+ q: number of concepts
* Why it matters: This equation represents the concept importance score, which is a key component of ICON decomposition.

### Equation 2: R^2
R^2 = 1 - (|H_l| / (1 + |H_l|))^2 \* (|c_i| / (1 + |c_i|))

* Equation: A measure of the proportion of variance in the representation explained by a concept.
* Symbols:
	+ R^2: representation variance explained by concept i
	+ H_l: representation importance at layer l
	+ c_i: concept i
	+ q: number of concepts
* Why it matters: This equation provides a quantitative measure of the contribution of each concept to the representation.

### Equation 3: 64 × 64
64 × 64 = 4096

* Equation: A constant representing the size of the input images.
* Symbols:
	+ 64: width of the input images
	+ 64: height of the input images
* Why it matters: This equation is used to specify the dimensions of the input images in the ToyBrains dataset.

### Equation 4: \mathbf{l}_k
\mathbf{l}_k = \frac{1}{q} \sum_{i=1}^q |c_i| \* |H_l|

* Equation: A weighted sum of concept importance and representation importance.
* Symbols:
	+ \mathbf{l}_k: concept importance at layer l
	+ c_i: concept i
	+ H_l: representation importance at layer l
	+ q: number of concepts
* Why it matters: This equation represents the concept importance at each layer, which is used to compute the concept importance score.

### Equation 5: \mathbf{l}_d
\mathbf{l}_d = \frac{1}{q} \sum_{i=1}^q |c_i| \* |H_l| \* (1 - \beta_i)

* Equation: A weighted sum of concept importance, representation importance, and a correction term.
* Symbols:
	+ \mathbf{l}_d: concept importance at layer l, corrected
	+ c_i: concept i
	+ H_l: representation importance at layer l
	+ q: number of concepts
	+ \beta_i: correction term for concept i
* Why it matters: This equation represents the corrected concept importance at each layer, which is used to compute the concept importance score.

**Method Summary**
================

* ICON decomposition is a method for multivariate concept-level explanations of deep representations.
* It provides a more accurate and nuanced understanding of concept importance than existing methods.
* ICON decomposition is based on the concept importance score, which is computed using a weighted sum of concept importance and representation importance.
* The method is evaluated on synthetic data and skin cancer detection datasets.

**Experimental Overview**
=====================

* Tasks:
	+ Skin cancer detection using the ISIC 2019 Challenge dataset.
	+ Evaluation of ICON decomposition on synthetic data.
* Datasets:
	+ ISIC 2019 Challenge dataset.
	+ ToyBrains dataset.
* Baselines/comparisons:
	+ Seven baseline methods, including linear probes, CAV-classic, and CAV-signal.
	+ Four classical variable-importance estimators.
* Main claimed findings:
	+ ICON decomposition provides more accurate and nuanced concept importance scores than existing methods.
	+ ICON decomposition is effective in isolating the concepts on which a model genuinely relies.

**What to Verify in the PDF**
==========================

* The mathematical derivations of the concept importance score and corrected concept importance.
* The evaluation of ICON decomposition on the skin cancer detection dataset, including the accuracy of the model and the quality of the explanations.
* The comparison of ICON decomposition with other methods, including the baseline methods and classical variable-importance estimators.
* The results of the out-of-distribution testing, which is used to validate the performance of ICON decomposition.
{% endraw %}

{% raw %}
## 5) Prefix Sliding for efficient test-time scaling
- **Authors:** Niklas Muennighoff, Zhengyang Wang, Zeyi Chen, Weijia Shi, Binyuan Hui, John Yang, Dapeng Jiang, Mika Senghaas, Fares Obeid, Johannes Hagemann, Sami Jaghouar, Ludwig Schmidt, Percy Liang, Jason Wei, Andrew Y. Ng, Luke Zettlemoyer, Yejin Choi, Mike Lewis
- **arXiv:** [2608.26070](https://arxiv.org/abs/2608.26070v1) · [pdf](https://arxiv.org/pdf/2608.26070v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.26070v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> Test-time scaling uses extra test-time compute to improve performance, such as letting language models reason longer when solving a problem. As models keep the entire reasoning trace in memory via full attention, hard tasks that need long thinking can be prohibitively expensive. However, we find most intermediate reasoning tokens lose importance as the model continues reasoning. This calls into question whether retaining them is worth the cost. Based on this insight, we propose Prefix Sliding, which discards tokens during reasoning that are not part of the prefix or the window of the last few thousand tokens. The prefix has key instructions and tools available to the model, while the most recent tokens are the current reasoning the model is working on. This caps the total memory requirement regardless of how long the model reasons, allowing for efficient long-horizon test-time scaling. Without training, Prefix Sliding can make existing models 3x faster while maintaining performance. Training with Prefix Sliding using reinforcement learning can achieve better performance by enabling scaling to reasoning traces beyond a hundred thousand tokens. Ablations show Prefix Sliding outperforms summarizing intermediate tokens or vanilla sliding window. Our code is at https://github.com/Muennighoff/prefix-sliding
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Not found in extracted context.

### Equation 2: Not found in extracted context.

### Equation 3: Not found in extracted context.

### Equation 4: Not found in extracted context.

### Equation 5: Not found in extracted context.

**Method Summary**
==================

* Prefix Sliding is a method that discards tokens during reasoning that are not part of the prefix or the window of the last few thousand tokens.
* The prefix has key instructions and tools available to the model, while the most recent tokens are the current reasoning the model is working on.
* Prefix Sliding can make existing models 3x faster while maintaining performance without training.
* Training with Prefix Sliding using reinforcement learning can achieve better performance by enabling scaling to reasoning traces beyond a hundred thousand tokens.

**Experimental Overview**
========================

* Tasks/Datasets: The authors experiment with the Qwen3-1.7B model on standard reasoning benchmarks such as GPQA, MATH500, and AIME25.
* Baselines/Comparisons: The authors compare Prefix Sliding with three key alternatives: summarizing intermediate tokens, vanilla sliding window, and explanation text generation.
* Main Claimed Findings: Prefix Sliding is more efficient than the baselines and achieves better performance when trained with reinforcement learning.

**What to Verify in the PDF**
=============================

* The authors claim that Prefix Sliding can make existing models 3x faster while maintaining performance without training. Verify this claim by checking the results in Figure 1.
* The authors also claim that training with Prefix Sliding using reinforcement learning can achieve better performance by enabling scaling to reasoning traces beyond a hundred thousand tokens. Verify this claim by checking the results in Figure 8.
* The authors mention that the optimal value of `last k` likely depends on the context window and the number of allowed passes. Verify this claim by checking the results in Table 2 and Figure 9.
{% endraw %}
