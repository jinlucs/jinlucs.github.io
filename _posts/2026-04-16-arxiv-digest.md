---
layout: post
title: "Daily arXiv Digest — 2026-04-16 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space
- **Authors:** Yuqiao Tan, Minzheng Wang, Bo Liu, Zichen Liu, Tian Liang, Shizhu He, Jun Zhao, Kang Liu
- **arXiv:** [2604.14142](https://arxiv.org/abs/2604.14142v1) · [pdf](https://arxiv.org/pdf/2604.14142v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.14142v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribution shift that hinders targeted reasoning enhancement. In this paper, we introduce PreRL (Pre-train Space RL), which applies reward-driven online updates directly to P(y). We theoretically and empirically validate the strong gradient alignment between log P(y) and log P(y|x), establishing PreRL as a viable surrogate for standard RL. Furthermore, we uncover a critical mechanism: Negative Sample Reinforcement (NSR) within PreRL serves as an exceptionally effective driver for reasoning. NSR-PreRL rapidly prunes incorrect reasoning spaces while stimulating endogenous reflective behaviors, increasing transition and reflection thoughts by 14.89x and 6.54x, respectively. Leveraging these insights, we propose Dual Space RL (DSRL), a Policy Reincarnation strategy that initializes models with NSR-PreRL to expand the reasoning horizon before transitioning to standard RL for fine-grained optimization. Extensive experiments demonstrate that DSRL consistently outperforms strong baselines, proving that pre-train space pruning effectively steers the policy toward a refined correct reasoning subspace.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**

### Equation 1: $P(y|x)$
\[ P(y|x) = \frac{P(x,y)}{P(x)} \]
Symbols: $P(y|x)$, $P(x,y)$, $P(x)$
Why it matters: This is the conditional probability of $y$ given $x$, which is a fundamental concept in probability theory.

### Equation 2: $P(y)$
\[ P(y) = \int P(y|x)P(x) dx \]
Symbols: $P(y)$, $P(y|x)$, $P(x)$
Why it matters: This is the marginal probability of $y$, which represents the overall probability of $y$ without considering the conditioning variable $x$.

### Equation 3: $\log P(y)$
\[ \log P(y) = \log \left( \int P(y|x)P(x) dx \right) \]
Symbols: $\log P(y)$, $P(y|x)$, $P(x)$
Why it matters: This is the logarithm of the marginal probability of $y$, which is used in the context of reinforcement learning to represent the log likelihood of the policy.

### Equation 4: $\log P(y|x)$
\[ \log P(y|x) = \log P(y|x) + \log P(x) \]
Symbols: $\log P(y|x)$, $P(y|x)$, $P(x)$
Why it matters: This is the logarithm of the conditional probability of $y$ given $x$, which is used in the context of reinforcement learning to represent the log likelihood of the policy.

### Equation 5: $\times$
\[ \times = \text{some unknown quantity} \]
Symbols: $\times$
Why it matters: This equation is not explicitly defined in the provided context, and its purpose is unclear.

**Method Summary**

* **Pre-train Space Reinforcement Learning (PreRL)**: A method that applies reward-driven online updates to the marginal distribution $P(y)$.
* **Negative Sample Reinforcement (NSR)**: A mechanism that uses negative samples to prune incorrect reasoning spaces and stimulate endogenous reflective behaviors.
* **Dual Space RL (DSRL)**: A policy reincarnation strategy that initializes models with NSR-PreRL to expand the reasoning horizon before transitioning to standard RL for fine-grained optimization.
* **Policy Reincarnation**: A technique that involves initializing a policy with a pre-trained model and then fine-tuning it using standard RL.

**Experimental Overview**

* **Tasks/Datasets**: The authors evaluate their method on several benchmarks, including MATH500, AMC23, AIME24, AIME25, Minerva, and OlympiadBench.
* **Baselines/Comparisons**: The authors compare their method to several strong baselines, including GRPO, PPO, Reinforce++, and RLOO.
* **Main Claimed Findings**: The authors claim that their method, DSRL, consistently outperforms strong baselines across all benchmarks and models, achieving significant improvements in accuracy and efficiency.

**What to Verify in the PDF**

* **Detailed training hyperparameters and setups**: The authors provide some information about the training hyperparameters and setups in Appendix B.1, but it would be helpful to see more detailed information about the specific hyperparameters used for each baseline and the authors' method.
* **More evaluation details**: The authors report some evaluation metrics, such as Avg@32 and Pass@K, but it would be helpful to see more detailed evaluation results, such as confusion matrices or ROC curves, to better understand the performance of each method.
* **Theoretical justification for NSR**: While the authors provide some theoretical justification for NSR, it would be helpful to see more detailed mathematical derivations or proofs to support their claims.
{% endraw %}

{% raw %}
## 2) LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning
- **Authors:** Sumeet Ramesh Motwani, Daniel Nichols, Charles London, Peggy Li, Fabio Pizzati, Acer Blake, Hasan Hammoud, Tavish McDonald, Akshat Naik, Alesia Ivanova, Vignesh Baskaran, Ivan Laptev, Ruben Glatt, Tal Ben-Nun, Philip Torr, Natasha Jaques, Ameya Prabhu, Brian Bartoldson, Bhavya Kailkhura, Christian Schroeder de Witt
- **arXiv:** [2604.14140](https://arxiv.org/abs/2604.14140v1) · [pdf](https://arxiv.org/pdf/2604.14140v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG, cs.AI

### Abstract
> As language models are increasingly deployed for complex autonomous tasks, their ability to reason accurately over longer horizons becomes critical. An essential component of this ability is planning and managing a long, complex chain-of-thought (CoT). We introduce LongCoT, a scalable benchmark of 2,500 expert-designed problems spanning chemistry, mathematics, computer science, chess, and logic to isolate and directly measure the long-horizon CoT reasoning capabilities of frontier models. Problems consist of a short input with a verifiable answer; solving them requires navigating a graph of interdependent steps that span tens to hundreds of thousands of reasoning tokens. Each local step is individually tractable for frontier models, so failures reflect long-horizon reasoning limitations. At release, the best models achieve <10% accuracy (GPT 5.2: 9.8%; Gemini 3 Pro: 6.1%) on LongCoT, revealing a substantial gap in current capabilities. Overall, LongCoT provides a rigorous measure of long-horizon reasoning, tracking the ability of frontier models to reason reliably over extended periods.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

Unfortunately, the extracted context does not provide any mathematical equations to walkthrough.

**Method Summary**
================

* LongCoT is a benchmark for evaluating long-horizon chain-of-thought (CoT) reasoning capabilities of language models.
* The benchmark consists of 2,500 expert-designed problems covering various domains (chemistry, mathematics, computer science, chess, and logic).
* Each problem requires navigating a graph of interdependent steps, with a short input and a verifiable answer.
* The benchmark assesses a model's ability to reason reliably over extended periods.

**Experimental Overview**
========================

* **Tasks/Datasets**: LongCoT benchmark
* **Baselines/Comparisons**: GPT 5.2 and Gemini 3 Pro
* **Main Claimed Findings**: The best models achieve <10% accuracy on LongCoT, revealing a substantial gap in current capabilities.

**What to Verify in the PDF**
=============================

* The exact formulation of the LongCoT problems and the graph structure used in the benchmark.
* The evaluation metrics used to assess the models' performance on LongCoT.
* The specific reasoning steps and graph traversal mechanisms employed by the models to solve the problems.
{% endraw %}

{% raw %}
## 3) From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs
- **Authors:** Itay Itzhak, Eliya Habba, Gabriel Stanovsky, Yonatan Belinkov
- **arXiv:** [2604.14137](https://arxiv.org/abs/2604.14137v1) · [pdf](https://arxiv.org/pdf/2604.14137v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.14137v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> Evaluating LLMs is challenging, as benchmark scores often fail to capture models' real-world usefulness. Instead, users often rely on ``vibe-testing'': informal experience-based evaluation, such as comparing models on coding tasks related to their own workflow. While prevalent, vibe-testing is often too ad hoc and unstructured to analyze or reproduce at scale. In this work, we study how vibe-testing works in practice and then formalize it to support systematic analysis. We first analyze two empirical resources: (1) a survey of user evaluation practices, and (2) a collection of in-the-wild model comparison reports from blogs and social media. Based on these resources, we formalize vibe-testing as a two-part process: users personalize both what they test and how they judge responses. We then introduce a proof-of-concept evaluation pipeline that follows this formulation by generating personalized prompts and comparing model outputs using user-aware subjective criteria. In experiments on coding benchmarks, we find that combining personalized prompts and user-aware evaluation can change which model is preferred, reflecting the role of vibe-testing in practice. These findings suggest that formalized vibe-testing can serve as a useful approach for bridging benchmark scores and real-world experience.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 47%
No equation provided.

### Equation 2: 92%
No equation provided.

### Equation 3: 82%
No equation provided.

### Equation 4: 5.31
No equation provided.

### Equation 5: 59%
No equation provided.

### Equation 6: 41%
No equation provided.

**Method Summary**
==================

* The authors formalize vibe-testing as a two-part process: (1) users personalize both what they test and how they judge responses.
* They introduce a proof-of-concept evaluation pipeline that generates personalized prompts and compares model outputs using user-aware subjective criteria.
* The pipeline consists of two stages: (1) trend analysis and common dimensions, and (2) framework consistency check and gap analysis.
* The authors use a combination of manual review and automated evaluation to derive a final closed set of common dimensions.

**Experimental Overview**
========================

* Tasks/Datasets: The authors analyze coding benchmarks and in-the-wild model comparison reports from blogs and social media.
* Baselines/Comparisons: The authors compare the performance of different LLMs on coding benchmarks and evaluate the reliability of automated pairwise evaluation.
* Main Claimed Findings: The authors find that combining personalized prompts and user-aware evaluation can change which model is preferred, reflecting the role of vibe-testing in practice.

**What to Verify in the PDF**
==========================

* The authors mention that the code and study artifacts are available at `https://itay1itzhak.github.io/vibe-testing-llms`. Verify that this link is correct and that the code and artifacts are publicly accessible.
* The authors mention that the survey findings suggest a gap between benchmarks and real-world experience. Verify that the survey results are presented in the paper and that the findings are supported by the data.
* The authors mention that the authors used GPT-5.1, GPT-OSS-20B, and Qwen3-14B as judges for the consistency check. Verify that the authors explain the reasoning behind this choice and that the results are presented in the paper.
{% endraw %}

{% raw %}
## 4) Rhetorical Questions in LLM Representations: A Linear Probing Study
- **Authors:** Louie Hong Yao, Vishesh Anand, Yuan Zhuang, Tianyu Jiang
- **arXiv:** [2604.14128](https://arxiv.org/abs/2604.14128v1) · [pdf](https://arxiv.org/pdf/2604.14128v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.14128v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> Rhetorical questions are asked not to seek information but to persuade or signal stance. How large language models internally represent them remains unclear. We analyze rhetorical questions in LLM representations using linear probes on two social-media datasets with different discourse contexts, and find that rhetorical signals emerge early and are most stably captured by last-token representations. Rhetorical questions are linearly separable from information-seeking questions within datasets, and remain detectable under cross-dataset transfer, reaching AUROC around 0.7-0.8. However, we demonstrate that transferability does not simply imply a shared representation. Probes trained on different datasets produce different rankings when applied to the same target corpus, with overlap among the top-ranked instances often below 0.2. Qualitative analysis shows that these divergences correspond to distinct rhetorical phenomena: some probes capture discourse-level rhetorical stance embedded in extended argumentation, while others emphasize localized, syntax-driven interrogative acts. Together, these findings suggest that rhetorical questions in LLM representations are encoded by multiple linear directions emphasizing different cues, rather than a single shared direction.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: {x_{1},\dots,x_{T}}
```markdown
Equation 1: {x_{1},\dots,x_{T}}
Symbols: x_{1},\dots,x_{T} (input tokens)
Why it matters: This equation represents the input sequence of tokens that the model processes.
```

### Equation 2: h_{T}\in\mathbb{R}^{d}
```markdown
Equation 2: h_{T}\in\mathbb{R}^{d}
Symbols: h_{T} (last token representation), d (dimensionality of the representation space)
Why it matters: This equation represents the representation of the last token in the input sequence.
```

### Equation 3: \bar{h}=\frac{1}{T}\sum_{t=1}^{T}h_{t}
```markdown
Equation 3: \bar{h}=\frac{1}{T}\sum_{t=1}^{T}h_{t}
Symbols: \bar{h} (average representation), T (number of tokens), h_{t} (representation of token t)
Why it matters: This equation represents the average representation of all tokens in the input sequence.
```

### Equation 4: h_{t}
```markdown
Equation 4: h_{t}
Symbols: h_{t} (representation of token t)
Why it matters: This equation represents the representation of a single token in the input sequence.
```

### Equation 5: k=64
```markdown
Equation 5: k=64
Symbols: k (dimensionality of the representation space)
Why it matters: This equation specifies the dimensionality of the representation space used in the analysis.
```

**Method Summary**
==================

* The authors analyze rhetorical questions in LLM representations using linear probes on two social-media datasets with different discourse contexts.
* The analysis uses a linear probing framework to examine the representation of rhetorical questions in the model's internal representations.
* The authors compare the behavior of different linear probes and evaluate their performance using AUROC and rank agreement metrics.

**Experimental Overview**
========================

* Tasks: The authors conduct steering experiments on the RQ dataset to evaluate the representation of rhetorical questions in the model's internal representations.
* Datasets: The analysis is performed on two social-media datasets with different discourse contexts.
* Baselines/Comparisons: The authors compare the performance of different linear probes and evaluate their performance using AUROC and rank agreement metrics.
* Main claimed findings: The authors demonstrate that rhetorical questions are linearly separable from information-seeking questions and that the identified linear directions capture rhetorical question intent in the model's internal representations.
{% endraw %}

{% raw %}
## 5) Complex Interpolation of Matrices with an application to Multi-Manifold Learning
- **Authors:** Adi Arbel, Stefan Steinerberger, Ronen Talmon
- **arXiv:** [2604.14118](https://arxiv.org/abs/2604.14118v1) · [pdf](https://arxiv.org/pdf/2604.14118v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.14118v1))
- **Categories:** cs.LG, math.SP

### Abstract
> Given two symmetric positive-definite matrices $A, B \in \mathbb{R}^{n \times n}$, we study the spectral properties of the interpolation $A^{1-x} B^x$ for $0 \leq x \leq 1$. The presence of `common structures' in $A$ and $B$, eigenvectors pointing in a similar direction, can be investigated using this interpolation perspective. Generically, exact log-linearity of the operator norm $\|A^{1-x} B^x\|$ is equivalent to the existence of a shared eigenvector in the original matrices; stability bounds show that approximate log-linearity forces principal singular vectors to align with leading eigenvectors of both matrices. These results give rise to and provide theoretical justification for a multi-manifold learning framework that identifies common and distinct latent structures in multiview data.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $A, B \in \mathbb{R}^{n \times n}$

* Equation: $A, B \in \mathbb{R}^{n \times n}$
* Symbols: $A, B$ (symmetric positive-definite matrices)
* Why it matters: This equation states that the matrices $A$ and $B$ are real-valued and have size $n \times n$.

### Equation 2: $A^{1-x}B^x$

* Equation: $A^{1-x}B^x$
* Symbols: $A, B, x$ (real-valued, $0 \leq x \leq 1$)
* Why it matters: This equation represents the interpolation of matrices $A$ and $B$ using the parameter $x$.

### Equation 3: $0 \leq x \leq 1$

* Equation: $0 \leq x \leq 1$
* Symbols: $x$ (real-valued, parameter)
* Why it matters: This equation specifies the range of values for the parameter $x$ that defines the interpolation.

### Equation 4: $\|A^{1-x}B^x\|$

* Equation: $\|A^{1-x}B^x\|$
* Symbols: $A, B, x$ (real-valued, $0 \leq x \leq 1$)
* Why it matters: This equation represents the norm of the interpolated matrix $A^{1-x}B^x$.

### Equation 5: $\sigma(A) = \{\lambda_1, \dots, \lambda_n\}$

* Equation: $\sigma(A) = \{\lambda_1, \dots, \lambda_n\}$
* Symbols: $\sigma(A)$, $\lambda_i$ (eigenvalues of $A$)
* Why it matters: This equation states that the set of eigenvalues of matrix $A$ is $\{\lambda_1, \dots, \lambda_n\}$.

### Equation 6: $\sigma(B) = \{\mu_1, \dots, \mu_n\}$

* Equation: $\sigma(B) = \{\mu_1, \dots, \mu_n\}$
* Symbols: $\sigma(B)$, $\mu_i$ (eigenvalues of $B$)
* Why it matters: This equation states that the set of eigenvalues of matrix $B$ is $\{\mu_1, \dots, \mu_n\}$.

**Method Summary**
================

* The authors propose a method for complex interpolation of matrices using kernel interpolation.
* The method involves applying the eigenvalue decomposition to the normalized kernels $A^2$ and $B^2$ to obtain their eigenvalues.
* The interpolation is performed using a regular grid with $M+1$ points, where $M$ is a parameter that controls the smoothness of the interpolation.
* The resulting interpolated matrices are then analyzed to identify common and distinct latent structures in the data.

**Experimental Overview**
========================

* Tasks/Datasets: The authors do not specify the exact tasks or datasets used in the experiments.
* Baselines/Comparisons: The authors do not mention any baselines or comparisons with other methods.
* Main Claimed Findings: The authors claim that the interpolated singular values of the matrix $A^{1-x}B^x$ exhibit interesting mathematical structures and provide a new framework for multi-manifold learning.

**What to Verify in the PDF**
==========================

* The authors mention that the maximum principle is used to obtain stability estimates, but the details of this argument are not provided in the abstract.
* The authors also mention that the approach is inspired by the work of Alan McIntosh, but the specific results and implications of this inspiration are not fully explained.
* The authors propose a new framework for multi-manifold learning, but the details of this framework and its applications are not fully developed in the abstract.
{% endraw %}
