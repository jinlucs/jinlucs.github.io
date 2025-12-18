---
layout: post
title: "Daily arXiv Digest — 2025-12-18 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Intertemporal Hedging Demand under Epstein-Zin Preferences in a Multi-Asset Long-Run Risk Model: Evidence from Projected Pontryagin-Guided Deep Policy Optimization
- **Authors:** Wonchan Cho
- **arXiv:** [2512.15175](https://arxiv.org/abs/2512.15175v1) · [pdf](https://arxiv.org/pdf/2512.15175v1)
- **Categories:** eess.SY, math.OC

### Abstract
> I study intertemporal hedging demand in a continuous-time multi-asset long-run risk (LRR) model under Epstein--Zin (EZ) recursive preferences. The investor trades a risk-free asset and several risky assets whose drifts and volatilities depend on an Ornstein--Uhlenbeck type LRR factor. Preferences are described by EZ utility with risk aversion $R$, elasticity of intertemporal substitution $ψ$, and discount rate $δ$, so that the standard time-additive CRRA case appears as a limiting benchmark. To handle the high-dimensional consumption--investment problem, I use a projected Pontryagin-guided deep policy optimization (P-PGDPO) scheme adapted to EZ preferences. The method starts from the continuous-time Hamiltonian implied by the Pontryagin maximum principle, represents the value and costate processes with neural networks, and updates the policy along the Hamiltonian gradient. Portfolio constraints and a lower bound on wealth are enforced by explicit projection operators rather than by adding ad hoc penalties. Three main findings emerge from numerical experiments in a five-asset LRR economy: \textbf{(1)} the P-PGDPO algorithm achieves stable convergence across multiple random seeds, validating its reliability for solving high-dimensional EZ problems; \textbf{(2)} wealth floors materially reduce hedging demand by limiting the investor's ability to exploit intertemporal risk-return tradeoffs; and \textbf{(3)} the learned hedging portfolios concentrate exposure in assets with high correlation to the LRR factor, confirming that EZ agents actively hedge long-run uncertainty rather than merely following myopic rules. Because EZ preferences nest time-additive CRRA in the limit $ψ\to 1/R$, I use CRRA as an explicit diagnostic benchmark and, when needed, a warm start to stabilize training in high dimensions.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Long-Run Average Reward Maximization of A Regulated Regime-Switching Diffusion Model
- **Authors:** Lingjia Zeng, Manman Li
- **arXiv:** [2512.15167](https://arxiv.org/abs/2512.15167v1) · [pdf](https://arxiv.org/pdf/2512.15167v1)
- **Categories:** math.OC

### Abstract
> This study considers an optimal reinsurance, investment, and dividend strategy control problem for insurance companies in a regulated Markov regime-switching environment, intending to maximize long-run average reward. Unlike existing single or dual strategy studies, an integrated control framework is established under solvency constraints, allowing investment and dividends only when the surplus process exceeds a minimum cash requirement level. To address the analytical difficulties associated with solving HJB equations and stationary distributions in high-dimensional state spaces under regime switching, we construct a numerical approximation scheme for the optimal strategy function based on Markov chains and neural networks. Furthermore, we establish the convergence of the corresponding sequence of surplus processes and rigorously prove that the associated optimal values converge to the true value function. Finally, we provide a numerical example based on the approximate dynamic programming method to demonstrate the feasibility of the proposed method.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning
- **Authors:** Zhenwen Liang, Sidi Lu, Wenhao Yu, Kishan Panaganti, Yujun Zhou, Haitao Mi, Dong Yu
- **arXiv:** [2512.15687](https://arxiv.org/abs/2512.15687v1) · [pdf](https://arxiv.org/pdf/2512.15687v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Reinforcement learning has become essential for strengthening the reasoning abilities of large language models, yet current exploration mechanisms remain fundamentally misaligned with how these models actually learn. Entropy bonuses and external semantic comparators encourage surface level variation but offer no guarantee that sampled trajectories differ in the update directions that shape optimization. We propose G2RL, a gradient guided reinforcement learning framework in which exploration is driven not by external heuristics but by the model own first order update geometry. For each response, G2RL constructs a sequence level feature from the model final layer sensitivity, obtainable at negligible cost from a standard forward pass, and measures how each trajectory would reshape the policy by comparing these features within a sampled group. Trajectories that introduce novel gradient directions receive a bounded multiplicative reward scaler, while redundant or off manifold updates are deemphasized, yielding a self referential exploration signal that is naturally aligned with PPO style stability and KL control. Across math and general reasoning benchmarks (MATH500, AMC, AIME24, AIME25, GPQA, MMLUpro) on Qwen3 base 1.7B and 4B models, G2RL consistently improves pass@1, maj@16, and pass@k over entropy based GRPO and external embedding methods. Analyzing the induced geometry, we find that G2RL expands exploration into substantially more orthogonal and often opposing gradient directions while maintaining semantic coherence, revealing that a policy own update space provides a far more faithful and effective basis for guiding exploration in large language model reinforcement learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Hybrid Set-Seeking Systems: Model-Free Feedback Optimization via Hybrid Inclusions
- **Authors:** Jorge I. Poveda, Andrew R. Teel
- **arXiv:** [2512.15678](https://arxiv.org/abs/2512.15678v1) · [pdf](https://arxiv.org/pdf/2512.15678v1)
- **Categories:** math.OC

### Abstract
> This article aims to provide an accessible, tutorial-style introduction to hybrid extremum-seeking systems, which are model-free, feedback-optimization controllers that incorporate hybrid dynamics, meaning both continuous-time and discrete-time behaviors. Such systems arise when advanced control and optimization tools are needed to overcome the limitations of smooth feedback methods and to satisfy demanding transient and steady-state requirements in high-performance applications. They also appear when controllers must operate on plants that inherently exhibit hybrid behaviors, as is common in cyber-physical and autonomous systems that rely on digital sensing, computation, and actuation. To study hybrid extremum-seeking dynamics through control-theoretic methods, we first review the key concepts that support the development of perturbation theory for hybrid inclusions, forming the basis for averaging and singular perturbation analyses. We then show how these ideas apply to the design and evaluation of hybrid extremum-seeking algorithms for static and dynamic plants. Several examples are presented, including set-valued and switching algorithms under different switching regimes such as arbitrarily fast switching, dwell-time and average dwell-time constraints, and average activation time conditions. We also discuss state-based switching extremum seeking for obstacle-avoidance problems and gradient-Newton switching schemes. Additional topics include momentum-based and reset-type extremum seeking, intermittent updates, slowly varying parameters, hybrid filters, and safety-aware schemes that incorporate constraints. Across all these settings, we illustrate how perturbation-based methods traditionally used for extremum-seeking control naturally extend to hybrid systems when mild regularity assumptions are satisfied, and solutions are modeled on hybrid time domains.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Double Horizon Model-Based Policy Optimization
- **Authors:** Akihiro Kubo, Paavo Parmas, Shin Ishii
- **arXiv:** [2512.15439](https://arxiv.org/abs/2512.15439v1) · [pdf](https://arxiv.org/pdf/2512.15439v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Model-based reinforcement learning (MBRL) reduces the cost of real-environment sampling by generating synthetic trajectories (called rollouts) from a learned dynamics model. However, choosing the length of the rollouts poses two dilemmas: (1) Longer rollouts better preserve on-policy training but amplify model bias, indicating the need for an intermediate horizon to mitigate distribution shift (i.e., the gap between on-policy and past off-policy samples). (2) Moreover, a longer model rollout may reduce value estimation bias but raise the variance of policy gradients due to backpropagation through multiple steps, implying another intermediate horizon for stable gradient estimates. However, these two optimal horizons may differ. To resolve this conflict, we propose Double Horizon Model-Based Policy Optimization (DHMBPO), which divides the rollout procedure into a long "distribution rollout" (DR) and a short "training rollout" (TR). The DR generates on-policy state samples for mitigating distribution shift. In contrast, the short TR leverages differentiable transitions to offer accurate value gradient estimation with stable gradient updates, thereby requiring fewer updates and reducing overall runtime. We demonstrate that the double-horizon approach effectively balances distribution shift, model bias, and gradient instability, and surpasses existing MBRL methods on continuous-control benchmarks in terms of both sample efficiency and runtime.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
