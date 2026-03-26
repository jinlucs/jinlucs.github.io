---
layout: post
title: "Daily arXiv Digest — 2026-03-26 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Model Predictive Path Integral Control as Preconditioned Gradient Descent
- **Authors:** Mahyar Fazlyab, Sina Sharifi, Jiarui Wang
- **arXiv:** [2603.24489](https://arxiv.org/abs/2603.24489v1) · [pdf](https://arxiv.org/pdf/2603.24489v1)
- **Categories:** math.OC, eess.SY

### Abstract
> Model Predictive Path Integral (MPPI) control is a popular sampling-based method for trajectory optimization in nonlinear and nonconvex settings, yet its optimization structure remains only partially understood. We develop a variational, optimization-theoretic interpretation of MPPI by lifting constrained trajectory optimization to a KL-regularized problem over distributions and reducing it to a negative log-partition (free-energy) objective over a tractable sampling family. For a general parametric family, this yields a preconditioned gradient method on the distribution parameters and a natural multi-step extension of MPPI. For the fixed-covariance Gaussian family, we show that classical MPPI is recovered exactly as a preconditioned gradient descent step with unit step size. This interpretation enables a direct convergence analysis: under bounded feasible sets, we derive an explicit upper bound on the smoothness constant and a simple sufficient condition guaranteeing descent of exact MPPI. Numerical experiments support the theory and illustrate the effect of key hyperparameters on performance.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) The Riemannian Landing Method: From projected gradient flows to SQP
- **Authors:** Florentin Goyens, Florian Feppon
- **arXiv:** [2603.24309](https://arxiv.org/abs/2603.24309v1) · [pdf](https://arxiv.org/pdf/2603.24309v1)
- **Categories:** math.OC

### Abstract
> Landing methods have recently emerged in Riemannian matrix optimization as efficient schemes for handling nonlinear equality constraints without resorting to costly retractions. These methods decompose the search direction into tangent and normal components, enabling asymptotic feasibility while maintaining inexpensive updates. In this work, we provide a unifying geometric framework which reveals that, under suitable choices of Riemannian metric, the landing algorithm encompasses several classical optimization methods such as projected and null-space gradient flows, Sequential Quadratic Programming (SQP), and a certain form of the augmented Lagrangian method. In particular, we show that a quadratically convergent landing method essentially reproduces the quadratically convergent SQP method. These connections also allow us to propose a globally convergent landing method using adaptive step sizes. The backtracking line search satisfies an Armijo condition on a merit function, and does not require prior knowledge of Lipschitz constants. Our second key contribution is to analyze landing methods through a geometric parameterization of the metric in terms of fields of oblique projectors and associated metric restrictions. This viewpoint disentangles the roles of orthogonality, tangent and normal metrics, and elucidates how to design the metric to obtain explicit tangent and normal updates. For matrix optimization, this framework not only recovers recent constructions in the literature for problems with orthogonality constraints, but also provides systematic guidelines for designing new metrics that admit closed-form search directions.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) HEART-PFL: Stable Personalized Federated Learning under Heterogeneity with Hierarchical Directional Alignment and Adversarial Knowledge Transfer
- **Authors:** Minjun Kim, Minje Kim
- **arXiv:** [2603.24209](https://arxiv.org/abs/2603.24209v1) · [pdf](https://arxiv.org/pdf/2603.24209v1)
- **Categories:** cs.CV, cs.LG

### Abstract
> Personalized Federated Learning (PFL) aims to deliver effective client-specific models under heterogeneous distributions, yet existing methods suffer from shallow prototype alignment and brittle server-side distillation. We propose HEART-PFL, a dual-sided framework that (i) performs depth-aware Hierarchical Directional Alignment (HDA) using cosine similarity in the early stage and MSE matching in the deep stage to preserve client specificity, and (ii) stabilizes global updates through Adversarial Knowledge Transfer (AKT) with symmetric KL distillation on clean and adversarial proxy data. Using lightweight adapters with only 1.46M trainable parameters, HEART-PFL achieves state-of-the-art personalized accuracy on CIFAR-100, Flowers-102, and Caltech-101 (63.42%, 84.23%, and 95.67%, respectively) under Dirichlet non-IID partitions, and remains robust to out-of-domain proxy data. Ablation studies further confirm that HDA and AKT provide complementary gains in alignment, robustness, and optimization stability, offering insights into how the two components mutually reinforce effective personalization. Overall, these results demonstrate that HEART-PFL simultaneously enhances personalization and global stability, highlighting its potential as a strong and scalable solution for PFL(code available at https://github.com/danny0628/HEART-PFL).

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) On Gossip Algorithms for Machine Learning with Pairwise Objectives
- **Authors:** Igor Colin, Aurélien Bellet, Stephan Clémençon, Joseph Salmon
- **arXiv:** [2603.24128](https://arxiv.org/abs/2603.24128v1) · [pdf](https://arxiv.org/pdf/2603.24128v1)
- **Categories:** cs.LG

### Abstract
> In the IoT era, information is more and more frequently picked up by connected smart sensors with increasing, though limited, storage, communication and computation abilities. Whether due to privacy constraints or to the structure of the distributed system, the development of statistical learning methods dedicated to data that are shared over a network is now a major issue. Gossip-based algorithms have been developed for the purpose of solving a wide variety of statistical learning tasks, ranging from data aggregation over sensor networks to decentralized multi-agent optimization. Whereas the vast majority of contributions consider situations where the function to be estimated or optimized is a basic average of individual observations, it is the goal of this article to investigate the case where the latter is of pairwise nature, taking the form of a U -statistic of degree two. Motivated by various problems such as similarity learning, ranking or clustering for instance, we revisit gossip algorithms specifically designed for pairwise objective functions and provide a comprehensive theoretical framework for their convergence. This analysis fills a gap in the literature by establishing conditions under which these methods succeed, and by identifying the graph properties that critically affect their efficiency. In particular, a refined analysis of the convergence upper and lower bounds is performed.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Retrieval Improvements Do Not Guarantee Better Answers: A Study of RAG for AI Policy QA
- **Authors:** Saahil Mathur, Ryan David Rittner, Vedant Ajit Thakur, Daniel Stuart Schiff, Tunazzina Islam
- **arXiv:** [2603.24580](https://arxiv.org/abs/2603.24580v1) · [pdf](https://arxiv.org/pdf/2603.24580v1)
- **Categories:** cs.CL, cs.AI, cs.CY, cs.IR, cs.LG

### Abstract
> Retrieval-augmented generation (RAG) systems are increasingly used to analyze complex policy documents, but achieving sufficient reliability for expert usage remains challenging in domains characterized by dense legal language and evolving, overlapping regulatory frameworks. We study the application of RAG to AI governance and policy analysis using the AI Governance and Regulatory Archive (AGORA) corpus, a curated collection of 947 AI policy documents. Our system combines a ColBERT-based retriever fine-tuned with contrastive learning and a generator aligned to human preferences using Direct Preference Optimization (DPO). We construct synthetic queries and collect pairwise preferences to adapt the system to the policy domain. Through experiments evaluating retrieval quality, answer relevance, and faithfulness, we find that domain-specific fine-tuning improves retrieval metrics but does not consistently improve end-to-end question answering performance. In some cases, stronger retrieval counterintuitively leads to more confident hallucinations when relevant documents are absent from the corpus. These results highlight a key concern for those building policy-focused RAG systems: improvements to individual components do not necessarily translate to more reliable answers. Our findings provide practical insights for designing grounded question-answering systems over dynamic regulatory corpora.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
