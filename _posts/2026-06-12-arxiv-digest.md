---
layout: post
title: "Daily arXiv Digest — 2026-06-12 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Understanding Truncated Positional Encodings for Graph Neural Networks
- **Authors:** James Flora, Mitchell Black, Weng-Keen Wong, Amir Nayyeri
- **arXiv:** [2606.13671](https://arxiv.org/abs/2606.13671v1) · [pdf](https://arxiv.org/pdf/2606.13671v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.13671v1))
- **Categories:** cs.LG

### Abstract
> Positional encodings (PEs) enhance the power of graph neural networks (GNNs), both theoretically and empirically. Two of the most popular families of PEs - spectral (e.g., Laplacian eigenspaces, effective resistance) and walk-based (polynomials of the adjacency matrix) - are theoretically equivalent in expressive power, with expressivity between the 1-WL and 3-WL tests. However, this equivalence assumes the GNN uses the "complete" version of these PEs, which requires $O(n^3)$ time and space complexity. Instead, practitioners commonly use truncated variants of these encodings, such as the first $k$ eigenspaces or powers of the adjacency matrix. However, the theoretical properties of these truncated PEs are unknown. In this work, we initiate the study of these truncated PEs. Theoretically, we show that, under truncation, several families of PEs are fundamentally different in expressive power. As a corollary, we show that truncated spectral PEs are no longer stronger than the 1-WL test. We also study a family of spectral PEs, the $k$-harmonic distances, to highlight the differences in expressive power of even closely related truncated PEs. Finally, we experimentally show that a mix of truncated PEs is preferable to any single family on real-world datasets.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: O(n^3)
```markdown
O(n^{3})
```
* Symbols: `O`, `n`
* Why it matters: This equation represents the time and space complexity of the "complete" version of the spectral positional encoding, which requires O(n^3) operations.

### Equation 2: Ω(n)
```markdown
\Omega(n)
```
* Symbols: `Ω`, `n`
* Why it matters: This equation represents the lower bound on the expressivity of the truncated spectral positional encoding, which is Ω(n) in terms of the number of nodes in the graph.

### Equation 3: Θ(n)
```markdown
\Theta(n)
```
* Symbols: `Θ`, `n`
* Why it matters: This equation represents the upper bound on the expressivity of the truncated spectral positional encoding, which is Θ(n) in terms of the number of nodes in the graph.

### Equation 4: O(n)
```markdown
O(n)
```
* Symbols: `O`, `n`
* Why it matters: This equation represents the time and space complexity of the truncated spectral positional encoding, which is O(n) operations.

### Equation 5: Ω(n) - size spectral encodings
```markdown
\Omega(n)
```
* Symbols: `Ω`, `n`
* Why it matters: This equation represents the lower bound on the expressivity of Ω(n) - size spectral encodings, which is Ω(n) in terms of the number of nodes in the graph.

**Method Summary**
================

* The authors propose a study on truncated positional encodings for graph neural networks (GNNs).
* They compare fixed-size spectral and walk positional encodings both theoretically and empirically.
* The authors show that truncated spectral and walk encodings have very different expressive powers.
* They also show that Ω(n) - size spectral encodings can be less expressive than the 1-WL test.

**Experimental Overview**
=====================

* The authors test several different versions of truncated PEs, including concatenating them together.
* They conduct experiments specifically for the k-harmonics in order to explore their usefulness as a PE.
* The authors use the Graphormer-GD architecture as outlined in Section 3.
* The experiments are conducted on the BREC dataset, which includes several families of graphs ranging from 1-WL indistinguishable to 4-WL indistinguishable.

**What to Verify in the PDF**
==========================

* The authors' theoretical results, including the differences in expressive power between truncated spectral and walk PEs.
* The authors' experimental results, including the performance of different versions of truncated PEs on the BREC dataset.
* The authors' analysis of the limitations of the 1-WL test and the effectiveness of truncated PEs in capturing global structural information.
{% endraw %}

{% raw %}
## 2) Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation
- **Authors:** Guo Yu, Wenlin Liu, Yulan Hu, Hao-Xuan Ma, Jun-Peng Jiang, Han-Jia Ye
- **arXiv:** [2606.13657](https://arxiv.org/abs/2606.13657v1) · [pdf](https://arxiv.org/pdf/2606.13657v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.13657v1))
- **Categories:** cs.LG

### Abstract
> On-policy distillation (\textsc{OPD}) has recently become a prominent post-training recipe as it combines two desirable ingredients: on-policy student trajectories and dense teacher supervision, yet how this hybrid changes a model's parameters remains unclear. Across several language and vision-language model pairs and use cases, our analysis yields two main findings. On sparsity, \textsc{OPD}-style updates are small and coordinate-sparse. They are distributed across layers and are usually FFN-heavy. This sparse structure is operationally useful: training only the discovered subnetwork recovers nearly the same performance as full \textsc{OPD}. However, the sparsity-inducing SGD optimizer underperforms AdamW in our optimizer ablation, likely because dense teacher supervision preserves heterogeneous coordinate-wise gradient scales where AdamW's adaptive scaling remains useful. On geometry, the updates are numerically full-rank but spectrally concentrated; they lie mostly away from the principal singular subspaces of the source weights and fall disproportionately on coordinates where the source weights are close to zero. These findings suggest that dense teacher supervision does not turn \textsc{OPD} into ordinary dense parameter rewriting; instead, \textsc{OPD} retains important geometric signatures of on-policy post-training.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: π_{\theta}
π_{\theta} represents the trainable policy, which is a function that maps input x to output y.

### Equation 2: π_{T}
π_{T} represents the teacher policy, which is also a function that maps input x to output y.

### Equation 3: x \sim \mathcal{D}
x represents a random input from the data distribution \mathcal{D}.

### Equation 4: y = (y_{1},\ldots,y_{T}) \sim \pi_{\theta}(\cdot|x)
y represents a response to the input x, which is a sequence of T outputs generated by the trainable policy π_{\theta}.

### Equation 5: \mathcal{L}_{\mathrm{OPD}}(\theta) = \mathbb{E}_{x\sim\mathcal{D},\,y\sim\pi_{\theta}(\cdot|x)} \left[\sum_{t=1}^{T}D\!\left(\pi_{T}(\cdot|x,y_{<t})\,\|\,\pi_{\theta}(\cdot|x,y_{<t})\right)\right]
\mathcal{L}_{\mathrm{OPD}}(\theta) represents the loss function for on-policy distillation, which measures the difference between the teacher policy π_{T} and the trainable policy π_{\theta} at each time step t.

**Method Summary**
================

* The authors analyze the sparsity and geometry of on-policy distillation (OPD) updates.
* OPD-style updates are small and coordinate-sparse, with a sparse structure that is operationally useful.
* The updates are numerically full-rank but spectrally concentrated, with a low-rank structure that is not preserved by the optimizer.
* The authors examine the parameter updates between source and trained checkpoints across ten model pairs.

**Experimental Overview**
=====================

* The authors analyze OPD-style updates on several language and vision-language model pairs and use cases.
* The experiments include:
	+ Large-to-small distillation
	+ Capability consolidation
	+ Self-distillation from privileged information
* The authors compare OPD to conventional distillation-style contrast and to baselines such as DeepScaleR-1.5B and JustRL.
* The main claimed findings include:
	+ OPD-style updates are small and coordinate-sparse.
	+ OPD retains important geometric signatures of on-policy post-training.

**What to Verify in the PDF**
==========================

* The authors mention that the spectral and off-principal results relate to parameter-efficient adaptation and optimizer design.
* The authors also mention that recent work argues that spectral normalization can fail in VLA and RLVR post-training and proposes high-pass remedies.
* The authors provide additional static-analysis metrics in Tables 8, 9, and 10, which provide fuller static-analysis metrics for the OPD-style targets.
* The authors provide a benchmark-wise breakdown of interventional experiments in Section A.7, which supports the same conclusions as the averaged curves in Figure 3.
{% endraw %}

{% raw %}
## 3) Operadic consistency: a label-free signal for compositional reasoning failures in LLMs
- **Authors:** Nathaniel Bottman, Yinhong Liu, Kyle Richardson
- **arXiv:** [2606.13649](https://arxiv.org/abs/2606.13649v1) · [pdf](https://arxiv.org/pdf/2606.13649v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.13649v1))
- **Categories:** cs.CL, cs.LG

### Abstract
> Detecting LLM reasoning failures at inference time without ground-truth labels has motivated a wide range of confidence baselines, including self-consistency, semantic entropy, and P(True), built on within-question sampling and self-evaluation. Operad theory, the formalism for systems built by iterated substitution, suggests a complementary diagnostic: a model's direct answer to a compositional query should agree with the answer it produces by composing a stated decomposition of the same query. We instantiate this idea as operadic consistency (OC), a per-question signal. Across twelve instruction-tuned LLMs (4B to 671B parameters, open-weights and closed-source) on four multi-hop QA datasets, OC is strongly correlated with accuracy on every dataset (Pearson $r \in [0.86, 0.94]$, all $p \leq 0.0004$), and is the only signal we evaluate with $r \geq 0.85$ uniformly across all four datasets. Chain-of-thought self-consistency (CoT-SC; Wang et al., 2023) matches OC on HotpotQA and DROP ($r = 0.93, 0.87$) but drops to $r \approx 0.45$ on MuSiQue and StrategyQA. At the per-question level, OC contributes information beyond CoT-SC and semantic entropy on every dataset (cluster-robust $p \leq 10^{-16}$ for the OC coefficient), and the conclusion is robust to additionally controlling for constructed decomposition-aware baselines ($p \leq 10^{-13}$). The same signal yields selective-prediction improvements (accuracy at fixed coverage) over a tuned CoT-SC baseline at the equal-cost $K = 3$ budget (AUARC lifts of +0.086 to +0.096 and AUROC lifts of +0.092 to +0.164; 95% CIs exclude zero on every cell). On five frontier thinking models, where the decomposition is extracted from the model's own chain of thought, the same equal-cost comparison gives positive selective-prediction point-estimate lift on all 16 (dataset, budget, metric) cells tested, with 95% CIs excluding zero on 12 of the 16.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: r ∈ [0.86, 0.94]

* Equation: r ∈ [0.86, 0.94]
* Symbols: r (Pearson correlation coefficient)
* Why it matters: This equation represents the range of Pearson correlation coefficients obtained for operadic consistency (OC) across the four multi-hop QA datasets.

### Equation 2: p ≤ 0.0004

* Equation: p ≤ 0.0004
* Symbols: p (p-value)
* Why it matters: This equation represents the p-value threshold for statistical significance, indicating that the observed correlation between OC and accuracy is statistically significant.

### Equation 3: r ≥ 0.85

* Equation: r ≥ 0.85
* Symbols: r (Pearson correlation coefficient)
* Why it matters: This equation represents the minimum Pearson correlation coefficient required for a signal to be considered a strong indicator of accuracy.

### Equation 4: r = 0.93, 0.87

* Equation: r = 0.93, 0.87
* Symbols: r (Pearson correlation coefficient)
* Why it matters: These values represent the Pearson correlation coefficients obtained for OC on HotpotQA and DROP, respectively.

### Equation 5: r ≈ 0.45

* Equation: r ≈ 0.45
* Symbols: r (Pearson correlation coefficient)
* Why it matters: This value represents the Pearson correlation coefficient obtained for OC on MuSiQue, indicating a weaker correlation with accuracy.

**Method Summary**
==================

* Operadic consistency (OC) is a label-free signal for compositional reasoning failures in LLMs.
* OC is calculated as the semantic-agreement score between the model's greedy direct answer and its greedy decomposed answer.
* Statistical methodology involves logistic regression with cluster-robust standard errors and McFadden's pseudo-R^2.
* Baselines include self-consistency (CoT-SC), semantic entropy, and P(True).

**Experimental Overview**
========================

* Tasks: Multi-hop QA datasets (HotpotQA, MuSiQue, StrategyQA, DROP)
* Baselines: CoT-SC, semantic entropy, P(True), and constructed decomposition-aware baselines
* Main claimed findings: OC is strongly correlated with accuracy across all datasets, and is the only signal with r ≥ 0.85 uniformly across all four datasets.

**What to Verify in the PDF**
=============================

* The decomposition process used for each dataset (e.g., Break QDMR annotations for HotpotQA and DROP, native decompositions for MuSiQue and StrategyQA).
* The experimental protocol for evaluating thinking models (e.g., 100 questions per cell, removal of extractor-flagged unfactorable traces).
* The results for the equal-cost comparison between OC and CoT-SC, including the selective-prediction point-estimate lift and 95% CIs.
{% endraw %}

{% raw %}
## 4) SkMTEB: Slovak Massive Text Embedding Benchmark and Model Adaptation
- **Authors:** Marek Šuppa, Andrej Ridzik, Daniel Hládek, Natália Kňažeková, Viktória Ondrejová
- **arXiv:** [2606.13647](https://arxiv.org/abs/2606.13647v1) · [pdf](https://arxiv.org/pdf/2606.13647v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.13647v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> We introduce SkMTEB, the first comprehensive MTEB-style text embedding benchmark for Slovak, a low-resource West Slavic language, comprising 31 datasets across 7 task types -- nearly 4$\times$ the depth of existing multilingual benchmark coverage for Slovak. Our evaluation of 31 embedding models reveals that large instruction-tuned multilingual models achieve the strongest performance, while existing Slovak-specific models trained for NLU tasks transfer poorly to embedding tasks. To address the need for efficient, locally-deployable Slovak embeddings, we develop \texttt{e5-sk-small} (45M parameters) and \texttt{e5-sk-large} (365M) by applying vocabulary trimming and fine-tuning to Multilingual E5 models. Despite size reductions of up to 62\%, our open-source models achieve competitive performance with proprietary APIs while remaining locally deployable for semantic search and retrieval-augmented generation (RAG). We release the benchmark, models, datasets, and code openly, hoping our approach offers a replicable path for other under-resourced languages.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: {}^{\alpha,~\beta}

* Equation: {}^{\alpha,~\beta}
* Symbols: \alpha, \beta
* Why it matters: Not found in extracted context.

### Equation 2: {}^{\alpha,~\delta}

* Equation: {}^{\alpha,~\delta}
* Symbols: \alpha, \delta
* Why it matters: Not found in extracted context.

### Equation 3: \times

* Equation: \times
* Symbols: None
* Why it matters: Not found in extracted context.

### Equation 4: \bigstar

* Equation: \bigstar
* Symbols: None
* Why it matters: Not found in extracted context.

### Equation 5: nDCG@k (primarily nDCG@10)

* Equation: nDCG@k (primarily nDCG@10)
* Symbols: nDCG@k, Wang et al. (2013)
* Why it matters: This is a standard metric used to evaluate the retrieval of documents in the SkMTEB benchmark.

**Method Summary**
================

* The authors introduce SkMTEB, a comprehensive text embedding benchmark for Slovak, covering 31 datasets across 7 task types.
* The benchmark is designed to evaluate the performance of text embedding models in various tasks, including retrieval, classification, and clustering.
* The authors develop two models, e5-sk-small and e5-sk-large, by applying vocabulary trimming and fine-tuning to Multilingual E5 models.
* The models achieve competitive performance with proprietary APIs while remaining locally deployable for semantic search and retrieval-augmented generation (RAG).

**Experimental Overview**
=====================

* Tasks/Datasets: SkMTEB comprises 31 datasets across 7 task types, including retrieval, classification, and clustering.
* Baselines/Comparisons: The authors evaluate the performance of various models, including multilingual-e5-large-instruct, gemini-embedding-001, and smaller alternatives.
* Main Claimed Findings: Large instruction-tuned multilingual models achieve the strongest performance, while existing Slovak-specific models transfer poorly to embedding tasks.

**What to Verify in the PDF**
==========================

* The curation details for newly created datasets in Appendices B and C.
* The full task and dataset metadata provided in Appendix E.
* The results of the ablation study, including the contributions of vocabulary trimming, fine-tuning, and inference prompts to the final models.
{% endraw %}

{% raw %}
## 5) The Stable Recovery Manifold: Geometric Principles Governing Recoverability in Continual Learning
- **Authors:** Ayushman Trivedi, Bhavika Melwani
- **arXiv:** [2606.13637](https://arxiv.org/abs/2606.13637v1) · [pdf](https://arxiv.org/pdf/2606.13637v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG

### Abstract
> Catastrophic forgetting is often viewed as the destruction of previously learned knowledge during sequential learning. Building on the Accessibility Collapse framework, we investigate the geometric structure of recoverability in continual learning. Using Split CIFAR-100 and a sequentially trained ResNet-18, we analyze recoverability, representational drift, and recovery complexity across ten tasks. We introduce Recovery Subspace Dimensionality (k_t), a measure of the minimum number of singular directions required to preserve 90 percent of full probe performance. Contrary to our Recoverability Diffusion hypothesis, recovery dimensionality remains stable throughout training (mean k_t = 8.0) despite substantial representational drift. Principal-angle drift strongly predicts recoverability (r = -0.862), and a simple geometric model explains 82.2 percent of recoverability variance. These findings support the Stable Recovery Manifold hypothesis, suggesting that forgotten knowledge remains compactly decodable despite representational reorganization. The results indicate that catastrophic forgetting is primarily an accessibility and manifold-alignment problem rather than information destruction.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
#### 1. Recovery Subspace Dimensionality (k_t)
- Equation: Not explicitly provided in the context.
- Symbols: Not found in extracted context.
- Why it matters: k_t is a measure of the minimum number of singular directions required to preserve 90 percent of full probe performance.

#### 2. Principal-angle drift
- Equation: Not explicitly provided in the context.
- Symbols: Not found in extracted context.
- Why it matters: Principal-angle drift strongly predicts recoverability (r = -0.862).

#### 3. Recoverability Diffusion hypothesis
- Equation: Not explicitly provided in the context.
- Symbols: Not found in extracted context.
- Why it matters: Contrary to the Recoverability Diffusion hypothesis, recovery dimensionality remains stable throughout training.

#### 4. Recoverability variance
- Equation: Not explicitly provided in the context.
- Symbols: Not found in extracted context.
- Why it matters: A simple geometric model explains 82.2 percent of recoverability variance.

#### 5. Principal-angle drift formula
- Equation: Not found in extracted context.
- Symbols: Not found in extracted context.
- Why it matters: Not explicitly mentioned in the context.

### Method Summary
* The authors use a sequentially trained ResNet-18 on Split CIFAR-100.
* They analyze recoverability, representational drift, and recovery complexity across ten tasks.
* The authors introduce Recovery Subspace Dimensionality (k_t) as a measure of the minimum number of singular directions required to preserve 90 percent of full probe performance.

### Experimental Overview
* Tasks/Datasets: Split CIFAR-100
* Baselines/Comparisons: Not mentioned in the context.
* Main claimed findings: 
  * Recovery dimensionality remains stable throughout training despite substantial representational drift.
  * Principal-angle drift strongly predicts recoverability.
  * A simple geometric model explains 82.2 percent of recoverability variance.

### What to Verify in the PDF
* The Recoverability Diffusion hypothesis and its implications.
* The mathematical formulation of Recovery Subspace Dimensionality (k_t) and its calculation.
* The details of the simple geometric model that explains recoverability variance.
{% endraw %}
