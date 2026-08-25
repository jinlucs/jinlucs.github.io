---
layout: post
title: "Daily arXiv Digest — 2026-08-25 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Provably adaptive sampling with uniform and remasking discrete diffusion models
- **Authors:** Daniil Dmitriev, Zhihan Huang, Yuting Wei
- **arXiv:** [2608.23554](https://arxiv.org/abs/2608.23554v1) · [pdf](https://arxiv.org/pdf/2608.23554v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.23554v1))
- **Categories:** cs.LG, cs.IT, math.ST, stat.ML

### Abstract
> Discrete diffusion models offer a promising alternative to autoregressive generation by enabling parallel updates, but their sampling efficiency can depend strongly on the choice of the forward process and the sampler. For the uniform forward process, existing lower bounds for the standard $τ$-leaping sampler scale linearly with the ambient dimension $d$, raising the question of whether this dependence is intrinsic to the forward process. We answer this question in the negative. We consider a first-order sampler based on the leave-one-out denoiser for uniform and remasking processes whose coordinate updates can be performed in parallel. In both cases, the sampler can correct denoising mistakes during the sampling process, which becomes necessary when many coordinates are updated together. Our main result establishes an adaptive sampling guarantee: up to logarithmic factors, $N = O(\mathrm{DTC}(X_0) / \varepsilon)$ discretization steps suffice to achieve sampling error $O(\varepsilon_{\mathrm{score}}+\varepsilon)$, where $\varepsilon_{\mathrm{score}}$ is the error in score estimation. Thus, the sampling complexity is governed by the intrinsic dependence structure of the target distribution, as measured by its dual total correlation $\mathrm{DTC}(X_0)$, rather than directly by the ambient dimension $d$. Our analysis proceeds through a Bayes-optimal auxiliary sampler that separates discretization error from score-estimation error. We also derive an exact information-theoretic representation of the discretization error in terms of the mutual information between different coordinates of the forward process at different times. This representation applies to general forward processes and, in the uniform and remasking cases, can be controlled by $\mathrm{DTC}(X_0)$. Numerical experiments on structured synthetic distributions illustrate the predicted dimension-adaptive behavior.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\tau = \frac{1}{\varepsilon}$

* Equation: $\tau = \frac{1}{\varepsilon}$
* Symbols: $\tau$ (discretization parameter), $\varepsilon$ (error tolerance)
* Why it matters: This equation relates the discretization parameter $\tau$ to the error tolerance $\varepsilon$. A smaller $\varepsilon$ requires a larger $\tau$, which can lead to more accurate samples.

### Equation 2: $N = O\left(\frac{\mathrm{DTC}(X_{0})}{\varepsilon}\right)$

* Equation: $N = O\left(\frac{\mathrm{DTC}(X_{0})}{\varepsilon}\right)$
* Symbols: $N$ (number of discretization steps), $\mathrm{DTC}(X_{0})$ (dual total correlation at $X_{0}$), $\varepsilon$ (error tolerance)
* Why it matters: This equation provides an upper bound on the number of discretization steps $N$ required to achieve a certain level of accuracy $\varepsilon$. The bound depends on the dual total correlation $\mathrm{DTC}(X_{0})$ at the initial state $X_{0}$.

### Equation 3: $O(\varepsilon_{\mathrm{score}} + \varepsilon)$

* Equation: $O(\varepsilon_{\mathrm{score}} + \varepsilon)$
* Symbols: $\varepsilon_{\mathrm{score}}$ (score error), $\varepsilon$ (error tolerance)
* Why it matters: This equation provides an upper bound on the score error $\varepsilon_{\mathrm{score}}$ required to achieve a certain level of accuracy $\varepsilon$. The bound depends on the error tolerance $\varepsilon$.

### Equation 4: $\varepsilon_{\mathrm{score}}$

* Equation: $\varepsilon_{\mathrm{score}}$
* Symbols: $\varepsilon_{\mathrm{score}}$ (score error)
* Why it matters: This equation represents the score error, which measures the difference between the predicted and true scores.

### Equation 5: $\mathrm{DTC}(X_{0})$

* Equation: $\mathrm{DTC}(X_{0})$
* Symbols: $\mathrm{DTC}(X_{0})$ (dual total correlation at $X_{0}$)
* Why it matters: This equation represents the dual total correlation at the initial state $X_{0}$, which is used to bound the number of discretization steps required to achieve a certain level of accuracy.

**Method Summary**
==================

* The authors propose a provably adaptive sampling algorithm for uniform and remasking discrete diffusion models.
* The algorithm uses a first-order sampler based on the leave-one-out denoiser and corrects denoising mistakes during the sampling process.
* The authors establish an adaptive sampling guarantee, which depends on the dual total correlation of the target distribution.

**Experimental Overview**
=========================

* The authors evaluate the proposed algorithm on a variety of tasks and datasets.
* The main claimed findings include:
	+ Improved sampling efficiency compared to existing algorithms.
	+ Adaptivity to the intrinsic dependence structure of the target distribution.

**What to Verify in the PDF**
=============================

* The authors provide a detailed proof of the adaptive sampling guarantee in Appendix C.
* The proof relies on several technical lemmas and propositions, which are not fully explained in the abstract.
* The authors also provide additional results and experiments in Appendix B and D, which may be of interest to readers.
{% endraw %}

{% raw %}
## 2) ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings
- **Authors:** Na Li, Yuchen Jiao, Changxiao Cai, Gen Li
- **arXiv:** [2608.23551](https://arxiv.org/abs/2608.23551v1) · [pdf](https://arxiv.org/pdf/2608.23551v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.23551v1))
- **Categories:** cs.CL, cs.AI, cs.LG, stat.ML

### Abstract
> Recent advances in continuous diffusion and flow-based language models (LMs) have achieved performance competitive with discrete LMs. However, existing continuous frameworks still rely on decoders supervised with cross entropy (CE) because the flow trajectories are not guaranteed to terminate at valid token embeddings. Motivated by this limitation, we introduce \textbf{ConvergeFlow}, an embedding-space flow-based LM, which constrains the data predictor to the convex hull of token embeddings and trains it solely with the mean squared error objective induced by flow matching. Under suitable regularity conditions, we prove that the resulting flow converges to valid token embeddings despite errors in the data predictor, enabling direct token prediction without a CE-supervised decoder. We further develop three sampling mechanisms for controlling the trade-off between the generative perplexity and entropy. Experiments on OpenWebText demonstrate that ConvergeFlow achieves performance competitive with existing continuous and discrete diffusion LMs. These findings demonstrate the potential of the flow-based paradigm for language modeling. Our code is available at https://github.com/Na-Li66/ConvergeFlow.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 5.44

* Equation: `5.44`
* Symbols: `p_{0}`, `x^{t_k}`, `μ^θ(x^{t_k}, t_k)`
* Why it matters: This equation is not explicitly mentioned in the context, but it seems to be related to the flow-based language model. Without more information, it's difficult to provide further context.

### Equation 2: 33.17

* Equation: `33.17`
* Symbols: `p_{0}`, `x^{t_k}`, `μ^θ(x^{t_k}, t_k)`
* Why it matters: Similar to Equation 1, this equation is not explicitly mentioned in the context. It's unclear what this equation represents or how it relates to the flow-based language model.

### Equation 3: \downarrow

* Equation: `\downarrow`
* Symbols: `x^{t_k}`, `μ^θ(x^{t_k}, t_k)`
* Why it matters: This equation represents a downward arrow, which could indicate a decrease in some quantity. However, without more context, it's difficult to determine what this equation represents or how it relates to the flow-based language model.

### Equation 4: \uparrow

* Equation: `\uparrow`
* Symbols: `x^{t_k}`, `μ^θ(x^{t_k}, t_k)`
* Why it matters: This equation represents an upward arrow, which could indicate an increase in some quantity. Like Equation 3, without more context, it's difficult to determine what this equation represents or how it relates to the flow-based language model.

### Equation 5: p_{0}

* Equation: `p_{0}`
* Symbols: `p_{0}`, `x^{t_k}`, `μ^θ(x^{t_k}, t_k)`
* Why it matters: This equation represents the initial distribution `p_{0}`. It's likely used as a reference point for the flow-based language model, but without more context, it's difficult to provide further information.

**Method Summary**
==================

* The authors introduce ConvergeFlow, an embedding-space flow-based language model that constrains the data predictor to the convex hull of token embeddings.
* The model is trained solely with the mean squared error objective induced by flow matching.
* The authors prove that the resulting flow converges to valid token embeddings despite errors in the data predictor.
* The model achieves performance competitive with existing continuous and discrete diffusion language models.

**Experimental Overview**
========================

* The authors conduct experiments on the OpenWebText dataset, which contains approximately 9B tokens.
* The experiments use a DiT-style Transformer architecture with 12 layers, a hidden dimension of 768, and 12 attention heads.
* The authors compare the performance of ConvergeFlow with existing continuous and discrete diffusion language models.
* The main claimed finding is that ConvergeFlow achieves performance competitive with existing models.

**What to Verify in the PDF**
=============================

* The authors mention that the code is available at https://github.com/Na-Li66/ConvergeFlow, but it's unclear what specific details are missing from the paper.
* The authors discuss the effect of the training objective (MSE versus CE) on the model's performance, but it's unclear what specific details are missing from the paper.
* The authors provide additional experimental results in Appendix B, but it's unclear what specific details are missing from the paper.
{% endraw %}

{% raw %}
## 3) Inertial Manifold Neural Operator for Dissipative Time-Dependent Partial Differential Equations
- **Authors:** Xiaoyang Xie, Clarence W. Rowley
- **arXiv:** [2608.23546](https://arxiv.org/abs/2608.23546v1) · [pdf](https://arxiv.org/pdf/2608.23546v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.23546v1))
- **Categories:** math.NA, cs.LG, math.DS

### Abstract
> In this paper, we introduce the Inertial Manifold Neural Operator (IMNO) for solving dissipative time-dependent partial differential equations (PDEs). The long-time dynamics of such systems often exhibit an effective low-dimensional structure due to dissipation. Unlike standard neural operator architectures such as the Fourier Neural Operator (FNO), IMNO explicitly leverages the low-dimensional structure to achieve better physical interpretability, accuracy, and stability in long-horizon autoregressive training and prediction for nonlinear dissipative PDEs. For shift-equivariant PDEs, we further introduce a shift-equivariant variant (IMNO-SE) of the proposed neural operator, ensuring that a spatial shift in the input induces the same spatial shift in the output. This symmetry-preserving inductive bias substantially improves its performance in shift-equivariant PDEs. Extensive benchmark experiments are presented to evaluate IMNO's performance numerically.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\Omega \subset \mathbb{R}^{d}$

* Equation: $\Omega \subset \mathbb{R}^{d}$
* Symbols: $\Omega$, $\mathbb{R}^{d}$
* Why it matters: Defines the spatial domain of the problem.

### Equation 2: $\Omega$

* Equation: $\Omega$
* Symbols: $\Omega$
* Why it matters: Same as Equation 1, defines the spatial domain of the problem.

### Equation 3: $u(t) \in H$

* Equation: $u(t) \in H$
* Symbols: $u(t)$, $H$
* Why it matters: Defines the space of functions that the solution $u(t)$ belongs to.

### Equation 4: $S(t): H \to H, u_{0} \mapsto u(t; u_{0})$

* Equation: $S(t): H \to H, u_{0} \mapsto u(t; u_{0})$
* Symbols: $S(t)$, $H$, $u_{0}$, $u(t; u_{0})$
* Why it matters: Defines the solution operator that maps the initial condition $u_{0}$ to the solution $u(t; u_{0})$ at time $t$.

### Equation 5: $u(t; u_{0})$

* Equation: $u(t; u_{0})$
* Symbols: $u(t; u_{0})$
* Why it matters: Same as Equation 4, defines the solution operator.

### Equation 6: $u_{0}$

* Equation: $u_{0}$
* Symbols: $u_{0}$
* Why it matters: Defines the initial condition of the problem.

### Equation 7: $\Delta t > 0$

* Equation: $\Delta t > 0$
* Symbols: $\Delta t$
* Why it matters: Defines the time step size for the numerical solution.

### Equation 8: $\mathcal{G}: H \to H, \mathcal{G}(u) = S(\Delta t)u$

* Equation: $\mathcal{G}: H \to H, \mathcal{G}(u) = S(\Delta t)u$
* Symbols: $\mathcal{G}$, $H$, $u$, $S(\Delta t)$
* Why it matters: Defines the operator that maps the solution $u$ to the solution at time $\Delta t$.

**Method Summary**
================

* The Inertial Manifold Neural Operator (IMNO) is introduced for solving dissipative time-dependent partial differential equations (PDEs).
* IMNO explicitly leverages the low-dimensional structure of the system to achieve better physical interpretability, accuracy, and stability.
* A shift-equivariant variant (IMNO-SE) of the proposed neural operator is introduced for shift-equivariant PDEs.
* Extensive benchmark experiments are presented to evaluate IMNO's performance numerically.

**Experimental Overview**
=====================

* Tasks/Datasets: The performance of IMNO and its shift-equivariant variant (IMNO-SE) is evaluated on the Burgers, nonlocal Burgers, Kuramoto–Sivashinsky, and Navier–Stokes equations.
* Baselines/Comparisons: FNO and RNO baselines are used for comparison.
* Main Claimed Findings: IMNO outperforms FNO and RNO in terms of accuracy and stability for nonlinear dissipative PDEs.

**What to Verify in the PDF**
==========================

* The proof of the universal approximation theorem of Fourier neural operators.
* The implementation details of the numerical experiments, including the choice of Fourier modes, channel width, and activation functions.
* The theoretical analysis of the stability and accuracy of IMNO and IMNO-SE.
{% endraw %}

{% raw %}
## 4) Interpretable AI with Local Distillation
- **Authors:** Erin Craig, Yiling Huang, Snigdha Panigrahi
- **arXiv:** [2608.23538](https://arxiv.org/abs/2608.23538v1) · [pdf](https://arxiv.org/pdf/2608.23538v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.23538v1))
- **Categories:** stat.ME, cs.LG, stat.ML

### Abstract
> Modern AI models such as tabular foundation models and gradient-boosted ensembles can outpredict classical methods, but provide little basis for reasoning about their predictions. High-stakes decisions call for models that are both accurate and interpretable as built. Local linear modeling offers a path forward: a smooth regression function is locally well approximated by a linear one, allowing a linear fit near each query point to achieve high accuracy without sacrificing transparency. The challenges lie in learning what is "local" and developing statistical tools for interpretation. Here, we propose local distillation, in which a black-box "teacher" guides a regularized linear "student" model at each query point. The teacher (1) defines locality by upweighting training observations with similar predicted outcomes, and (2) anchors the fit with its prediction at the query point, included as a pseudo-observation whose weight is estimated from the data. For interpretation, we add a small amount of Gaussian randomization to the local objective and use refits to assess stability: selection frequencies identify reliable features at a query point, and clustering the randomized fits identifies stable subgroups across the data. Under the lasso penalty, we prove that this randomization yields feature-selection probabilities that are stable under small perturbations of the training responses. Across 17 benchmark datasets, local distillation nearly matches its AI teacher's accuracy while producing a sparse linear model at each test point. In a high-dimensional cancer gene expression example, the framework identifies patient subgroups whose local models use different genes; this heterogeneity is invisible to a global linear model, and difficult to surface in a black-box model.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `X ∈ ℝ^{n×p}`

* Equation: `X ∈ ℝ^{n×p}`
* Symbols: `X`, `n`, `p`
* Why it matters: This equation defines the input matrix `X` as a real-valued matrix with `n` rows and `p` columns.

### Equation 2: `y ∈ ℝ^{n}`

* Equation: `y ∈ ℝ^{n}`
* Symbols: `y`, `n`
* Why it matters: This equation defines the response vector `y` as a real-valued vector with `n` elements.

### Equation 3: `x^{*}`

* Equation: `x^{*}`
* Symbols: `x^{*}`
* Why it matters: This equation defines a query point `x^{*}` without a specific value or meaning in the context of the paper.

### Equation 4: `hat(φ): ℝ^{p} → ℝ`

* Equation: `hat(φ): ℝ^{p} → ℝ`
* Symbols: `hat(φ)`, `φ`, `p`
* Why it matters: This equation defines a function `hat(φ)` that maps a real-valued vector `φ` of length `p` to a real-valued scalar.

### Equation 5: `hat(β) = argmin_{β} ...`

* Equation: `hat(β) = argmin_{β} ...`
* Symbols: `hat(β)`, `β`, `n`, `μ`, `S`, `S_{j}`
* Why it matters: This equation defines the optimization problem for finding the coefficients `β` that minimize the loss function, which involves the regularization term `μ` and the selection probabilities `S_{j}`.

**Method Summary**
================

* The proposed method, Local Distillation, uses a teacher model to generate a set of local linear models, each trained on a specific subset of the input features.
* The method aims to provide a more interpretable and transparent model by learning a smooth regression function that is locally well approximated by a linear one.
* The method uses a regularization term to encourage the selection of relevant features and a stability guarantee to ensure that the feature selection probabilities are robust to perturbations in the input responses.

**Experimental Overview**
=====================

* The authors evaluate the proposed method on 17 regression datasets, including the UCI Machine Learning Repository and the OpenML-CTR23 regression benchmark.
* The datasets span sample sizes `n ∈ [159, 4177]` and feature counts `p ∈ [5, 51]`.
* The authors compare the proposed method to several baselines, including:
	+ Student model (global lasso or ridge regression)
	+ Teacher model (TabPFN or XGBoost)
	+ Two local linear models (LOESS and local linear forests)
* The main claimed findings are that the proposed method outperforms the baselines in terms of accuracy and provides more interpretable results.

**What to Verify in the PDF**
==========================

* The authors claim that the feature selection probabilities are stable under small perturbations of the training response. Verify this claim by checking the proof of Theorem 1 and Corollary 1 in the appendix.
* The authors also claim that the method is robust to perturbations in the input responses. Verify this claim by checking the proof of Theorem 2 in the appendix.
* The authors provide a detailed analysis of the theoretical results, including the proof of Theorem 1 and Corollary 1. Verify that the proof is correct and that the results are consistent with the claimed findings.
{% endraw %}

{% raw %}
## 5) Strong Averaging Principle and Long-Time Dynamics for Fast-Slow SDEs with Increasing Time-Scale Separation and Degenerate Noise
- **Authors:** Sebastian Kassing, Asuto Miwa
- **arXiv:** [2608.23462](https://arxiv.org/abs/2608.23462v1) · [pdf](https://arxiv.org/pdf/2608.23462v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.23462v1))
- **Categories:** math.PR, math.OC, stat.ML

### Abstract
> We establish a strong averaging principle for fast-slow stochastic differential equations with a time-dependent scale-separation parameter $(\varepsilon_t)_{t \geq 0}$ satisfying $\varepsilon_t \to 0$ as $t \to \infty$. In contrast to approaches based on noise-induced smoothing or elliptic regularity, our approach relies on dissipativity of the frozen fast dynamics and therefore permits degenerate diffusion coefficients. We prove a maximal $L^p$-estimate between the slow variable and the averaged ODE at late times, with the classical strong convergence rate of order $1/2$. Under an additional decay condition on $(\varepsilon_t)_{t \ge 0}$, this estimate implies that the slow variable is almost surely an asymptotic pseudo-trajectory of the averaged ODE. As a consequence, we obtain criteria for the identification of possible limit points and for convergence toward asymptotically stable equilibria for the slow variable by analyzing the dynamical behavior of the averaged equation.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### 1. (\varepsilon_{t})_{t\geq 0}

* Equation: Time-dependent scale-separation parameter
* Symbols: εt, t ≥ 0
* Why it matters: Represents the time-dependent scaling factor for the fast dynamics

### 2. \varepsilon_{t}\to 0

* Equation: Limit of the time-dependent scale-separation parameter as t → ∞
* Symbols: εt, t → ∞
* Why it matters: Indicates the asymptotic behavior of the fast dynamics as time increases

### 3. t\to\infty

* Equation: Time variable
* Symbols: t
* Why it matters: Represents the time axis for the stochastic differential equation

### 4. L^{p}

* Equation: Lp norm
* Symbols: Lp, p
* Why it matters: Used to establish a maximal Lp-estimate between the slow variable and the averaged ODE

### 5. f:{\mathbb{R}}^{d_{1}+d_{2}}\to{\mathbb{R}}^{d_{1}}

* Equation: Function from R^{d1+d2} to R^d1
* Symbols: f, d1, d2
* Why it matters: Represents the fast dynamics of the system

**Method Summary**
==================

* The authors establish a strong averaging principle for fast-slow stochastic differential equations with increasing time-scale separation and degenerate noise.
* The approach relies on dissipativity of the frozen fast dynamics, allowing for degenerate diffusion coefficients.
* The method provides a maximal Lp-estimate between the slow variable and the averaged ODE at late times, with a classical strong convergence rate of order 1/2.

**Experimental Overview**
=========================

* Tasks/Datasets: Not explicitly mentioned in the extracted context.
* Baselines/Comparisons: Not mentioned in the extracted context.
* Main Claimed Findings: The authors establish a strong averaging principle and a maximal Lp-estimate for fast-slow SDEs with increasing time-scale separation and degenerate noise.

**What to Verify in the PDF**
=============================

* The proof of Theorem 1.5 using the Poisson equation.
* The moment bounds and ergodicity of the frozen fast equation under the dissipativity and regularity assumptions.
* The well-definedness of the Poisson equation and the regularity results for the Poisson equation.
{% endraw %}
