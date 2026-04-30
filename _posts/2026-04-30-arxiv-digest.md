---
layout: post
title: "Daily arXiv Digest — 2026-04-30 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Exact Dynamic Programming for Solow--Polasky Diversity Subset Selection on Lines and Staircases
- **Authors:** Michael T. M. Emmerich
- **arXiv:** [2604.26929](https://arxiv.org/abs/2604.26929v1) · [pdf](https://arxiv.org/pdf/2604.26929v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.26929v1))
- **Categories:** cs.CG, cs.DS, math.OC

### Abstract
> We study exact fixed-cardinality Solow--Polasky diversity subset selection on ordered finite $\ell_1$ sets, with monotone biobjective Pareto fronts and their higher-dimensional staircase analogues as central applications. Solow--Polasky diversity was introduced in biodiversity conservation, whereas the same inverse-matrix expression appears in metric geometry as magnitude: for a finite metric space $(X,d)$ with exponential similarity matrix $Z_{ij}=e^{-q d(x_i,x_j)}$, the quantity $\1^\top Z^{-1}\1$ is the magnitude of the scaled finite metric space $(X,qd)$ whenever the weighting is defined by the inverse matrix. Thus, in this finite exponential-kernel setting, Solow--Polasky diversity and magnitude are mathematically the same object viewed through different motivations. Building on the linear-chain magnitude formula of Leinster and Willerton, we provide a detailed proof of the scaled consecutive-gap identity $ \SP(X)=1+\sum_r \tanh(qg_r/2), $ where the $g_r$ are the gaps between consecutive selected points. We then prove an exact Bellman-recursion theorem for maximizing this value over all subsets of a prescribed cardinality, yielding an $O(kn^2)$ dynamic program for an ordered $n$-point candidate set and subset size $k$. Finally, we prove ordered $\ell_1$ reductions showing that the same algorithm applies to monotone biobjective Pareto-front approximations and, more generally, to finite coordinatewise monotone $\ell_1$ staircases in $\R^d$. These are precisely the ordered $\ell_1$ chains for which the Manhattan metric becomes a line metric along the chosen order, so the one-dimensional dynamic program applies without modification. Keywords: Dynamic Programming, Solow--Polasky Diversity, Complexity Theory, Multiobjective Optimization, Pareto front, Magnitude
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula walkthrough**
=====================

### Equation 1: ℓ1
ℓ1
This equation is not explicitly mentioned in the context. However, it is likely referring to the ℓ1 norm, which is a common norm used in machine learning and optimization.

### Equation 2: (X,d)
(X,d)
This equation is not explicitly defined in the context, but it is likely referring to a finite set X and a distance metric d.

### Equation 3: Z_{ij}=e^{-qd(x_{i},x_{j})}
Z_{ij}=e^{-qd(x_{i},x_{j})}
This equation defines the similarity matrix Z, where Z_{ij} is the similarity between points x_i and x_j, and q is a parameter that controls the similarity.

### Equation 4: \mathbf{1}^{\top}Z^{-1}\mathbf{1}
\mathbf{1}^{\top}Z^{-1}\mathbf{1}
This equation is the magnitude of the scaled finite metric space (X, qd), where \mathbf{1} is a vector of ones, Z^{-1} is the inverse of the similarity matrix Z, and q is the parameter from Equation 3.

### Equation 5: (X,qd)
(X,qd)
This equation is not explicitly defined in the context, but it is likely referring to a scaled finite metric space (X, qd), where X is a set, q is a parameter, and d is a distance metric.

### Equation 6: \mathrm{SP}(X)=1+\sum_{r}\tanh(qg_{r}/2)
\mathrm{SP}(X)=1+\sum_{r}\tanh(qg_{r}/2)
This equation defines the Solow-Polasky diversity value SP(X), which is a sum of hyperbolic tangents over the gaps between consecutive selected points.

### Equation 7: g_{r}
g_{r}
This equation defines the gap between consecutive selected points, where g_r = x_{r+1} - x_r.

### Equation 8: O(kn^{2})
O(kn^{2})
This equation states that the dynamic program for fixed-cardinality subset selection has a time complexity of O(kn^2).

**Method summary**
================

* The paper presents an exact dynamic programming algorithm for Solow-Polasky diversity subset selection on lines and staircases.
* The algorithm has a time complexity of O(kn^2) for an ordered n-point candidate set and subset size k.
* The algorithm can be applied to monotone biobjective Pareto-front approximations and finite coordinatewise monotone ℓ1 staircases.
* The paper establishes a connection between Solow-Polasky diversity and magnitude of scaled finite metric spaces.

**Experimental overview**
=====================

* The paper does not provide any experimental results or datasets.
* The main claimed finding is the existence of an exact dynamic programming algorithm for Solow-Polasky diversity subset selection.

**What to verify in the PDF**
==========================

* The proof of the consecutive-gap formula on the line (Section 3).
* The proof of the Bellman-recursion theorem for fixed-cardinality subset selection (Section 4).
* The ordered ℓ1 Pareto-front reduction (Section 5).
* The higher-dimensional characterization of the algorithm (Section 6).
{% endraw %}

{% raw %}
## 2) Learning Over-Relaxation Policies for ADMM with Convergence Guarantees
- **Authors:** Junan Lin, Paul J. Goulart, Luca Furieri
- **arXiv:** [2604.26932](https://arxiv.org/abs/2604.26932v1) · [pdf](https://arxiv.org/pdf/2604.26932v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.26932v1))
- **Categories:** math.OC, cs.LG

### Abstract
> The Alternating Direction Method of Multipliers (ADMM) is a widely used method for structured convex optimization, and its practical performance depends strongly on the choice of penalty and relaxation parameters. Motivated by settings such as Model Predictive Control (MPC), where one repeatedly solves related optimization problems with fixed structure and changing parameter values, we propose learning online updates of the relaxation parameter to improve performance on problem classes of interest. This choice is computationally attractive in OSQP-like architectures, since adapting relaxation does not trigger the matrix refactorizations associated with penalty updates. We establish convergence guarantees for ADMM with time-varying penalty and relaxation parameters under mild assumptions, and show on benchmark quadratic programs that the resulting learned policies improve both iteration count and wall-clock time over baseline OSQP.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Minimization Problem
```math
\displaystyle\min_{x,z}
```
* Symbols: `x` and `z` are variables.
* Matters: This equation represents the minimization problem, which is the core of the optimization process.

### Equation 2: Objective Function
```math
\displaystyle f(x)+g(z)
```
* Symbols: `f(x)` and `g(z)` are functions.
* Matters: This equation represents the objective function, which is the function to be minimized.

### Equation 3: Constraint
```math
\displaystyle Ax+Bz=c,
```
* Symbols: `A`, `B`, and `c` are matrices and vectors.
* Matters: This equation represents the constraint, which is a fundamental aspect of optimization problems.

### Equation 4: Variable Constraints
```math
x\in\mathbb{R}^{n}
```
* Symbols: `x` is a variable, `n` is the dimension of the variable.
* Matters: This equation represents the variable constraints, which limit the possible values of the variables.

### Equation 5: Variable Constraints (continued)
```math
z\in\mathbb{R}^{m}
```
* Symbols: `z` is a variable, `m` is the dimension of the variable.
* Matters: This equation represents the variable constraints, which limit the possible values of the variables.

**Method Summary**
==================

* The proposed method learns online updates of the relaxation parameter to improve performance on problem classes of interest.
* The method adapts the ADMM relaxation parameter online while preserving convergence guarantees, even in the presence of updates for the penalty parameter.
* The method is compatible with existing adaptive penalty rules, such as OSQP's adaptive-ρ heuristic.
* The method is computationally attractive in OSQP-like architectures, as adapting relaxation does not trigger matrix refactorizations associated with penalty updates.

**Experimental Overview**
=========================

* Tasks/Datasets: The proposed method is evaluated on benchmark quadratic program families from the OSQP benchmark suite and a Model Predictive Control (MPC) benchmark.
* Baselines/Comparisons: The proposed method is compared to OSQP's adaptive-ρ heuristic.
* Main Claimed Findings: The proposed method improves both iteration count and wall-clock time over the baseline OSQP.

**What to Verify in the PDF**
=============================

* The mathematical proof of the convergence guarantees for the proposed method.
* The detailed analysis of the summable-change conditions for the relaxation and penalty parameter sequences.
* The experimental results for the MPC benchmark, including the initial state and fixed parameters.
{% endraw %}

{% raw %}
## 3) Uncertainty-Aware Predictive Safety Filters for Probabilistic Neural Network Dynamics
- **Authors:** Bernd Frauenknecht, Lukas Kesper, Daniel Mayfrank, Henrik Hose, Sebastian Trimpe
- **arXiv:** [2604.26836](https://arxiv.org/abs/2604.26836v1) · [pdf](https://arxiv.org/pdf/2604.26836v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.26836v1))
- **Categories:** cs.LG, eess.SY

### Abstract
> Predictive safety filters (PSFs) leverage model predictive control to enforce constraint satisfaction during deep reinforcement learning (RL) exploration, yet their reliance on first-principles models or Gaussian processes limits scalability and broader applicability. Meanwhile, model-based RL (MBRL) methods routinely employ probabilistic ensemble (PE) neural networks to capture complex, high-dimensional dynamics from data with minimal prior knowledge. However, existing attempts to integrate PEs into PSFs lack rigorous uncertainty quantification. We introduce the Uncertainty-Aware Predictive Safety Filter (UPSi), a PSF that provides rigorous safety predictions using PE dynamics models by formulating future outcomes as reachable sets. UPSi introduces an explicit certainty constraint that prevents model exploitation and integrates seamlessly into common MBRL frameworks. We evaluate UPSi within Dyna-style MBRL on standard safe RL benchmarks and report substantial improvements in exploration safety over prior neural network PSFs while maintaining performance on par with standard MBRL. UPSi bridges the gap between the scalability and generality of modern MBRL and the safety guarantees of predictive safety filters.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: \dagger

* Equation: Not provided in the extracted context.
* Symbols: Not provided in the extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: \bullet

* Equation: Not provided in the extracted context.
* Symbols: Not provided in the extracted context.
* Why it matters: Not found in extracted context.

### Equation 3: \mathbb{S}

* Equation: Not provided in the extracted context.
* Symbols: \mathbb{S} (set of states)
* Why it matters: Represents the set of all possible states in the environment.

### Equation 4: \mathbb{C}

* Equation: Not provided in the extracted context.
* Symbols: \mathbb{C} (set of certain states)
* Why it matters: Represents the set of certain states that can be reached by the controller.

### Equation 5: \mathcal{M}=\{\mathcal{S},\mathcal{A},r,p,\mathbb{I},\gamma\}

* Equation: Not provided in the extracted context.
* Symbols:
	+ \mathcal{S} (set of states)
	+ \mathcal{A} (set of actions)
	+ r (reward function)
	+ p (transition model)
	+ \mathbb{I} (initial state)
	+ \gamma (discount factor)
* Why it matters: Represents the model-free Markov decision process.

**Method Summary**
==================

* The authors propose the Uncertainty-Aware Predictive Safety Filter (UPSi) for probabilistic neural network dynamics.
* UPSi integrates a probabilistic ensemble (PE) model into predictive safety filters (PSFs) to provide rigorous safety predictions.
* The authors evaluate UPSi on standard safe RL benchmarks and report improvements in exploration safety over prior neural network PSFs.
* UPSi maintains performance on par with standard model-based RL (MBRL) methods.

**Experimental Overview**
========================

* Tasks/Datasets: Standard safe RL benchmarks (e.g., Cartpole, Pendulum, Drone).
* Baselines/Comparisons: Prior neural network PSFs, MBRL methods (e.g., MBPO).
* Main claimed findings: UPSi improves exploration safety while maintaining performance on par with MBRL methods.

**What to Verify in the PDF**
=============================

* The authors claim that the reachable set computation of UPSi is a consistent overapproximation of the true reachable sets.
* The authors claim that UPSi reduces constraint violations compared to prior PE-based PSFs.
* The authors claim that UPSi employs a sampling-based scheme to approximate the terminal set expansion.
* The authors claim that the expansion of the terminal set must remain highly conservative to ensure safety.
{% endraw %}

{% raw %}
## 4) Language Diffusion Models are Associative Memories Capable of Retrieving Unseen Data
- **Authors:** Bao Pham, Mohammed J. Zaki, Luca Ambrogioni, Dmitry Krotov, Matteo Negri
- **arXiv:** [2604.26841](https://arxiv.org/abs/2604.26841v1) · [pdf](https://arxiv.org/pdf/2604.26841v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.26841v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> When do language diffusion models memorize their training data, and how to quantitatively assess their true generative regime? We address these questions by showing that Uniform-based Discrete Diffusion Models (UDDMs) fundamentally behave as Associative Memories (AMs) $\textit{with emergent creative capabilities}$. The core idea of an AM is to reliably recover stored data points as $\textit{memories}$ by establishing distinct basins of attraction around them. Historically, models like Hopfield networks use an explicit energy function to guarantee these stable attractors. We broaden this perspective by leveraging the observation that energy is not strictly necessary, as basins of attraction can also be formed via conditional likelihood maximization. By evaluating token recovery of $\textit{training}$ and $\textit{test}$ examples, we identify in UDDMs a sharp memorization-to-generalization transition governed by the size of the training dataset: as it increases, basins around training examples shrink and basins around unseen test examples expand, until both later converge to the same level. Crucially, we can detect this transition using only the conditional entropy of predicted token sequences: memorization is characterized by vanishing conditional entropy, while in the generalization regime the conditional entropy of most tokens remains finite. Thus, conditional entropy offers a practical probe for the memorization-to-generalization transition in deployed models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `t=0.2`

* Equation: `t=0.2`
* Symbols: `t` (time)
* Why it matters: This equation represents a specific time point in the diffusion process.

### Equation 2: `{x} ∈ ℋ`

* Equation: `{x} ∈ ℋ`
* Symbols: `{x}` (token), `ℋ` (vocabulary)
* Why it matters: This equation defines the set of all possible tokens in the vocabulary.

### Equation 3: `q_data`

* Equation: `q_data`
* Symbols: `q_data` (data distribution)
* Why it matters: This equation represents the data distribution used in the Uniform-State Discrete Diffusion Model.

### Equation 4: `ℒ = {x ∈ {0, 1}^K : ∑i=1^K xi = 1}`

* Equation: `ℒ = {x ∈ {0, 1}^K : ∑i=1^K xi = 1}`
* Symbols: `ℒ` (vocabulary), `x` (token), `K` (number of tokens)
* Why it matters: This equation defines the set of all possible tokens in the vocabulary, where each token is a binary vector of length `K`.

### Equation 5: `z_t ∼ q_t(x; α_t) = Cat(z_t; α_t⋅x + (1-α_t)π)`

* Equation: `z_t ∼ q_t(x; α_t) = Cat(z_t; α_t⋅x + (1-α_t)π)`
* Symbols: `z_t` (perturbed token), `q_t` (conditional distribution), `α_t` (diffusion parameter), `x` (token), `π` (prior distribution), `Cat` (categorical distribution)
* Why it matters: This equation represents the conditional distribution of the perturbed token `z_t` given the token `x` and the diffusion parameter `α_t`. The categorical distribution `Cat` is used to model the binary nature of the tokens.

**Method Summary**
================

* The Uniform-State Discrete Diffusion Model (UDDM) is a type of generative model that uses a sequence of Markov states to model the diffusion process.
* The model uses a conditional sampling approach to generate new tokens, where the conditional distribution of each token is modeled using a categorical distribution.
* The model is trained on a dataset and uses the data distribution to initialize the prior distribution `π`.
* The diffusion parameter `α_t` is used to control the amount of noise added to each token during the diffusion process.
* The model is evaluated on its ability to recover training and test examples, and the results show that the model exhibits a memorization-to-generalization transition as the training dataset size increases.

**Experimental Overview**
=====================

* Tasks/Datasets: The model is evaluated on its ability to recover training and test examples from a dataset of binary tokens.
* Baselines/Comparisons: The model is compared to a baseline model that does not use the UDDM approach.
* Main Claimed Findings: The model exhibits a memorization-to-generalization transition as the training dataset size increases, where the model recovers training examples more accurately for small datasets and generalizes better for larger datasets.

**What to Verify in the PDF**
==========================

* The mathematical derivation of the categorical distribution `Cat` and its properties.
* The implementation details of the UDDM model, including the choice of hyperparameters and the training procedure.
* The results of the experiments, including the recovery rates for training and test examples, and the basins of attraction around these examples.
{% endraw %}

{% raw %}
## 5) Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding
- **Authors:** Hayate Iso, Tiyasa Mitra, Sudipta Mondal, Rasoul Shafipour, Venmugil Elango, Terry Kong, Yuki Huang, Seonjin Na, Izzy Putterman, Benjamin Chislett, Maor Ashkenazi, Joseph Guman, Gerald Shen, Tugrul Konuk, Ashwath Aithal, Ritika Borkar, Ran Zilberstein, Bita Rouhani
- **arXiv:** [2604.26779](https://arxiv.org/abs/2604.26779v1) · [pdf](https://arxiv.org/pdf/2604.26779v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.26779v1))
- **Categories:** cs.LG, cs.CL

### Abstract
> RL post-training of frontier language models is increasingly bottlenecked by autoregressive rollout generation, making rollout acceleration a central systems challenge. Many existing efficiency methods improve throughput by changing the rollout or optimization regime, for example, through off-policy execution, replay, or lower-precision generation. We study speculative decoding as a lossless acceleration primitive for RL rollouts that preserves the target model's output distribution. We implement speculative decoding in NeMo-RL with a vLLM backend, supporting both synchronous and asynchronous pipelines and enabling speculation during RL rollouts. This benefit is realizable across speculation mechanisms, such as pretrained MTP heads, small external draft models or even techniques such as Eagle3, which are traditionally applied after RL phase. This yields a deployment path for state-of-the-art speculative decoding inside RL training. In a reasoning post-training workload at 8B scale under synchronous RL, speculative decoding improves rollout throughput by 1.8x. Using a high-fidelity performance simulator, we project that combining speculative decoding with asynchronous RL yields up to 2.5x end-to-end training speedup at 235B scale.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**

### Equation 1: 
\[ \text{learning speed} = \text{effectiveness} \times \text{throughput} \]

* Symbols: `learning speed`, `effectiveness`, `throughput`
* Why it matters: This equation relates the learning speed of a model to its effectiveness and throughput. It suggests that increasing either effectiveness or throughput can lead to faster learning.

### Equation 2: 
\[ T_{\text{step}} = T_{\text{data}} + T_{\text{prepare}} + T_{\text{gen}} + T_{\text{logprob}} + T_{\text{train}} \]

* Symbols: `T_step`, `T_data`, `T_prepare`, `T_gen`, `T_logprob`, `T_train`
* Why it matters: This equation breaks down the components of a typical RL step, highlighting the relative contributions of data loading, preparation, generation, log-probability recomputation, and training to the overall step time.

### Equation 3: 
\[ T_{\text{prepare}} \]

* Symbols: `T_prepare`
* Why it matters: This equation is not fully specified in the provided context, but it likely represents the time required for weight synchronization and backend preparation.

### Equation 4: 
\[ T_{\text{gen}} \]

* Symbols: `T_gen`
* Why it matters: This equation is not fully specified in the provided context, but it likely represents the time required for rollout generation.

### Equation 5: 
\[ T_{\text{logprob}} \]

* Symbols: `T_logprob`
* Why it matters: This equation is not fully specified in the provided context, but it likely represents the time required for log-probability recomputation under the current policy.

### Equation 6: 
\[ T_{\text{train}} \]

* Symbols: `T_train`
* Why it matters: This equation is not fully specified in the provided context, but it likely represents the time required for advantage computation and policy optimization.

**Method Summary**

* The authors propose speculative decoding as a lossless acceleration primitive for RL rollouts.
* Speculative decoding targets only the autoregressive decode phase of rollout generation, which is the bottleneck in RL post-training.
* The technique can be applied to various speculation mechanisms, including pretrained MTP heads, small external draft models, and Eagle3.
* The authors evaluate their approach on two datasets: UltraChat and Magpie, and compare the results with a draft trained on DAPO post-training data.

**Experimental Overview**

* Tasks: Mathematical reasoning
* Datasets: DAPO-Math-17K, AIME-2024
* Baselines: GRPO-based RL post-training
* Main claimed findings:
	+ Speculative decoding speeds up rollout generation by 1.8 × and 1.5 × on RL-Zero and RL-Think, respectively.
	+ The technique improves overall step speedup by 1.41 × and 1.35 × on RL-Zero and RL-Think, respectively.

**What to Verify in the PDF**

* The authors mention that the draft initialization strongly affects the realized speedup, but the provided context does not provide enough information to verify this claim.
* The authors also mention that the draft length and online adaptation have a significant impact on the speedup, but the provided context does not provide enough information to verify these claims.
* The authors use a proprietary GPU performance simulator, but the provided context does not provide enough information to verify the accuracy of this simulator.
{% endraw %}
