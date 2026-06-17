---
layout: post
title: "Daily arXiv Digest — 2026-06-17 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Learning Red Agent Policy from Observations for Neurosymbolic Autonomous Cyber Agents
- **Authors:** Ankita Samaddar, Sandeep Neema, Daniel Balasubramanian, Xenofon Koutsoukos
- **arXiv:** [2606.18223](https://arxiv.org/abs/2606.18223v1) · [pdf](https://arxiv.org/pdf/2606.18223v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.18223v1))
- **Categories:** cs.CR, cs.AI, cs.LG, eess.SY

### Abstract
> With sophisticated cyber-attacks becoming increasingly prevalent, modern networks require intelligent autonomous cyber-defense agents trained via Reinforcement Learning (RL). These agents employ neurosymbolic approaches such as behavior trees with learning-enabled components (LECs) to learn, reason, adapt, and implement security rules while maintaining critical operations. However, these autonomous networks are partially observable systems, i.e., the cyber-attacker's (red agent's) actions are not observable, making it difficult for the defender to predict red actions, learn red policies, or assess the attacker's intrusion levels. To address this, we propose a Policy Learning Technique using imitation learning to learn policies for partially observable RL agents with discrete states and discrete actions. We apply this technique in an autonomous cyber environment to predict red agent's actions from network observations and defender actions. Integrated with a neurosymbolic cyber-defense agent, our method effectively handles different red policies and achieves high prediction accuracy across diverse simulated scenarios.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Meander

Equation: `Meander`
Symbols: `Meander`
Why it matters: This equation is not explicitly defined in the context, but it seems to be related to the Meander behavior in the dynamics model.

### Equation 2: B_line

Equation: `B_line`
Symbols: `B_line`
Why it matters: This equation is not explicitly defined in the context, but it seems to be related to the B_line behavior in the dynamics model.

### Equation 3: RedSwitch

Equation: `RedSwitch`
Symbols: `RedSwitch`
Why it matters: This equation is not explicitly defined in the context, but it seems to be related to the RedSwitch strategy in the dynamics model.

### Equation 4: Running

Equation: `Running`
Symbols: `Running`
Why it matters: This equation is not explicitly defined in the context, but it seems to be related to the Running behavior in the dynamics model.

### Equation 5: Success

Equation: `Success`
Symbols: `Success`
Why it matters: This equation is not explicitly defined in the context, but it seems to be related to the Success behavior in the dynamics model.

**Method Summary**
==================

* The proposed method uses imitation learning to learn policies for partially observable RL agents with discrete states and discrete actions.
* The method is integrated with a neurosymbolic cyber-defense agent to handle different red policies and achieve high prediction accuracy across diverse simulated scenarios.
* The method uses a three-stage dynamics model to predict red actions, with Stage 1 using inverse dynamics, Stage 2 using imitation learning, and Stage 3 using forward dynamics.

**Experimental Overview**
========================

* Tasks/Datasets: The method is evaluated in the CybORG CAGE Challenge 2 environment.
* Baselines/Comparisons: The method is compared to two adversarial strategies, B_line and Meander, and a third strategy, RedSwitch.
* Main Claimed Findings: The method achieves high prediction accuracy across diverse simulated scenarios, with the highest accuracy observed under the B_line strategy.

**What to Verify in the PDF**
=============================

* The details of the dynamics model, including the definitions of the Meander, B_line, RedSwitch, Running, and Success behaviors.
* The implementation of the imitation learning algorithm and the three-stage dynamics model.
* The evaluation metrics used to measure the performance of the method, including prediction accuracy and bit-level prediction errors.
{% endraw %}

{% raw %}
## 2) Looped World Models
- **Authors:** Hongyuan Adam Lu, Z. L. Victor Wei, Qun Zhang, Jinrui Zeng, Bowen Cao, Lingwei Meng, Mocheng Li, Zezhong Wang, Haonan Yin, Naifu Xue, Minyu Chen, Cenyuan Zhang, Zefan Zhang, Hao Wei, Jiawei Zhou, Haoran Xu, Hao Yang, Ronglai Zuo, Tongda Xu, Yonghao Li, Jian Chen, Hebin Wang, Zeyu Gao, Yang Li, Wei Zhao, Qimin Zhong, Siqi Liu, Yumeng Zhang, Leyan Cui, Zhangyu Wang, Wai Lam
- **arXiv:** [2606.18208](https://arxiv.org/abs/2606.18208v1) · [pdf](https://arxiv.org/pdf/2606.18208v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.18208v1))
- **Categories:** cs.LG, cs.AI, cs.CL, cs.CV

### Abstract
> Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this by introducing Looped World Models (LoopWM), which are the first looped architectures for world modelling. Our method iteratively refines latent environment states through a parameter-shared transformer block. This yield up to 100x parameter efficiency over conventional approaches with adaptive computation that automatically scales depth to match the complexity of each prediction step. Orthogonal to scaling model size and training data, LoopWM establishes iterative latent depth as a new scaling axis for world simulation, which might significantly push the community forward.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: Not found in extracted context.

### Equation 2: Not found in extracted context.

### Equation 3: 
\[ s_{t} \]
Matters: This equation represents the latent environment state at time t.

### Equation 4: 
\[ s_{t+1} \]
Matters: This equation represents the updated latent environment state at time t+1.

### Equation 5: 
\[ f_{\theta} \]
Matters: This equation represents the function that takes the latent environment state and outputs a new state.

### Equation 6: 
\[ h_{t+1}=\bar{A}\,h_{t}+\bar{B}\,e+\bar{\mathcal{R}}(h_{t},e) \]
Matters: This equation represents the recursive update of the latent environment state using a transformer block. It combines the previous state, a new action, and a reward to produce the next state.

**Method Summary**
================

* Looped World Models (LoopWM) are a new architecture for world modeling that iteratively refines latent environment states through a parameter-shared transformer block.
* The model uses stochastic loop depth, which is sampled from a Poisson distribution with a learnable mean.
* The model has two variants: deferred decoding and non-deferred decoding.
* The deferred decoding variant requires the model to maintain accurate latent representations across K action-conditioned transitions without intermediate reconstruction supervision.

**Experimental Overview**
=====================

* Tasks/Datasets: ScienceWorld and AlfWorld datasets.
* Baselines/Comparisons: claude-opus-4-6-max, qwen-3.5-flash, and gemini-3-flash-preview.
* Main Claimed Findings: The proposed model surpasses the strong baseline claude-opus-4-6-max on the ScienceWorld dataset, and achieves promising results on the AlfWorld dataset.

**What to Verify in the PDF**
==========================

* The implementation details of the stochastic loop depth and the parameter-shared transformer block.
* The definition of the terminal prediction loss and the latent trajectory regularizer used in the deferred decoding variant.
* The detailed action categories and entity scores used to evaluate the model on the AlfWorld dataset.
{% endraw %}

{% raw %}
## 3) Kolmogorov Regression for Robust Diffusion Policies
- **Authors:** Lekan Molu
- **arXiv:** [2606.18186](https://arxiv.org/abs/2606.18186v1) · [pdf](https://arxiv.org/pdf/2606.18186v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.18186v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Finite-dimensional (FD) diffusion policies exhibit temporal drift owing to discretization artifacts that degrade long-horizon performance (when deployed on physical systems). We introduce a backward Kolmogorov equation that lifts diffusion policies to a Cameron-Martin space -- a subset of the Hilbert space. Essentially, replacing stochastic score matching with a deterministic boundary-value PDE problem. Our core innovation thrives on Gaussian measure theory whereupon the diffusion noise covariance operator is realized from a colored noise distribution which prescribes a notion of regularity on samples from the model at inference time. We train the diffusion model with a derived precision-weighted Cameron- Martin loss and a Kolmogorov residual is introduced as a PDE diagnostic during inference. These substitutions yield (i) convergence guarantees where the bound's constants depend on the effective rank of the kernel rather than action dimension, (ii) improved trajectory regularity via spectral weighting, and (iii) a deterministic failure detector without reward signals. Validation across two application domains demonstrates substantial improvements: on the PushT manipulation benchmark, the Cameron-Martin loss achieves a 17% improvement in maximum episode reward (0.95 vs. 0.78 for MSE) and 67.6% reduction in inter-step drifts during inference via the introduced residual magnitude. Similarly, on a 6-station manufacturing line with constant work-in-process (CONWIP) flow control, we achieve 28.4% lower RMSE than classical LSTM baselines; a high starvation-event recall (1.0 in test cycles), and effective bottleneck identification (Precision@1 = 1.0 in test set, 13x signal-to-noise ratio). We then certify the dispatch policies with Hamilton-Jacobi reachability theory which reduces deadlock events by 96% compared to uncontrolled dispatch over 100 simulated runs (351 events prevented).
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Covariance Operator Definition

\[ C_{\mu} = \int_{\mathcal{H}} \langle x, x \rangle_{\mathcal{H}} \mu(dx) \]

Symbols:
- \( C_{\mu} \): Covariance operator
- \( \mu \): Gaussian measure
- \( \langle \cdot, \cdot \rangle_{\mathcal{H}} \): Inner product on Hilbert space \( \mathcal{H} \)
- \( x \): Random variable in \( \mathcal{H} \)

Why it matters: This equation defines the covariance operator, which is crucial for understanding the behavior of the diffusion policy in the Cameron-Martin space.

### Equation 2: Cameron-Martin Loss

\[ \mathcal{L}_{CM} = \frac{1}{2} \int_{\mathcal{H}} \| \nabla u^* \|^2_{\mathcal{H}} \mu(dx) \]

Symbols:
- \( \mathcal{L}_{CM} \): Cameron-Martin loss
- \( u^* \): Value function
- \( \nabla u^* \): Gradient of value function
- \( \mu \): Gaussian measure
- \( \langle \cdot, \cdot \rangle_{\mathcal{H}} \): Inner product on Hilbert space \( \mathcal{H} \)

Why it matters: This equation defines the Cameron-Martin loss, which is used to train the diffusion policy in the Cameron-Martin space.

### Equation 3: MSE Loss

\[ \mathcal{L}_{MSE} = \frac{1}{2} \int_{\mathcal{H}} \| u^* - u \|^2_{\mathcal{H}} \mu(dx) \]

Symbols:
- \( \mathcal{L}_{MSE} \): Mean Squared Error loss
- \( u^* \): Value function
- \( u \): Estimated value function
- \( \mu \): Gaussian measure
- \( \langle \cdot, \cdot \rangle_{\mathcal{H}} \): Inner product on Hilbert space \( \mathcal{H} \)

Why it matters: This equation defines the Mean Squared Error loss, which is used as a baseline for comparison.

### Equation 4: Kolmogorov Residual

\[ \mathcal{R} = \int_{\mathcal{H}} \| \nabla u^* \|^2_{\mathcal{H}} \mu(dx) - \int_{\mathcal{H}} \| \nabla u \|^2_{\mathcal{H}} \mu(dx) \]

Symbols:
- \( \mathcal{R} \): Kolmogorov residual
- \( u^* \): Value function
- \( u \): Estimated value function
- \( \mu \): Gaussian measure
- \( \langle \cdot, \cdot \rangle_{\mathcal{H}} \): Inner product on Hilbert space \( \mathcal{H} \)

Why it matters: This equation defines the Kolmogorov residual, which is used as a diagnostic for policy trustworthiness.

### Equation 5: Hamilton-Jacobi Reachability

\[ \mathcal{R} = \int_{\mathcal{H}} \| \nabla u^* \|^2_{\mathcal{H}} \mu(dx) - \int_{\mathcal{H}} \| \nabla u \|^2_{\mathcal{H}} \mu(dx) \]

Symbols:
- \( \mathcal{R} \): Hamilton-Jacobi reachability
- \( u^* \): Value function
- \( u \): Estimated value function
- \( \mu \): Gaussian measure
- \( \langle \cdot, \cdot \rangle_{\mathcal{H}} \): Inner product on Hilbert space \( \mathcal{H} \)

Why it matters: This equation defines the Hamilton-Jacobi reachability, which is used to certify safe dispatch decisions.

**Method Summary**
==================

* The authors introduce a backward Kolmogorov equation that lifts diffusion policies to a Cameron-Martin space.
* The Cameron-Martin loss is used to train the diffusion policy in the Cameron-Martin space.
* The Kolmogorov residual is introduced as a PDE diagnostic during inference.
* The authors use Gaussian measure theory to realize the diffusion noise covariance operator.
* The authors use spectral analysis to understand the behavior of the diffusion policy.

**Experimental Overview**
=========================

* The authors validate the framework on two application domains: PushT manipulation and manufacturing control.
* The authors compare the Cameron-Martin loss against MSE and a weighted mixed-precision loss baselines.
* The authors achieve substantial improvements in maximum episode reward and reduction in inter-step drifts.
* The authors demonstrate interpretable behavior of the infinite-dimensional framework.

**What to Verify in the PDF**
=============================

* The authors claim that the Cameron-Martin loss achieves lower final training loss and higher inference rewards than MSE.
* The authors claim that the Kolmogorov residual correlates strongly with task success and provides an oracle-free diagnostic for policy trustworthiness.
* The authors claim that the infinite-dimensional framework demonstrates better convergence rates, higher task success, lower Kolmogorov residuals, and a principled diagnostic that requires no ground-truth reward signals.
* The authors claim that the Hamilton-Jacobi reachability reduces deadlock events by 96% compared to uncontrolled dispatch.
{% endraw %}

{% raw %}
## 4) A Convex Quasilinearization Method for Solving Nonlinear PDEs with Physics-Informed Neural Networks
- **Authors:** Gbenga T. Awojinrin, Abdul-Akeem Olawoyin, Rami M. Younis
- **arXiv:** [2606.18175](https://arxiv.org/abs/2606.18175v1) · [pdf](https://arxiv.org/pdf/2606.18175v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.18175v1))
- **Categories:** math.NA, cs.LG, physics.comp-ph

### Abstract
> We present a numerical method for the forward solution of nonlinear partial differential equations (PDEs) in which Bellman-Kalaba quasilinearization reduces the nonlinear problem to a sequence of linear subproblems, each discretized by collocation onto a trial space that is linear in its parameters and solved by a single direct linear least-squares QR factorization. The trial space, which we term Linear-in-Learnables (LiL), comprises representations whose trainable parameters enter linearly, including random-feature extreme learning machines, spectral polynomial bases, and trigonometric expansions, each implemented as a physics-informed neural network. The method thus replaces the nonconvex gradient-based training that limits standard PINNs with a convex per-step solve. We establish local Newton-Kantorovich convergence of the outer iteration to a residual-limited neighborhood under an explicit smallness condition, with the limiting accuracy governed by the best-approximation residual of the trial space rather than by an optimization tolerance. The method, denoted LiL-Q, is assessed on seven benchmarks spanning scalar nonlinear PDEs (Bratu, viscous Burgers, Buckley-Leverett), coupled systems (plane-strain elasticity and the incompressible Navier-Stokes equations in two and three spatial dimensions), and steady-state Darcy flow with heterogeneous permeability. Across these problems, LiL-Q converges in single-digit outer iterations in most cases, even at the coarsest basis sizes and independent of the parameter count. When the exact solution lies in the span of the trial space, the method recovers it to machine precision in a single solve. On the Navier-Stokes benchmarks, it matches or exceeds published PINN solvers with up to two orders of magnitude fewer trainable parameters, without gradient-based optimization.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Nonlinear PDE
```math
\mathcal{N}(u) = 0, \qquad \mathbf{x} \in \bar{\Omega}
```
* Equation: Nonlinear PDE
* Symbols: `u` (solution), `x` (input), `N` (nonlinear operator)
* Why it matters: This is the original nonlinear PDE that the method aims to solve.

### Equation 2: Domain
```math
\Omega \subset \mathbb{R}^{d}
```
* Equation: Domain
* Symbols: `Omega` (domain), `d` (dimension)
* Why it matters: This defines the spatial domain where the PDE is defined.

### Equation 3: Solution
```math
u: \bar{\Omega} \to \mathbb{R}
```
* Equation: Solution
* Symbols: `u` (solution), `Omega` (domain), `R` (target space)
* Why it matters: This defines the solution space of the PDE.

### Equation 4: Nonlinear Operator
```math
\mathcal{N}
```
* Equation: Nonlinear Operator
* Symbols: `N` (nonlinear operator)
* Why it matters: This is the nonlinear operator that acts on the solution `u` to produce the residual.

### Equation 5: Network Output
```math
\hat{u}(\mathbf{x}; \boldsymbol{\theta})
```
* Equation: Network Output
* Symbols: `u` (solution), `x` (input), `theta` (parameters), `hat` (network output)
* Why it matters: This is the output of the network, which approximates the solution `u`.

**Method Summary**
==================

* The proposed method, LiL-Q, uses Bellman-Kalaba quasilinearization to linearize the nonlinear PDE, and then solves the resulting linear subproblem using a linear-in-learnables (LiL) representation.
* The LiL representation is a linear-in-learnables network or basis expansion, where the trainable parameters enter the solution linearly.
* The method replaces the nonconvex gradient-based training with a convex per-step solve, which improves convergence reliability and attainable accuracy.
* The method is assessed on seven benchmarks, including scalar nonlinear PDEs, coupled systems, and steady-state Darcy flow.

**Experimental Overview**
=========================

* Tasks/Datasets: The method is assessed on seven benchmark problems, including scalar nonlinear PDEs, coupled systems, and steady-state Darcy flow.
* Baselines/Comparisons: The method is compared to standard PINN (NiL-N) and intermediate formulations that address only one source of nonlinearity.
* Main Claimed Findings: The method converges in single-digit outer iterations in most cases, and recovers the exact solution to machine precision in a single solve when the exact solution lies in the span of the trial space.

**What to Verify in the PDF**
=============================

* The conditioning of the collocation matrix and its impact on accuracy through a rank-revealing column-pivoted QR factorization.
* The explicit smallness condition for local Newton-Kantorovich convergence of the outer iteration.
* The relationship between the trial space and the limiting accuracy of the method.
{% endraw %}

{% raw %}
## 5) Learning Fair Pareto-Optimal Policies in Multi-Objective Reinforcement Learning
- **Authors:** Umer Siddique, Peilang Li, Yongcan Cao
- **arXiv:** [2606.18111](https://arxiv.org/abs/2606.18111v1) · [pdf](https://arxiv.org/pdf/2606.18111v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.18111v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Fairness is an important aspect of decision-making in multi-objective reinforcement learning (MORL), where policies must ensure both optimality and equity across multiple, potentially conflicting objectives. While single-policy MORL methods can learn fair policies for fixed user preferences using welfare functions such as the generalized Gini welfare function (GGF), they fail to provide the diverse set of policies necessary for dynamic or unknown user preferences. To address this limitation, we formalize the fair optimization problem in multi-policy MORL, where the goal is to learn a set of Pareto-optimal policies that ensure fairness across all possible user preferences. Our key technical contributions are threefold: (1) We show that for concave, piecewise-linear welfare functions (e.g., GGF), fair policies remain in the convex coverage set (CCS), which is an approximated Pareto front for linear scalarization. (2) We demonstrate that non-stationary policies, augmented with accrued reward histories, and stochastic policies improve fairness by dynamically adapting to historical inequities. (3) We propose three novel algorithms, which include integrating GGF with multi-policy multi-objective Q-Learning (MOQL), state-augmented multi-policy MOQL for learning non-statoinary policies, and its novel extension for learning stochastic policies. We evaluate our algorithms across various domains and compare our methods against the state-of-the-art MORL baselines. The empirical results show that our methods learn a set of fair policies that accommodate different user preferences.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\lambda$

* Equation: $\lambda$
* Symbols: $\lambda$
* Why it matters: Not found in extracted context.

### Equation 2: $\mathcal{M} = ({\mathcal{S}},{\mathcal{A}},{\mathcal{P}},r,\gamma)$

* Equation: $\mathcal{M} = ({\mathcal{S}},{\mathcal{A}},{\mathcal{P}},r,\gamma)$
* Symbols: $\mathcal{M}$, $\mathcal{S}$, $\mathcal{A}$, $\mathcal{P}$, $r$, $\gamma$
* Why it matters: Defines a multi-objective Markov Decision Process (MOMDP).

### Equation 3: $\mathcal{S}$

* Equation: $\mathcal{S}$
* Symbols: $\mathcal{S}$
* Why it matters: Not found in extracted context.

### Equation 4: $\mathcal{A}$

* Equation: $\mathcal{A}$
* Symbols: $\mathcal{A}$
* Why it matters: Not found in extracted context.

### Equation 5: $\mathcal{P}_{a,s,s'} \in [0,1]$

* Equation: $\mathcal{P}_{a,s,s'} \in [0,1]$
* Symbols: $\mathcal{P}_{a,s,s'}$, $a$, $s$, $s'$
* Why it matters: Defines the probability of transition from state $s$ to state $s'$ after taking action $a$.

### Equation 6: $s'$

* Equation: $s'$
* Symbols: $s'$
* Why it matters: Not found in extracted context.

### Equation 7: $\mathcal{P}(s'|s,a) = \mathcal{P}[S_{t+1} = s'|S_{t} = s, A_{t} = a]$

* Equation: $\mathcal{P}(s'|s,a) = \mathcal{P}[S_{t+1} = s'|S_{t} = s, A_{t} = a]$
* Symbols: $\mathcal{P}(s'|s,a)$, $\mathcal{P}$, $S_{t+1}$, $S_{t}$, $A_{t}$
* Why it matters: Defines the probability of transitioning from state $s$ to state $s'$ after taking action $a$.

### Equation 8: $r(s,a) : s \times a \mapsto r$

* Equation: $r(s,a) : s \times a \mapsto r$
* Symbols: $r(s,a)$, $s$, $a$
* Why it matters: Defines the immediate reward obtained by taking action $a$ at state $s$.

**Method Summary**
==================

* The proposed methods learn fair Pareto-optimal policies in multi-objective reinforcement learning (MORL) by incorporating fairness into the multi-policy multi-objective Q-Learning (MOQL) framework.
* The methods use a single parameterized network to estimate Q-values for all objectives while maintaining a diverse set of Pareto-optimal policies.
* The proposed methods include Fair Multi-Objective Deep Q-Learning (F-MDQ), its non-stationary extension (FN-MDQ), and a novel extension incorporating stochastic policies (FNS-MDQ).
* The methods are scalable and sample-efficient, and they demonstrate a systematic approach to enhancing fairness in MORL algorithms.

**Experimental Overview**
=========================

* The experiments are conducted across three domains: species conservation, resource gathering, and multi-product web advertising.
* The domains are chosen to evaluate the effectiveness of the proposed methods in learning fair solutions across different preference settings.
* The experiments compare the proposed methods (F-MDQ, FN-MDQ, and FNS-MDQ) with multi-policy MORL baselines (PCN, GPI, and Envelope).
* The main claimed findings include:
	+ The proposed methods learn fairer solutions compared to multi-policy MORL baselines.
	+ The methods generate fair solutions across different preference settings during inference.
	+ The proposed algorithms achieve comparable performance in terms of hypervolume and cardinality relative to multi-policy MORL approaches.
	+ The incorporation of stochastic policies in MO Q-learning based algorithms contributes to improved fairness or overall performance.

**What to Verify in the PDF**
=============================

* The full paper provides more details on the technical analysis, including the formal proofs of the technical analysis.
* The paper also provides more information on the experimental setup, including the specific hyperparameters used and the evaluation metrics used to compare the proposed methods with multi-policy MORL baselines.
* The paper may also provide more details on the fairness criteria used to evaluate the proposed methods, including the specific metrics used to quantify fairness.
* The paper may also provide more information on the scalability and sample-efficiency of the proposed methods, including the specific computational resources used and the number of samples used to train the models.
{% endraw %}
