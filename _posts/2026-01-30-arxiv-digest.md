---
layout: post
title: "Daily arXiv Digest — 2026-01-30 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Efficient Stochastic Optimisation via Sequential Monte Carlo
- **Authors:** James Cuin, Davide Carbone, Yanbo Tang, O. Deniz Akyildiz
- **arXiv:** [2601.22003](https://arxiv.org/abs/2601.22003v1) · [pdf](https://arxiv.org/pdf/2601.22003v1)
- **Categories:** stat.ML, cs.LG, stat.CO

### Abstract
> The problem of optimising functions with intractable gradients frequently arise in machine learning and statistics, ranging from maximum marginal likelihood estimation procedures to fine-tuning of generative models. Stochastic approximation methods for this class of problems typically require inner sampling loops to obtain (biased) stochastic gradient estimates, which rapidly becomes computationally expensive. In this work, we develop sequential Monte Carlo (SMC) samplers for optimisation of functions with intractable gradients. Our approach replaces expensive inner sampling methods with efficient SMC approximations, which can result in significant computational gains. We establish convergence results for the basic recursions defined by our methodology which SMC samplers approximate. We demonstrate the effectiveness of our approach on the reward-tuning of energy-based models within various settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Investigating Batch Inference in a Sequential Monte Carlo Framework for Neural Networks
- **Authors:** Andrew Millard, Joshua Murphy, Peter Green, Simon Maskell
- **arXiv:** [2601.21983](https://arxiv.org/abs/2601.21983v1) · [pdf](https://arxiv.org/pdf/2601.21983v1)
- **Categories:** cs.LG

### Abstract
> Bayesian inference allows us to define a posterior distribution over the weights of a generic neural network (NN). Exact posteriors are usually intractable, in which case approximations can be employed. One such approximation - variational inference - is computationally efficient when using mini-batch stochastic gradient descent as subsets of the data are used for likelihood and gradient evaluations, though the approach relies on the selection of a variational distribution which sufficiently matches the form of the posterior. Particle-based methods such as Markov chain Monte Carlo and Sequential Monte Carlo (SMC) do not assume a parametric family for the posterior by typically require higher computational cost. These sampling methods typically use the full-batch of data for likelihood and gradient evaluations, which contributes to this computational expense. We explore several methods of gradually introducing more mini-batches of data (data annealing) into likelihood and gradient evaluations of an SMC sampler. We find that we can achieve up to $6\times$ faster training with minimal loss in accuracy on benchmark image classification problems using NNs.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Diverse Approaches to Optimal Execution Schedule Generation
- **Authors:** Robert de Witt, Mikko S. Pakkanen
- **arXiv:** [2601.22113](https://arxiv.org/abs/2601.22113v1) · [pdf](https://arxiv.org/pdf/2601.22113v1)
- **Categories:** q-fin.TR, cs.LG

### Abstract
> We present the first application of MAP-Elites, a quality-diversity algorithm, to trade execution. Rather than searching for a single optimal policy, MAP-Elites generates a diverse portfolio of regime-specialist strategies indexed by liquidity and volatility conditions. Individual specialists achieve 8-10% performance improvements within their behavioural niches, while other cells show degradation, suggesting opportunities for ensemble approaches that combine improved specialists with the baseline PPO policy. Results indicate that quality-diversity methods offer promise for regime-adaptive execution, though substantial computational resources per behavioural cell may be required for robust specialist development across all market conditions. To ensure experimental integrity, we develop a calibrated Gymnasium environment focused on order scheduling rather than tactical placement decisions. The simulator features a transient impact model with exponential decay and square-root volume scaling, fit to 400+ U.S. equities with R^2>0.02 out-of-sample. Within this environment, two Proximal Policy Optimization architectures - both MLP and CNN feature extractors - demonstrate substantial improvements over industry baselines, with the CNN variant achieving 2.13 bps arrival slippage versus 5.23 bps for VWAP on 4,900 out-of-sample orders ($21B notional). These results validate both the simulation realism and provide strong single-policy baselines for quality-diversity methods.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Anderson Mixing in Bures Wasserstein Space of Gaussian Measures
- **Authors:** Vitalii Aksenov, Martin Eigel, Mathias Oster
- **arXiv:** [2601.22038](https://arxiv.org/abs/2601.22038v1) · [pdf](https://arxiv.org/pdf/2601.22038v1)
- **Categories:** math.OC

### Abstract
> Various statistical tasks, including sampling or computing Wasserstein barycenters, can be reformulated as fixed-point problems for operators on probability distributions. Accelerating standard fixed-point iteration schemes provides a promising novel approach to the design of efficient numerical methods for these problems. The Wasserstein geometry on the space of probability measures, although not precisely Riemannian, allows us to define various useful Riemannian notions, such as tangent spaces, exponential maps and parallel transport, motivating the adaptation of Riemannian numerical methods. We demonstrate this by developing and implementing the Riemannian Anderson Mixing (RAM) method for Gaussian distributions. The method reuses the history of the residuals and improves the iteration complexity, and we argue that the additional costs, compared to Picard method, are negligible. We show that certain open balls in the Bures-Wasserstein manifold satisfy the requirements for convergence of RAM. The numerical experiments show a significant acceleration compared to a Picard iteration, and performance on par with Riemannian Gradient Descent and Conjugate Gradient methods.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Exploring Diverse Generation Paths via Inference-time Stiefel Activation Steering
- **Authors:** Dongxuan Zhu, Ly Tran Ho Khanh, Andy Yat-Ming Cheung, Man-Chung Yue, Viet Anh Nguyen
- **arXiv:** [2601.22010](https://arxiv.org/abs/2601.22010v1) · [pdf](https://arxiv.org/pdf/2601.22010v1)
- **Categories:** cs.LG

### Abstract
> Language models often default to a narrow set of high-probability outputs, leaving their generation paths homogeneous and prone to mode collapse. Sampling-based strategies inject randomness but still struggle to guarantee diversity across multiple concurrent generation runs. We address this limitation by introducing STARS ($\textbf{St}$iefel-based $\textbf{A}$ctivation Steering for Diverse $\textbf{R}$ea$\textbf{S}$oning), a training-free, inference-time intervention method that transforms activation steering into an exploration engine. At each token, STARS collects the hidden activations of concurrent generation runs and optimizes multiple additive steering directions jointly on the Stiefel manifold. STARS maximizes the geometric volume of the steered activations, while the Stiefel manifold induces orthogonality of the steering interventions. This formulation explicitly promotes divergent activation vectors of concurrent generation runs, and implicitly promotes divergent generation trajectories. This manifold optimization formulation can be solved using a Riemannian gradient descent algorithm with convergence guarantees, but this algorithm is too time-consuming for real-time inference. To guarantee low latency, we further design a lightweight one-step update with an aggressive, closed-form stepsize. For test case generation and scientific discovery benchmarks, STARS consistently outperforms standard sampling methods, achieving greater diversity without sacrificing qualitative performance.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
