---
layout: post
title: "Daily arXiv Digest — 2026-04-23 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) FedSIR: Spectral Client Identification and Relabeling for Federated Learning with Noisy Labels
- **Authors:** Sina Gholami, Abdulmoneam Ali, Tania Haghighi, Ahmed Arafa, Minhaj Nur Alam
- **arXiv:** [2604.20825](https://arxiv.org/abs/2604.20825v1) · [pdf](https://arxiv.org/pdf/2604.20825v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.20825v1))
- **Categories:** cs.LG, cs.AI, cs.CV, cs.DC, eess.SP

### Abstract
> Federated learning (FL) enables collaborative model training without sharing raw data; however, the presence of noisy labels across distributed clients can severely degrade the learning performance. In this paper, we propose FedSIR, a multi-stage framework for robust FL under noisy labels. Different from existing approaches that mainly rely on designing noise-tolerant loss functions or exploiting loss dynamics during training, our method leverages the spectral structure of client feature representations to identify and mitigate label noise. Our framework consists of three key components. First, we identify clean and noisy clients by analyzing the spectral consistency of class-wise feature subspaces with minimal communication overhead. Second, clean clients provide spectral references that enable noisy clients to relabel potentially corrupted samples using both dominant class directions and residual subspaces. Third, we employ a noise-aware training strategy that integrates logit-adjusted loss, knowledge distillation, and distance-aware aggregation to further stabilize federated optimization. Extensive experiments on standard FL benchmarks demonstrate that FedSIR consistently outperforms state-of-the-art methods for FL with noisy labels. The code is available at https://github.com/sinagh72/FedSIR.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{C}$

* Equation: $\mathcal{C}$
* Symbols: $\mathcal{C}$ (set of clients)
* Why it matters: This equation represents the set of clients in the federated learning system.

### Equation 2: $|\mathcal{C}|$

* Equation: $|\mathcal{C}|$
* Symbols: $|\mathcal{C}|$ (number of clients)
* Why it matters: This equation gives the number of clients in the system, which is essential for understanding the scale of the federated learning setup.

### Equation 3: $\mathbf{x}$

* Equation: $\mathbf{x}$
* Symbols: $\mathbf{x}$ (feature vector)
* Why it matters: This equation represents the feature vector of a client, which is used to construct the spectral reference model.

### Equation 4: $\|\mathbf{x}\|_{2}$

* Equation: $\|\mathbf{x}\|_{2}$
* Symbols: $\|\mathbf{x}\|_{2}$ (Euclidean norm of $\mathbf{x}$)
* Why it matters: This equation calculates the Euclidean norm of the feature vector $\mathbf{x}$, which is used to measure the magnitude of the vector.

### Equation 5: $\ell_{2}$

* Equation: $\ell_{2}$
* Symbols: $\ell_{2}$ (loss function)
* Why it matters: This equation represents the loss function used in the federated learning system, which is essential for training the model.

**Method Summary**
================

* The proposed method, FedSIR, is a multi-stage framework for robust federated learning with noisy labels.
* The framework consists of three stages: client identification, spectral relabeling, and local updates.
* The method leverages the spectral structure of client feature representations to identify and mitigate label noise.
* The spectral relabeling mechanism is used to correct noisy labels and improve the accuracy of the model.

**Experimental Overview**
=======================

* The proposed method is evaluated on CIFAR-10 and CIFAR-100 datasets under symmetric label noise.
* The experiments are conducted with different levels of noise and heterogeneity in client-level noise.
* The method is compared with standard FL baselines and recent noise-robust FL approaches.
* The results show that the proposed method achieves the best performance across all noise levels and heterogeneity settings.

**What to Verify in the PDF**
==========================

* The implementation details of the spectral relabeling mechanism, including the choice of residual right singular vectors and the number of communication rounds.
* The impact of the number of clean clients on the performance of the proposed method.
* The effect of different loss functions on the performance of the proposed method.
{% endraw %}

{% raw %}
## 2) Closing the Domain Gap in Biomedical Imaging by In-Context Control Samples
- **Authors:** Ana Sanchez-Fernandez, Thomas Pinetz, Werner Zellinger, Günter Klambauer
- **arXiv:** [2604.20824](https://arxiv.org/abs/2604.20824v1) · [pdf](https://arxiv.org/pdf/2604.20824v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.20824v1))
- **Categories:** cs.LG, q-bio.QM

### Abstract
> The central problem in biomedical imaging are batch effects: systematic technical variations unrelated to the biological signal of interest. These batch effects critically undermine experimental reproducibility and are the primary cause of failure of deep learning systems on new experimental batches, preventing their practical use in the real world. Despite years of research, no method has succeeded in closing this performance gap for deep learning models. We propose Control-Stabilized Adaptive Risk Minimization via Batch Normalization (CS-ARM-BN), a meta-learning adaptation method that exploits negative control samples. Such unperturbed reference images are present in every experimental batch by design and serve as stable context for adaptation. We validate our novel method on Mechanism-of-Action (MoA) classification, a crucial task for drug discovery, on the large-scale JUMP-CP dataset. The accuracy of standard ResNets drops from 0.939 $\pm$ 0.005, on the training domain, to 0.862 $\pm$ 0.060 on data from new experimental batches. Foundation models, even after Typical Variation Normalization, fail to close this gap. We are the first to show that meta-learning approaches close the domain gap by achieving 0.935 $\pm$ 0.018. If the new experimental batches exhibit strong domain shifts, such as being generated in a different lab, meta-learning approaches can be stabilized with control samples, which are always available in biomedical experiments. Our work shows that batch effects in bioimaging data can be effectively neutralized through principled in-context adaptation, which also makes them practically usable and efficient.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: 0.939 ± 0.005
```markdown
0.939 ± 0.005
```
* Equation: Not explicitly provided, but likely represents the accuracy of a standard ResNet50 model on the training domain.
* Symbols: `0.939` represents the accuracy, and `± 0.005` represents the standard deviation.
* Why it matters: This equation shows the high accuracy of the standard ResNet50 model on the training domain, indicating that it performs well on the data it was trained on.

### Equation 2: 0.862 ± 0.060
```markdown
0.862 ± 0.060
```
* Equation: Not explicitly provided, but likely represents the accuracy of the standard ResNet50 model on the test domain (new experimental batches).
* Symbols: `0.862` represents the accuracy, and `± 0.060` represents the standard deviation.
* Why it matters: This equation shows that the standard ResNet50 model performs significantly worse on the test domain, highlighting the issue of batch effects.

### Equation 3: 0.935 ± 0.018
```markdown
0.935 ± 0.018
```
* Equation: Not explicitly provided, but likely represents the accuracy of the proposed CS-ARM-BN method on the test domain (new experimental batches).
* Symbols: `0.935` represents the accuracy, and `± 0.018` represents the standard deviation.
* Why it matters: This equation shows that the proposed CS-ARM-BN method outperforms the standard ResNet50 model on the test domain, indicating its effectiveness in addressing batch effects.

### Equation 4: \boldsymbol{c}
```markdown
\boldsymbol{c}
```
* Equation: Not explicitly provided, but likely represents a vector or matrix used in the CS-ARM-BN method.
* Symbols: `\boldsymbol{c}` represents a vector or matrix with unknown elements.
* Why it matters: This equation is not explicitly explained in the context, but it is likely used in the CS-ARM-BN method to represent some aspect of the data or model.

### Equation 5: \mathcal{L}_{\mathrm{CE}}(\bm{y},\hat{\bm{y}})=-\sum_{k=1}^{K}y_{k}\log(\hat{y}_{k})
```markdown
\mathcal{L}_{\mathrm{CE}}(\bm{y},\hat{\bm{y}})=-\sum_{k=1}^{K}y_{k}\log(\hat{y}_{k})
```
* Equation: Cross-entropy loss function.
* Symbols:
	+ `\mathcal{L}_{\mathrm{CE}}` represents the cross-entropy loss function.
	+ `\bm{y}` represents the true labels.
	+ `\hat{\bm{y}}` represents the predicted labels.
	+ `K` represents the number of classes.
* Why it matters: This equation is used to evaluate the performance of the proposed CS-ARM-BN method, as it is a common loss function used in classification tasks.

**Method Summary**
================

* The proposed CS-ARM-BN method uses negative control samples to adapt to new experimental batches.
* The method exploits the fact that control samples are present in every experimental batch and serve as a stable context for adaptation.
* The method is designed to address batch effects in biomedical imaging, which are a major challenge in deep learning-based image classification tasks.

**Experimental Overview**
=====================

* The proposed CS-ARM-BN method is evaluated on the JUMP-CP dataset, which consists of eight well-defined Mechanism-of-Action (MoA) classes.
* The method is compared to standard ResNet50 and Foundation Model CA-MAE baselines.
* The experiments are designed to evaluate the effectiveness of the CS-ARM-BN method in addressing batch effects under different scenarios, including mild domain shift, strong domain shift, and label shift.

**What to Verify in the PDF**
==========================

* The implementation details of the CS-ARM-BN method, including the specific architecture and hyperparameter settings used.
* The evaluation metrics used to assess the performance of the proposed method, including accuracy, precision, recall, and F1-score.
* The results of the experiments, including the accuracy and standard deviation of the proposed method and the baselines under different scenarios.
{% endraw %}

{% raw %}
## 3) Stream-CQSA: Avoiding Out-of-Memory in Attention Computation via Flexible Workload Scheduling
- **Authors:** Yiming Bian, Joshua M. Akey
- **arXiv:** [2604.20819](https://arxiv.org/abs/2604.20819v1) · [pdf](https://arxiv.org/pdf/2604.20819v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.20819v1))
- **Categories:** cs.LG, cs.DC

### Abstract
> The scalability of long-context large language models is fundamentally limited by the quadratic memory cost of exact self-attention, which often leads to out-of-memory (OOM) failures on modern hardware. Existing methods improve memory efficiency to near-linear complexity, while assuming that the full query, key, and value tensors fit in device memory. In this work, we remove this assumption by introducing CQS Divide, an operation derived from cyclic quorum sets (CQS) theory that decomposes attention into a set of independent subsequence computations whose recomposition yields exactly the same result as full-sequence attention. Exploiting this decomposition, we introduce Stream-CQSA, a memory-adaptive scheduling framework that partitions attention into subproblems that fit within arbitrary memory budgets. This recasts attention from a logically monolithic operation into a collection of schedulable tasks, enabling flexible execution across devices without inter-device communication. Experiments demonstrate predictable memory scaling and show that exact attention over billion-token sequences can be executed on a single GPU via streaming, without changing the underlying mathematical definition of attention or introducing approximation error.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `c(c-1)/2`

* Equation: `c(c-1)/2`
* Symbols: `c` (number of chunks)
* Why it matters: This equation represents the number of possible pairs of elements in a sequence of length `c`. It is used in the context of attention computation and is related to the number of attention weights that need to be computed.

### Equation 2: `l(l-1)/2`

* Equation: `l(l-1)/2`
* Symbols: `l` (length of the sequence)
* Why it matters: This equation represents the number of possible pairs of elements in a sequence of length `l`. It is used in the context of attention computation and is related to the number of attention weights that need to be computed.

### Equation 3: `c × (l(l-1)/2) = c(c-1)/2`

* Equation: `c × (l(l-1)/2) = c(c-1)/2`
* Symbols: `c` (number of chunks), `l` (length of the sequence)
* Why it matters: This equation relates the number of attention weights that need to be computed for a sequence of length `l` and a number of chunks `c`. It shows that the number of attention weights is proportional to the number of chunks and the length of the sequence.

### Equation 4: `c = l(l-1) + 1`

* Equation: `c = l(l-1) + 1`
* Symbols: `c` (number of chunks), `l` (length of the sequence)
* Why it matters: This equation relates the number of chunks `c` to the length of the sequence `l`. It shows that the number of chunks is one more than the number of pairs of elements in the sequence.

### Equation 5: `{1, 3, 7, 13, 21, ...}`

* Equation: `{1, 3, 7, 13, 21, ...}`
* Symbols: None
* Why it matters: This equation represents a sequence of numbers that are one more than a power of 2. It is used in the context of attention computation and is related to the divide granularity.

### Equation 6: `{1, 2, 3, 4, 5, ...}`

* Equation: `{1, 2, 3, 4, 5, ...}`
* Symbols: None
* Why it matters: This equation represents a sequence of natural numbers. It is used in the context of attention computation and is related to the length of the sequence.

**Method Summary**
==================

* **Stream-CQSA**: A memory-adaptive scheduling framework that partitions attention into subproblems that fit within arbitrary memory budgets.
* **CQS Divide**: An operation derived from cyclic quorum sets (CQS) theory that decomposes attention into a set of independent subsequence computations.
* **Memory-adaptive scheduling**: Enables flexible execution across devices without inter-device communication.
* **Predictable memory scaling**: Demonstrated in experiments, showing that exact attention over billion-token sequences can be executed on a single GPU via streaming.

**Experimental Overview**
========================

* **Tasks/Datasets**: Not specified in the extracted context.
* **Baselines/Comparisons**: Not specified in the extracted context.
* **Main claimed findings**: Stream-CQSA enables predictable memory scaling and allows for the execution of exact attention over billion-token sequences on a single GPU via streaming.

**What to Verify in the PDF**
==========================

* **Detailed implementation of Stream-CQSA**: Verify the implementation of Stream-CQSA and how it decomposes attention into subproblems.
* **Optimization of attention kernel**: Verify the optimization of the attention kernel and how it affects the performance of Stream-CQSA.
* **Memory usage and allocation**: Verify the memory usage and allocation strategies used in Stream-CQSA to ensure predictable memory scaling.
* **Experimental setup and results**: Verify the experimental setup and results to ensure that the claimed findings are accurate.
{% endraw %}

{% raw %}
## 4) Convergent Evolution: How Different Language Models Learn Similar Number Representations
- **Authors:** Deqing Fu, Tianyi Zhou, Mikhail Belkin, Vatsal Sharan, Robin Jia
- **arXiv:** [2604.20817](https://arxiv.org/abs/2604.20817v1) · [pdf](https://arxiv.org/pdf/2604.20817v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.20817v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> Language models trained on natural text learn to represent numbers using periodic features with dominant periods at $T=2, 5, 10$. In this paper, we identify a two-tiered hierarchy of these features: while Transformers, Linear RNNs, LSTMs, and classical word embeddings trained in different ways all learn features that have period-$T$ spikes in the Fourier domain, only some learn geometrically separable features that can be used to linearly classify a number mod-$T$. To explain this incongruity, we prove that Fourier domain sparsity is necessary but not sufficient for mod-$T$ geometric separability. Empirically, we investigate when model training yields geometrically separable features, finding that the data, architecture, optimizer, and tokenizer all play key roles. In particular, we identify two different routes through which models can acquire geometrically separable features: they can learn them from complementary co-occurrence signals in general language data, including text-number co-occurrence and cross-number interaction, or from multi-token (but not single-token) addition problems. Overall, our results highlight the phenomenon of convergent evolution in feature learning: A diverse range of models learn similar features from different training signals.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: T=2,5,10
\[ T = 2, 5, 10 \]
Symbols: \( T \) (periods)
Why it matters: This equation represents the periods at which Fourier spikes appear in the embeddings of number tokens.

### Equation 2: T=2,5
\[ T = 2, 5 \]
Symbols: \( T \) (periods)
Why it matters: This equation is a subset of Equation 1, representing the specific periods at which Fourier spikes appear in the embeddings.

### Equation 3: n mod T
\[ n \bmod T \]
Symbols: \( n \) (number), \( T \) (period)
Why it matters: This equation represents the modular arithmetic operation, which is used to evaluate whether the embeddings encode modular arithmetic at period \( T \).

### Equation 4: {\bm{e}}(n)
\[ {\bm{e}}(n) \]
Symbols: \( {\bm{e}}(n) \) (token embedding of number \( n \))
Why it matters: This equation represents the token embedding of a number \( n \), which is used to evaluate the Fourier spikes and modular arithmetic.

**Method Summary**
================

* The authors investigate the phenomenon of convergent evolution in feature learning, where different language models learn similar number representations.
* They identify a two-tiered hierarchy of features: periodic features with dominant periods at \( T = 2, 5, 10 \) and geometrically separable features that can be used to linearly classify numbers modulo \( T \).
* The authors prove that Fourier domain sparsity is necessary but not sufficient for mod- \( T \) geometric separability.
* They find that the data, architecture, optimizer, and tokenizer all play key roles in determining whether mod- \( T \) classes become linearly separable in the embeddings.

**Experimental Overview**
=========================

* Tasks/Datasets:
	+ Training 300M Transformers on integer addition using the same architecture as in the paper.
	+ Evaluating the embeddings using linear probing to predict numbers modulo \( T \).
* Baselines/Comparisons:
	+ Baseline: Training a linear probe to predict numbers modulo \( T \) on the embeddings.
	+ Comparisons: Other language models (e.g., LSTMs, classical word embeddings) and baselines (e.g., random initialization).
* Main Claimed Findings:
	+ Fourier spikes appear in every system, but probing is not sufficient for mod- \( T \) separability.
	+ Geometric convergence requires data, architecture, and optimizer alignment.

**What to Verify in the PDF**
==========================

* The authors' experimental methodology for perturbing data and ablation studies.
* The condition number of the weight matrices \( {\bm{S}}_{W} \) and \( \Phi_{T} \) for different models and architectures.
* The impact of reducing the number of layers in LSTMs on the phenomenon of convergent evolution.
{% endraw %}

{% raw %}
## 5) Physics-Conditioned Synthesis of Internal Ice-Layer Thickness for Incomplete Layer Traces
- **Authors:** Zesheng Liu, Maryam Rahnemoonfar
- **arXiv:** [2604.20783](https://arxiv.org/abs/2604.20783v1) · [pdf](https://arxiv.org/pdf/2604.20783v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.20783v1))
- **Categories:** cs.LG

### Abstract
> Internal ice layers imaged by radar provide key evidence of snow accumulation and ice dynamics, but radar-derived layer boundary observations are often incomplete, with discontinuous traces and sometimes entirely missing layers, due to limited resolution, sensor noise, and signal loss. Existing graph-based models for ice stratigraphy generally assume sufficiently complete layer profiles and focus on predicting deeper-layer thickness from reliably traced shallow layers. In this work, we address the layer-completion problem itself by synthesizing complete ice-layer thickness annotations from incomplete radar-derived layer traces by conditioning on colocated physical features synchronized from physical climate models. The proposed network combines geometric learning to aggregate within-layer spatial context with a transformer-based temporal module that propagates information across layers to encourage coherent stratigraphy and consistent thickness evolution. To learn from incomplete supervision, we optimize a mask-aware robust regression objective that evaluates errors only at observed thickness values and normalizes by the number of valid entries, enabling stable training under varying sparsity without imputation and steering completions toward physically plausible values. The model preserves observed thickness where available and infers only missing regions, recovering fragmented segments and even fully absent layers while remaining consistent with measured traces. As an additional benefit, the synthesized thickness stacks provide effective pretraining supervision for a downstream deep-layer predictor, improving fine-tuned accuracy over training from scratch on the same fully traced data.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `x'_{i} = W_{1}x_{i} + W_{2} \cdot \mathrm{mean}_{j \in \mathcal{N}(i)} x_{j}`

* Equation: `x'_{i} = W_{1}x_{i} + W_{2} \cdot \mathrm{mean}_{j \in \mathcal{N}(i)} x_{j}`
* Symbols:
	+ `x'_{i}`: predicted value for node `i`
	+ `W_{1}`: weight matrix for node `i`
	+ `W_{2}`: weight matrix for mean aggregation
	+ `x_{i}`: node feature vector for node `i`
	+ `x_{j}`: node feature vector for node `j` in the neighborhood of `i`
	+ `mean_{j \in \mathcal{N}(i)}`: mean of node feature vectors in the neighborhood of `i`
* Why it matters: This equation represents the node update rule in the graph transformer network, where the predicted value for node `i` is computed by aggregating the node feature vector with the mean of its neighboring nodes.

### Equation 2: Not found in extracted context.

### Equation 3: Not found in extracted context.

### Equation 4: Not found in extracted context.

### Equation 5: Not found in extracted context.

### Equation 6: Not found in extracted context.

### Equation 7: Not found in extracted context.

### Equation 8: Not found in extracted context.

**Method Summary**
================

* The proposed graph transformer network combines geometric learning and temporal modules to complete incomplete ice-layer traces.
* The network uses a GraphSAGE inductive geometric learning framework and a transformer encoder to capture spatial and temporal dependencies.
* The model is conditioned on colocated physical features from physical climate models to improve accuracy.

**Experimental Overview**
========================

* Tasks: Ice-layer completion
* Datasets: SRED dataset
* Baselines: GraphSAGE, Transformer encoder
* Main claimed findings: The proposed graph transformer network outperforms baselines in completing incomplete ice-layer traces, with improved accuracy and robustness.

**What to Verify in the PDF**
==========================

* The implementation details of the GraphSAGE network and transformer encoder, including the choice of hyperparameters and architecture.
* The evaluation metrics used to measure performance, including mean absolute error and RMSE.
* The results of the two-stage learning rate schedule and its impact on training stability and GPU memory.
{% endraw %}
