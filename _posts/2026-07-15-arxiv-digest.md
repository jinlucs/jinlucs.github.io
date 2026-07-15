---
layout: post
title: "Daily arXiv Digest — 2026-07-15 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) A Shortcut to Statistically Steady-State Turbulence with Flow Matching
- **Authors:** Gianluca Galletti, Gerald Gutenbrunner, William Hornsby, Lorenzo Zanisi, Naomi Carey, Stanislas Pamela, Johannes Brandstetter, Fabian Paischer
- **arXiv:** [2607.13022](https://arxiv.org/abs/2607.13022v1) · [pdf](https://arxiv.org/pdf/2607.13022v1)
- **LLM context source:** abstract only
- **Categories:** physics.plasm-ph, cs.LG

### Abstract
> Many nonlinear physical systems exhibit an initial transient phase in which perturbations grow before nonlinear interactions lead to a statistically steady state. While this saturated regime is of primary interest, direct numerical simulations must resolve the full transient dynamics before reaching it, incurring significant computational cost. In Computational Fluid Dynamics, reduced-order approaches such as Large Eddy Simulation mitigate computational cost by modeling small-scale dynamics, enabling tractable approximations of turbulent flows. In contrast, for systems such as gyrokinetics, comparably effective closures for the full dynamics are not generally available, and high-fidelity simulations remain necessary. Existing surrogate modeling approaches for these systems are autoregressive, hence they suffer from accumulating error. We instead propose to bypass explicit time evolution by directly modeling the distribution of saturated states under an ergodicity assumption, stating that ensemble averages over samples are equivalent to time averages of a single long simulation. We introduce GyroFlow, a latent generative model that directly estimates steady-state statistics of gyrokinetic turbulence in 5D phase space, without resolving the transient phase. GyroFlow generates saturated snapshots from noise, conditioned on dimensionless operating parameters and outperforms autoregressive, reduced-order, and other generative approaches, while providing substantial speedup. To evaluate generation quality we propose FGyD, a distributional metric computed in the latent space of a pretrained gyrokinetic model, and show that it correlates with downstream flux accuracy and solver convergence. Finally, GyroFlow can be used to warm-start the numerical code used to produce the data.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough

1. **Equation:** Not found in extracted context.
2. **Equation:** Not found in extracted context.
3. **Equation:** Not found in extracted context.
4. **Equation:** Not found in extracted context.
5. **Equation:** Not found in extracted context.

### Method Summary

* The authors propose GyroFlow, a latent generative model that directly estimates steady-state statistics of gyrokinetic turbulence in 5D phase space.
* GyroFlow bypasses explicit time evolution by modeling the distribution of saturated states under an ergodicity assumption.
* The model is conditioned on dimensionless operating parameters.
* GyroFlow outperforms autoregressive, reduced-order, and other generative approaches.
* GyroFlow provides a substantial speedup compared to high-fidelity simulations.

### Experimental Overview

* **Tasks/Datasets:** The authors evaluate GyroFlow on gyrokinetic turbulence data.
* **Baselines/Comparisons:** The authors compare GyroFlow to autoregressive, reduced-order, and other generative approaches.
* **Main Claimed Findings:** GyroFlow outperforms baselines and provides a substantial speedup compared to high-fidelity simulations.

### What to Verify in the PDF

* Details on the FGyD distributional metric, including its computation and correlation with downstream flux accuracy and solver convergence.
* The pretrained gyrokinetic model used to evaluate GyroFlow's generation quality.
* The implementation of GyroFlow and its conditioning on dimensionless operating parameters.
{% endraw %}

{% raw %}
## 2) Watermark Forensics for Generative Models: An Information-Theoretic Perspective
- **Authors:** Xiaoyu Li, Zheng Gao, Xiaoyan Feng, Jiaojiao Jiang, Yulei Sui, Jiankun Hu
- **arXiv:** [2607.13003](https://arxiv.org/abs/2607.13003v1) · [pdf](https://arxiv.org/pdf/2607.13003v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.13003v1))
- **Categories:** cs.CR, cs.IT, cs.LG

### Abstract
> A watermark in a generative model's output is usually asked only whether a text is machine-made. The same mark can do more: attribute it to the user who produced it, extract a hidden payload, or localize the part that survives editing. These form a forensic ladder, and we ask what each rung costs in the sample length $n$. One object organizes the answers. Let $S$ be the secret the mark carries (a user's identity or payload), and let the information profile $ν(t)=I(S;X_t\mid X_{<t})$ record how much the $t$-th token reveals about $S$ given the earlier ones. Its total mass pays for attribution and extraction; how that mass is spread pays for localization; and detection alone is paid for not by information but by presence, the distance from the marked to the unmarked distribution. The literature's two quality models, a mark subtle on every token and one that stamps a few tokens loudly, are two incomparable ways of capping this profile. Our main theorem settles the ladder's entropy column. For statistically distortion-free schemes, attributing a text to one of $N$ users costs $Θ(\log N/h)$ tokens over every stationary-ergodic source of entropy rate $h$, sharp to a $(1+o(1))$ factor: to our knowledge the first tight entropy-rate law for multi-user attribution (via exact alignment). The natural collision-counting analysis overcharges without bound; only a decoder thresholding each candidate by its own realized surprisal attains the rate while almost never implicating an innocent user. A matching converse makes the law two-sided, and extraction of an $\ell$-bit payload costs $Θ(\ell/h)$. Two gaps are real, not modeling artifacts: a $Θ(\log N)$-token window in which a text is provably machine-made yet unattributable, and a footprint-resolution uncertainty principle. Experiments on GPT-2, Pythia-410M, and Qwen2.5 recover the predicted constants.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. Equation: ν(t) = I(S;X_t | X_<t>)
Symbols: ν(t), I(S;X_t | X_<t>)
Why it matters: This equation represents the information profile of the scheme's forensic payload S, which records how much the t-th token reveals about S given the earlier ones.

### 2. Equation: ∥ν∥1 = I(S;X)
Symbols: ∥ν∥1, I(S;X)
Why it matters: This equation represents the total mass of the information profile, which is the amount of information that the scheme's forensic payload S carries about the source S.

### 3. Equation: Φ(n) = ∥ν∥1
Symbols: Φ(n), ∥ν∥1
Why it matters: This equation represents the forensic-recovery budget, which is the maximum amount of information that the scheme's forensic payload S can carry about the source S.

### 4. Equation: ν(t) = ∑t I(S;X_t | X_<t>)
Symbols: ν(t), I(S;X_t | X_<t>)
Why it matters: This equation represents the chain rule, which resolves the information about S position by position.

### 5. Equation: ∥ν∥1 = I(S;X) = Φ(n)
Symbols: ∥ν∥1, I(S;X), Φ(n)
Why it matters: This equation represents the relationship between the total mass of the information profile and the forensic-recovery budget, which is a key concept in the paper.

**Method Summary**
==================

* The paper proposes a new approach to watermark forensics for generative models, which treats the forensic uses of a watermark as a ladder of four statistical problems.
* The approach is based on the concept of an information profile, which records how much the t-th token reveals about S given the earlier ones.
* The paper shows that the forensic power of a watermark is set by the information it makes recoverable, position by position, and not by the mechanics of how the mark is embedded.
* The approach is compared to two existing quality models, which are shown to be norm caps on the information profile.

**Experimental Overview**
=========================

* Tasks: The paper evaluates the proposed approach on three datasets: GPT-2, Pythia-410M, and Qwen2.5.
* Baselines: The paper compares the proposed approach to two existing quality models, which are shown to be norm caps on the information profile.
* Main claimed findings: The paper shows that the proposed approach outperforms the existing quality models in terms of attribution, extraction, and localization.

**What to Verify in the PDF**
=============================

* The proof of the main theorem, which shows that attributing a text to one of N users costs Θ( log N / h ) tokens over every stationary-ergodic source of entropy rate h.
* The derivation of the relationship between the total mass of the information profile and the forensic-recovery budget, which is a key concept in the paper.
* The experimental results, which show the performance of the proposed approach on the three datasets.
{% endraw %}

{% raw %}
## 3) Ensemble Controlled-Flow Filtering for Implicit Data Assimilation
- **Authors:** Zhuoyuan Li, Yue Zhao, Ming Li
- **arXiv:** [2607.12975](https://arxiv.org/abs/2607.12975v1) · [pdf](https://arxiv.org/pdf/2607.12975v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.12975v1))
- **Categories:** stat.ML, cs.LG, math.NA, math.OC

### Abstract
> Data assimilation estimates the state of a dynamical system from model forecasts and incoming observations. Many observation mechanisms, however, are many-to-one, implicit, non-smooth, or accessible only through simulation, and need not provide the residual structures or likelihood guidance required by existing ensemble filters. We introduce implicit data assimilation, in which the analysis law is defined as an energy tilt of the forecast distribution. We then propose the Ensemble Controlled-flow Filter (EnCF), which realizes this update through a stochastic controlled flow and learns the observation-dependent control by adjoint matching from terminal energy gradients. For simulator-defined observations, EnCF-LF learns a surrogate conditional energy from samples and applies the same controlled-flow solver. We prove ideal exactness, derive a one-step error decomposition, and establish non-accumulation of local errors under filter stability. Numerical results show that Kalman-type filters remain preferable for smooth additive-Gaussian observations, while the proposed methods are better suited to non-Gaussian, many-to-one, multimodal, and implicit observation models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: π^{\mathrm{f}}
π^{\mathrm{f}} is the forecast distribution, which represents the probability distribution of the state at the next time step.

### Equation 2: π^{\mathrm{a}}\propto\ell(\cdot;y)\pi^{\mathrm{f}}
π^{\mathrm{a}} is the analysis distribution, which is proportional to the product of the likelihood function ℓ and the forecast distribution π^{\mathrm{f}}. This equation represents the update of the analysis distribution based on the likelihood of the observation.

### Equation 3: ℓ
ℓ is the likelihood function, which represents the probability of observing the data given the state.

### Equation 4: J(x;y)
J(x;y) is the energy function, which measures the difference between the observation and the predicted state.

### Equation 5: π^{\mathrm{a}}(x\mid y)\propto\pi^{\mathrm{f}}(x)\exp[-J(x;y)]
This equation represents the posterior distribution of the state given the observation, which is proportional to the product of the forecast distribution π^{\mathrm{f}} and the exponential of the negative energy function J(x;y).

**Method Summary**
==================

*   The proposed method, Ensemble Controlled-Flow Filtering (EnCF), is a novel approach to data assimilation that uses a controlled transport from the forecast law to an energy-tilted analysis law.
*   EnCF approximates the optimal feedback control through adjoint matching and learns the observation-dependent control by matching the terminal energy gradients.
*   The likelihood-free variant, EnCF-LF, learns a surrogate energy from simulator samples and uses the same controlled-flow solver.
*   The method is designed to handle implicit, non-additive observation models and is particularly useful for many-to-one, multimodal, and non-Gaussian observation regimes.

**Experimental Overview**
=========================

*   The experiments evaluate the proposed EnCF and its likelihood-free variant EnCF-LF against classical ensemble filters and recently developed flow-based filters.
*   The experiments are organized according to the structure of the observation model, including smooth additive-Gaussian, non-Gaussian additive noise, many-to-one sign-blind sensor, and implicit, non-additive observation relation.
*   The main claimed findings include that Kalman-type filters remain preferable for smooth additive-Gaussian observations, while the proposed methods are better suited to non-Gaussian, many-to-one, multimodal, and implicit observation models.

**What to Verify in the PDF**
=============================

*   The mathematical derivation of the controlled-flow solver and the adjoint-matching regression.
*   The implementation details of the convolutional neural network and the merge convolution.
*   The hyperparameter tuning and regularization schedule used in the experiments.
*   The numerical results and error analysis for the different observation models and baselines.
{% endraw %}

{% raw %}
## 4) Sharp Optimal Algorithm for Derivative-Free Stochastic Convex Optimization in One Dimension
- **Authors:** Alexandra Carpentier, Chloé Rouyer, Alexandre Tsybakov, Arya Akhavan
- **arXiv:** [2607.12938](https://arxiv.org/abs/2607.12938v1) · [pdf](https://arxiv.org/pdf/2607.12938v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.12938v1))
- **Categories:** math.OC, stat.ML

### Abstract
> Stochastic convex optimization is a classical problem with well-understood guarantees under first-order feedback. In contrast, for zero-order optimization with noisy function evaluations, a logarithmic gap has persisted between known upper bounds and the $Ω(1/\sqrt{T})$ lower bound, even in the one-dimensional case. In this work, we study the problem of minimizing a convex function $f : [0,1] \to [0,1]$ using a zero-order oracle with subGaussian noise. We propose a computationally efficient algorithm that achieves the optimal $O(1/\sqrt{T})$ convergence rate, matching the lower bound. The result closes the existing gap in one dimension, providing the first sharp rate guarantee in this setting.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Ω(1/√T)
```latex
\Omega(1/\sqrt{T})
```
* Symbols: Ω, 1/√T
* Matters: Lower bound on the rate of convergence for zero-order optimization in one dimension.

### Equation 2: f:[0,1]→[0,1]
```latex
f:[0,1]\to[0,1]
```
* Symbols: f, [0,1]
* Matters: Domain and range of the convex function f.

### Equation 3: O(1/√T)
```latex
O(1/\sqrt{T})
```
* Symbols: O, 1/√T
* Matters: Upper bound on the rate of convergence for zero-order optimization in one dimension.

### Equation 4: x_t
```latex
x_{t}
```
* Symbols: x_t
* Matters: Query point selected by the learner at each round t.

### Equation 5: [0,1]
```latex
[0,1]
```
* Symbols: [0,1]
* Matters: Domain of the convex function f.

### Equation 6: f(x_t) + ξ_t
```latex
f(x_{t})+\xi_{t}
```
* Symbols: f(x_t), ξ_t
* Matters: Noisy function evaluation at query point x_t.

### Equation 7: f(x_t)
```latex
f(x_{t})
```
* Symbols: f(x_t)
* Matters: Clean function evaluation at query point x_t.

### Equation 8: ξ_t
```latex
\xi_{t}
```
* Symbols: ξ_t
* Matters: SubGaussian noise added to the function evaluation.

**Method Summary**
==================

* The proposed algorithm consists of a meta-algorithm and a splitting algorithm.
* The meta-algorithm applies the splitting algorithm in epochs numbered r = 1, 2, …, R.
* The splitting algorithm reduces the size of the searched interval and achieves a significantly smaller range of function f on the reduced interval.
* The algorithm is designed to achieve the optimal O(1/√T) convergence rate.

**Experimental Overview**
=========================

* Tasks/Datasets: Stochastic convex optimization in one dimension.
* Baselines/Comparisons: Not specified.
* Main claimed findings: The proposed algorithm achieves the optimal O(1/√T) convergence rate, closing the existing gap in one dimension.

**What to Verify in the PDF**
=============================

* The proof of Theorem 4.1, including the bound on the budget and the bound on the simple regret.
* The analysis of the expected simple regret, including the choice of δ* and the derivation of the bound.
* The condition C¯ ≥ 2( log(3) ) − 1/2( log(log(3) ) − 2, which is assumed throughout the proof.
{% endraw %}

{% raw %}
## 5) Accelerated Mixing Time of Randomized Hamiltonian Monte Carlo
- **Authors:** Siddharth Mitra, Vishwak Srinivasan, Xiuyuan Wang, Andre Wibisono
- **arXiv:** [2607.12902](https://arxiv.org/abs/2607.12902v1) · [pdf](https://arxiv.org/pdf/2607.12902v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.12902v1))
- **Categories:** stat.ML, cs.DS, cs.LG, math.PR, math.ST, stat.CO

### Abstract
> We show the Randomized Hamiltonian Monte Carlo (RHMC) algorithm has accelerated mixing time guarantees for sampling from log-concave probability distributions. RHMC proceeds by repeatedly simulating the continuous-time Hamiltonian dynamics for some random integration times, and resetting the velocity to be an independent Gaussian random variable between each simulation. We show that when the target distribution is log-concave and satisfies an $α$-Talagrand inequality (for example, if the target distribution is $α$-strongly log-concave), if we use a random integration time from either the triangular or the exponential distribution with mean $Θ(α^{-1/2})$, then RHMC converges exponentially fast in KL divergence, and the total integration time to reach error $\varepsilon$ in KL divergence scales as $O(α^{-1/2} \log(\varepsilon^{-1}))$. We also show that when the target distribution is log-concave, if we use a sequence of random integration times from the triangular distribution with exponentially increasing means, then the total integration time to reach error $\varepsilon$ in KL divergence scales as $O(\varepsilon^{-1/2})$. Our analysis relies on a bound on the average KL divergence along Hamiltonian dynamics, which is inspired by an analogous result on accelerated optimization methods based on Hamiltonian dynamics.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: α

* Equation: α
* Symbols: α
* Why it matters: α represents the parameter that determines the strength of the Talagrand inequality, which is used to analyze the mixing time of the Randomized Hamiltonian Monte Carlo (RHMC) algorithm.

### Equation 2: Θ(α^{-1/2})

* Equation: Θ(α^{-1/2})
* Symbols: Θ, α^{-1/2}
* Why it matters: Θ(α^{-1/2}) represents the mean of the triangular distribution used to generate random integration times in the RHMC algorithm. It is inversely proportional to the square root of α.

### Equation 3: ε

* Equation: ε
* Symbols: ε
* Why it matters: ε represents the error level in the KL divergence between the target distribution and the distribution output by the RHMC algorithm.

### Equation 4: O(α^{-1/2} log(ε^{-1}))

* Equation: O(α^{-1/2} log(ε^{-1}))
* Symbols: O, α^{-1/2}, log(ε^{-1})
* Why it matters: This equation represents the complexity of the RHMC algorithm in terms of the total integration time required to reach a prescribed error in KL divergence. It shows that the complexity scales as the inverse square root of α times the logarithm of the inverse of ε.

### Equation 5: O(ε^{-1/2})

* Equation: O(ε^{-1/2})
* Symbols: O, ε^{-1/2}
* Why it matters: This equation represents the complexity of the RHMC algorithm in terms of the total integration time required to reach a prescribed error in KL divergence when the target distribution is log-concave. It shows that the complexity scales as the inverse square root of ε.

### Equation 6: ν^X

* Equation: ν^X
* Symbols: ν^X
* Why it matters: ν^X represents the target distribution that the RHMC algorithm aims to sample from.

**Method Summary**
==================

* The Randomized Hamiltonian Monte Carlo (RHMC) algorithm is a stochastic algorithm that uses Hamiltonian dynamics to sample from a target distribution.
* The algorithm consists of repeatedly simulating the Hamiltonian flow for random integration times and resetting the velocity to be an independent Gaussian random variable between each simulation.
* The RHMC algorithm has accelerated mixing time guarantees for sampling from log-concave probability distributions that satisfy certain structural assumptions.
* The algorithm can be analyzed using a bound on the average KL divergence along Hamiltonian dynamics, which is inspired by an analogous result on accelerated optimization methods based on Hamiltonian dynamics.

**Experimental Overview**
=========================

* Tasks/Datasets: The paper analyzes the RHMC algorithm on various settings, including log-concave distributions and distributions that satisfy the α-Talagrand inequality.
* Baselines/Comparisons: The paper compares the RHMC algorithm with other algorithms, such as the overdamped and underdamped Langevin dynamics.
* Main Claimed Findings: The paper shows that the RHMC algorithm has accelerated mixing time guarantees for sampling from log-concave probability distributions, and that the complexity of the algorithm scales as the inverse square root of α times the logarithm of the inverse of ε.

**What to Verify in the PDF**
=============================

* The proof of Theorem 1, which shows that the RHMC algorithm converges exponentially fast in KL divergence for target distributions that satisfy the α-Talagrand inequality and are M-M semi-log-concave.
* The proof of Theorem 2, which shows that the RHMC algorithm converges exponentially fast in KL divergence for log-concave distributions.
* The analysis of the RHMC algorithm in the setting of log-smooth distributions, which is not fully presented in the extracted context.
{% endraw %}
