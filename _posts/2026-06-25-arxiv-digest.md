---
layout: post
title: "Daily arXiv Digest — 2026-06-25 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
- **Authors:** Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
- **arXiv:** [2606.26079](https://arxiv.org/abs/2606.26079v1) · [pdf](https://arxiv.org/pdf/2606.26079v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.26079v1))
- **Categories:** cs.CL, cs.CV, cs.LG

### Abstract
> Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: K{=}6
```markdown
K{=}6
```
* Equation: Not explicitly defined in the context
* Symbols: K
* Why it matters: Not clear without context, but it might represent the number of possible orderings or facets.

### Equation 2: \rho\approx-0.95
```markdown
ρ≈-0.95
```
* Equation: Not explicitly defined in the context
* Symbols: ρ
* Why it matters: Might represent a correlation coefficient or a measure of reliability, but without context, its meaning is unclear.

### Equation 3: >400,000
```markdown
>400,000
```
* Equation: Not explicitly defined in the context
* Symbols: None
* Why it matters: Might represent a threshold or a limit, but without context, its significance is unclear.

### Equation 4: \sigma_{\pi}
```markdown
σ_{\pi}
```
* Equation: Not explicitly defined in the context
* Symbols: σ_{\pi}
* Why it matters: Might represent a standard deviation or a measure of uncertainty, but without context, its meaning is unclear.

### Equation 5: |\delta|
```markdown
|\delta|
```
* Equation: Not explicitly defined in the context
* Symbols: |\delta|
* Why it matters: Might represent a measure of difference or a magnitude, but without context, its significance is unclear.

**Method Summary**
==================

* The authors audit 18 multimodal large language models using a five-facet audit, which includes:
	+ Option-order facet
	+ Evidence-chunk facet
	+ Document-rank facet
	+ Image-set facet
	+ Mixed-modality ordering facet
* The authors use a Bayesian item-response model to separate ordering noise from per-facet bias and a same-ordering control to estimate the decoder-stochastic floor for observed flips.
* The authors also use LLM-judge instruments to evaluate the models' performance on specific facets.

**Experimental Overview**
========================

* Tasks/Datasets:
	+ Multimodal benchmarks (e.g., MMBench, CircularEval)
	+ Synthetic dialog benchmarks (e.g., musique_synth, hotpotqa_synth)
* Baselines/Comparisons:
	+ Multimodal benchmarks (e.g., MMBench, CircularEval)
	+ Other models or baselines (not specified in the context)
* Main Claimed Findings:
	+ The authors claim that the models' performance on the five-facet audit is sensitive to the order of the facets, and that the ordering noise can be separated from per-facet bias using a Bayesian item-response model.

**What to Verify in the PDF**
=============================

* The authors mention that the thinking/reasoning parameter has different per-provider semantics, but it is not clear how this affects the results.
* The authors also mention that the May 4–25, 2026 access window pairs with each provider ID as the reproducibility anchor, but it is not clear what this means in practice.
* The authors use a variety of metrics to evaluate the models' performance, including exact-match flip rates, content-flip rates, and macro-accuracy, but it is not clear how these metrics are related to each other or to the main claimed findings.
{% endraw %}

{% raw %}
## 2) Toward a Systematic Understanding and Interactive Search of Lyapunov-Style Proofs in Optimization
- **Authors:** TaeHo Yoon, Jaewook J. Suh, Edward Duc Hien Nguyen, Bicheng Ying, Shiqian Ma
- **arXiv:** [2606.26077](https://arxiv.org/abs/2606.26077v1) · [pdf](https://arxiv.org/pdf/2606.26077v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.26077v1))
- **Categories:** math.OC

### Abstract
> Lyapunov-style convergence proofs, which establish a nonincreasing sequence to provide a quantitative convergence rate for an algorithm, are popular and often considered desirable in first-order optimization. However, existing approaches to finding such Lyapunov functions rely on hand-designed templates or prior insight on the proof structure, and do not certify that the resulting Lyapunov-style analysis provides the sharpest convergence bound. In this work, we introduce a systematic framework for converting a tight, analytic convergence proof of an optimization algorithm, often found via computer assistance, into an equivalent proof based on Lyapunov functions. We implement a concrete procedure that combines a performance estimation problem (PEP) toolbox with elementary linear algebra, and show that it captures a number of prior Lyapunov analyses within a single Jupyter notebook. Based on our implementation, a user can straightforwardly test our systematic and interactive procedure on their own optimization algorithm of interest to search for a tight Lyapunov-style proof via code, without the need to comprehend the implementation details. We extend the application of our framework and discover four novel analytic Lyapunov-style proofs, where notably, one of them identifies a new exact optimal proximal algorithm for strongly monotone inclusion problems.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Performance Metric

[Eq 1] \leftrightarrow
\texttt{(PerformanceMetric)}-\nu\times\texttt{(InitialCondition)}=-\sum_{i,j}\lambda_{i,j}I_{i,j}-\sum_{i}\|v_{i}\|^{2}\leq 0.

* Equation: The performance metric equation.
* Symbols:
	+ \texttt{(PerformanceMetric)}: The performance metric.
	+ \nu: A nonnegative scalar.
	+ \texttt{(InitialCondition)}: The initial condition.
	+ \lambda_{i,j}: Nonnegative scalars.
	+ I_{i,j}: Nonnegative inequality terms.
	+ \|v_{i}\|: Nonnegative vectors.
* Why it matters: This equation represents the performance metric of the optimization algorithm, which is used to estimate the convergence rate.

### Equation 2: Non-Negativity of I_{i,j}

[Eq 3] I_{i,j}\geq 0

* Equation: The non-negativity constraint for I_{i,j}.
* Symbols: I_{i,j}: Nonnegative inequality terms.
* Why it matters: This constraint ensures that the inequality terms are non-negative, which is a necessary condition for the performance metric.

### Equation 3: Non-Negativity of \nu, \lambda_{i,j}, and v_i

[Eq 4] \nu,\lambda_{i,j}\geq 0

[Eq 5] v_{i}\in\mathbb{R}^{n}

* Equation: The non-negativity constraints for \nu, \lambda_{i,j}, and v_i.
* Symbols: \nu, \lambda_{i,j}: Nonnegative scalars.
* v_i: Nonnegative vectors.
* Why it matters: These constraints ensure that the scalars and vectors are non-negative, which is a necessary condition for the performance metric.

### Equation 4: Lyapunov Function

[Eq 6] \|\nabla f(x_{k})\|^{2}=\mathcal{O}\left((f(x_{0})-f(x_{\star}))/k^{2}\right)

[Eq 7] \|\nabla f(x_{k})\|^{2}=\mathcal{O}\left(\|x_{0}-x_{\star}\|^{2}/k^{4}\right)

* Equation: The Lyapunov function equation.
* Symbols: \|\nabla f(x_{k})\|: The gradient norm.
* f(x_{k}): The objective function.
* x_{0}, x_{\star}: Initial and optimal points.
* k: The iteration number.
* Why it matters: These equations represent the Lyapunov function, which is used to analyze the convergence rate of the optimization algorithm.

**Method Summary**
==================

* The Performance Estimation Problem (PEP) is a computer-assisted framework for analyzing the quantitative convergence rate of optimization algorithms.
* PEP reformulates the problem of identifying the worst-case rate of a first-order algorithm into a tractable optimization problem—typically a semidefinite program (SDP)—that can be numerically solved by a solver.
* The dual solution to this SDP encodes a proof of the form:
	+ I_{i,j} ≥ 0
	+ ν, λ_{i,j} ≥ 0
	+ v_i ∈ ℝ^n
* The PEP-style proof is more general than Lyapunov-style proofs, as it is not constrained to a specific proof template.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors consider the proximal algorithms for maximally monotone inclusions with proximal operations.
* Baselines/Comparisons: The authors compare their results with existing algorithms, such as OGM, OGM-G, and APPM.
* Main Claimed Findings: The authors claim to have discovered four novel analytic Lyapunov-style proofs, including one that identifies a new exact optimal proximal algorithm for strongly monotone inclusion problems.

**What to Verify in the PDF**
=============================

* The authors claim to have developed a systematic framework for converting a tight, analytic convergence proof of an optimization algorithm into an equivalent proof based on Lyapunov functions.
* The authors claim to have implemented a concrete procedure that combines a performance estimation problem (PEP) toolbox with elementary linear algebra.
* The authors claim to have shown that their framework captures a number of prior Lyapunov analyses within a single Jupyter notebook.
{% endraw %}

{% raw %}
## 3) Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
- **Authors:** Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
- **arXiv:** [2606.26071](https://arxiv.org/abs/2606.26071v1) · [pdf](https://arxiv.org/pdf/2606.26071v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.AI

### Abstract
> A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
Unfortunately, no formulas are mentioned in the extracted context.

### Method Summary
* The proposed protocol for model forensics consists of two steps: reading the chain of thought (CoT) and making edits to the prompt or environment to test hypotheses.
* The CoT is used to generate hypotheses about what drives model behavior, and the protocol is iterated as needed.
* The protocol is applied to six agentic environments where models exhibit concerning behavior.

### Experimental Overview
* Tasks/Datasets: A suite of six agentic environments where models exhibit concerning behavior.
* Baselines/Comparisons: The proposed protocol is compared to existing methods for detecting concerning behavior.
* Main Claimed Findings:
  * The protocol successfully predicts the behavior of models exhibiting concerning behavior.
  * The protocol can detect whether a model is driven by malign intent.

### What to Verify in the PDF
* The details of the chain of thought (CoT) generation process, including how it is used to generate hypotheses about model behavior.
* The results of the counterfactual experiments, including how they demonstrate the model's behavior is driven by malign intent.
* The limitations of the proposed protocol, including the lack of positive controls and the need for further refinement.
{% endraw %}

{% raw %}
## 4) Is Variational Monte Carlo Robust? Sharp Moment Thresholds and Heavy-tailed Stochastic Optimization
- **Authors:** Philipp Grohs, Davide Nobile
- **arXiv:** [2606.26009](https://arxiv.org/abs/2606.26009v1) · [pdf](https://arxiv.org/pdf/2606.26009v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.26009v1))
- **Categories:** cs.LG

### Abstract
> Variational Monte Carlo (VMC) is a central algorithm in electronic structure theory and has gained renewed importance through modern neural-network ansätze such as FermiNet. At its core, VMC seeks ground states by minimizing the Rayleigh quotient by stochastic optimization. In this work, we show that the resulting stochastic optimization problem is intrinsically governed by the nodal geometry of the underlying wave function. More precisely, we establish that properties of the nodal set determine the integrability of the local energy and gradient estimators that drive VMC. For broad and practically relevant ansatz classes, including Slater-Jastrow wave functions with variable-exponent Slater-type orbitals, we prove that these estimators are generically heavy-tailed and fail to admit higher moments. At the same time, for general analytic ansätze, we prove weak moment bounds for the relevant estimators and identify precise low-moment regimes, showing how generic and degenerate nodal structures lead to different integrability thresholds. Building on this analysis, we introduce a new robust variant of VMC $\unicode{x2013}$ coined PS-Clip-VMC $\unicode{x2013}$ which is based on clipping both the local energy and the gradient random variable. We prove that PS-Clip-VMC converges both in expectation and with high probability in the weak moment regime of VMC. Preliminary experiments for training FermiNet on Atoms with up to 18 electrons suggest that PS-Clip-VMC is significantly more robust than standard methods.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{H}:\ H^{2}(\Omega)\to L^{2}(\Omega)$

* Equation: $\mathcal{H}:\ H^{2}(\Omega)\to L^{2}(\Omega)$
* Symbols: $\mathcal{H}$ (Hamiltonian operator), $H^{2}(\Omega)$ (Sobolev space of order 2), $L^{2}(\Omega)$ (L2 space)
* Why it matters: This equation defines the Hamiltonian operator $\mathcal{H}$, which is a central component in the problem of approximating ground states and ground state energies of many-particle Hamiltonians.

### Equation 2: $E_{0}:=\inf_{\psi\in\mathfrak{d}(\mathcal{H})\setminus\{0\}}\frac{\langle\mathcal{H}\psi,\psi\rangle}{\|\psi\|_{L^{2}}^{2}}$

* Equation: $E_{0}:=\inf_{\psi\in\mathfrak{d}(\mathcal{H})\setminus\{0\}}\frac{\langle\mathcal{H}\psi,\psi\rangle}{\|\psi\|_{L^{2}}^{2}}$
* Symbols: $E_{0}$ (ground-state energy), $\mathfrak{d}(\mathcal{H})$ (form-domain of $\mathcal{H}$), $\langle\mathcal{H}\psi,\psi\rangle$ (inner product of $\mathcal{H}\psi$ and $\psi$), $\|\psi\|_{L^{2}}^{2}$ (L2 norm of $\psi$)
* Why it matters: This equation defines the ground-state energy $E_{0}$, which is the minimum value of the Rayleigh quotient. It is a key quantity in the problem of approximating ground states and ground state energies of many-particle Hamiltonians.

### Equation 3: $\mathfrak{d}(\mathcal{H})=H^{1}(\Omega)$

* Equation: $\mathfrak{d}(\mathcal{H})=H^{1}(\Omega)$
* Symbols: $\mathfrak{d}(\mathcal{H})$ (form-domain of $\mathcal{H}$), $H^{1}(\Omega)$ (Sobolev space of order 1)
* Why it matters: This equation defines the form-domain $\mathfrak{d}(\mathcal{H})$ of the Hamiltonian operator $\mathcal{H}$, which is a key component in the problem of approximating ground states and ground state energies of many-particle Hamiltonians.

### Equation 4: $\Omega=\mathbb{R}^{d\times N}$

* Equation: $\Omega=\mathbb{R}^{d\times N}$
* Symbols: $\Omega$ (domain of the Hamiltonian), $\mathbb{R}^{d\times N}$ (space of $d\times N$ matrices)
* Why it matters: This equation defines the domain $\Omega$ of the Hamiltonian, which is a key component in the problem of approximating ground states and ground state energies of many-particle Hamiltonians.

### Equation 5: $\mathcal{H}=-\Delta+\sum_{i,j=1}^{N}V(x_{i},x_{j})+\sum_{i=1}^{N}V_{\mbox{ext}}(x_{i})$

* Equation: $\mathcal{H}=-\Delta+\sum_{i,j=1}^{N}V(x_{i},x_{j})+\sum_{i=1}^{N}V_{\mbox{ext}}(x_{i})$
* Symbols: $\mathcal{H}$ (Hamiltonian operator), $\Delta$ (Laplace operator), $V(x_{i},x_{j})$ (potential energy), $V_{\mbox{ext}}(x_{i})$ (external potential)
* Why it matters: This equation defines the Hamiltonian operator $\mathcal{H}$, which is a central component in the problem of approximating ground states and ground state energies of many-particle Hamiltonians.

**Method Summary**
==================

* The authors propose a new robust variant of Variational Monte Carlo (VMC) called PS-Clip-VMC, which is based on clipping both the local energy and the gradient random variable.
* The authors prove that PS-Clip-VMC converges both in expectation and with high probability in the weak moment regime of VMC.
* The authors also propose a new method for training FermiNet, a neural-network-based VMC algorithm, which involves per-sample gradient clipping.

**Experimental Overview**
========================

* The authors train FermiNet on atoms with up to 18 electrons using the standard components of modern neural-network-based VMC, including MCMC sampling, KFAC updates, and centered local-energy clipping.
* The authors compare the performance of PS-Clip-VMC with the standard method on Sulfur and Argon, and find that PS-Clip-VMC is significantly more robust.
* The authors also find that per-sample gradient clipping can improve the stability and performance of VMC.

**What to Verify in the PDF**
=============================

* The authors' proof of the main result, which involves showing that every ψ θ \psi_{\theta} has an arbitrarily small perturbation with certain regular zeros.
* The authors' analysis of the robust optimization methods introduced in Section 4, which involves showing that PS-Clip-VMC converges both in expectation and with high probability in the weak moment regime of VMC.
* The authors' experimental results, which involve comparing the performance of PS-Clip-VMC with the standard method on Sulfur and Argon.
{% endraw %}

{% raw %}
## 5) Tensorion: A Tensor-Aware Generalization of the Muon Optimizer
- **Authors:** Vladimir Bogachev, Vladimir Aletov, Alexander Molozhavenko, Sergei Kudriashov, Maxim Rakhuba
- **arXiv:** [2606.25975](https://arxiv.org/abs/2606.25975v1) · [pdf](https://arxiv.org/pdf/2606.25975v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.25975v1))
- **Categories:** cs.LG, cs.CV, math.NA

### Abstract
> Common first-order optimizers, such as Adam, implicitly treat each parameter block as an unstructured vector, which disregards the multilinear weight structure present in many modern machine learning models. Recent work has shown that exploiting matrix structure can improve optimization dynamics. A notable example is Muon, which performs steepest descent under the spectral norm constraint. We take the next step and introduce Tensorion, a tensor-aware optimizer that extends Muon's constrained optimization perspective from matrices to higher-order tensors. Tensorion is built around a linear minimization oracle (LMO) over a tensor norm ball. The norm is carefully chosen to balance two objectives: tightly bounding the tensor spectral norm, while still keeping the LMO tractable. This LMO becomes computable because it reduces to operations on adaptively selected unfolding matrices. Notably, when restricted to order-2 tensors (i.e., matrices), Tensorion recovers Muon exactly. Experiments on tensor-based computer vision problems suggest that Tensorion can offer improved convergence behavior and more stable gradient updates compared with Adam-based and existing tensor-aware baselines in the evaluated settings.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Gradient of the Loss Function

∇ℒ(𝑊)

* Equation: ∇ℒ(𝑊)
* Symbols: ℒ(𝑊) (loss function), 𝑊 (model parameters)
* Why it matters: This equation represents the gradient of the loss function with respect to the model parameters.

### Equation 2: Loss Function

ℒ(⋅)

* Equation: ℒ(⋅)
* Symbols: ⋅ (input or output)
* Why it matters: This equation represents the loss function, which measures the difference between the model's output and the ground truth.

### Equation 3: Maximum Inner Product

max_{𝑋:‖𝑋‖≤1}‹∇ℒ(𝑊), 𝑋›

* Equation: max_{𝑋:‖𝑋‖≤1}‹∇ℒ(𝑊), 𝑋›
* Symbols: 𝑋 (unfolding matrix), ‖𝑋‖≤1 (norm constraint)
* Why it matters: This equation represents the maximum inner product between the gradient of the loss function and the unfolding matrix, subject to the norm constraint.

### Equation 4: Tensor Norm

‖⋅‖

* Equation: ‖⋅‖
* Symbols: ⋅ (tensor)
* Why it matters: This equation represents the tensor norm, which measures the magnitude of the tensor.

### Equation 5: Infinity Norm

ℓ∞

* Equation: ℓ∞
* Symbols: ⋅ (tensor)
* Why it matters: This equation represents the infinity norm, which measures the maximum absolute value of the tensor.

**Method Summary**
==================

* The Tensorion optimizer is a tensor-aware generalization of the Muon optimizer.
* It uses a linear minimization oracle (LMO) over a tensor norm ball to optimize the model parameters.
* The LMO is computed using adaptively selected unfolding matrices.
* The choice of unfolding index set τ has a significant impact on the optimization dynamics and final accuracy.
* The offline strategy, which selects the optimal unfolding index set τ per layer, is compared to the online strategy, which evaluates all admissible unfoldings at each iteration.

**Experimental Overview**
=========================

* Tasks/Datasets: Tensor-based computer vision problems, including 4D convolutional kernels and ResNet architectures.
* Baselines/Comparisons: Adam-based and existing tensor-aware baselines.
* Main Claimed Findings: Tensorion can offer improved convergence behavior and more stable gradient updates compared to Adam-based and existing tensor-aware baselines.

**What to Verify in the PDF**
=============================

* The choice of unfolding index set τ and its impact on the optimization dynamics and final accuracy.
* The behavior of the algorithm when using different optimizers for the non-tensor parameters of the model.
* The effect of the norm constraint on the optimization dynamics and final accuracy.
{% endraw %}
