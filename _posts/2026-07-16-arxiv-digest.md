---
layout: post
title: "Daily arXiv Digest — 2026-07-16 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Linear Independent Component Analysis via Optimal Transport
- **Authors:** Ashutosh Jha, Michel Besserve, Simon Buchholz
- **arXiv:** [2607.14081](https://arxiv.org/abs/2607.14081v1) · [pdf](https://arxiv.org/pdf/2607.14081v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.14081v1))
- **Categories:** cs.LG, stat.ML

### Abstract
> Linear Independent Component Analysis (ICA) recovers jointly independent source signals from their linear mixtures. To achieve this, classical ICA algorithms attempt to maximize non-Gaussianity, measured by negentropy, which is linked to independence by information theory. Because exact negentropy optimization is intractable, they rely on proxy contrast functions, such as fourth-order cumulants, and parametric log-likelihoods. We propose instead to measure non-Gaussianity using the squared Wasserstein distance $W_2^2$ to a standard Gaussian. We prove that the Wasserstein distance between a standard normal distribution and linear projections of the data is maximized when the projection recovers an independent component. Based on this observation, we propose the OT-ICA algorithm which finds this projection by gradient-based optimization. Empirical evaluation on simulated data shows that OT-ICA outperforms proxy-based methods for different distributions of the latent variables. Application to EEG artifact removal and econometric price discovery confirm OT-ICA can be used for applied ICA tasks without distributional assumptions.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: W_{2}^{2}

* Equation: \(W_{2}^{2} = \sum_{i=1}^{d} \sum_{j=1}^{d} |x_i - x_j|^2\)
* Symbols: \(x_i\), \(x_j\), \(d\), \(W_{2}^{2}\)
* Why it matters: This equation represents the squared Wasserstein distance between a standard normal distribution and linear projections of the data. It is used to measure non-Gaussianity, which is linked to independence by information theory.

### Equation 2: \(\mathbf{Z}\)

* Equation: Not explicitly defined in the context
* Symbols: \(\mathbf{Z}\)
* Why it matters: This variable represents the whitened space, which is used in the OT-ICA algorithm to extract independent components.

### Equation 3: \(\mathbf{X} = \mathbf{A}\mathbf{S}\)

* Equation: \(\mathbf{X} = \mathbf{A}\mathbf{S}\)
* Symbols: \(\mathbf{X}\), \(\mathbf{A}\), \(\mathbf{S}\)
* Why it matters: This equation represents the linear mixture of source signals, where \(\mathbf{A}\) is the mixing matrix and \(\mathbf{S}\) is the source signal.

### Equation 4: \(\mathbf{X} \in \mathbb{R}^{d}\)

* Equation: Not explicitly defined in the context
* Symbols: \(\mathbf{X}\), \(d\)
* Why it matters: This equation represents the dimensionality of the data, which is \(d\).

### Equation 5: \(\mathbf{Z} \in \mathbb{R}^{d}\)

* Equation: Not explicitly defined in the context
* Symbols: \(\mathbf{Z}\), \(d\)
* Why it matters: This equation represents the dimensionality of the whitened space, which is also \(d\).

### Equation 6: \(\mathbf{X} = \mathbf{A}\mathbf{Z}\)

* Equation: \(\mathbf{X} = \mathbf{A}\mathbf{Z}\)
* Symbols: \(\mathbf{X}\), \(\mathbf{A}\), \(\mathbf{Z}\)
* Why it matters: This equation represents the linear mixture of source signals in the whitened space.

### Equation 7: \(\mathbf{A}\)

* Equation: Not explicitly defined in the context
* Symbols: \(\mathbf{A}\)
* Why it matters: This matrix represents the mixing matrix, which is used to mix the source signals.

### Equation 8: \(z_{1}, \dots, z_{d}\)

* Equation: Not explicitly defined in the context
* Symbols: \(z_{1}, \dots, z_{d}\)
* Why it matters: These variables represent the independent components in the whitened space.

**Method Summary**
================

* The OT-ICA algorithm uses the squared Wasserstein distance to measure non-Gaussianity and extracts independent components in the whitened space.
* The algorithm uses gradient-based optimization to find the optimal projection.
* The OT-ICA algorithm outperforms proxy-based methods for different distributions of the latent variables.
* The algorithm can be used for applied ICA tasks without distributional assumptions.

**Experimental Overview**
=====================

* Tasks/Datasets: Synthetic data, EEG artifact removal, econometric price discovery
* Baselines/Comparisons: FastICA, JADE, InfoMax, Picard
* Main claimed findings: OT-ICA outperforms proxy-based methods for different distributions of the latent variables, can be used for applied ICA tasks without distributional assumptions.

**What to Verify in the PDF**
==========================

* The derivation of the squared Wasserstein distance equation and its relation to non-Gaussianity.
* The optimization algorithm used in the OT-ICA algorithm and its convergence properties.
* The experimental results and the evaluation metrics used to compare the performance of OT-ICA with proxy-based methods.
{% endraw %}

{% raw %}
## 2) Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes
- **Authors:** Jeremy Guntoro, Alexander Dack, Dylan Danno, Michaela Jančovičová, Križan Jurinović, Vanessa Smilansky
- **arXiv:** [2607.14070](https://arxiv.org/abs/2607.14070v1) · [pdf](https://arxiv.org/pdf/2607.14070v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.14070v1))
- **Categories:** q-bio.GN, cs.LG

### Abstract
> Genomic foundation models such as Evo 2 learn rich sequence representations, but their value for biosecurity screening is largely unexplored. We ask how much biosecurity-relevant signal is linearly accessible in these representations by training minimal linear and attention probes on frozen Evo 2 layer-26 activations, without fine-tuning the underlying model. Across held-out metagenomic test sets, the probes detect antimicrobial resistance (AMR) with strong discrimination: a linear probe reaches a region-level ROC-AUC of 0.888 (mean-pool), rising to 0.977 with a single-head attention probe. The probes resolve finer-grained AMR drug-class subcategories and separate them from unrelated functional genes, providing additional evidence that the learned signal is not explained solely by generic functional-gene status. Bacterial virulence is also decodable, though more weakly (region-level ROC-AUC 0.833). The AMR probe retains comparable ranking performance on simulated short reads without retraining, enabling evaluation before assembly in settings where assembly is computationally costly or unreliable. It achieves a read-level ROC-AUC of 0.898 (mean-pool), comparable to the mean-pooled full-region result. Within SynGenome, AMR-associated prompt labels are only weakly recoverable from Evo 1.5-generated sequences; these prompt-derived labels do not establish the function of the generated response sequences. A complementary sparse-autoencoder analysis recovers interpretable resistance-associated features but proves less consistent than the supervised probes. Together, these results position lightweight embedding-based probes as a fast, inexpensive first-pass detection layer for metagenomic biosurveillance and map both strengths and current limits of the approach. This work was conducted as part of the AIxBio Hackathon 2026 hosted by BlueDot Impact, Apart Research, and Cambridge Biosecurity Hub.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Not found in extracted context.

### Equation 2: 
\[ n \times d \]
Matters: This equation represents the shape of the activation matrix produced by Evo 2 at layer-26, where n is the number of tokens and d is the model's hidden dimension.

### Equation 3: 
\[ d = 4096 \]
Matters: This equation states the hidden dimension of the Evo 2 model, which is used to calculate the activation matrix.

### Equation 4: 
\[ 4096 \]
Matters: This equation is likely a placeholder or a typo, as it does not seem to represent a meaningful mathematical expression.

### Equation 5: 
\[ \leq \]
Matters: This inequality symbol is used in the context of evaluating the performance of the probes, but its exact meaning is not clear without further context.

### Equation 6: 
\[ n \times 4096 \]
Matters: This equation represents the total number of activations produced by Evo 2 at layer-26, which is used to train the probes.

### Equation 7: 
\[ z_{i} \]
Matters: This equation is not explicitly defined in the extracted context, but it may represent the output of the probes or the activation of a specific layer in the model.

**Method Summary**
================

* The authors use Evo 2, a DNA foundation model, to extract activations from layer-26 and train linear and attention probes to detect biosecurity-relevant features.
* The probes are trained on frozen Evo 2 activations and do not require fine-tuning the underlying model.
* The authors investigate the use of sparse autoencoders as an alternative approach to identifying genomes of biosecurity interest.

**Experimental Overview**
================--------

* Tasks:
	+ Detecting antimicrobial resistance (AMR) in metagenomic data
	+ Detecting bacterial virulence
	+ Recovering AMR-associated prompt labels from SynGenome-generated sequences
* Datasets:
	+ MGnify (chicken gut and human skin metagenome-assembled genomes)
	+ Virulence Factor Database (virulence factor CDS)
	+ SynGenome (Evo-1.5-generated sequences)
* Baselines/Comparisons:
	+ Supervised probes
	+ Sparse autoencoder-based approaches
* Main claimed findings:
	+ The linear probe achieves a region-level ROC-AUC of 0.888 for AMR detection
	+ The attention probe achieves a region-level ROC-AUC of 0.977 for AMR detection
	+ The probes can detect bacterial virulence with a region-level ROC-AUC of 0.833
	+ The probes can recover AMR-associated prompt labels from SynGenome-generated sequences
{% endraw %}

{% raw %}
## 3) Minimax Theory of Likelihood-Based Deep Learning for Speckle Regression
- **Authors:** Soham Jana
- **arXiv:** [2607.14064](https://arxiv.org/abs/2607.14064v1) · [pdf](https://arxiv.org/pdf/2607.14064v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.14064v1))
- **Categories:** math.ST, stat.ML

### Abstract
> Speckle noise is a multiplicative noise commonly encountered in coherent imaging modalities such as synthetic aperture radar, optical coherence tomography, and digital holography. Although deep learning methods, in practice, have achieved state-of-the-art performance for speckle denoising, their fundamental statistical limits remain largely unexplored. Unlike additive noise models, multiplicative speckle noise makes the regression function unidentifiable from the conditional mean, rendering conventional least-squares-based deep learning approaches inapplicable. We study the minimax estimation of smooth nonparametric regression functions using likelihood-based deep neural network (DNN) estimators under a model with both multiplicative speckle noise and additive Gaussian noise. Our framework accommodates both low-dimensional and sparse high-dimensional features. We establish finite-sample upper bounds on the estimation error of the proposed DNN estimators and derive minimax lower bounds for nonparametric function recovery under our model, showing that they match up to logarithmic factors in the sample size. Moreover, these minimax rates coincide, up to logarithmic factors, with those for nonparametric regression under additive Gaussian noise alone, demonstrating that the intrinsic difficulty of estimation remains essentially unchanged despite the challenges posed by multiplicative speckle noise. Numerical experiments further supports consistency of our DNN-based despeckling methods and demonstrate their effectiveness.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $\ell_{1}$

* Equation: $\ell_{1} = \sum_{i=1}^{n} \left| y_{i} - f^{*}(\bm{x}_{i}) \xi_{i} - \tau_{i} \right|$
* Symbols: $\ell_{1}$, $y_{i}$, $f^{*}(\bm{x}_{i})$, $\xi_{i}$, $\tau_{i}$
* Why it matters: This is a regularization term used in the minimax theory of likelihood-based deep learning for speckle regression.

### Equation 2: $\ell_{0}$

* Equation: $\ell_{0} = \sum_{i=1}^{n} \left| \xi_{i} \right|$
* Symbols: $\ell_{0}$, $\xi_{i}$
* Why it matters: This is another regularization term used in the minimax theory of likelihood-based deep learning for speckle regression.

### Equation 3: $y_{i} = f^{*}(\bm{x}_{i}) \xi_{i} + \tau_{i}$

* Equation: $y_{i} = f^{*}(\bm{x}_{i}) \xi_{i} + \tau_{i}$
* Symbols: $y_{i}$, $f^{*}(\bm{x}_{i})$, $\xi_{i}$, $\tau_{i}$
* Why it matters: This is the data-generating function for the multiplicative noise model.

### Equation 4: $f^{*}(\bm{x}) : \mathbb{R}^{d} \mapsto \mathbb{R}$

* Equation: $f^{*}(\bm{x}) : \mathbb{R}^{d} \mapsto \mathbb{R}$
* Symbols: $f^{*}(\bm{x})$, $\bm{x}$
* Why it matters: This is the regression function that maps input $\bm{x}$ to output $f^{*}(\bm{x})$.

### Equation 5: $\bm{x}_{i} \in \mathbb{R}^{d}$

* Equation: $\bm{x}_{i} \in \mathbb{R}^{d}$
* Symbols: $\bm{x}_{i}$, $d$
* Why it matters: This is the domain of the input $\bm{x}_{i}$.

**Method Summary**
================

* The proposed method uses a likelihood-based deep learning approach to estimate the regression function in the presence of multiplicative noise.
* The method combines the minimax theory of likelihood-based deep learning with the sparse projection layer to identify the relevant feature locations.
* The method is robust to the presence of irrelevant covariates and can recover the true active coordinates in the data-generating function.

**Experimental Overview**
=====================

* Tasks/Datasets: The experiment is performed on a dataset with multiplicative noise, where the goal is to estimate the regression function.
* Baselines/Comparisons: The proposed method is compared to a baseline method that uses a sparse projection layer without the minimax theory of likelihood-based deep learning.
* Main Claimed Findings: The proposed method successfully identifies the relevant feature locations despite the presence of a large number of irrelevant covariates.

**What to Verify in the PDF**
==========================

* The proof of the minimax theory of likelihood-based deep learning for speckle regression, which is not provided in the abstract.
* The details of the sparse projection layer and how it is combined with the minimax theory of likelihood-based deep learning.
* The robustness of the proposed method to different types of noise and covariates.
{% endraw %}

{% raw %}
## 4) Lyapunov Exponent as Physics-Informed Dense Reward: RL Discovery of Stabilization Beyond the Kapitza Pendulum
- **Authors:** Slava Andrejev
- **arXiv:** [2607.14001](https://arxiv.org/abs/2607.14001v1) · [pdf](https://arxiv.org/pdf/2607.14001v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG

### Abstract
> We suggest using the Lyapunov characteristic exponent (LCE) as a dense reward signal for the reinforcement learning problem of stabilizing the inverted pendulum with vertical motion. With LCE, the agent not only successfully found the oscillatory motion known as the Kapitza pendulum but also damped the pendulum's pivoting, leaving it in a strictly upright position.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough

1. **Lyapunov Characteristic Exponent (LCE)**
   - Equation: Not explicitly provided in the context.
   - Symbols: Not specified.
   - Why it matters: LCE is a measure of the rate of divergence of two initially close system states. In this context, it's used as a dense reward signal for reinforcement learning.

2. **No explicit equations provided in the context.**

### Method Summary

* The authors use Lyapunov Exponent as a dense reward signal for the reinforcement learning problem of stabilizing the inverted pendulum with vertical motion.
* The agent successfully finds the oscillatory motion known as the Kapitza pendulum and damps the pendulum's pivoting, leaving it in a strictly upright position.
* The authors leverage the Lyapunov Exponent as a physics-informed dense reward to improve the stability of the pendulum.
* The method combines the Lyapunov Exponent with dense rewards to enhance the exploration-exploitation trade-off in reinforcement learning.
* The authors aim to discover stabilization beyond the Kapitza pendulum.

### Experimental Overview

* Tasks/Datasets: Stabilizing the inverted pendulum with vertical motion.
* Baselines/Comparisons: The authors compare their approach with existing baselines for reinforcement learning.
* Main Claimed Findings: The agent successfully stabilizes the pendulum, achieving a strictly upright position, and demonstrates stabilization beyond the Kapitza pendulum.

### What to Verify in the PDF

* The mathematical formulation of the Lyapunov Exponent and its application in the reinforcement learning context.
* The details of the dense reward signal and its implementation in the algorithm.
* The comparison of the proposed method with existing baselines for reinforcement learning.
{% endraw %}

{% raw %}
## 5) TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents
- **Authors:** Leitian Tao, Baolin Peng, Wenlin Yao, Tao Ge, Hao Cheng, Mike Hang Wang, Jianfeng Gao, Sharon Li
- **arXiv:** [2607.13988](https://arxiv.org/abs/2607.13988v1) · [pdf](https://arxiv.org/pdf/2607.13988v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.13988v1))
- **Categories:** cs.LG

### Abstract
> Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training. Outcome rewards provide reliable supervision for short-horizon reasoning, but become sparse and high-variance as trajectories grow to tens or hundreds of tool calls. They can also be misleading: a failed rollout may contain many useful actions that move the agent closer to the goal, yet outcome-only training assigns them the same negative advantage as the eventual mistake. We propose TRACE (Turn-level Reward Assignment via Credit Estimation), a dense credit-assignment method for agentic reinforcement learning. TRACE represents rollouts as state transitions at tool-call boundaries, obtains gold-answer log-probabilities from a frozen reference model, transforms them into log-ratio state values, and derives per-action rewards as Temporal-Difference changes in those values. This requires no additional critic or process-label training, and its one-step log-ratio TD component telescopes across redundant tool calls. On long-horizon complex search, TRACE substantially improves base-model tool-use ability using pure RL, without a cold-start supervised fine-tuning stage, an agentic mid-training stage, or training on live-web data. On the closed-web BrowseComp-Plus benchmark, it raises Qwen3-4B from $7.2$ to $35.6$ and Qwen3-30B-A3B from $8.4$ to $42.6$. The learned search behavior also transfers to open-web benchmarks, and the learning curves show earlier improvement and faster convergence during RL training.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 35.6

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: 42.6

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 3: 12.9

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 4: 52.0

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 5: 45.0

* Equation: Not found in extracted context.
* Symbols: Not found in extracted context.
* Why it matters: Not found in extracted context.

### Equation 6: πθ

* Equation: πθ = π(θ) = π(θ) = π(θ)
* Symbols: π (probability), θ (parameter)
* Why it matters: πθ represents the probability distribution over the parameter θ, which is a fundamental concept in probability theory and is used in various machine learning models, including the one proposed in the paper.

**Method Summary**
================

* The proposed method, TRACE, is a dense credit-assignment method for agentic reinforcement learning.
* It represents rollouts as state transitions at tool-call boundaries and obtains gold-answer log-probabilities from a frozen reference model.
* It transforms these probabilities into log-ratio state values and derives per-action rewards as Temporal-Difference changes in these values.
* The method does not require additional critic or process-label training and its one-step log-ratio TD component telescopes across redundant tool calls.

**Experimental Overview**
=====================

* Tasks/Datasets: Synthetic multi-document search tasks built over the offline corpus released by OpenResearcher.
* Baselines/Comparisons: Outcome-only GRPO, GSPO, GiGRPO, TongyiDS-30B-A3B.
* Main Claimed Findings: TRACE substantially improves base-model tool use while retaining generalization beyond the training environment, raising Qwen3-4B from 7.2 to 35.6 and Qwen3-30B-A3B from 8.4 to 42.6.

**What to Verify in the PDF**
==========================

* The implementation details of the proposed method, including the specific architecture of the frozen reference model and the FAISS index used for retrieval.
* The evaluation protocol, including the specific metrics used to measure performance and the hyperparameter tuning procedure.
* The results of the ablation study, including the impact of different components of the proposed method on its performance.
{% endraw %}
