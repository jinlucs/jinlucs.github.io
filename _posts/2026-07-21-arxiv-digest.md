---
layout: post
title: "Daily arXiv Digest — 2026-07-21 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Vector Search As Nearest Neighbor Matching: RAG-based Policy Learning in Causal Inference
- **Authors:** Masahiro Kato, Taka Kato
- **arXiv:** [2607.18225](https://arxiv.org/abs/2607.18225v1) · [pdf](https://arxiv.org/pdf/2607.18225v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.18225v1))
- **Categories:** econ.EM, cs.LG, math.ST, stat.ME, stat.ML

### Abstract
> We propose one-step and two-step methods for policy learning with retrieval-augmented generation (RAG). We formulate RAG-based action selection under the potential outcome framework. In the two-step method, vector search retrieves action-specific neighboring evidence in an embedding space, the generator estimates conditional expected outcomes or their contrasts, and a plug-in rule selects an action. This formulation connects action-specific vector search with nearest-neighbor matching in causal inference. We decompose the regret of the two-step method into candidate-generation regret and within-candidate choice regret, and we bound the latter using prediction-error guarantees for nearest-neighbor estimators and transformers. We evaluate the one-step method directly as a policy because its intermediate computation is unobserved.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**1. Formula Walkthrough**
### Equation 1: Defining the Action Set
\[ A \in \mathcal{K} \coloneqq \left\{ 0, 1, \dots, K - 1 \right\} \]
Symbols: \( A \), \( \mathcal{K} \), \( K \)
Why it matters: This equation defines the set of possible actions, \( \mathcal{K} \), which is a set of integers from 0 to \( K - 1 \).

### Equation 2: Defining the Outcome Function
\[ Y(a) \]
Symbols: \( Y \), \( a \)
Why it matters: This equation defines the outcome function, \( Y \), which takes an action \( a \) as input and produces an outcome.

### Equation 3: Defining the Optimal Action
\[ a^{*}(x) \in \operatorname*{arg\,max}_{a \in \mathcal{K}} \mathbb{E} \left[ Y(a) \mid X = x \right] \]
Symbols: \( a^{*} \), \( x \), \( \mathcal{K} \), \( \mathbb{E} \)
Why it matters: This equation defines the optimal action, \( a^{*} \), which is the action that maximizes the expected outcome, \( \mathbb{E} \left[ Y(a) \mid X = x \right] \), given the covariates \( X = x \).

### Equation 4: Defining the Optimal Action (Alternative Form)
\[ a^{*}(x) \]
Symbols: \( a^{*} \), \( x \)
Why it matters: This equation is an alternative form of Equation 3, which defines the optimal action, \( a^{*} \), as the action that maximizes the expected outcome.

### Equation 5: Defining the Covariates and Action Space
\[ X \in \mathcal{X} \subseteq \mathbb{R}^{d} \]
Symbols: \( X \), \( \mathcal{X} \), \( d \)
Why it matters: This equation defines the covariates, \( X \), which are a subset of \( \mathbb{R}^{d} \), and the action space, \( \mathcal{X} \), which is a subset of \( \mathbb{R}^{d} \).

**2. Method Summary**
* The authors propose two methods for policy learning with retrieval-augmented generation (RAG): one-step and two-step methods.
* The one-step method returns an action directly, while the two-step method returns the two action-specific conditional expected outcomes and selects the candidate with the largest estimate.
* The authors use prediction-error guarantees from the literature on in-context learning to bound the regret of the two-step method.

**3. Experimental Overview**
* Tasks/Datasets: The authors evaluate the proposed methods on three datasets (DGP 1, DGP 2, and DGP 3).
* Baselines/Comparisons: The authors compare the proposed methods with a baseline method, RAG without covariates.
* Main Claimed Findings: The authors claim that the proposed methods reduce the mean regret from the baseline method, and that the optimal-action probability increases.

**4. What to Verify in the PDF**
* The authors mention that the optimal-action probability counts any action attaining the largest true conditional expected outcome as optimal. Verify that this is indeed the case.
* The authors also mention that ties are handled by value rather than by agreement with one tie-breaking label. Verify that this is the case.
* The authors use a fixed tie-breaking rule when needed. Verify that this rule is applied correctly.
* The authors mention that the embedding input contains only a fixed-order description of the pre-action information. Verify that this is the case.
{% endraw %}

{% raw %}
## 2) Unveiling Invariant and Transferable Latent Factors Across Heterogeneous Environments via ATLAS
- **Authors:** Yihong Gu, Katherine Liao, Tianxi Cai
- **arXiv:** [2607.18209](https://arxiv.org/abs/2607.18209v1) · [pdf](https://arxiv.org/pdf/2607.18209v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.18209v1))
- **Categories:** math.ST, cs.LG, stat.ME, stat.ML

### Abstract
> This paper considers a multi-environment factor model in which high-dimensional covariates are collected from heterogeneous environments, with auxiliary labels available in a subset of these environments. The joint distribution of the covariates may vary across environments, whereas the latent structure is decomposed into invariant factors with shared loadings and heterogeneous factors with environment-specific loadings. Such a model is motivated by transfer learning and latent factor regression, where one seeks stable low-dimensional representations for both interpretation and robust out-of-sample prediction of the response $Y$. Leveraging the invariance principle, we show that the invariant and heterogeneous factors are disentangled under a minimal structural condition. Based on this, we propose ATLAS, an Auxiliary-label and invariance-guided Transfer via Latent Alignment across heterogeneous environmentS. ATLAS is a unified procedure that leverages the invariance principle to separate aligned invariant and unaligned heterogeneous factors, and further exploits supervision from auxiliary labels to extract prediction-invariant and transferable factors from those unaligned heterogeneous factors. ATLAS yields near-oracle performance for downstream latent factor regression, enables transferable prediction in new environments through the full latent signal when auxiliary labels are available, and reduces to robust invariant-factor-only prediction otherwise. We establish sharp non-asymptotic error bounds for recovering invariant and heterogeneous factors, identifying all the response-invariant factors, and estimating the invariant signal in $Y$.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mathcal{E}$

* Equation: $\mathcal{E}$
* Symbols: $\mathcal{E}$
* Why it matters: $\mathcal{E}$ represents the set of environments.

### Equation 2: $e \in \mathcal{E}$

* Equation: $e \in \mathcal{E}$
* Symbols: $e \in \mathcal{E}$
* Why it matters: $e$ represents an environment in $\mathcal{E}$.

### Equation 3: $X^{(e)} \in \mathbb{R}^{d}$

* Equation: $X^{(e)} \in \mathbb{R}^{d}$
* Symbols: $X^{(e)} \in \mathbb{R}^{d}$
* Why it matters: $X^{(e)}$ represents the covariates in environment $e$.

### Equation 4: $Z^{(e)} \in \mathbb{R}^{q}$

* Equation: $Z^{(e)} \in \mathbb{R}^{q}$
* Symbols: $Z^{(e)} \in \mathbb{R}^{q}$
* Why it matters: $Z^{(e)}$ represents the auxiliary labels in environment $e$.

### Equation 5: $Y^{(e)}$

* Equation: $Y^{(e)}$
* Symbols: $Y^{(e)}$
* Why it matters: $Y^{(e)}$ represents the target responses in environment $e$.

**Method Summary**
==================

* The authors propose ATLAS, an Auxiliary-label and invariance-guided Transfer via Latent Alignment across heterogeneous environments.
* ATLAS leverages the invariance principle to separate aligned invariant and unaligned heterogeneous factors.
* The authors use diversified projection (DP) to disentangle invariant from environment-specific latent structure.
* ATLAS adapts DP to the multi-environment setting in three stages: (1) constructing separate DP matrices for invariant and heterogeneous factors, (2) aligning prediction-invariant components across environments, and (3) estimating the invariant prediction rule and transferring it to new environments.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors evaluate ATLAS on a single-environment benchmark for weak factor recovery.
* Baselines/Comparisons: The authors compare ATLAS to standard factor models and diversified projection (DP).
* Main Claimed Findings: ATLAS yields near-oracle performance for downstream latent factor regression and enables transferable prediction in new environments through the full latent signal when auxiliary labels are available.

**What to Verify in the PDF**
=============================

* The authors establish sharp non-asymptotic error bounds for recovering invariant and heterogeneous factors, identifying all the response-invariant factors, and estimating the invariant signal in $Y$.
* The authors provide an intuitive explanation of the necessity of Condition 1 and establish deterministic results on $\|\cdot\|_{2}$ error bounds for the residuals.
* The authors discuss the implications of the invariance principle and the role of auxiliary labels in transfer learning and latent factor regression.
{% endraw %}

{% raw %}
## 3) PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning
- **Authors:** Hang Zhang, Warren J. Gross
- **arXiv:** [2607.18199](https://arxiv.org/abs/2607.18199v1) · [pdf](https://arxiv.org/pdf/2607.18199v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.18199v1))
- **Categories:** cs.CL, cs.LG

### Abstract
> Not all training samples contribute equally to large language model fine-tuning. Selecting informative training samples can reduce the computational cost while preserving downstream performance. Many existing data selection methods rely on indirect heuristics, such as data quality, diversity or reasoning trace length. However, the effectiveness of these fixed criteria is task-dependent and difficult to generalize across diverse downstream tasks. Perplexity-based data selection provides a simple and model-aware solution to estimate the sample difficulty, but existing approaches typically score the entire training sequence and ignore the difference in learning objectives of language modeling and reasoning tasks. In this paper, we propose PPL-Factory, a simple and interpretable data selection framework that combines task-aware perplexity-based scores and data budget-aware selection criteria. Experiments on GSM8K demonstrate that PPL-Factory outperforms other state-of-the-art data selection methods using only $1\%$ of the training set. With $10\%$ of the data, PPL-Factory exceeds full-data fine-tuning accuracy by 0.9 on GSM8K and 4.8 on MATH. Overall, our results demonstrate that task-aware and budget-aware perplexity-based selection provides an effective and applicable approach for efficient fine-tuning.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Selection Ratio
```markdown
ρ ∈ (0, 1]
```
* Symbols: ρ (selection ratio)
* Why it matters: The selection ratio ρ represents the proportion of the training dataset that will be selected for fine-tuning.

### Equation 2: Uniform Distribution
```markdown
u(x) ∼ U(0, 1)
```
* Symbols: u(x) (utility score), U(0, 1) (uniform distribution)
* Why it matters: The utility score u(x) is assumed to follow a uniform distribution U(0, 1), which means that all scores are equally likely to be chosen.

### Equation 3: Computational Complexity
```markdown
C_{forward}(x) + O(d|V|)
```
* Symbols: C_{forward}(x) (forward computation cost), O(d|V|) (big O notation)
* Why it matters: The forward computation cost C_{forward}(x) is proportional to the number of tokens in the input x and the size of the vocabulary V.

### Equation 4: Perplexity Score
```markdown
u(x) = PPL_{θ}(x)
```
* Symbols: u(x) (utility score), PPL_{θ}(x) (perplexity score)
* Why it matters: The utility score u(x) is equivalent to the perplexity score PPL_{θ}(x), which measures the model's uncertainty about the input x.

### Equation 5: Informative-Coverage Score
```markdown
u(x) = sim(h_{θ}(x), h_{θ}(V))
```
* Symbols: u(x) (utility score), sim (similarity function), h_{θ}(x) (hidden state of the model), h_{θ}(V) (hidden state of the model for the vocabulary)
* Why it matters: The utility score u(x) measures the similarity between the hidden state of the model for the input x and the hidden state of the model for the vocabulary, which represents the informative coverage of the input.

**Method Summary**
==================

* **Task-aware data selection**: PPL-Factory selects data based on the task-aware perplexity score, which is computed using the frozen pre-trained LLM.
* **Budget-aware selection**: The selected subset is then used to fine-tune the pre-trained LLM, with a budget-aware selection criterion to minimize the fine-tuning cost.
* **Combination of NLL scores**: The utility score is computed by combining the NLL scores from the reasoning and answer components.
* **Efficient fine-tuning**: The fine-tuning cost is reduced by selecting a subset of the training data, with a trade-off between performance and training cost.

**Experimental Overview**
========================

* **Tasks/Datasets**: CLM tasks (WikiText-2 and WikiText-103), mathematical reasoning tasks (GSM8K and MATH)
* **Baselines/Comparisons**: Random selection, single-component NLL scoring variants (reasoning NLL, answer NLL, response NLL)
* **Main Claimed Findings**: PPL-Factory achieves the most stable performance across datasets, with a trade-off between performance and training cost.

**What to Verify in the PDF**
=============================

* **Theoretical analysis**: Verify the mathematical derivations of the informative-coverage score and the utility score.
* **Fine-tuning cost analysis**: Verify the computational complexity of the forward computation cost and the fine-tuning cost.
* **Ablation study**: Verify the results of the ablation study, including the performance of different NLL scoring variants and the effect of the selection ratio on the fine-tuning cost.
{% endraw %}

{% raw %}
## 4) Three-Body Scattering for Generative Modeling
- **Authors:** Peng Sun, Zhenglin Cheng, Deyuan Liu, Jun Xie, Xinyi Shang, Tao Lin
- **arXiv:** [2607.18198](https://arxiv.org/abs/2607.18198v1) · [pdf](https://arxiv.org/pdf/2607.18198v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.18198v1))
- **Categories:** cs.LG, cs.CV

### Abstract
> Modern generative models typically rely on an adversarial critic, a prescribed noise-to-data path, or an autoregressive factorization. Instead, we show that a proper distributional energy can induce sample-level motion and provide direct regression supervision for a one-step generator. Three-Body Scattering Modeling (TBSM) for generation turns the energy distance into a constant-size per-projectile interaction: each projectile is attracted toward one real source and repelled from one independently generated source. Conditioned on the projectile and its condition, its expectation equals the $2$-Wasserstein gradient-flow velocity of $\frac12D_E^2(P_θ,Q)$. A batch of $B$ frozen-target events yields $O(B)$ sample-level losses, each using one reference for its condition instead of the minibatch-wide all-pairs field used by methods such as Drifting Models. Tracking this conditional expectation online can reduce field noise. Using scattering in frozen image features, TBSM trains one-step generators on ImageNet-256, achieving FID${}=2.23$ with pixel-space PixelDiT-XL and FID${}=1.63$ with latent-space DiT-XL at NFE${}=1$. We provide a design map relating diffusion-related supervision, Drift-like dynamics, and GAN-like objectives. These results establish tracked scattering as a route to high-dimensional one-step generation. Code: https://github.com/sp12138/TBSM.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Squared Energy Distance

\[ \frac{1}{2}D_{E}^{2}(P_{\boldsymbol{\theta}},Q) \]

Symbols: \( D_{E}^{2} \) (squared energy distance), \( P_{\boldsymbol{\theta}} \) (probability law induced by generator), \( Q \) (true probability law)

Why it matters: This equation represents the squared energy distance between the induced probability law \( P_{\boldsymbol{\theta}} \) and the true probability law \( Q \), which is used as the population discrepancy in the distributional objective.

### Equation 2: Batch Size

\[ O(B) \]

Symbols: \( B \) (batch size)

Why it matters: This equation represents the number of sample-level losses that can be computed from a batch of \( B \) frozen-target events.

### Equation 3: FID Score (Pixel-Space)

\[ {}=2.23 \]

Symbols: \( FID \) (Frechet Inception Distance), \( {} \) (score)

Why it matters: This equation represents the FID score achieved by the proposed method on the ImageNet-256 dataset, indicating the similarity between the generated samples and the real data.

### Equation 4: FID Score (Latent-Space)

\[ {}=1.63 \]

Symbols: \( FID \) (Frechet Inception Distance), \( {} \) (score)

Why it matters: This equation represents the FID score achieved by the proposed method on the ImageNet-256 dataset, indicating the similarity between the generated samples and the real data.

### Equation 5: Number of Training Steps

\[ {}=1 \]

Symbols: \( {} \) (number of training steps)

Why it matters: This equation represents the number of training steps used to train the proposed method.

**Method Summary**
==================

* The proposed method uses a three-body scattering modeling approach to induce sample-level motion and provide direct regression supervision for a one-step generator.
* The method consists of a conditional generator and a tracker, which are trained using a population objective and stochastic optimization.
* The tracker is designed to track the conditional expectation of the generator, which is computed using the Wasserstein gradient-flow velocity.

**Experimental Overview**
========================

* Tasks: One-step generation on ImageNet-256 and ImageNet-512 datasets.
* Datasets: ImageNet-1K, MNIST, Fashion-MNIST, and CIFAR-10.
* Baselines: JiT, DiT, PixelDiT, and W-Flow.
* Main claimed findings: The proposed method achieves competitive results on the ImageNet-256 and ImageNet-512 datasets, with FID scores of 2.23 and 1.63, respectively.

**What to Verify in the PDF**
=============================

* The derivation of the population objective and stochastic optimization algorithm.
* The implementation details of the tracker and generator architectures.
* The results of the ablation study on the effect of the number of frozen feature spaces on the performance of the proposed method.
{% endraw %}

{% raw %}
## 5) Certified Training for Convolutional Perturbations
- **Authors:** Benedikt Brückner, Alessio Lomuscio
- **arXiv:** [2607.18195](https://arxiv.org/abs/2607.18195v1) · [pdf](https://arxiv.org/pdf/2607.18195v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.18195v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> Vision models have been found to be susceptible to perturbations such as motion blur induced at runtime by a shaking camera. This impedes their deployment in critical applications since phenomena such as slightly blurred vision might lead to failures, for example an object detector missing objects. While methods such as data augmentation or Adversarial Training can improve empirical robustness, they lack formal safety guarantees, making it difficult to identify and mitigate hidden vulnerabilities. We introduce a novel Certified Training approach that leverages an efficient encoding of convolutional perturbations to train provably robust models. Our method significantly outperforms Adversarial Training, achieving, for example, over 80% robust accuracy against motion blur of reasonable intensity on CIFAR10 while maintaining comparable standard accuracy.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Robust Accuracy
```markdown
80%
```
* Equation: Not applicable
* Symbols: Not applicable
* Why it matters: The authors report that their method achieves over 80% robust accuracy against motion blur on CIFAR10.

### Equation 2: L-infinity Norm
```markdown
l_{\infty}
```
* Equation: Not applicable
* Symbols: Not applicable
* Why it matters: The authors use the L-infinity norm to define the perturbation radius ϵ.

### Equation 3: Robust Accuracy
```markdown
70%
```
* Equation: Not applicable
* Symbols: Not applicable
* Why it matters: The authors report that their method achieves 70% robust accuracy against motion blur on CIFAR10.

### Equation 4: Perturbation Coefficient
```markdown
{\bm{a}}
```
* Equation: Not applicable
* Symbols: {\bm{a}} (perturbation coefficient)
* Why it matters: The authors use the perturbation coefficient {\bm{a}} to encode the desired perturbations.

### Equation 5: Perturbation Matrix
```markdown
{\bm{A}}
```
* Equation: Not applicable
* Symbols: {\bm{A}} (perturbation matrix)
* Why it matters: The authors use the perturbation matrix {\bm{A}} to simulate perturbations such as motion blur or sharpen.

**Method Summary**
================

* The authors introduce a novel Certified Training approach that leverages an efficient encoding of convolutional perturbations to train provably robust models.
* The method uses a parameterized perturbation kernel to simulate perturbations and a batched convolution operation to compute the perturbation coefficients.
* The authors use the bound propagation implementation of VeriNet to handle convolutional perturbations and add the required training functionality.
* The method is compared to Adversarial Training and achieves higher robust accuracy.

**Experimental Overview**
========================

* Tasks: The authors evaluate their method on the CIFAR10 and TinyImageNet datasets.
* Baselines: The authors compare their method to Adversarial Training and Standard Training.
* Main claimed findings: The authors report that their method achieves higher robust accuracy than Adversarial Training and Standard Training, and that the verified robust accuracy is higher than the empirical robust accuracy.

**What to Verify in the PDF**
=============================

* The authors claim that their method is effective in training provably robust models. Verify that the method is able to achieve high robust accuracy on the CIFAR10 and TinyImageNet datasets.
* The authors claim that their method is more effective than Adversarial Training and Standard Training. Verify that the method achieves higher robust accuracy and verified robust accuracy than the baselines.
* The authors claim that the method is scalable to larger network architectures. Verify that the method is able to achieve high robust accuracy on the ResNet18 model.
{% endraw %}
