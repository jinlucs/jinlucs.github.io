---
layout: post
title: "Daily arXiv Digest — 2026-08-28 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Adversarially-Informed Node Criticality Identification in Power Grid Measurements
- **Authors:** Koto Omiloli, Olugbenga Moses Anubi
- **arXiv:** [2608.27393](https://arxiv.org/abs/2608.27393v1) · [pdf](https://arxiv.org/pdf/2608.27393v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.27393v1))
- **Categories:** eess.SY, math.OC

### Abstract
> Power grid state estimation relies on sensor measurements that are increasingly vulnerable to adversarial corruption in cyberphysical environments, potentially leading to significant deviations in system observations. This motivates the need to identify critical measurement nodes whose compromise results in the most severe system-level impact. However, existing node criticality methods primarily rely on structural or steady-state analyses and do not explicitly account for adversarial effects on system behavior. To address this gap, this paper proposes an adversarially informed framework for identifying critical measurement nodes in linearized power systems. Within this framework, a structured attack generation mechanism is developed to construct stealthy and effective false data injection attacks (FDIAs) against an H-infinity resilient state estimator. Node criticality is then evaluated using coalition-based marginal contributions of compromised sensor subsets, estimated via permutation sampling over a prescribed set of admissible nodes, with the resulting importance scores mapped to the corresponding physical buses. Simulation results on the IEEE 14-bus system show that adversarially identified nodes induce larger deviations in frequency, voltage angle, and net power compared to randomly selected nodes, demonstrating the effectiveness of the proposed framework.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: H∞

\[ H_{\infty} = \begin{bmatrix} M & D_g \\ D_l & M \end{bmatrix} \]

Symbols:

*   \( M \): generator inertia matrix
*   \( D_g \): generator damping matrix
*   \( D_l \): load damping matrix

Why it matters: This equation represents the system matrices for the linearized power system model.

### Equation 2: ℝ

\[ \mathbb{R} = \{ x \in \mathbb{R} : x \geq 0 \} \]

Symbols:

*   \( \mathbb{R} \): set of real numbers
*   \( x \): scalar variable

Why it matters: This equation defines the set of real numbers, which is used to denote scalar variables.

### Equation 3: ℝ^n

\[ \mathbb{R}^n = \{ \mathbf{x} \in \mathbb{R} : \mathbf{x} = (x_1, x_2, \ldots, x_n) \} \]

Symbols:

*   \( \mathbb{R}^n \): space of real-valued vectors of dimension n
*   \( \mathbf{x} \): vector variable

Why it matters: This equation defines the space of real-valued vectors of dimension n, which is used to denote vector variables.

### Equation 4: x ∈ ℝ

\[ x \in \mathbb{R} \]

Symbols:

*   \( x \): scalar variable
*   \( \mathbb{R} \): set of real numbers

Why it matters: This equation denotes a scalar variable x as an element of the set of real numbers.

### Equation 5: \mathbf{x} ∈ \mathbb{R}^n

\[ \mathbf{x} \in \mathbb{R}^n \]

Symbols:

*   \( \mathbf{x} \): vector variable
*   \( \mathbb{R}^n \): space of real-valued vectors of dimension n

Why it matters: This equation denotes a vector variable x as an element of the space of real-valued vectors of dimension n.

**Method Summary**
==================

*   The proposed framework identifies critical measurement nodes in linearized power systems using an adversarially informed approach.
*   The framework consists of a structured attack generation mechanism and a node criticality evaluation method based on coalition-based marginal contributions.
*   The method is evaluated using a linearized dynamic model of the IEEE 14-bus power system.

**Experimental Overview**
=========================

*   Tasks/Datasets: The proposed framework is evaluated using a linearized dynamic model of the IEEE 14-bus power system.
*   Baselines/Comparisons: The framework is compared to randomly selected nodes in terms of system-level impact.
*   Main Claimed Findings: The proposed framework identifies critical measurement nodes that induce larger deviations in frequency, voltage angle, and net power compared to randomly selected nodes.

**What to Verify in the PDF**
=============================

*   The detailed derivation of the structured attack generation mechanism.
*   The evaluation of the framework's performance using different network parameters and attack scenarios.
*   The comparison of the proposed framework with other node criticality methods.
{% endraw %}

{% raw %}
## 2) How Language Models Organize and Structure Moral Knowledge
- **Authors:** Orion Reblitz-Richardson
- **arXiv:** [2608.27402](https://arxiv.org/abs/2608.27402v1) · [pdf](https://arxiv.org/pdf/2608.27402v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.27402v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> How do large language models (LLMs) organize moral knowledge? Models detect moral content broadly, but detection is a low bar. We ask whether they go further, distinguishing moral foundations from one another and organizing the relationships between them geometrically. We train six independent linear probes on open-weight language models, one per Moral Foundations Theory (MFT) category (care/harm, fair/cheat, lib/oppress, loy/betray, auth/subv, sanc/degrade), and examine how the resulting directions relate to each other in representation space. We find the directions neither collapse into a single moral detector nor isolate from one another. Rather, they span a near-maximal number of independent dimensions while sharing a positive common component. The shared component is the signature of integration, and it is moral-specific relative to a matched non-moral concept battery built identically (mean pairwise cosine 0.26 vs. 0.013). The geometry is consistent across architectures and scale and reaches its integration regime early in pre-training, well before probe accuracy saturates. The structure the model discovers shows no evidence of the individualizing/binding distinction predicted by Moral Foundations Theory (an underpowered test: only 20 candidate partitions exist) but rather reflects corpus statistics. Extending to moral dilemmas, each dilemma direction partially composes from its component foundations, at 2.7x a mismatched-pair baseline, while the majority of its variance encodes conflict-specific structure. The model represents moral tension itself, not a pre-resolved judgment.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 2.7 ×

* Equation: 2.7 ×
* Symbols: 2.7, ×
* Why it matters: Not found in extracted context.

### Equation 2: ×

* Equation: ×
* Symbols: ×
* Why it matters: Not found in extracted context.

### Equation 3: ≈ 0.22

* Equation: ≈ 0.22
* Symbols: ≈, 0.22
* Why it matters: Not found in extracted context.

### Equation 4: 0.27

* Equation: 0.27
* Symbols: 0.27
* Why it matters: Not found in extracted context.

### Equation 5: {\sim}20 ×

* Equation: {\sim}20 ×
* Symbols: {\sim}, 20, ×
* Why it matters: Not found in extracted context.

### Equation 6: Δ=0.223

* Equation: Δ=0.223
* Symbols: Δ, 0.223
* Why it matters: Not found in extracted context.

### Equation 7: [0.202,0.244]

* Equation: [0.202,0.244]
* Symbols: [0.202,0.244]
* Why it matters: Not found in extracted context.

### Equation 8: p=0.05

* Equation: p=0.05
* Symbols: p, 0.05
* Why it matters: Not found in extracted context.

**Method Summary**
==================

* We train six foundation-specific linear probes at each transformer layer.
* We extract the learned weight vectors as geometric directions in representation space and analyze the angular relationships between these directions.
* The methodology decomposes into five components: foundation-specific probing, geometric analysis of probe directions, bootstrap direction stability assessment, framework-specific fragility testing, and the probing dataset.

**Experimental Overview**
=========================

* Tasks/Datasets: Moral dilemma scenarios, neutral sentences
* Baselines/Comparisons: Three base models from the same lab (Ai2), a larger dense model as a scale control
* Main Claimed Findings: Moral foundation content is linearly separable from the earliest layer, with distinct directions for each moral foundation.
{% endraw %}

{% raw %}
## 3) Token-Level Advertising
- **Authors:** Hanbing Liu, Bowei Zhang, Changyuan Yu, Yinyu Ye, Qi Qi
- **arXiv:** [2608.27382](https://arxiv.org/abs/2608.27382v1) · [pdf](https://arxiv.org/pdf/2608.27382v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.27382v1))
- **Categories:** cs.GT, cs.LG

### Abstract
> Generative AI is transforming how people access information, challenging traditional advertising mechanisms built around predefined slots. Towards generation-native advertising, we propose the Latent Advertiser Mixture Auction (LAMA), a token-level advertising mechanism that embeds advertiser influence directly into the generation process. Advertisers report local continuation values that induce advertiser-specific next-token policies, from which the platform decodes through a latent mixture while updating an allocation posterior. We show that LAMA satisfies Markov DSIC and IR, and achieves near-optimal KL-regularized welfare. We further develop a learning-based implementation that reconstructs the required reports online from learned local advantages and root values. Proof-of-concept experiments on real-world commercial-search query splits show that LAMA improves platform welfare and revenue while maintaining user-facing response quality, providing initial evidence for the feasibility of generation-native advertising.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: β\log|\mathcal{N}|

* Equation: β\log|\mathcal{N}|
* Symbols: β, \mathcal{N}
* Why it matters: This equation is likely related to the calculation of a loss function or regularization term in the context of the Latent Advertiser Mixture Auction (LAMA) mechanism.

### Equation 2: \mathcal{V}

* Equation: \mathcal{V}
* Symbols: \mathcal{V}
* Why it matters: This equation is likely related to the calculation of a value or utility function in the context of the LAMA mechanism.

### Equation 3: |\mathcal{V}|\geq 3

* Equation: |\mathcal{V}|\geq 3
* Symbols: |\mathcal{V}|
* Why it matters: This equation is likely related to a constraint or condition on the value function \mathcal{V} in the context of the LAMA mechanism.

### Equation 4: \mathcal{S}:=\mathcal{V}^{\leq L}=\bigcup_{t=0}^{L}\mathcal{V}^{t}

* Equation: \mathcal{S}:=\mathcal{V}^{\leq L}=\bigcup_{t=0}^{L}\mathcal{V}^{t}
* Symbols: \mathcal{S}, \mathcal{V}^{\leq L}, \mathcal{V}^{t}
* Why it matters: This equation is likely related to the definition of a set or collection of sets in the context of the LAMA mechanism.

### Equation 5: \mathcal{V}^{0}=\{\emptyset\}

* Equation: \mathcal{V}^{0}=\{\emptyset\}
* Symbols: \mathcal{V}^{0}
* Why it matters: This equation is likely related to the initialization or base case of the LAMA mechanism.

**Method Summary**
==================

* The Latent Advertiser Mixture Auction (LAMA) is a token-level advertising mechanism that embeds advertiser influence directly into the generation process.
* LAMA uses a latent mixture to decode the next token based on the advertiser's local continuation values.
* The mechanism is designed to satisfy Markov DSIC and IR, and achieves near-optimal KL-regularized welfare.
* LAMA is implemented using a learning-based approach that reconstructs the required reports online from learned local advantages and root values.

**Experimental Overview**
========================

* The experiments evaluate the performance of LAMA in generation-native advertising settings.
* The goal is to test whether token-level participation of advertisers can improve monetization while preserving the quality and naturalness of generated responses.
* The experiments use a reference language model, advertiser-shared report models, and a prediction model for oracle impression value.
* The main claimed findings include:
	+ LAMA achieves the strongest overall performance among the compared methods.
	+ LAMA delivers a clear improvement in revenue, welfare, and advertiser value.
	+ LAMA preserves user-facing response quality, matching the best-performing baseline on this dimension.

**What to Verify in the PDF**
=============================

* The implementation details of the LAMA mechanism, including the learning-based approach and the reconstruction of reports online.
* The experimental results for the three verticals (Workout, Vacation, and Car), including the performance metrics and the comparison with baselines.
* The additional experimental evidence presented in the appendix, including case studies, token-level analyses, latency measurements, and value prediction accuracy and calibration.
{% endraw %}

{% raw %}
## 4) Universality and sharp thresholds for ellipsoid fitting
- **Authors:** Frederic Koehler, Youngtak Sohn
- **arXiv:** [2608.27372](https://arxiv.org/abs/2608.27372v1) · [pdf](https://arxiv.org/pdf/2608.27372v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.27372v1))
- **Categories:** math.PR, cond-mat.dis-nn, cs.DS, cs.LG, math.ST

### Abstract
> We establish a sharp phase transition for fitting random vectors by an ellipsoid. The random vectors have independent subgaussian coordinates with mean zero, variance one, and a common fourth moment, and the number of vectors is proportional to the square of the dimension. We identify an explicit satisfiability threshold such that, with high probability, a positive definite ellipsoid passes through every data point below the threshold, whereas no positive semidefinite fit exists above it. We also determine the optimal squared fitting error throughout the unsatisfiable regime. In particular, the threshold depends on the coordinate distributions only through their common fourth moment, revealing a fourth moment universality phenomenon. For standard Gaussian data the threshold is $1/4$, resolving the ellipsoid fitting conjecture.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: x_{1},\ldots,x_{n}\in\mathbb{R}^{d}

* Equation: $x_{1},\ldots,x_{n}\in\mathbb{R}^{d}$
* Symbols: $x_i$ (random vectors), $n$ (dimension)
* Why it matters: Defines the input space for the ellipsoid fitting problem.

### Equation 2: R\succeq 0

* Equation: $R\succeq 0$
* Symbols: $R$ (positive definite matrix)
* Why it matters: Ensures that the ellipsoid is positive definite, which is a necessary condition for fitting.

### Equation 3: x_{i}^{\top}Rx_{i}=1,\quad\textnormal{for all}\quad i=1,\ldots,n.

* Equation: $x_{i}^{\top}Rx_{i}=1,\quad\textnormal{for all}\quad i=1,\ldots,n$
* Symbols: $x_i$ (random vectors), $R$ (positive definite matrix)
* Why it matters: Defines the constraint that the ellipsoid passes through every data point.

### Equation 4: x_{1},\ldots,x_{n}

* Equation: $x_{1},\ldots,x_{n}$
* Symbols: $x_i$ (random vectors), $n$ (dimension)
* Why it matters: Not explicitly defined in the context, but likely refers to the input space.

### Equation 5: d^{2}/4

* Equation: $d^{2}/4$
* Symbols: $d$ (dimension)
* Why it matters: Appears in the context of the fourth moment universality phenomenon.

**Method Summary**
==================

* The authors establish a sharp phase transition for fitting random vectors by an ellipsoid.
* They identify an explicit satisfiability threshold that depends solely on the common fourth moment of the coordinate distributions.
* The threshold is determined by the characteristic that determines its location.
* The authors use a combination of analytical and numerical methods to study the scalar variational problem.

**Experimental Overview**
========================

* Tasks/Datasets: The authors use a location mixture of two Gaussians to simulate random vectors with independent subgaussian coordinates.
* Baselines/Comparisons: Not explicitly mentioned in the context.
* Main Claimed Findings: The authors resolve Conjecture 1.1 and extend it to a broad class of non-Gaussian distributions. They show that the threshold is determined solely by the common fourth moment of the coordinate distributions.

**What to Verify in the PDF**
=============================

* The connection between the scalar variational problem and the GOE matrix is rigorously proved in Section 5.2.
* The numerical experiments in Section A.5 are used to validate the analytical results.
* The dependence of the threshold on the common fourth moment is explicitly shown in the context.
{% endraw %}

{% raw %}
## 5) UGM: A Unified Framework and New Perspectives for Accelerated Gradient Methods in Smooth and Strongly Convex Optimization
- **Authors:** Danqing Zhou, Shiqian Ma, Junfeng Yang
- **arXiv:** [2608.27368](https://arxiv.org/abs/2608.27368v1) · [pdf](https://arxiv.org/pdf/2608.27368v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.27368v1))
- **Categories:** math.OC

### Abstract
> In this paper, we propose a unified framework for accelerated gradient methods, dubbed UGM, which subsumes a wide range of accelerated and conventional gradient-type methods designed for minimizing $L$-smooth and $μ$-strongly convex functions. We demonstrate that the iteration update of the proposed framework can be intrinsically interpreted as a hybrid combination of the heavy-ball method and vanilla gradient descent. This interpretation reveals that classical accelerated gradient methods essentially integrate a conservative gradient descent step into the fast yet unstable heavy-ball dynamics, which achieves a favorable trade-off between acceleration and stability. We further establish a unified convergence analysis using Lyapunov functions. Guided by our analysis, we develop a family of enhanced accelerated gradient algorithms that leverage the inner product relationship between gradient information and iterative variables to optimize iterative updates. Extensive numerical experiments on unconstrained quadratic optimization and logistic regression validate that the proposed algorithms achieve superior performance compared with existing baseline methods under typical structural conditions.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 0 < μ < L < ∞

* Equation: 0 < μ < L < ∞
* Symbols: μ, L
* Why it matters: This equation represents the range of values for the strong convexity parameter μ and the smoothness parameter L, which are used to define the class of functions ℱ μ , L.

### Equation 2: ℰ μ , L

* Equation: ℰ μ , L
* Symbols: ℰ μ , L
* Why it matters: This equation represents the class of functions ℱ μ , L, which are μ-strongly convex and L-smooth.

### Equation 3: ℝ n

* Equation: ℝ n
* Symbols: ℝ n
* Why it matters: This equation represents the set of real numbers in n-dimensional space, which is the domain of the functions in ℱ μ , L.

### Equation 4: min x ∈ ℝ n f ( x ) , f ∈ ℱ μ , L

* Equation: min x ∈ ℝ n f ( x ) , f ∈ ℱ μ , L
* Symbols: min, x ∈ ℝ n, f ∈ ℱ μ , L
* Why it matters: This equation represents the minimization problem over the set of real numbers in n-dimensional space, where the objective function f is in the class ℱ μ , L.

### Equation 5: κ := L / μ

* Equation: κ := L / μ
* Symbols: κ, L, μ
* Why it matters: This equation represents the ratio of the smoothness parameter L to the strong convexity parameter μ, which is used to define the acceleration factor κ.

### Equation 6: x ∗

* Equation: x ∗
* Symbols: x ∗
* Why it matters: This equation represents the optimal solution x ∗, which is the minimizer of the function f in the class ℱ μ , L.

### Equation 7: f ∗ := f ( x ∗ )

* Equation: f ∗ := f ( x ∗ )
* Symbols: f ∗, f, x ∗
* Why it matters: This equation represents the optimal value f ∗, which is the value of the function f at the optimal solution x ∗.

### Equation 8: α > 0

* Equation: α > 0
* Symbols: α
* Why it matters: This equation represents the positive step size parameter α, which is used to control the convergence rate of the algorithms.

**Method Summary**
==================

* The UGM framework unifies diverse gradient methods by combining the heavy-ball method and vanilla gradient descent.
* The UGM framework subsumes a wide range of accelerated and conventional gradient-type methods designed for minimizing L-smooth and μ-strongly convex functions.
* The proposed algorithms leverage the inner product relationship between gradient information and iterative variables to optimize iterative updates.

**Experimental Overview**
=========================

* Tasks/Datasets: Unconstrained quadratic optimization, logistic regression, and softmax regression.
* Baselines/Comparisons: Classical FGM algorithm and existing baseline methods.
* Main Claimed Findings: The proposed UGM algorithms achieve superior performance compared with existing baseline methods under typical structural conditions.

**What to Verify in the PDF**
=============================

* The detailed configurations of the five eigenvalue distributions used in the numerical experiments.
* The proofs of the equivalence between the UGM framework and the classical FGM algorithm.
* The symbolic computation verification of the cumbersome identities used in the proofs of Lemmas B.4, B.5, B.6, and B.7.
{% endraw %}
