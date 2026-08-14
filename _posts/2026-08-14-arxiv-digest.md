---
layout: post
title: "Daily arXiv Digest — 2026-08-14 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Joint Communication-Control Strategy Optimization with Partially Nested Information Structures: The Linear-Quadratic Case
- **Authors:** Haoyi You, Kaiqing Zhang
- **arXiv:** [2608.13535](https://arxiv.org/abs/2608.13535v1) · [pdf](https://arxiv.org/pdf/2608.13535v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.13535v1))
- **Categories:** eess.SY, cs.MA, math.OC

### Abstract
> In this paper, we formalize a joint communication-control strategy optimization (JCCO) problem in multi-agent linear systems with quadratic costs, under the common-information-based (CIB) framework from decentralized stochastic control. For computational tractability, we focus on such JCCO problems with partially nested (PN) information structures (ISs). In particular, with a baseline communication protocol that leads to a PN IS, we establish a series of conditions under which the partial nestedness is preserved under the (additional) communication strategies to be optimized, while violating them may cause nonlinearity of the optimal strategies in general, with open-loop communication strategies. We then develop a dynamic-programming-based approach to compute the optimal control strategies of JCCO with open-loop communication strategies, which yields a set of closed-form Riccati Equations. As a byproduct of independent interest, such an approach also offers a way to solve decentralized linear-quadratic control with PN ISs and output feedback, under the CIB framework. Finally, we extend such an approach to JCCOs with closed-loop communication strategies, yielding a more tractable dynamic program than an infinite-dimensional CIB-belief-based one.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1) Formula walkthrough**

### Equation 1: X^{\dagger}
\[ X^{\dagger} = \begin{bmatrix} \bm{X}_{1} \\ \vdots \\ \bm{X}_{n} \end{bmatrix} \]
Symbols: \( X^{\dagger} \), \( \bm{X}_{i} \) (state vectors)
Why it matters: This equation represents the joint state vector of all agents.

### Equation 2: X\succeq 0
\[ X \succeq 0 \]
Symbols: \( X \) (symmetric matrix)
Why it matters: This inequality ensures that the state matrix is positive semi-definite.

### Equation 3: 0\leq a<b
\[ 0 \leq a < b \]
Symbols: \( a \), \( b \) (indices)
Why it matters: This inequality defines the range of indices for a set.

### Equation 4: [a:b]:=\{a,a+1,\cdots,b\}
\[ [a:b] := \{a, a+1, \cdots, b\} \]
Symbols: \( [a:b] \) (set notation), \( a \), \( b \) (indices)
Why it matters: This equation defines a set of indices.

### Equation 5: [a]=[1:a]
\[ [a] = [1:a] \]
Symbols: \( [a] \) (set notation), \( a \) (index)
Why it matters: This equation establishes an equivalence between two sets.

**2) Method summary**

* The paper proposes a joint communication-control strategy optimization (JCCO) approach for multi-agent linear systems with quadratic costs.
* The approach focuses on partially nested information structures (ISs) and develops a dynamic-programming-based method to compute optimal control strategies.
* The method yields a set of closed-form Riccati Equations, which can be used to solve decentralized linear-quadratic control problems with output feedback.

**3) Experimental overview**

* Tasks/Datasets: The paper presents numerical examples to demonstrate the proposed method.
* Baselines/Comparisons: The approach is compared to a baseline sharing strategy with one-step measurement delay.
* Main claimed findings: The experimental results show that the proposed method outperforms the baseline strategy in terms of control performance.

**4) What to verify in the PDF**

* The derivation of the closed-form Riccati Equations (Section III-B).
* The assumptions under which the method holds (Section II-B).
* The experimental results and their implications for the proposed method.
{% endraw %}

{% raw %}
## 2) DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees
- **Authors:** Tianyi Li, Yaxin Luo, Xinyi Shang, Zhiqiang Shen
- **arXiv:** [2608.13524](https://arxiv.org/abs/2608.13524v1) · [pdf](https://arxiv.org/pdf/2608.13524v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.13524v1))
- **Categories:** cs.LG

### Abstract
> Speculative decoding losslessly accelerates autoregressive language models by verifying multiple draft tokens in parallel. Diffusion-based drafters further reduce proposal latency by predicting an entire token block in parallel, but their position-wise distributions are marginal rather than conditioned on tokens selected along each draft path. Existing recurrent correction incorporates causal information along a single draft chain, whereas diffusion-based tree construction broadens candidate coverage without carrying this correction along individual branches. We introduce DARTree, a training-free speculative decoding method that extends a pretrained AR correction head from chains to trees. DARTree first constructs a fixed-width candidate tree by expanding and scoring all nodes at each depth in a single batch, and then only applies best-first pruning to select the verification tree, decoupling AR-head inference from sequential heap operations. Across seven math, code, and chat benchmarks, DARTree achieves the highest average acceptance length and speedup in all four model--temperature configurations, accepting up to 12.97 tokens per verification round, 98.6\% more than DFlash and 27.9\% more than Domino in the same setting, and reaching up to 9.73$\times$ lossless speedup over locally measured autoregressive decoding.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 
\[ \gamma = \frac{1}{1 + \exp(-\beta \cdot \mathcal{L})} \]

* Symbols: $\gamma$, $\beta$, $\mathcal{L}$
* Why it matters: This equation represents the sigmoid function used to compute the probability of acceptance, where $\beta$ is a hyperparameter and $\mathcal{L}$ is the loss function.

### Equation 2: 
\[ x_{1:t} = \mathcal{E}(y_{1:\gamma}) \]

* Symbols: $x_{1:t}$, $y_{1:\gamma}$, $\mathcal{E}$
* Why it matters: This equation represents the forward pass of the autoregressive model, where $x_{1:t}$ is the output at time $t$ and $y_{1:\gamma}$ is the output of the draft tokens.

### Equation 3: 
\[ \gamma = \frac{1}{1 + \exp(-\beta \cdot \mathcal{L})} \]

* Symbols: $\gamma$, $\beta$, $\mathcal{L}$
* Why it matters: This equation is identical to Equation 1, representing the sigmoid function used to compute the probability of acceptance.

### Equation 4: 
\[ y_{<i} = (y_{1}, \ldots, y_{i-1}) \]

* Symbols: $y_{<i}$, $y_{i}$
* Why it matters: This equation represents the prefix of the output sequence up to time $i-1$.

### Equation 5: 
\[ c_{i} = (x_{1:t}, y_{<i}) \]

* Symbols: $c_{i}$, $x_{1:t}$, $y_{<i}$
* Why it matters: This equation represents the context at time $i$, which includes the output sequence up to time $i-1$ and the input sequence up to time $t$.

**Method Summary**
==================

* DARTree is a training-free speculative decoding method that extends a pretrained causal correction head from chains to trees.
* The method first constructs a fixed-width candidate tree by expanding and scoring all nodes at each depth in a single batch.
* Then, only the best-first pruning is applied to select the verification tree, decoupling AR-head inference from sequential heap operations.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors evaluate DARTree on seven benchmarks: GSM8K, MATH-500, AIME25, HumanEval, MBPP, MT-Bench, and Alpaca.
* Baselines/Comparisons: The authors compare DARTree with DDTree and Domino, as well as a sequential correction method.
* Main Claimed Findings: DARTree achieves the highest average acceptance length and speedup in all four model-temperature configurations, outperforming DDTree and Domino by up to 28.9% and 46.8% in acceptance length and up to 22.7% and 40.1% in speedup.

**What to Verify in the PDF**
=============================

* The authors claim that DARTree achieves a 98.6% increase in acceptance length over DFlash and a 27.9% increase over Domino in the same setting. Verify the actual values and the calculation method used to obtain these results.
* The authors also claim that DARTree's speedup is up to 9.73 × lossless. Verify the actual speedup values and the calculation method used to obtain these results.
* The authors provide an ablation study comparing DARTree with two alternative methods. Verify the results of this study and the conclusions drawn from it.
{% endraw %}

{% raw %}
## 3) Vero: Can AI Agents Build Formally Verified Software Repositories?
- **Authors:** Zhe Ye, Hantao Lou, Yuechun Sun, Peiyang Song, Zhengxu Yan, Timothe Kasriel, Qingyang Zhang, Kaiyu Yang, Soonho Kong, Jingxuan He, Dawn Song
- **arXiv:** [2608.13522](https://arxiv.org/abs/2608.13522v1) · [pdf](https://arxiv.org/pdf/2608.13522v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.13522v1))
- **Categories:** cs.LG, cs.AI, cs.LO, cs.PL, cs.SE

### Abstract
> AI agents are increasingly used for programming, but do not provide any guarantee on the correctness of generated code. Verified code generation, in which an agent produces both an implementation and a machine-checked proof of its specification, offers a stronger path toward trustworthy AI-generated software. Existing benchmarks in this direction either focus on individual functions or only evaluate proof generation with provided implementations. It is still an open question whether agents can make coherent implementation and proof choices across real multi-module codebases. To bridge this gap, we introduce Vero, the first benchmark to evaluate joint implementation and proof synthesis at the repository level. Vero contains 43 multi-module instances sourced from real-world repositories spanning Python, Dafny, Verus, and Coq, and covering diverse domains from cryptographic protocols to distributed systems. Each instance consists of a multi-module Lean 4 repository with predetermined API interfaces, manually curated formal specifications, and reference implementations, supporting both proof-only and code-and-proof evaluation modes. To improve benchmark reliability, Vero also includes an audit mechanism where agents are allowed to formally prove unsatisfiability of provided specification or incorrectness of reference code, which surfaces and corrects latent code and specification errors during curation. We evaluate frontier coding-agent configurations with Lean toolchain access. The strongest agent fully solves only 27 of 43 instances and closes no specifications on the hardest repositories. Vero provides a concrete testbed for measuring progress toward repository-scale verified software synthesis, where current agents still fall short. We release the benchmark, curation pipeline, and evaluation harness at https://github.com/sunblaze-ucb/vero.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

Here's a walkthrough of up to 5 equations extracted from the context:

### Equation 1: $\mathcal{A}=\{a_{1},\dots,a_{m}\}$

* Equation: $\mathcal{A}$ represents a set of elements.
* Symbols: $\mathcal{A}$ (set), $a_{i}$ (elements)
* Why it matters: This equation introduces the concept of a set $\mathcal{A}$, which is used to represent a collection of elements.

### Equation 2: $a_{i}$

* Equation: $a_{i}$ represents an individual element within the set $\mathcal{A}$.
* Symbols: $a_{i}$ (element), $\mathcal{A}$ (set)
* Why it matters: This equation highlights the individual elements within the set $\mathcal{A}$.

### Equation 3: $a_{i}\in\mathcal{A}$

* Equation: $a_{i}$ is an element of the set $\mathcal{A}$.
* Symbols: $a_{i}$ (element), $\mathcal{A}$ (set), $\in$ (subset)
* Why it matters: This equation establishes the relationship between an individual element $a_{i}$ and the set $\mathcal{A}$.

### Equation 4: $\mathcal{S}=\{S_{1},\dots,S_{n}\}$

* Equation: $\mathcal{S}$ represents a set of specifications.
* Symbols: $\mathcal{S}$ (set), $S_{i}$ (specifications)
* Why it matters: This equation introduces the concept of a set $\mathcal{S}$, which represents a collection of specifications.

### Equation 5: $\texttt{RepoImpl}\to\mathtt{Prop}$

* Equation: $\texttt{RepoImpl}$ represents a repository implementation, and $\mathtt{Prop}$ represents a proposition (a statement that can be proven or disproven).
* Symbols: $\texttt{RepoImpl}$ (repository implementation), $\mathtt{Prop}$ (proposition)
* Why it matters: This equation establishes the relationship between a repository implementation and a proposition, which is used to formalize the verification process.

**Method Summary**
================

Here's a summary of the method in 3-5 bullets:

* The authors introduce the Vero benchmark, which evaluates joint implementation and proof synthesis at the repository level.
* The benchmark consists of 43 multi-module instances sourced from real-world repositories, covering diverse domains and programming languages.
* The authors use a combination of coding-agent configurations and formal verification techniques to evaluate the performance of the agents.
* The benchmark includes an audit mechanism to detect latent errors in the specifications and implementations.

**Experimental Overview**
=====================

Here's an overview of the experimental setup:

* Tasks/Datasets: The authors evaluate four frontier coding-agent configurations on the Vero benchmark, using a combination of code-and-proof and proof-only modes.
* Baselines/Comparisons: The authors compare the performance of the coding-agent configurations with the reference implementations and formal verification techniques.
* Main Claimed Findings: The authors report that the strongest agent fully solves only 27 of 43 instances and closes no specifications on the hardest repositories.

**What to Verify in the PDF**
==========================

Here are 2-4 bullets on details that still need to be verified in the full paper:

* The authors mention that the audit mechanism can surface latent errors in the specifications and implementations. Can the authors provide more details on how this mechanism works and its effectiveness?
* The authors report that the strongest agent fully solves only 27 of 43 instances. Can the authors provide more details on the difficulty of the instances and how the agent's performance compares to other baselines?
* The authors mention that the benchmark includes an audit mechanism to detect latent errors. Can the authors provide more details on how this mechanism is implemented and its impact on the benchmark's results?
{% endraw %}

{% raw %}
## 4) Exponential quantum advantage for learning signals with a single qubit
- **Authors:** Ishaan Kannan, Sridhar Prabhu, Saeed A. Khan, Mandar M. Sohoni, Xingrui Song, Saswata Roy, Alen Senanian, Valla Fatemi, Peter L. McMahon, Jordan Cotler
- **arXiv:** [2608.13521](https://arxiv.org/abs/2608.13521v1) · [pdf](https://arxiv.org/pdf/2608.13521v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.13521v1))
- **Categories:** quant-ph, cs.IT, cs.LG

### Abstract
> Quantum technology has the potential to transform scientific discovery, but quantum advantages often require processing capabilities well beyond the reach of experimental platforms. We show that coupling a single controllable qubit to an otherwise conventional sensor can exponentially reduce the number of measurements required to learn classical signals. These rigorous quantum advantages apply to fundamental sensing tasks, including learning Fourier coefficients, extracting temporal correlations from time-varying signals, and estimating transformations of physical observables. Using a superconducting cavity--qubit architecture, we experimentally demonstrate $10^7$-fold reductions in the number of measurements required for Fourier-amplitude and time-varying signal learning. Our $\textit{quantum feature sensing}$ algorithms further enable orders-of-magnitude improvements in simulations of weak-signal dark matter detection and wireless communication applications. These quantum advantages are derived from Quantum Phase-Space Inference (Q$Ψ$), a unifying theory of quantum-enhanced experiments that simultaneously converts a set of experimental objectives and constraints into tight lower bounds and optimal quantum-enhanced learning algorithms while producing a certificate of quantum advantage. Q$Ψ$ extends beyond the regimes captured by quantum Fisher information and provides a framework for systematically identifying rigorous quantum advantages in practical experimental tasks. Together, our results establish that near-term quantum technology can exponentially enhance our ability to learn from classical signals.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: 10^{7}

* Equation: 10^{7}
* Symbols: None
* Why it matters: This equation represents the exponential quantum advantage achieved by the authors. The number 10^{7} indicates that the authors were able to learn classical signals with a single qubit, which is an exponential improvement over conventional sensing protocols.

### Equation 2: \Psi

* Equation: \Psi
* Symbols: \Psi (representing the phase-space representation of the observable)
* Why it matters: This equation represents the phase-space representation of the observable, which is a key concept in the authors' Quantum Phase-Space Inference (Q Ψ \Psi ) framework. The phase-space representation is used to convert the set of experimental objectives and constraints into tight lower bounds and optimal quantum-enhanced learning algorithms.

### Equation 3: Q\Psi

* Equation: Q\Psi
* Symbols: Q (representing the quantum information processing-enabled family) and \Psi (representing the phase-space representation of the observable)
* Why it matters: This equation represents the Q Ψ \Psi instance, which is a combination of the conventional experimental family and the quantum information processing-enabled family. The Q Ψ \Psi instance is used to construct phase-space representations of the observable and of the response functions generated by protocols in each family.

### Equation 4: ECD(β)

* Equation: ECD(β) = D(β/2) | g ⟩ ⟨ e | + D(-β/2) | e ⟩ ⟨ g |
* Symbols: β (representing the control parameter), D(β/2) (representing the single-qubit rotation), | g ⟩ (representing the ground state of the qubit), and | e ⟩ (representing the excited state of the qubit)
* Why it matters: This equation represents the control unitary ECD (β), which is used to implement the entangling operation between the qubit and the cavity. The ECD (β) is composed of single-qubit rotations and echoed conditional displacements, which provide programmable non-Gaussian control and readout of the qubit–cavity system.

### Equation 5: t = 110 ns and d = 1100 ns

* Equation: t = 110 ns and d = 1100 ns
* Symbols: t (representing the time of the Ramsey response) and d (representing the displacement of the signal)
* Why it matters: This equation represents the parameters used to plot the Ramsey response for the qubit excitation probability. The values of t and d are chosen such that the amplitude of the response is smaller than in the idealized scenario without experimental imperfections.

**Method Summary**
==================

* The authors introduce Quantum Phase-Space Inference (Q Ψ \Psi ), a unifying theory of quantum-enhanced experiments that simultaneously converts a set of experimental objectives and constraints into tight lower bounds and optimal quantum-enhanced learning algorithms.
* The Q Ψ \Psi framework provides a framework for systematically identifying rigorous quantum advantages in practical experimental tasks.
* The authors use a superconducting cavity–qubit architecture to demonstrate exponential quantum advantage for learning classical signals with a single qubit.

**Experimental Overview**
========================

* Tasks/Datasets: The authors use a transmon qubit coupled to the fundamental mode of a 3D stub-post cavity to demonstrate exponential quantum advantage for learning classical signals.
* Baselines/Comparisons: The authors compare their results with conventional sensing protocols, which require access to Gaussian resources with the same energy.
* Main Claimed Findings: The authors demonstrate an exponential quantum advantage of 10^{7} -fold for learning classical signals with a single qubit.

**What to Verify in the PDF**
=============================

* The authors claim that their results establish that near-term quantum technology can exponentially enhance our ability to learn from classical signals. Verify this claim by examining the experimental results and the theoretical framework used to derive the exponential quantum advantage.
* The authors use a transmon qubit coupled to the fundamental mode of a 3D stub-post cavity to demonstrate exponential quantum advantage for learning classical signals. Verify the experimental setup and the parameters used to achieve the exponential quantum advantage.
* The authors introduce Quantum Phase-Space Inference (Q Ψ \Psi ), a unifying theory of quantum-enhanced experiments. Verify the theoretical framework used to derive the Q Ψ \Psi instance and the phase-space representations of the observable and of the response functions generated by protocols in each family.
{% endraw %}

{% raw %}
## 5) The data geometry of masking diffusion: Certified-optimal schedules via unmasking growth complexity
- **Authors:** Martin J. Wainwright
- **arXiv:** [2608.13520](https://arxiv.org/abs/2608.13520v1) · [pdf](https://arxiv.org/pdf/2608.13520v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2608.13520v1))
- **Categories:** cs.LG, cs.AI, cs.IT, math.ST, stat.ML

### Abstract
> We study masking diffusion for discrete sampling and introduce a path-resolved measure of data geometry called the \emph{unmasking growth complexity} ({\textsf{UGC}\xspace}). Its local increments directly control Kullback--Leibler (KL) discretization error, yielding a unified analysis of Bernoulli-subset and fixed-cardinality unmasking schemes. In log-reveal-odds coordinates, this structure yields optimized single-block and multi-block schedules, and quantifies the gains from adapting computational effort to data geometry. Crucially, we show how {\textsf{UGC}\xspace} increments can be estimated from samples via KL increments along coupled reveal trajectories. This leads to \emph{certified-optimal} samplers that achieve a prescribed KL error with high probability and iteration complexity within a constant factor of the corresponding oracle procedure. Collapsing the \ugc path yields the aggregate {\textsf{UGC}\xspace} mass, which connects to classical multivariate dependence measures and complexity measures from previous analyses of discrete diffusion. In the fine-partition limit, the squared integral of the square-root {\textsf{UGC}\xspace} density determines the sharp leading-order optimal Euler discretization error. Examples exhibit substantial dimension-dependent gains over coarse schedules, including $\widetildeΩ(\sqrt{d})$ improvements achievable with a constant number of adaptively placed blocks.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\widetilde{\Omega}(\sqrt{d})$

* Equation: $\widetilde{\Omega}(\sqrt{d})$
* Symbols: $\widetilde{\Omega}$, $d$
* Why it matters: This equation represents the optimal Euler discretization error in the fine-partition limit, which is a key concept in the paper. The notation $\widetilde{\Omega}$ indicates a big-O notation, and $\sqrt{d}$ represents the square root of the dimensionality $d$.

### Equation 2: $Z \in (\mathcal{A})^d$

* Equation: $Z \in (\mathcal{A})^d$
* Symbols: $Z$, $\mathcal{A}$
* Why it matters: This equation represents the set of all possible unmasking schedules $Z$, which is a crucial component in the paper. The notation $(\mathcal{A})^d$ indicates the power set of $\mathcal{A}$, which is a set of all possible subsets of $\mathcal{A}$.

### Equation 3: $\mathcal{A}$

* Equation: $\mathcal{A}$
* Symbols: $\mathcal{A}$
* Why it matters: This equation represents the set of all possible unmasking blocks $\mathcal{A}$. The exact definition of $\mathcal{A}$ is not provided in the extracted context, but it is mentioned as a crucial component in the paper.

### Equation 4: $Z^* = (\star, \ldots, \star)$

* Equation: $Z^* = (\star, \ldots, \star)$
* Symbols: $Z^*$, $\star$
* Why it matters: This equation represents the optimal unmasking schedule $Z^*$, which is a special case of the general unmasking schedule $Z$. The notation $\star$ represents a placeholder or a dummy variable.

### Equation 5: $\star$

* Equation: $\star$
* Symbols: $\star$
* Why it matters: This equation represents a placeholder or a dummy variable used in the notation $Z^* = (\star, \ldots, \star)$. The exact meaning of $\star$ is not provided in the extracted context.

**Method Summary**
================

* The paper introduces a new measure of data geometry called the unmasking growth complexity (UGC), which is used to analyze the performance of masking diffusion algorithms.
* The UGC is defined as a path-resolved measure that directly controls the Kullback-Leibler (KL) discretization error.
* The paper provides a unified analysis of both Bernoulli and fixed-cardinality unmasking samplers using the UGC.
* The UGC is estimated from samples via KL increments along coupled reveal trajectories, which leads to certified-optimal samplers that achieve a prescribed KL error with high probability.

**Experimental Overview**
=========================

* The paper experiments with various datasets and compares the performance of the proposed masking diffusion algorithm with baselines.
* The main claimed findings include:
	+ Substantial dimension-dependent gains over coarse schedules.
	+ Ω ~ (d) improvements achievable with a constant number of adaptively placed blocks.
* The paper also compares the proposed algorithm with the DHW τ-leaping unmasking algorithm.

**What to Verify in the PDF**
=============================

* The proof of Lemma 1 in Section 6.3.1, which provides a data-based certification result.
* The proof of Proposition 2 in Section 6.3.2, which provides a data-based certification result.
* The verification of the score-evaluation budget, which ensures that the procedure terminates in at most N unmasking rounds.
{% endraw %}
