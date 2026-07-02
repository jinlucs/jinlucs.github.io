---
layout: post
title: "Daily arXiv Digest — 2026-07-02 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) The State-Prediction Separation Hypothesis
- **Authors:** Giovanni Monea, Nathan Godey, Kianté Brantley, Yoav Artzi
- **arXiv:** [2607.01218](https://arxiv.org/abs/2607.01218v1) · [pdf](https://arxiv.org/pdf/2607.01218v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.01218v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> Transformers use the same forward computation stream to both predict the next token and store useful state for future token predictions. We formulate the \emph{state-prediction separation hypothesis}: disentangling the two roles yields better language modeling performance. We design a Transformer variant that uses two computation streams to separate the two functions, and conduct pretraining experiments across various scales. Our experiments show that state-prediction separation consistently offers better data and compute efficiencies, improving validation loss and outperforming standard Transformers by 2--3 percentage points on average on downstream tasks. We also conduct extensive empirical analysis that rules out potential confounders and demonstrates the fundamental difference in the gradients our design entails.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: `x_i`

* Equation: `x_i`
* Symbols: `x_i` (input token)
* Why it matters: This equation represents the input token at position `i` in the sequence.

### Equation 2: `\rho_i`

* Equation: `\rho_i`
* Symbols: `\rho_i` (predict token)
* Why it matters: This equation represents the predict token at position `i` in the sequence.

### Equation 3: `2.6\times`

* Equation: `2.6\times`
* Symbols: `2.6` (constant)
* Why it matters: This equation is not explicitly used in the paper, but it is mentioned as a constant value.

### Equation 4: `\Delta\mathrm{NLL}=-0.071`

* Equation: `\Delta\mathrm{NLL}=-0.071`
* Symbols: `\Delta\mathrm{NLL}` (change in NLL), `-0.071` (value)
* Why it matters: This equation represents the change in negative log likelihood (NLL) between the SPS and Standard models.

### Equation 5: `\theta`

* Equation: `\theta`
* Symbols: `\theta` (model parameters)
* Why it matters: This equation represents the model parameters used in the SPS and Standard models.

**Method Summary**
================

* The SPS (State-Prediction Separation Hypothesis) model separates the state-prediction roles into two computation streams.
* The model uses two computation streams to disentangle the two roles, which yields better language modeling performance.
* The SPS model is compared to a standard Transformer (Standard) and two ablations: 2x Memory and Delayed State.

**Experimental Overview**
=====================

* Tasks/Datasets: The paper evaluates the SPS model on various downstream tasks, including FineWeb-Edu, WikiText, C4, Pile-Books3, GovReport, ARC-Easy, HellaSwag, PIQA, SciQ, and LAMBADA.
* Baselines/Comparisons: The paper compares the SPS model to a standard Transformer (Standard) and two ablations: 2x Memory and Delayed State.
* Main Claimed Findings: The SPS model outperforms the Standard model on validation loss and generalization, and achieves minimal increase in inference cost.

**What to Verify in the PDF**
==========================

* The paper mentions that the results are verified with a 3-3 seed sweep at S, 10 10 B, but it would be useful to see the detailed results of this sweep.
* The paper also mentions that the gap between SPS and Standard is significant at p < 0.005, but it would be useful to see the detailed analysis of this result.
* The paper does not provide a detailed analysis of the inference efficiency of the 2x Memory and Delayed State models, which would be useful to understand the trade-offs between these models and SPS.
{% endraw %}

{% raw %}
## 2) Language-Critique Imitation Learning from Suboptimal Demonstrations
- **Authors:** Chih-Han Yang, Dai-Jie Wu, Yun-Ping Huang, Ping-Chun Hsieh, Kenneth Marino, Shao-Hua Sun
- **arXiv:** [2607.01225](https://arxiv.org/abs/2607.01225v1) · [pdf](https://arxiv.org/pdf/2607.01225v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.01225v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Prior work on imitation learning from suboptimal demonstrations typically relies on compressed supervision signals such as confidence estimates, discriminator scores, or importance weights. These scalar signals are inherently limited, as they cannot explicitly express intermediate reasoning about task progress, failure modes, or corrective actions. We propose a language-critique framework for imitation learning from suboptimal demonstrations that instead leverages natural language as a structured supervision signal, avoiding the collapse of expressive feedback into scalars. Our method first constructs language labels from demonstrations that explicitly describe current progress, identify suboptimal behaviors, and provide fine-grained corrective guidance. We then introduce a language-critique loss that directly trains policies using these structured signals without reducing them to scalars, and instantiate it for both behavior cloning and diffusion policies, yielding LC-BC and LC-DP. We further provide a theoretical result showing that the proposed objective upper-bounds the expert performance gap under standard assumptions. Empirically, we evaluate on diverse continuous control tasks spanning navigation, manipulation, and gameplay, where our methods consistently outperform strong imitation learning and offline reinforcement learning baselines. These results demonstrate that language can serve as a powerful and structured form of supervision for learning robust policies from suboptimal data.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: M
```markdown
\mathcal{M} := (\mathcal{S}, \mathcal{A}, P, r, \rho_{0}, \gamma, T)
```
* Symbols: $\mathcal{M}$, $\mathcal{S}$, $\mathcal{A}$, $P$, $r$, $\rho_{0}$, $\gamma$, $T$
* Why it matters: This equation defines the Markov Decision Process (MDP) environment, which is the foundation of reinforcement learning.

### Equation 2: \mathcal{S}
```markdown
\mathcal{S}
```
* Symbols: $\mathcal{S}$
* Why it matters: This equation is not explicitly defined in the context, but it likely represents the state space of the MDP environment.

### Equation 3: \mathcal{A}
```markdown
\mathcal{A}
```
* Symbols: $\mathcal{A}$
* Why it matters: This equation is not explicitly defined in the context, but it likely represents the action space of the MDP environment.

### Equation 4: P(s' | s, a)
```markdown
P(s' | s, a) := Q_r, t π (s, a) - V_r, t π (s)
```
* Symbols: $P(s' | s, a)$, $Q_r, t π (s, a)$, $V_r, t π (s)$
* Why it matters: This equation defines the transition model, which describes the probability of moving from one state to another given the current state and action.

### Equation 5: r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}
```markdown
r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}
```
* Symbols: $r$, $\mathcal{S}$, $\mathcal{A}$
* Why it matters: This equation defines the reward function, which measures the desirability of taking a particular action in a given state.

**Method Summary**
==================

* The proposed method, Language-Critique Imitation Learning, uses natural language as a structured supervision signal to learn policies from suboptimal demonstrations.
* The method consists of two main components:
	+ A language label generator that produces structured labels from demonstrations.
	+ A language-critique loss function that trains policies using these structured labels.
* The method is instantiated for both behavior cloning and diffusion policies.

**Experimental Overview**
========================

* The experiments evaluate the proposed method on diverse continuous-control environments, including navigation, driving, and manipulation tasks.
* The method is compared to strong imitation learning and offline reinforcement learning baselines.
* The main claimed findings are:
	+ The proposed method consistently outperforms baselines on all tasks.
	+ The method is particularly effective on complex manipulation tasks.

**What to Verify in the PDF**
=============================

* The theoretical analysis in Section A.1 provides a formal definition of the expert-state language-critique objective.
* The ablation studies in Section I.2 investigate the impact of different LLM-Captioner backbones and finetuning regimes on the performance of the proposed method.
* The experimental results in Section 5 provide a comprehensive evaluation of the proposed method on various tasks and baselines.
{% endraw %}

{% raw %}
## 3) Theoria: Rewrite-Acceptability Verification over Informal Reasoning States
- **Authors:** Ben Slivinski, Michael Saldivar
- **arXiv:** [2607.01223](https://arxiv.org/abs/2607.01223v1) · [pdf](https://arxiv.org/pdf/2607.01223v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.01223v1))
- **Categories:** cs.AI, cs.CL, cs.LG, cs.LO, cs.SE

### Abstract
> When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a citation, computation, or problem-given fact, and every transition is independently auditable. The foundational invariant is completeness of change: every difference between consecutive proof states must be accounted for, so hidden premises surface as unlicensed mutations rather than passing silently. On HLE-Verified Gold (185 text-only expert problems), Theoria certifies 105 at 91.4% strict precision (Wilson 95% CI [84.5%, 95.4%]). Every certification produces a human readable proof trace in which each step can be independently challenged. Holistic LLM judges achieve comparable precision at matched coverage but fail on different problems (Jaccard 0.14-0.36), making the approaches complementary. On 95 adversarial poisoned proofs across 15 domains, structured judges catch 94.7% versus 83.2% for holistic judging (p= 0.0017). The overall 11.5 pp gap concentrates in hidden premises (90.6% vs. 62.5%, a 28 pp difference) and fabricated citations (100% vs. 90%), the error classes where the formal analysis predicts an advantage; performance is identical on arithmetic and theorem-misapplication errors, where no advantage is predicted. On GPQA Diamond (n= 65), certified precision is 97.1% (Wilson CI [85.1%, 99.5%]).
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: p = 0.0017

* Equation: `p = 0.0017`
* Symbols: `p` (probability), `0.0017` (value)
* Why it matters: This equation represents the Jaccard index between Theoria and holistic judging, indicating the similarity between their error sets.

### Equation 2: n = 65

* Equation: `n = 65`
* Symbols: `n` (number), `65` (value)
* Why it matters: This equation represents the number of problems used in the evaluation set.

### Equation 3: S_{0}

* Equation: `S_{0}`
* Symbols: `S_{0}` (state), subscript indicating initial state
* Why it matters: This equation represents the initial state of the system, which is not explicitly defined in the context.

### Equation 4: (S_{1},\tau_{1},e_{1}),(S_{2},\tau_{2},e_{2}),\dots,(S_{n},\tau_{n},e_{n})

* Equation: `(S_{1},\tau_{1},e_{1}),(S_{2},\tau_{2},e_{2}),\dots,(S_{n},\tau_{n},e_{n})`
* Symbols: `(S_{i},\tau_{i},e_{i})` (state, transition, error), `n` (number of problems)
* Why it matters: This equation represents the sequence of state transitions and errors for each problem, which is used to verify the correctness of the system.

### Equation 5: S_{i}

* Equation: `S_{i}`
* Symbols: `S_{i}` (state), subscript indicating the current state
* Why it matters: This equation represents the current state of the system, which is used to verify the correctness of the system.

### Equation 6: (S_{i},\tau_{i},e_{i})

* Equation: `(S_{i},\tau_{i},e_{i})`
* Symbols: `(S_{i},\tau_{i},e_{i})` (state, transition, error)
* Why it matters: This equation represents the current state, transition, and error for each problem, which is used to verify the correctness of the system.

### Equation 7: S_{i-1}

* Equation: `S_{i-1}`
* Symbols: `S_{i-1}` (state), subscript indicating the previous state
* Why it matters: This equation represents the previous state of the system, which is used to verify the correctness of the system.

**Method Summary**
==================

* Theoria is a verification architecture that uses a sequence of state transitions and errors to verify the correctness of a system.
* The system is composed of a candidate solution that is rewritten into a sequence of typed state transitions, each licensed by an explicit justification.
* The foundational invariant is completeness of change, which ensures that every difference between consecutive proof states is accounted for.
* The system is designed to be auditable, with every transition independently verifiable.

**Experimental Overview**
==========================

* Tasks/Datasets: The evaluation is performed on a random sample of 200 problems from HLE-Verified Gold, a systematic validation of Humanity's Last Exam.
* Baselines/Comparisons: The evaluation is compared to two holistic judges, Claude Opus and GPT-based Codex.
* Main Claimed Findings: Theoria catches 90/95 poisoned proofs (94.7%) versus 79/95 for holistic judging (83.2%), with a 28 percentage-point gap in catching hidden premises.

**What to Verify in the PDF**
=============================

* The definition of the state transitions and errors used in Theoria.
* The explicit justifications used to license each transition.
* The completeness of change invariant and its implications for the system's correctness.
* The evaluation methodology used to compare Theoria to holistic judging.
{% endraw %}

{% raw %}
## 4) Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation
- **Authors:** Shayan Talaei, Abhinav Chinta, Devvrit Khatri, Amin Karbasi, Azalia Mirhoseini, Amin Saberi
- **arXiv:** [2607.01208](https://arxiv.org/abs/2607.01208v1) · [pdf](https://arxiv.org/pdf/2607.01208v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.01208v1))
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, with the signal residing entirely in the soft logit distribution and remaining invisible to text-based inspection. However, the defender faces a fundamental asymmetry: without knowing the bias topic, no detection method can reliably surface a stealth preferential bias, regardless of whether it examines generated text, internal representations, or model weights. Here we introduce Distill to Detect (D2D), a method that surfaces hidden biases by distilling the distributional shift between a suspected model and its base into a cartridge (a KV-cache prefix adapter), concentrating the dominant divergence and amplifying the bias signal into generated text. We show that D2D successfully amplifies the hidden biases of stealth models to the extent that they can be reliably detected across multiple bias types. We also propose a theoretical framework that explains the efficacy of D2D through the lens of Fisher-weighted projection of the logit distribution shift, supported by empirical observations. By turning the capacity bottleneck of prefix-tuning adapters into a detection tool, D2D provides a practical building block for auditing hidden behaviors in deployed language models.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================================

### Equation 1: Logit Shift
\pi_{\theta_{B}}(y\mid x) - \log\pi_{\theta_{0}}(y\mid x) + const

* Symbols: \pi_{\theta_{B}}(y\mid x), \pi_{\theta_{0}}(y\mid x), const
* Why it matters: This equation represents the logit shift between the suspected model \pi_{\theta_{B}} and the base model \pi_{\theta_{0}}.

### Equation 2: Fisher Information Matrix
F_x = diag(\pi_{\theta_{0}}(\cdot\mid x)) - \pi_{\theta_{0}}(\cdot\mid x)\,\pi_{\theta_{0}}(\cdot\mid x)^{\top}

* Symbols: F_x, \pi_{\theta_{0}}(\cdot\mid x)
* Why it matters: This equation represents the Fisher information matrix for the base model \pi_{\theta_{0}}, which is used to analyze the bias concentration.

### Equation 3: Logit Shift Decomposition
\Delta(y,x) = \Delta_{\mathrm{bias}} + \Delta_{\mathrm{res}}

* Symbols: \Delta(y,x), \Delta_{\mathrm{bias}}, \Delta_{\mathrm{res}}
* Why it matters: This equation decomposes the logit shift into two components: the bias component and the residual component.

### Equation 4: Rank of the Logit Shift
k = |\alpha|

* Symbols: k, \alpha
* Why it matters: This equation represents the rank of the logit shift, which is used to analyze the capacity bottleneck of the prefix-tuning adapter.

### Equation 5: Bias Concentration Ratio
|\theta_{0}|

* Symbols: |\theta_{0}|
* Why it matters: This equation represents the bias concentration ratio, which is used to analyze the effectiveness of the Distill to Detect method.

**Method Summary**
=====================

* The Distill to Detect method uses cartridge distillation to amplify the bias in a suspected model, making it detectable.
* The method involves distilling the logit shift between the suspected model and the base model into a cartridge, which is a KV-cache prefix adapter.
* The cartridge is used to amplify the bias signal, making it detectable across multiple bias types.
* The method provides a practical building block for auditing hidden behaviors in deployed language models.

**Experimental Overview**
==========================

* Tasks/Datasets: The experiments involve implanting hidden preferential biases in language models through on-policy context distillation.
* Baselines/Comparisons: The experiments compare the performance of the Distill to Detect method with LoRA and full-model distillation.
* Main Claimed Findings: The Distill to Detect method successfully amplifies the hidden biases of stealth models to reliably detectable levels across multiple bias types.

**What to Verify in the PDF**
=============================

* The theoretical framework that explains the efficacy of the Distill to Detect method through the lens of Fisher-weighted projection of the logit distribution shift.
* The empirical observations that support the theoretical framework.
* The results of the LoRA rank sweep, which shows that the representational alignment between the cartridge parameterization and the bias injection mechanism is a key factor in the method's effectiveness.
{% endraw %}

{% raw %}
## 5) TiRex-2: Generalizing TiRex to Multivariate Data and Streaming
- **Authors:** Patrick Podest, Marco Pichler, Elias Bürger, Levente Zólyomi, Bernhard Voggenberger, Wilhelm Berghammer, Daniel Klotz, Sebastian Böck, Günter Klambauer, Sepp Hochreiter
- **arXiv:** [2607.01204](https://arxiv.org/abs/2607.01204v1) · [pdf](https://arxiv.org/pdf/2607.01204v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.01204v1))
- **Categories:** cs.LG

### Abstract
> We introduce TiRex-2, a recurrent xLSTM-based time series foundation model that generalizes the univariate TiRex to multivariate forecasting with both past and future covariates. Real-world forecasting is inherently sequential: observations arrive continuously, variables evolve jointly, and a subset of covariates is known ahead of time. Existing Transformer-based time series foundation models capture cross-variate dependencies but incur quadratic complexity in context length and require full-history recomputation as new observations arrive. TiRex-2 addresses these limitations through a memory-centric recurrent design that operates at constant per-patch cost under streaming. The model combines a bidirectional time mixer with an asymmetric grouped-attention variate mixer, enabling the integration of future-known covariates while preserving strict causality over target variables. To our knowledge, this is the first time series foundation model that achieves this combination of properties. To support scalable multivariate pretraining, we propose a synthetic coupling pipeline that composes diverse multivariate samples on the fly from large univariate corpora. Empirically, TiRex-2 achieves state-of-the-art zero-shot performance on GIFT-Eval and fev-bench, remains stable when streamed to arbitrary context lengths, and maintains constant inference cost per patch. The model uses 38.4M active parameters in univariate mode, with an additional 44.1M parameters activated for multivariate forecasting.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: V_{\text{tgt}}
```python
V_{\text{tgt}}
```
Symbols: `V_{\text{tgt}}`
Why it matters: This represents the number of target variables in the multivariate time series forecasting problem.

### Equation 2: \mathbf{X}_{\text{tgt}}^{1:T}\in\mathbb{R}^{V_{\text{tgt}}\times T}
```python
\mathbf{X}_{\text{tgt}}^{1:T}\in\mathbb{R}^{V_{\text{tgt}}\times T}
```
Symbols: `V_{\text{tgt}}`, `T`, `X_{\text{tgt}}`
Why it matters: This represents the input data for the target variables, a matrix of shape `(V_{\text{tgt}} x T)` containing the historical values of the target variables.

### Equation 3: V_{\text{pcov}}
```python
V_{\text{pcov}}
```
Symbols: `V_{\text{pcov}}`
Why it matters: This represents the number of past covariates in the multivariate time series forecasting problem.

### Equation 4: \mathbf{X}_{\text{pcov}}^{1:T}\in\mathbb{R}^{V_{\text{pcov}}\times T}
```python
\mathbf{X}_{\text{pcov}}^{1:T}\in\mathbb{R}^{V_{\text{pcov}}\times T}
```
Symbols: `V_{\text{pcov}}`, `T`, `X_{\text{pcov}}`
Why it matters: This represents the input data for the past covariates, a matrix of shape `(V_{\text{pcov}} x T)` containing the historical values of the past covariates.

### Equation 5: V_{\text{fcov}}
```python
V_{\text{fcov}}
```
Symbols: `V_{\text{fcov}}`
Why it matters: This represents the number of future-known covariates in the multivariate time series forecasting problem.

### Equation 6: \mathbf{X}_{\text{fcov}}^{1:T+F}\in\mathbb{R}^{V_{\text{fcov}}\times(T+F)}
```python
\mathbf{X}_{\text{fcov}}^{1:T+F}\in\mathbb{R}^{V_{\text{fcov}}\times(T+F)}
```
Symbols: `V_{\text{fcov}}`, `T`, `F`, `X_{\text{fcov}}`
Why it matters: This represents the input data for the future-known covariates, a matrix of shape `(V_{\text{fcov}} x (T+F))` containing the historical and future values of the future-known covariates.

**Method Summary**
==================

* TiRex-2 is a recurrent xLSTM-based time series foundation model that generalizes the univariate TiRex to multivariate forecasting with both past and future covariates.
* The model combines a bidirectional time mixer with an asymmetric grouped-attention variate mixer, enabling the integration of future-known covariates while preserving strict causality over target variables.
* TiRex-2 addresses the limitations of existing Transformer-based time series foundation models by operating at constant per-patch cost under streaming.

**Experimental Overview**
========================

* Tasks/Datasets: Multivariate time series forecasting on fev-bench and GIFT-Eval.
* Baselines/Comparisons: Chronos-Bolt, Moirai-2, Toto-1.0, Chronos-2, Chronos-2-Synth, PatchTST-FM-r1, FlowState-r1.1, TimesFM-2.5.
* Main Claimed Findings: TiRex-2 achieves state-of-the-art zero-shot performance on fev-bench and GIFT-Eval, remains stable when streamed to arbitrary context lengths, and maintains constant inference cost per patch.

**What to Verify in the PDF**
=============================

* The implementation details of the asymmetric grouped-attention variate mixer.
* The proof that the asymmetric mask together with the forward-only xLSTM on targets and past covariates is sufficient for target-causality (Proposition ˜ 1).
* The counterexample showing that the asymmetric mask is necessary.
* The full hyperparameters and training details for both phases of TiRex-2.
{% endraw %}
