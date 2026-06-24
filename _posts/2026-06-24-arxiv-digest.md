---
layout: post
title: "Daily arXiv Digest — 2026-06-24 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) New Bounds for the Last Iterate of the Stochastic subGradient Method
- **Authors:** Guglielmo Beretta, Tommaso Cesari, Roberto Colomboni, Andrea Paudice
- **arXiv:** [2606.24879](https://arxiv.org/abs/2606.24879v1) · [pdf](https://arxiv.org/pdf/2606.24879v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.24879v1))
- **Categories:** math.OC, cs.LG

### Abstract
> We study the last iterate of the stochastic subgradient method for one-dimensional convex Lipschitz objectives. For a fixed horizon $n$, we consider the standard fixed stepsizes $η=Θ(1/\sqrt n)$. We prove that, for such stepsize policies, under additive i.i.d. subgradient noise with uniformly bounded variance, the last iterate features an optimization error of order $1/\sqrt n$, thereby removing the extra $(\log n)$ factor present in existing generic bounds. On the other hand, we show that without the i.i.d. assumption, the optimization error can be of order $(\log n)/\sqrt n$. Thus, under the uniformly bounded variance assumption alone, the last iterate of SsGM is suboptimal even in dimension one, resolving negatively an open problem posed in Koren and Segal, COLT, 2020.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: η = Θ(1/√n)

* Equation: η = Θ(1/√n)
* Symbols: η (step size), n (natural number)
* Why it matters: This equation defines the step size policy used in the stochastic subgradient method, which is a key component of the algorithm.

### Equation 2: 1/√n

* Equation: 1/√n
* Symbols: n (natural number)
* Why it matters: This equation represents the order of the optimization error in the last iterate of the stochastic subgradient method.

### Equation 3: (log n)

* Equation: (log n)
* Symbols: n (natural number)
* Why it matters: This equation represents the order of the optimization error in the last iterate of the stochastic subgradient method without the i.i.d. assumption.

### Equation 4: (log n)/√n

* Equation: (log n)/√n
* Symbols: n (natural number)
* Why it matters: This equation represents the order of the optimization error in the last iterate of the stochastic subgradient method without the i.i.d. assumption.

### Equation 5: (η_i)_{1 ≤ i ≤ n} ≡ η

* Equation: (η_i)_{1 ≤ i ≤ n} ≡ η
* Symbols: η_i (subgradient noise), η (step size)
* Why it matters: This equation defines the subgradient noise used in the stochastic subgradient method.

**Method Summary**
==================

* The stochastic subgradient method is a first-order optimization algorithm that uses a fixed step size to iteratively update the solution.
* The algorithm is used to minimize a convex Lipschitz objective function.
* The method is sensitive to the choice of step size and subgradient noise.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors consider a one-dimensional convex Lipschitz objective function.
* Baselines/Comparisons: The authors compare the performance of the stochastic subgradient method with existing generic bounds.
* Main Claimed Findings: The authors prove that the last iterate of the stochastic subgradient method has an optimization error of order 1/√n under the i.i.d. assumption, and (log n)/√n without the i.i.d. assumption.

**What to Verify in the PDF**
=============================

* The authors' proof of the optimization error bound for the stochastic subgradient method.
* The assumptions made in the proof, such as the i.i.d. assumption on the subgradient noise.
* The implications of the results for the stochastic subgradient method in practice.
{% endraw %}

{% raw %}
## 2) Real vs. Complex Spectral Bases for Neural Operators: The Role of Green's Function Alignment
- **Authors:** Jason Sulskis, Sathya Ravi
- **arXiv:** [2606.24851](https://arxiv.org/abs/2606.24851v1) · [pdf](https://arxiv.org/pdf/2606.24851v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.24851v1))
- **Categories:** cs.LG

### Abstract
> Fourier Neural Operators (FNO) learn solution operators of partial differential equations by parameterizing global convolutions in the complex Fourier domain. For real-valued PDE solutions, the complex FFT carries representational redundancy through conjugate symmetry. We introduce the Hartley Neural Operator (HNO), the exact real-valued mirror of FNO: it replaces the FFT with the purely real Discrete Hartley Transform and learns a single real multiplier per retained spectral mode, with no complex arithmetic. Because the real Hartley spectrum is not halved by conjugate symmetry, HNO retains twice as many frequency corners as FNO but one real weight where FNO carries a complex pair, so the two operators are iso-parametric at equal width and differ only in spectral basis. Our central thesis is that the best basis is a property of the operator. Self-adjoint elliptic operators (Poisson, biharmonic) have real, symmetric Green's functions that the real Hartley multiplier diagonalizes exactly, and HNO is favored there. Time-dependent operators carry phase, from oscillation in the wave equation to transport in advection, Burgers, and Navier-Stokes, which a real diagonal multiplier cannot represent, so FNO is favored there, and increasingly so with the operator's phase content, leaving the phaseless heat equation as the borderline case. Training both operators identically and benchmarking across PDE classes, initial-condition families, and boundary conditions, we find an elliptic-versus-time-dependent split that is monotone in operator phase content and matches the Green's-function theory we develop. Rather than a universal winner, our findings give a predictive rule: match the spectral basis to the symmetry of the solution operator.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: f[n]
```markdown
f[n]
```
* Equation: Not provided
* Symbols: `f[n]` represents a function of `n`
* Why it matters: This equation is likely the output of the neural operator, representing a solution to a partial differential equation.

### Equation 2: H_{k}=\sum_{n=0}^{N-1}f[n]\cdot\mathrm{cas}\!\left(\frac{2\pi kn}{N}\right)
```markdown
H_{k}=\sum_{n=0}^{N-1}f[n]\cdot\mathrm{cas}\!\left(\frac{2\pi kn}{N}\right)
```
* Equation: Hartley transform of the function `f[n]`
* Symbols:
	+ `H_{k}`: Hartley transform of `f[n]` at frequency `k`
	+ `f[n]`: function of `n`
	+ `cas(\theta)`: cosine and sine functions
	+ `k`: frequency
	+ `N`: number of samples
* Why it matters: This equation represents the Hartley transform of the function `f[n]`, which is used in the Hartley Neural Operator.

### Equation 3: \mathrm{cas}(\theta)=\cos(\theta)+\sin(\theta)
```markdown
\mathrm{cas}(\theta)=\cos(\theta)+\sin(\theta)
```
* Equation: Definition of the cosine and sine functions
* Symbols:
	+ `cas(\theta)`: cosine and sine functions
	+ `\theta`: angle
* Why it matters: This equation defines the cosine and sine functions, which are used in the Hartley transform.

### Equation 4: H\{f\}(k)=\mathrm{Re}\{F\{f\}(k)\}-\mathrm{Im}\{F\{f\}(k)\}
```markdown
H\{f\}(k)=\mathrm{Re}\{F\{f\}(k)\}-\mathrm{Im}\{F\{f\}(k)\}
```
* Equation: Real-valued Hartley transform of `f[k]`
* Symbols:
	+ `H\{f\}(k)`: real-valued Hartley transform of `f[k]`
	+ `F\{f\}(k)`: complex-valued Fourier transform of `f[k]`
	+ `Re`: real part
	+ `Im`: imaginary part
* Why it matters: This equation represents the real-valued Hartley transform of `f[k]`, which is used in the Hartley Neural Operator.

### Equation 5: \mathrm{Re}-\mathrm{Im}
```markdown
\mathrm{Re}-\mathrm{Im}
```
* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation is likely used to separate the real and imaginary parts of a complex-valued function.

### Equation 6: x\circledast y
```markdown
x\circledast y
```
* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation is likely used to represent the convolution of two functions.

### Equation 7: Z_{k}=\frac{1}{2}\left[X_{k}(Y_{k}+Y_{-k})+X_{-k}(Y_{k}-Y_{-k})\right]
```markdown
Z_{k}=\frac{1}{2}\left[X_{k}(Y_{k}+Y_{-k})+X_{-k}(Y_{k}-Y_{-k})\right]
```
* Equation: Not provided
* Symbols:
	+ `Z_{k}`: not provided
	+ `X_{k}`: not provided
	+ `Y_{k}`: not provided
	+ `Y_{-k}`: not provided
* Why it matters: This equation is likely used to represent a specific operation or transformation.

### Equation 8: Y_{-k}=Y_{N-k\bmod N}
```markdown
Y_{-k}=Y_{N-k\bmod N}
```
* Equation: Not provided
* Symbols:
	+ `Y_{-k}`: not provided
	+ `Y_{N-k\bmod N}`: not provided
* Why it matters: This equation is likely used to represent a specific operation or transformation.

**Method Summary**
==================

* The authors propose two neural operators: the Fourier Neural Operator (FNO) and the Hartley Neural Operator (HNO).
* FNO uses the complex Fourier transform, while HNO uses the real Hartley transform.
* The authors train both operators with an identical optimizer, schedule, and regularization.
* The choice of spectral basis affects the optimization landscape for learning elliptic Green's functions.
* The authors develop a theoretical framework to justify the empirical observation that HNO outperforms FNO on elliptic PDEs.

**Experimental Overview**
========================

* The authors evaluate HNO against FNO across five classes of canonical PDEs: parabolic, hyperbolic, advective, nonlinear, and elliptic.
* The authors test three initial-condition families and both periodic and homogeneous Dirichlet boundary conditions.
* The authors report the relative L2 error averaged over test samples and gradient error.
* The results divide cleanly along operator symmetry, and the division is monotone in phase content rather than binary.

**What to Verify in the PDF**
=============================

* The authors' theoretical framework for justifying the empirical observation that HNO outperforms FNO on elliptic PDEs.
* The optimization landscape geometry analysis for learning elliptic Green's functions.
* The computational setup and training procedures for both FNO and HNO.
* The results and findings presented in the paper, including the relative L2 error and gradient error.
{% endraw %}

{% raw %}
## 3) Grad Detect: Gradient-Based Hallucination Detection in LLMs
- **Authors:** Anand Kamat, Daniel Blake, Brent M. Werness
- **arXiv:** [2606.24790](https://arxiv.org/abs/2606.24790v1) · [pdf](https://arxiv.org/pdf/2606.24790v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.24790v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks, yet they remain prone to generating hallucinations. Detecting these hallucinations is critical for deploying LLMs reliably in high-stakes applications. We present Grad Detect, a gradient-based approach for predicting hallucinations by analyzing layer-wise gradient patterns from a single forward-backward pass during inference. Our method shows that the internal gradient structure of a model carries rich information about the correctness of its output. This information is not accessible through output-level signals alone. We evaluate Grad Detect on several Q&A benchmarks across both hallucination detection and model abstention prediction, where it consistently outperforms confidence-based and sampling-based baselines. Through comprehensive layer ablation studies across all eleven models from four architectural families, we find that the final five layers concentrate over 97% of the discriminative gradient signal, enabling efficient deployment with minimal performance loss. Grad Detect provides a unified framework for predicting multiple dimensions of LLM reliability, offering strong predictive performance alongside interpretable insights into where and how model failures originate.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: L × |C|

* Equation: L × |C|
* Symbols: L (number of layers), |C| (number of categories)
* Why it matters: This equation represents the total number of parameters in the model, which is a critical component in understanding the model's capacity to learn and generalize.

### Equation 2: r+, r-

* Equation: r+, r-
* Symbols: r+ (affirming response), r- (rejection response)
* Why it matters: These two responses represent the canonical behavioral modes of the model, which are used to compute the teacher-forced auto-regressive loss.

### Equation 3: F_i ∈ ℝ^(L × |C|)

* Equation: F_i ∈ ℝ^(L × |C|)
* Symbols: F_i (layer-wise gradients), L (number of layers), |C| (number of categories), ℝ (real numbers)
* Why it matters: This equation represents the layer-wise gradients of the model's parameters, which are used to compute the discriminative gradient signal.

### Equation 4: g_c,r^(l), c ∈ C

* Equation: g_c,r^(l), c ∈ C
* Symbols: g_c,r^(l) (category-specific reference gradients), c (category), C (set of categories)
* Why it matters: These gradients represent the reference gradients for each category, which are used to compute the cosine similarity features between per-sample gradients and each reference.

### Equation 5: f_θ

* Equation: f_θ
* Symbols: f_θ (auto-regressive language model), θ (model parameters)
* Why it matters: This equation represents the auto-regressive language model, which is used to compute the teacher-forced auto-regressive loss.

**Method Summary**
================

* **Gradient-based approach**: Grad Detect uses a gradient-based approach to predict hallucinations in LLMs.
* **Layer-wise gradients**: The method analyzes layer-wise gradients to capture the discriminative gradient signal.
* **Category-specific reference gradients**: The method uses category-specific reference gradients to compute cosine similarity features between per-sample gradients and each reference.
* **Lightweight transformer encoder**: The method uses a lightweight transformer encoder to classify the resulting low-dimensional feature matrix.

**Experimental Overview**
=====================

* **Tasks/Datasets**: The method is evaluated on four Q&A benchmarks: TriviaQA, SciQ, PopQA, and TruthfulQA.
* **Baselines/Comparisons**: The method is compared to confidence-based and sampling-based baselines.
* **Main Claimed Findings**: The method consistently outperforms baselines and achieves high accuracy across datasets, with the last 5 layers retaining 98-99% of full-model accuracy.
{% endraw %}

{% raw %}
## 4) Dirac-Frenkel dynamics with inertia for nonlinearly parametrized solutions of evolution problems
- **Authors:** Matteo Raviola, Benjamin Peherstorfer
- **arXiv:** [2606.24769](https://arxiv.org/abs/2606.24769v1) · [pdf](https://arxiv.org/pdf/2606.24769v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.24769v1))
- **Categories:** math.NA, cs.LG

### Abstract
> Even when Dirac-Frenkel dynamics determine a well-defined evolution in function space, the corresponding parameter dynamics can be non-unique or ill-conditioned for redundant nonlinear parametrizations such as neural networks or mixture models. We propose to add inertia to the Dirac-Frenkel dynamics and show that this allows useful parameter velocity information to persist from the past trajectory in directions that are weakly informed, while well-informed parameter velocity directions continue to follow the Dirac-Frenkel dynamics. We prove that the inertial formulation yields well-posed parameter dynamics and provide a posteriori error bounds. After time discretization, the method requires the solution of the same type of regularized linear least-squares problem as standard Dirac-Frenkel dynamics, but with the previous velocity appearing as an anchor. Numerical experiments demonstrate the increased robustness obtained with inertia.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\dot{u}(t) = F(u(t))$

* Equation: $\dot{u}(t) = F(u(t))$
* Symbols: $\dot{u}(t)$ (velocity), $u(t)$ (position), $F(u(t))$ (vector field)
* Why it matters: This equation describes the evolution of the system in function space.

### Equation 2: $\hat{u}(t) = \Phi(\theta(t))$

* Equation: $\hat{u}(t) = \Phi(\theta(t))$
* Symbols: $\hat{u}(t)$ (parameterized position), $\theta(t)$ (parameter), $\Phi(\theta(t))$ (parameterized position)
* Why it matters: This equation relates the parameterized position to the parameter.

### Equation 3: $\Theta$

* Equation: $\Theta$
* Symbols: $\Theta$ (parameter space)
* Why it matters: This equation defines the set of possible parameters.

### Equation 4: $\Phi: \Theta \to H$

* Equation: $\Phi: \Theta \to H$
* Symbols: $\Phi$ (parameterized position map), $\Theta$ (parameter space), $H$ (Hilbert space)
* Why it matters: This equation defines the mapping from parameters to positions.

### Equation 5: $\Phi$

* Equation: $\Phi$
* Symbols: $\Phi$ (parameterized position map)
* Why it matters: This equation is not explicitly defined, but it is mentioned as a mapping from parameters to positions.

### Equation 6: $\theta(t)$

* Equation: $\theta(t)$
* Symbols: $\theta(t)$ (parameter)
* Why it matters: This equation represents the parameter at time $t$.

### Equation 7: $\dot{\theta}(t)$

* Equation: $\dot{\theta}(t)$
* Symbols: $\dot{\theta}(t)$ (parameter velocity)
* Why it matters: This equation describes the evolution of the parameter.

### Equation 8: $J(\theta(t))\dot{\theta}(t)$

* Equation: $J(\theta(t))\dot{\theta}(t)$
* Symbols: $J(\theta(t))$ (Jacobian), $\dot{\theta}(t)$ (parameter velocity)
* Why it matters: This equation is used in the a posteriori error analysis of the DFI scheme.

**Method Summary**
================

* The authors propose adding inertia to the Dirac-Frenkel dynamics to improve the robustness of the parameter dynamics.
* The inertial formulation allows useful parameter velocity information to persist from the past trajectory in directions that are weakly informed.
* The method requires solving a regularized linear least-squares problem after time discretization.
* The authors provide a posteriori error bounds and demonstrate the increased robustness obtained with inertia.

**Experimental Overview**
=====================

* The authors demonstrate the DFI scheme on examples with the Allen-Cahn and Fokker-Planck equations.
* The tasks/datasets include:
	+ One-dimensional Allen-Cahn equation on the periodic domain [0, 2π)
	+ Fokker-Planck equation for a probability density on ℝ^10
* The baselines/comparisons include:
	+ Tikhonov-regularized Dirac-Frenkel dynamics
* The main claimed findings include:
	+ Increased robustness obtained with inertia
	+ Improved performance on the Allen-Cahn and Fokker-Planck equations

**What to Verify in the PDF**
==========================

* The authors claim that the inertial formulation yields well-posed parameter dynamics and provides a posteriori error bounds. Verify that these claims are supported by the mathematical analysis and numerical experiments.
* The authors use a fixed time step $h$ and a fixed parameter velocity $\eta$ over all time steps $k$. Verify that these assumptions are justified and that the results are not sensitive to these choices.
* The authors use a uniform periodic grid $x_0, \dots, x_{N_x-1}$ to approximate the inner product in space. Verify that this choice is reasonable and that the results are not sensitive to the choice of grid.
{% endraw %}

{% raw %}
## 5) A Concentration Inequality for the Covariance Matrix of an Arbitrary Subset of Random Vectors
- **Authors:** Huikang Liu, Peng Wang, Laura Balzano
- **arXiv:** [2606.24766](https://arxiv.org/abs/2606.24766v1) · [pdf](https://arxiv.org/pdf/2606.24766v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.24766v1))
- **Categories:** math.ST, math.OC

### Abstract
> Concentration inequalities for sample covariance matrices are fundamental tools in high-dimensional probability. Classical results typically assume that the selected random vectors are independent of the selection rule. In this paper, we study spectral concentration for sample covariance matrices formed from arbitrary, possibly data-dependent subsets of i.i.d. random vectors. Such data-dependent selection destroys the usual independence structure and makes standard covariance concentration bounds inapplicable. For i.i.d. Gaussian random vectors, we prove high-probability lower and upper bounds for the minimal and maximal eigenvalues of such selected covariance matrices. Compared with a direct union-bound argument, our results provide substantially sharper guarantees and allow much smaller subset proportions. We further discuss extensions from Gaussian to sub-Gaussian random vectors, and beyond independence to weakly dependent observations, with geometrically strong-mixing Gaussian sequences serving as a representative example of the latter. Finally, we apply the developed concentration inequalities to the K-subspace clustering problem under a low-rank Gaussian mixture model, where the optimal clusters are inherently data-dependent. Our results yield recovery guarantees showing that the clustering error of global minimizers decays polynomially with the signal-to-noise ratio.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Subset of Random Vectors
```math
\{\bm{a}_{i}\}_{i=1}^{M}\subseteq\mathbb{R}^{m}
```
* Symbols: `M`, `m`, `a_i` (i = 1 to M)
* Why it matters: Defines the set of random vectors used in the analysis.

### Equation 2: Positive Value
```math
\eta>0
```
* Symbols: `η` (eta)
* Why it matters: Serves as a parameter in the concentration inequality.

### Equation 3: Concentration Bound
```math
1-2\exp\left(-2\eta^{2}\right)
```
* Symbols: `η` (eta)
* Why it matters: Provides a concentration bound for the sample covariance matrix.

### Equation 4: Covariance Matrix Bound
```math
\displaystyle\left\|\frac{1}{M}\sum_{i=1}^{M}\bm{a}_{i}\bm{a}_{i}^{T}-\bm{I}_{m}\right\|\leq\frac{9(\sqrt{m}+\eta)}{\sqrt{M}}
```
* Symbols: `M`, `m`, `η` (eta), `a_i` (i = 1 to M), `I_m` (identity matrix in R^m)
* Why it matters: Establishes a bound on the covariance matrix of the sample covariance matrix.

### Equation 5: Percentage
```math
15\%
```
* Symbols: `%` (percent sign)
* Why it matters: Represents a specific percentage value used in the analysis.

### Equation 6: Random Vector
```math
\bm{a}\in\mathbb{R}^{d}
```
* Symbols: `a` (random vector), `d`
* Why it matters: Defines the dimensionality of the random vector.

### Equation 7: Norm
```math
\|\bm{a}\|
```
* Symbols: `a` (random vector), `||` (norm)
* Why it matters: Represents the norm of the random vector.

### Equation 8: L2 Norm
```math
\ell_{2}
```
* Symbols: `ell_2` (L2 norm)
* Why it matters: Represents the L2 norm of the random vector.

**Method Summary**
==================

* The K-subspace clustering problem aims to recover both the subspace bases and the cluster assignment from unlabeled samples.
* The analysis uses a data-dependent subset of Gaussian random vectors.
* The concentration inequalities are established for both Gaussian and sub-Gaussian random vectors.

**Experimental Overview**
========================

* Tasks:
	+ Simulate data from the Low-Rank Gaussian Mixture Model (LRGMM).
	+ Compute the recovery bound using the K-subspaces algorithm.
* Datasets:
	+ LRGMM with varying noise levels and fixed parameters (K = 2, n = 100, N1 = N2 = 500, d = 20, μmax = 0.67).
* Baselines/Comparisons:
	+ Wang2022: Thresholding inner-product spectral method.
* Main claimed findings:
	+ The recovery bound remains bounded and exhibits small variance across tested SNR values, suggesting a moderate unspecified constant.
{% endraw %}
