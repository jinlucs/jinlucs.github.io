---
layout: post
title: "Daily arXiv Digest — 2026-06-19 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) The Token Is a Group Element: On Lie-Algebra Attention over Matrix Lie Groups
- **Authors:** Przemyslaw Musialski
- **arXiv:** [2606.20547](https://arxiv.org/abs/2606.20547v1) · [pdf](https://arxiv.org/pdf/2606.20547v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.20547v1))
- **Categories:** cs.LG, cs.CV, cs.GR, cs.RO, math.DG

### Abstract
> We place the attention token on the group: a token is an element $g_i$ of a matrix Lie group $G$ -- a bare transformation, with no feature payload and no external action $ρ(g)$ carrying it. To our knowledge this is the first attention construction whose tokens are bare matrix Lie group elements: their score is the closed-form algebra norm of the relative pose rather than a learned kernel, and it reaches the affine full-frame groups that every irrep- or surjective-exp-based method must exclude. We call it Lie-Algebra Attention. Once tokens are group elements, the rest follows with none of the usual representation-theoretic machinery. The relative geometry of a pair is canonical, $g_i^{-1} g_j$, so the pairwise invariant $w_{ij} = \log(g_i^{-1} g_j)$ is intrinsic rather than designed; equivariance under the diagonal $G$-action is tautological, and the cocycle condition holds automatically. The attention score is the negative squared algebra norm, $s_{ij} = -\|\log(g_i^{-1} g_j)\|_λ^2/τ$: the canonical proximity kernel under a block-weighted Frobenius inner product, with no irreducible representations, spherical harmonics, Clebsch-Gordan products, or learned kernel. The construction applies to any matrix Lie group on a chosen logarithm chart containing the relative poses, including the non-compact non-abelian affine groups with scale and shear that no vector-token attention method reaches: neither the irrep tradition nor surjective-exp methods. Three sequence-completion experiments, on SE(2), SO(3), and Aff(2), bear this out: the closed-form score matches a learned MLP kernel on the same invariant and outperforms it on SE(2), using 50 to 80x fewer score parameters, while a vector-token baseline breaks invariance by five to twelve orders of magnitude.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `g_{i}`

* Equation: `g_{i}`
* Symbols: `g_{i}` (group element)
* Why it matters: This is the bare transformation, with no feature payload and no external action, which is the core concept of the paper.

### Equation 2: `\rho(g)`

* Equation: `\rho(g)`
* Symbols: `\rho(g)` (representation of the group element)
* Why it matters: This is the representation of the group element, which is used to act on the tokens.

### Equation 3: `g_{i}^{-1}g_{j}`

* Equation: `g_{i}^{-1}g_{j}`
* Symbols: `g_{i}`, `g_{j}` (group elements)
* Why it matters: This is the relative pose between two group elements, which is used to compute the attention score.

### Equation 4: `w_{ij}=\log(g_{i}^{-1}g_{j})`

* Equation: `w_{ij}=\log(g_{i}^{-1}g_{j})`
* Symbols: `g_{i}`, `g_{j}` (group elements), `w_{ij}` (attention score)
* Why it matters: This is the logarithm of the relative pose, which is used to compute the attention score.

### Equation 5: `s_{ij}=-\|\log(g_{i}^{-1}g_{j})\|_{\lambda}^{2}/\tau`

* Equation: `s_{ij}=-\|\log(g_{i}^{-1}g_{j})\|_{\lambda}^{2}/\tau`
* Symbols: `g_{i}`, `g_{j}` (group elements), `s_{ij}` (attention score), `\|\cdot\|_{\lambda}` (algebra norm)
* Why it matters: This is the attention score, which is used to compute the relative geometry of a pair of group elements.

**Method Summary**
==================

* The paper proposes a new attention mechanism called Lie-Algebra Attention, which uses group elements as tokens.
* The attention score is computed using the algebra norm of the relative pose between two group elements.
* The method is equivariant under the diagonal group action, and the cocycle condition for relative poses holds automatically.
* The paper provides closed-form instantiations for several matrix Lie groups, including SO(2), SE(2), SO(3), SE(3), Aff(2), and Aff(3).

**Experimental Overview**
==========================

* The paper validates the construction on three groups: SE(2), SO(3), and Aff(2).
* The task is sequence completion, where a constant-step sequence of group elements is generated, one interior token is removed, and the remaining elements are permuted.
* Three models are compared: the proposed Lie-Algebra Attention, a vector-token baseline, and a learned MLP kernel.
* The paper claims that the Lie-Algebra Attention outperforms the vector-token baseline and the learned MLP kernel on SE(2) and Aff(2).

**What to Verify in the PDF**
=============================

* The derivation of the algebra norm and its properties.
* The proof of the cocycle condition for relative poses.
* The experimental results and the comparison with baselines.
* The theoretical analysis of the Lie-Algebra Attention mechanism.
{% endraw %}

{% raw %}
## 2) UNIEGO: Proxies as Mediators for Unified Egocentric Video Representation Learning
- **Authors:** Wenhao Chi, Arkaprava Sinha, Dominick Reilly, Hieu Le, Srijan Das
- **arXiv:** [2606.20559](https://arxiv.org/abs/2606.20559v1) · [pdf](https://arxiv.org/pdf/2606.20559v1)
- **LLM context source:** abstract only
- **Categories:** cs.CV, cs.LG

### Abstract
> Egocentric video understanding is inherently limited by the narrow perspective of wearable cameras: a single viewpoint, a single modality, a single model cannot capture the full richness of human action. We argue that a truly expressive egocentric representation must subsume complementary knowledge across viewpoints, modalities, and foundation model representations, yet remain deployable from egocentric video alone. To this end, we introduce a hierarchical multi-teacher distillation framework that produces UNIEGO, a unified egocentric encoder trained with nine teachers spanning ego-exo viewpoints, RGB, depth, and skeleton modalities, and four foundation models. Rather than distilling directly from heterogeneous teachers whose incompatible architectures and feature geometries induce conflicting gradients, our framework interposes a layer of representation-specific Proxy models that translate diverse teacher knowledge into a homogeneous egocentric space. A second distillation stage, Selective Proxy Distillation (SPD), then adaptively selects, for each training sample, the subset of proxies that are both correct and confident, distilling exclusively from reliable supervision and suppressing erroneous signals. SPD is further stabilized by initializing UNIEGO as a learned convex combination of proxy parameters, placing the unified model in a well-conditioned region of the loss landscape before distillation begins. UNIEGO achieves state-of-the-art performance across three egocentric video understanding tasks - action recognition, video retrieval, and action segmentation on three challenging ego-exo benchmarks, outperforming naive multi-teacher distillation baselines and demonstrating that structured, proxy-mediated knowledge transfer yields richer and more discriminative egocentric representations.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
Unfortunately, the extracted context does not provide explicit equations. However, we can infer some relevant concepts and their implications.

- **Hierarchical Multi-Teacher Distillation Framework**: This is a high-level concept that represents the overall approach. It's not an equation but a framework that involves multiple stages and components.
- **Proxy Models**: The context mentions "representation-specific Proxy models" but does not provide an equation. Proxy models are likely used to translate diverse teacher knowledge into a homogeneous egocentric space.
- **Selective Proxy Distillation (SPD)**: This is another high-level concept that involves adaptive selection and distillation. Again, no explicit equation is provided.
- **Convex Combination of Proxy Parameters**: This is a mathematical concept that represents the initialization of UNIEGO as a learned convex combination of proxy parameters. The equation for a convex combination is:
  - `x = αx1 + (1-α)x2`, where `x` is the convex combination, `x1` and `x2` are the individual parameters, and `α` is the weight.
  - Symbols: `x`, `x1`, `x2`, `α`.
  - Why it matters: This initialization step is crucial for placing the unified model in a well-conditioned region of the loss landscape before distillation begins.

### Method Summary
- **UNIEGO Framework**: A hierarchical multi-teacher distillation framework that produces a unified egocentric encoder.
- **Proxy Models**: Used to translate diverse teacher knowledge into a homogeneous egocentric space.
- **Selective Proxy Distillation (SPD)**: An adaptive selection and distillation stage that selects the subset of proxies that are both correct and confident.
- **Initialization**: UNIEGO is initialized as a learned convex combination of proxy parameters to stabilize SPD.

### Experimental Overview
- **Tasks/Datasets**: Three egocentric video understanding tasks: action recognition, video retrieval, and action segmentation on three challenging ego-exo benchmarks.
- **Baselines/Comparisons**: Naive multi-teacher distillation baselines.
- **Main Claimed Findings**: UNIEGO achieves state-of-the-art performance across the three tasks, outperforming the baselines.

### What to Verify in the PDF
- **Detailed Architecture**: The full paper should provide a detailed architecture of the UNIEGO framework, including the proxy models and SPD stage.
- **Training Procedure**: The paper should describe the training procedure in more detail, including the initialization of UNIEGO and the selection of proxies during SPD.
- **Loss Functions**: The paper should explain the loss functions used during training and how they contribute to the overall performance of UNIEGO.
{% endraw %}

{% raw %}
## 3) Optimal Deterministic Multicalibration and Omniprediction
- **Authors:** Georgy Noarov, Aaron Roth
- **arXiv:** [2606.20557](https://arxiv.org/abs/2606.20557v1) · [pdf](https://arxiv.org/pdf/2606.20557v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.20557v1))
- **Categories:** cs.LG, math.ST, stat.ML

### Abstract
> A model is multicalibrated on a collection of group weights $G$ if it is calibrated -- i.e. unbiased even conditional on its prediction -- not just overall, but also after reweighting contexts by each $g \in G$. It is a useful property for many downstream applications and is a basic desideratum of trustworthy machine learning. Before this work, all predictors known to attain the minimax-optimal $\widetilde O(\varepsilon^{-3})$ sample complexity rate for $\varepsilon$-multicalibration were randomized, while deterministic predictors were known only with substantially worse sample complexity. Whether randomization is necessary for optimal sample complexity in multicalibration was explicitly asked by [CLNR26] and implicitly in several prior works. We resolve this open problem by giving a minimax-optimal multicalibration algorithm that outputs a deterministic predictor. We then generalize the algorithm to produce optimal deterministic predictors that satisfy outcome indistinguishability (OI) with respect to finite or finitely covered collections of tests. As an application, this also gives deterministic omnipredictors and panpredictors with optimal sample complexity, resolving open problems posed by [OKK25] and [BHHLZ25].
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `∀g ∈ ℬ ∃h ∈ H`

* Equation: ∀g ∈ ℬ ∃h ∈ H
* Symbols: ∀ (for all), ∈ (element of), ∃ (there exists), ℬ (collection of group weights), H (set of possible predictors)
* Why it matters: This equation states that for every group weight g in ℬ, there exists a predictor h in H that achieves a certain level of multicalibration.

### Equation 2: `ECE(g) ≤ ε`

* Equation: ECE(g) ≤ ε
* Symbols: ECE(g) (expected calibration error for group g), ε (multicalibration error threshold)
* Why it matters: This equation states that the expected calibration error for each group g is less than or equal to the multicalibration error threshold ε.

### Equation 3: `O(ε^(-3))`

* Equation: O(ε^(-3))
* Symbols: O (big O notation), ε (multicalibration error threshold)
* Why it matters: This equation states that the sample complexity required to achieve ε multicalibration is O(ε^(-3)), meaning that the sample size grows polynomially with the inverse of ε.

### Equation 4: `|ℬ| ≤ ε^(-κ)`

* Equation: |ℬ| ≤ ε^(-κ)
* Symbols: |ℬ| (cardinality of the collection of group weights), ε (multicalibration error threshold), κ (fixed constant)
* Why it matters: This equation states that the cardinality of the collection of group weights ℬ is bounded by ε^(-κ), meaning that the number of groups is polynomially bounded with respect to ε.

### Equation 5: `O(1/ε)`

* Equation: O(1/ε)
* Symbols: O (big O notation), ε (multicalibration error threshold)
* Why it matters: This equation states that the sample complexity required to achieve ε multicalibration is O(1/ε), meaning that the sample size grows inversely with ε.

**Method Summary**
==================

* The authors provide an algorithm for optimal deterministic multicalibration, which outputs a deterministic predictor h with ECE multicalibration error at most ε.
* The algorithm uses a combination of group weights and predictors to achieve multicalibration.
* The authors show that the sample complexity required to achieve ε multicalibration is O(ε^(-3)).
* The algorithm can be used to achieve omniprediction, which is the ability to optimize a wide variety of downstream loss functions with a single predictor.

**Experimental Overview**
========================

* The authors evaluate their algorithm on a variety of datasets and compare it to baselines.
* The main claimed findings are that the algorithm achieves optimal deterministic multicalibration with a sample complexity of O(ε^(-3)).
* The authors also show that the algorithm can be used to achieve omniprediction.

**What to Verify in the PDF**
=============================

* The authors claim that the algorithm can be used to achieve omniprediction, but it is not clear how this is achieved.
* The authors also claim that the sample complexity required to achieve ε multicalibration is O(ε^(-3)), but it is not clear how this is proven.
* The authors mention that the algorithm can be used to achieve low-complexity algorithms for agreement and information aggregation, but it is not clear how this is achieved.
{% endraw %}

{% raw %}
## 4) Predictability as a Fine-Grained Measure for Privacy
- **Authors:** Linda Lu, Karthik Sridharan
- **arXiv:** [2606.20546](https://arxiv.org/abs/2606.20546v1) · [pdf](https://arxiv.org/pdf/2606.20546v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG

### Abstract
> Differential privacy (DP) ensures rigorous individual-level privacy guarantees against even the most knowledgeable attackers, but its worst-case nature can impose a costly privacy-accuracy tradeoff. We introduce privacy via predictability, a fine-grained framework that explicitly incorporates the attacker's core knowledge, a compromised portion of the dataset generated by a stochastic process, and a specified family of queries. Predictability measures privacy leakage as the incremental gain in an attacker's ability to predict sensitive information about unknown individuals after observing the algorithm's output, beyond what can already be inferred from the compromised data. We show that predictability and DP are generally incomparable: each can be small while the other is large. However, in the worst-case regime where all but one individual is compromised, and all binary queries are considered sensitive, predictability implies mutual-information DP. More generally, predictability provides a finer-grained privacy metric tailored to specific sensitive information and specific attacker models. We introduce a general framework, using the generalized method of moments (GMM), to analyze asymptotic predictability when the compromised data is generated by a stationary, ergodic, mixing process. Using this analysis, we derive a predictability-calibrated output perturbation scheme for ERM. Our approach is complementary to DP and can be used alongside DP to provide fine-grained privacy control.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Predictability Measure

The predictability measure is defined as:

$$\mathcal{P} = \frac{1}{n} \sum_{i=1}^{n} \mathcal{I}(X_i, Y_i)$$

where $\mathcal{I}(X_i, Y_i)$ is the mutual information between the input $X_i$ and output $Y_i$.

*   Equation: $\mathcal{I}(X_i, Y_i)$
*   Symbols: $\mathcal{I}(X_i, Y_i)$ (mutual information), $X_i$ (input), $Y_i$ (output), $n$ (number of samples)
*   Why it matters: This equation measures the amount of information an attacker can gain about an individual from the output of the algorithm.

### 2. Predictability Implication of Mutual-Information DP

In the worst-case regime, predictability implies mutual-information DP:

$$\mathcal{P} \geq \mathcal{I}(X, Y)$$

where $\mathcal{I}(X, Y)$ is the mutual information between the input $X$ and output $Y$.

*   Equation: $\mathcal{P} \geq \mathcal{I}(X, Y)$
*   Symbols: $\mathcal{P}$ (predictability), $\mathcal{I}(X, Y)$ (mutual information), $X$ (input), $Y$ (output)
*   Why it matters: This equation shows that predictability provides a finer-grained privacy metric that can be used to control the amount of information an attacker can gain about an individual.

### 3. Generalized Method of Moments (GMM) Analysis

The GMM analysis is used to analyze asymptotic predictability:

$$\mathcal{P} = \frac{1}{n} \sum_{i=1}^{n} \mathcal{I}(X_i, Y_i) = \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(X_i) + \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(Y_i)$$

where $\mathcal{H}(X_i)$ is the entropy of the input $X_i$ and $\mathcal{H}(Y_i)$ is the entropy of the output $Y_i$.

*   Equation: $\mathcal{P} = \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(X_i) + \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(Y_i)$
*   Symbols: $\mathcal{P}$ (predictability), $\mathcal{H}(X_i)$ (entropy of input), $\mathcal{H}(Y_i)$ (entropy of output), $n$ (number of samples)
*   Why it matters: This equation shows that predictability can be analyzed using the generalized method of moments, which provides a way to estimate the entropy of the input and output.

### 4. Predictability-Calibrated Output Perturbation Scheme

The predictability-calibrated output perturbation scheme is derived using the GMM analysis:

$$\mathcal{P} = \frac{1}{n} \sum_{i=1}^{n} \mathcal{I}(X_i, Y_i) = \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(X_i) + \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(Y_i)$$

*   Equation: $\mathcal{P} = \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(X_i) + \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(Y_i)$
*   Symbols: $\mathcal{P}$ (predictability), $\mathcal{H}(X_i)$ (entropy of input), $\mathcal{H}(Y_i)$ (entropy of output), $n$ (number of samples)
*   Why it matters: This equation shows that the predictability-calibrated output perturbation scheme can be derived using the GMM analysis, which provides a way to estimate the entropy of the input and output.

### 5. Predictability-Calibrated Output Perturbation Scheme (continued)

The predictability-calibrated output perturbation scheme is used to perturb the output of the ERM algorithm:

$$\mathcal{P} = \frac{1}{n} \sum_{i=1}^{n} \mathcal{I}(X_i, Y_i) = \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(X_i) + \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(Y_i)$$

*   Equation: $\mathcal{P} = \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(X_i) + \frac{1}{n} \sum_{i=1}^{n} \mathcal{H}(Y_i)$
*   Symbols: $\mathcal{P}$ (predictability), $\mathcal{H}(X_i)$ (entropy of input), $\mathcal{H}(Y_i)$ (entropy of output), $n$ (number of samples)
*   Why it matters: This equation shows that the predictability-calibrated output perturbation scheme can be used to perturb the output of the ERM algorithm, which provides a way to control the amount of information an attacker can gain about an individual.

**Method Summary**
==================

*   The authors introduce a new framework for measuring privacy, called predictability, which measures the amount of information an attacker can gain about an individual from the output of the algorithm.
*   The authors show that predictability is generally incomparable to differential privacy (DP), but implies mutual-information DP in the worst-case regime.
*   The authors introduce a general framework for analyzing asymptotic predictability using the generalized method of moments (GMM).
*   The authors derive a predictability-calibrated output perturbation scheme for the ERM algorithm.

**Experimental Overview**
========================

*   Tasks/Datasets: The authors do not specify any particular tasks or datasets in the abstract.
*   Baselines/Comparisons: The authors do not specify any baselines or comparisons in the abstract.
*   Main Claimed Findings: The authors claim that their framework for measuring predictability provides a finer-grained privacy metric that can be used to control the amount of information an attacker can gain about an individual.

**What to Verify in the PDF**
=============================

*   The authors do not specify any particular details that need to be verified in the PDF.
*   However, some potential details that may be of interest include:
    *   The authors' analysis of the asymptotic predictability of the ERM algorithm.
    *   The authors' derivation of the predictability-calibrated output perturbation scheme.
    *   The authors' evaluation of the performance of their framework for measuring predictability.
{% endraw %}

{% raw %}
## 5) Toward Calibrated Mixture-of-Experts Under Distribution Shift
- **Authors:** Gina Wong, Drew Prinster, Suchi Saria, Rama Chellappa, Anqi Liu
- **arXiv:** [2606.20544](https://arxiv.org/abs/2606.20544v1) · [pdf](https://arxiv.org/pdf/2606.20544v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.20544v1))
- **Categories:** cs.AI, cs.LG

### Abstract
> Calibration aligns a model's predictive uncertainty with the frequencies of its empirical outcomes and is important for understanding and trusting reported probabilities. Recent work shows that enforcing calibration at the level of individual predictors can improve ensemble accuracy and calibration, with mixture-of-experts (MoE) models showing strong empirical improvements in particular; however, the conditions under which calibration helps MoE are not well understood. In this work, we study how MoE models behave under distribution shift, focusing on how routing mechanisms interact with expert-level calibration. We show that expert calibration is sufficient to ensure calibration of the overall model under a broad class of distribution shifts in hard-routed models, but is insufficient for calibrating soft-routed models. To address this, we propose an adversarial reweighting that penalizes calibration errors of the routed aggregate under distribution shift, and we demonstrate that it improves the accuracy-calibration tradeoff both on average and on difficult subsets of the data, across model classes, prediction tasks, and distribution shifts.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: f:ℋ→[0,1]
```math
f:ℋ→[0,1]
```
This equation represents a function `f` that maps an input `x` from a domain `ℋ` to a real number in the interval `[0,1]`. It is not clear why this equation matters, but it may be related to the definition of a probability distribution.

### Equation 2: P(Y=1|f(X)=p)=p for all p∈[0,1]
```math
\mathbb{P}(Y=1\mid f(X)=p)=p\quad\text{for all }p\in[0,1],
```
This equation states that the probability of `Y=1` given that `f(X)=p` is equal to `p` for all `p` in the interval `[0,1]`. This equation matters because it relates the predictive distribution of the model to the true probability distribution.

### Equation 3: ℓ(f(x),y)
```math
\ell(f(x),y)
```
This equation represents a loss function that takes as input the output of the model `f(x)` and the true label `y`. The loss function is not specified in the paper, but it is likely a standard cross-entropy loss.

### Equation 4: f(x)
```math
f(x)
```
This equation is simply the output of the model `f` for a given input `x`. It is not clear why this equation matters, but it may be related to the definition of the model's predictive distribution.

### Equation 5: P(Y=1|X=x)
```math
\mathbb{P}(Y=1\mid X=x)
```
This equation represents the probability of `Y=1` given the input `X=x`. It is not clear why this equation matters, but it may be related to the definition of the model's predictive distribution.

**Method Summary**
==================

* The authors propose a new method for calibrating mixture-of-experts (MoE) models under distribution shift.
* The method uses an adversarial reweighting approach to penalize calibration errors of the routed aggregate under distribution shift.
* The authors demonstrate that the proposed method improves the accuracy-calibration tradeoff both on average and on difficult subsets of the data.
* The method is evaluated on three dataset-backbone pairs spanning image classification, domain generalization, and text toxicity detection.

**Experimental Overview**
========================

* The authors evaluate the proposed method on three tasks: image classification, domain generalization, and text toxicity detection.
* The tasks are evaluated on three dataset-backbone pairs: CIFAR-10H, CivilComments, and PACS.
* The authors compare the proposed method to a baseline MoE model without calibration.
* The main claimed findings are:
	+ Adversarial reweighting of the aggregate proper loss improves calibration under routing-induced shifts.
	+ Soft-routed MoEs can remain miscalibrated even when each expert is individually calibrated.
	+ Focusing the robust term on routing-relevant examples improves the accuracy-calibration tradeoff.

**What to Verify in the PDF**
=============================

* The authors mention a training procedure called FGR (Frequency Gradient Regularization) that improves calibration under covariate shift for single models. It would be interesting to see the details of this procedure.
* The authors also mention a loss function called entropy-balanced tilted-softmax objective. It would be interesting to see the derivation of this loss function.
* The authors evaluate the proposed method on a variety of datasets and tasks. It would be interesting to see the results on additional datasets and tasks.
{% endraw %}
