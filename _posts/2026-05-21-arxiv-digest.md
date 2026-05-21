---
layout: post
title: "Daily arXiv Digest — 2026-05-21 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) EvoStruct: Bridging Evolutionary and Structural Priors for Antibody CDR Design via Protein Language Model Adaptation
- **Authors:** Mansoor Ahmed, Sujin Lee, Umar Khayaz, Murray Patterson
- **arXiv:** [2605.21485](https://arxiv.org/abs/2605.21485v1) · [pdf](https://arxiv.org/pdf/2605.21485v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.21485v1))
- **Categories:** cs.LG

### Abstract
> Equivariant graph neural network (GNN) methods for antibody complementarity-determining region (CDR) design achieve the highest sequence recovery but suffer from severe vocabulary collapse. The current best GNN methods over-predict very few amino acids, such as tyrosine and glycine, while ignoring functionally important residues. We trace this failure to GNN encoders learning amino acid distributions de novo from limited structural data, discarding substitution patterns encoded in evolutionary databases. To resolve this, we propose EvoStruct, which bridges a frozen protein language model (PLM) with 3D structural context from an E(3)-equivariant GNN via a cross-attention adapter. Unlike prior PLM-structure adapters for general protein design, EvoStruct targets the vocabulary collapse problem specific to CDR design through progressive PLM unfreezing and R-Drop consistency regularization. On the CHIMERA-Bench dataset, EvoStruct achieves the highest amino acid recovery and lowest perplexity among several antibody design methods, improving sequence recovery by 16% and reducing perplexity by 43% relative to the best GNN baselines, while recovering 2.3x greater amino acid diversity and the highest binding-pair correlation with ground truth.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Effective Vocabulary Calculation

\[ V_{\text{eff}} = \exp\!\left(-\sum_{a}p(a)\log p(a)\right) \]

* Equation: Effective vocabulary calculation
* Symbols:
	+ \( V_{\text{eff}} \): Effective vocabulary
	+ \( p(a) \): Predicted amino acid distribution
	+ \( a \): Amino acid
* Why it matters: This equation calculates the effective vocabulary, which is used to evaluate the diversity of predicted amino acids. A higher effective vocabulary indicates more diverse predictions.

### Equation 2: Not Found in Extracted Context

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 3: Not Found in Extracted Context

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 4: Not Found in Extracted Context

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 5: Not Found in Extracted Context

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

**Method Summary**
==================

* EvoStruct bridges evolutionary and structural priors for antibody CDR design via protein language model adaptation.
* The method uses a frozen protein language model to produce CDR embeddings that encode evolutionary substitution patterns, and an E(3)-equivariant graph neural network to capture spatial geometry.
* EvoStruct leverages a cross-attention adapter to fuse the outputs of the protein language model and the graph neural network.
* The method achieves the highest amino acid recovery and lowest perplexity among several antibody design methods.

**Experimental Overview**
========================

* Tasks: Antibody CDR design
* Datasets: Chimera-Bench benchmark
* Baselines/comparisons: Eleven CDR-H3 design methods spanning five architectural families
* Main claimed findings: EvoStruct achieves the highest amino acid recovery and lowest perplexity among several antibody design methods, improving sequence recovery by 16% and reducing perplexity by 43% relative to the best GNN baselines.

**What to Verify in the PDF**
=============================

* The implementation details of the E(3)-equivariant graph neural network and the cross-attention adapter.
* The evaluation metrics used to measure the performance of EvoStruct, including the amino acid recovery and perplexity.
* The results of the epitope-group split, which clusters complexes by epitope similarity to test generalization to unseen binding sites.
{% endraw %}

{% raw %}
## 2) Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning
- **Authors:** Benhao Huang, Zhengyang Geng, Zico Kolter
- **arXiv:** [2605.21488](https://arxiv.org/abs/2605.21488v1) · [pdf](https://arxiv.org/pdf/2605.21488v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.21488v1))
- **Categories:** cs.LG

### Abstract
> Scaling test-time compute by iteratively updating a latent state has emerged as a powerful paradigm for reasoning. Yet the internal mechanisms that enable these iterative models to generalize beyond memorized patterns remain unclear. We hypothesize that generalizable reasoning arises from learning task-conditioned attractors: latent dynamical systems whose stable fixed points correspond to valid solutions. We formalize this process through Equilibrium Reasoners (EqR), which enable test-time scaling without external verifiers or task-specific priors. EqR scales internal dynamics along two axes: depth, by running more iterations, and breadth, by aggregating stochastic trajectories from multiple initializations. Empirically, gains from test-time scaling are tightly coupled with stronger convergence toward solution-aligned attractors. This attractor perspective allows neural networks to adaptively allocate test-time compute based on task difficulty. While simple cases converge within 1 to 5 iteration steps, harder cases benefit from massive test-time scaling. By unrolling up to the equivalent of 40,000 layers, scalable latent reasoning boosts accuracy from 2.6% for feedforward models to over 99% on Sudoku-Extreme. These results suggest that learned attractor landscapes provide a useful mechanistic lens for understanding scalable reasoning in iterative latent models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: \lVert f_{\theta}(\mathbf{z};\mathbf{x})-\mathbf{z}\rVert

* Equation: \lVert f_{\theta}(\mathbf{z};\mathbf{x})-\mathbf{z}\rVert
* Symbols: \lVert \cdot \rVert (norm), f_{\theta} (parameterized update operator), \mathbf{z} (latent state), \mathbf{x} (input)
* Why it matters: This equation measures the distance between the output of the update operator and the latent state, indicating how well the model has converged.

### Equation 2: \mathbf{z}

* Equation: \mathbf{z}
* Symbols: \mathbf{z} (latent state)
* Why it matters: This equation represents the latent state of the model, which is updated iteratively.

### Equation 3: \mathbf{z}^{\star}=f_{\theta}(\mathbf{z}^{\star};\mathbf{x})

* Equation: \mathbf{z}^{\star}=f_{\theta}(\mathbf{z}^{\star};\mathbf{x})
* Symbols: \mathbf{z}^{\star} (stable fixed point), f_{\theta} (parameterized update operator), \mathbf{x} (input)
* Why it matters: This equation shows how the stable fixed point is updated using the parameterized update operator.

### Equation 4: f_{\theta}

* Equation: f_{\theta}
* Symbols: f_{\theta} (parameterized update operator)
* Why it matters: This equation represents the parameterized update operator used to update the latent state.

### Equation 5: r=\lVert f_{\theta}(\mathbf{z};\mathbf{x})-\mathbf{z}\rVert

* Equation: r=\lVert f_{\theta}(\mathbf{z};\mathbf{x})-\mathbf{z}\rVert
* Symbols: r (residual), \lVert \cdot \rVert (norm), f_{\theta} (parameterized update operator), \mathbf{z} (latent state), \mathbf{x} (input)
* Why it matters: This equation measures the residual error between the output of the update operator and the latent state.

**Method Summary**
==================

* The authors study iterative reasoning models that update a latent state iteratively.
* The models use a parameterized update operator to update the latent state.
* The authors focus on weight-tied iterative models with fixed-size latent states.
* The models are compared to feedforward models and hierarchical reasoning models.

**Experimental Overview**
========================

* The authors evaluate the models on two tasks: Sudoku and Maze.
* The tasks are serialized into token sequences, which are used to encode the unsolved puzzle and its solution.
* The authors compare the models to a feedforward baseline and a hierarchical reasoning model.
* The main claimed findings are that the weight-tied iterative models can scale to larger inputs and achieve higher accuracy than the feedforward baseline.

**What to Verify in the PDF**
=============================

* The authors' residual-diagnostic formulation and its interpretation.
* The training-dynamics ablations and their results.
* The experiments on generalization beyond the main setting and seed stability.
{% endraw %}

{% raw %}
## 3) Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate
- **Authors:** Dayal Singh Kalra, Maissam Barkeshli
- **arXiv:** [2605.21486](https://arxiv.org/abs/2605.21486v1) · [pdf](https://arxiv.org/pdf/2605.21486v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.21486v1))
- **Categories:** cs.LG, cond-mat.dis-nn, cs.AI, stat.ML

### Abstract
> Hyperparameter transfer allows extrapolating optimal optimization hyperparameters from small to large scales, making it critical for training large language models (LLMs). This is done either by fitting a scaling law to the hyperparameters or by a judicious choice of parameterization, such as Maximal Update ($μ$P), that renders optimal hyperparameters approximately scale invariant. In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization. Next, we investigate through a comprehensive series of ablations why $μ$P appears to offer high-quality learning rate transfer relative to standard parameterization (SP), as existing theory is inadequate. We find that the overwhelming benefit of $μ$P relative to SP when training with AdamW arises simply from maximizing the learning rate of the embedding layer. In SP, the embedding layer learning rate acts as a bottleneck that induces training instabilities; increasing it by a factor of width to match $μ$P dramatically smooths out training while improving hyperparameter transfer. We also find that weight decay improves the scaling law fits, while, in the fixed token-per-parameter setting, it hurts the robustness of the extrapolation.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: η^{*}

η^{*} = \frac{\sqrt{\lambda}}{\sqrt{1 + \frac{\lambda}{\beta_2}}}

* Symbols: η^{*} (optimal learning rate), λ (weight decay), β_2 (AdamW decay rate)
* Why it matters: This equation represents the optimal learning rate for a neural network with weight decay.

### Equation 2: \mathcal{E}

\mathcal{E} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{\partial L}{\partial \theta_i} \right| \cdot \left| \frac{\partial L}{\partial \theta_i} \right|_{\theta_i = \theta_i^{(t)}} \cdot \left| \frac{\partial L}{\partial \theta_i} \right|_{\theta_i = \theta_i^{(t)}}^{-1}

* Symbols: \mathcal{E} (loss predictability error), n (number of data points), L (loss function), \theta_i (model parameters), \theta_i^{(t)} (model parameters at time t)
* Why it matters: This equation measures the predictability of the loss function with respect to the model parameters.

### Equation 3: \kappa

\kappa = \alpha - 2\beta + \gamma

* Symbols: \kappa (curvature), α (scaling exponent), β (scaling exponent), γ (scaling exponent)
* Why it matters: This equation represents the curvature of the loss landscape with respect to the model parameters.

### Equation 4: \mathcal{R}(\infty)

\mathcal{R}(\infty) = \lim_{n \to \infty} \frac{L^{*}(n)}{L^{*}(\infty)}

* Symbols: \mathcal{R}(\infty) (asymptotic loss penalty), L^{*}(n) (optimal loss at width n), L^{*}(\infty) (optimal loss at infinite width)
* Why it matters: This equation measures the asymptotic loss penalty due to the choice of parameterization.

### Equation 5: \to\mu

\to\mu = \frac{\sqrt{\lambda}}{\sqrt{1 + \frac{\lambda}{\beta_2}}}

* Symbols: \to\mu (optimal learning rate), λ (weight decay), β_2 (AdamW decay rate)
* Why it matters: This equation represents the optimal learning rate for a neural network with weight decay.

**Method Summary**
==================

* The authors develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization.
* The authors investigate the importance of embedding layer learning rate and weight decay in hyperparameter transfer.
* The authors use a comprehensive series of ablations to compare the performance of different parameterizations and widths.

**Experimental Overview**
========================

* The authors pre-train GPT-style Transformers on FineWeb-Edu using a depth of 12 Transformer blocks, a context length of 1024, and a vocabulary size of 50,304.
* The authors scale the embedding dimension (width) from 128 to 2048 and train the models using AdamW with a Warmup-Stable-Decay schedule.
* The authors compare the performance of different parameterizations and widths using a fixed-step setting and a compute-optimal setting.

**What to Verify in the PDF**
=============================

* The authors claim that the embedding layer learning rate is the key factor in achieving high-quality learning rate transfer.
* The authors claim that weight decay improves the scaling law fits but hurts the robustness of the extrapolation.
* The authors provide a detailed analysis of the stability conditions for scaling analysis and the design principles for scaling analysis.
{% endraw %}

{% raw %}
## 4) Velocityformer: Broken-Symmetry-Matched Equivariant Graph Transformers for Cosmological Velocity Reconstruction
- **Authors:** Tilman Tröster, David Mirkovic, Veronika Oehl, Arne Thomsen
- **arXiv:** [2605.21483](https://arxiv.org/abs/2605.21483v1) · [pdf](https://arxiv.org/pdf/2605.21483v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.21483v1))
- **Categories:** astro-ph.CO, cs.LG

### Abstract
> Precise measurement of the kinematic Sunyaev-Zel'dovich (kSZ) effect - a probe of the large-scale distribution of baryonic matter, a key observable for cosmological inference - requires accurate reconstruction of galaxy velocities from spectroscopic surveys. The signal-to-noise ratio (SNR) of kSZ measurements scales directly with the correlation coefficient $r$ between reconstructed and true velocities. We introduce Velocityformer, an equivariant graph transformer architecture designed to match the specific symmetry of the observational data. While the underlying physics is equivariant with respect to translations and rotations, observational effects break this symmetry due to the preferred line-of-sight direction. Matching the model's inductive bias to the data's broken symmetry consistently improves performance across all model sizes and training volumes, with Velocityformer improving $r$ by 35% over the standard linear theory baseline and outperforming ML baselines at every data volume. By matching the model's inductive bias to the data and conditioning on the physics-based long-wavelength solution, Velocityformer is highly data-efficient, training to high accuracy on as few as 4 low-fidelity simulations, and generalises zero-shot across input geometry, cosmological parameters, and galaxy sample. On high-fidelity simulated galaxy catalogues, this yields a 30% improvement in $r$ over the physical baseline, directly translating to the same SNR gain on observational data.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: E(3)
#### Equation
E(3) = ...
#### Symbols
- E(3): Not explicitly defined in the context
- h: Hubble constant
- Mpc: Megaparsec
#### Why it matters
Not found in extracted context.

### Equation 2: ~70h^{-1}Mpc
#### Equation
~70h^{-1}Mpc
#### Symbols
- ~: Notation for a rough estimate
- h: Hubble constant
- Mpc: Megaparsec
#### Why it matters
Not found in extracted context.

### Equation 3: \mathcal{O}(10^{3})
#### Equation
\mathcal{O}(10^{3})
#### Symbols
- \mathcal{O}: Big O notation
- 10^{3}: 10 to the power of 3
#### Why it matters
Not found in extracted context.

### Equation 4: 35%
#### Equation
35%
#### Symbols
- %: Percentage sign
#### Why it matters
Not found in extracted context.

### Equation 5: \gtrsim 30%
#### Equation
\gtrsim 30%
#### Symbols
- \gtrsim: Notation for "greater than or equal to"
- 30%: 30 percent
#### Why it matters
Not found in extracted context.

### Equation 6: 80%
#### Equation
80%
#### Symbols
- %: Percentage sign
#### Why it matters
Not found in extracted context.

**Method Summary**
================

* The velocity reconstruction task can be cast as a point cloud regression problem, where the 3D galaxy positions serve as inputs and the targets are the per-galaxy 3D velocity vectors.
* The regression is conditioned on the long-wavelength velocity field obtained from linear theory.
* The model predicts velocities for all galaxies in a sample, using the per-galaxy linear velocity estimate as a feature vector.

**Experimental Overview**
========================

* Tasks/Datasets:
	+ Quijote N-body simulation suite
	+ Halo catalogues from simulation snapshots at redshift z = 0.5
	+ Galaxy catalogues with a halo-occupation distribution (HOD) model
* Baselines/Comparisons:
	+ Physical baseline
	+ Broken-symmetry Velocityformer
	+ Full-E(3) variant
* Main Claimed Findings:
	+ Velocityformer consistently outperforms all baselines across all model sizes and training-data volumes.
	+ Achieving a comparable gain in SNR through increasing the number of galaxies the kSZ effect is measured on would require a 70–80% larger galaxy catalogue.
{% endraw %}

{% raw %}
## 5) Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning
- **Authors:** Yi Huang, Qingyun Sun, Jia Li, Xingcheng Fu, Jianxin Li
- **arXiv:** [2605.21475](https://arxiv.org/abs/2605.21475v1) · [pdf](https://arxiv.org/pdf/2605.21475v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2605.21475v1))
- **Categories:** cs.LG

### Abstract
> Relational prediction tasks are fundamental in many real-world applications, where data are naturally stored in relational databases (RDBs). Relational Deep Learning (RDL) addresses this problem by modeling RDBs as graphs and applying graph neural networks (GNNs) for end-to-end learning. However, the full-resolution property is commonly adopted as a design principle in graph construction for RDBs to preserve relational semantics, which leads most existing methods to rely on fixed graph structures. In this paper, we propose FROG, a Full-Resolution and Optimizable Graph Structure Learning} framework for RDL that formulates relational structure learning as a learnable table role modeling problem, allowing tables to contribute as nodes and edges in message passing. We further design role-driven message passing mechanisms to capture relational semantics, enabling joint optimization of graph structure and GNN representations. To ensure semantic consistency, we introduce functional dependency constraints that regularize representations across table and entity levels. Extensive experiments demonstrate that our method outperforms existing approaches and reveal how table roles impact downstream tasks, offering new insights into graph construction for RDL
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: review → user1

* Equation: review → user1
* Symbols: review, user1
* Why it matters: This equation represents a functional dependency between the "review" table and the "user1" entity. It indicates that a review is related to a specific user.

### Equation 2: review1 ⊥ user2

* Equation: review1 ⊥ user2
* Symbols: review1, user2
* Why it matters: This equation represents a non-functional dependency between the "review1" table and the "user2" entity. It indicates that a review is not related to a specific user.

### Equation 3: (T, R)

* Equation: (T, R)
* Symbols: T, R
* Why it matters: This equation represents the set of tables and relations in the relational database. It is a formal representation of the database schema.

### Equation 4: (T, R)

* Equation: (T, R)
* Symbols: T, R
* Why it matters: This equation is identical to Equation 3 and represents the set of tables and relations in the relational database.

### Equation 5: T = {T1, ..., Tn}

* Equation: T = {T1, ..., Tn}
* Symbols: T, T1, ..., Tn
* Why it matters: This equation represents the set of tables in the relational database. It is a formal representation of the database schema.

**Method Summary**
==================

* The authors propose FROG, a full-resolution graph structure learning framework for relational deep learning.
* FROG formulates relational structure learning as a learnable table role modeling problem, allowing tables to contribute as nodes and edges in message passing.
* The framework introduces functional dependency constraints to regularize representations across table and entity levels.
* The authors prove that table-as-node and table-as-edge satisfy the full-resolution property under preserved entity and FPK types, features, and directions.

**Experimental Overview**
=========================

* The authors evaluate FROG on Relbench, a benchmark suite consisting of large-scale, real-world relational databases.
* The experiments cover 23 downstream tasks across 6 datasets.
* The authors compare FROG to existing GNN baselines and report strong performance across different tasks and datasets.
* The results indicate that the role assigned to tables has a substantial impact on model performance, and that jointly optimizing graph structures and GNN models enables more expressive modeling.

**What to Verify in the PDF**
=============================

* The authors claim that FROG achieves strong performance across different tasks and datasets. Verify the results in Table 1, 2, and 3, and the complete results in Appendix F.2.
* The authors introduce functional dependency constraints to regularize representations across table and entity levels. Verify the implementation details in Appendix E.
* The authors prove that table-as-node and table-as-edge satisfy the full-resolution property under preserved entity and FPK types, features, and directions. Verify the theoretical analysis in Appendix B.
{% endraw %}
