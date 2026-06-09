---
layout: post
title: "Daily arXiv Digest — 2026-06-09 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Rethinking the Divergence Regularization in LLM RL
- **Authors:** Jiarui Yao, Xiangxin Zhou, Penghui Qi, Wee Sun Lee, Liefeng Bo, Tianyu Pang
- **arXiv:** [2606.09821](https://arxiv.org/abs/2606.09821v1) · [pdf](https://arxiv.org/pdf/2606.09821v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.09821v1))
- **Categories:** cs.LG

### Abstract
> Reinforcement learning (RL) has become a key component of post-training large language models (LLMs). In practice, LLM RL is often off-policy because of training-inference mismatch and policy staleness, making trust-region control essential for stable optimization. Mainstream methods such as PPO and GRPO approximate this control with a ratio-clipping mechanism, but the importance ratio can be a poor proxy for distributional shift in long-tailed vocabularies. Recent work such as DPPO addresses this mismatch by replacing ratio-based clipping with a divergence-based mask, yielding a trust region defined by the sampled token's absolute probability shift. However, DPPO still relies on a hard mask: once a token crosses the trust-region boundary in a harmful direction, its gradient is discarded rather than corrected. To address this, we propose Divergence Regularized Policy Optimization (DRPO), which replaces the hard mask with a smooth advantage-weighted quadratic regularizer on policy shift. DRPO preserves the same trust-region geometry as DPPO while inducing bounded, continuous gradient weights that attenuate diverging updates and provide corrective signals beyond the boundary. Experiments across model scales, architectures, and precision settings show that DRPO improves the stability and efficiency of LLM RL training.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Binary-TV proxy

^{1,*\,\mathparagraph}
\[ D_{t}^{\mathrm{Bin\text{-}TV}} = \big|\pi(y_{t}|s_{t}) - \mu(y_{t}|s_{t})\big| = \mu(y_{t}|s_{t}) |r_{t} - 1| \]

* Equation: $D_{t}^{\mathrm{Bin\text{-}TV}}$
* Symbols: $\pi(y_{t}|s_{t})$, $\mu(y_{t}|s_{t})$, $r_{t}$
* Why it matters: This equation represents the Binary-TV proxy, which is used to define the trust region in the paper.

### Equation 2: Trust region analysis

^{3,*\,\mathparagraph}
\[ w_{t} = 1 - \frac{D_{t}^{\mathrm{Bin\text{-}TV}}}{\delta} \]

* Equation: $w_{t}$
* Symbols: $D_{t}^{\mathrm{Bin\text{-}TV}}$, $\delta$
* Why it matters: This equation shows how the weight $w_{t}$ is calculated based on the Binary-TV proxy and the regularization threshold $\delta$.

### Equation 3: Policy

\[
\pi(y_{t}|s_{t})
\]

* Equation: $\pi(y_{t}|s_{t})$
* Symbols: $\pi$, $y_{t}$, $s_{t}$
* Why it matters: This equation represents the policy, which is a probability distribution over the possible actions given the current state.

### Equation 4: Advantage

\[
\mu(y_{t}|s_{t})
\]

* Equation: $\mu(y_{t}|s_{t})$
* Symbols: $\mu$, $y_{t}$, $s_{t}$
* Why it matters: This equation represents the advantage, which is a measure of the difference between the policy and the true distribution.

### Equation 5: Regularization threshold

\[
\delta = 0.15
\]

* Equation: $\delta$
* Symbols: $\delta$
* Why it matters: This equation sets the regularization threshold, which controls the size of the trust region.

**Method Summary**
==================

* The paper proposes a new method called Divergence Regularized Policy Optimization (DRPO), which is an extension of the DPPO method.
* DRPO uses a smooth advantage-weighted quadratic regularizer on policy shift to replace the hard mask in DPPO.
* The method preserves the same trust-region geometry as DPPO but induces bounded, continuous gradient weights that attenuate diverging updates and provide corrective signals beyond the boundary.

**Experimental Overview**
=========================

* The paper evaluates the proposed method on several tasks and datasets, including Qwen3-4B-Base, Qwen3-30B-A3B-Base, and Qwen3.5-35B-A3B-Base.
* The method is compared to several baselines, including GRPO, SPO, and DPPO.
* The main claimed findings are that DRPO consistently enables stable and efficient training, matching or exceeding the best evaluation accuracy achieved by the baselines.

**What to Verify in the PDF**
=============================

* The mathematical derivation of the gradient of the objective function in Equation 8.
* The implementation details of the VeRL framework and the Megatron training backend.
* The results of the ablation studies on the design considerations of the regularizer, including the advantage weight and the regularization threshold.
{% endraw %}

{% raw %}
## 2) Weighted universal approximation of differentiable maps on infinite-dimensional manifolds
- **Authors:** Philipp Schmocker, Josef Teichmann
- **arXiv:** [2606.09820](https://arxiv.org/abs/2606.09820v1) · [pdf](https://arxiv.org/pdf/2606.09820v1)
- **LLM context source:** abstract only
- **Categories:** math.FA, cs.LG, math.PR, q-fin.MF, stat.ML

### Abstract
> We generalize the universal approximation theorem for functional input neural networks (FNN) to differentiable maps by including the approximation of the derivatives. A FNN maps the input from a possibly infinite-dimensional weighted manifold to the real-valued hidden layer, on which a non-linear scalar activation function is applied, and then returns the output into a Banach space via some linear readouts. By proving a weighted Nachbin theorem, we establish a universal approximation theorem (UAT) for differentiable maps, which goes beyond the usual formulation on compact sets and also includes the approximation of the derivatives. This leads us to approximation results for non-anticipative functionals including the horizontal and vertical derivatives. As a further application, we show that linear functions of the signature are able to approximate path space functionals including their directional derivatives.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

1. **Weighted Nachbin Theorem**
   - Equation: Not explicitly provided in the context
   - Symbols: Not specified
   - Why it matters: The paper claims to establish a universal approximation theorem (UAT) for differentiable maps using the weighted Nachbin theorem, which is a generalization of the universal approximation theorem for functional input neural networks (FNN).

2. **Approximation of Derivatives**
   - Equation: Not explicitly provided in the context
   - Symbols: Not specified
   - Why it matters: The paper aims to approximate not only the function itself but also its derivatives, which is a crucial aspect of differentiable maps.

3. **Non-anticipative Functionals**
   - Equation: Not explicitly provided in the context
   - Symbols: Not specified
   - Why it matters: The paper shows that the universal approximation theorem can be applied to non-anticipative functionals, including the horizontal and vertical derivatives.

4. **Linear Functions of the Signature**
   - Equation: Not explicitly provided in the context
   - Symbols: Not specified
   - Why it matters: The paper demonstrates that linear functions of the signature can approximate path space functionals, including their directional derivatives.

5. **Approximation of Path Space Functionals**
   - Equation: Not explicitly provided in the context
   - Symbols: Not specified
   - Why it matters: The paper shows that the universal approximation theorem can be applied to path space functionals, which is a key application of the theorem.

**Method Summary**
================

* The authors generalize the universal approximation theorem for functional input neural networks (FNN) to differentiable maps.
* They include the approximation of derivatives in the theorem.
* The method is based on a weighted Nachbin theorem.
* The authors aim to establish a universal approximation theorem for differentiable maps.

**Experimental Overview**
=====================

* Tasks/Datasets: Not specified in the context
* Baselines/Comparisons: Not specified in the context
* Main Claimed Findings: The authors claim to establish a universal approximation theorem for differentiable maps, which goes beyond the usual formulation on compact sets.

**What to Verify in the PDF**
=========================

* The weighted Nachbin theorem and its proof.
* The details of the approximation of derivatives and non-anticipative functionals.
* The experimental results and datasets used to test the proposed method.
{% endraw %}

{% raw %}
## 3) Limit Theory for $N$-Player $α$-Potential Games
- **Authors:** Xin Guo, Meng Wang, Yufei Zhang
- **arXiv:** [2606.09815](https://arxiv.org/abs/2606.09815v1) · [pdf](https://arxiv.org/pdf/2606.09815v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.09815v1))
- **Categories:** math.OC, math.PR

### Abstract
> The framework of $α$-potential games has recently been introduced as a tool to analyze finite-player dynamic games, reducing the challenging task of finding approximate Nash equilibria to a control problem of minimizing a single function called $α$-potential function. In this work, we investigate the limiting behavior of $α$-potential games as the number of players $N$ tends to infinity. We show that potential mean field games (MFGs) arise naturally as this limit. Specifically, both the optimal values and the minimizers of normalized $N$-player $α_N$-potential functions converge to those of a mean field control (MFC) problem with measure-valued controls. We establish the equivalence of $\lim_{N\to\infty}α_N= 0$ with the existing conditions for potential MFGs, and provide an unified approach to construct the potential function for MFGs using the techniques from differential geometry in Wasserstein space. We further demonstrate that the objective of the limiting MFC problem serves as a potential function for the corresponding MFGs, an extension of the analogous finite-player setting. This connection yields new constructions of potential MFGs from a finite-player game, through the asymptotic condition $\lim_{N\to \infty}α_N= 0$. As a by-product, we establish propagation of chaos for $N$-player games converging to MFGs for general controlled diffusions with common noise and non-separable control interactions.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1) Formula walkthrough**
### Equation 1: α
```latex
\alpha
```
Symbols: `α`
Why it matters: The α-potential function is a key concept in the paper, and this equation likely represents the definition or a property of the α-potential function.

### Equation 2: α_N
```latex
\alpha_{N}
```
Symbols: `α_N`
Why it matters: This equation likely represents the α-potential function for an N-player game, and it is used to study the limiting behavior of α-potential games as N tends to infinity.

### Equation 3: lim_N→∞ α_N = 0
```latex
\lim_{N\to\infty}\alpha_{N}=0
```
Symbols: `lim_N→∞ α_N = 0`
Why it matters: This equation represents the asymptotic condition that the α-potential function for an N-player game converges to 0 as N tends to infinity, which is a key assumption in the paper.

### Equation 4: (3.2)
```latex
\alpha_{N}
```
Symbols: `α_N`
Why it matters: This equation is part of the derivation of the limiting MFC problem, and it represents the control objective for the MFC problem.

### Equation 5: (3.9)
```latex
\Phi_{\tilde{\Omega}}^{\tilde{\mu}}(\tilde{\mu},\tilde{\Lambda}_{t}(dm)\delta_{m}(dm^{\prime})dt,\tilde{B})
```
Symbols: `Φ_tildeΩ_tildeμ_tildeΛ_t_δ_m_δ_m_prime_dt_tildeB`
Why it matters: This equation represents the objective function of the MFC problem, which is used to identify the potential function for the MFG.

**2) Method summary**
* The paper investigates the limiting behavior of α-potential games as the number of players N tends to infinity.
* The authors derive the limiting MFC problem using techniques from differential geometry in Wasserstein space.
* The MFC problem is used to construct the potential function for the MFG, which is a key concept in the paper.
* The authors establish the equivalence of the asymptotic condition lim_N→∞ α_N = 0 with the existing conditions for potential MFGs.

**3) Experimental overview**
* Tasks/Datasets: The paper does not mention specific tasks or datasets, but it is likely that the authors used numerical simulations to test their results.
* Baselines/Comparisons: The paper does not mention any baselines or comparisons, but it is likely that the authors compared their results with existing methods for analyzing finite-player dynamic games.
* Main claimed findings: The paper claims that the limiting MFC problem arises naturally as the limit of α-potential games as N tends to infinity, and that the objective of the limiting MFC problem serves as a potential function for the corresponding MFG.

**4) What to verify in the PDF**
* The authors' assumption that the probability space (Ω, ℱ, ℙ) supports an ℝn-valued random variable ξ with law ν ∈ 𝒫2(Rn) is not explicitly stated in the extracted context.
* The authors' use of the fundamental theorem of calculus in the derivation of the limiting MFC problem is not explicitly stated in the extracted context.
* The authors' claim that the objective function of the MFC problem serves as a potential function for the MFG is not explicitly stated in the extracted context.
{% endraw %}

{% raw %}
## 4) Topological Neural Operators
- **Authors:** Lennart Bastian, Samuel Leventhal, Mustafa Hajij, Tolga Birdal
- **arXiv:** [2606.09806](https://arxiv.org/abs/2606.09806v1) · [pdf](https://arxiv.org/pdf/2606.09806v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.09806v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> We introduce Topological Neural Operators (TNOs), a principled framework for operator learning on cell complexes that lifts neural operators (NOs) from functions on points and/or edges to topological domains. TNOs represent data as features defined on cells of varying dimension and model their interactions through Discrete Exterior Calculus, enabling explicit cross-dimensional coupling via gradient-, curl-, and divergence-type operators. The key design principle is to decouple where information flows, as governed by fixed topological operators, from how it is transformed (which is learned), yielding models that respect the geometric support of physical quantities and expose conservation and compatibility structure. We further propose Hierarchical TNOs (HTNOs), which incorporate learned coarse complexes to propagate long-range and topology-dependent information. Our framework subsumes existing NOs as a special case, providing a unified perspective on operator learning across discretizations. Across a range of PDE benchmarks, including irregular-geometry flow problems, TNOs and HTNOs improve accuracy; controlled studies further isolate the benefits of native higher-rank and topological structure. Project page: https://circle-group.github.io/research/TNO
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Not found in extracted context.

### Equation 2: 
\[ \mathrm{div}\,\mathrm{curl} = 0 \]
Symbols: 
- \( \mathrm{div} \) represents the divergence operator.
- \( \mathrm{curl} \) represents the curl operator.
Why it matters: This equation is a fundamental property of vector calculus, stating that the divergence of the curl of any vector field is always zero. In the context of Topological Neural Operators, this equation is used to define the curl operator.

### Equation 3: 
\[ d^{k} \]
Symbols: 
- \( d \) represents the exterior derivative operator.
- \( k \) is the degree of the differential form.
Why it matters: This notation represents the exterior derivative operator raised to the power of \( k \), which is used to define the differential forms used in the Topological Neural Operators framework.

### Equation 4: 
\[ \delta^{k} \]
Symbols: 
- \( \delta \) represents the codifferential operator.
- \( k \) is the degree of the differential form.
Why it matters: This notation represents the codifferential operator raised to the power of \( k \), which is used to define the codifferential forms used in the Topological Neural Operators framework.

### Equation 5: 
\[ \mathrm{rk}: K \to \mathbb{Z}_{\geq 0} \]
Symbols: 
- \( \mathrm{rk} \) represents the rank function.
- \( K \) is the cell complex.
- \( \mathbb{Z}_{\geq 0} \) represents the set of non-negative integers.
Why it matters: This notation represents the rank function, which assigns a non-negative integer to each cell in the cell complex, representing the dimension of the cell.

### Equation 6: 
\[ \sigma \prec \tau \]
Symbols: 
- \( \sigma \) and \( \tau \) represent two cells in the cell complex.
- \( \prec \) represents the inclusion relation.
Why it matters: This notation represents the inclusion relation between two cells, which is used to define the hierarchical structure of the cell complex.

### Equation 7: 
\[ \mathrm{rk}(\tau) - \mathrm{rk}(\sigma) = 1 \]
Symbols: 
- \( \mathrm{rk}(\tau) \) and \( \mathrm{rk}(\sigma) \) represent the ranks of two cells.
Why it matters: This notation represents the difference in ranks between two cells, which is used to define the hierarchical structure of the cell complex.

**Method Summary**
================

* Topological Neural Operators (TNOs) represent data as features defined on cells of varying dimension and model their interactions through Discrete Exterior Calculus.
* TNOs decouple where information flows from how it is transformed, yielding models that respect the geometric support of physical quantities and expose conservation and compatibility structure.
* Hierarchical TNOs (HTNOs) incorporate learned coarse complexes to propagate long-range and topology-dependent information.
* TNOs and HTNOs improve accuracy on a range of PDE benchmarks, including irregular-geometry flow problems.

**Experimental Overview**
=========================

* Tasks: Steady-state PDE benchmarks, including Poisson's equation, hyper-elastic deformations, compressible flow past airfoils, and large-scale 3D wing-surface aerodynamics.
* Datasets: Three established public suites, including Poisson-Gauss, Airfoil Flow, and Elasticity.
* Baselines: Seven baselines reported in [67], including RIGNO-18, RIGNO-12, MeshGraphNet, Geo-FNO, FNO DSE, GINO, and UPT.
* Main claimed findings: TNO and HTNO outperform all seven baselines on Poisson-Gauss and Elasticity, and are competitive with RIGNO-18 on Airfoil Flow.

**What to Verify in the PDF**
=============================

* The implementation details of the Topological Neural Operators framework, including the Discrete Exterior Calculus and the hierarchical structure of the cell complex.
* The experimental results, including the accuracy and robustness of TNO and HTNO on the various PDE benchmarks.
* The theoretical foundations of the Topological Neural Operators framework, including the relationship between the rank function and the hierarchical structure of the cell complex.
{% endraw %}

{% raw %}
## 5) Echo-Memory: A Controlled Study of Memory in Action World Models
- **Authors:** Wayne King, Zeyue Xue, Yuxuan Bian, Jie Huang, Haoran Li, Yaowei Li, Yaofeng Su, Yuming Li, Haoyu Wang, Shiyi Zhang, Songchun Zhang, Yuwei Niu, Sihan Xu, Junhao Zhuang, Haoyang Huang, Nan Duan
- **arXiv:** [2606.09803](https://arxiv.org/abs/2606.09803v1) · [pdf](https://arxiv.org/pdf/2606.09803v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.09803v1))
- **Categories:** cs.CV, cs.GR, cs.LG

### Abstract
> We present \textbf{Echo-Memory}, a controlled study of memory mechanisms in action-conditioned world models. These models generate multi-segment videos from a first frame, text prompt, and camera-action sequence, but their central failure is often memory rather than local image synthesis: after the camera leaves and returns, the scene or salient object may silently change. Existing memory designs are hard to compare because gains are entangled with backbone, training, retrieval, and evaluation differences. Echo-Memory fixes the action-to-video interface and varies only how history is stored and read by the generator. Under a shared video diffusion backbone, optimizer, camera-action representation, sampler, and evaluation pipeline, we compare raw context, compression-based memory, spatial summaries with different read-out paths, and state-space recurrence. This matched matrix separates four otherwise conflated axes: \emph{capacity}, \emph{compression}, \emph{read-out}, and \emph{recurrence}. We also evaluate memory through a three-branch protocol: replay quality, in-domain loop revisit, and open-domain return probes. The branches routinely disagree, showing that replay fidelity is not a sufficient proxy for remembering a world. Three findings follow. Raw context is a strong capacity baseline and improves open-domain return far more than it improves replay metrics. Compactness is not a free substitute for capacity: aggressive spatial and hybrid-compression memories lose the salient evidence needed for return. Finally, block-wise state-space recurrence is the strongest open-domain return mechanism in our matrix, showing that the structure of implicit memory matters as much as the decision to use it. These results provide a compact protocol for studying memory in action world models beyond isolated replay metrics.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: K{=}1

* Equation: K{=}1
* Symbols: K (capacity)
* Why it matters: This equation represents the capacity of the memory mechanism, which is a key factor in determining the model's ability to remember the world.

### Equation 2: K{=}20

* Equation: K{=}20
* Symbols: K (capacity)
* Why it matters: This equation represents a different capacity setting for the memory mechanism, which is used to evaluate the model's performance under different conditions.

### Equation 3: 12.25

* Equation: 12.25
* Symbols: None
* Why it matters: This equation represents a specific value that is used to evaluate the model's performance, but its exact meaning is not clear from the context.

### Equation 4: 58.63

* Equation: 58.63
* Symbols: None
* Why it matters: This equation represents another specific value that is used to evaluate the model's performance, but its exact meaning is not clear from the context.

### Equation 5: 69.00

* Equation: 69.00
* Symbols: None
* Why it matters: This equation represents a specific value that is used to evaluate the model's performance, but its exact meaning is not clear from the context.

**Method Summary**
================

* The Echo-Memory design space is formalized as a factorization of how an action world model can represent the past: Context tokens, Compression operators, Spatial summaries, or a State-Space state.
* The backbone is a pre-trained video diffusion-transformer that models the conditional velocity field.
* The memory mechanism is varied across different variants, including raw context, compression-based memory, spatial summaries with different read-out paths, and state-space recurrence.

**Experimental Overview**
================--------

* Tasks/Datasets: The experiments are conducted on a variety of tasks, including in-domain and open-domain return, replay, and semantic verification.
* Baselines/Comparisons: The experiments compare the performance of different memory mechanisms, including raw context, compression-based memory, spatial summaries, and state-space recurrence.
* Main Claimed Findings: The experiments show that replay alone is insufficient to evaluate the model's performance, and that different low-level metrics select different winners. The results highlight the importance of considering multiple evaluation metrics to get a comprehensive understanding of the model's performance.

**What to Verify in the PDF**
=============================

* The evaluation protocol: Verify that the evaluation protocol is correctly implemented and that the results are consistent with the expected behavior of the model.
* The memory mechanism: Verify that the memory mechanism is correctly implemented and that the results are consistent with the expected behavior of the memory mechanism.
* The comparison of different memory mechanisms: Verify that the comparison of different memory mechanisms is correctly implemented and that the results are consistent with the expected behavior of the model.
{% endraw %}
