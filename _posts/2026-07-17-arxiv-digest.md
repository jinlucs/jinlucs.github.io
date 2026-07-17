---
layout: post
title: "Daily arXiv Digest — 2026-07-17 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

{% raw %}
## 1) Decoding Market Emotion from Blockchain Activity: A Data-Driven Sentiment Classifier
- **Authors:** Arthur G. Bubolz, Abreu Quevedo, Giancarlo Lucca, Rafael A. Berri, Eduardo Borges, Bruno L. Dalmazo
- **arXiv:** [2607.15258](https://arxiv.org/abs/2607.15258v1) · [pdf](https://arxiv.org/pdf/2607.15258v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.15258v1))
- **Categories:** cs.LG, cs.CE

### Abstract
> The growing use of Bitcoin as a decentralized digital asset and investment tool has sparked strong interest in understanding its market behavior. This study presents a new approach to analyze Bitcoin market sentiment by combining on-chain and financial data with social media posts. Unlike models that aim to predict prices, this work focuses on explaining market sentiment using blockchain transactions, historical price data of Bitcoin, and daily Twitter sentiment classifications. The method merges sentiment trends with on-chain and financial metrics, normalized into a dataset for detailed market analysis. Multiple machine learning models were tested using cross-validation, with Gradient Boosting (XGBoost) emerging as the most reliable model for classifying sentiment, achieving an average F1-score of about 0.84. SHAP (SHapley Additive exPlanations), a game theory-based method for model interpretability, was used to quantify the contribution of on-chain features to the model's predictions, improving transparency. The results indicate that this data combination yields meaningful predictive signals and insights, supporting data-driven cryptocurrency analysis and future improvements with deep learning.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: [Eq 1] https://gz.blockchair.com/bitcoin/blocks/

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 2: DF_Result

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 3: \mathrm{Filter\_and\_Download}(\mathrm{Links})

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 4: \mathrm{Process\_File}(\mathrm{Raw\_DF})

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 5: DF\_Result\leftarrow

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 6: Files\leftarrow\mathrm{Filter\_and\_Download}(\mathrm{Links})

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 7: Raw\_DF\leftarrow\mathrm{LoadCSV}(file)

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

### Equation 8: Raw\_DF

* Equation: Not found in extracted context
* Symbols: Not found in extracted context
* Why it matters: Not found in extracted context

**Method Summary**
================

* The study proposes a predictive model that integrates on-chain data with sentiment analysis from social network posts to explore the relationship between blockchain behavior and market sentiment.
* The model uses on-chain data as input (X) and sentiment analysis from tweets as output (Y), normalized to fit the requirements of the predictive model.
* The study uses a 5-fold cross-validation procedure to evaluate the models, with the F1-score as the primary metric.

**Experimental Overview**
=====================

* Tasks/Datasets: The study uses on-chain data and sentiment analysis from tweets to predict market sentiment.
* Baselines/Comparisons: The study compares the performance of various classification algorithms, including XGBoost, using cross-validation.
* Main Claimed Findings: The study finds that XGBoost is the most reliable model for classifying sentiment, achieving an average F1-score of about 0.84.

**What to Verify in the PDF**
==========================

* The implementation details of the SHAP method for model interpretability.
* The specific on-chain features used in the model and their contribution to the predictions.
* The evaluation results for the SHAP method, including the contribution of on-chain features to the model's predictions.
{% endraw %}

{% raw %}
## 2) MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators
- **Authors:** Yushi Huang, Xiangxin Zhou, Jun Zhang, Liefeng Bo, Tianyu Pang
- **arXiv:** [2607.15273](https://arxiv.org/abs/2607.15273v1) · [pdf](https://arxiv.org/pdf/2607.15273v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.15273v1))
- **Categories:** cs.CV, cs.LG

### Abstract
> MeanFlow generators achieve fast few-step sampling by predicting average velocities over time intervals, making them attractive for efficient generation. Reinforcement learning (RL) has become a powerful way to align diffusion and flow models with human preferences and task-specific objectives. In particular, DiffusionNFT offers an efficient forward-process RL framework that does not require reverse-process trajectories or likelihood estimation. However, applying such RL methods to MeanFlow remains underexplored. DiffusionNFT optimizes instantaneous velocities, whereas MeanFlow samples with average velocities. To bridge this gap, we introduce MeanFlowNFT. Inspired by the MeanFlow identity, which bridges average and instantaneous velocities, we construct an induced instantaneous-velocity predictor. We apply the DiffusionNFT objective to this predictor, making reward optimization well-defined for MeanFlow. Sampling remains based on the average velocity, preserving MeanFlow's fast few-step generation. We further prove that MeanFlowNFT inherits DiffusionNFT's strict policy-improvement guarantee. Experiments on image and video generation show that MeanFlowNFT consistently improves baselines. Moreover, it outperforms prior state-of-the-art RL-tuned few-step generators on most metrics ($6$ of $8$ on SD3.5-M), and can even surpass multi-step RL-tuned diffusion while using only a few sampling steps. For instance, on Wan 2.1, $4$-step MeanFlowNFT reaches a VBench score of $84.33$, surpassing $50$-step LongCat-Video RL ($82.57$).
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: VBench score
```markdown
[Eq 1] 84.33
```
* Equation: VBench score
* Symbols: 84.33 (VBench score value)
* Why it matters: This is the VBench score achieved by the 4-step MeanFlowNFT model on the Wan 2.1 dataset.

### Equation 2: LongCat-Video RL score
```markdown
[Eq 2] 82.57
```
* Equation: VBench score
* Symbols: 82.57 (VBench score value)
* Why it matters: This is the VBench score achieved by the 50-step LongCat-Video RL model on the Wan 2.1 dataset.

### Equation 3: State vector
```markdown
[Eq 3] {\bm{x}}_{t}
```
* Equation: State vector
* Symbols: {\bm{x}}_{t} (state vector at time t)
* Why it matters: This represents the state vector at time t, which is used in the MeanFlowNFT model.

### Equation 4: Conditioning vector
```markdown
[Eq 4] {\bm{c}}
```
* Equation: Conditioning vector
* Symbols: {\bm{c}} (conditioning vector)
* Why it matters: This represents the conditioning vector used in the MeanFlowNFT model.

### Equation 5: Velocity vector
```markdown
[Eq 5] {\bm{u}}
```
* Equation: Velocity vector
* Symbols: {\bm{u}} (velocity vector)
* Why it matters: This represents the velocity vector used in the MeanFlowNFT model.

**Method Summary**
==================

* The MeanFlowNFT model combines the benefits of MeanFlow generators and DiffusionNFT's forward-process RL framework.
* The model uses an induced instantaneous-velocity predictor to optimize the MeanFlow policy.
* The model inherits DiffusionNFT's strict policy-improvement guarantee.
* The model is trained using CLIPScore, PickScore, and HPSv2 on image generation, and HPSv3-general and HPSv3-percentile on video generation.
* The model is compared to baselines such as AnyFlow, DMD, CDM, and RTDMD.

**Experimental Overview**
========================

* Tasks: Image and video generation
* Datasets: SD3.5-M, Wan 2.1 1.3B
* Baselines: AnyFlow, DMD, CDM, RTDMD, DiffusionNFT
* Main claimed findings:
	+ MeanFlowNFT outperforms baselines on most metrics.
	+ MeanFlowNFT achieves better generation quality and fewer reward-hacking artifacts than DiffusionNFT and RTDMD.
	+ MeanFlowNFT can surpass multi-step RL-tuned diffusion while using only a few sampling steps.

**What to Verify in the PDF**
=============================

* The derivation of the induced instantaneous-velocity predictor and its optimization.
* The proof of the strict policy-improvement guarantee.
* The detailed analysis of the design choices in MeanFlowNFT on SD3.5-M.
* The comparison of the MeanFlowNFT model to other few-step generators and RL methods.
{% endraw %}

{% raw %}
## 3) Online Neural Space Time Memory for Dynamic Novel View Synthesis
- **Authors:** Baback Elmieh, Lynn Tsai, Zeman Li, Srinivas Kaza, Tiancheng Sun, Gabor Csapo, Ali Behrouz, Yuan Deng, Stephen Lombardi, Steven M. Seitz, Xuan Luo
- **arXiv:** [2607.15271](https://arxiv.org/abs/2607.15271v1) · [pdf](https://arxiv.org/pdf/2607.15271v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.15271v1))
- **Categories:** cs.CV, cs.GR, cs.LG

### Abstract
> Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes. The computational cost of heavy memory updates precludes real-time application and can lead to instability over long contexts. Given that memory updates are more demanding than memory application and video content is largely redundant, we propose to decouple the frequencies of these two processes. Our approach performs periodic memory updates while applying the memory on a per-frame basis, using cross-view attention to manage deformations between the prior memory state and the current frame. To lock in the historical context, we introduce two critical mechanisms: an auxiliary Memory Loss that forces persistent internalization of the scene, and a Memory Caching strategy that regularizes active weights against catastrophic drift. Our method demonstrates real-time, state-of-the-art performance on scenes with dynamic human motion as well as minute-scale online memorization.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
=====================

### Equation 1: 256 × 256

* Equation: 256 × 256
* Symbols: None
* Why it matters: This equation represents the resolution of the input images used in the NSTM model. The model processes images of size 256 × 256, which is a common resolution for many computer vision tasks.

### Equation 2: L2

* Equation: L2
* Symbols: None
* Why it matters: This equation represents the loss function used in the NSTM model to regularize the weights and prevent catastrophic drift. The L2 loss is a common choice in deep learning to prevent overfitting.

### Equation 3: T = 60

* Equation: T = 60
* Symbols: T (time step)
* Why it matters: This equation represents the time step at which the model observes the input views. In this case, the model observes 60 frames of video at each time step.

### Equation 4: \mathcal{O}_{t} = {(\mathbf{I}_{t,i},\mathbf{P}_{t,i})}_{i=1}^{N}

* Equation: \mathcal{O}_{t} = {(\mathbf{I}_{t,i},\mathbf{P}_{t,i})}_{i=1}^{N}
* Symbols: \mathcal{O}_{t} (set of observations at time t), \mathbf{I}_{t,i} (input image at time t and view i), \mathbf{P}_{t,i} (camera pose at time t and view i)
* Why it matters: This equation represents the set of observations at each time step, which includes the input images and camera poses. The model uses these observations to synthesize the target image.

### Equation 5: \mathbf{I}_{t,i} ∈ \mathbb{R}^{H × W × 3}

* Equation: \mathbf{I}_{t,i} ∈ \mathbb{R}^{H × W × 3}
* Symbols: \mathbf{I}_{t,i} (input image at time t and view i), H (height), W (width), 3 (color channels)
* Why it matters: This equation represents the format of the input images, which are 3D tensors with height, width, and color channels.

**Method Summary**
================

* The NSTM model performs online novel view synthesis from multi-view dynamic video streams.
* The model uses a combination of cross-view attention, auxiliary memory loss, and memory caching to manage deformations and maintain a persistent memory state.
* The model applies the memory on a per-frame basis and updates the memory periodically using a stable L2 objective.
* The model uses a stack of Transformer blocks to process the input tokens and generate the target tokens.

**Experimental Overview**
=====================

* Tasks: The model is evaluated on the MVHumanNet++ dataset, which features 60,000 multi-view motion sequences across 4,500 identities and 9,000 outfits.
* Datasets: The model is evaluated on the 90%/10% train/test split of the MVHumanNet++ dataset.
* Baselines: The model is compared to the Token-Mem and LaCT-NVS baselines.
* Main claimed findings: The model demonstrates real-time, state-of-the-art performance on scenes with dynamic human motion and minute-scale online memorization.

**What to Verify in the PDF**
==========================

* The implementation details of the auxiliary memory loss and memory caching mechanisms.
* The effect of the stable L2 objective on the model's performance and stability.
* The evaluation protocol used to measure the model's performance on the MVHumanNet++ dataset.
* The results of the ablation study, which measures the impact of each component on the model's performance.
{% endraw %}

{% raw %}
## 4) Mutable Low-Rank Sketches for Retrain-Free Recommendation
- **Authors:** Hector J. Garcia, Nick Clayton
- **arXiv:** [2607.15242](https://arxiv.org/abs/2607.15242v1) · [pdf](https://arxiv.org/pdf/2607.15242v1)
- **LLM context source:** arXiv HTML ([html](https://arxiv.org/html/2607.15242v1))
- **Categories:** cs.LG

### Abstract
> A common bottleneck in two-stage recommendation is embedding staleness: when a user rates a new item, their embedding remains fixed until the next retrain cycle. We propose mutable sketches, which store each user's preferences in a KP-tree (a sparse segment tree with sum aggregation), fit a low-rank projection once, and recompute embeddings on-the-fly as ratings arrive. We prove that each new observation monotonically tightens the prediction error envelope (Theorem 1), a guarantee that FunkSVD and eALS lack. On KuaiRec, the mutable sketch achieves 0.810 RMSE at 1.8% data read vs. ALS 0.822 at 100%, with 8x faster per-batch updates. A new user receives personalized recommendations in <1 ms after their first rating, with no model retraining required. A comparison of sampling strategies across density regimes shows that the KP-tree's norm-proportional sampling provides 40-130% better item coverage on sparse data (<1% density), while uniform sampling suffices on dense matrices.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
**Formula Walkthrough**
======================

### Equation 1: 
\[ \mathbf{a} \in \mathbb{R}^{n} \]

* Symbols: \( \mathbf{a} \) (user preference vector), \( \mathbb{R}^{n} \) (n-dimensional real space)
* Why it matters: This equation represents the input space for user preference vectors, which are stored in a KP-tree.

### Equation 2: 
\[ O(\log n) \]

* Symbols: \( O(\log n) \) (Big O notation for logarithmic time complexity)
* Why it matters: This equation indicates the time complexity of operations supported by the KP-tree, such as sampling, querying, and updating.

### Equation 3: 
\[ V_{k} \]

* Symbols: \( V_{k} \) (low-rank projection matrix)
* Why it matters: This equation represents the fixed low-rank basis used to project user preference vectors onto item embeddings.

### Equation 4: 
\[ \mathbf{a} \in \mathbb{R}^{n} \]

* Symbols: \( \mathbf{a} \) (user preference vector), \( \mathbb{R}^{n} \) (n-dimensional real space)
* Why it matters: This equation is identical to Equation 1 and represents the input space for user preference vectors.

### Equation 5: 
\[ \lceil\log_{2}n\rceil \]

* Symbols: \( \lceil\log_{2}n\rceil \) (ceiling function for logarithm base 2)
* Why it matters: This equation represents the maximum depth of the KP-tree, which is used to determine the number of levels in the tree.

**Method Summary**
================

* The proposed method uses a KP-tree to store user preference vectors, which supports efficient sampling, querying, and updating operations.
* A low-rank projection matrix \( V_{k} \) is fitted once from a small sketch, and user embeddings are recomputed on-the-fly as ratings arrive.
* The method decouples data freshness from model freshness, allowing for retrain-free recommendation.

**Experimental Overview**
=====================

* The proposed method is evaluated on several datasets, including KuaiRec, Amazon Electronics, Amazon Video Games, Amazon Music, and Book-Crossing.
* Baselines include ALS, FunkSVD, and eALS, as well as full-data methods such as SVD.
* The method achieves competitive performance on KuaiRec and sparser benchmarks, with a trade-off in accuracy and data read.

**What to Verify in the PDF**
==========================

* The proof of Theorem 2, which guarantees that the prediction error envelope monotonically tightens with new observations.
* The detailed analysis of the KP-tree's sampling strategy and its impact on item coverage on sparse data.
* The experimental results on the ML-1M dataset, which may provide additional insights into the method's performance on very sparse data.
{% endraw %}

{% raw %}
## 5) In-Place Tokenizer Expansion for Pre-trained LLMs
- **Authors:** Jimmy T. H. Smith, Tarek Dakhran, Alberto Cabrera, Simon S. Lee, Paul Pak, Aditya Tadimeti, Tim Seyde, Maxime Labonne, Alexander Amini, Mathias Lechner
- **arXiv:** [2607.15232](https://arxiv.org/abs/2607.15232v1) · [pdf](https://arxiv.org/pdf/2607.15232v1)
- **LLM context source:** abstract only
- **Categories:** cs.CL, cs.AI, cs.LG

### Abstract
> A tokenizer fixed at the start of pre-training allocates vocabulary in proportion to the pre-training corpus, reflecting the deployment priorities at that time. When those priorities shift, languages added later are split into many more tokens per word, which can raise latency, compute, and energy consumption for users of those languages. Cloud models can afford a broad vocabulary because the embedding and LM-head matrices are a small fraction of their parameters. On a compact model those matrices are a material share of per-token decode bandwidth, so on-device models ship small vocabularies and accept fragmentation outside a fixed language set. We present tokenizer expansion, an in-place recipe for upgrading a pre-trained model's tokenizer when the model producer controls its design. We continue the existing tokenizer's BPE merges on a multilingual corpus, so most source tokens carry over unchanged as single tokens and every new token has an exact decomposition into source tokens. We copy the carried-over embedding rows unchanged and initialize new rows as the mean of their source sub-token embeddings. A two-stage adaptation, embedding-only training then full-model continued pre-training, recovers source-checkpoint quality. We apply the recipe to a continued pre-trained checkpoint of LFM2-8B-A1B, an 8B-parameter Mixture-of-Experts model, to help produce LFM2.5-8B-A1B with a 128K tokenizer. The expanded tokenizer encodes Hindi and Vietnamese in roughly $2.4\times$ and $2.6\times$ fewer tokens than the source (up to $4.0\times$ on Thai). Combining these reductions with the measured per-token cost of the larger vocabulary, we estimate a $2.2$-$3.7\times$ per-character decode speedup for these languages across our reference devices. We release the model weights and the expanded tokenizer, and report the negative findings that shaped the recipe.
{% endraw %}

### Formula and Experiment Notes (LLM)
{% raw %}
### Formula Walkthrough
#### 1. Vocabulary Allocation
Not found in extracted context.

#### 2. Embedding Decomposition
Not found in extracted context.

#### 3. Tokenizer Expansion
Not found in extracted context.

#### 4. Embedding Initialization
Not found in extracted context.

#### 5. Per-Character Decode Speedup
Not found in extracted context.

### Method Summary
* The proposed method, tokenizer expansion, is an in-place recipe for upgrading a pre-trained model's tokenizer.
* The existing tokenizer's BPE merges are continued on a multilingual corpus.
* Most source tokens carry over unchanged as single tokens, and every new token has an exact decomposition into source tokens.
* The carried-over embedding rows are copied unchanged, and new rows are initialized as the mean of their source sub-token embeddings.
* A two-stage adaptation is applied: embedding-only training and full-model continued pre-training.

### Experimental Overview
* Tasks/Datasets: The authors apply the tokenizer expansion recipe to a continued pre-trained checkpoint of LFM2-8B-A1B.
* Baselines/Comparisons: The authors compare the performance of the expanded tokenizer to the original tokenizer.
* Main Claimed Findings: The expanded tokenizer encodes Hindi and Vietnamese in roughly $2.4\times$ and $2.6\times$ fewer tokens than the source, resulting in a $2.2$-$3.7\times$ per-character decode speedup.

### What to Verify in the PDF
* The implementation details of the two-stage adaptation process.
* The exact decomposition of new tokens into source tokens.
* The impact of the tokenizer expansion on the model's performance on other languages.
{% endraw %}
