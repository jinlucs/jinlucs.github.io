---
layout: post
title: "Daily arXiv Digest — 2026-08-06 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Predicting Brain Morphometry with MT-GNN: Mesh Evolution in Continuous Time with Graph-Based Metric Tensor Embeddings
- **Authors:** Hao Ding, Daniel Semchin, Paul M. Thompson, Boris Gutman
- **arXiv:** [2608.05132](https://arxiv.org/abs/2608.05132v1) · [pdf](https://arxiv.org/pdf/2608.05132v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.05132v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> Predicting how a subcortical structure's shape will evolve from a few prior scans could support prognosis and clinical-trial enrichment. Existing longitudinal mesh predictors either extrapolate shape trajectories via high-dimensional embeddings or regress vertex deformations directly. We instead predict the surface's intrinsic geometry in continuous time: a single per-structure graph network predicts the future per-vertex first fundamental form (metric tensor) for an arbitrary causal multiple-visit history and an arbitrary prediction horizon, conditioned on a Fourier encoding of the lead time. The predicted metric is decoded into a surface by a differentiable As-Rigid-As-Possible solver, and the model is trained end-to-end on the rigid-aligned vertex error. Training through the reconstruction keeps the decoded prediction a valid surface and consistently improves it. On 14 subcortical structures from the ADNI dataset, the proposed mesh evolution model (MT-GNN) predicts best among the evaluated methods at every horizon ($-2.29\%$ mean vertex error vs. the temporal mean, $p{=}6.1{\times}10^{-5}$, beating it on 14/14 structures), ahead of geodesic shape regression (DCM, $-0.19\%$) and a mesh transformer (TransforMesh, $-0.45\%$; $p{=}1.2{\times}10^{-4}$), with the lead widening as the horizon grows.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Mean Vertex Error (MVE)
```latex
-2.29\%
```
* Symbols: `%` (percentage), `MVE` (Mean Vertex Error)
* Why it matters: This is the mean vertex error of the predicted surface compared to the ground-truth surface, reported as a percentage.

### Equation 2: p-value
```latex
p = 6.1 × 10^{-5}
```
* Symbols: `p` (p-value), `×` (multiplication), `10^{-5}` (10 to the power of -5)
* Why it matters: This is the p-value of the statistical test used to compare the performance of MT-GNN with the temporal mean, indicating the significance of the difference.

### Equation 3: Mean Vertex Error (MVE) of Baseline
```latex
-0.19\%
```
* Symbols: `%` (percentage), `MVE` (Mean Vertex Error)
* Why it matters: This is the mean vertex error of the baseline method (DCM) compared to the ground-truth surface, reported as a percentage.

### Equation 4: Mean Vertex Error (MVE) of Another Baseline
```latex
-0.45\%
```
* Symbols: `%` (percentage), `MVE` (Mean Vertex Error)
* Why it matters: This is the mean vertex error of another baseline method (TransforMesh) compared to the ground-truth surface, reported as a percentage.

### Equation 5: Mean Vertex Error (MVE) of MT-GNN+H
```latex
-2.48\%
```
* Symbols: `%` (percentage), `MVE` (Mean Vertex Error)
* Why it matters: This is the mean vertex error of the variant of MT-GNN (MT-GNN+H) compared to the ground-truth surface, reported as a percentage.

**Method Summary**
================

* The proposed method, MT-GNN, predicts the surface's intrinsic geometry in continuous time using a graph network.
* The method takes into account the causal history of the structure and the lead time to predict the future surface.
* The predicted surface is decoded into a valid mesh using an As-Rigid-As-Possible solver.
* The model is trained end-to-end on the rigid-aligned vertex error.

**Experimental Overview**
=========================

* Tasks: Predicting brain morphometry with MT-GNN on 14 subcortical structures from the ADNI dataset.
* Datasets: Longitudinal T1 MRI from ADNI, processed with FreeSurfer 8.
* Baselines: DCM (geodesic/hierarchical Riemannian regressor) and TransforMesh (mesh transformer).
* Main claimed findings: MT-GNN outperforms the baselines in terms of mean vertex error at every horizon, with the lead widening as the horizon grows.

**What to Verify in the PDF**
=============================

* The implementation details of the As-Rigid-As-Possible solver used to decode the predicted surface into a valid mesh.
* The effect of the lead time on the performance of MT-GNN, including the impact of longer lead times on the widening gap to the temporal mean.
* The robustness of MT-GNN to outliers and segmentation failures, including the use of outlier flags and persistence error to remove such failures.
{% endraw %}

{% raw %}
## 2) SSTQ:Privacy-Preserving Vector Quantization via Subsampled Stochastic TurboQuant
- **Authors:** Adel Javanmard, David P. Woodruff, Vahab Mirrokni
- **arXiv:** [2608.05127](https://arxiv.org/abs/2608.05127v1) · [pdf](https://arxiv.org/pdf/2608.05127v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.05127v1))
- **Categories:** cs.LG, cs.AI, stat.ML

### Abstract
> Achieving local differential privacy in distributed optimization while maintaining low communication cost remains challenging. Existing vector quantization methods, such as vqSGD, use high-dimensional geometric constructions but incur unfavorable dimension-dependent variance. In this work, we propose Subsampled Stochastic TurboQuant (SSTQ), a framework that combines overcomplete equal-norm tight frames, coordinate subsampling, and privacy-aware one-dimensional quantization. SSTQ includes two variants: a Flat Randomized Response version and a Metric-Aware Laplace version, the latter being better suited to higher codebook bit-width regimes. We show that SSTQ achieves optimal mean squared error scaling while using only $\lceil \log_2 N \rceil + b$ bits per client, where $N = Θ(d)$ is the frame size. We also derive a surrogate privacy-aware codebook objective that reduces the codebook-dependent MSE scaling from $O(4^b)$ to $O(2^b)$. Finally, we empirically evaluate SSTQ against established baselines on federated learning tasks using CIFAR-10 and Fashion-MNIST, demonstrating favorable utility and communication efficiency.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: ⌈ log 2 N ⌉ + b

* Equation: ⌈ log 2 N ⌉ + b
* Symbols: ⌈ ⌉ (ceiling function), log 2 (base-2 logarithm), N (frame size)
* Why it matters: This equation represents the total number of bits required to represent the frame size N, where ⌈ log 2 N ⌉ is the ceiling of the base-2 logarithm of N and b is the bit budget.

### Equation 2: N = Θ(d)

* Equation: N = Θ(d)
* Symbols: N (frame size), d (dimensionality)
* Why it matters: This equation states that the frame size N is asymptotically equivalent to the dimensionality d, indicating that the frame size grows linearly with the dimensionality.

### Equation 3: O(4^b)

* Equation: O(4^b)
* Symbols: O (big O notation), b (bit budget)
* Why it matters: This equation represents the upper bound on the mean squared error scaling of the SSTQ algorithm, which is O(4^b), indicating that the error scaling grows exponentially with the bit budget.

### Equation 4: O(2^b)

* Equation: O(2^b)
* Symbols: O (big O notation), b (bit budget)
* Why it matters: This equation represents the improved mean squared error scaling of the SSTQ algorithm, which is O(2^b), indicating that the error scaling grows exponentially with the bit budget, but with a smaller constant factor.

### Equation 5: O(d/ε^2)

* Equation: O(d/ε^2)
* Symbols: O (big O notation), d (dimensionality), ε (privacy parameter)
* Why it matters: This equation represents the upper bound on the variance scaling of the SSTQ algorithm, which is O(d/ε^2), indicating that the variance scaling grows quadratically with the dimensionality and inversely with the privacy parameter.

**Method Summary**
==================

* The SSTQ algorithm combines overcomplete equal-norm tight frames, coordinate subsampling, and privacy-aware one-dimensional quantization to achieve local differential privacy in distributed optimization.
* The algorithm includes two variants: Flat Randomized Response and Metric-Aware Laplace.
* The SSTQ algorithm achieves optimal mean squared error scaling while using only ⌈ log 2 N ⌉ + b bits per client.
* The algorithm also derives a surrogate privacy-aware codebook objective that reduces the codebook-dependent MSE scaling from O(4^b) to O(2^b).

**Experimental Overview**
=========================

* Tasks: Federated learning on Fashion-MNIST and CIFAR-10 datasets.
* Baselines: SQKR, vqSGD.
* Main claimed findings: SSTQ achieves favorable utility and communication efficiency compared to established baselines, with optimal mean squared error scaling and reduced variance scaling.

**What to Verify in the PDF**
=============================

* The derivation of the surrogate privacy-aware codebook objective in Section C.1.
* The convergence analysis of the SSTQ algorithm in Section 6.
* The experimental results, including the training loss, test accuracy, and accuracy-vs-communication-cost tradeoff for both datasets.
{% endraw %}

{% raw %}
## 3) Chained Recursive Language Models for Multi-Iteration Reasoning
- **Authors:** Purbesh Mitra, Sennur Ulukus
- **arXiv:** [2608.05124](https://arxiv.org/abs/2608.05124v1) · [pdf](https://arxiv.org/pdf/2608.05124v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.05124v1))
- **Categories:** cs.CL, cs.AI, cs.IT, cs.LG, eess.SP

### Abstract
> Long context reasoning in large language models (LLMs) is usually constrained by the fact that a single inference trajectory has to simultaneously explore the context, store intermediate state, verify evidence, and produce the final answer. This becomes particularly difficult in tasks that require extraction, counting, ordering, or multi-hop reasoning, where an early mistake can propagate until the final response. In this work, we propose Chained Recursive Language Models (Chained RLM), an inference-time architecture, in which the same underlying model is called repeatedly as a sequence of fresh reasoning roots. Each root receives the original problem and context, but does not inherit the full conversational history. Instead, it receives a compact plain-text summary, a plain-text blackboard, and some durable task-specific artifacts written by predecessor roots. The motivation is to manage the context by chopping into partial tasks rather than one large inference response; in each staged computation, intermediate artifacts can be inspected, corrected, and extended by a later fresh inference by the same model. We describe the system model, handoff mechanism, artifact workspace, and evaluation protocol for this system. We study when fresh-context artifact continuation gives a measurable gain in accuracy over direct LLM answering even with recursive tool-calling.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: (q,c)

* Equation: (q,c)
* Symbols: q (query), c (context)
* Why it matters: This equation represents the input to the model, where q is the query and c is the context.

### Equation 2: y ~ f_{\theta}(q,c)

* Equation: y ~ f_{\theta}(q,c)
* Symbols: y (output), f_{\theta} (model output), q (query), c (context), \theta (model parameters)
* Why it matters: This equation represents the output of the model, where y is the predicted answer, f_{\theta} is the model output, and q and c are the input query and context.

### Equation 3: f_{\theta}

* Equation: f_{\theta}
* Symbols: f_{\theta} (model output), \theta (model parameters)
* Why it matters: This equation represents the model output, which is a function of the model parameters \theta.

### Equation 4: \theta

* Equation: \theta
* Symbols: \theta (model parameters)
* Why it matters: This equation represents the model parameters, which are learned during training.

### Equation 5: r = 0, 1, ..., R-1

* Equation: r = 0, 1, ..., R-1
* Symbols: r (iteration), R (number of iterations)
* Why it matters: This equation represents the iteration number, which is used to index the roots in the chaining mechanism.

**Method Summary**
==================

* The proposed architecture, Chained Recursive Language Models (Chained RLM), uses a sequence of fresh reasoning roots to manage the context.
* Each root receives the original problem and context, but does not inherit the full conversational history.
* The roots use a compact plain-text summary, a plain-text blackboard, and some durable task-specific artifacts written by predecessor roots.
* The architecture encourages later roots to read existing artifacts before starting a new extraction.

**Experimental Overview**
=========================

* Tasks/Datasets: Long-context tasks, including multi-hop retrieval, long-context aggregation, counting, and ordered event extraction.
* Baselines/Comparisons: Regular LLM, direct prediction from the problem and context.
* Main Claimed Findings: Chained RLM outperforms regular LLM in tasks that require multi-hop reasoning and long-context extraction.

**What to Verify in the PDF**
=============================

* The evaluation protocol for the proposed architecture, including the use of pass@1 accuracy as the primary metric.
* The handoff mechanism and artifact workspace, including how the model handles the transfer of artifacts between roots.
* The experimental results for the proposed architecture, including the comparison with regular LLM and the evaluation of the proposed architecture on different tasks and datasets.
{% endraw %}

{% raw %}
## 4) DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery
- **Authors:** Roberto Aliaga Medina, Paulina Quintanilla, Antonio del Rio Chanona
- **arXiv:** [2608.05120](https://arxiv.org/abs/2608.05120v1) · [pdf](https://arxiv.org/pdf/2608.05120v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.CE, cs.SC

### Abstract
> Kinetic model discovery is a central challenge in chemical engineering, as accurate rate expressions are essential for understanding and controlling chemical and biological processes. Symbolic regression (SR) has emerged as a powerful data-driven approach for identifying interpretable kinetic models, but usually operates without domain knowledge, often exploring physicochemically implausible models. Large language models (LLMs) offer a promising avenue for injecting domain expertise into this search. Here, we introduce an LLM-guided SR framework, embedding an LLM module within an iterative SR algorithm for automated kinetic model discovery. The LLM performs two roles at each iteration: (1) a qualitative physicochemical critique of the best SR candidates, and (2) the proposal of new candidate rate expressions guided by the SR-generated models and embedded chemical knowledge. Our framework is evaluated on four in silico case studies of increasing complexity, spanning heterogeneous catalysis and bioprocess systems. Results show the LLM-guided framework reduces iterations to identify the ground-truth model by $41.7-79.3\%$ versus a state-of-the-art SR framework, with the LLM directly proposing the correct model structure in over half of the guided runs. In practical settings, where each iteration typically requires a new wet-lab experiment, this translates into a substantial reduction in experimental effort. Predictive performance on an independent validation set is equivalent between both approaches, with $R^2>0.98$ in all case studies. Ablation studies indicate that both the SR component and the LLM scale contribute to this performance, with a reduced-size LLM largely retaining discovery efficiency. These findings demonstrate that LLMs can effectively inject domain knowledge into scientific model discovery, paving the way toward fully automated, domain-aware kinetic modelling pipelines.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
Unfortunately, no equations were found in the extracted context.

### Method Summary
* The authors propose a framework that combines symbolic regression (SR) with large language models (LLMs) for kinetic model discovery.
* The LLM is embedded within an iterative SR algorithm, performing two roles at each iteration: qualitative physicochemical critique and proposal of new candidate rate expressions.
* The framework is designed to reduce iterations and experimental effort in identifying the ground-truth model.
* The authors evaluate their framework on four in silico case studies, comparing it to a state-of-the-art SR framework.
* The LLM-guided framework achieves equivalent predictive performance to the baseline SR framework.

### Experimental Overview
* Tasks/Datasets: In silico case studies of increasing complexity, spanning heterogeneous catalysis and bioprocess systems.
* Baselines/Comparisons: State-of-the-art SR framework.
* Main Claimed Findings: The LLM-guided framework reduces iterations to identify the ground-truth model by 41.7-79.3% compared to the baseline SR framework, with equivalent predictive performance on an independent validation set.

### What to Verify in the PDF
* The exact implementation details of the LLM module and its integration with the SR algorithm.
* The physicochemical critique performed by the LLM and how it informs the proposal of new candidate rate expressions.
* The evaluation metrics used to assess the predictive performance of the LLM-guided framework, including the R^2 values reported in the paper.
{% endraw %}

{% raw %}
## 5) Representational separation between unitary and channel quantum generative models via shared classical randomness at shallow depth
- **Authors:** Arunava Majumder, Marius Krumm, Hendrik Poulsen Nautrup, Hans J. Briegel
- **arXiv:** [2608.05110](https://arxiv.org/abs/2608.05110v1) · [pdf](https://arxiv.org/pdf/2608.05110v1)
- **LLM context source:** abstract only
- **Categories:** quant-ph, cs.AI, cs.LG, stat.ML

### Abstract
> Near-term quantum hardware limits circuit depth and often imposes geometrically local connectivity for quantum generative models, restricting the output distributions accessible to shallow unitary Born models. Introducing stochasticity into a unitary quantum Born model can improve the empirical generative performance of the resulting channel model and, for a restricted small-scale architecture, has been proven to represent a strictly larger family of distributions than its unitary counterpart. However, whether such randomness provides a provable separation at fixed shallow depth for arbitrarily large systems has remained open. Here, we show that shared classical randomness, a comparatively weak resource from entanglement theory, is sufficient to establish such a strict scalable representational separation over the corresponding shallow unitary Born model. More specifically, we augment bounded-connectivity shallow unitary circuits, followed by computational-basis measurements, with spatially separated local Pauli operations, whose joint application is controlled by a single classically sampled random bit. The resulting shallow-depth channel model generates long-range correlations in the classical output distribution that no purely unitary shallow-depth model with bounded connectivity can reproduce. For one-dimensional nearest-neighbour architectures, reproducing such distributions with a purely unitary model can require depth $Ω(N)$ in the worst case. We further show that measurement-based quantum computation (MBQC) provides a natural implementation of the required shared classical randomness through suitable adaptation of the random measurement outcomes. Numerical experiments on MBQC-based generative models support the analytical results.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
### 1. Equation: No explicit equation found in the extracted context.

### 2. Equation: No explicit equation found in the extracted context.

### 3. Equation: No explicit equation found in the extracted context.

### 4. Equation: No explicit equation found in the extracted context.

### 5. Equation: No explicit equation found in the extracted context.

**Method Summary**
* The authors introduce a new method to representational separation between unitary and channel quantum generative models via shared classical randomness at shallow depth.
* The method involves augmenting bounded-connectivity shallow unitary circuits with spatially separated local Pauli operations, controlled by a single classically sampled random bit.
* The resulting shallow-depth channel model generates long-range correlations in the classical output distribution that no purely unitary shallow-depth model with bounded connectivity can reproduce.
* The authors show that measurement-based quantum computation (MBQC) provides a natural implementation of the required shared classical randomness.

**Experimental Overview**
* Tasks/Datasets: The authors perform numerical experiments on MBQC-based generative models.
* Baselines/Comparisons: The authors compare the performance of the proposed method with purely unitary shallow-depth models.
* Main Claimed Findings: The authors show that the proposed method can reproduce long-range correlations in the classical output distribution that no purely unitary shallow-depth model with bounded connectivity can reproduce.

**What to Verify in the PDF**
* The authors claim that for one-dimensional nearest-neighbour architectures, reproducing such distributions with a purely unitary model can require depth $Ω(N)$ in the worst case.
* The authors mention that the measurement-based quantum computation (MBQC) provides a natural implementation of the required shared classical randomness through suitable adaptation of the random measurement outcomes.
* The authors also mention that the numerical experiments support the analytical results, but it would be useful to see the specific details of these experiments, such as the datasets used and the evaluation metrics employed.
{% endraw %}
