---
layout: post
title: "Daily arXiv Digest — 2026-07-10 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Finding Simple Proofs for First-Order Optimization
- **Authors:** Daniel Berg Thomsen, Manu Upadhyaya, Baptiste Goujaud, Aymeric Dieuleveut, Adrien Taylor
- **arXiv:** [2607.08753](https://arxiv.org/abs/2607.08753v1) · [pdf](https://arxiv.org/pdf/2607.08753v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.08753v1))
- **Categories:** math.OC

### Abstract
> Progress in mathematics often requires more than a certificate of truth: it requires proof structures that are transparent, checkable, and reusable. Automated systems can increasingly certify that a result is true; what they typically return, however, is a dense certificate rather than an interpretable, reusable proof structure. Recent work on performance estimation problems has shown that performance bounds and complexity analyses of first-order optimization methods can be discovered by searching over a structured space of Lagrangian dual certificates. We cast the search for simpler proof structures as a second-stage optimization problem over these certificates. Starting from dual certificates, we develop post-processing procedures using tools from sparse optimization and statistical learning. We measure complexity through features such as active hypotheses and residual structure, and introduce methods based on exhaustive sparsification, weighted $\ell_1$-type heuristics, and semidefinite programming (SDP) formulations for discovering simple proofs and intermediate lemmas. Examples on gradient descent, proximal methods, and fast-gradient methods show that these procedures can autonomously prune redundant inequalities, reveal structured proof patterns, and, in the proximal setting, recover Lyapunov functions as intermediate lemmas that lead to simple, streamlined proofs. By distilling dense machine-generated certificates into compact proof structures, this workflow acts as a pre-processing step for the final proof, reducing the complexity that must be managed during human interpretation, reuse, and formalization.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\ell_{1}$

* Equation: $\ell_{1}$
* Symbols: $\ell_{1}$ (not defined in the context)
* Why it matters: Not found in extracted context.

### Equation 2: $\operatorname*{minimize}_{x\in\mathbb{R}^{d}}\;f\mathord{\left(x\right)}$

* Equation: $\operatorname*{minimize}_{x\in\mathbb{R}^{d}}\;f\mathord{\left(x\right)}$
* Symbols: $x$, $f(x)$
* Why it matters: This is the objective function for the minimization problem.

### Equation 3: $f:\mathbb{R}^{d}\to\mathbb{R}$

* Equation: $f:\mathbb{R}^{d}\to\mathbb{R}$
* Symbols: $f$, $x$, $d$
* Why it matters: This defines the function $f$ as a mapping from $\mathbb{R}^{d}$ to $\mathbb{R}$.

### Equation 4: $\mathcal{F}$

* Equation: $\mathcal{F}$
* Symbols: $\mathcal{F}$ (not defined in the context)
* Why it matters: Not found in extracted context.

### Equation 5: $\mathcal{T}_{\mathcal{A}}\mathord{\left(f,N,x_{0}\right)}$

* Equation: $\mathcal{T}_{\mathcal{A}}\mathord{\left(f,N,x_{0}\right)}$
* Symbols: $\mathcal{T}_{\mathcal{A}}$, $f$, $N$, $x_{0}$
* Why it matters: This is a notation for a transformation or operation involving the function $f$, parameters $N$ and $x_{0}$.

### Equation 6: $\mathcal{A}$

* Equation: $\mathcal{A}$
* Symbols: $\mathcal{A}$ (not defined in the context)
* Why it matters: Not found in extracted context.

### Equation 7: $f\in\mathcal{F}$

* Equation: $f\in\mathcal{F}$
* Symbols: $f$, $\mathcal{F}$
* Why it matters: This is a statement that the function $f$ belongs to the class $\mathcal{F}$.

**Method Summary**
================

* The paper proposes a method for finding simple proofs for first-order optimization problems.
* The method involves simplifying the proof structures of optimization problems using techniques such as sparsification and interpolation.
* The paper presents experimental results showing the effectiveness of the method on several different problems.

**Experimental Overview**
=====================

* Tasks/Datasets: The paper presents experimental results on several different optimization problems, including one-step gradient descent, fast-gradient methods, and proximal point methods.
* Baselines/Comparisons: The paper compares the proposed method to classical methods such as classical function-value contraction and proximal point methods.
* Main Claimed Findings: The paper claims that the proposed method can simplify the proof structures of optimization problems and recover tight proofs for the proximal point method and its accelerated variant.

**What to Verify in the PDF**
==========================

* The paper claims that the proposed method can simplify the proof structures of optimization problems and recover tight proofs for the proximal point method and its accelerated variant.
* The paper presents experimental results showing the effectiveness of the method on several different problems, but it is unclear how the results were obtained and what the limitations of the method are.
* The paper also mentions the use of a public source-code repository, but it is unclear what the code does and how it relates to the experimental results.
{% endraw %}

{% raw %}
## 2) Dimensionality Reduction Meets Network Science: Sensemaking on UMAP's kNN Graph
- **Authors:** Duen Horng Chau, Donghao Ren, Fred Hohman, Dominik Moritz
- **arXiv:** [2607.08746](https://arxiv.org/abs/2607.08746v1) · [pdf](https://arxiv.org/pdf/2607.08746v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.08746v1))
- **Categories:** cs.LG, cs.AI, cs.DS, cs.HC

### Abstract
> While UMAP is widely used for exploring high-dimensional data, typical workflows focus on its lower-dimensional embedding, largely overlooking the rich k-nearest-neighbor (kNN) graph that UMAP constructs internally. This graph encodes the data manifold in its original high-dimensional space, before the distortion that UMAP's 2D projection introduces. We demonstrate the untapped potential of this internal representation, showing how standard graph algorithms applied to this graph enhance data sensemaking: (1) PageRank identifies representative data points, (2) k-core decomposition reveals dense core regions versus sparse periphery, and (3) clustering coefficient detects tight-knit neighborhoods with highly-similar data points. Through quantitative and qualitative evaluation on MNIST and Fashion MNIST, we show that these graph-based analyses are not only practical but also competitive with or complementary to purpose-built methods (e.g., k-medoids for exemplar selection, HDBSCAN for density-based clustering).
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
================================

### Equation 1: σ_i

σ_i = bandwidth

* Equation: σ_i = bandwidth
* Symbols: σ_i (bandwidth), i (index)
* Why it matters: The bandwidth σ_i is used to calculate the edge weights in the kNN graph. It is calibrated so that the total outgoing weight of each point is approximately constant regardless of local density.

### Equation 2: [0,1]

[0,1]

* Equation: [0,1]
* Symbols: [0,1] (interval)
* Why it matters: This equation is not explicitly used in the paper, but it is mentioned as a possible range for the edge weights in the kNN graph.

### Equation 3: ρ=0.93

ρ=0.93

* Equation: ρ=0.93
* Symbols: ρ (correlation coefficient), 0.93 (value)
* Why it matters: This equation is used to evaluate the correlation between the PageRank rankings and the k-core coreness on the Fashion MNIST dataset.

### Equation 4: 4.3×

4.3×

* Equation: 4.3×
* Symbols: 4.3 (value), × (multiplication)
* Why it matters: This equation is used to evaluate the performance of the k-core decomposition on the Fashion MNIST dataset.

### Equation 5: ρ ∼ 0.95

ρ ∼ 0.95

* Equation: ρ ∼ 0.95
* Symbols: ρ (correlation coefficient), ∼ (approximation), 0.95 (value)
* Why it matters: This equation is used to evaluate the correlation between the PageRank rankings and the k-core coreness on the MNIST dataset.

**Method Summary**
================

* The authors apply standard graph algorithms to the kNN graph constructed by UMAP to enhance data sensemaking.
* The algorithms used are:
	+ PageRank to identify representative data points
	+ k-core decomposition to reveal dense core regions versus sparse periphery
	+ Clustering coefficient to detect tight-knit neighborhoods with highly-similar data points
* The authors evaluate the performance of these algorithms on the MNIST and Fashion MNIST datasets.

**Experimental Overview**
=====================

* Tasks:
	+ Evaluating the stability of representatives across neighborhood sizes using PageRank
	+ Evaluating the representativeness and class balance of the selected points
	+ Evaluating the structural characterization of the k-core decomposition
	+ Evaluating the clustering coefficient
* Datasets:
	+ MNIST
	+ Fashion MNIST
* Baselines:
	+ k-k-medoids
	+ HDBSCAN
* Main claimed findings:
	+ PageRank selects representative data points that are not artifacts of a particular neighborhood scale
	+ k-core decomposition reveals dense core regions versus sparse periphery
	+ Clustering coefficient detects tight-knit neighborhoods with highly-similar data points

**What to Verify in the PDF**
==========================

* The authors claim that the k-core decomposition produces a graduated hierarchy that distinguishes core from periphery within each cluster. Verify that this is indeed the case by examining the results of the k-core decomposition on the Fashion MNIST dataset.
* The authors also claim that the clustering coefficient is moderately correlated with k-core coreness and PageRank rankings. Verify that this is indeed the case by examining the results of the clustering coefficient evaluation on the MNIST and Fashion MNIST datasets.
* The authors mention that the top 5% of points by CC have mean neighborhood label purity of 0.98 on MNIST and 0.94 on Fashion MNIST. Verify that this is indeed the case by examining the results of the clustering coefficient evaluation on the MNIST and Fashion MNIST datasets.
{% endraw %}

{% raw %}
## 3) ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation
- **Authors:** Kaifeng Zhao, Mathis Petrovich, Haotian Zhang, Tingwu Wang, Siyu Tang, Davis Rempe
- **arXiv:** [2607.08741](https://arxiv.org/abs/2607.08741v1) · [pdf](https://arxiv.org/pdf/2607.08741v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.08741v1))
- **Categories:** cs.GR, cs.CV, cs.LG, cs.RO

### Abstract
> Generating realistic 3D human motions in real-time within interactive applications is key for animation, simulation, and humanoid robotics. While recent offline motion generation approaches offer precise control via text and kinematic constraints, they lack the inference speed required for interactive settings. Conversely, existing online methods enable real-time synthesis but often sacrifice controllability or struggle with complex text semantics and long-horizon goals due to limited context windows. In this work, we introduce ARDY, a streaming generation framework that bridges this gap by enabling high-fidelity motion generation controllable via online text prompts and flexible kinematic constraints. ARDY employs a hybrid representation that combines explicit root features with a latent body embedding, balancing precise trajectory control with efficient generative learning. We propose a two-stage autoregressive transformer denoiser that features variable history context and supports conditioning on flexible, long-horizon kinematic constraints. By training on a large-scale motion capture dataset and being directly conditioned on text labels and kinematic constraints sampled from ground truth poses, ARDY natively learns controllable generation that supports online prompting and flexible long-horizon goals. Extensive evaluations on the HumanML3D benchmark and the large-scale, high-fidelity Bones Rigplay dataset demonstrate ARDY's high motion quality and constraint adherence, validating the efficacy of our key architectural decisions. Finally, we demonstrate the method's practical versatility through an interactive demo featuring dynamic text control, diverse keyframe pose constraints, path following, and interactive locomotion control via mouse and keyboard. Supplementary video results, code, and model releases can be found at https://research.nvidia.com/labs/sil/projects/ardy/.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

Here's a walkthrough of the first five equations extracted from the context:

### Equation 1: $\mathbf{m} = (\mathbf{m}_{\text{root}}, \mathbf{m}_{\text{body}}) \in \mathbb{R}^{M}$

* Equation: $\mathbf{m} = (\mathbf{m}_{\text{root}}, \mathbf{m}_{\text{body}})$
* Symbols: $\mathbf{m}$ (motion vector), $\mathbf{m}_{\text{root}}$ (root motion vector), $\mathbf{m}_{\text{body}}$ (body motion vector)
* Why it matters: This equation defines the hybrid motion representation, where $\mathbf{m}$ is a vector containing both root and body motion vectors.

### Equation 2: $\mathbf{m}_{\text{root}} = (\mathbf{p}, \cos{\psi}, \sin{\psi}) \in \mathbb{R}^{5}$

* Equation: $\mathbf{m}_{\text{root}} = (\mathbf{p}, \cos{\psi}, \sin{\psi})$
* Symbols: $\mathbf{m}_{\text{root}}$ (root motion vector), $\mathbf{p}$ (position vector), $\psi$ (orientation angle)
* Why it matters: This equation defines the root motion vector, which includes position and orientation information.

### Equation 3: $\mathbf{p} \in \mathbb{R}^{3}$

* Equation: $\mathbf{p} \in \mathbb{R}^{3}$
* Symbols: $\mathbf{p}$ (position vector)
* Why it matters: This equation defines the position vector, which is a 3D vector.

### Equation 4: $\psi \in (-\pi, \pi]$

* Equation: $\psi \in (-\pi, \pi]$
* Symbols: $\psi$ (orientation angle)
* Why it matters: This equation defines the range of the orientation angle, which is used to represent the orientation of the root motion vector.

### Equation 5: $\boldsymbol{\theta} \in \mathbb{R}^{6j}$

* Equation: $\boldsymbol{\theta} \in \mathbb{R}^{6j}$
* Symbols: $\boldsymbol{\theta}$ (body motion vector)
* Why it matters: This equation defines the body motion vector, which is a 6j-dimensional vector.

**Method Summary**
================

Here's a summary of the ARDY method in 5 bullets:

* ARDY is a streaming generation framework that combines autoregressive diffusion with a hybrid representation to generate high-fidelity human motions.
* The hybrid representation decouples root motion from body motion, using explicit root features and a compact latent body embedding.
* The autoregressive two-stage motion diffusion model learns to denoise hybrid motion tokens containing latent body motion and explicit root motion.
* The model is conditioned on flexible, long-horizon kinematic constraints and text prompts, allowing for controllable generation of high-quality motions.
* The ARDY framework is evaluated on the HumanML3D benchmark and the large-scale Bones Rigplay dataset, demonstrating high motion quality and constraint adherence.

**Experimental Overview**
=====================

Here's an overview of the experimental setup:

* **Tasks/Datasets**: The ARDY framework is evaluated on the HumanML3D benchmark and the large-scale Bones Rigplay dataset.
* **Baselines/Comparisons**: The ARDY framework is compared to an autoregressive baseline that uses explicit pose features.
* **Main Claimed Findings**: The ARDY framework achieves high motion quality and constraint adherence, outperforming the autoregressive baseline.

**What to Verify in the PDF**
==========================

Here are 4 bullets on details that still need to be verified in the PDF:

* The implementation details of the hybrid motion representation and the autoregressive two-stage motion diffusion model.
* The evaluation metrics used to assess motion quality and constraint adherence.
* The experimental setup, including the hyperparameter tuning and the evaluation protocol.
* The results of the ablation study, including the comparison between the hybrid motion representation and the explicit motion representation.
{% endraw %}

{% raw %}
## 4) Super Weights in LLMs and the Failure of Selective Training
- **Authors:** Shreyas Subramanian, Adewale Akinfaderin, Akarsha Sehwag
- **arXiv:** [2607.08733](https://arxiv.org/abs/2607.08733v1) · [pdf](https://arxiv.org/pdf/2607.08733v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.08733v1))
- **Categories:** cs.LG

### Abstract
> Recent work identified Super Weights, individual parameters whose removal degrades model performance by orders of magnitude. We show that this degradation due to pruning Super Weights does not universally apply to all LLMs. Furthermore, if these parameters are so important, Super Weight-aware training should be effective. We show the opposite. Training Super Weights in isolation (100 to 8,192 parameters) drops accuracy to random-guessing levels on both OLMo-1B and OLMo-7B, and expanding to local neighborhoods of up to 36K parameters provides no improvement. The failure is specific to Super Weight coordinates: training an equal number of randomly chosen positions in the same down_proj layers instead improves over the baseline, so the collapse comes from targeting Super Weights, not from sparsity itself. Vanilla LoRA, updating every position in attention weight matrices through low-rank structure, succeeds with only 0.16% of parameters, and applying the same low-rank update to down_proj succeeds as well. A 10-seed ablation confirms that constraining LoRA updates at positions corresponding to Super Weight coordinates yields statistically indistinguishable results. These findings establish that parameter importance does not imply parameter trainability in isolation, and that effective fine-tuning relies on structured decompositions over entire layers rather than targeting individually important weights.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: ΔW
ΔW = BA
Symbols: ΔW (weight change), B (matrix), A (matrix)
Why it matters: This equation represents the full update of the weights in the LoRA method.

### Equation 2: p > 0.05
Symbols: p (probability), 0.05 (threshold)
Why it matters: This equation is used to determine the significance of the weight change, with a threshold of 0.05 indicating statistical significance.

### Equation 3: ΔW = BA
Symbols: ΔW (weight change), B (matrix), A (matrix)
Why it matters: This equation is equivalent to Equation 1 and represents the full update of the weights in the LoRA method.

### Equation 4: 10^(-4)
Symbols: 10^(-4) (learning rate)
Why it matters: This equation represents the learning rate used in the AdamW optimizer.

### Equation 5: α = 16
Symbols: α (parameter scaling factor), 16 (value)
Why it matters: This equation represents the parameter scaling factor used in the LoRA method.

**Method Summary**
================

* The authors investigate the effect of pruning Super Weights on the performance of large language models (LLMs).
* They propose a method called LoRA (Low-Rank Adaptation) that updates the weights of the attention layers using a low-rank structure.
* The authors also propose a method called direct SW training that trains the model on the Super Weight coordinates.
* The authors compare the performance of these methods with a baseline method that trains the model on all weights.

**Experimental Overview**
=====================

* Tasks: The authors evaluate the performance of the proposed methods on two datasets: ARC-Easy and Winogrande.
* Datasets: ARC-Easy (4-choice questions) and Winogrande (9,248 train, 1,267 test).
* Baselines: The authors use a baseline method that trains the model on all weights.
* Main claimed findings: The authors claim that the LoRA method outperforms the baseline method, while the direct SW training method fails to improve performance.

**What to Verify in the PDF**
==========================

* The authors claim that the Super Weight phenomenon is specific to down_proj layers, but it is not clear why this is the case.
* The authors propose a method called LoRA that updates the weights of the attention layers using a low-rank structure, but it is not clear why this method is effective.
* The authors use a threshold of 0.05 to determine the significance of the weight change, but it is not clear why this threshold was chosen.
{% endraw %}

{% raw %}
## 5) Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference
- **Authors:** Chuning Zhu, Eva Xu, Jose Barreiros, Krishnan Srinivasan, Paarth Shah, Abhishek Gupta
- **arXiv:** [2607.08724](https://arxiv.org/abs/2607.08724v1) · [pdf](https://arxiv.org/pdf/2607.08724v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.08724v1))
- **Categories:** cs.LG, cs.RO

### Abstract
> Human decision-making is highly flexible -- some actions are taken immediately; others require longer deliberation. Language models have exhibited a similar capacity for adaptive "reasoning." However, transferring this capability to continuous control policies has been challenging, as directly reasoning in language space may lack the granularity for spatial understanding and precise motions. In this work, we show that reasoning for control policies can emerge by organizing information in an autoregressive latent space reminiscent of a memory palace, where retrieval is iterative and adaptive. Our method, Latent Memory Palace (LMP), formulates reasoning as variational inference with an autoregressive latent distribution. We derive a latent-space reinforcement learning technique to tractably optimize its variational lower bound. The resulting policy, LMP-$π$, achieves strong empirical performance in simulation and real-world domains while exhibiting interpretable, adaptive allocation of test-time compute. We further show that the same framework yields a variable-length action tokenizer, LMP-$\texttt{tok}$, which significantly improves the performance of downstream autoregressive policies. Together, these results present a new perspective on latent reasoning for control through the lens of variational inference.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1. Formula Walkthrough**
### Equation 1: π_{\theta}:\mathcal{O}\rightarrow\mathcal{A}
- Equation: π_{\theta}:\mathcal{O}\rightarrow\mathcal{A}
- Symbols: π_{\theta} (π_{\theta}) - policy, θ (θ) - parameters
- Why it matters: This equation represents the policy learned by the model, which maps observations to actions.

### Equation 2: \mathcal{D}=\{(o_{i},a_{i})\}_{i=1}^{n}
- Equation: \mathcal{D}=\{(o_{i},a_{i})\}_{i=1}^{n}
- Symbols: \mathcal{D} (D) - dataset, o_{i} (o_i) - observations, a_{i} (a_i) - actions
- Why it matters: This equation represents the dataset used to train the model, consisting of observation-action pairs.

### Equation 3: o_{i}
- Equation: o_{i}
- Symbols: o_{i} (o_i) - observation
- Why it matters: This equation represents a single observation in the dataset.

### Equation 4: a_{i}
- Equation: a_{i}
- Symbols: a_{i} (a_i) - action
- Why it matters: This equation represents a single action in the dataset.

### Equation 5: J(\theta)=\mathbb{E}_{(o_{i},a_{i})\sim\mathcal{D}}\left[\log p_{\theta}(a_{i}|o_{i})\right]
- Equation: J(\theta)=\mathbb{E}_{(o_{i},a_{i})\sim\mathcal{D}}\left[\log p_{\theta}(a_{i}|o_{i})\right]
- Symbols: J(\theta) (J(\theta)) - loss function, \mathbb{E} (E) - expectation, p_{\theta}(a_{i}|o_{i}) (p_{\theta}(a_i|o_i)) - probability
- Why it matters: This equation represents the expected log-likelihood of the model's action probabilities given observations, used to train the model.

**2. Method Summary**
- The Latent Memory Palace (LMP) method uses autoregressive variational inference to organize information in a latent space, allowing for iterative and adaptive reasoning.
- The method formulates reasoning as variational inference with an autoregressive latent distribution.
- LMP uses a latent-space reinforcement learning technique to tractably optimize its variational lower bound.

**3. Experimental Overview**
- The experiments evaluate LMP on real-world and simulated visuomotor control benchmarks, including DROID, LIBERO, D3IL, and RoboMimic.
- The experiments compare LMP to non-iterative baselines, including VAE Policy and VQ-BeT.
- The main claimed findings include:
  - LMP achieves strong empirical performance in simulation and real-world domains.
  - LMP demonstrates adaptive allocation of test-time compute.
  - LMP- tok achieves significantly higher success rates than baselines in downstream autoregressive policies.

**4. What to Verify in the PDF**
- The role of uniform-interpolated regularization in mitigating posterior collapse.
- The effect of iterative computation on performance compared to non-iterative baselines.
- The impact of environment stochasticity on the model's behavior.
{% endraw %}
