---
layout: post
title: "Daily arXiv Digest — 2026-07-08 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) EntroPath: Maximum Entropy Path Ensemble Embedding for Manifold Learning
- **Authors:** Przemysław Rola
- **arXiv:** [2607.06497](https://arxiv.org/abs/2607.06497v1) · [pdf](https://arxiv.org/pdf/2607.06497v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.06497v1))
- **Categories:** cs.LG, q-bio.QM, stat.ML

### Abstract
> We introduce EntroPath, a manifold learning method that recovers geodesic geometry from data graphs through ensembles of diffusion paths. Many existing graph-based embeddings rely either on locally normalised random walks or on shortest-path distances. The former can concentrate diffusion in densely sampled regions, while the latter are sensitive to spurious shortcut edges in the graph. EntroPath instead builds its dissimilarities from the maximum entropy random walk (MERW), which aggregates the full ensemble of k-step paths between points rather than relying on any single trajectory. We show that the resulting free-energy dissimilarity converges to squared geodesic distance in the short-time limit, via Varadhan's heat-kernel formula. The diffusion depth k interpolates smoothly between local neighbourhood structure and global manifold geometry, and the symmetrised kernel admits an exact Gram factorisation connecting EntroPath to kernel methods. We further provide scalable extensions via landmark projection and diffusion-potential pseudotime. Across synthetic manifolds and single-cell benchmarks, EntroPath consistently matches or outperforms diffusion- and shortest-path-based methods, while remaining competitive with neighbourhood-preserving embeddings (UMAP, t-SNE) on local-structure metrics. Its gains are most pronounced on manifolds with non-uniform sampling density and well-separated branching trajectories, where path-ensemble diffusion more faithfully preserves the underlying geodesic geometry.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: Affinity Matrix Definition

\[ A_{ij} = \exp\left(-\frac{(d_i - d_j)^2}{2\sigma_i^2}\right) \]

*   Symbols: \( A_{ij} \) (affinity matrix), \( d_i \) and \( d_j \) (node distances), \( \sigma_i \) (bandwidth)
*   Why it matters: This equation defines the affinity matrix used in the adaptive-bandwidth Gaussian kernel.

### Equation 2: Combinatorial Graph Laplacian

\[ L = D - A \]

*   Symbols: \( L \) (combinatorial graph Laplacian), \( D \) (degree matrix), \( A \) (affinity matrix)
*   Why it matters: This equation is used to compute the combinatorial graph Laplacian, which is a key component in the method.

### Equation 3: Diffusion Map Embedding

\[ Y = \sum_{m=1}^n \lambda_m \phi^{(m)} \]

*   Symbols: \( Y \) (embedding), \( \lambda_m \) (eigenvalues), \( \phi^{(m)} \) (eigenvectors)
*   Why it matters: This equation defines the embedding of the data points using the diffusion map.

### Equation 4: Free-Energy Dissimilarity

\[ D_{\text{free}} = -\log \mathbb{E}_{x \sim p(x)} \left[ e^{-\sum_{i=1}^n \lambda_i H(x_i)} \right] \]

*   Symbols: \( D_{\text{free}} \) (free-energy dissimilarity), \( \lambda_i \) (eigenvalues), \( H(x_i) \) (Schrödinger operator)
*   Why it matters: This equation defines the free-energy dissimilarity used in the method.

### Equation 5: Geodesic Distance

\[ d(x, y) = \sqrt{\sum_{i=1}^n \lambda_i (x_i - y_i)^2} \]

*   Symbols: \( d(x, y) \) (geodesic distance), \( \lambda_i \) (eigenvalues), \( x_i \) and \( y_i \) (node coordinates)
*   Why it matters: This equation defines the geodesic distance between two points on the manifold.

**Method Summary**
==================

*   **EntroPath**: A manifold learning method that recovers geodesic geometry from data graphs through ensembles of diffusion paths.
*   **Maximum Entropy Path Ensemble Embedding**: EntroPath uses the maximum entropy random walk (MERW) to build dissimilarities from the ensemble of k-step paths between points.
*   **Schrödinger Heat Kernel**: EntroPath uses the Schrödinger heat kernel to define the dissimilarity between points.
*   **Diffusion Map Embedding**: EntroPath uses the diffusion map to embed the data points in a lower-dimensional space.

**Experimental Overview**
=========================

*   **Tasks/Datasets**: EntroPath is evaluated on synthetic manifolds with known geometry and on biological single-cell datasets.
*   **Baselines/Comparisons**: EntroPath is compared to diffusion-based methods (PHATE, HeatGeo, DTNE), geodesic and shortest-path methods (Isomap, Landmark Isomap), and neighbourhood-preserving embeddings (UMAP, t-SNE).
*   **Main Claimed Findings**: EntroPath consistently matches or outperforms diffusion- and shortest-path-based methods, while remaining competitive with neighbourhood-preserving embeddings on local-structure metrics.

**What to Verify in the PDF**
=============================

*   **Theoretical Derivation**: Verify the theoretical derivation of the free-energy dissimilarity and its relationship to the geodesic distance.
*   **Scalability**: Verify the scalability of EntroPath on large datasets and its ability to handle high-dimensional data.
*   **Robustness**: Verify the robustness of EntroPath to noise and outliers in the data.
*   **Comparison to Other Methods**: Verify the comparison of EntroPath to other manifold learning methods and its performance on different datasets.
{% endraw %}

{% raw %}
## 2) Graph Convolutional Attention: A Spectral Perspective on Graph Denoising and Diffusion
- **Authors:** Shervin Khalafi, Igor Krawczuk, Sergio Rozada, Charilaos Kanatsoulis, Antonio G Marques, Alejandro Ribeiro
- **arXiv:** [2607.06546](https://arxiv.org/abs/2607.06546v1) · [pdf](https://arxiv.org/pdf/2607.06546v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.06546v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Denoising graphs is a fundamental problem in graph learning and the core operation of graph diffusion models. Attention-based architectures like graph transformers have recently shown promise in denoising graphs. However, our principled understanding of attention-based graph denoising remains limited, making it unclear whether standard attention is the right mechanism for this task. Here we show that, under a denoising objective, linear attention is suboptimal and can only learn an average spectral denoising filter over the training distribution. This creates a fundamental limitation as graphs often vary spectrally across the distribution. To overcome this limitation, we introduce Spectral Attention, which directly utilizes the input graph spectrum and provably outperforms linear attention by a margin governed by the spectral diversity of the distribution. We then derive Graph Convolutional Attention (GCA), a practical and permutation-equivariant realization of this idea that implements spectral denoising through graph-filtered queries and keys. For stochastic block models, GCA provably matches the idealized Spectral Attention mechanism. We further show that the softmax operation, that follows the attention, provides additional denoising by approximately projecting noisy eigenvectors onto the clean eigenspace. Empirically, replacing linear attention with GCA consistently improves graph denoising and diffusion on synthetic and real datasets, with gains strongly correlated with spectral diversity. In DiGress, GCA matches standard graph-transformer performance without computing expensive structural features, and when combined with the recently proposed PEARL positional encodings, avoids explicit eigendecomposition computations resulting in faster inference without degrading quality. The code can be found here: github.com/shervinkhalafi/graph_conv_att
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1. Formula Walkthrough**
### Equation 1: $\mathcal{G}$

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: $\mathcal{D}_{\mathcal{G}}$

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 3: $A \in \mathbb{R}^{n \times n}$

* Equation: $A$ is a matrix.
* Symbols: $A$, $n$, $\mathbb{R}$.
* Why it matters: $A$ is the adjacency matrix of the graph.

### Equation 4: $\widetilde{A} = A + \mathcal{E}$

* Equation: $\widetilde{A}$ is the noisy adjacency matrix.
* Symbols: $\widetilde{A}$, $A$, $\mathcal{E}$.
* Why it matters: $\widetilde{A}$ represents the noisy graph.

### Equation 5: $\mathcal{E} \in \mathbb{R}^{n \times n}$

* Equation: $\mathcal{E}$ is a noise matrix.
* Symbols: $\mathcal{E}$, $n$, $\mathbb{R}$.
* Why it matters: $\mathcal{E}$ represents the noise added to the graph.

### Equation 6: $A = U \Lambda U^{\top}$

* Equation: $A$ is diagonalized.
* Symbols: $A$, $U$, $\Lambda$, $U^{\top}$.
* Why it matters: $A$ is diagonalized to simplify the eigendecomposition.

### Equation 7: $\widetilde{A} = \widetilde{U} \widetilde{\Lambda} \widetilde{U}^{\top}$

* Equation: $\widetilde{A}$ is diagonalized.
* Symbols: $\widetilde{A}$, $\widetilde{U}$, $\widetilde{\Lambda}$, $\widetilde{U}^{\top}$.
* Why it matters: $\widetilde{A}$ is diagonalized to simplify the eigendecomposition of the noisy graph.

**2. Method Summary**
* The authors propose a new attention mechanism, Spectral Attention, which directly utilizes the input graph spectrum.
* Spectral Attention is more robust than linear attention and can learn an average spectral denoising filter over the training distribution.
* The authors also propose Graph Convolutional Attention (GCA), a practical and permutation-equivariant realization of Spectral Attention.
* GCA implements spectral denoising through graph-filtered queries and keys.
* The authors show that GCA provably matches the idealized Spectral Attention mechanism for stochastic block models.

**3. Experimental Overview**
* Tasks/Datasets: The authors evaluate their method on synthetic and real datasets.
* Baselines/Comparisons: The authors compare their method to a standard graph transformer (GT) and a variant of GT with graph convolutional attention.
* Main Claimed Findings: The authors show that replacing linear attention with GCA improves graph denoising performance, with gains strongly correlated with spectral diversity.

**4. What to Verify in the PDF**
* The authors use a KNN approach to estimate spectral diversity, but the details of this approach are not provided in the extracted context.
* The authors also mention that the softmax operation provides additional denoising by approximately projecting noisy eigenvectors onto the clean eigenspace, but the mathematical details of this are not provided.
* The authors mention that their method avoids explicit eigendecomposition computations, but the details of how this is achieved are not provided.
{% endraw %}

{% raw %}
## 3) GraphBU: MILP Instance Generation with Graph-Native Block Units
- **Authors:** Xiaolei Guo, Chenyu Zhou, Jianghao Lin, Dongdong Ge
- **arXiv:** [2607.06532](https://arxiv.org/abs/2607.06532v1) · [pdf](https://arxiv.org/pdf/2607.06532v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.06532v1))
- **Categories:** cs.LG, math.OC

### Abstract
> Mixed-integer linear programming (MILP) instances used for solver development are hard to obtain when models come from private or application-specific pipelines. A generator must keep the structure that solvers and learned policies rely on. Existing general generators usually choose their generation unit from a formulation template, summary statistics, local graph edits, or blocks found after recombination. These units do not explicitly record how a local part of the MILP is coupled to the rest of the instance. We propose GraphBU, a graph-native generator whose basic unit is a local subproblem plus its interface. The method promotes coupling nodes into master constraints or boundary variables and uses the resulting block units for compatibility-checked replacement. The analysis focuses on the properties needed by this construction: promotion separates interfaces, replacement can preserve feasibility under an interface-slack condition, and the graph construction is invariant to row-column permutations. On MILP instances generation, this unit keeps graph statistics close to the source family, preserves feasibility on most datasets, and improves downstream Predict-and-Search training. Genrated by GraphBU, The average graph-statistical similarity was approximately 0.934, the average feasibility was approximately 96.7%, and the average increase in the main index of downstream PS was approximately 8.0%.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: Minimization Objective
```markdown
\displaystyle\min_{x}
```
* Symbols: `x` represents the variables to be optimized.
* Why it matters: This equation represents the minimization objective of the Mixed-Integer Linear Programming (MILP) instance.

### Equation 2: Objective Function
```markdown
c^{\top}x
```
* Symbols: `c` represents the coefficients of the objective function, and `x` represents the variables to be optimized.
* Why it matters: This equation represents the objective function of the MILP instance, which is to be minimized.

### Equation 3: Constraints
```markdown
\mathrm{s.t.}
```
* Symbols: `s.t.` is a notation for "subject to" constraints.
* Why it matters: This equation represents the constraints of the MILP instance, which are used to define the feasible region.

### Equation 4: Constraint Enforcement
```markdown
a_{i}^{\top}x\ \bowtie_{i}\ b_{i},\quad i=1,\ldots,m,
```
* Symbols: `a_i` represents the coefficients of the constraints, `x` represents the variables to be optimized, `b_i` represents the right-hand side values, and `\bowtie_i` represents the constraint operator (e.g., `≤`, `=`, `≥`).
* Why it matters: This equation represents the enforcement of the constraints in the MILP instance, where `a_i^{\top}x` represents the linear combination of the coefficients and `b_i` represents the right-hand side value.

### Equation 5: Variable Bounds
```markdown
l\leq x\leq u,\quad x_{j}\in\mathbb{Z}\ \forall j\in I,
```
* Symbols: `l` and `u` represent the lower and upper bounds of the variables, respectively, and `x_j` represents the `j`-th variable.
* Why it matters: This equation represents the bounds of the variables in the MILP instance, where `x_j` is restricted to integer values.

**Method Summary**
================

* **GraphBU Generation**: GraphBU generates MILP instances by decomposing the bipartite graph into local modules and coupling interfaces.
* **Coupling Nodes**: GraphBU identifies coupling nodes in the bipartite graph and decomposes the remaining graph into local modules.
* **Interface Slices**: Each residual component is stored with the interface slices that touch it.
* **Constrained Replacement**: Generation is a constrained replacement step, where a target block unit can be replaced only by a source unit with the same local shape, interface dimensions, and metadata signature.

**Experimental Overview**
=====================

* **Tasks**: GraphBU is evaluated on four MILP families: combinatorial auctions (CA), capacitated facility location (FA), item placement (IP), and workload appointment (WA).
* **Datasets**: The experiments use four MILP families, with original scales reported in Appendix Table 6.
* **Baselines/Comparisons**: The experiments compare GraphBU with existing general generators.
* **Main Claimed Findings**: GraphBU improves downstream Predict-and-Search training, with average graph-statistical similarity of approximately 0.934, average feasibility of approximately 96.7%, and average increase in the main index of downstream PS of approximately 8.0%.

**What to Verify in the PDF**
==========================

* **Detailed Generation Process**: Verify the detailed generation process of GraphBU, including the decomposition of the bipartite graph and the construction of the weighted bipartite graph.
* **Feasibility Preservation**: Verify that GraphBU preserves feasibility under an interface-slack condition.
* **Graph Statistics**: Verify that GraphBU maintains graph statistics close to the source family.
* **Experimental Results**: Verify the experimental results, including the average graph-statistical similarity, average feasibility, and average increase in the main index of downstream PS.
{% endraw %}

{% raw %}
## 4) The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology
- **Authors:** Ghassen Marrakchi, Basarab Matei
- **arXiv:** [2607.06531](https://arxiv.org/abs/2607.06531v1) · [pdf](https://arxiv.org/pdf/2607.06531v1)
- **LLM context source:** abstract only
- **Categories:** cs.AI, cs.LG

### Abstract
> - Objective: Multimodal deep learning models in oncology are currently limited by monolithic designs that rigidly couple data ingestion, clinical routing, and artificial intelligence (AI) inference. To address this inflexibility, we propose the Large Cancer Assistant (LCA), a model-agnostic, post-hoc orchestration framework designed for scalable clinical decision support. - Methods: The LCA is mathematically formalized as a 7-tuple architecture grounded in the principle of Algorithmic Impermeability, ensuring the orchestration logic remains strictly independent of underlying black-box AI models. We introduce the Entry Theory, leveraging Geometric Deep Learning (GDL) to standardize multimodal patient data along distinct structural and medical axes. The system dynamically orchestrates data via a Cancer Switching Module and intentionally isolates the core AI execution from volatile hospital IT infrastructures by outputting a Standardized Intermediate Payload (SIP). - Results: A Proof of Concept (PoC) validated the orchestration logic across four technical scenarios. The framework executed a nominal flow with negligible orchestration overhead. It empirically demonstrated algorithmic impermeability by maintaining an invariant routing projection during AI model swaps, and it validated strict failure-safety by achieving a 100\% recall rate in generating targeted Supplementary Data Requests (SDR) under injected data anomalies. Multi-protocol execution capability was also successfully verified. - Conclusion: By structurally decoupling multimodal ingestion from feature inference, the LCA provides a highly adaptable and modular orchestration foundation. The SIP establishes a clear architectural boundary, natively setting the stage for downstream Electronic Medical Record (EMR) interoperability as an independent future paradigm.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
#### 1. Entry Theory
Not found in extracted context.

#### 2. Cancer Switching Module
Not found in extracted context.

#### 3. Standardized Intermediate Payload (SIP)
Not found in extracted context.

#### 4. Geometric Deep Learning (GDL)
Not found in extracted context.

#### 5. Algorithmic Impermeability
Not found in extracted context.

### Method Summary
* The LCA is a 7-tuple architecture grounded in Algorithmic Impermeability.
* It uses the Entry Theory, which leverages Geometric Deep Learning (GDL) to standardize multimodal patient data.
* The system dynamically orchestrates data via a Cancer Switching Module.
* The core AI execution is isolated from volatile hospital IT infrastructures by outputting a Standardized Intermediate Payload (SIP).

### Experimental Overview
* Tasks/Datasets: Not found in extracted context.
* Baselines/Comparisons: Not found in extracted context.
* Main Claimed Findings:
  * The LCA executed a nominal flow with negligible orchestration overhead.
  * The framework demonstrated algorithmic impermeability by maintaining an invariant routing projection during AI model swaps.
  * It achieved a 100% recall rate in generating targeted Supplementary Data Requests (SDR) under injected data anomalies.
  * The framework successfully verified multi-protocol execution capability.

### What to Verify in the PDF
* Details about the tasks/datasets used in the experiments.
* The comparison with existing baselines or state-of-the-art methods.
* The implementation of the Geometric Deep Learning (GDL) in the Entry Theory.
* The specific architecture of the Cancer Switching Module.
{% endraw %}

{% raw %}
## 5) What Images Cannot Say: Language-Guided Olfactory Representation Learning
- **Authors:** Eleftherios Tsonis, Xi Wang, Vicky Kalogeiton
- **arXiv:** [2607.06402](https://arxiv.org/abs/2607.06402v1) · [pdf](https://arxiv.org/pdf/2607.06402v1)
- **LLM context source:** abstract only
- **Categories:** cs.CV, cs.AI, cs.LG

### Abstract
> Images tell us what a scene looks like, but rarely what it would feel like to be there. While recent datasets pair visual scenes with electronic-nose measurements, aligning smell signals with images remains challenging because many olfactory cues arise from contextual environmental factors that are not directly visible in pixels. We introduce SCENT, a multimodal framework that uses language guidance as a semantic bridge between vision and olfaction. Our approach leverages Vision-Language Models (VLMs) to generate scene descriptors capturing objects, environmental context, and plausible ambient smell cues suggested by the visual scene. These descriptors provide semantic guidance for learning olfactory representations. We train a smell encoder that maps electronic-nose signals into a shared embedding space aligned with both visual and textual representations, and introduce a languageguided latent decomposition that separates object-specific odors from contextual environmental contributions. Experiments on the New York Smells dataset demonstrate that SCENT significantly improves crossmodal retrieval compared to vision-only baselines, achieving state-of-theart performance on smell-to-image and smell-to-text retrieval tasks. In addition, our framework produces interpretable olfactory representations that enable the disentanglement of complex smell mixtures. Our results reveal the importance of contextual semantic information for grounding olfactory perception in multimodal learning and pave the way for future research in this area.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
Unfortunately, no specific equations are mentioned in the extracted context.

### Method Summary
* The authors introduce SCENT, a multimodal framework that uses language guidance to align vision and olfaction.
* The framework leverages Vision-Language Models (VLMs) to generate scene descriptors capturing objects, environmental context, and plausible ambient smell cues.
* A smell encoder is trained to map electronic-nose signals into a shared embedding space aligned with both visual and textual representations.
* A language-guided latent decomposition separates object-specific odors from contextual environmental contributions.

### Experimental Overview
* Tasks/Datasets: smell-to-image and smell-to-text retrieval tasks on the New York Smells dataset.
* Baselines/Comparisons: vision-only baselines.
* Main Claimed Findings: SCENT significantly improves crossmodal retrieval and achieves state-of-the-art performance on smell-to-image and smell-to-text retrieval tasks.

### What to Verify in the PDF
* The exact formulation of the scene descriptors generated by Vision-Language Models (VLMs).
* The architecture and training procedure of the smell encoder and language-guided latent decomposition.
* The evaluation metrics used to measure the performance of SCENT on the New York Smells dataset.
{% endraw %}
