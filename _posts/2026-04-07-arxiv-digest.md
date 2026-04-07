---
layout: post
title: "Daily arXiv Digest — 2026-04-07 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) A Near-Optimal Total Complexity for the Inexact Accelerated Proximal Gradient Method via Quadratic Growth
- **Authors:** Hongda Li, Xianfu Wang
- **arXiv:** [2604.04551](https://arxiv.org/abs/2604.04551v1) · [pdf](https://arxiv.org/pdf/2604.04551v1)
- **Categories:** math.OC

### Abstract
> We consider the optimization problem $\min_{x\in \mathbb R^n}{F(x):=f(x)+ω(Ax)}$, where $f$ is an $L$-Lipschitz smooth function, and $ω$ is a proper, lower semicontinuous, and convex function. We prove in this paper that when $ω$ is a conic polyhedral function, the inexact accelerated proximal gradient method (IAPG), employed in a double-loop structure, achieves a total complexity of $\mathcal O(\ln(1/\varepsilon)/\sqrt{\varepsilon})$ measured by the total number of calls to the proximal operator of the convex conjugate $ω^\star$ and the gradient of $f$ to achieve $\varepsilon$-optimality in function value. To the best of our knowledge, this improves upon the best-known complexity for IAPG. The key theoretical ingredient is a quadratic growth condition on the dual of the inexact proximal problem, which arises from the conic polyhedral structure of $ω$ and implies linear convergence of the inner proximal gradient loop. To validate these findings, we conduct numerical experiments on a robust TV-$\ell_2$ signal recovery problem, demonstrating fast convergence.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control
- **Authors:** Donghu Kim, Youngdo Lee, Minho Park, Kinam Kim, I Made Aswin Nahendra, Takuma Seno, Sehee Min, Daniel Palenicek, Florian Vogt, Danica Kragic, Jan Peters, Jaegul Choo, Hojoon Lee
- **arXiv:** [2604.04539](https://arxiv.org/abs/2604.04539v1) · [pdf](https://arxiv.org/pdf/2604.04539v1)
- **Categories:** cs.LG, cs.RO

### Abstract
> Reinforcement learning (RL) is a core approach for robot control when expert demonstrations are unavailable. On-policy methods such as Proximal Policy Optimization (PPO) are widely used for their stability, but their reliance on narrowly distributed on-policy data limits accurate policy evaluation in high-dimensional state and action spaces. Off-policy methods can overcome this limitation by learning from a broader state-action distribution, yet suffer from slow convergence and instability, as fitting a value function over diverse data requires many gradient updates, causing critic errors to accumulate through bootstrapping. We present FlashSAC, a fast and stable off-policy RL algorithm built on Soft Actor-Critic. Motivated by scaling laws observed in supervised learning, FlashSAC sharply reduces gradient updates while compensating with larger models and higher data throughput. To maintain stability at increased scale, FlashSAC explicitly bounds weight, feature, and gradient norms, curbing critic error accumulation. Across over 60 tasks in 10 simulators, FlashSAC consistently outperforms PPO and strong off-policy baselines in both final performance and training efficiency, with the largest gains on high-dimensional tasks such as dexterous manipulation. In sim-to-real humanoid locomotion, FlashSAC reduces training time from hours to minutes, demonstrating the promise of off-policy RL for sim-to-real transfer.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Distributed Covariance Steering via Non-Convex ADMM for Large-Scale Multi-Agent Systems
- **Authors:** Augustinos D. Saravanos, Isin M. Balci, Arshiya Taj Abdul, Efstathios Bakolas, Evangelos A. Theodorou
- **arXiv:** [2604.04499](https://arxiv.org/abs/2604.04499v1) · [pdf](https://arxiv.org/pdf/2604.04499v1)
- **Categories:** eess.SY, math.OC

### Abstract
> This paper studies the problem of steering large-scale multi-agent stochastic linear systems between Gaussian distributions under probabilistic collision avoidance constraints. We introduce a family of \textit{distributed covariance steering (DCS)} methods based on the Alternating Direction Method of Multipliers (ADMM), each offering different trade-offs between conservatism and computational efficiency. The first method, Full-Covariance-Consensus (FCC)-DCS, enforces consensus over both the means and covariances of neighboring agents, yielding the least conservative safe solutions. The second approach, Partial-Covariance-Consensus (PCC)-DCS, leverages the insight that safety can be maintained by exchanging only partial covariance information, reducing computational demands. The third method, Mean-Consensus (MC)-DCS, provides the most scalable alternative by requiring consensus only on mean states. Furthermore, we establish novel convergence guarantees for distributed ADMM with iteratively linearized non-convex constraints, covering a broad class of consensus optimization problems. This analysis proves convergence to stationary points for PCC-DCS and MC-DCS, while the convergence of FCC-DCS follows from standard ADMM theory. Simulations in 2D and 3D multi-agent environments verify safety, illustrate the trade-offs between methods, and demonstrate scalability to thousands of agents.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Optimizing LLM Prompt Engineering with DSPy Based Declarative Learning
- **Authors:** Shiek Ruksana, Sailesh Kiran Kurra, Thipparthi Sanjay Baradwaj
- **arXiv:** [2604.04869](https://arxiv.org/abs/2604.04869v1) · [pdf](https://arxiv.org/pdf/2604.04869v1)
- **Categories:** cs.LG

### Abstract
> Large Language Models (LLMs) have shown strong performance across a wide range of natural language processing tasks; however, their effectiveness is highly dependent on prompt design, structure, and embedded reasoning signals. Conventional prompt engineering methods largely rely on heuristic trial-and-error processes, which limits scalability, reproducibility, and generalization across tasks. DSPy, a declarative framework for optimizing text-processing pipelines, offers an alternative approach by enabling automated, modular, and learnable prompt construction for LLM-based systems.This paper presents a systematic study of DSPy-based declarative learning for prompt optimization, with emphasis on prompt synthesis, correction, calibration, and adaptive reasoning control. We introduce a unified DSPy LLM architecture that combines symbolic planning, gradient free optimization, and automated module rewriting to reduce hallucinations, improve factual grounding, and avoid unnecessary prompt complexity. Experimental evaluations conducted on reasoning tasks, retrieval-augmented generation, and multi-step chain-of-thought benchmarks demonstrate consistent gains in output reliability, efficiency, and generalization across models. The results show improvements of up to 30 to 45% in factual accuracy and a reduction of approximately 25% in hallucination rates. Finally, we outline key limitations and discuss future research directions for declarative prompt optimization frameworks.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Optimal Contest Beyond Convexity
- **Authors:** Negin Golrezaei, MohammadTaghi Hajiaghayi, Suho Shin
- **arXiv:** [2604.04844](https://arxiv.org/abs/2604.04844v1) · [pdf](https://arxiv.org/pdf/2604.04844v1)
- **Categories:** cs.GT, cs.DS, econ.TH, math.OC

### Abstract
> In the contest design problem, there are $n$ strategic contestants, each of whom decides an effort level. A contest designer with a fixed budget must then design a mechanism that allocates a prize $p_i$ to the $i$-th rank based on the outcome, to incentivize contestants to exert higher costly efforts and induce high-quality outcomes. In this paper, we significantly deepen our understanding of optimal mechanisms under general settings by considering nonconvex objectives in contestants' qualities. Notably, our results accommodate the following objectives: (i) any convex combination of user welfare (motivated by recommender systems) and the average quality of contestants, and (ii) arbitrary posynomials over quality, both of which may neither be convex nor concave. In particular, these subsume classic measures such as social welfare, order statistics, and (inverse) S-shaped functions, which have received little or no attention in the contest literature to the best of our knowledge. Surprisingly, across all these regimes, we show that the optimal mechanism is highly structured: it allocates potentially higher prize to the first-ranked contestant, zero to the last-ranked one, and equal prizes to the all intermediate contestants, i.e., $p_1 \ge p_2 = \ldots = p_{n-1} \ge p_n = 0$. Thanks to the structural characterization, we obtain a fully polynomial-time approximation scheme given a value oracle. Our technical results rely on Schur-convexity of Bernstein basis polynomial-weighted functions, total positivity and variation diminishing property. En route to our results, we obtain a surprising reduction from a structured high-dimensional nonconvex optimization to a single-dimensional optimization by connecting the shape of the gradient sequences of the objective function to the number of transition points in optimum, which might be of independent interest.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
