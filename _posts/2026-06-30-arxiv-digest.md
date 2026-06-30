---
layout: post
title: "Daily arXiv Digest — 2026-06-30 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Optimization Dynamics Imprint Semantic Specificity in Contrastive Embedding Norms
- **Authors:** Ziwei Su, Junyu Ren, Victor Veitch
- **arXiv:** [2606.30625](https://arxiv.org/abs/2606.30625v1) · [pdf](https://arxiv.org/pdf/2606.30625v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.30625v1))
- **Categories:** stat.ML, cs.AI, cs.LG, math.OC

### Abstract
> Contrastive embedding models trained with scale-invariant losses are typically paired with distance metrics like cosine similarity, effectively ignoring embedding magnitudes. However, surprisingly, empirical studies reveal that despite this, these "discarded" norms seem to correlate with semantic properties such as concept specificity, token frequency, and human uncertainty. In this work, we provide a formal theoretical framework explaining this phenomenon. By analyzing the optimization dynamics, we derive an analytic formula demonstrating that embedding length naturally encodes this information as a byproduct of the training process. We also show how this gives rise to signals that can serve as "free" calibration tools in specific models and retrieval tasks, providing a grounded explanation for a previously heuristic observation.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: z/\|z\|
\[ z/\|z\| = u_i \]
Symbols: \( z \), \( \|z\| \), \( u_i \)
Why it matters: This equation represents the normalized embedding vector \( u_i \), which is used to compute the similarity matrix \( S_{ij} \).

### Equation 2: \|z\|
\[ \|z\| = R \]
Symbols: \( z \), \( R \)
Why it matters: This equation represents the norm (magnitude) of the embedding vector \( z \), which is used to normalize the embedding.

### Equation 3: z=f(x;\theta)
\[ z = f(x;\theta) \]
Symbols: \( z \), \( x \), \( \theta \)
Why it matters: This equation represents the embedding function, which maps the input \( x \) to an embedding vector \( z \) using the model parameters \( \theta \).

### Equation 4: z_{t}(x):=f(x;{}_{t})
\[ z_{t}(x) = f(x;{}_{t}) \]
Symbols: \( z_{t}(x) \), \( x \), \( {}_{t} \)
Why it matters: This equation represents the embedding vector at time step \( t \), which is computed by applying the embedding function to the input \( x \) using the model parameters at time step \( t \).

### Equation 5: \ell_{2}
\[ \ell_{2} \]
Symbols: \( \ell_{2} \)
Why it matters: This equation represents the squared loss function, which is used to compute the contrastive loss.

**Method Summary**
==================

* The authors propose a theoretical framework to explain the phenomenon of embedding norms correlating with semantic properties in contrastive embedding models.
* The framework is based on the optimization dynamics of the model, which is analyzed using the gradient of the loss function.
* The authors derive an analytic formula that demonstrates how the embedding length naturally encodes semantic information as a byproduct of the training process.

**Experimental Overview**
=========================

* The authors conduct experiments on two datasets: a synthetic dataset containing artificial concepts and a real-world dataset (CIFAR-10H).
* The experiments involve training the model using different optimization algorithms (SGD) and evaluating the performance of the model on the validation set.
* The authors compare the performance of the model with different hyperparameters (batch size, learning rate, weight decay) and evaluate the correlation between the embedding norms and semantic properties.

**What to Verify in the PDF**
=============================

* The authors claim that the embedding norms correlate with semantic properties such as concept specificity, token frequency, and human uncertainty. Verify this claim by analyzing the results of the experiments and computing the correlation between the embedding norms and these semantic properties.
* The authors propose a theoretical framework to explain the phenomenon of embedding norms correlating with semantic properties. Verify this framework by analyzing the optimization dynamics of the model and computing the gradient of the loss function.
* The authors evaluate the performance of the model on the validation set using different optimization algorithms and hyperparameters. Verify the results of these experiments by analyzing the performance of the model on the validation set and comparing it with the baseline performance.
{% endraw %}

{% raw %}
## 2) C$^{2}$R: Cross-sample Consistency Regularization Mitigates Feature Splitting and Absorption in Sparse Autoencoders
- **Authors:** Haoran Jin, Xiting Wang, Shijie Ren, Hong Xie, Defu Lian
- **arXiv:** [2606.30609](https://arxiv.org/abs/2606.30609v1) · [pdf](https://arxiv.org/pdf/2606.30609v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.30609v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Sparse Autoencoders (SAEs) are widely used to interpret large language models by decomposing activations into sparse, human-understandable features, but scaling to large dictionaries exposes fundamental challenges. Systematic studies reveal pervasive feature splitting that fragments coherent concepts into non-atomic latents and widespread feature absorption that creates arbitrary exceptions in general features, severely compromising latent reliability. These issues stem from inconsistent latent assignment across samples: without cross-sample constraints, per-sample optimization often allows a single underlying concept to be inconsistently distributed across multiple redundant or interfering latents. To address this, we introduce C$^2$R (\underline{\textbf{C}}ross-sample \underline{\textbf{C}}onsistency \underline{\textbf{R}}egularization). C$^2$R explicitly encourages that each semantic feature is consistently represented by a unified latent across the batch by penalizing the co-activation of directionally similar latents. Comprehensive evaluation demonstrates that C$^2$R effectively mitigates both splitting and absorption while, crucially, preserving reconstruction fidelity, providing a principled solution that enhances latent interpretability without degrading model performance. Source code is available at https://github.com/hr-jin/Cross-sample-Consistency-Regularization.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\ell_{1}$

* Equation: $\ell_{1} = \sum_{i=1}^{n} \left\| \mathbf{x}_i - \mathbf{y}_i \right\|_1$
* Symbols: $\ell_{1}$, $\mathbf{x}_i$, $\mathbf{y}_i$, $n$
* Why it matters: This is a common regularization term used to promote sparsity in the model's weights.

### Equation 2: $\times$

* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation is not explicitly provided in the context, so its significance is unclear.

### Equation 3: $\checkmark$

* Equation: Not provided
* Symbols: Not provided
* Why it matters: This equation is not explicitly provided in the context, so its significance is unclear.

**Method Summary**
==================

* The authors propose a geometric framework to unify feature splitting and absorption in sparse autoencoders.
* The framework introduces a redundancy parameter $\alpha$ to quantify the extent to which a semantic feature "leaks" into varying latents.
* The authors derive a single consistency condition that prevents both feature splitting and absorption.
* The method uses a unified problem formulation to analyze the behavior of $\ell_{1}$ and TopK objectives.

**Experimental Overview**
========================

* The authors conduct systematic experiments on Gemma-2-2B using a 500M-token subset from the OpenWebText dataset.
* The experiments evaluate the effectiveness of C$^{2}$R on feature absorption and feature splitting.
* The authors compare C$^{2}$R with four different SAE architectures: TopK SAEs, Batch TopK SAEs, Matryoshka SAEs, and OrtSAEs.
* The main claimed findings include:
	+ C$^{2}$R effectively mitigates feature absorption and feature splitting.
	+ C$^{2}$R preserves reconstruction fidelity.
	+ C$^{2}$R enhances latent interpretability without degrading model performance.

**What to Verify in the PDF**
=============================

* The authors mention that the source code is available at https://github.com/hr-jin/Cross-sample-Consistency-Regularization. Verify that the code implements the C$^{2}$R method correctly.
* The authors claim that the computational efficiency of C$^{2}$R is improved using a block-wise computation strategy. Verify that this approach reduces the overhead to negligible levels while preserving performance.
* The authors perform an ablation study to evaluate the sensitivity of C$^{2}$R to the regularization strength $\lambda_{C^{2}R}$. Verify that the results show that $\lambda_{C^{2}R} = 5$ achieves the best trade-off between feature absorption and reconstruction fidelity.
{% endraw %}

{% raw %}
## 3) Uncertainty-Aware Generation and Decision-Making Under Ambiguity
- **Authors:** Nico Daheim, Iryna Gurevych
- **arXiv:** [2606.30578](https://arxiv.org/abs/2606.30578v1) · [pdf](https://arxiv.org/pdf/2606.30578v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.30578v1))
- **Categories:** cs.CL, cs.LG

### Abstract
> With rapidly improving capabilities, Large Language Models (LLMs) are increasingly used in many complex real-world tasks. Beyond requiring in-depth knowledge and reasoning skills, many of these tasks exhibit a high degree of subjectivity and require that the outputs of the model can be trusted. While a lot of progress has been made to train better models, decision-making algorithms have received less attention. In this work, we present and evaluate various uncertainty-aware decision-making algorithms based on Bayesian decision theory and risk-averse decision making on the tasks of tutoring and automatic peer reviewing. Concretely, we take uncertainty over tutoring strategies and review scores into account when generating a tutor response or review and use conformal prediction to provide guarantees over strategy and score. We find empirically that these algorithms can improve the utility of the generations but need to be carefully implemented when ambiguity is high. For example, risk-averse rules can degrade performance by optimizing for generic outputs, while Bayesian methods tend to perform better. Our work uses techniques from decision theory to improve LLM-based decision-making and outlines open challenges for the community.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $\mbox{$\mbox{$\mathbf{y}$}$}=(y_{1},\dots,y_{T})\in\mathcal{V}^{\ast}$

* Equation: $\mbox{$\mbox{$\mathbf{y}$}$}=(y_{1},\dots,y_{T})\in\mathcal{V}^{\ast}$
* Symbols: $\mbox{$\mbox{$\mathbf{y}$}$}$ (review), $y_{i}$ (review score), $\mathcal{V}^{\ast}$ (set of reviews)
* Why it matters: This equation represents the set of reviews $\mbox{$\mbox{$\mathbf{y}$}$}$, which is a sequence of review scores $y_{1}, \dots, y_{T}$.

### Equation 2: $\mathcal{V}$

* Equation: $\mathcal{V}$
* Symbols: $\mathcal{V}$ (set of reviews)
* Why it matters: This equation represents the set of reviews $\mathcal{V}$, which is the input for the review generation model.

### Equation 3: $\mbox{$\mbox{$\mathbf{x}$}$}\in\mathcal{V}^{\ast}$

* Equation: $\mbox{$\mbox{$\mathbf{x}$}$}\in\mathcal{V}^{\ast}$
* Symbols: $\mbox{$\mbox{$\mathbf{x}$}$}$ (context), $\mathcal{V}^{\ast}$ (set of reviews)
* Why it matters: This equation represents the context $\mbox{$\mbox{$\mathbf{x}$}$}$, which is a review that is used to generate a review score.

### Equation 5: $\mbox{$\mbox{$\mathbf{y}$}$}\sim p(\cdot\mid\mbox{$\mbox{$\mathbf{x}$}$})$

* Equation: $\mbox{$\mbox{$\mathbf{y}$}$}\sim p(\cdot\mid\mbox{$\mbox{$\mathbf{x}$}$})$
* Symbols: $\mbox{$\mbox{$\mathbf{y}$}$}$ (review), $p(\cdot\mid\mbox{$\mbox{$\mathbf{x}$}$})$ (probability distribution over reviews given context)
* Why it matters: This equation represents the probability distribution over reviews given the context $\mbox{$\mbox{$\mathbf{x}$}$}$.

### Equation 7: $\mathbf{y}$

* Equation: $\mathbf{y}$
* Symbols: $\mathbf{y}$ (review score)
* Why it matters: This equation represents the review score $\mathbf{y}$, which is the output of the review generation model.

**Method Summary**
==================

* The authors propose a method for uncertainty-aware generation and decision-making under ambiguity in the context of peer review and tutoring.
* The method uses a combination of automated and human review generation to provide uncertainty-aware reviews and tutoring responses.
* The authors compare their method to a baseline that uses a Bayes decision rule and a method that uses conformal set pruning.
* The authors also evaluate the performance of their method on a set of tasks and datasets, including review generation and scoring, and tutor response generation and tutoring strategy prediction.

**Experimental Overview**
========================

* Tasks: Review generation and scoring, tutor response generation and tutoring strategy prediction.
* Datasets: Review-5k, NLPEER, MathDial.
* Baselines: Bayes decision rule, conformal set pruning, minmax objective.
* Main claimed findings: The authors claim that their method outperforms the baselines on review generation and scoring, and tutor response generation and tutoring strategy prediction.

**What to Verify in the PDF**
=============================

* The authors' method for uncertainty-aware generation and decision-making under ambiguity.
* The performance of the method on the Review-5k and NLPEER datasets.
* The evaluation of the method on the MathDial dataset.
* The authors' conclusions about the effectiveness of the method in providing uncertainty-aware reviews and tutoring responses.
{% endraw %}

{% raw %}
## 4) Forensic Trajectory Signatures for Agent Memory Poisoning Detection
- **Authors:** Jun Wen Leong
- **arXiv:** [2606.30566](https://arxiv.org/abs/2606.30566v1) · [pdf](https://arxiv.org/pdf/2606.30566v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.30566v1))
- **Categories:** cs.CR, cs.LG

### Abstract
> We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool invocations, successful attacks require calling memory_recall_fact before email_send_email, a transition that non-exfiltrating sessions rarely exhibit. Under the evaluated architecture, this invariant follows from the attack's information-retrieval dependency rather than being merely an empirical correlation, and suppressing it breaks the attack. A simple rule exploiting this invariant alone achieves AUC = 0.9563. A Random Forest classifier over 19 trajectory features refines it to AUC = 0.9904 (BCa 95% CI [0.987, 0.993], N=10,000 resamples), demonstrating that the attack imprints on multiple independent behavioral channels. The signature is overdetermined: removing all recall-related features (half the feature set) leaves AUC unchanged at 0.990, confirming that memory poisoning induces a distributed trajectory signature rather than a single observable anomaly. Cross-model hold-out on 9 models (7B-120B parameters) confirms AUC = 1.000 on 6/9 hold-out splits, with all three exceptions mechanistically explained. The invariant generalizes to frontier models (GPT-4.1, GPT-4o) without retraining. A strictly prefix-only variant achieves AUC = 0.934, suggesting that real-time blocking is feasible with moderate degradation. The boundary is forensically useful: prompt-injection attacks that bypass memory produce a distinct trajectory (score = 0.541), enabling incident responders to distinguish memory-channel attacks from prompt-injection attacks using tool-call logs alone.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: AUC = 0.9563

* Equation: AUC = 0.9563
* Symbols: AUC (Area Under the Curve), None
* Why it matters: This is the AUC value of the simplest detector, which uses only the behavioral invariant to classify attacks.

### Equation 2: AUC = 0.9904

* Equation: AUC = 0.9904
* Symbols: AUC (Area Under the Curve), None
* Why it matters: This is the AUC value of the Random Forest classifier, which refines the simplest detector by incorporating multiple independent behavioral channels.

### Equation 3: [0.987, 0.993]

* Equation: [0.987, 0.993]
* Symbols: None
* Why it matters: This represents the 95% confidence interval (BCa) for the AUC value of the Random Forest classifier, indicating the reliability of the results.

### Equation 4: N = 10,000

* Equation: N = 10,000
* Symbols: N (number of resamples)
* Why it matters: This represents the number of resamples used to estimate the 95% confidence interval for the AUC value of the Random Forest classifier.

### Equation 5: AUC = 0.990

* Equation: AUC = 0.990
* Symbols: AUC (Area Under the Curve), None
* Why it matters: This is the AUC value of the Random Forest classifier after removing all recall-related features, demonstrating the overdetermination of the attack signature.

### Equation 6: AUC = 1.000

* Equation: AUC = 1.000
* Symbols: AUC (Area Under the Curve), None
* Why it matters: This is the AUC value of the Random Forest classifier after cross-model hold-out on 9 models, indicating the robustness of the detector across different architectures.

### Equation 7: AUC = 0.934

* Equation: AUC = 0.934
* Symbols: AUC (Area Under the Curve), None
* Why it matters: This is the AUC value of the prefix-only variant of the detector, which achieves a moderate degradation in performance.

### Equation 8: score = 0.541

* Equation: score = 0.541
* Symbols: score, None
* Why it matters: This represents the score value of the prompt-injection attacks that bypass memory, enabling incident responders to distinguish memory-channel attacks from prompt-injection attacks using tool-call logs alone.

**Method Summary**
==================

* The authors propose a memory-channel poisoning attack, where the adversary injects a malicious instruction via a RAG-retrieved document, which the agent stores in persistent memory.
* The detector targets the memory-channel poisoning attack and reports its behavior on prompt-injection attacks as the evasion boundary.
* The authors use a simple rule exploiting the behavioral invariant alone to achieve AUC = 0.9563, which is refined by a Random Forest classifier to achieve AUC = 0.9904.
* The detector is overdetermined, as removing all recall-related features leaves AUC unchanged at 0.990.

**Experimental Overview**
=========================

* Tasks/Datasets: The authors evaluate the detector on 405 attack sessions and 560 non-attack sessions across frontier models from separate experiments.
* Baselines/Comparisons: The authors compare the performance of the detector to a logistic regression baseline and a random forest baseline.
* Main Claimed Findings: The authors claim that the detector achieves high accuracy (AUC = 0.9904) and robustness across different architectures (AUC = 1.000) and that the attack signature is overdetermined.

**What to Verify in the PDF**
=============================

* The authors mention that the detector achieves Recall = 0.901 with FPR = 23.0% on frontier models. Verify that this is indeed the case and that the elevated FPR compared to training is due to the higher baseline of self-correction in non-attack sessions.
* Verify that the 40 missed attacks are overwhelmingly from evasion experiments (prompt-inline attacks, expected by design).
* Verify that the authors provide a principled explanation for the near-invariance of the AUC value across feature-group removals, demonstrating the overdetermination of the attack signature.
{% endraw %}

{% raw %}
## 5) Convergence of Continual Learning in Homogeneous Deep Networks
- **Authors:** Matan Schliserman, Gon Buzaglo, Itay Evron, Daniel Soudry
- **arXiv:** [2606.30559](https://arxiv.org/abs/2606.30559v1) · [pdf](https://arxiv.org/pdf/2606.30559v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2606.30559v1))
- **Categories:** cs.LG, math.NA, math.OC, stat.ML

### Abstract
> We characterize weakly regularized continual classification in homogeneous models as sequential projections onto task margin sets. This result generalizes prior analyses restricted to either stationary (single-task) deep models or continual linear models. We show that global convergence generally fails, even for simple models linear in data but nonlinear in parameters. Nevertheless, by leveraging results from nonconvex projection theory, we identify regularity properties of homogeneous deep networks that guarantee local linear convergence under random and cyclic task sequences. Finally, we extend our analysis to continual regression, unifying the framework for homogeneous models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Update Rule for Continual Classification

\[ \Theta_{t}^{(\lambda)} \leftarrow \operatorname*{argmin}_{\Theta} \big\{ \mathcal{L}_{t}(\Theta) + \lambda \big\| \Theta - \Theta_{t-1}^{(\lambda)} \big\|_{\mathbf{B}_{t}}^2 \big\} \]

*   **Equation:** Update rule for the model parameters $\Theta$ at time step $t$.
*   **Symbols:**
    *   $\Theta_{t}^{(\lambda)}$: updated model parameters at time step $t$ with regularization parameter $\lambda$.
    *   $\mathcal{L}_{t}(\Theta)$: loss function for task $t$.
    *   $\mathbf{B}_{t}$: regularization matrix.
*   **Why it matters:** This equation describes how the model parameters are updated at each time step, incorporating both the loss function and regularization term.

### Equation 2: Regularization Matrix

\[ \mathbf{B}_{t} \succeq 0 \]

*   **Equation:** Regularization matrix $\mathbf{B}_{t}$.
*   **Symbols:** $\mathbf{B}_{t}$: regularization matrix.
*   **Why it matters:** This equation specifies the properties of the regularization matrix, which is used to enforce the regularization term in the update rule.

### Equation 3: Identity Regularization Matrix

\[ \mathbf{B}_{t} = \mathbf{I} \]

*   **Equation:** Identity regularization matrix.
*   **Symbols:** $\mathbf{I}$: identity matrix.
*   **Why it matters:** This equation specifies a special case of the regularization matrix, where it is equal to the identity matrix.

### Equation 4: Decreasing Regularization Parameter

\[ \lambda \downarrow 0 \]

*   **Equation:** Decreasing regularization parameter.
*   **Symbols:** $\lambda$: regularization parameter.
*   **Why it matters:** This equation specifies how the regularization parameter decreases over time, which affects the trade-off between model plasticity and stability.

### Equation 5: Optimized Model Parameters

\[ \bm{\theta}^{(\lambda)} \]

*   **Equation:** Optimized model parameters with regularization parameter $\lambda$.
*   **Symbols:** $\bm{\theta}^{(\lambda)}$: optimized model parameters.
*   **Why it matters:** This equation describes the optimized model parameters at each time step, incorporating both the loss function and regularization term.

**Method Summary**
==================

*   **Continual Learning Algorithm:** The algorithm minimizes the margin-based logistic loss for each task, incorporating isotropic L2 regularization to prevent catastrophic forgetting.
*   **Regularization Parameter:** The regularization parameter $\lambda$ decreases over time, affecting the trade-off between model plasticity and stability.
*   **Optimized Model Parameters:** The optimized model parameters are updated at each time step, incorporating both the loss function and regularization term.

**Experimental Overview**
==========================

*   **Tasks/Datasets:** The algorithm is tested on $M$ classification tasks, with feature matrices $\mathbf{X}^{(m)} \in \mathbb{R}^{n_m \times d}$ and binary labels $\mathbf{y}^{(m)} \in \{-1, 1\}^{n_m}$.
*   **Baselines/Comparisons:** The algorithm is compared to standard deep learning practices, such as weighted L2 regularization.
*   **Main Claimed Findings:** The algorithm achieves local linear convergence under random and cyclic task sequences, even for simple models linear in data but nonlinear in parameters.

**What to Verify in the PDF**
=============================

*   **Proof of Local Linear Convergence:** Verify the proof of local linear convergence, which relies on nonconvex projection theory.
*   **Regularization Matrix Properties:** Verify the properties of the regularization matrix, including its relationship to the identity matrix.
*   **Effect of Decreasing Regularization Parameter:** Verify the effect of decreasing the regularization parameter on the trade-off between model plasticity and stability.
{% endraw %}
