---
layout: post
title: "Daily arXiv Digest — 2026-04-21 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval
- **Authors:** Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman, Antonio Torralba
- **arXiv:** [2604.18584](https://arxiv.org/abs/2604.18584v1) · [pdf](https://arxiv.org/pdf/2604.18584v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.18584v1))
- **Categories:** cs.AI, cs.DL, cs.IR, cs.LG

### Abstract
> Mathematical problem solving remains a challenging test of reasoning for large language and multimodal models, yet existing benchmarks are limited in size, language coverage, and task diversity. We introduce MathNet, a high-quality, large-scale, multimodal, and multilingual dataset of Olympiad-level math problems together with a benchmark for evaluating mathematical reasoning in generative models and mathematical retrieval in embedding-based systems. MathNet spans 47 countries, 17 languages, and two decades of competitions, comprising 30,676 expert-authored problems with solutions across diverse domains. In addition to the core dataset, we construct a retrieval benchmark consisting of mathematically equivalent and structurally similar problem pairs curated by human experts. MathNet supports three tasks: (i) Problem Solving, (ii) Math-Aware Retrieval, and (iii) Retrieval-Augmented Problem Solving. Experimental results show that even state-of-the-art reasoning models (78.4% for Gemini-3.1-Pro and 69.3% for GPT-5) remain challenged, while embedding models struggle to retrieve equivalent problems. We further show that retrieval-augmented generation performance is highly sensitive to retrieval quality; for example, DeepSeek-V3.2-Speciale achieves gains of up to 12%, obtaining the highest scores on the benchmark. MathNet provides the largest high-quality Olympiad dataset together with the first benchmark for evaluating mathematical problem retrieval, and we publicly release both the dataset and benchmark at https://mathnet.mit.edu.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: $x^{2}+y^{2}=1$

* Equation: $x^{2}+y^{2}=1$
* Symbols: $x$, $y$
* Why it matters: This equation represents a circle with radius 1 centered at the origin (0,0) in the Cartesian coordinate system. It is a fundamental concept in geometry and is often used to describe the shape of a circle.

### Equation 2: $\sqrt{a^{2}+b^{2}}=1$

* Equation: $\sqrt{a^{2}+b^{2}}=1$
* Symbols: $a$, $b$
* Why it matters: This equation represents the Pythagorean theorem, which is a fundamental concept in geometry and is used to calculate the length of the hypotenuse of a right-angled triangle.

### Equation 3: $|u|^{2}=1$

* Equation: $|u|^{2}=1$
* Symbols: $u$
* Why it matters: This equation represents the definition of a unit vector, which is a vector with a magnitude of 1. It is often used in physics and engineering to describe the direction and magnitude of a vector.

### Equation 4: $x+y=1$

* Equation: $x+y=1$
* Symbols: $x$, $y$
* Why it matters: This equation represents a line with a slope of -1 and a y-intercept of 1. It is a fundamental concept in algebra and is often used to describe linear relationships.

### Equation 5: $p_{n+1}-p_{n}\leq C(\log p_{n})^{2}$

* Equation: $p_{n+1}-p_{n}\leq C(\log p_{n})^{2}$
* Symbols: $p_{n}$, $C$
* Why it matters: This equation represents a bound on the difference between consecutive probabilities, which is often used in optimization and machine learning to ensure that the probabilities are non-increasing.

**Method Summary**
================

* **Dataset**: MathNet is a large-scale, multimodal, and multilingual dataset of Olympiad-level math problems with solutions.
* **Benchmark**: The dataset includes three tasks: Problem Solving accuracy on MathNet-Solve, Math-Aware Retrieval using Recall@k on MathNet-Retrieve, and Retrieval-Augmented Problem Solving accuracy on MathNet-RAG.
* **Models**: The paper evaluates 27 models, including LLMs and LMMs, on the three tasks.
* **Findings**: The paper reports that the strongest overall model is gemini-3.1-pro, which achieves 76.3% overall accuracy, followed by gemini-2.5-pro and gpt-5.

**Experimental Overview**
=====================

* **Tasks/Datasets**: The paper evaluates models on three tasks: Problem Solving accuracy on MathNet-Solve, Math-Aware Retrieval using Recall@k on MathNet-Retrieve, and Retrieval-Augmented Problem Solving accuracy on MathNet-RAG.
* **Baselines/Comparisons**: The paper compares the performance of 27 models, including LLMs and LMMs, on the three tasks.
* **Main Claimed Findings**: The paper reports that Olympiad-level mathematical reasoning remains challenging even for state-of-the-art systems, with the largest appearing in Geometry and Discrete Mathematics.

**What to Verify in the PDF**
==========================

* **Detailed analysis of the dataset**: The paper mentions that the dataset spans 47 countries, 17 languages, and two decades of competitions, but it would be interesting to see a more detailed analysis of the dataset, including the distribution of problems across different domains and languages.
* **Evaluation protocol**: The paper uses a score-based model grading procedure, but it would be interesting to see more details on how this protocol was developed and validated.
* **Robustness of the results**: The paper reports that the strongest model is gemini-3.1-pro, but it would be interesting to see more analysis on the robustness of the results across different models and tasks.
{% endraw %}

{% raw %}
## 2) Sessa: Selective State Space Attention
- **Authors:** Liubomyr Horbatko
- **arXiv:** [2604.18580](https://arxiv.org/abs/2604.18580v1) · [pdf](https://arxiv.org/pdf/2604.18580v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.18580v1))
- **Categories:** cs.LG, cs.AI, cs.CL

### Abstract
> Modern sequence models are dominated by Transformers, where self-attention mixes information from the visible context in an input-dependent way. However, when retrieval is not sharp and attention remains diffuse over an effective support $S_{\mathrm{eff}}(t)$, the influence of any individual token is diluted, typically scaling as $O(1/S_{\mathrm{eff}}(t))$ and reaching $O(1/\ell)$ for old tokens in full-prefix settings. Structured state-space models process sequences recurrently through an explicit feedback path; selective variants such as Mamba make this feedback input-dependent, yet when freeze time cannot be sustained over long intervals, their long-range sensitivity decays exponentially with lag. Existing architectures therefore either retrieve from the past in a single read or propagate information through a single feedback chain. We introduce Sessa, a decoder that places attention inside a feedback path, enabling recurrent many-path aggregation within a layer. Under stated assumptions, Sessa admits regimes with a power-law memory tail in lag $\ell$ of order $O(\ell^{-β})$ for $0<β<1$, which is asymptotically slower than $1/\ell$; moreover, this rate is tight in an explicit diffuse uniform-routing setting where the influence is $Θ(\ell^{-β})$. Under the same conditions, only Sessa among the compared model classes realizes flexible selective retrieval, including non-decaying profiles. Empirically, under matched architectures and training budgets, Sessa achieves the strongest performance on our long-context benchmarks while remaining competitive with Transformer and Mamba style baselines on short-context language modeling.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: $S_{\mathrm{eff}}(t)$

* Equation: Not provided in the extracted context.
* Symbols: Not provided in the extracted context.
* Why it matters: Not found in extracted context.

### Equation 2: $O(1/S_{\mathrm{eff}}(t))$

* Equation: Not provided in the extracted context.
* Symbols: Not provided in the extracted context.
* Why it matters: Not found in extracted context.

### Equation 3: $O(1/\ell)$

* Equation: Not provided in the extracted context.
* Symbols: Not provided in the extracted context.
* Why it matters: Not found in extracted context.

### Equation 4: $\ell$

* Equation: Not provided in the extracted context.
* Symbols: Not provided in the extracted context.
* Why it matters: Not found in extracted context.

### Equation 5: $O(\ell^{-\beta})$

* Equation: Not provided in the extracted context.
* Symbols: $\ell$, $\beta$
* Why it matters: Describes the memory tail in lag $\ell$ of order $O(\ell^{-\beta})$, which is asymptotically slower than $1/\ell$.

### Equation 6: $0 < \beta < 1$

* Equation: Not provided in the extracted context.
* Symbols: $\beta$
* Why it matters: Bounds the value of $\beta$, which affects the memory tail.

### Equation 7: $1/\ell$

* Equation: Not provided in the extracted context.
* Symbols: $\ell$
* Why it matters: Serves as a baseline for comparison with the memory tail.

### Equation 8: $\Theta(\ell^{-\beta})$

* Equation: Not provided in the extracted context.
* Symbols: $\ell$, $\beta$
* Why it matters: Describes the tightness of the memory tail in an explicit diffuse uniform-routing setting.

**Method Summary**
================

* Sessa introduces a decoder that places attention inside a feedback path, enabling recurrent many-path aggregation within a layer.
* The model admits regimes with a power-law memory tail in lag $\ell$ of order $O(\ell^{-\beta})$ for $0 < \beta < 1$.
* Sessa achieves flexible selective retrieval, including non-decaying profiles.
* The model is compared to Transformer and Mamba style baselines.

**Experimental Overview**
=====================

* Tasks: Long-context behavior on SymbolSoup and Diffuse MQAR, short-context language modeling on SimpleStories.
* Baselines: Multi-head self-attention and Mamba2 mixer.
* Main claimed findings: Sessa achieves the strongest performance on long-context benchmarks while remaining competitive with Transformer and Mamba style baselines.

**What to Verify in the PDF**
=========================

* The mathematical derivation of the memory tail in lag $\ell$ of order $O(\ell^{-\beta})$.
* The explicit diffuse uniform-routing setting and its implications on the memory tail.
* The comparison of Sessa with other models on the full Long Range Arena (LRA) suite.
{% endraw %}

{% raw %}
## 3) Bounded Ratio Reinforcement Learning
- **Authors:** Yunke Ao, Le Chen, Bruce D. Lee, Assefa S. Wahd, Aline Czarnobai, Philipp Fürnstahl, Bernhard Schölkopf, Andreas Krause
- **arXiv:** [2604.18578](https://arxiv.org/abs/2604.18578v1) · [pdf](https://arxiv.org/pdf/2604.18578v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.18578v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a significant disconnect between the underlying foundations of trust region methods and the heuristic clipped objective used in PPO. In this paper, we bridge this gap by introducing the Bounded Ratio Reinforcement Learning (BRRL) framework. We formulate a novel regularized and constrained policy optimization problem and derive its analytical optimal solution. We prove that this solution ensures monotonic performance improvement. To handle parameterized policy classes, we develop a policy optimization algorithm called Bounded Policy Optimization (BPO) that minimizes an advantage-weighted divergence between the policy and the analytic optimal solution from BRRL. We further establish a lower bound on the expected performance of the resulting policy in terms of the BPO loss function. Notably, our framework also provides a new theoretical lens to interpret the success of the PPO loss, and connects trust region policy optimization and the Cross-Entropy Method (CEM). We additionally extend BPO to Group-relative BPO (GBPO) for LLM fine-tuning. Empirical evaluations of BPO across MuJoCo, Atari, and complex IsaacLab environments (e.g., Humanoid locomotion), and of GBPO for LLM fine-tuning tasks, demonstrate that BPO and GBPO generally match or outperform PPO and GRPO in stability and final performance.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: (\mathcal{S},\mathcal{A},\mathcal{P},r,d,\gamma)

* Equation: (\mathcal{S},\mathcal{A},\mathcal{P},r,d,\gamma)
* Symbols:
	+ \mathcal{S}: State space
	+ \mathcal{A}: Action space
	+ \mathcal{P}: Transition model
	+ r: Reward function
	+ d: Discount factor
	+ \gamma: Discount factor
* Why it matters: This equation defines the basic components of a Markov Decision Process (MDP), which is the foundation of reinforcement learning.

### Equation 2: \mathcal{S}

* Equation: \mathcal{S}
* Symbols: None
* Why it matters: This equation is not explicitly defined in the context, but it is likely referring to the state space \mathcal{S} of the MDP.

### Equation 3: \mathcal{A}

* Equation: \mathcal{A}
* Symbols: None
* Why it matters: This equation is not explicitly defined in the context, but it is likely referring to the action space \mathcal{A} of the MDP.

### Equation 4: \mathcal{P}:\mathcal{S}\times\mathcal{A}\times\mathcal{S}\rightarrow\mathbb{R}

* Equation: \mathcal{P}:\mathcal{S}\times\mathcal{A}\times\mathcal{S}\rightarrow\mathbb{R}
* Symbols:
	+ \mathcal{P}: Transition model
	+ \mathcal{S}: State space
	+ \mathcal{A}: Action space
	+ \mathbb{R}: Real numbers
* Why it matters: This equation defines the transition model \mathcal{P} that takes in a state-action-state triplet and returns a real-valued reward.

### Equation 5: r:\mathcal{S}\times\mathcal{A}\times\mathcal{S}\rightarrow\mathbb{R}

* Equation: r:\mathcal{S}\times\mathcal{A}\times\mathcal{S}\rightarrow\mathbb{R}
* Symbols:
	+ r: Reward function
	+ \mathcal{S}: State space
	+ \mathcal{A}: Action space
	+ \mathbb{R}: Real numbers
* Why it matters: This equation defines the reward function r that takes in a state-action-state triplet and returns a real-valued reward.

### Equation 6: d_{0}:\mathcal{S}\rightarrow\mathbb{R}

* Equation: d_{0}:\mathcal{S}\rightarrow\mathbb{R}
* Symbols:
	+ d_{0}: Discount factor
	+ \mathcal{S}: State space
	+ \mathbb{R}: Real numbers
* Why it matters: This equation defines the discount factor d_{0} that is used to discount future rewards.

### Equation 7: \gamma\in(0,1)

* Equation: \gamma\in(0,1)
* Symbols:
	+ \gamma: Discount factor
* Why it matters: This equation defines the range of the discount factor \gamma, which is a hyperparameter that controls the trade-off between immediate and future rewards.

### Equation 8: \pi:\mathcal{\mathcal{S}}\times\mathcal{A}\rightarrow\mathbb{R}

* Equation: \pi:\mathcal{\mathcal{S}}\times\mathcal{A}\rightarrow\mathbb{R}
* Symbols:
	+ \pi: Policy
	+ \mathcal{S}: State space
	+ \mathcal{A}: Action space
	+ \mathbb{R}: Real numbers
* Why it matters: This equation defines the policy \pi that maps states to actions.

**Method Summary**
================

* The authors introduce Bounded Ratio Reinforcement Learning (BRRL), a novel framework that bridges the gap between trust region methods and the clipped objective used in Proximal Policy Optimization (PPO).
* BRRL formulates a regularized and constrained policy optimization problem that ensures monotonic performance improvement.
* The authors develop a policy optimization algorithm called Bounded Policy Optimization (BPO) that minimizes an advantage-weighted divergence between the policy and the analytic optimal solution from BRRL.
* BPO is shown to outperform PPO and Generalized Ratios Policy Optimization (GRPO) in various environments, including MuJoCo and Atari benchmarks.

**Experimental Overview**
=====================

* The authors evaluate BPO and PPO on various tasks and datasets, including:
	+ MuJoCo environments (e.g., Ant-v4, Hopper-v4, Humanoid-v4)
	+ Atari environments (e.g., Asterix)
	+ IsaacLab environments (e.g., Go1-rough, Anymal-C-rough, G1-rough, H1-rough)
* The authors compare BPO to PPO, GRPO, and Soft Actor-Critic (SAC) on these tasks.
* The main claimed findings include:
	+ BPO outperforms PPO and GRPO in various environments.
	+ BPO exhibits enhanced training stability and smoother dynamics compared to PPO.
	+ BPO is highly effective in complex robotic locomotion tasks.

**What to Verify in the PDF**
==========================

* The authors mention that the value function is not explicitly defined in the context, but it is likely referring to the value function used in the policy optimization algorithm. Verify the definition of the value function and its role in the algorithm.
* The authors also mention that the loss function is not explicitly defined in the context. Verify the definition of the loss function and its role in the algorithm.
* The authors mention that the λ parameter is not explicitly defined in the context. Verify the definition of the λ parameter and its role in the algorithm.
* The authors mention that the TV loss coefficient is not explicitly defined in the context. Verify the definition of the TV loss coefficient and its role in the algorithm.
{% endraw %}

{% raw %}
## 4) When Can LLMs Learn to Reason with Weak Supervision?
- **Authors:** Salman Rahman, Jingyan Shen, Anna Mordvina, Hamid Palangi, Saadia Gabriel, Pavel Izmailov
- **arXiv:** [2604.18574](https://arxiv.org/abs/2604.18574v1) · [pdf](https://arxiv.org/pdf/2604.18574v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.18574v1))
- **Categories:** cs.LG, cs.AI

### Abstract
> Large language models have achieved significant reasoning improvements through reinforcement learning with verifiable rewards (RLVR). Yet as model capabilities grow, constructing high-quality reward signals becomes increasingly difficult, making it essential to understand when RLVR can succeed under weaker forms of supervision. We conduct a systematic empirical study across diverse model families and reasoning domains under three weak supervision settings: scarce data, noisy rewards, and self-supervised proxy rewards. We find that generalization is governed by training reward saturation dynamics: models that generalize exhibit a prolonged pre-saturation phase during which training reward and downstream performance climb together, while models that saturate rapidly memorize rather than learn. We identify reasoning faithfulness, defined as the extent to which intermediate steps logically support the final answer, as the pre-RL property that predicts which regime a model falls into, while output diversity alone is uninformative. Motivated by these findings, we disentangle the contributions of continual pre-training and supervised fine-tuning, finding that SFT on explicit reasoning traces is necessary for generalization under weak supervision, while continual pre-training on domain data amplifies the effect. Applied together to Llama3.2-3B-Base, these interventions enable generalization across all three settings where the base model previously failed.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: `solve}@16 ∈ [0,16]`

* Equation: `solve}@16 ∈ [0,16]`
* Symbols: `solve` (a function or operation), `@16` (a notation indicating the output is evaluated at 16), `∈` (subset notation)
* Why it matters: This equation represents a condition where the output of the `solve` function is evaluated at 16 and is within the range [0,16]. This equation is likely used to evaluate the performance of the model on a specific task.

### Equation 2: `solve}@16 ∈ [1,15]`

* Equation: `solve}@16 ∈ [1,15]`
* Symbols: `solve` (a function or operation), `@16` (a notation indicating the output is evaluated at 16), `∈` (subset notation)
* Why it matters: This equation is similar to Equation 1, but with a different range [1,15]. This equation is likely used to evaluate the performance of the model on a specific task with a different condition.

### Equation 3: `avg@16`

* Equation: `avg@16`
* Symbols: `avg` (average), `@16` (a notation indicating the output is evaluated at 16)
* Why it matters: This equation represents the average performance of the model on a specific task, evaluated at 16. This equation is likely used to evaluate the overall performance of the model.

### Equation 4: `N_{max}`

* Equation: `N_{max}`
* Symbols: `N_{max}` (a variable representing the maximum number)
* Why it matters: This equation is not explicitly defined in the context, but it is likely used to represent a maximum value or a limit.

### Equation 5: `N_{max} = 2048`

* Equation: `N_{max} = 2048`
* Symbols: `N_{max}` (a variable representing the maximum number), `= 2048` (an equality statement)
* Why it matters: This equation sets the value of `N_{max}` to 2048, which is likely used to define a limit or a maximum value.

### Equation 6: `N_{max} = 882`

* Equation: `N_{max} = 882`
* Symbols: `N_{max}` (a variable representing the maximum number), `= 882` (an equality statement)
* Why it matters: This equation sets the value of `N_{max}` to 882, which is likely used to define a limit or a maximum value.

### Equation 7: `N_{max} = 256`

* Equation: `N_{max} = 256`
* Symbols: `N_{max}` (a variable representing the maximum number), `= 256` (an equality statement)
* Why it matters: This equation sets the value of `N_{max}` to 256, which is likely used to define a limit or a maximum value.

**Method Summary**
==================

* The authors evaluate the performance of large language models (LLMs) under weak supervision using reinforcement learning with verifiable rewards (RLVR).
* The authors investigate three weak supervision settings: scarce data, noisy rewards, and self-supervised proxy rewards.
* The authors analyze the behavior of LLMs under these conditions and identify the importance of reasoning faithfulness, which is the extent to which a model's intermediate steps logically support its final answer.
* The authors find that generalization is governed by training reward saturation dynamics, and that models that generalize exhibit a prolonged pre-saturation phase during which training reward and downstream performance climb together.

**Experimental Overview**
========================

* The authors evaluate the performance of five pre-RL configurations (Base, CPT, and Instruct, with Thinking SFT or Non-Thinking SFT applied to Base and CPT) across three weak supervision settings (scarce data, noisy rewards, and self-supervised proxy rewards).
* The authors use three domains (Math, Science, and Graph) and three model families (Qwen, Llama, and Qwen-Math).
* The authors report that Thinking SFT is necessary for substantial learning under weak supervision, and that Non-Thinking SFT shows modest gains only when paired with CPT.

**What to Verify in the PDF**
=============================

* The authors mention that the full paper provides more details on the implementation of the evaluation metrics, including the specific domains and datasets used.
* The authors also mention that the full paper provides more details on the results of the experiments, including the pass@k results for k ∈ {4, 8, 16}.
* The authors mention that the full paper provides more details on the analysis of the policy behavior under weak supervision, including the analysis of the GRPO baseline selection.
{% endraw %}

{% raw %}
## 5) Back into Plato's Cave: Examining Cross-modal Representational Convergence at Scale
- **Authors:** A. Sophia Koepke, Daniil Zverev, Shiry Ginosar, Alexei A. Efros
- **arXiv:** [2604.18572](https://arxiv.org/abs/2604.18572v1) · [pdf](https://arxiv.org/pdf/2604.18572v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2604.18572v1))
- **Categories:** cs.CV, cs.AI, cs.LG

### Abstract
> The Platonic Representation Hypothesis suggests that neural networks trained on different modalities (e.g., text and images) align and eventually converge toward the same representation of reality. If true, this has significant implications for whether modality choice matters at all. We show that the experimental evidence for this hypothesis is fragile and depends critically on the evaluation regime. Alignment is measured using mutual nearest neighbors on small datasets ($\approx$1K samples) and degrades substantially as the dataset is scaled to millions of samples. The alignment that remains between model representations reflects coarse semantic overlap rather than consistent fine-grained structure. Moreover, the evaluations in Huh et al. are done in a one-to-one image-caption setting, a constraint that breaks down in realistic many-to-many settings and further reduces alignment. We also find that the reported trend of stronger language models increasingly aligning with vision does not appear to hold for newer models. Overall, our findings suggest that the current evidence for cross-modal representational convergence is considerably weaker than subsequent works have taken it to be. Models trained on different modalities may learn equally rich representations of the world, just not the same one.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 
\[\mathbf{a_{i}}\in\mathbb{R}^{d_{1}}\]

*   Symbols: \(\mathbf{a_{i}}\) (feature vector of the i-th sample)
*   Why it matters: This equation defines the domain of the feature vector \(\mathbf{a_{i}}\), which is a real-valued vector of length \(d_{1}\).

### Equation 2: 
\[1024\]

*   Symbols: None
*   Why it matters: This equation is a constant value, but its significance is not explicitly stated in the context. It may be related to the size of the dataset or the number of samples.

### Equation 3: 
\[\mathbf{b_{i}}\in\mathbb{R}^{d_{2}}\]

*   Symbols: \(\mathbf{b_{i}}\) (feature vector of the i-th sample)
*   Why it matters: This equation defines the domain of the feature vector \(\mathbf{b_{i}}\), which is a real-valued vector of length \(d_{2}\).

### Equation 4: 
\[i\in\{1,\cdots,n\}\]

*   Symbols: i (sample index)
*   Why it matters: This equation defines the domain of the sample index i, which ranges from 1 to n.

### Equation 5: 
\[\mathcal{N}^{\mathbf{a}}_{k}(i)=\operatorname{argtopk}_{j\neq i}\mathbf{a}_{i}^{\top}\mathbf{a}_{j}\]

*   Symbols: \(\mathcal{N}^{\mathbf{a}}_{k}(i)\) (nearest neighbors of the i-th sample in the a-space), \(\mathbf{a}_{i}^{\top}\mathbf{a}_{j}\) (dot product of the i-th and j-th feature vectors)
*   Why it matters: This equation defines the nearest neighbors of the i-th sample in the a-space, which is used to compute the mutual nearest neighbors metric.

### Equation 6: 
\[\mathcal{N}^{\mathbf{b}}_{k}(i)=\operatorname{argtopk}_{j\neq i}\mathbf{b}_{i}^{\top}\mathbf{b}_{j}\]

*   Symbols: \(\mathcal{N}^{\mathbf{b}}_{k}(i)\) (nearest neighbors of the i-th sample in the b-space), \(\mathbf{b}_{i}^{\top}\mathbf{b}_{j}\) (dot product of the i-th and j-th feature vectors)
*   Why it matters: This equation defines the nearest neighbors of the i-th sample in the b-space, which is used to compute the mutual nearest neighbors metric.

### Equation 7: 
\[s_{i}=\frac{|\mathcal{N}^{\mathbf{a}}_{k}(i)\cap\mathcal{N}^{\mathbf{b}}_{k}(i)|}{k}\]

*   Symbols: \(s_{i}\) (score of the i-th sample), \(\mathcal{N}^{\mathbf{a}}_{k}(i)\) (nearest neighbors of the i-th sample in the a-space), \(\mathcal{N}^{\mathbf{b}}_{k}(i)\) (nearest neighbors of the i-th sample in the b-space), k (number of nearest neighbors)
*   Why it matters: This equation defines the score of the i-th sample, which is the number of common nearest neighbors between the a-space and b-space, normalized by the number of nearest neighbors.

### Equation 8: 
\[k=1\]

*   Symbols: k (number of nearest neighbors)
*   Why it matters: This equation defines the value of k, which is used to compute the mutual nearest neighbors metric.

**Method Summary**
==================

*   The authors use the mutual k-nearest neighbors (k-NN) metric to measure the alignment between representations from different models.
*   The k-NN metric is computed using the dot product of feature vectors and the number of nearest neighbors is normalized by k.
*   The authors use L2-normalization to ensure that the feature vectors have unit length.
*   The authors use a shared gallery set of n datapoints, encoded into feature vectors, to compute the mutual k-NN metric.

**Experimental Overview**
========================

*   The authors use the ImageNet validation set to evaluate the performance of their method.
*   The authors compare their method to a baseline that uses individual retrieval accuracy.
*   The authors find that the mutual k-NN metric does not capture the same level of cross-modal alignment as individual retrieval accuracy.
*   The authors also find that the ImageNet validation set provides a denser retrieval setting than the WIT-1024 and WIT-1M datasets.

**What to Verify in the PDF**
==========================

*   The authors mention that the ImageNet validation set serves as a suitable test bed, but it would be interesting to see how the results generalize to other datasets.
*   The authors also mention that the WIT-1024 and WIT-1M datasets provide a denser retrieval setting than the ImageNet validation set, but it would be interesting to see how the results change when using these datasets.
*   The authors use a strict setting for k=1, but it would be interesting to see how the results change when using different values of k.
{% endraw %}
