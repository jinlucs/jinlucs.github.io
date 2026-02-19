---
layout: post
title: "Daily arXiv Digest — 2026-02-19 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Primal-dual dynamical systems with closed-loop control for convex optimization in continuous and discrete time
- **Authors:** Huan Zhang, Xiangkai Sun, Shengjie Li, Kok Lay Teo
- **arXiv:** [2602.16402](https://arxiv.org/abs/2602.16402v1) · [pdf](https://arxiv.org/pdf/2602.16402v1)
- **Categories:** math.OC

### Abstract
> This paper develops a primal-dual dynamical system where the coefficients are designed in closed-loop way for solving a convex optimization problem with linear equality constraints. We first introduce a ``second-order primal" + ``first-order dual'' continuous-time dynamical system, in which both the time scaling and Hessian-driven damping are governed by a feedback control of the gradient for the Lagrangian function. This system achieves the fast convergence rates for the primal-dual gap, the feasibility violation, and the objective residual along its trajectory. Subsequently, by time discretization of this system, we develop an accelerated primal-dual algorithm with a gradient-defined adaptive step size. We also obtain convergence rates for the primal-dual gap, the feasibility violation, and the objective residual. Furthermore, we provide numerical results to demonstrate the practical efficacy and superior performance of the proposed algorithm.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Knowledge-Embedded Latent Projection for Robust Representation Learning
- **Authors:** Weijing Tang, Ming Yuan, Zongqi Xia, Tianxi Cai
- **arXiv:** [2602.16709](https://arxiv.org/abs/2602.16709v1) · [pdf](https://arxiv.org/pdf/2602.16709v1)
- **Categories:** cs.LG, math.ST, stat.ME

### Abstract
> Latent space models are widely used for analyzing high-dimensional discrete data matrices, such as patient-feature matrices in electronic health records (EHRs), by capturing complex dependence structures through low-dimensional embeddings. However, estimation becomes challenging in the imbalanced regime, where one matrix dimension is much larger than the other. In EHR applications, cohort sizes are often limited by disease prevalence or data availability, whereas the feature space remains extremely large due to the breadth of medical coding system. Motivated by the increasing availability of external semantic embeddings, such as pre-trained embeddings of clinical concepts in EHRs, we propose a knowledge-embedded latent projection model that leverages semantic side information to regularize representation learning. Specifically, we model column embeddings as smooth functions of semantic embeddings via a mapping in a reproducing kernel Hilbert space. We develop a computationally efficient two-step estimation procedure that combines semantically guided subspace construction via kernel principal component analysis with scalable projected gradient descent. We establish estimation error bounds that characterize the trade-off between statistical error and approximation error induced by the kernel projection. Furthermore, we provide local convergence guarantees for our non-convex optimization procedure. Extensive simulation studies and a real-world EHR application demonstrate the effectiveness of the proposed method.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Learning Distributed Equilibria in Linear-Quadratic Stochastic Differential Games: An $α$-Potential Approach
- **Authors:** Philipp Plank, Yufei Zhang
- **arXiv:** [2602.16555](https://arxiv.org/abs/2602.16555v1) · [pdf](https://arxiv.org/pdf/2602.16555v1)
- **Categories:** math.OC, cs.LG, math.PR

### Abstract
> We analyze independent policy-gradient (PG) learning in $N$-player linear-quadratic (LQ) stochastic differential games. Each player employs a distributed policy that depends only on its own state and updates the policy independently using the gradient of its own objective. We establish global linear convergence of these methods to an equilibrium by showing that the LQ game admits an $α$-potential structure, with $α$ determined by the degree of pairwise interaction asymmetry. For pairwise-symmetric interactions, we construct an affine distributed equilibrium by minimizing the potential function and show that independent PG methods converge globally to this equilibrium, with complexity scaling linearly in the population size and logarithmically in the desired accuracy. For asymmetric interactions, we prove that independent projected PG algorithms converge linearly to an approximate equilibrium, with suboptimality proportional to the degree of asymmetry. Numerical experiments confirm the theoretical results across both symmetric and asymmetric interaction networks.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Illustration of Barren Plateaus in Quantum Computing
- **Authors:** Gerhard Stenzel, Tobias Rohe, Michael Kölle, Leo Sünkel, Jonas Stein, Claudia Linnhoff-Popien
- **arXiv:** [2602.16558](https://arxiv.org/abs/2602.16558v1) · [pdf](https://arxiv.org/pdf/2602.16558v1)
- **Categories:** cs.LG, quant-ph

### Abstract
> Variational Quantum Circuits (VQCs) have emerged as a promising paradigm for quantum machine learning in the NISQ era. While parameter sharing in VQCs can reduce the parameter space dimensionality and potentially mitigate the barren plateau phenomenon, it introduces a complex trade-off that has been largely overlooked. This paper investigates how parameter sharing, despite creating better global optima with fewer parameters, fundamentally alters the optimization landscape through deceptive gradients -- regions where gradient information exists but systematically misleads optimizers away from global optima. Through systematic experimental analysis, we demonstrate that increasing degrees of parameter sharing generate more complex solution landscapes with heightened gradient magnitudes and measurably higher deceptiveness ratios. Our findings reveal that traditional gradient-based optimizers (Adam, SGD) show progressively degraded convergence as parameter sharing increases, with performance heavily dependent on hyperparameter selection. We introduce a novel gradient deceptiveness detection algorithm and a quantitative framework for measuring optimization difficulty in quantum circuits, establishing that while parameter sharing can improve circuit expressivity by orders of magnitude, this comes at the cost of significantly increased landscape deceptiveness. These insights provide important considerations for quantum circuit design in practical applications, highlighting the fundamental mismatch between classical optimization strategies and quantum parameter landscapes shaped by parameter sharing.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Reinforcement Learning for Parameterized Quantum State Preparation: A Comparative Study
- **Authors:** Gerhard Stenzel, Isabella Debelic, Michael Kölle, Tobias Rohe, Leo Sünkel, Julian Hager, Claudia Linnhoff-Popien
- **arXiv:** [2602.16523](https://arxiv.org/abs/2602.16523v1) · [pdf](https://arxiv.org/pdf/2602.16523v1)
- **Categories:** cs.LG, quant-ph

### Abstract
> We extend directed quantum circuit synthesis (DQCS) with reinforcement learning from purely discrete gate selection to parameterized quantum state preparation with continuous single-qubit rotations \(R_x\), \(R_y\), and \(R_z\). We compare two training regimes: a one-stage agent that jointly selects the gate type, the affected qubit(s), and the rotation angle; and a two-stage variant that first proposes a discrete circuit and subsequently optimizes the rotation angles with Adam using parameter-shift gradients. Using Gymnasium and PennyLane, we evaluate Proximal Policy Optimization (PPO) and Advantage Actor--Critic (A2C) on systems comprising two to ten qubits and on targets of increasing complexity with \(λ\) ranging from one to five. Whereas A2C does not learn effective policies in this setting, PPO succeeds under stable hyperparameters (one-stage: learning rate approximately \(5\times10^{-4}\) with a self-fidelity-error threshold of 0.01; two-stage: learning rate approximately \(10^{-4}\)). Both approaches reliably reconstruct computational basis states (between 83\% and 99\% success) and Bell states (between 61\% and 77\% success). However, scalability saturates for \(λ\) of approximately three to four and does not extend to ten-qubit targets even at \(λ=2\). The two-stage method offers only marginal accuracy gains while requiring around three times the runtime. For practicality under a fixed compute budget, we therefore recommend the one-stage PPO policy, provide explicit synthesized circuits, and contrast with a classical variational baseline to outline avenues for improved scalability.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
