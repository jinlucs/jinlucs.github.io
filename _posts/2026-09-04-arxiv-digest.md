---
layout: post
title: "Daily arXiv Digest — 2026-09-04 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Robust PAC Learning of Concurrent Stochastic Games
- **Authors:** Angel Y. He, David Parker
- **arXiv:** [2609.04189](https://arxiv.org/abs/2609.04189v1) · [pdf](https://arxiv.org/pdf/2609.04189v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.04189v1))
- **Categories:** cs.LG, cs.GT, cs.LO, cs.MA

### Abstract
> We introduce the first Probably Approximately Correct (PAC) learning framework for general-sum concurrent stochastic games (CSGs) with transition uncertainty, while addressing the challenge of Nash equilibrium (NE) existence. Our algorithm maintains data-driven $L^1$ confidence sets over transition kernels and solves a robust CSG to compute a social-welfare optimal $\varepsilon$-NE, using a robust MDP-based exploration mechanism to drive joint state-action coverage. Crucially, we introduce a Nash margin characterisation that enables principled reasoning about equilibrium existence: the framework either returns an $\varepsilon$-approximate NE whose social-welfare value is $\varepsilon$-close to optimal, or provides a sound certificate that no exact NE exists. Under a minimum reachability condition $p_{\mathrm{reach}}>0$ over relevant state-action pairs, the algorithm terminates after a polynomial number of trajectory samples, with sample complexity $\widetilde{O}\left( {R_{\max}^2 H^4 |S|^2 |A| / (p_{\mathrm{reach}} \varepsilon^2)} \right)$. Empirical results on benchmark CSGs demonstrate near-optimal performance, correct handling of equilibrium (non-)existence, and sample complexity consistent with theory.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: L^{1}

* Equation: L^{1} = ∑_{(s,a)∈X_{nt}} |P(s,a) - P^{*}(s,a)|
* Symbols: L^{1} (L1), P(s,a) (transition probability), P^{*}(s,a) (oracle transition probability)
* Why it matters: L^{1} is a confidence set over transition kernels, which is used to drive joint state-action coverage in the algorithm.

### Equation 2: ε

* Equation: ε = δ + 4Δt
* Symbols: ε (error tolerance), δ (delta), Δt (time complexity)
* Why it matters: ε is the error tolerance used to determine when to stop the algorithm, and it is related to the time complexity Δt.

### Equation 3: p_{\mathrm{reach}}>0

* Equation: p_{\mathrm{reach}}>0
* Symbols: p_{\mathrm{reach}} (reachability probability)
* Why it matters: p_{\mathrm{reach}} is a minimum reachability condition that ensures the algorithm terminates after a polynomial number of trajectory samples.

### Equation 4: \widetilde{\mathcal{O}}\!\left({R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})}\right)

* Equation: \widetilde{\mathcal{O}}\!\left({R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})}\right) = O\left({R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})}\right)
* Symbols: \widetilde{\mathcal{O}}\!\left({R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})}\right) (sample complexity), R_{\max} (maximum reward), H (horizon), S (states), A (actions), p_{\mathrm{reach}} (reachability probability), ε (error tolerance)
* Why it matters: This is the sample complexity of the algorithm, which is related to the number of trajectory samples required to achieve a certain level of accuracy.

### Equation 5: ε>0

* Equation: ε > 0
* Symbols: ε (error tolerance)
* Why it matters: ε is a positive value that represents the maximum allowed error in the algorithm's output.

**Method Summary**
================

* The algorithm uses a PAC-CSG framework to learn a social-welfare optimal ε-NE in concurrent stochastic games with transition uncertainty.
* The algorithm maintains data-driven L1 confidence sets over transition kernels and solves a robust CSG to compute the social-welfare optimal ε-NE.
* The algorithm uses a robust MDP-based exploration mechanism to drive joint state-action coverage.
* The algorithm terminates after a polynomial number of trajectory samples, with sample complexity O(R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})).

**Experimental Overview**
=====================

* Tasks/Datasets: The algorithm is evaluated on a suite of benchmark CSGs, including six small, interpretable CSGs.
* Baselines/Comparisons: The algorithm is compared to the PRISM-games CSG solver, which is used as ground truth.
* Main Claimed Findings: The algorithm achieves near-optimal performance, correct handling of equilibrium (non-)existence, and sample complexity consistent with theory.

**What to Verify in the PDF**
==========================

* The proof of the sample complexity bound O(R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})).
* The correctness of the algorithm's termination condition Δt ≤ ε/4.
* The handling of unbounded total reward in the Safe vs. Risky property.
* The soundness of the algorithm's non-existence certificate in the Cyclic Preferences and Hide-or-Run benchmarks.
{% endraw %}

{% raw %}
## 2) Computation of Strong Solutions to Stochastic Variational Inequalities
- **Authors:** Yao Ji, Guanghui Lan, Jason Zhu
- **arXiv:** [2609.04188](https://arxiv.org/abs/2609.04188v1) · [pdf](https://arxiv.org/pdf/2609.04188v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.04188v1))
- **Categories:** math.OC

### Abstract
> This paper studies the computation of strong solutions of monotone variational inequalities (VIs) with Lipschitz continuous operators. Building on the idea of accumulative regularization, we develop a general framework for VIs, with particular emphasis on stochastic settings. Under unbiased stochastic oracles with uniformly bounded variance $ σ^2$, AR computes an approximate solution with expected operator residual bounded by $\varepsilon$ using at most $ \widetilde{O}\left(\tfrac{LD_0}{\varepsilon}+\tfrac{ σ^2}{\varepsilon^2}(\log\tfrac{LD_0}{\varepsilon})^3\right) $ stochastic oracle calls, where $L$ is the Lipschitz constant and $D_0$ bounds the initial distance to the solution. It substantially improves the existing $\mathcal{O}( σ^2/\varepsilon^4)$ complexity for residual reduction and matches the lower bound up to logarithmic factors. For strongly monotone VIs, measured by the distance to the solution, AR achieves the optimal oracle complexity when the strong monotonicity modulus is known. By treating the problem as merely monotone, AR still achieves nearly optimal complexity without knowledge of this modulus. We further introduce a state-dependent noise model applicable to general monotone VIs with potentially nonunique solutions, extending state-dependent noise analysis beyond the strongly monotone setting. Under this model, AR, when equipped with an enhanced stochastic operator extrapolation (SOE) method, achieves nearly optimal complexity with the stochastic term depending on the variance at a solution.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\sigma^{2}$

* Equation: $\sigma^{2}$
* Symbols: $\sigma^{2}$ (variance)
* Why it matters: This equation represents the variance of the stochastic oracle.

### Equation 2: $\varepsilon$

* Equation: $\varepsilon$
* Symbols: $\varepsilon$ (error tolerance)
* Why it matters: This equation represents the desired error tolerance for the approximate solution.

### Equation 3: $\widetilde{\mathcal{O}}\left(\tfrac{LD_{0}}{\varepsilon}+\tfrac{\sigma^{2}}{\varepsilon^{2}}(\log\tfrac{LD_{0}}{\varepsilon})^{3}\right)$

* Equation: $\widetilde{\mathcal{O}}\left(\tfrac{LD_{0}}{\varepsilon}+\tfrac{\sigma^{2}}{\varepsilon^{2}}(\log\tfrac{LD_{0}}{\varepsilon})^{3}\right)$
* Symbols: $\widetilde{\mathcal{O}}$ (approximate time complexity), $L$ ( Lipschitz constant), $D_{0}$ (operator norm), $\varepsilon$ (error tolerance), $\sigma^{2}$ (variance)
* Why it matters: This equation represents the approximate time complexity of the accumulative regularization method.

### Equation 4: $D_{0}$

* Equation: $D_{0}$
* Symbols: $D_{0}$ (operator norm)
* Why it matters: This equation represents the operator norm of the operator $F$.

### Equation 5: $\mathcal{O}(\sigma^{2}/\varepsilon^{4})$

* Equation: $\mathcal{O}(\sigma^{2}/\varepsilon^{4})$
* Symbols: $\mathcal{O}$ (time complexity), $\sigma^{2}$ (variance), $\varepsilon$ (error tolerance)
* Why it matters: This equation represents the time complexity of the accumulative regularization method.

**Method Summary**
==================

* The accumulative regularization method is a general framework for computing strong solutions of monotone variational inequalities.
* The method targets a series of regularized VI subproblems and computes their approximate solutions using a subroutine.
* The method is applied to policy evaluation in reinforcement learning, where it is used to solve the operator equation $F(\theta) = 0$.

**Experimental Overview**
=========================

* Tasks/Datasets: Policy evaluation in reinforcement learning.
* Baselines/Comparisons: Classical TD learning, stochastic forward operator method.
* Main Claimed Findings: The accumulative regularization method achieves fast decay of the Bellman residual, outperforming classical TD learning and stochastic forward operator method.

**What to Verify in the PDF**
=============================

* The proof of the convergence of the accumulative regularization method for stochastic oracles.
* The analysis of the time complexity of the accumulative regularization method.
* The experimental results for policy evaluation in reinforcement learning, including the performance of the accumulative regularization method compared to classical TD learning and stochastic forward operator method.
{% endraw %}

{% raw %}
## 3) Para-Pipe: Exploiting Hierarchical Operator Parallelism of ML Computational Graphs on SoCs
- **Authors:** Yujie Zhang, Huiying Lan, Ehsan Aghapour, Zhiyuan Ning, Peng Zan, Weidong Shao, Anuj Pathania, Tulika Mitra
- **arXiv:** [2609.04168](https://arxiv.org/abs/2609.04168v1) · [pdf](https://arxiv.org/pdf/2609.04168v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.04168v1))
- **Categories:** cs.DC, cs.LG, cs.PF

### Abstract
> As edge-based deep learning applications become more complex, optimizing performance on heterogeneous System-on-Chips (SoCs) presents unique challenges. Traditional pipelining techniques distributing the computation across different on-chip processing units, while effective for throughput, do not address the latency demands posed by modern neural networks with complex interdependencies and extensive operator parallelism. There is a potential in leveraging operator parallelism to enable concurrent execution across multiple processing units, thereby reducing inference latency. However, prioritizing pipelining or parallel execution often necessitates a compromise, where optimizing one performance metric adversely impacts the other. This paper introduces Para-Pipe, a hierarchical mapping framework that integrates intra- and inter-stage operator parallelism within a pipelined architecture. Para-Pipe navigates the trade-off between throughput and latency by selectively fine-tuning parallelism levels within and across pipeline stages. This strategy can significantly reduce inter-processor communication overhead, significantly improving energy efficiency. Our evaluation demonstrates that Para-Pipe generates multiple Pareto-optimal configurations, achieving a balance between throughput and latency on an Amlogic SoC equipped with ARM big.LITTLE CPUs and GPU, as well as the Black Sesame Technology SoC featuring a deep learning accelerator and two DSPs. More importantly, throughput-optimized configurations under Para-Pipe on Amlogic SoC show an average energy efficiency improvement of 11.0% over purely pipelined strategies and 23.3% relative to non-pipelined parallel execution.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 1.15

* Equation: 1.15
* Symbols: None
* Why it matters: This value is mentioned as the peak performance level of the ARM GPU on the Khadas Vim3 Pro platform.

### Equation 2: 1.25

* Equation: 1.25
* Symbols: None
* Why it matters: This value is not explicitly mentioned in the context, but it might be related to the performance level of the ARM GPU.

### Equation 3: inputs

* Equation: inputs
* Symbols: None
* Why it matters: This is a variable representing the inputs to the neural network.

### Equation 4: outputs

* Equation: outputs
* Symbols: None
* Why it matters: This is a variable representing the outputs of the neural network.

### Equation 5: subgraphs

* Equation: subgraphs
* Symbols: None
* Why it matters: This is a variable representing the subgraphs of the neural network, which are used in the Para-Pipe framework.

**Method Summary**
==================

* The Para-Pipe framework exploits hierarchical operator parallelism of ML computational graphs on SoCs.
* The framework uses a combination of coarse-grained and fine-grained mapping strategies to achieve optimal performance.
* The authors evaluate the performance of Para-Pipe on two SoCs, Amlogic and BST, and compare it to traditional pipelining techniques.
* The framework is designed to balance throughput and latency, and it achieves Pareto optimality in terms of both metrics.

**Experimental Overview**
========================

* Tasks:
	+ Evaluate the performance of Para-Pipe on Amlogic and BST SoCs.
	+ Compare Para-Pipe to traditional pipelining techniques.
* Datasets:
	+ Six modern models with dense operator parallelism (GoogLeNet, Inception-v3, Inception-v4, Inception-ResNet-v2, PETR-based network, and BEVFormer-based network).
* Baselines/Comparisons:
	+ Traditional pipelining techniques.
	+ Coarse-grained and fine-grained mapping strategies.
* Main claimed findings:
	+ Para-Pipe achieves optimal performance in terms of both throughput and latency.
	+ The framework is designed to balance throughput and latency.

**What to Verify in the PDF**
=============================

* The detailed implementation of the Para-Pipe framework, including the Graph Partitioner and the Pipeline Configuration Generator.
* The evaluation of the framework on the BST SoC, including the simulation results.
* The analysis of the synchronization overhead and its impact on the performance of Para-Pipe.
{% endraw %}

{% raw %}
## 4) Parameterised graph theory for tensor networks: entanglement rerouting, structural simplification, and agnostic tomography
- **Authors:** Matthias C. Caro, Natalie McHugh, Sergii Strelchuk
- **arXiv:** [2609.04165](https://arxiv.org/abs/2609.04165v1) · [pdf](https://arxiv.org/pdf/2609.04165v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.04165v1))
- **Categories:** quant-ph, cs.DS, cs.LG

### Abstract
> Parameterised graph theory studies how the complexity of graph-theoretic problems depends on structural parameters of the input graph. This perspective has proved useful in analysing tensor-network simulation (Markov and Shi, 2008). Its implications for tensor-network representations and tomography are less well understood. In particular, which graph parameters determine whether a tensor-network state (TNS) admits a tractable matrix product state (MPS) or tree tensor network (TTN) representation, and which control the complexity of learning the state? We address these questions using parameterised graph theory. First, we show that cutwidth and tree-cutwidth bound the bond dimension overhead required to represent a TNS as an MPS or TTN. In the TTN case, tree-cutwidth also bounds the local dimension of the grouped subsystems. The proofs are based on entanglement rerouting, a tensor-network analogue of rerouting information in a classical network. Second, we derive graph-dependent upper bounds on the sample and computational complexity of realisable TNS tomography, with exponents that depend on cutwidth, tree-cutwidth, and a new graph parameter, learning complexity, which we bound in terms of degree and treewidth. We obtain these results by extending the disentangling MPS learner of (Cramer et al., 2010), as analysed further in (Bakshi et al., 2025; Lin et al., 2025), to TTNs and to tensor networks on arbitrary known graphs. Finally, we extend the framework beyond the realisable setting. For an arbitrary input state, our agnostic learner outputs a pure state whose fidelity is within additive error $ε$ of the optimum over tensor-network states on the given graph with a given bond dimension, with explicit graph-dependent bounds on sample and computational complexity.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: \epsilon

* Equation: \epsilon
* Symbols: \epsilon (epsilon)
* Why it matters: Not found in extracted context.

### Equation 2: \mathsf{BQP}

* Equation: \mathsf{BQP}
* Symbols: \mathsf{BQP} (Bounded-Error Quantum Polynomial Time)
* Why it matters: Not found in extracted context.

### Equation 3: G=([n],E)

* Equation: G=([n],E)
* Symbols: G, [n], E
* Why it matters: Denotes the unweighted tensor-network topology, where G is the graph, [n] is the set of vertices, and E is the set of edges.

### Equation 4: w:E\to\mathbb{N}

* Equation: w:E\to\mathbb{N}
* Symbols: w, E, \mathbb{N}
* Why it matters: Defines a weight function w that maps each edge e in E to a natural number \mathbb{N}.

### Equation 5: \mathcal{S}_{d}(G,w)

* Equation: \mathcal{S}_{d}(G,w)
* Symbols: \mathcal{S}_{d}, G, w
* Why it matters: Denotes the class of pure n n -qudit states admitting a TN representation with virtual dimension w(e) on each edge e.

### Equation 6: w(e)

* Equation: w(e)
* Symbols: w, e
* Why it matters: Represents the weight function w applied to edge e.

### Equation 7: \mathcal{S}_{d}(G,\chi)

* Equation: \mathcal{S}_{d}(G,\chi)
* Symbols: \mathcal{S}_{d}, G, \chi
* Why it matters: Denotes the class of pure n n -qudit states admitting a TN representation with a common upper bound \chi on the virtual dimensions.

### Equation 8: \chi

* Equation: \chi
* Symbols: \chi
* Why it matters: Represents a common upper bound on the virtual dimensions for the class \mathcal{S}_{d}(G,\chi).

**Method Summary**
==================

* The authors use parameterised graph theory to study properties of TN representations beyond simulability.
* They show how to transform a TN representation of a general graph to an MPS or TTN representation with bond dimension bounded in terms of suitable graph parameters.
* They also give upper bounds on the sample complexity of TNS learning for general graphs in terms of graph parameters.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors do not specify any specific tasks or datasets.
* Baselines/Comparisons: The authors do not mention any baselines or comparisons.
* Main Claimed Findings: The authors claim to show how to transform a TN representation of a general graph to an MPS or TTN representation with bond dimension bounded in terms of suitable graph parameters, and to give upper bounds on the sample complexity of TNS learning for general graphs in terms of graph parameters.

**What to Verify in the PDF**
=============================

* The authors mention entanglement rerouting, but do not provide any details on how it works or what it achieves.
* The authors also mention that the transformation from a TN representation to an MPS or TTN representation can be done in terms of suitable graph parameters, but do not provide any specific details on how this is achieved.
* The authors also mention that the sample complexity of TNS learning for general graphs can be bounded in terms of graph parameters, but do not provide any specific details on how this is achieved.
{% endraw %}

{% raw %}
## 5) Robust PAC Learning of Concurrent Stochastic Games
- **Authors:** Angel Y. He, David Parker
- **arXiv:** [2609.04189](https://arxiv.org/abs/2609.04189v1) · [pdf](https://arxiv.org/pdf/2609.04189v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2609.04189v1))
- **Categories:** cs.LG, cs.GT, cs.LO, cs.MA

### Abstract
> We introduce the first Probably Approximately Correct (PAC) learning framework for general-sum concurrent stochastic games (CSGs) with transition uncertainty, while addressing the challenge of Nash equilibrium (NE) existence. Our algorithm maintains data-driven $L^1$ confidence sets over transition kernels and solves a robust CSG to compute a social-welfare optimal $\varepsilon$-NE, using a robust MDP-based exploration mechanism to drive joint state-action coverage. Crucially, we introduce a Nash margin characterisation that enables principled reasoning about equilibrium existence: the framework either returns an $\varepsilon$-approximate NE whose social-welfare value is $\varepsilon$-close to optimal, or provides a sound certificate that no exact NE exists. Under a minimum reachability condition $p_{\mathrm{reach}}>0$ over relevant state-action pairs, the algorithm terminates after a polynomial number of trajectory samples, with sample complexity $\widetilde{O}\left( {R_{\max}^2 H^4 |S|^2 |A| / (p_{\mathrm{reach}} \varepsilon^2)} \right)$. Empirical results on benchmark CSGs demonstrate near-optimal performance, correct handling of equilibrium (non-)existence, and sample complexity consistent with theory.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: L^{1}

* Equation: L^{1} = \sum_{(s,a) \in \mathcal{X}_{\mathrm{nt}}} |P(s,a) - \hat{P}(s,a)|
* Symbols: L^{1} (L1), \mathcal{X}_{\mathrm{nt}} (non-target slots), P(s,a) (transition kernel), \hat{P}(s,a) (estimated transition kernel)
* Why it matters: L^{1} is a measure of the difference between the true and estimated transition kernels, used to construct confidence sets for the transition kernels.

### Equation 2: \varepsilon

* Equation: \varepsilon = \max_{(s,a) \in \mathcal{X}_{\mathrm{nt}}} |P(s,a) - \hat{P}(s,a)|
* Symbols: \varepsilon (error tolerance), \mathcal{X}_{\mathrm{nt}} (non-target slots), P(s,a) (transition kernel), \hat{P}(s,a) (estimated transition kernel)
* Why it matters: \varepsilon is the maximum error allowed between the true and estimated transition kernels, used to construct confidence sets.

### Equation 3: p_{\mathrm{reach}} > 0

* Equation: p_{\mathrm{reach}} > 0
* Symbols: p_{\mathrm{reach}} (reachability probability), \mathcal{X}_{\mathrm{nt}} (non-target slots)
* Why it matters: p_{\mathrm{reach}} > 0 ensures that the reachability problem is well-defined and that the algorithm can terminate.

### Equation 4: \widetilde{\mathcal{O}}\!\left({R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})}\right)

* Equation: \widetilde{\mathcal{O}}\!\left({R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})}\right)
* Symbols: \widetilde{\mathcal{O}}\!\left({R_{\max}^{2}H^{4}|S|^{2}|A|/(p_{\mathrm{reach}}\varepsilon^{2})}\right) (sample complexity), R_{\max} (maximum reachability distance), H (horizon), S (states), A (actions), p_{\mathrm{reach}} (reachability probability), \varepsilon (error tolerance)
* Why it matters: This equation provides an upper bound on the sample complexity required to achieve a certain level of accuracy in the learned profile.

### Equation 5: \varepsilon > 0

* Equation: \varepsilon > 0
* Symbols: \varepsilon (error tolerance)
* Why it matters: \varepsilon > 0 ensures that the algorithm is able to learn a profile that is close to the true one.

**Method Summary**
==================

* The algorithm uses a PAC-CSG framework to learn a profile that is close to the true one.
* The algorithm maintains data-driven L^{1} confidence sets over transition kernels.
* The algorithm solves a robust CSG to compute a social-welfare optimal ε-NE.
* The algorithm uses a robust MDP-based exploration mechanism to drive joint state-action coverage.

**Experimental Overview**
========================

* Tasks/Datasets: The algorithm is evaluated on a suite of benchmark CSGs.
* Baselines/Comparisons: The algorithm is compared to the PRISM-games CSG solver.
* Main Claimed Findings: The algorithm is able to learn a profile that is close to the true one, and that the learned profile is near-optimal.

**What to Verify in the PDF**
=============================

* The proof of the sample complexity bound.
* The details of the reachability problem used to compute p_{\mathrm{reach}}.
* The implementation of the algorithm in Java and its evaluation in the PRISM-games model checker.
{% endraw %}
