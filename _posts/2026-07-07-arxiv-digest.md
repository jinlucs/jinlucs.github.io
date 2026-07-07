---
layout: post
title: "Daily arXiv Digest — 2026-07-07 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Authors:** Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini
- **arXiv:** [2607.05391](https://arxiv.org/abs/2607.05391v1) · [pdf](https://arxiv.org/pdf/2607.05391v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.05391v1))
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA, cs.RO

### Abstract
> Scaling pre-training, post-training, and test-time compute have become the central paradigms for improving the capabilities of LLMs. In this work, we identify verification, the ability to determine the correctness of a solution, as a new scaling axis. To unlock this and demonstrate its effectiveness, we introduce LLM-as-a-Verifier, a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training. Unlike standard LM judges that prompt LLMs to produce discrete scores for candidate solutions, LLM-as-a-Verifier computes the expectation over the distribution of scoring token logits to generate continuous scores. This probabilistic formulation enables verification to scale along multiple dimensions: (1) score granularity, (2) repeated evaluation, and (3) criteria decomposition. In particular, we show that scaling the scoring granularity leads to better separation between positive and negative solutions, resulting in more calibrated comparisons. Moreover, scaling repeated evaluation and criteria decomposition consistently lead to additional gains in verification accuracy through variance and complexity reduction. We further introduce a cost-efficient ranking algorithm for selecting the best solution among candidates using the verifier's continuous scores. LLM-as-a-Verifier achieves state-of-the-art performance on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), and MedAgentBench (73.3%). Beyond verification, the fine-grained signals from LLM-as-a-Verifier can also serve as a proxy for estimating task progress. We build an extension for Claude Code, enabling developers to monitor and improve their own agentic systems. Finally, we show that LLM-as-a-Verifier can provide dense feedback for RL, improving the sample efficiency of SAC and GRPO on robotics and mathematical reasoning benchmarks.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
===============

### Equation 1
\[\approx 1.8\times\]

* Equation: Approximation of a value
* Symbols: ≈, 1.8
* Why it matters: This equation represents the approximation of a value, likely used in the context of the verifier's scoring system.

### Equation 2
\[\pi_{0}\]

* Equation: Not explicitly defined in the context
* Symbols: π0
* Why it matters: This equation is not explicitly defined in the context, but it may represent a probability or a parameter in the verifier's scoring system.

### Equation 3
\[\approx 1.1\times\]

* Equation: Approximation of a value
* Symbols: ≈, 1.1
* Why it matters: This equation represents the approximation of a value, likely used in the context of the verifier's scoring system.

### Equation 4
\[\mathcal{M}=(\mathcal{C},\mathcal{S},\mathcal{A},P,R,H)\]

* Equation: Definition of a Markov decision process
* Symbols: \(\mathcal{M}\), \(\mathcal{C}\), \(\mathcal{S}\), \(\mathcal{A}\), \(P\), \(R\), \(H\)
* Why it matters: This equation defines a Markov decision process, which is a mathematical framework for modeling decision-making problems.

### Equation 5
\[\mathcal{C}\]

* Equation: Not explicitly defined in the context
* Symbols: \(\mathcal{C}\)
* Why it matters: This equation is not explicitly defined in the context, but it may represent a set of states or a set of actions in the Markov decision process.

### Equation 6
\[\mathcal{S}\]

* Equation: Not explicitly defined in the context
* Symbols: \(\mathcal{S}\)
* Why it matters: This equation is not explicitly defined in the context, but it may represent a set of states or a set of actions in the Markov decision process.

### Equation 7
\[\mathcal{A}\]

* Equation: Not explicitly defined in the context
* Symbols: \(\mathcal{A}\)
* Why it matters: This equation is not explicitly defined in the context, but it may represent a set of actions or a set of possible choices in the Markov decision process.

### Equation 8
\[P:\mathcal{C}\times\mathcal{S}\times\mathcal{A}\rightarrow\Delta(\mathcal{S})\]

* Equation: Transition probability function
* Symbols: \(P\), \(\mathcal{C}\), \(\mathcal{S}\), \(\mathcal{A}\), \(\Delta(\mathcal{S})\)
* Why it matters: This equation defines the transition probability function, which is a fundamental component of the Markov decision process. It represents the probability of transitioning from one state to another given an action.

**Method Summary**
================

* The proposed approach, LLM-as-a-Verifier, is a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training.
* The framework uses a probabilistic formulation to compute the expectation over the distribution of scoring token logits to generate continuous scores.
* The framework can scale along multiple dimensions, including score granularity, repeated evaluation, and criteria decomposition.
* The framework achieves state-of-the-art performance on several benchmarks, including Terminal-Bench V2, SWE-Bench Verified, RoboRewardBench, and MedAgentBench.

**Experimental Overview**
=====================

* The experiments evaluate LLM-as-a-Verifier as a trajectory reward model (TRM) for test-time scaling across four benchmarks:
	+ Terminal-Bench V2
	+ SWE-Bench Verified
	+ RoboRewardBench
	+ MedAgentBench
* The benchmarks span three domains: coding, robotics, and medical.
* The main claimed findings include:
	+ LLM-as-a-Verifier achieves state-of-the-art performance on all four benchmarks.
	+ The framework can scale along multiple dimensions, including score granularity, repeated evaluation, and criteria decomposition.
	+ The framework provides fine-grained feedback that can be used to estimate task progress.

**What to Verify in the PDF**
==========================

* The role of the verifier in estimating task progress and providing fine-grained feedback.
* The limitations of the framework in terms of scalability and generalizability.
* The impact of the verifier's scoring system on the performance of the agentic tasks.
* The potential applications of the framework in other domains beyond coding, robotics, and medical.
{% endraw %}

{% raw %}
## 2) What Does a Discrete Diffusion Model Learn?
- **Authors:** Rodrigo Casado Noguerales, Bernhard Schölkopf, Thomas Hofmann, Aran Raoufi
- **arXiv:** [2607.05381](https://arxiv.org/abs/2607.05381v1) · [pdf](https://arxiv.org/pdf/2607.05381v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.05381v1))
- **Categories:** cs.LG, cs.AI, cs.CL, cs.IT, stat.ML

### Abstract
> What does a discrete diffusion model learn: a denoiser, a score ratio, or a bridge plug-in predictor? At the level of jump rates, these are one object in different coordinates, and reading a neural network in the wrong coordinate changes the process being trained and sampled. Starting with a rigorous derivation of the continuous-time Markov chain (CTMC) ELBO for any noising process, boundary terms included, we prove the \emph{Oracle Distance} theorem: the negative ELBO is exactly equal to the data entropy plus the path KL from the oracle reverse process to the learned one, not merely a bound. Its unique optimizer is therefore the conditional expectation of the true reverse jump rate given the current noisy state, and its irreducible cost is the rate at which the forward process $Z_t$ destroys information about the clean data $Z_0$, $-\tfrac{d}{dt}I(Z_0; Z_t)$, so every noising process shares the same best achievable negative ELBO: the data entropy. For sequences with token-factorizing noise, the oracle projection yields three exact coordinates for the optimizer: denoiser, cavity (bridge plug-in), and score, with closed-form conversions among them. This framework identifies which law each loss in the literature actually optimizes, recovering MDM, UDM, SEDD, and GIDD as special cases; explains why denoiser and cavity coincide for masked diffusion but not for uniform diffusion; proves that a denoiser parameterization makes the uniform ELBO diverge at initialization while the bridge plug-in stays finite; and calibrates ELBO implementations exactly at initialization. Every identity is verified numerically, without approximation, on an exactly solvable model.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: Z_{t}

* Equation: \(Z_{t}\)
* Symbols: \(Z_{t}\) (random target rate)
* Why it matters: This equation represents the random target rate in the continuous-time Markov chain (CTMC) ELBO.

### Equation 2: Z_{0}

* Equation: \(Z_{0}\)
* Symbols: \(Z_{0}\) (clean data)
* Why it matters: This equation represents the clean data that the model is trying to recover.

### Equation 3: -\tfrac{d}{dt}I(Z_{0};Z_{t})

* Equation: \(-\tfrac{d}{dt}I(Z_{0};Z_{t})\)
* Symbols: \(I(Z_{0};Z_{t})\) (information between clean data and noisy data)
* Why it matters: This equation represents the rate at which the forward process destroys information about the clean data.

### Equation 4: (Z_{t})_{t\in[0,T]}

* Equation: \((Z_{t})_{t\in[0,T]}\)
* Symbols: \(Z_{t}\) (random target rate), \(t \in [0, T]\) (time)
* Why it matters: This equation represents the random target rate over time.

### Equation 5: q_{t}:=\mathrm{Law}(Z_{t})

* Equation: \(q_{t} := \mathrm{Law}(Z_{t})\)
* Symbols: \(q_{t}\) (law of the noisy data at time \(t\)), \(Z_{t}\) (noisy data at time \(t\))
* Why it matters: This equation represents the law of the noisy data at time \(t\).

**Method Summary**
==================

* The model rate cannot depend on the unknown clean data \(Z_{0}\).
* The local CTMC ELBO poses a projection problem: given a random target rate depending on \((Z_{0}, Z_{t})\), choose the best rate that only has access to \(Z_{t}\).
* The optimal projection is governed by an exact Pythagorean theorem for \(\Phi\), which identifies the optimal projection and splits the trained cost into oracle cost plus model mismatch.
* The unique optimizer is the conditional expectation of the true reverse jump rate given the current noisy state.

**Experimental Overview**
=========================

* Tasks/Datasets: Discrete diffusion models are applied to generative modeling on language and other categorical data.
* Baselines/Comparisons: The paper compares the learned reverse process to different objects (denoisers, score ratios, bridge plug-ins, leave-one-out predictors, masked-token losses, finite-step reverse kernels) in the discrete-diffusion literature.
* Main Claimed Findings: The paper provides a self-contained, general theory of continuous-time discrete diffusion, identifies which law each loss in the literature actually optimizes, and recovers MDM, UDM, SEDD, and GIDD as special cases.

**What to Verify in the PDF**
=============================

* The support and regularity conditions under which the CTMC ELBO is well-defined.
* The two complementary derivations (infinitesimal-KL limit and Girsanov argument) for the CTMC ELBO.
* The numerical verification of the identity without approximation on an exactly solvable model.
{% endraw %}

{% raw %}
## 3) TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning
- **Authors:** Yury Gorishniy, Akim Kotelnikov, Ivan Rubachev, Artem Babenko
- **arXiv:** [2607.05380](https://arxiv.org/abs/2607.05380v1) · [pdf](https://arxiv.org/pdf/2607.05380v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.05380v1))
- **Categories:** cs.LG

### Abstract
> In deep learning for tabular data, efficient ensembles of multilayer perceptrons (MLPs) have recently emerged as effective and practical architectures. Existing methods of this kind use the same hyperparameters for all underlying MLPs, which requires hyperparameter tuning for achieving the best performance. In this work, we introduce TabPack, an efficient MLP ensemble with strong out-of-the-box performance and reduced reliance on traditional tuning. In a single run, TabPack samples and trains many MLPs with different hyperparameters efficiently in parallel and selects ensemble members on the fly during training. Thus, TabPack only requires specifying ranges from which to sample MLP hyperparameter rather than exact hyperparameter values, which naturally demands less precision for good performance. In experiments on medium-to-large public datasets, TabPack with default settings performs on par with extensively tuned prior methods, thus substantially reducing effort and compute resources needed to achieve competitive results on tabular tasks. Notably, running the default TabPack configuration on a modern MacBook took less time than tuning some baselines on an industry-grade GPU.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: TabPack^{\dagger}_{\text{MacBook}}
```latex
\mbox{TabPack}^{\dagger}_{\text{MacBook}}
```
Symbols: `TabPack`, `^{\dagger}`, `_{\text{MacBook}}`
Why it matters: This equation represents the TabPack ensemble on a MacBook, indicating the specific hardware used for training.

### Equation 2: (^{*})
No equation provided.
No symbols or explanation.
No significance.

### Equation 3: (^{**})
No equation provided.
No symbols or explanation.
No significance.

### Equation 4: L_{2}
```latex
L_{2}
```
Symbols: `L`, `_{2}`
Why it matters: This equation represents the L2 loss function, commonly used in deep learning for regularization.

### Equation 5: \hat{y}
```latex
\hat{y}
```
Symbols: `\hat{y}`
Why it matters: This equation represents the predicted output, often used in evaluation metrics such as accuracy or mean squared error.

### Equation 6: W_{i}
```latex
W_{i}
```
Symbols: `W`, `_{i}`
Why it matters: This equation represents the weights of the model, crucial for training and prediction.

### Equation 7: d_{1}<d_{2}<d_{3}
No equation provided.
No symbols or explanation.
No significance.

### Equation 8: W^{i}_{j}
```latex
W^{i}_{j}
```
Symbols: `W`, `^{i}`, `_{j}`
Why it matters: This equation represents the weights of the model, specifically the interaction between the `i`-th layer and the `j`-th neuron.

**Method Summary**
================

* TabPack is an efficient ensemble of multilayer perceptrons (MLPs) that samples and trains many models with different hyperparameters in parallel.
* The ensemble selects members on the fly during training, reducing the need for traditional hyperparameter tuning.
* TabPack uses random hyperparameter sampling, which is efficient but may not improve task performance.
* The method is compared to traditional tuning and other baselines in the experiments.

**Experimental Overview**
=========================

* Tasks: Tabular deep learning tasks on medium-to-large public datasets.
* Baselines: XGBoost, plain MLP, ModernNCA, RealMLP, TabM, TabICLv2, TabPFN-3.
* Main claimed findings: TabPack outperforms baselines on most datasets with reduced runtime and hyperparameter tuning.
* Additional experiments: TabPack is evaluated on large datasets and the TabArena benchmark.

**What to Verify in the PDF**
=============================

* The implementation details of TabPack, including the random hyperparameter sampling and ensemble selection.
* The results of the experiments, including the performance metrics and runtime comparisons.
* The discussion of the limitations of TabPack, such as the potential impact of validation set size on performance.
{% endraw %}

{% raw %}
## 4) CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents
- **Authors:** Yujiang Li, Zhenyu Hou, Yi Jing, Jie Tang, Yuxiao Dong
- **arXiv:** [2607.05378](https://arxiv.org/abs/2607.05378v1) · [pdf](https://arxiv.org/pdf/2607.05378v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.05378v1))
- **Categories:** cs.LG

### Abstract
> Long-horizon agentic LLMs are increasingly limited by finite context windows, as extended interaction trajectories can exceed the maximum context length before a task is completed. Context compaction offers a natural solution by summarizing previous interaction states and continuing the rollout under a compressed context, but incorporating compaction into reinforcement learning remains underexplored. We propose CompactionRL, a reinforcement learning strategy to train long-horizon agentic LLMs with context compaction. Our approach jointly optimizes task execution and summary generation with token-level loss normalization and cross-trajectory generalized advantage estimation. This design enables the LLM agents to learn from compacted long-horizon trajectories. We train CompactionRL on top of open models and observe consistent performance gains on agentic coding tasks. CompactionRL enables the open GLM-4.5-Air model (106B-A30B) to achieve Pass@1 scores of 66.8% on SWE-bench Verified and 24.5% on Terminal-Bench 2.0, with absolute gains of 7.0 and 3.1 points, respectively. Built upon GLM-4.7-Flash (30B-A3B), CompactionRL improves Pass@1 by 5.5 and 6.8 points, reaching 56.0% on SWE-bench Verified and 20.2% on Terminal-Bench 2.0, respectively. CompactionRL is thus deployed in the RL pipeline for training the open GLM-5.2 model (750B-A40B).
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: J^{\mathrm{CLIP}}(\theta)=\mathbb{E}_{t}\left[\min\left(\rho_{t}(\theta)A_{t},\,\mathrm{clip}(\rho_{t}(\theta),1-\epsilon,1+\epsilon)A_{t}\right)\right]

* Equation: The clipped value function (CLIP) loss function, which combines the policy's value function (`\rho_{t}(\theta)`) with the clipped advantage (`\mathrm{clip}(\rho_{t}(\theta),1-\epsilon,1+\epsilon)A_{t}`).
* Symbols: `\theta` (model parameters), `\rho_{t}(\theta)` (policy value function), `A_{t}` (advantage), `\epsilon` (clip ratio).
* Why it matters: This equation represents the loss function used to train the policy in the CLIP framework, which balances the policy's value function with the clipped advantage to prevent overestimation.

### Equation 2: \rho_{t}(\theta)

* Equation: The policy value function, which estimates the expected return for a given state `x_{t}`.
* Symbols: `\theta` (model parameters), `x_{t}` (state).
* Why it matters: This equation represents the policy's estimate of the expected return for a given state, which is used to compute the policy's value function.

### Equation 3: A_{t}

* Equation: The advantage function, which estimates the expected return for a given state `x_{t}` and action `a_{t}`.
* Symbols: `\theta` (model parameters), `x_{t}` (state), `a_{t}` (action).
* Why it matters: This equation represents the estimate of the expected return for a given state and action, which is used to compute the policy's value function.

### Equation 4: \epsilon

* Equation: The clip ratio, which controls the amount of clipping applied to the policy's value function.
* Symbols: `\epsilon` (clip ratio).
* Why it matters: This equation represents the clip ratio, which controls the amount of clipping applied to the policy's value function to prevent overestimation.

### Equation 5: V_{\phi}

* Equation: The value function, which estimates the expected return for a given state `x_{T+1}`.
* Symbols: `\phi` (value function parameters), `x_{T+1}` (state).
* Why it matters: This equation represents the estimate of the expected return for a given state, which is used to compute the policy's value function.

**Method Summary**
==================

* CompactionRL is a reinforcement learning framework that incorporates context compaction into the rollout collection process.
* The framework jointly optimizes task execution and summary generation using token-level loss normalization and cross-trajectory generalized advantage estimation.
* CompactionRL is trained on top of open models and achieves consistent performance gains on agentic coding tasks.

**Experimental Overview**
==========================

* Tasks/Datasets: SWE-bench Verified and Terminal-Bench 2.0.
* Baselines/Comparisons: Standard PPO trained without compaction, GLM-4.5-Air-SFT, and GLM-4.7-Flash.
* Main Claimed Findings: CompactionRL achieves the best compacted-inference performance among all variants on both benchmarks, demonstrating the benefit of jointly training task execution and compaction.

**What to Verify in the PDF**
=============================

* The effect of varying the clip ratio on the policy's value function and the overall performance of CompactionRL.
* The impact of compaction on the model's ability to retain task-relevant information and reduce redundant re-exploration after compaction.
* The relationship between the summary length and the model's performance on compacted-inference tasks.
{% endraw %}

{% raw %}
## 5) How Far is Too Far? Defining the Distance Threshold for Verification Siamese Networks
- **Authors:** Heloísa Dias Viotto, Cauê Samonek, Lucas Garcia Pedroso, Marcos Sunye, André Abed Grégio, Paulo Lisboa de Almeida
- **arXiv:** [2607.05329](https://arxiv.org/abs/2607.05329v1) · [pdf](https://arxiv.org/pdf/2607.05329v1)
- **LLM context source:** abstract only
- **Categories:** cs.LG

### Abstract
> Siamese verification networks are widely used to compare items such as faces, cars, or signatures. In these scenarios, the network is trained to learn an embedding space in which similar objects are mapped closer together, while dissimilar objects are mapped further apart. Two objects are considered to belong to the same class (e.g., the same person in two different images) when the distance between their embeddings falls below a predefined threshold. Defining this threshold, however, is a non-trivial task and typically requires labeled data. In this work, we assume that the distribution of distances produced by a siamese verification network can be approximated by a bimodal function. Based on this assumption, we propose an unsupervised method to determine the verification threshold by identifying the minimum point between the two modes. The proposed approach does not require annotated samples, enabling the verification threshold to be updated directly in the deployment environment without the cost of manual labeling. We evaluate our method on four datasets: MNIST, CIFAR-10, LFW, and PKLot. The results indicate that the proposed approach achieves an average verification accuracy of 94%, comparable to the Equal Error Rate method, while eliminating the need for labeled data.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
#### 1. Bimodal Function Assumption
- Equation: Not explicitly provided
- Symbols: Not explicitly provided
- Why it matters: The authors assume that the distribution of distances produced by a siamese verification network can be approximated by a bimodal function, which is used to determine the verification threshold.

#### 2. Verification Threshold Definition
- Equation: Not explicitly provided
- Symbols: Not explicitly provided
- Why it matters: The verification threshold is defined as the minimum point between the two modes of the bimodal function, which separates similar objects from dissimilar ones.

#### 3. Distance Threshold
- Equation: Not explicitly provided
- Symbols: Not explicitly provided
- Why it matters: The distance threshold is the value below which two objects are considered to belong to the same class, and the authors propose an unsupervised method to determine this threshold.

#### 4. Equal Error Rate (EER) Method
- Equation: Not explicitly provided
- Symbols: Not explicitly provided
- Why it matters: The authors compare their proposed approach with the EER method, which is a baseline for verifying the performance of siamese verification networks.

#### 5. Verification Accuracy
- Equation: Not explicitly provided
- Symbols: Not explicitly provided
- Why it matters: The authors report an average verification accuracy of 94% for their proposed approach, which is comparable to the EER method.

### Method Summary
- The authors propose an unsupervised method to determine the verification threshold for siamese verification networks.
- The method assumes that the distribution of distances produced by a siamese verification network can be approximated by a bimodal function.
- The verification threshold is defined as the minimum point between the two modes of the bimodal function.
- The proposed approach does not require annotated samples, enabling the verification threshold to be updated directly in the deployment environment.

### Experimental Overview
- Tasks/Datasets: The authors evaluate their proposed approach on four datasets: MNIST, CIFAR-10, LFW, and PKLot.
- Baselines/Comparisons: The authors compare their proposed approach with the Equal Error Rate (EER) method.
- Main Claimed Findings: The proposed approach achieves an average verification accuracy of 94%, comparable to the EER method, while eliminating the need for labeled data.

### What to Verify in the PDF
- The mathematical formulation of the bimodal function assumption and its implications on the verification threshold.
- The evaluation metrics used to measure the performance of the proposed approach.
- The details of the four datasets used for evaluation, including their characteristics and challenges.
{% endraw %}
