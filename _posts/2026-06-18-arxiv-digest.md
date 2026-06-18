---
layout: post
title: "Daily arXiv Digest — 2026-06-18 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning
- **Authors:** Mohamed Nabail, Leo Cheng, Jingmin Wang, Nicholas Rhinehart
- **arXiv:** [2606.19328](https://arxiv.org/abs/2606.19328v1) · [pdf](https://arxiv.org/pdf/2606.19328v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.19328v1))
- **Categories:** cs.LG, cs.AI, cs.RO

### Abstract
> Preference-based RL provides an approach to learning reward models from pairwise comparisons of behaviors, bypassing the need for explicit reward design. However, existing methods typically rely on passive data collection and suffer from poor sample efficiency, especially during the early stages of learning. We introduce a model-based approach that actively directs exploration by jointly reasoning over uncertainties in the reward, dynamics, and value functions. Our method, Uncertainty-Balanced Preference Planning (UBP2), uses ensembles of reward, dynamics, and value function models to evaluate candidate trajectories according to a unified score that combines expected reward, terminal value, and epistemic uncertainty. Planning under this objective yields an explicit tradeoff between exploitation and information acquisition without requiring ad hoc exploration heuristics. Under standard regularity assumptions, we establish sublinear regret guarantees for both finite-horizon and infinite-horizon settings. Empirically, experiments on the Meta-World benchmark show UBP2 achieves substantially higher sample efficiency than model-free preference-based methods and non-optimistic model-based baselines.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: a_{t=1}

a_{t=1} = \pi(s_t, a_t)

* Equation: This represents the policy at time step t.
* Symbols: π (policy), s_t (state at time t), a_t (action at time t).
* Why it matters: This equation shows how the policy is defined as a mapping from state and action pairs to actions.

### Equation 2: (\mathcal{S},\mathcal{A},p,r,\gamma,\rho_{0})

(\mathcal{S},\mathcal{A},p,r,\gamma,\rho_{0}) = (\text{state space}, \text{action space}, \text{transition model}, \text{reward function}, \text{discount factor}, \text{initial state distribution})

* Equation: This represents the environment and its parameters.
* Symbols: \mathcal{S} (state space), \mathcal{A} (action space), p (transition model), r (reward function), \gamma (discount factor), \rho_0 (initial state distribution).
* Why it matters: This equation shows the components of the environment and their relationships.

### Equation 3: s\in\mathcal{S}

s\in\mathcal{S}

* Equation: This is a simple statement about the state space.
* Symbols: s (state), \mathcal{S} (state space).
* Why it matters: This equation is a placeholder for the state space, which is not explicitly defined in the paper.

### Equation 4: d_{s}

d_{s} = p(s'|s,a)

* Equation: This represents the transition model.
* Symbols: d_s (transition model), s (state), a (action), s' (next state).
* Why it matters: This equation shows how the next state is determined by the current state and action.

### Equation 5: a\in\mathcal{A}

a\in\mathcal{A}

* Equation: This is a simple statement about the action space.
* Symbols: a (action), \mathcal{A} (action space).
* Why it matters: This equation is a placeholder for the action space, which is not explicitly defined in the paper.

**Method Summary**
==================

* UBP2 is a model-based approach that actively directs exploration by jointly reasoning over uncertainties in the reward, dynamics, and value functions.
* UBP2 uses ensembles of reward, dynamics, and value function models to evaluate candidate trajectories according to a unified score that combines expected reward, terminal value, and epistemic uncertainty.
* UBP2 optimizes a loss per-member that combines consistency, reward, and value losses.
* UBP2 selects the most informative preference pairs for labeling by scoring each candidate segment pair using both predicted reward and reward-model epistemic uncertainty.

**Experimental Overview**
=========================

* Tasks/Datasets: UBP2 is evaluated on 10 manipulation tasks of varying degrees of complexity from the MetaWorld benchmark.
* Baselines/Comparisons: UBP2 is compared to the following baselines: RUNE, MRN, and MBP (Model-Based PbRL).
* Main Claimed Findings: UBP2 achieves substantially higher sample efficiency than model-free preference-based methods and non-optimistic model-based baselines.

**What to Verify in the PDF**
=============================

* The mathematical derivations of the UBP2 objective function and the regret bounds.
* The experimental results for the high-dimensional visual observations and DinoV2 encoding experiments.
* The analysis of the conservative evaluation objective and its impact on performance.
{% endraw %}

{% raw %}
## 2) Explaining Attention with Program Synthesis
- **Authors:** Amiri Hayes, Belinda Li, Jacob Andreas
- **arXiv:** [2606.19317](https://arxiv.org/abs/2606.19317v1) · [pdf](https://arxiv.org/pdf/2606.19317v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.19317v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> A longstanding goal of research on interpretable deep learning is to replace opaque neural computations with human-meaningful symbolic descriptions. In this paper, we propose an approach for approximating the behavior of components of deep networks with executable programs. We focus on attention heads in transformer language models. For a given head, we first compute its associated attention matrices on a collection of randomly selected training examples. Next, we prompt a pre-trained language model with a summary of these matrices, and instruct it to generate a set of Python programs that can reproduce the associated attention patterns given only text from the input sentence. Finally, we re-rank programs according to how well our final set of programs predict behavior on held-out inputs. We demonstrate that a set of fewer than 1,000 such generated programs can reproduce the attention patterns of heads in GPT-2, TinyLlama-1.1B, and Llama-3B, achieving an average Intersection-over-Union similarity above 75% on TinyStories. Moreover, the best-fit programs can replace neural attention heads without substantially affecting model behavior: replacing 25% of attention heads with programmatic surrogates across the three models incurs only a 16% average perplexity increase, while maintaining performance on a variety of downstream question answering benchmarks. This work contributes a scalable pipeline for reverse-engineering attention heads in transformer models using human-readable, executable code, advancing a path toward symbolic transparency in neural models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{M}$

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 2: $\mathcal{A}_{i}$

* Equation: Not provided
* Symbols: Not provided
* Why it matters: Not found in extracted context.

### Equation 3: $A=\mathrm{softmax}\left(\frac{QK^{\top}}{\sqrt{d_{k}}}\right)$

* Equation: $A=\mathrm{softmax}\left(\frac{QK^{\top}}{\sqrt{d_{k}}}\right)$
* Symbols: $A$, $Q$, $K$, $d_{k}$
* Why it matters: This equation represents the attention matrix $A$ in a transformer model, where $Q$ and $K$ are query and key matrices, and $d_{k}$ is a dimensionality parameter. The softmax function is used to normalize the attention weights.

### Equation 4: $A\in\mathbb{R}^{n\times n}$

* Equation: $A\in\mathbb{R}^{n\times n}$
* Symbols: $A$, $n$
* Why it matters: This equation states that the attention matrix $A$ is a square matrix of size $n \times n$, where $n$ is the number of tokens in the input sequence.

**Method Summary**
==================

* The authors propose a framework for approximating the behavior of attention heads in transformer models using program synthesis.
* The framework consists of four steps:
	+ Computing attention matrices on a collection of randomly selected training examples.
	+ Prompting a pre-trained language model to generate a set of Python programs that can reproduce the associated attention patterns.
	+ Re-ranking programs according to how well they predict behavior on held-out inputs.
* The authors demonstrate that a set of fewer than 1,000 generated programs can reproduce the attention patterns of heads in GPT-2, TinyLlama-1.1B, and Llama-3B with high accuracy.

**Experimental Overview**
========================

* Tasks/Datasets: The authors evaluate their programs on a variety of downstream question answering benchmarks.
* Baselines/Comparisons: The authors compare their programs to two random baselines (Random Token and Random Column) and a uniform attention baseline.
* Main Claimed Findings: The authors demonstrate that their programs can reproduce the attention patterns of heads in GPT-2, TinyLlama-1.1B, and Llama-3B with high accuracy, and that the best-fit programs can replace neural attention heads without substantially affecting model behavior.

**What to Verify in the PDF**
=============================

* The authors claim that the best program for each head significantly outperforms random and uniform baselines across every model. Verify that this is indeed the case by examining the results of the experiments.
* The authors also claim that the IoU scores increase with model scale. Verify that this is true by examining the results of the experiments on GPT-2, TinyLlama-1.1B, and Llama-3B.
* The authors attribute the poor performance of BERT's synthesized programs to the masked language modeling objective producing bidirectional attention distributions that are more complex and less amenable to symbolic approximation. Verify that this is indeed the case by examining the results of the experiments on BERT.
{% endraw %}

{% raw %}
## 3) Diffusion-Proof: Recipe for Formal Theorem Proving Beyond Auto-Regressive Generation
- **Authors:** Ruida Wang, Rui Pan, Pengcheng Wang, Shizhe Diao, Tong Zhang
- **arXiv:** [2606.19315](https://arxiv.org/abs/2606.19315v1) · [pdf](https://arxiv.org/pdf/2606.19315v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.19315v1))
- **Categories:** cs.LG

### Abstract
> Enhancing the formal math reasoning capabilities of Large Language Models (LLMs) has become a key focus in both mathematical and computer science communities in recent years. While significant progress has been made in using state-of-the-art Auto-Regressive (AR) LLMs for formal theorem proving, these models suffer from inherent limitations. Their next-token prediction generation methods may yield suboptimal performance due to the challenges of long-range coherence and the compounding of errors over long sequences. Recent advancements in diffusion LLMs (dLLMs), which generate text through iterative denoising of a multi-token block, offer a promising alternative. However, the application of dLLMs to formal mathematics, where maintaining long-range coherence is critical, remains largely understudied. To address the challenges above, we propose **Diffusion-Proof**, to the best of our knowledge, the first framework to train and apply dLLMs for formal theorem proving. Our frameworks contain training and inference methods for two models. The first one is *dLLM-Prover-7B*, which performs whole-proof writing with long-range coherent tactic usage. The second one is *dLLM-Corrector-7B*, which is a novel large block diffusion-based correction model. It leverages the in-filling capabilities of dLLMs to perform local proof correction using bi-directional information. Extensive experiments demonstrate that **Diffusion-Proof** relatively significantly outperforms the AR LLM baseline trained under the same dataset. **Diffusion-Proof** achieves an absolute improvement of **1.61%** on ProofNet-Test and **6.14%** on MiniF2F-Test benchmarks compare to the baseline. Notably, **Diffusion-Proof** successfully resolves one IMO problem that more advanced thinking model DeepSeek-Prover-V2-7B could not solve, showcasing the unique advantage of dLLMs in formal theorem proving.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

Here's a walkthrough of the first five extracted equations:

### Equation 1: `x = {x1, x2, ..., xL}`
* Equation: `x = {x1, x2, ..., xL}`
* Symbols: `x`, `L`
* Why it matters: This equation represents a token sequence `x` with length `L`, which is used to denote the input sequence for the diffusion-based model.

### Equation 2: `Pθ(x_i | x[0:i-1])`
* Equation: `Pθ(x_i | x[0:i-1])`
* Symbols: `x_i`, `x[0:i-1]`, `θ`
* Why it matters: This equation represents the conditional probability distribution of `x_i` given the previous tokens `x[0:i-1]`, which is used to model the conditional distribution in the diffusion-based model.

### Equation 3: `θ`
* Equation: `θ`
* Symbols: `θ`
* Why it matters: This equation represents the model's parameters, which are used to define the conditional probability distribution `Pθ(x_i | x[0:i-1])`.

### Equation 4: `t ∈ [0, 1]`
* Equation: `t ∈ [0, 1]`
* Symbols: `t`
* Why it matters: This equation represents the time step `t` in the diffusion process, which is used to update the model's parameters.

### Equation 5: `x^(t)`
* Equation: `x^(t)`
* Symbols: `x^(t)`
* Why it matters: This equation represents the updated input sequence `x` at time step `t`, which is used to compute the conditional probability distribution `Pω(x^(0) | x^(t))`.

**Method Summary**
================

Here's a summary of the method:

* The Diffusion-Proof framework leverages the long-range coherence and in-filling correction capabilities of diffusion-based models for formal theorem proving.
* The framework consists of two models: `dLLM-Prover-7B` and `dLLM-Corrector-7B`.
* `dLLM-Prover-7B` performs whole-proof writing with long-range coherent tactic usage.
* `dLLM-Corrector-7B` is a novel large block diffusion-based correction model that leverages the in-filling capabilities of dLLMs to perform local proof correction using bi-directional information.

**Experimental Overview**
=====================

Here's an overview of the experiments:

* Tasks: Formal theorem proving on MiniF2F-Test and ProofNet-Test benchmarks.
* Datasets: MiniF2F-Test and ProofNet-Test benchmarks.
* Baselines: Qwen-2.5-Instruct-7B and DeepSeek-Prover-V1.5.
* Main claimed findings: Diffusion-Proof achieves significant improvements over the baseline on both MiniF2F-Test and ProofNet-Test benchmarks.

**What to Verify in the PDF**
==========================

Here are some details that still need to be verified in the full paper:

* The implementation details of the `dLLM-Prover-7B` and `dLLM-Corrector-7B` models.
* The analysis of the failed proofs in Appendix D, including the specific limitations of the model.
* The detailed results of the training-loss study in Section 3.4.
* The performance of Diffusion-Proof on harder problems that require longer proofs.
{% endraw %}

{% raw %}
## 4) P-K-GCN: Physics-augmented Koopman-enhanced Graph Convolutional Network for Deep Spatiotemporal Super-resolution
- **Authors:** Xizhuo, Zhang, Zekai Wang, Fei Liu, Bing Yao
- **arXiv:** [2606.19303](https://arxiv.org/abs/2606.19303v1) · [pdf](https://arxiv.org/pdf/2606.19303v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.19303v1))
- **Categories:** cs.LG

### Abstract
> High-fidelity simulation of spatiotemporal dynamics is computationally prohibitive, necessitating efficient super-resolution techniques to reconstruct high-resolution data from coarse-grained inputs. Traditional data-driven methods often lack physical constraints, and simple physics-informed learning struggles with irregular spatial geometries and intricately evolving temporal dynamics. To tackle these challenges, we propose a Physics-augmented Koopman-enhanced Graph Convolutional Network (P-K-GCN) for spatiotemporal super-resolution on irregular geometries. Specifically, a continuous spline-based GCN is first designed to extract spatial dependencies directly from coarse graph, and Koopman operator theory is incorporated to project the nonlinear dynamics into a compact latent space where temporal progression is linearized. Second, we augment the optimization objective with a physics-based loss to force the data-driven reconstructions to adhere to physical laws for improving predictive fidelity and robustness. Finally, we provide a rigorous theoretical analysis, establishing that the physics augmentation and Koopman regularization mathematically guarantees a reduction in super-resolution error by diminishing Rademacher complexity and tightening generalization bounds. We evaluate our framework on reconstructing spatially high-resolution cardiac electrodynamics across a 3D heart geometry from sparse low-resolution measurements. Numerical experiments demonstrate that our method achieves superior accuracy compared to baseline models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Δ

* Equation: Δ
* Symbols: Δ, 
* Why it matters: Not found in extracted context.

### Equation 2: \bm{q}(\bm{x},t)\in\mathbb{R}^{C}

* Equation: 
* Symbols: \bm{q}, \bm{x}, t, C
* Why it matters: Represents the system state at spatial location \bm{x} and time t, with C feature channels.

### Equation 3: \bm{x}

* Equation: 
* Symbols: \bm{x}
* Why it matters: Not found in extracted context.

### Equation 4: \mathcal{X}_{l}=\{\bm{x}_{1},\dots,\bm{x}_{N_{\text{s}}}\}

* Equation: 
* Symbols: \mathcal{X}_{l}, \bm{x}_{i}, N_{\text{s}}
* Why it matters: Represents the set of N_{\text{s}} spatial locations for the low-resolution observations.

### Equation 5: \mathcal{T}=\{t_{1},\dots,t_{N_{\text{t}}}\}

* Equation: 
* Symbols: \mathcal{T}, t_{i}, N_{\text{t}}
* Why it matters: Represents the set of time instances for the low-resolution observations.

**Method Summary**
==================

* The proposed framework combines a graph-based encoder with a Koopman operator formulation to model spatiotemporal dynamics.
* The encoder extracts spatial features from the low-resolution observations and maps them to a compact latent representation space.
* The Koopman operator is used to linearize the nonlinear temporal evolution and propagate the latent state forward.
* Physics-based regularization is incorporated to constrain the reconstructions to remain physically consistent with the underlying dynamical system.

**Experimental Overview**
========================

* Tasks/Datasets: Reconstructing high-resolution cardiac electrodynamics from low-resolution measurements.
* Baselines/Comparisons: Standard neural network (NN), Koopman-based graph convolutional network (K-GCN), and physics-informed neural network (PINN).
* Main Claimed Findings: The proposed P-K-GCN framework achieves superior accuracy compared to the baseline models, with improved robustness to noise and stable temporal evolution.

**What to Verify in the PDF**
=============================

* The mathematical derivation of the Koopman operator formulation and its application to the spatiotemporal super-resolution problem.
* The theoretical analysis of the error mitigation via Koopman regularization, including the derivation of the Rademacher complexity and generalization bounds.
* The experimental results for the 3D ventricular geometry, including the visual comparison of reconstructed transmembrane potential and the quantitative prediction performance under different noise levels.
{% endraw %}

{% raw %}
## 5) UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning
- **Authors:** Mohamed Nabail, Leo Cheng, Jingmin Wang, Nicholas Rhinehart
- **arXiv:** [2606.19328](https://arxiv.org/abs/2606.19328v1) · [pdf](https://arxiv.org/pdf/2606.19328v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.19328v1))
- **Categories:** cs.LG, cs.AI, cs.RO

### Abstract
> Preference-based RL provides an approach to learning reward models from pairwise comparisons of behaviors, bypassing the need for explicit reward design. However, existing methods typically rely on passive data collection and suffer from poor sample efficiency, especially during the early stages of learning. We introduce a model-based approach that actively directs exploration by jointly reasoning over uncertainties in the reward, dynamics, and value functions. Our method, Uncertainty-Balanced Preference Planning (UBP2), uses ensembles of reward, dynamics, and value function models to evaluate candidate trajectories according to a unified score that combines expected reward, terminal value, and epistemic uncertainty. Planning under this objective yields an explicit tradeoff between exploitation and information acquisition without requiring ad hoc exploration heuristics. Under standard regularity assumptions, we establish sublinear regret guarantees for both finite-horizon and infinite-horizon settings. Empirically, experiments on the Meta-World benchmark show UBP2 achieves substantially higher sample efficiency than model-free preference-based methods and non-optimistic model-based baselines.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: a_{t=1}

a_{t=1} = \pi(s_t, a_t)

* Equation: This represents the policy at time step t+1, where π is the policy, s_t is the state at time t, and a_t is the action taken at time t.
* Symbols: π, s_t, a_t
* Why it matters: This equation shows how the policy is defined at each time step, which is crucial for understanding how the policy is updated and improved over time.

### Equation 2: (\mathcal{S},\mathcal{A},p,r,\gamma,\rho_{0})

(\mathcal{S},\mathcal{A},p,r,\gamma,\rho_{0}) = (\text{state space}, \text{action space}, \text{transition model}, \text{reward function}, \text{discount factor}, \text{initial state distribution})

* Equation: This represents the environment and the parameters that define it.
* Symbols: \mathcal{S}, \mathcal{A}, p, r, \gamma, \rho_{0}
* Why it matters: This equation shows the components of the environment and the parameters that are used to define the dynamics and the reward.

### Equation 3: s\in\mathcal{S}

s\in\mathcal{S}

* Equation: This represents the state space.
* Symbols: s, \mathcal{S}
* Why it matters: This equation shows the set of possible states that the environment can be in.

### Equation 4: d_{s}

d_{s} = p(s'|s,a)

* Equation: This represents the transition model, which defines the probability of transitioning from state s to state s' given action a.
* Symbols: d_s, p, s, s', a
* Why it matters: This equation shows how the environment transitions from one state to another given an action.

### Equation 5: a\in\mathcal{A}

a\in\mathcal{A}

* Equation: This represents the action space.
* Symbols: a, \mathcal{A}
* Why it matters: This equation shows the set of possible actions that can be taken in the environment.

**Method Summary**
==================

* UBP2 is a model-based approach that actively directs exploration by jointly reasoning over uncertainties in the reward, dynamics, and value functions.
* UBP2 uses ensembles of reward, dynamics, and value function models to evaluate candidate trajectories according to a unified score that combines expected reward, terminal value, and epistemic uncertainty.
* The method planning under this objective yields an explicit tradeoff between exploitation and information acquisition without requiring ad hoc exploration heuristics.
* UBP2 achieves substantially higher sample efficiency than model-free preference-based methods and non-optimistic model-based baselines.

**Experimental Overview**
========================

* Tasks/Datasets: UBP2 is evaluated on 10 manipulation tasks of varying degrees of complexity from the MetaWorld benchmark.
* Baselines/Comparisons: UBP2 is compared to the following baselines: RUNE, MRN, and MBP.
* Main Claimed Findings: UBP2 achieves substantially higher sample efficiency than model-free preference-based methods and non-optimistic model-based baselines.

**What to Verify in the PDF**
=============================

* The theoretical justification for the sublinear regret guarantees for both finite-horizon and infinite-horizon settings.
* The analysis of the discount factor and its impact on the regret bound.
* The results of the experiments on the MetaWorld benchmark, including the success rates and the impact of varying the planning horizon and the preference feedback budget.
{% endraw %}
