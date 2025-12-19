---
layout: post
title: "Daily arXiv Digest — 2025-12-19 (ML + Optimization)"
categories: [arxiv]
tags: [arxiv, digest, ml, optimization]
mathjax: true
---

> Auto-generated from arXiv metadata + an LLM reading only titles/abstracts.
> Equations are **interpretive**; always verify with the PDF.

## 1) Pixel Seal: Adversarial-only training for invisible image and video watermarking
- **Authors:** Tomáš Souček, Pierre Fernandez, Hady Elsahar, Sylvestre-Alvise Rebuffi, Valeriu Lacatusu, Tuan Tran, Tom Sander, Alexandre Mourachko
- **arXiv:** [2512.16874](https://arxiv.org/abs/2512.16874v1) · [pdf](https://arxiv.org/pdf/2512.16874v1)
- **Categories:** cs.CV, cs.AI, cs.CR, cs.LG

### Abstract
> Invisible watermarking is essential for tracing the provenance of digital content. However, training state-of-the-art models remains notoriously difficult, with current approaches often struggling to balance robustness against true imperceptibility. This work introduces Pixel Seal, which sets a new state-of-the-art for image and video watermarking. We first identify three fundamental issues of existing methods: (i) the reliance on proxy perceptual losses such as MSE and LPIPS that fail to mimic human perception and result in visible watermark artifacts; (ii) the optimization instability caused by conflicting objectives, which necessitates exhaustive hyperparameter tuning; and (iii) reduced robustness and imperceptibility of watermarks when scaling models to high-resolution images and videos. To overcome these issues, we first propose an adversarial-only training paradigm that eliminates unreliable pixel-wise imperceptibility losses. Second, we introduce a three-stage training schedule that stabilizes convergence by decoupling robustness and imperceptibility. Third, we address the resolution gap via high-resolution adaptation, employing JND-based attenuation and training-time inference simulation to eliminate upscaling artifacts. We thoroughly evaluate the robustness and imperceptibility of Pixel Seal on different image types and across a wide range of transformations, and show clear improvements over the state-of-the-art. We finally demonstrate that the model efficiently adapts to video via temporal watermark pooling, positioning Pixel Seal as a practical and scalable solution for reliable provenance in real-world image and video settings.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 2) Non-Asymptotic Global Convergence of PPO-Clip
- **Authors:** Yin Liu, Qiming Dai, Junyu Zhang, Zaiwen Wen
- **arXiv:** [2512.16565](https://arxiv.org/abs/2512.16565v1) · [pdf](https://arxiv.org/pdf/2512.16565v1)
- **Categories:** math.OC, cs.LG

### Abstract
> Reinforcement learning (RL) has gained attention for aligning large language models (LLMs) via reinforcement learning from human feedback (RLHF). The actor-only variants of Proximal Policy Optimization (PPO) are widely applied for their efficiency. These algorithms incorporate a clipping mechanism to improve stability. Besides, a regularization term, such as the reverse KL-divergence or a more general \(f\)-divergence, is introduced to prevent policy drift. Despite their empirical success, a rigorous theoretical understanding of the problem and the algorithm's properties is limited. This paper advances the theoretical foundations of the PPO-Clip algorithm by analyzing a deterministic actor-only PPO algorithm within the general RL setting with \(f\)-divergence regularization under the softmax policy parameterization. We derive a non-uniform Lipschitz smoothness condition and a Łojasiewicz inequality for the considered problem. Based on these, a non-asymptotic linear convergence rate to the globally optimal policy is established for the forward KL-regularizer. Furthermore, stationary convergence and local linear convergence are derived for the reverse KL-regularizer.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 3) Continuized Nesterov Acceleration for Non-Convex Optimization
- **Authors:** Julien Hermant, Jean-François Aujol, Charles Dossal, Lorick Huang, Aude Rondepierre
- **arXiv:** [2512.16533](https://arxiv.org/abs/2512.16533v1) · [pdf](https://arxiv.org/pdf/2512.16533v1)
- **Categories:** math.OC

### Abstract
> In convex optimization, continuous-time counterparts have been a fruitful tool for analyzing momentum algorithms. Fewer such examples are available when the function to minimize is non-convex. In several cases, discrepancies arise between the existing discrete-time results, namely those obtained for momentum algorithms, and their continuous-time counterparts, with the latter typically yielding stronger guarantees. We argue that the continuized framework (Even et al., 2021), mixing continuous and discrete components, can tighten the gap between known continuous and discrete results. This framework relies on computations akin to standard Lyapunov analyses, from which are deduced convergence bounds for an algorithm that can be written as a Nesterov momentum algorithm with stochastic parameters. In this work, we extend the range of applicability of the continuized framework, e.g. by allowing it to handle non-smooth Lyapunov functions. We then strengthen its trajectory-wise guarantees for linear convergence rate, deriving finite time bounds with high probability and asymptotic almost sure bounds. We apply this framework to the non-convex class of strongly quasar convex functions. Adapting continuous-time results that have weaker discrete equivalents to the continuized method, we improve by a constant factor the known convergence rate, and relax the existing assumptions on the set of minimizers.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 4) Distributed Online Economic Dispatch With Time-Varying Coupled Inequality Constraints
- **Authors:** Yingjie Zhou, Xiaoqian Wang, Tao Li
- **arXiv:** [2512.16241](https://arxiv.org/abs/2512.16241v1) · [pdf](https://arxiv.org/pdf/2512.16241v1)
- **Categories:** math.OC, stat.ME

### Abstract
> We investigate the distributed online economic dispatch problem for power systems with time-varying coupled inequality constraints. The problem is formulated as a distributed online optimization problem in a multi-agent system. At each time step, each agent only observes its own instantaneous objective function and local inequality constraints; agents make decisions online and cooperate to minimize the sum of the time-varying objectives while satisfying the global coupled constraints. To solve the problem, we propose an algorithm based on the primal-dual approach combined with constraint-tracking. Under appropriate assumptions that the objective and constraint functions are convex, their gradients are uniformly bounded, and the path length of the optimal solution sequence grows sublinearly, we analyze theoretical properties of the proposed algorithm and prove that both the dynamic regret and the constraint violation are sublinear with time horizon T. Finally, we evaluate the proposed algorithm on a time-varying economic dispatch problem in power systems using both synthetic data and Australian Energy Market data. The results demonstrate that the proposed algorithm performs effectively in terms of tracking performance, constraint satisfaction, and adaptation to time-varying disturbances, thereby providing a practical and theoretically well-supported solution for real-time distributed economic dispatch.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_

## 5) Learning Confidence Ellipsoids and Applications to Robust Subspace Recovery
- **Authors:** Chao Gao, Liren Shan, Vaidehi Srinivas, Aravindan Vijayaraghavan
- **arXiv:** [2512.16875](https://arxiv.org/abs/2512.16875v1) · [pdf](https://arxiv.org/pdf/2512.16875v1)
- **Categories:** cs.DS, cs.LG, math.ST, stat.ML

### Abstract
> We study the problem of finding confidence ellipsoids for an arbitrary distribution in high dimensions. Given samples from a distribution $D$ and a confidence parameter $α$, the goal is to find the smallest volume ellipsoid $E$ which has probability mass $\Pr_{D}[E] \ge 1-α$. Ellipsoids are a highly expressive class of confidence sets as they can capture correlations in the distribution, and can approximate any convex set. This problem has been studied in many different communities. In statistics, this is the classic minimum volume estimator introduced by Rousseeuw as a robust non-parametric estimator of location and scatter. However in high dimensions, it becomes NP-hard to obtain any non-trivial approximation factor in volume when the condition number $β$ of the ellipsoid (ratio of the largest to the smallest axis length) goes to $\infty$. This motivates the focus of our paper: can we efficiently find confidence ellipsoids with volume approximation guarantees when compared to ellipsoids of bounded condition number $β$? Our main result is a polynomial time algorithm that finds an ellipsoid $E$ whose volume is within a $O(β^{γd})$ multiplicative factor of the volume of best $β$-conditioned ellipsoid while covering at least $1-O(α/γ)$ probability mass for any $γ< α$. We complement this with a computational hardness result that shows that such a dependence seems necessary up to constants in the exponent. The algorithm and analysis uses the rich primal-dual structure of the minimum volume enclosing ellipsoid and the geometric Brascamp-Lieb inequality. As a consequence, we obtain the first polynomial time algorithm with approximation guarantees on worst-case instances of the robust subspace recovery problem.

### Math explanation (LLM)
_(No LLM key configured — showing abstract only. Set `LLM_PROVIDER` + an API key secret to enable math explanations.)_
