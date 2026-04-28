---
layout: post
title: "Daily arXiv Digest — 2026-04-28 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Conflict-Aware Harmonized Rotational Gradient for Multiscale Kinetic Regimes
- **Authors:** Zhangyong Liang
- **arXiv:** [2604.24745](https://arxiv.org/abs/2604.24745v1) · [pdf](https://arxiv.org/pdf/2604.24745v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.24745v1))
- **Categories:** cs.LG

### Abstract
> In this paper, we propose a harmonized rotational gradient method, termed HRGrad, for simultaneously tackling multiscale time-dependent kinetic problems with varying small parameters. These parameters exhibit asymptotic transitions from microscopic to macroscopic physics, making it a challenging multi-task problem to solve over all ranges simultaneously. Solving tasks in different asymptotic regions often encounter gradient conflicts, which can lead to the failure of multi-task learning. To address this challenge, we explicitly encode a hidden representation of these parameters, ensuring that the corresponding solving tasks are serialized for simultaneous training. Furthermore, to mitigate gradient conflicts, we segment the prediction results to construct task losses and introduce a novel gradient alignment metric to ensure a positive dot product between the final update and each loss-specific gradient. This metric maintains consistent optimization rates for all task losses and dynamically adjusts gradient magnitudes based on conflict levels. Moreover, we provide a mathematical proof demonstrating the convergence of the HRGrad method, which is evaluated across a range of challenging asymptotic-preserving neural networks (APNNs) scenarios. We conduct an extensive set of experiments encompassing the Bhatnagar-Gross-Krook (BGK) equation and the linear transport equation in all ranges of Knudsen number. Our results indicate that HRGrad effectively overcomes the `failure modes' of APNNs in these problems.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: f(t, x, v)

* Equation: `f(t, x, v)`
* Symbols: `f`, `t`, `x`, `v`
* Why it matters: This is the particle distribution function, which describes the evolution of a particle distribution over time, position, and velocity.

### Equation 2: ε

* Equation: Not explicitly defined in the context
* Symbols: `ε`
* Why it matters: The Knudsen number, which represents the ratio of the mean free path to the characteristic length scale, is used to describe the asymptotic behavior of the kinetic equations.

### Equation 3: ∂t f + v∂x f = (1/ε)(M(U) - f)

* Equation: The Boltzmann-BGK equation
* Symbols: `∂t f`, `v`, `f`, `M(U)`, `ε`
* Why it matters: This equation describes the evolution of the particle distribution function `f` over time, taking into account the effects of collisions with the walls and the Maxwellian distribution `M(U)`.

### Equation 4: M(U)

* Equation: The local Maxwellian distribution
* Symbols: `M(U)`, `U`
* Why it matters: The Maxwellian distribution `M(U)` is a statistical distribution that describes the equilibrium distribution of particles in a system, where `U` represents the macroscopic moments (density, velocity, and energy).

### Equation 5: U = ⟨mf⟩ = (ρ, ρu, E)^T

* Equation: The macroscopic moments
* Symbols: `U`, `m`, `ρ`, `u`, `E`
* Why it matters: The macroscopic moments `U` describe the average properties of the particle distribution, such as density, velocity, and energy.

**Method Summary**
==================

* The authors propose a harmonized rotational gradient method, HRGrad, to tackle multiscale kinetic problems with varying small parameters.
* HRGrad explicitly encodes a hidden representation of the parameters to ensure that the corresponding solving tasks are serialized for simultaneous training.
* The method introduces a novel gradient alignment metric to mitigate gradient conflicts and ensures a positive dot product between the final update and each loss-specific gradient.
* HRGrad is evaluated across a range of challenging asymptotic-preserving neural networks (APNNs) scenarios.

**Experimental Overview**
========================

* The authors conduct experiments on several multiscale kinetic equations, including the Boltzmann-BGK equation, the linear transport equation, and two additional kinetic models.
* The proposed HRGrad method is compared to ten popular multi-task learning (MTL) baselines, including PCGrad, IMTL-G, and others.
* The main claimed findings include the effectiveness of HRGrad in overcoming "failure modes" of APNNs and achieving consistent optimization rates across tasks.

**What to Verify in the PDF**
=============================

* The mathematical proof of the convergence of HRGrad for both convex and non-convex settings.
* The detailed implementation of the HRGrad method, including the specific hyperparameter tuning and optimization procedure.
* The experimental results for the additional kinetic models, such as the ES-BGK equation and the linear semiconductor Boltzmann-Poisson equation.
{% endraw %}

{% raw %}
## 2) Learning to Think from Multiple Thinkers
- **Authors:** Nirmit Joshi, Roey Magen, Nathan Srebro, Nikolaos Tsilivis, Gal Vardi
- **arXiv:** [2604.24737](https://arxiv.org/abs/2604.24737v1) · [pdf](https://arxiv.org/pdf/2604.24737v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.24737v1))
- **Categories:** cs.LG, cs.AI, cs.CC, stat.ML

### Abstract
> We study learning with Chain-of-Thought (CoT) supervision from multiple thinkers, all of whom provide correct but possibly systematically different solutions, e.g., step-by-step solutions to math problems written by different thinkers, or step-by-step execution traces of different programs solving the same problem. We consider classes that are computationally easy to learn using CoT supervision from a single thinker, but hard to learn with only end-result supervision, i.e., without CoT (Joshi et al. 2025). We establish that, under cryptographic assumptions, learning can be hard from CoT supervision provided by two or a few different thinkers, in passive data-collection settings. On the other hand, we provide a generic computationally efficient active learning algorithm that learns with a small amount of CoT data per thinker that is completely independent of the target accuracy $\varepsilon$, a moderate number of thinkers that scales as $\log \frac{1}{\varepsilon}\log \log \frac{1}{\varepsilon}$, and sufficient passive end-result data that scales as $\frac{1}{\varepsilon}\cdot poly\log\frac{1}{\varepsilon}$.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: ε

* Equation: ε
* Symbols: ε
* Why it matters: ε represents the error tolerance or accuracy threshold. It is a key parameter in the learning algorithm, and the algorithm's performance is measured in terms of its ability to achieve a certain level of accuracy (i.e., ε) on the target distribution.

### Equation 2: log(1/ε) log log(1/ε)

* Equation: log(1/ε) log log(1/ε)
* Symbols: ε, log
* Why it matters: This equation represents the lower bound on the number of examples required to achieve a certain level of accuracy (ε) using the Chain-of-Thought (CoT) supervision. The logarithmic terms indicate that the number of examples grows exponentially with the inverse of ε.

### Equation 3: (1/ε) ⋅ poly(log(1/ε))

* Equation: (1/ε) ⋅ poly(log(1/ε))
* Symbols: ε, poly, log
* Why it matters: This equation represents the upper bound on the number of CoT examples required to achieve a certain level of accuracy (ε) using the Chain-of-Thought (CoT) supervision. The term "poly" indicates that the number of examples grows polynomially with the inverse of ε.

### Equation 4: κ ||T||

* Equation: κ ||T||
* Symbols: κ, ||T||
* Why it matters: This equation represents the hardness parameter, which is related to the number of rounds of CoT examples required to achieve a certain level of accuracy (ε). The term "||T||" represents the number of rounds, and κ is a constant that depends on the specific problem instance.

### Equation 5: GapSVP

* Equation: GapSVP
* Symbols: GapSVP
* Why it matters: GapSVP is a problem in computational complexity theory, which is related to the hardness of learning with Chain-of-Thought (CoT) supervision. The problem involves finding a shortest vector in a lattice, and it is used as a benchmark for the hardness of learning with CoT supervision.

### Equation 6: SIVP

* Equation: SIVP
* Symbols: SIVP
* Why it matters: SIVP is another problem in computational complexity theory, which is related to the hardness of learning with Chain-of-Thought (CoT) supervision. The problem involves finding a shortest vector in a lattice, and it is used as a benchmark for the hardness of learning with CoT supervision.

### Equation 7: f: {0,1}^* → {0,1}

* Equation: f: {0,1}^* → {0,1}
* Symbols: f, {0,1}^*, {0,1}
* Why it matters: This equation represents the input space of the learning algorithm, which consists of all possible binary strings. The function f is a mapping from this input space to the output space {0,1}.
{% endraw %}

{% raw %}
## 3) SpecRLBench: A Benchmark for Generalization in Specification-Guided Reinforcement Learning
- **Authors:** Zijian Guo, İlker Işık, H. M. Sabbir Ahmad, Wenchao Li
- **arXiv:** [2604.24729](https://arxiv.org/abs/2604.24729v1) · [pdf](https://arxiv.org/pdf/2604.24729v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.24729v1))
- **Categories:** cs.LG

### Abstract
> Specification-guided reinforcement learning (RL) provides a principled framework for encoding complex, temporally extended tasks using formal specifications such as linear temporal logic (LTL). While recent methods have shown promising results, their ability to generalize across unseen specifications and diverse environments remains insufficiently understood. In this work, we introduce SpecRLBench, a benchmark designed to evaluate the generalization capabilities of LTL-based specification-guided RL methods. The benchmark spans multiple difficulty levels across navigation and manipulation domains, incorporating both static and dynamic environments, diverse robot dynamics, and varied observation modalities. Through extensive empirical evaluation, we characterize the strengths and limitations of existing approaches and reveal the challenges that emerge as specification and environment complexity increase. SpecRLBench provides a structured platform for systematic comparison and supports the development of more generalizable specification-guided RL methods. Code is available at https://github.com/BU-DEPEND-Lab/SpecRLBench.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, r, \gamma, d_0)$

* Equation: $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, r, \gamma, d_0)$
* Symbols:
	+ $\mathcal{M}$: Markov decision process
	+ $\mathcal{S}$: state space
	+ $\mathcal{A}$: action space
	+ $P$: transition model
	+ $r$: reward function
	+ $\gamma$: discount factor
	+ $d_0$: initial state distribution
* Why it matters: This equation defines the basic structure of a Markov decision process, which is a fundamental concept in reinforcement learning.

### Equation 2: $\mathcal{S}$

* Equation: $\mathcal{S}$
* Symbols: None
* Why it matters: This equation is not fully defined in the context, but it appears to represent the state space of the Markov decision process.

### Equation 3: $\mathcal{A}$

* Equation: $\mathcal{A}$
* Symbols: None
* Why it matters: This equation is not fully defined in the context, but it appears to represent the action space of the Markov decision process.

### Equation 4: $P: \mathcal{S} \times \mathcal{A} \times \mathcal{S} \rightarrow [0, 1]$

* Equation: $P: \mathcal{S} \times \mathcal{A} \times \mathcal{S} \rightarrow [0, 1]$
* Symbols:
	+ $P$: transition model
	+ $\mathcal{S}$: state space
	+ $\mathcal{A}$: action space
* Why it matters: This equation defines the transition model, which specifies the probability of transitioning from one state to another given an action.

### Equation 5: $r: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$

* Equation: $r: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$
* Symbols:
	+ $r$: reward function
	+ $\mathcal{S}$: state space
	+ $\mathcal{A}$: action space
* Why it matters: This equation defines the reward function, which specifies the reward received for taking an action in a particular state.

### Equation 6: $\gamma \in (0, 1)$

* Equation: $\gamma \in (0, 1)$
* Symbols:
	+ $\gamma$: discount factor
* Why it matters: This equation defines the discount factor, which determines the importance of future rewards.

### Equation 7: $d_0 \in \Delta(\mathcal{S})$

* Equation: $d_0 \in \Delta(\mathcal{S})$
* Symbols:
	+ $d_0$: initial state distribution
	+ $\Delta(\mathcal{S})$: set of probability distributions over $\mathcal{S}$
* Why it matters: This equation defines the initial state distribution, which specifies the probability distribution of the initial state.

### Equation 8: $\pi: \mathcal{S} \times \mathcal{A} \mapsto [0, 1]$

* Equation: $\pi: \mathcal{S} \times \mathcal{A} \mapsto [0, 1]$
* Symbols:
	+ $\pi$: policy
	+ $\mathcal{S}$: state space
	+ $\mathcal{A}$: action space
* Why it matters: This equation defines the policy, which specifies the probability of taking an action in a particular state.

**Method Summary**
================

* The authors introduce SpecRLBench, a benchmark for evaluating the generalization capabilities of specification-guided reinforcement learning methods.
* The benchmark includes navigation and manipulation tasks in both single-agent and multi-agent settings.
* The authors evaluate five baselines: LTL2Action, GCRL-LTL, DeepLTL, GenZ-LTL, and RAD-Embeddings.
* The results show that the baselines exhibit varying levels of performance across different tasks and environments.

**Experimental Overview**
=======================

* Tasks/Datasets: The benchmark includes navigation and manipulation tasks in both single-agent and multi-agent settings.
* Baselines/Comparisons: The authors compare five baselines: LTL2Action, GCRL-LTL, DeepLTL, GenZ-LTL, and RAD-Embeddings.
* Main claimed findings: The results show that the baselines exhibit varying levels of performance across different tasks and environments.

**What to Verify in the PDF**
==========================

* The authors claim that the benchmark includes multiple difficulty levels across navigation and manipulation domains, incorporating both static and dynamic environments, diverse robot dynamics, and varied observation modalities. Verify that this is indeed the case by checking the environments and tasks described in Section 4.
* The authors also claim that the benchmark supports the development of more generalizable specification-guided RL methods. Verify that this is the case by checking the experimental results and the discussion of the limitations of the baselines.
* The authors mention that the code is available at https://github.com/BU-DEPEND-Lab/SpecRLBench. Verify that this is indeed the case and that the code is well-documented and easy to use.
{% endraw %}

{% raw %}
## 4) Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling
- **Authors:** Parsa Ashrafi Fashi, Utkarsh Saxena, Mehdi Rezagholizadeh, Aref Jafari, Akash Haridas, Mingyu Yang, Vansh Bhatia, Guihong Li, Vikram Appia, Emad Barsoum
- **arXiv:** [2604.24715](https://arxiv.org/abs/2604.24715v1) · [pdf](https://arxiv.org/pdf/2604.24715v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.24715v1))
- **Categories:** cs.CL, cs.LG

### Abstract
> Hybrid sequence models that combine efficient Transformer components with linear sequence modeling blocks are a promising alternative to pure Transformers, but most are still pretrained from scratch and therefore fail to reuse existing Transformer checkpoints. We study upcycling as a practical path to convert pretrained Transformer LLMs into hybrid architectures while preserving short-context quality and improving long-context capability. We call our solution \emph{HyLo} (HYbrid LOng-context): a long-context upcycling recipe that combines architectural adaptation with efficient Transformer blocks, Multi-Head Latent Attention (MLA), and linear blocks (Mamba2 or Gated DeltaNet), together with staged long-context training and teacher-guided distillation for stable optimization. HyLo extends usable context length by up to $32\times$ through efficient post-training and reduces KV-cache memory by more than $90\%$, enabling up to 2M-token prefill and decoding in our \texttt{vLLM} inference stack, while comparable Llama baselines run out of memory beyond 64K context. Across 1B- and 3B-scale settings (Llama- and Qwen-based variants), HyLo delivers consistently strong short- and long-context performance and significantly outperforms state-of-the-art upcycled hybrid baselines on long-context evaluations such as RULER. Notably, at similar scale, HyLo-Qwen-1.7B trained on only 10B tokens significantly outperforms JetNemotron (trained on 400B tokens) on GSM8K, Lm-Harness common sense reasoning and RULER-64K.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: 
\clubsuit

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not provided

### Equation 2: 
32×

* Equation: Not provided
* Symbols: ×
* Why it matters: Indicates the factor by which the context length is extended.

### Equation 3: 
90%

* Equation: Not provided
* Symbols: %
* Why it matters: Indicates the percentage reduction in KV-cache memory.

### Equation 4: 
×

* Equation: Not provided
* Symbols: ×
* Why it matters: Indicates the ratio of MLA to linear blocks.

### Equation 5: 
3.9%

* Equation: Not provided
* Symbols: %
* Why it matters: Not provided

**Method Summary**
==================

* The proposed method, HyLo, is a long-context aware upcycling recipe that combines efficient Transformer components with linear sequence modeling blocks.
* HyLo extends usable context length by up to 32× through efficient post-training and reduces KV-cache memory by more than 90%.
* The method uses staged long-context training and teacher-guided distillation for stable optimization.
* HyLo generalizes across architectures and scales, and is effective for both short- and long-context tasks.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Common Sense Reasoning
	+ GSM8K
	+ RULER
* Baselines/Comparisons:
	+ Llama baselines
	+ JetNemotron
* Main Claimed Findings:
	+ HyLo outperforms state-of-the-art upcycled hybrid baselines on long-context evaluations.
	+ HyLo significantly improves long-context performance, while maintaining comparable short-context performance.

**What to Verify in the PDF**
=============================

* The full implementation details of the HyLo recipe, including the specific architecture and training hyperparameters.
* The effectiveness of the YaRN position interpolation technique for extending context length.
* The impact of knowledge distillation on long-context learning, including the role of teacher models and training token budgets.
{% endraw %}

{% raw %}
## 5) Scalable Hyperparameter-Divergent Ensemble Training with Automatic Learning Rate Exploration for Large Models
- **Authors:** Hailing Cheng, Tao Huang, Chen Zhu, Antonio Alonso
- **arXiv:** [2604.24708](https://arxiv.org/abs/2604.24708v1) · [pdf](https://arxiv.org/pdf/2604.24708v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.24708v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Training large neural networks with data-parallel stochastic gradient descent allocates N GPU replicas to compute effectively identical updates -- a practice that leaves the rich space of learning rate configurations entirely unexplored during training. We propose Hyperparameter-Divergent Ensemble Training (HDET), a method that repurposes these replicas for simultaneous learning rate exploration at negligible communication overhead. HDET operates in alternating phases: a fan-out stage in which replicas train independently under a structured, symmetric spread of learning rates, and a converge stage in which parameters are averaged across all replicas via AllReduce every T steps. Building on this ensemble substrate, we further propose an automatic learning rate (auto-LR) controller that treats the relative training loss across replicas as a performance signal, updating the shared base schedule toward higher-performing configurations via a momentum-based gradient-free meta-update. The combined method produces a self-adapting learning rate schedule that improves both optimization quality and generalization without additional hyperparameter sweeps or training budget. Crucially, the framework generalizes beyond learning rate: any scalar hyperparameter that does not alter model architecture -- such as dropout rate, attention scale temperature, or weight-decay coefficient -- can be explored across replicas using the same fan-out/converge protocol, with inter-replica loss differences serving as zero-order hypergradients that guide the search direction. HDET is implemented as a drop-in replacement for PyTorch's OneCycleLR scheduler, requiring no changes to model architecture, optimizer, or data pipeline.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: [\bar{\eta}\,(1-\alpha),\;\bar{\eta}\,(1+\alpha)]

* Equation: `[\bar{\eta}\,(1-\alpha),\;\bar{\eta}\,(1+\alpha)]`
* Symbols:
	+ `\bar{\eta}`: average learning rate
	+ `\alpha`: learning rate spread factor
* Why it matters: This equation represents the two learning rates used in the fan-out stage of HDET. The first term `\bar{\eta}\,(1-\alpha)` is the learning rate for the replicas that are farther away from the optimal learning rate, while the second term `\bar{\eta}\,(1+\alpha)` is the learning rate for the replicas that are closer to the optimal learning rate.

### Equation 2: \bar{\eta}^{(t)}

* Equation: `\bar{\eta}^{(t)}`
* Symbols:
	+ `\bar{\eta}`: average learning rate
	+ `t`: time step
* Why it matters: This equation represents the average learning rate at time step `t`. It is used to update the learning rate in the converge stage of HDET.

### Equation 3: \alpha\geq 0

* Equation: `\alpha\geq 0`
* Symbols:
	+ `\alpha`: learning rate spread factor
* Why it matters: This equation represents the constraint on the learning rate spread factor `\alpha`. It ensures that `\alpha` is non-negative, which is necessary for the learning rate spread to be effective.

### Equation 4: \theta_{r}^{(t)}=\theta^{(t)}

* Equation: `\theta_{r}^{(t)}=\theta^{(t)}`
* Symbols:
	+ `\theta_{r}^{(t)}`: replica parameters at time step `t`
	+ `\theta^{(t)}`: model parameters at time step `t`
* Why it matters: This equation represents the update rule for the replica parameters `\theta_{r}^{(t)}`. In the converge stage, the replica parameters are updated by averaging the model parameters `\theta^{(t)}`.

### Equation 5: N\times

* Equation: `N\times`
* Symbols:
	+ `N`: number of replicas
* Why it matters: This equation represents the number of replicas used in the fan-out stage of HDET. The number of replicas is a hyperparameter that controls the level of parallelism in the training process.

### Equation 6: \bar{\theta}^{(kT)}

* Equation: `\bar{\theta}^{(kT)}`
* Symbols:
	+ `\bar{\theta}`: average model parameters
	+ `k`: number of iterations
	+ `T`: number of steps in the converge stage
* Why it matters: This equation represents the average model parameters after `k` iterations and `T` steps in the converge stage. It is used to update the model parameters in the converge stage.

### Equation 7: \eta_{0}=(1{-}\alpha)\bar{\eta}

* Equation: `\eta_{0}=(1{-}\alpha)\bar{\eta}`
* Symbols:
	+ `\eta_{0}`: initial learning rate
	+ `\bar{\eta}`: average learning rate
	+ `\alpha`: learning rate spread factor
* Why it matters: This equation represents the initial learning rate `\eta_{0}` used in the fan-out stage. It is calculated as a weighted average of the average learning rate `\bar{\eta}` and the learning rate spread factor `\alpha`.

### Equation 8: \eta_{1}

* Equation: `\eta_{1}`
* Symbols:
	+ `\eta_{1}`: learning rate at time step 1
* Why it matters: This equation represents the learning rate at time step 1. It is used to update the learning rate in the fan-out stage.

**Method Summary**
================

* HDET (Hyperparameter-Divergent Ensemble Training) is a method for training large neural networks with automatic learning rate exploration.
* HDET operates in two stages: a fan-out stage and a converge stage.
* In the fan-out stage, replicas are trained independently under a structured, symmetric spread of learning rates.
* In the converge stage, parameters are averaged across all replicas via AllReduce every `T` steps.
* An automatic learning rate (auto-LR) controller is used to update the shared base schedule toward higher-performing configurations via a momentum-based gradient-free meta-update.

**Experimental Overview**
========================

* Tasks: HDET is evaluated on a production-scale news-feed dataset from a major social network, comprising one year of user–item interaction logs.
* Baselines: Baseline-High, Baseline-Low, Warm-Init, and Baseline-Low without auto-LR are compared to HDET.
* Main claimed findings: HDET improves optimization quality and generalization without additional hyperparameter sweeps or training budget.

**What to Verify in the PDF**
=============================

* The implementation details of the auto-LR controller, including the momentum-based gradient-free meta-update.
* The effect of the learning rate spread factor `\alpha` on the performance of HDET.
* The impact of the number of replicas `N` on the training time and accuracy of HDET.
{% endraw %}
