---
layout: post
title: "Daily arXiv Digest — 2026-07-28 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Global Convergence of DGM and PINN Algorithms for Solving Nonlinear PDEs
- **Authors:** Justin Sirignano, Konstantinos Spiliopoulos, Samuel Cohen
- **arXiv:** [2607.24726](https://arxiv.org/abs/2607.24726v1) · [pdf](https://arxiv.org/pdf/2607.24726v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.24726v1))
- **Categories:** cs.LG, math.NA

### Abstract
> The Deep Galerkin Method (DGM) and Physics Informed Neural Networks (PINNs) have become widely-used methods for solving partial differential equations (PDEs) in the rapidly growing field of scientific machine learning. In these methods, a neural network is trained to approximate the PDE solution by using (stochastic) gradient descent to minimize the PDE residual of the neural network. Due to the non-convexity of the PDE residual objective function, the trained neural network may, in principle, only converge to a local minimizer of the objective function (which would not be a solution of the PDE). Therefore, there is a longstanding question regarding the mathematical foundations of these algorithms, and it is highly valuable to establish that the trained neural network will converge to the PDE solution. For a class of semi-linear PDEs (nonlinear in the solution and its first derivative), we prove that neural networks trained with gradient descent to minimize the PDE residual objective function will converge to the PDE solution.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{A}_{u}u$

* Equation: $\mathcal{A}_{u}u$
* Symbols: $\mathcal{A}_{u}$ (operator), $u$ (solution)
* Why it matters: This equation represents the PDE that the neural network is trying to solve.

### Equation 2: $\frac{\partial u}{\partial t} + \mathcal{A}_{u}u = g$

* Equation: $\frac{\partial u}{\partial t} + \mathcal{A}_{u}u = g$
* Symbols: $\frac{\partial u}{\partial t}$ (partial derivative), $\mathcal{A}_{u}$ (operator), $u$ (solution), $g$ (source term)
* Why it matters: This is the original PDE that the neural network is trying to solve.

### Equation 3: $g, x \in \Omega$

* Equation: $g, x \in \Omega$
* Symbols: $g$ (source term), $x$ (spatial variable), $\Omega$ (domain)
* Why it matters: This equation specifies the domain and source term of the PDE.

### Equation 4: $u = 0, x \in \partial\Omega$

* Equation: $u = 0, x \in \partial\Omega$
* Symbols: $u$ (solution), $x$ (spatial variable), $\partial\Omega$ (boundary)
* Why it matters: This equation specifies the boundary condition of the PDE.

### Equation 5: $\Omega \subset \mathbb{R}^{n}$

* Equation: $\Omega \subset \mathbb{R}^{n}$
* Symbols: $\Omega$ (domain), $\mathbb{R}^{n}$ (space)
* Why it matters: This equation specifies the domain of the PDE.

**Method Summary**
==================

* The paper presents a convergence analysis of the Deep Galerkin Method (DGM) and Physics Informed Neural Networks (PINNs) for solving nonlinear PDEs.
* The authors derive formulas for the evolution of the objective function and the neural network as a function of the training time.
* They use clipped gradient descent to analyze the convergence of the neural network.
* The authors prove that the neural network converges to the PDE solution as the number of training iterations increases.

**Experimental Overview**
========================

* Tasks/Datasets: The paper does not specify a particular dataset or task.
* Baselines/Comparisons: The paper does not compare the performance of the DGM and PINNs with other methods.
* Main Claimed Findings: The authors claim that the neural network trained with clipped gradient descent converges to the PDE solution as the number of training iterations increases.

**What to Verify in the PDF**
=============================

* The authors use a specific clipping procedure to analyze the convergence of the neural network. It would be interesting to verify the effect of different clipping procedures on the convergence of the neural network.
* The paper assumes that the nonlinearity $f(v, w)$ is properly defined. It would be interesting to verify the robustness of the convergence analysis to different nonlinearity definitions.
* The authors use a specific kernel function $\phi(x)$. It would be interesting to verify the effect of different kernel functions on the convergence of the neural network.
{% endraw %}

{% raw %}
## 2) Beyond Scale and Generation: Understanding Language Model-based Entity Matching
- **Authors:** Zeyu Zhang, Xue Li, Iacer Calixto, Paul Groth, Sebastian Schelter
- **arXiv:** [2607.24688](https://arxiv.org/abs/2607.24688v1) · [pdf](https://arxiv.org/pdf/2607.24688v1)
- **LLM context source:** abstract only
- **Categories:** cs.DB, cs.CL, cs.LG

### Abstract
> Entity matching identifies records that refer to the same real-world entity. Language models can be adapted to this task through bi-encoder, cross-encoder, and generative matcher architectures. However, prior studies often conflate matcher architecture with differences in model backbone, model variant(reflecting different pretraining objectives), and model size, making it difficult to isolate the sources of performance gains. We address this issue through a controlled factorial study spanning three matcher architectures, three model variants and three model sizes from the Qwen3 family, and nine datasets, totaling 1,215 fine-tuning runs. We also evaluate cross-dataset transferability and computational cost. Our results show that model variant is critical for bi-encoders: embedding-oriented variants provide stronger initialization and more favorable representation geometry predictive of downstream matching performance. Cross-encoders retain a consistent advantage over bi-encoders because they jointly encode record pairs rather than representing each record independently, although larger models partially narrow this gap. Generative matchers do not universally outperform cross-encoders. Instead, their advantages concentrate under distribution shift, including subtle unseen differences in record schemas and cross-dataset transfer. We further find that larger models rely more heavily on shortcut learning and therefore do not necessarily perform better. These findings clarify the factors underlying performance differences across matcher architectures and motivate future research and benchmark designs that better disentangle architectural choices from model-level factors while explicitly evaluating distribution shift and cross-dataset transferability. We release our experimental results, code, training scripts, and evaluation data at https://github.com/Jantory/llm-trained-matcher.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
Unfortunately, no specific equations are mentioned in the extracted context.

### Method Summary
* The authors conduct a controlled factorial study with three matcher architectures (bi-encoder, cross-encoder, and generative matcher), three model variants, and three model sizes from the Qwen3 family.
* The study spans nine datasets, totaling 1,215 fine-tuning runs.
* The authors evaluate cross-dataset transferability and computational cost.

### Experimental Overview
* Tasks/Datasets: Entity matching, using nine datasets.
* Baselines/Comparisons: The authors compare the performance of different matcher architectures and model variants.
* Main Claimed Findings:
  * Model variant is critical for bi-encoders.
  * Cross-encoders retain a consistent advantage over bi-encoders.
  * Generative matchers do not universally outperform cross-encoders.
  * Larger models rely more heavily on shortcut learning.

### What to Verify in the PDF
* The exact experimental setup, including the specific datasets used for each matcher architecture and model variant.
* The evaluation metrics used to measure performance, such as precision, recall, and F1-score.
* The results of the cross-dataset transferability evaluation, including any notable differences in performance across datasets.
{% endraw %}

{% raw %}
## 3) Explainable Reinforcement Learning via Physics-Aware Policy Distillation
- **Authors:** Shaker Al-Tamari, Waled Kadour
- **arXiv:** [2607.24672](https://arxiv.org/abs/2607.24672v1) · [pdf](https://arxiv.org/pdf/2607.24672v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.24672v1))
- **Categories:** cs.LG

### Abstract
> In safety-critical sectors such as robotics and automotive engineering, the deployment of Deep Reinforcement Learning (DRL) is often hindered by the black-box nature of deep neural networks. This lack of transparency poses significant challenges for regulatory compliance and human-agent trust. This paper presents an experimental study aimed at making high-performance continuous control DRL systems interpretable. A policy distillation framework is implemented using the classic Inverted Pendulum benchmark. A high-performance Twin Delayed DDPG (TD3) agent serves as an opaque, continuous teacher model, whose policy is distilled into an interpretable student surrogate based on a shallow Decision Tree. By leveraging a custom physics-aware feature and "Noisy Oracle Rollouts" for dataset generation, the distillation process achieves performance equivalent to the expert teacher. Furthermore, comparative control theory analysis reveals a fundamental trade-off: transitioning from continuous to discrete rule-based control induces high-frequency Bang-Bang actuation and a stable bimodal limit cycle. Simulation results indicate that Bounded-Input Bounded-Output (BIBO) stability is maintained while providing both global and local interpretability for safe autonomous systems.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: π_T
π_T = π_T(s, a)

* Equation: π_T(s, a) represents the policy of the teacher model.
* Symbols: π_T(s, a) is a function that maps states (s) to actions (a).
* Why it matters: This equation represents the policy of the teacher model, which is used to guide the learning process.

### Equation 2: π_S
π_S = π_S(s; θ_S)

* Equation: π_S(s; θ_S) represents the policy of the student model.
* Symbols: π_S(s; θ_S) is a function that maps states (s) to actions (a) using parameters θ_S.
* Why it matters: This equation represents the policy of the student model, which is learned through policy distillation.

### Equation 3: d^π_S
d^π_S = d^π_S(s, a)

* Equation: d^π_S(s, a) represents the derivative of the policy π_S with respect to the state-action pair (s, a).
* Symbols: d^π_S(s, a) is a function that maps states (s) to actions (a) to the derivative of the policy.
* Why it matters: This equation is used to compute the gradient of the loss function with respect to the student model's parameters.

### Equation 4: J(π_S)
J(π_S) = E_s∼d^π_S[ℓ(π_T(s), π_S(s))]

* Equation: J(π_S) represents the expected loss of the student model.
* Symbols: J(π_S) is the expected loss of the student model, computed over the dataset d^π_S.
* Why it matters: This equation represents the expected loss of the student model, which is used to evaluate its performance.

### Equation 5: Q^π_T(s, a)
Q^π_T(s, a) = Q^π_T(s, a; θ_T)

* Equation: Q^π_T(s, a) represents the value function of the teacher model.
* Symbols: Q^π_T(s, a; θ_T) is a function that maps states (s) to actions (a) using parameters θ_T.
* Why it matters: This equation represents the value function of the teacher model, which is used to compute the expected return.

**Method Summary**
==================

* The proposed method uses policy distillation to transfer knowledge from a complex neural network teacher to a simpler, interpretable student model.
* The teacher model is a Twin Delayed DDPG (TD3) agent, which is trained to maximize the expected return in the InvertedPendulum-v4 environment.
* The student model is a Decision Tree, which is trained to approximate the policy of the teacher model using "Noisy Oracle Rollouts" and a physics-aware feature.

**Experimental Overview**
=========================

* Tasks/Datasets: The proposed method is evaluated on the InvertedPendulum-v4 environment, which is a classic control theory benchmark.
* Baselines/Comparisons: The proposed method is compared to a baseline that uses a standard optimal agent, which is not interpretable.
* Main Claimed Findings: The proposed method achieves performance equivalent to the expert teacher model, while providing global and local interpretability for safe autonomous systems.

**What to Verify in the PDF**
=============================

* The custom physics-aware feature used in the proposed method is not explicitly defined in the abstract. Verify the definition of this feature in the PDF.
* The "Noisy Oracle Rollouts" used in the proposed method are not explicitly defined in the abstract. Verify the definition of this rollout strategy in the PDF.
* The results of the comparative control theory analysis are not explicitly shown in the abstract. Verify the results of this analysis in the PDF.
{% endraw %}

{% raw %}
## 4) When Can You Correct Distribution Drift in Temporal Graph Generation? A Sharpening--Drift Tension and an Impossibility for Observation-Based Correction
- **Authors:** Tianpeng Li, Xuan Guo, Wenjun Wang, Wang Zhang, Pengfei Jiao
- **arXiv:** [2607.24662](https://arxiv.org/abs/2607.24662v1) · [pdf](https://arxiv.org/pdf/2607.24662v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.24662v1))
- **Categories:** cs.LG, cs.SI

### Abstract
> Generative models of temporal graphs are trained on one stretch of an evolving network and deployed on the next, and they degrade badly in the gap. We show this degradation is derivable, general, and not fixable from observations. The masked flow-matching loss decomposes exactly, with no independence assumption, into an irreducible entropy plus a divergence whose derivative along the training path is positive precisely for structures rare during training and common at deployment, diverging as their training probability goes to zero. Empirically the trade-off is a power law with exponent $-0.605$ ($R^2=0.9977$), and drift raises the sampler's error floor without changing how many steps reach it: across seven well-powered conditions the drift-period marginal error varies by at most $6\%$ over a $50\times$ range of sampling budgets, while the floor sits $2.2\times$ to $34.3\times$ above the in-period floor. Because the deployment period is observed, correction looks like a matter of measurement. It is not. We prove that any corrector measurable with respect to past observations leaves at least the conditional variance of the statistic it tracks, and that trend extrapolation beats trusting the last observation only when $μ^2>v(1-2ρ)$. Both premises are measurable and both go the wrong way: the drift is trendless and mean-reverting, with a one-step innovation as large as the drift itself. An oracle removes $60\%$ of the error, the best observation-based corrector recovers $5.7\%$ of that, and extrapolation is strictly worse than doing nothing clever.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

1. **Equation 1: -0.605**
   - Equation: -0.605
   - Symbols: None
   - Why it matters: This is the exponent of the power law trade-off between drift and error floor.

2. **Equation 2: R^{2}=0.9977**
   - Equation: R^2 = 0.9977
   - Symbols: R^2
   - Why it matters: This is the R-squared value of the power law trade-off between drift and error floor.

3. **Equation 3: 50\times**
   - Equation: 50 ×
   - Symbols: 50
   - Why it matters: This is the range of sampling budgets used in the experiment.

4. **Equation 4: 2.2\times**
   - Equation: 2.2 ×
   - Symbols: 2.2
   - Why it matters: This is the error floor above the in-period floor.

5. **Equation 5: 34.3\times**
   - Equation: 34.3 ×
   - Symbols: 34.3
   - Why it matters: This is the error floor above the in-period floor.

6. **Equation 6: \mu^{2}>v(1-2\rho)**
   - Equation: μ^2 > v(1 - 2ρ)
   - Symbols: μ^2, v, ρ
   - Why it matters: This is the condition under which trend extrapolation beats trusting the last observation.

7. **Equation 7: 60\%**
   - Equation: 60%
   - Symbols: None
   - Why it matters: This is the error reduction achieved by an oracle.

8. **Equation 8: 5.7\%**
   - Equation: 5.7%
   - Symbols: None
   - Why it matters: This is the error reduction achieved by the best observation-based corrector.

**Method Summary**
==================

* The authors propose no method for correcting distribution drift in temporal graph generation.
* They argue that the mechanism for re-aiming a discrete generator is off the shelf and the idea of extrapolating a temporal trend is already taken.
* The focus is on proving the impossibility of observation-based correction and publishing the bound and the measurement.

**Experimental Overview**
=========================

* Tasks/Datasets: Temporal graph generation
* Baselines/Comparisons: None mentioned
* Main claimed findings: The error floor is raised by drift, and trend extrapolation beats trusting the last observation under certain conditions.

**What to Verify in the PDF**
=============================

* The derivation of the masked flow-matching loss and its decomposition into irreducible entropy and divergence.
* The proof of the impossibility of observation-based correction and the condition under which trend extrapolation beats trusting the last observation.
* The experimental results and the power law trade-off between drift and error floor.
{% endraw %}

{% raw %}
## 5) Efficiency Matters in Autonomous Research
- **Authors:** Haiqian Yang, Yuan Cao
- **arXiv:** [2607.24647](https://arxiv.org/abs/2607.24647v1) · [pdf](https://arxiv.org/pdf/2607.24647v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.24647v1))
- **Categories:** cs.AI, cs.LG

### Abstract
> AI-driven autonomous research (AR) systems are becoming increasingly effective across a broad range of tasks. Their performance, however, is still evaluated primarily by the quality of the final outcome. In this paper, we argue that the efficiency of the solution-search process is an equally important but often overlooked dimension of performance. A strong AR system should not only produce high-quality results, but also reach them with as small a budget as possible. Search efficiency will become increasingly important as AR expands from domains with inexpensive verification, such as mathematics and coding, to real-world scientific settings in which solution evaluation may require costly physical experiments. To capture this dimension, we propose evaluating AR systems using the area under the curve (AUC) of the Pareto frontier, alongside final outcome quality. We compare several families of search algorithms, including hill climbing, beam search, tree search, and evolutionary search, across twelve systems-optimization tasks. We find that no single search structure is consistently the most efficient. We also show that search efficiency and final outcome quality are distinct performance dimensions: a method that eventually achieves the best result may nevertheless improve slowly and consume substantially more evaluation budget before reaching that result. Because the most effective search policy is generally unknown in advance, we introduce an adaptive procedure called fluid search, which uses a portfolio bandit to dynamically allocate a fixed evaluation budget across a forest of search processes. Across the evaluated tasks, fluid search achieves the highest overall search efficiency, closely matching the performance of a per-task oracle that is given the best search structure for each task in advance.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: R(n)

* Equation: R(n)
* Symbols: R, n
* Why it matters: This equation is not explicitly defined in the provided context, but it seems to represent a reward function or a metric for evaluating the quality of solutions.

### Equation 2: \hat{R} = R(N)

* Equation: \hat{R} = R(N)
* Symbols: \hat{R}, R, N
* Why it matters: This equation represents the estimated reward or quality of the solution after N evaluations. It is likely used to calculate the average or expected reward.

### Equation 3: \bar{R}

* Equation: \bar{R}
* Symbols: \bar{R}
* Why it matters: This equation represents the average reward or quality of solutions across multiple evaluations. It is likely used to calculate the overall performance of the search algorithm.

### Equation 4: \bar{R}_{A} > \bar{R}_{B}

* Equation: \bar{R}_{A} > \bar{R}_{B}
* Symbols: \bar{R}_{A}, \bar{R}_{B}
* Why it matters: This equation represents a comparison between the average rewards of two different search algorithms or strategies. It is likely used to evaluate the relative performance of different approaches.

### Equation 5: \rightarrow

* Equation: \rightarrow
* Symbols: \rightarrow
* Why it matters: This equation represents the direction of the search process, indicating that the algorithm is moving towards a solution or improving the current state.

### Equation 6: x_{1}, x_{2}, \ldots, x_{N}

* Equation: x_{1}, x_{2}, \ldots, x_{N}
* Symbols: x_{1}, x_{2}, \ldots, x_{N}
* Why it matters: This equation represents the sequence of states or solutions explored by the search algorithm. It is likely used to track the progress of the search process.

**Method Summary**
==================

* The authors propose a novel search algorithm called fluid search, which uses a portfolio bandit to dynamically allocate a fixed evaluation budget across a forest of search processes.
* The algorithm is designed to adapt to changing problem structures and optimize the search process for each task.
* The authors also introduce an adaptive procedure called ArchiveUpdate, which retains diverse valid artifacts and replaces similar ones with higher-scoring ones.

**Experimental Overview**
========================

* The authors evaluate the performance of several search algorithms, including hill climbing, beam search, tree search, and evolutionary search, across twelve systems-optimization tasks.
* The tasks are designed to mimic real-world scientific settings, where solution evaluation may require costly physical experiments.
* The authors compare the performance of the search algorithms using the area under the curve (AUC) of the Pareto frontier, alongside final outcome quality.

**What to Verify in the PDF**
=============================

* The authors claim that fluid search achieves the highest overall search efficiency, closely matching the performance of a per-task oracle that is given the best search structure for each task in advance.
* The authors also claim that the search efficiency and final outcome quality are distinct performance dimensions, and that a method that eventually achieves the best result may nevertheless improve slowly and consume substantially more evaluation budget before reaching that result.
* The authors use a variety of metrics to evaluate the performance of the search algorithms, including the AUC of the Pareto frontier and the final outcome quality.
{% endraw %}
