---
layout: post
title: "Daily arXiv Digest — 2026-07-31 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) KAISEN: Reproducible Subgroup Fairness Auditing for Clinical Risk Models
- **Authors:** Sparsh Roy, Samuel Girmachew, Nishita Chavan
- **arXiv:** [2607.28608](https://arxiv.org/abs/2607.28608v1) · [pdf](https://arxiv.org/pdf/2607.28608v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.28608v1))
- **Categories:** cs.LG, q-bio.QM

### Abstract
> Clinical risk models routinely achieve strong aggregate performance while producing materially different error rates across patient subgroups. Audit pipelines have been proposed to catch this, but their components are rarely stress-tested, so it is unclear which parts of an audit can be trusted and under what conditions. We present KAISEN, a five-phase audit pipeline covering subgroup stratification, disparity measurement, mechanism diagnostics, post-hoc mitigation, and drift monitoring, evaluated to the point of failure on a synthetic benchmark of 16 disease tasks, 15 social-determinant axes from Healthy People 2030, and three prespecified intersections. Four findings follow. (i) Significance tracks each axis's gap against its own minimum detectable effect: rank correlation between significance count and raw equalized-odds difference (EOD) across the 15 axes is rho = 0.56, rising to rho = 0.78 once EOD is standardized by that floor. (ii) Per-group threshold optimization reduces EOD in 48 of 48 held-out runs (paired delta = -0.285, 95% CI [-0.313, -0.252]), while group-wise Platt scaling -- the better calibrator -- behaves as a coin flip on EOD (19 of 48 runs improved, 95% CI [0.26, 0.55]) with mean effect near zero, so what an audit should report is the variance, not the average. (iii) The mechanism diagnostic classifies 144 of 144 controlled cases correctly but recovers none of 48 model-driven cases under proxy misspecification, with no signal that it failed. (iv) CUSUM failures and false alarms track cohort realization far more than disease: at the reference threshold, all 27 false alarms and 7 of 8 missed shifts come from different seeds (chi-squared p = 0.002), so a threshold tuned on one cohort fails to transfer. All results are synthetic with known ground truth and do not establish clinical validity. Code, artifacts, and scripts reproducing every number are released.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: ρ = 0.56

* Equation: ρ = 0.56
* Symbols: ρ (rho) - correlation coefficient
* Why it matters: This equation represents the rank correlation between significance count and raw equalized-odds difference (EOD) across 15 single axes.

### Equation 2: ρ = 0.78

* Equation: ρ = 0.78
* Symbols: ρ (rho) - correlation coefficient
* Why it matters: This equation represents the standardizing EOD by its detectable floor, showing a stronger correlation between significance count and EOD.

### Equation 3: Δ = -0.285

* Equation: Δ = -0.285
* Symbols: Δ (delta) - change in EOD
* Why it matters: This equation represents the reduction in EOD in 48 of 48 held-out runs when per-group threshold optimization is used.

### Equation 4: [-0.313, -0.252]

* Equation: [-0.313, -0.252]
* Symbols: None
* Why it matters: This represents the 95% confidence interval for the change in EOD in 48 held-out runs when per-group threshold optimization is used.

### Equation 5: [0.26, 0.55]

* Equation: [0.26, 0.55]
* Symbols: None
* Why it matters: This represents the 95% confidence interval for the improvement in EOD when group-wise Platt scaling is used.

**Method Summary**
================

* The KAISEN audit pipeline consists of five phases: subgroup stratification, disparity measurement, mechanism diagnostics, post-hoc mitigation, and longitudinal drift monitoring.
* The authors use a synthetic benchmark of 16 disease tasks, 15 social-determinant axes, and three prespecified intersections to evaluate each phase.
* The method uses counterfactual fairness, debiasing methods, and post-hoc weighted calibration to address subgroup fairness.

**Experimental Overview**
=====================

* Tasks/Datasets: Synthetic SDOH benchmark of 16 disease tasks, 15 social-determinant axes, and three prespecified intersections.
* Baselines/Comparisons: The authors compare their results with group-wise Platt scaling and per-group threshold optimization.
* Main Claimed Findings:
	+ Per-group threshold optimization reduces EOD in 48 of 48 held-out runs.
	+ Group-wise Platt scaling is the better calibrator but behaves as a coin flip on EOD.
	+ The mechanism diagnostic classifies 144 of 144 controlled cases correctly but recovers none of 48 model-driven cases when its proxy columns are misspecified.

**What to Verify in the PDF**
==========================

* The structural causal model used to generate the synthetic SDOH benchmark.
* The results of the mechanism diagnostic on model-driven cases when its proxy columns are misspecified.
* The implications of the findings on subgroup fairness and clinical risk models.
{% endraw %}

{% raw %}
## 2) ReToken: One Token to Improve Vision-Language Models for Visual Retrieval
- **Authors:** Yao Xiao, Reuben Tan, Zhen Zhu, Yuqun Wu, Jianfeng Gao, Derek Hoiem
- **arXiv:** [2607.28627](https://arxiv.org/abs/2607.28627v1) · [pdf](https://arxiv.org/pdf/2607.28627v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.28627v1))
- **Categories:** cs.CV, cs.AI, cs.LG

### Abstract
> Long visual context poses a challenge for vision-language models: performance degrades as the number of distractors grows, and processing all tokens at once is computationally infeasible under GPU memory constraints. We present ReToken, a single learnable embedding trained as an explicit retrieval target that selects a sparse set of query-relevant visual tokens from a pre-filled visual KV cache. Trained on only a small image-QA dataset, ReToken yields consistent gains across image and video benchmarks: on Visual Haystacks it improves Qwen3VL-8B by 13.4 points and InternVL3.5 by 12.4 points (>20% relative), and on LVBench it transfers zero-shot to long video for an 8.0-point gain with Qwen3VL-8B. Thanks to its lightweight design, both training and long-video inference fit on a single H100. Code is available at: https://github.com/avaxiao/ReToken
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: {}_{\text{Test-MC}}
```latex
{}_{\text{Test-MC}}
```
Symbols: `{}` (set notation), `Test-MC` (test set, multiple choice)
Why it matters: This notation represents the test set for multiple-choice evaluation.

### Equation 2: \{L_{1},\dots,L_{N}\}
```latex
\{L_{1},\dots,L_{N}\}
```
Symbols: `{}` (set notation), `L_{i}` (transformer layer)
Why it matters: This notation represents a set of transformer layers used in the VLM.

### Equation 3: \mathbf{T}_{t}
```latex
\mathbf{T}_{t}
```
Symbols: `T` (token), `t` (time step)
Why it matters: This notation represents the token embedding at time step `t`.

### Equation 4: \mathbf{I}_{v}
```latex
\mathbf{I}_{v}
```
Symbols: `I` (image), `v` (visual tokens)
Why it matters: This notation represents the visual tokens.

### Equation 5: p(\mathbf{y}\mid\mathbf{I}_{v},\mathbf{T}_{t})
```latex
p(\mathbf{y}\mid\mathbf{I}_{v},\mathbf{T}_{t})
```
Symbols: `p` (probability), `y` (response), `I` (image), `T` (token), `t` (time step)
Why it matters: This notation represents the conditional probability of the response `y` given the image `I` and token `T` at time step `t`.

**Method Summary**
================

* ReToken uses a learnable token embedding to help compute more informative retrieval scores over relevant visual tokens.
* The VLM generates the response autoregressively based on the conditional probability of the response given the image and token.
* ReToken retrieves a subset of the most relevant frames, where each frame contributes a sparse set of query-relevant visual tokens.
* The method is lightweight and can be trained on a single GPU.

**Experimental Overview**
=====================

* Tasks/Datasets: Image question-answering (QA) and video benchmarks.
* Baselines/Comparisons: VLM, ReKV, uniform sampling.
* Main Claimed Findings: ReToken improves performance on image and video benchmarks, with gains of up to 20% relative.

**What to Verify in the PDF**
==========================

* The implementation details of ReToken, including the training procedure and inference settings.
* The ablation studies on design choices, including the influence of the inference setting and error analysis.
* The efficiency analysis of ReToken, including the computational and memory costs.
{% endraw %}

{% raw %}
## 3) AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis
- **Authors:** Bing Yan, Gregory Wolfe, Stefano Martiniani, Kyunghyun Cho
- **arXiv:** [2607.28618](https://arxiv.org/abs/2607.28618v1) · [pdf](https://arxiv.org/pdf/2607.28618v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.28618v1))
- **Categories:** cs.CL, cs.AI, cs.IR, cs.LG

### Abstract
> Chemistry literature synthesis often requires assembling specific findings scattered across many publications, yet existing literature-search systems primarily return ranked document lists. As a result, scientists and AI agents need to locate relevant information, verify their provenance, and assemble cross-paper answers manually. We present AskChem, a claim-centered infrastructure for cross-paper chemistry search. AskChem changes the unit of retrieval from the paper to the provenance-carrying claim: each paper is converted into atomic, typed claims, each grounded by a source DOI and a verbatim quote or an explicit evidence locator. Over this shared claim store, AskChem exposes complementary structures for search and synthesis: a stabilized faceted taxonomy for hierarchical retrieval and browsing, an evidence graph linking claims through relations, and an exploratory living taxonomy that situates indexed papers under scientific principles. AskChem currently indexes 2.4M claims from 147K papers and provides a web interface, as well as REST, SDK, and MCP access for AI agents. On AskChem-Bench, grounding a GPT-5.5 reader in AskChem yields 100% resolvable DOIs, compared with 88.3% without retrieval, and the highest citation density among five tested systems. AskChem is live at https://askchem.org.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: ≥ 2

* Equation: ≥ 2
* Symbols: ≥ (greater than or equal to), 2
* Why it matters: This equation is not explicitly used in the context, but it might be related to the claim extraction process or the evaluation metrics.

### Equation 2: ∼

* Equation: ∼
* Symbols: ∼ (not explicitly defined in the context)
* Why it matters: This equation is not explicitly used in the context, and its meaning is unclear.

### Equation 3: j_{\mathrm{CO}}=20

* Equation: j_{\mathrm{CO}}=20
* Symbols: j_{\mathrm{CO}} (not explicitly defined in the context), = (equals)
* Why it matters: This equation might be related to the evaluation of the system's performance on CO reduction tasks.

### Equation 4: κ=0.914

* Equation: κ=0.914
* Symbols: κ (not explicitly defined in the context), = (equals)
* Why it matters: This equation is used to describe the inter-rater agreement between the Gemini 3.1 Pro relevance judge and domain-expert labels, with a κ value of 0.914 indicating moderate agreement.

### Equation 5: ≥ 50

* Equation: ≥ 50
* Symbols: ≥ (greater than or equal to), 50
* Why it matters: This equation is not explicitly used in the context, but it might be related to the evaluation metrics or the system's performance.

**Method Summary**
================

* AskChem organizes claims along stabilized, corpus-induced facets such as reaction type, substance class, application, technique, mechanism topic, claim type, data, and time.
* The system links claims through typed relations such as supports, contradicts, extends, and derives_from.
* AskChem currently indexes 2.4M claims from 147K papers and provides a web interface, as well as REST, SDK, and MCP access for AI agents.

**Experimental Overview**
=========================

* Tasks/Datasets: AskChem-Bench v1.1 contains ten questions in each of three cross-paper tasks.
* Baselines/Comparisons: The system is judged against the claims it exposes, whereas paper-level systems are judged against cited titles and abstracts.
* Main Claimed Findings: AskChem rewrites each question into 3–4 keyword subqueries, fans them out to hybrid search, and diversifies the merged evidence to at most 40 claims before grounded synthesis. The system achieves 100% resolvable DOIs and the highest citation density among five tested systems.

**What to Verify in the PDF**
=============================

* The evaluation metrics and the specific details of the AskChem-Bench v1.1 dataset.
* The implementation of the faceted taxonomy and the evidence graph.
* The details of the grounding process for the extracted claims.
{% endraw %}

{% raw %}
## 4) MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers
- **Authors:** Md. Mehrab Hossain Opi, Robiul Islam Ryad, Md. Umar Faruk
- **arXiv:** [2607.28589](https://arxiv.org/abs/2607.28589v1) · [pdf](https://arxiv.org/pdf/2607.28589v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.28589v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform bit-widths across transformer components, overlooking their heterogeneous sensitivity to quantization and leading to inefficient precision allocation. In this paper, we propose {MixFrag, a fragility-guided mixed-precision PTQ framework for Vision Transformers. MixFrag first estimates component-level quantization fragility by measuring the Kullback--Leibler (KL) divergence between full-precision and isolated quantized output distributions using a small calibration set. It then formulates bit allocation as a Multiple-Choice Knapsack Problem (MCKP), enabling adaptive layer-wise precision assignment under a target bit budget. Extensive experiments on ImageNet-1K across multiple Vision Transformer architectures demonstrate that MixFrag achieves competitive classification performance under practical mixed-precision settings. Furthermore, evaluations on COCO object detection and instance segmentation show that MixFrag achieves state-of-the-art performance among existing mixed-precision PTQ methods, improving the previous best method by up to 9.6 AP under the challenging MP3/MP3 setting. Additional analyses validate the proposed fragility metric and demonstrate its strong correlation with the learned bit allocation. These results establish MixFrag as an effective framework for mixed-precision post-training quantization of Vision Transformers.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: \Omega_{c,b}

* Equation: \Omega_{c,b} = \sum_{i=1}^{B} \sum_{j=1}^{C} \mathbb{E}_{x \sim \mathcal{D}} \left[ \left| \frac{1}{b} \sum_{k=1}^{b} \mathbf{q}_k(x) - \mathbf{p}_j(x) \right| \right]
* Symbols: \Omega_{c,b}, \mathbb{E}, \mathcal{D}, \mathbf{q}_k(x), \mathbf{p}_j(x)
* Why it matters: This equation represents the expected performance degradation introduced by quantizing a single transformer component with a given bit-width.

### Equation 2: \Omega \in \mathbb{R}^{C \times B}

* Equation: \Omega = \left[ \Omega_{c,b} \right]_{C \times B}
* Symbols: \Omega, C, B
* Why it matters: This equation represents the component-bit fragility matrix, which captures the relative sensitivity of different transformer components to quantization.

### Equation 3: b_{c}^{*}

* Equation: b_{c}^{*} = \arg\max_{b \in \mathcal{B}} \left[ \sum_{i=1}^{B} \sum_{j=1}^{C} \mathbb{E}_{x \sim \mathcal{D}} \left[ \left| \frac{1}{b} \sum_{k=1}^{b} \mathbf{q}_k(x) - \mathbf{p}_j(x) \right| \right] \right]
* Symbols: b_{c}^{*}, \mathcal{B}, \mathbb{E}, \mathcal{D}, \mathbf{q}_k(x), \mathbf{p}_j(x)
* Why it matters: This equation represents the optimal bit-width for a given transformer component, which maximizes the expected performance degradation.

### Equation 4: \mathcal{C} = \{c_1, c_2, \ldots, c_C\}

* Equation: \mathcal{C} is the set of all transformer components.
* Symbols: \mathcal{C}, c_i
* Why it matters: This equation represents the set of all transformer components that can be quantized.

### Equation 5: \mathcal{B} = \{b_1, b_2, \ldots, b_B\}

* Equation: \mathcal{B} is the set of all possible bit-widths.
* Symbols: \mathcal{B}, b_i
* Why it matters: This equation represents the set of all possible bit-widths that can be used for quantization.

**Method Summary**
==================

* The proposed MixFrag framework estimates component-level quantization fragility by measuring the Kullback-Leibler (KL) divergence between full-precision and isolated quantized output distributions.
* The framework formulates bit allocation as a Multiple-Choice Knapsack Problem (MCKP), enabling adaptive layer-wise precision assignment under a target bit budget.
* The optimized bit allocation is supplied to the AdaLog backend to generate the final mixed-precision quantized models.

**Experimental Overview**
=========================

* Tasks: Image classification, object detection, and instance segmentation.
* Datasets: ImageNet-1K, COCO.
* Baselines: Random bit allocation, greedy bit allocation.
* Main claimed findings: MixFrag achieves competitive classification performance under practical mixed-precision settings, and achieves state-of-the-art performance on COCO object detection and instance segmentation.

**What to Verify in the PDF**
=============================

* The effectiveness of the proposed KL-based fragility metric in capturing the relative sensitivity of different transformer components to quantization.
* The performance of MixFrag on different Vision Transformer architectures and quantization configurations.
* The impact of the proposed MCKP-based bit allocation strategy on the overall performance of the mixed-precision quantized models.
{% endraw %}

{% raw %}
## 5) Oracle-Budgeted Molecular Optimization with Short-Term Graph Memory
- **Authors:** Jiannan Yang, Veronika Thost, Xiang Ling, Tengfei Ma
- **arXiv:** [2607.28437](https://arxiv.org/abs/2607.28437v1) · [pdf](https://arxiv.org/pdf/2607.28437v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.28437v1))
- **Categories:** cs.LG

### Abstract
> Molecular optimization is commonly performed under a limited oracle budget, which makes deciding what to evaluate as important as deciding what to generate. We introduce short-term graph memory, a plug-in module that preserves the generator architecture and native update rule while learning from previously evaluated molecules to prioritize subsequent oracle queries. The module maintains an online graph neural surrogate that pre-screens each round's candidate pool, so the fixed oracle budget is spent on molecules with higher predicted utility. Applied to a fragment-based generator on a standard molecular optimization benchmark, it improves the mean top-10 score at no extra oracle cost and never falls behind the base on any oracle; the gain extends to all four generators we tested at a tight budget of one thousand calls. We then analyze how surrogate-guided selection interacts with the exploration and exploitation behavior of different generators. Its benefit at larger budgets is consistent with two properties of the backbone: how broadly it searches, and how effectively its native search already exploits oracle feedback. We provide a simple way to spend a fixed oracle budget more selectively, and evidence on which generators benefit from it.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: (x,f(x))

* Equation: (x,f(x))
* Symbols: x (input molecule), f(x) (output score)
* Why it matters: This equation represents the evaluation of a molecule x using a scoring function f(x), which is a crucial step in the molecular optimization process.

### Equation 2: s_{\theta}

* Equation: s_{\theta}
* Symbols: s (utility score), \theta (model parameters)
* Why it matters: This equation represents the utility score s of a molecule, which is a measure of its quality or desirability. The model parameters \theta are used to compute this score.

### Equation 3: 0.648

* Equation: 0.648
* Symbols: None
* Why it matters: This equation is not explicitly defined in the context, but it may represent a threshold value or a constant used in the evaluation process.

### Equation 4: 0.784

* Equation: 0.784
* Symbols: None
* Why it matters: Similar to Equation 3, this equation is not explicitly defined in the context, but it may represent another threshold value or constant used in the evaluation process.

### Equation 5: 1{,}000

* Equation: 1{,}000
* Symbols: None
* Why it matters: This equation represents the total number of oracle calls, which is a fixed budget for the evaluation process.

**Method Summary**
==================

* The proposed method, Oracle-Budgeted Molecular Optimization with Short-Term Graph Memory, introduces a plug-in module that preserves the generator architecture and native update rule while learning from previously evaluated molecules to prioritize subsequent oracle queries.
* The module maintains an online graph neural surrogate that pre-screens each round's candidate pool, allowing the fixed oracle budget to be spent on molecules with higher predicted utility.
* The method is applied to four generators, including GenMol, InVirtuoGen, REINVENT, and Graph-GA, and shows improved performance on both top-10 score and top-10 AUC metrics.

**Experimental Overview**
==========================

* Tasks/Datasets: The proposed method is evaluated on the practical molecular optimization benchmark, which consists of a panel of property oracles that scores optimizers under an explicit query budget.
* Baselines/Comparisons: The method is compared to four generators, including GenMol, InVirtuoGen, REINVENT, and Graph-GA, on both tight and full oracle budgets.
* Main Claimed Findings: The proposed method improves performance on both top-10 score and top-10 AUC metrics, with the largest effect on GenMol, at no extra oracle cost.

**What to Verify in the PDF**
=============================

* The experimental results for the excluded oracle (valsartan SMARTS task) and the sensitivity analysis.
* The detailed per-backbone configurations and the full per-backbone configurations.
* The evaluation protocol and the evaluation metrics used in the experiment.
{% endraw %}
