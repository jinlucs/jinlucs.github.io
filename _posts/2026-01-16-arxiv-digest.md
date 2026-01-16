---
layout: post
title: "Daily arXiv Digest — 2026-01-16 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Queueing-Aware Optimization of Reasoning Tokens for Accuracy-Latency Trade-offs in LLM Servers
- **Authors:** Emre Ozbas, Melih Bastopcu
- **arXiv:** [2601.10274](https://arxiv.org/abs/2601.10274v1) · [pdf](https://arxiv.org/pdf/2601.10274v1)
- **Categories:** cs.LG, cs.AI, cs.IT, cs.NI, math.OC

### Abstract
> We consider a single large language model (LLM) server that serves a heterogeneous stream of queries belonging to $N$ distinct task types. Queries arrive according to a Poisson process, and each type occurs with a known prior probability. For each task type, the server allocates a fixed number of internal thinking tokens, which determines the computational effort devoted to that query. The token allocation induces an accuracy-latency trade-off: the service time follows an approximately affine function of the allocated tokens, while the probability of a correct response exhibits diminishing returns. Under a first-in, first-out (FIFO) service discipline, the system operates as an $M/G/1$ queue, and the mean system time depends on the first and second moments of the resulting service-time distribution. We formulate a constrained optimization problem that maximizes a weighted average accuracy objective penalized by the mean system time, subject to architectural token-budget constraints and queue-stability conditions. The objective function is shown to be strictly concave over the stability region, which ensures existence and uniqueness of the optimal token allocation. The first-order optimality conditions yield a coupled projected fixed-point characterization of the optimum, together with an iterative solution and an explicit sufficient condition for contraction. Moreover, a projected gradient method with a computable global step-size bound is developed to guarantee convergence beyond the contractive regime. Finally, integer-valued token allocations are attained via rounding of the continuous solution, and the resulting performance loss is evaluated in simulation results.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Communication-Efficient Federated Learning by Exploiting Spatio-Temporal Correlations of Gradients
- **Authors:** Shenlong Zheng, Zhen Zhang, Yuhui Deng, Geyong Min, Lin Cui
- **arXiv:** [2601.10491](https://arxiv.org/abs/2601.10491v1) · [pdf](https://arxiv.org/pdf/2601.10491v1)
- **Categories:** cs.LG

### Abstract
> Communication overhead is a critical challenge in federated learning, particularly in bandwidth-constrained networks. Although many methods have been proposed to reduce communication overhead, most focus solely on compressing individual gradients, overlooking the temporal correlations among them. Prior studies have shown that gradients exhibit spatial correlations, typically reflected in low-rank structures. Through empirical analysis, we further observe a strong temporal correlation between client gradients across adjacent rounds. Based on these observations, we propose GradESTC, a compression technique that exploits both spatial and temporal gradient correlations. GradESTC exploits spatial correlations to decompose each full gradient into a compact set of basis vectors and corresponding combination coefficients. By exploiting temporal correlations, only a small portion of the basis vectors need to be dynamically updated in each round. GradESTC significantly reduces communication overhead by transmitting lightweight combination coefficients and a limited number of updated basis vectors instead of the full gradients. Extensive experiments show that, upon reaching a target accuracy level near convergence, GradESTC reduces uplink communication by an average of 39.79% compared to the strongest baseline, while maintaining comparable convergence speed and final accuracy to uncompressed FedAvg. By effectively leveraging spatio-temporal gradient structures, GradESTC offers a practical and scalable solution for communication-efficient federated learning.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) H-EFT-VA: An Effective-Field-Theory Variational Ansatz with Provable Barren Plateau Avoidance
- **Authors:** Eyad I. B Hamid
- **arXiv:** [2601.10479](https://arxiv.org/abs/2601.10479v1) · [pdf](https://arxiv.org/pdf/2601.10479v1)
- **Categories:** quant-ph, cs.LG, math-ph

### Abstract
> Variational Quantum Algorithms (VQAs) are critically threatened by the Barren Plateau (BP) phenomenon. In this work, we introduce the H-EFT Variational Ansatz (H-EFT-VA), an architecture inspired by Effective Field Theory (EFT). By enforcing a hierarchical "UV-cutoff" on initialization, we theoretically restrict the circuit's state exploration, preventing the formation of approximate unitary 2-designs. We provide a rigorous proof that this localization guarantees an inverse-polynomial lower bound on the gradient variance: $Var[\partial θ] \in Ω(1/poly(N))$. Crucially, unlike approaches that avoid BPs by limiting entanglement, we demonstrate that H-EFT-VA maintains volume-law entanglement and near-Haar purity, ensuring sufficient expressibility for complex quantum states. Extensive benchmarking across 16 experiments -- including Transverse Field Ising and Heisenberg XXZ models -- confirms a 109x improvement in energy convergence and a 10.7x increase in ground-state fidelity over standard Hardware-Efficient Ansatze (HEA), with a statistical significance of $p < 10^{-88}$.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) CS-GBA: A Critical Sample-based Gradient-guided Backdoor Attack for Offline Reinforcement Learning
- **Authors:** Yuanjie Zhao, Junnan Qiu, Yue Ding, Jie Li
- **arXiv:** [2601.10407](https://arxiv.org/abs/2601.10407v1) · [pdf](https://arxiv.org/pdf/2601.10407v1)
- **Categories:** cs.LG

### Abstract
> Offline Reinforcement Learning (RL) enables policy optimization from static datasets but is inherently vulnerable to backdoor attacks. Existing attack strategies typically struggle against safety-constrained algorithms (e.g., CQL) due to inefficient random poisoning and the use of easily detectable Out-of-Distribution (OOD) triggers. In this paper, we propose CS-GBA (Critical Sample-based Gradient-guided Backdoor Attack), a novel framework designed to achieve high stealthiness and destructiveness under a strict budget. Leveraging the theoretical insight that samples with high Temporal Difference (TD) errors are pivotal for value function convergence, we introduce an adaptive Critical Sample Selection strategy that concentrates the attack budget on the most influential transitions. To evade OOD detection, we propose a Correlation-Breaking Trigger mechanism that exploits the physical mutual exclusivity of state features (e.g., 95th percentile boundaries) to remain statistically concealed. Furthermore, we replace the conventional label inversion with a Gradient-Guided Action Generation mechanism, which searches for worst-case actions within the data manifold using the victim Q-network's gradient. Empirical results on D4RL benchmarks demonstrate that our method significantly outperforms state-of-the-art baselines, achieving high attack success rates against representative safety-constrained algorithms with a minimal 5% poisoning budget, while maintaining the agent's performance in clean environments.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) X-SAM: Boosting Sharpness-Aware Minimization with Dominant-Eigenvector Gradient Correction
- **Authors:** Hongru Duan, Yongle Chen, Lei Guan
- **arXiv:** [2601.10251](https://arxiv.org/abs/2601.10251v1) · [pdf](https://arxiv.org/pdf/2601.10251v1)
- **Categories:** cs.LG, cs.AI

### Abstract
> Sharpness-Aware Minimization (SAM) aims to improve generalization by minimizing a worst-case perturbed loss over a small neighborhood of model parameters. However, during training, its optimization behavior does not always align with theoretical expectations, since both sharp and flat regions may yield a small perturbed loss. In such cases, the gradient may still point toward sharp regions, failing to achieve the intended effect of SAM. To address this issue, we investigate SAM from a spectral and geometric perspective: specifically, we utilize the angle between the gradient and the leading eigenvector of the Hessian as a measure of sharpness. Our analysis illustrates that when this angle is less than or equal to ninety degrees, the effect of SAM's sharpness regularization can be weakened. Furthermore, we propose an explicit eigenvector-aligned SAM (X-SAM), which corrects the gradient via orthogonal decomposition along the top eigenvector, enabling more direct and efficient regularization of the Hessian's maximum eigenvalue. We prove X-SAM's convergence and superior generalization, with extensive experimental evaluations confirming both theoretical and practical advantages.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
