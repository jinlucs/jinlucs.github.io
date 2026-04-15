---
layout: page
title: Research
subtitle: Machine learning, optimization, foundation models, and AI systems in the wild
---

I lead a research program on rigorous, efficient, and deployable AI. My work sits at the intersection of machine learning, optimization, systems, and interdisciplinary applications. A recurring goal across projects is to design methods that remain useful when computation, communication, interpretability, or reliability constraints matter as much as raw accuracy.

### 1. Optimization for AI
Optimization is a core theme of my work. I study optimization methods that support modern machine learning systems, especially when standard first-order assumptions break down or deployment constraints become important.

Current directions include:
- convex and nonconvex optimization for machine learning;
- projected, proximal, and bilevel methods;
- derivative-free and zeroth-order optimization;
- optimization under communication, memory, and hardware constraints.

This line of work also informs my teaching, especially my graduate course on Optimization in AI and the proposed new course CSCI 8830 Advanced Optimization Methods in AI.

### 2. Efficient Foundation Models and LLM Adaptation
Recent projects in my group focus on efficient adaptation and fine-tuning of large models. I am interested in making foundation model training and deployment more practical without giving up robustness or scientific rigor.

Representative topics include:
- zeroth-order optimization for LLM fine-tuning;
- quantization-aware and memory-efficient on-device training;
- efficient DNN training and layer freezing;
- instruction tuning, causal control, and robustness;
- machine unlearning and model editing.

This work connects optimization, systems, and trustworthy AI, and it is motivated by the growing need to adapt large models in resource-limited environments.

### 3. Federated, Distributed, and On-Device Learning
Another major thrust of my research is learning in decentralized and heterogeneous environments. Real deployments often involve multiple devices, partial data, unreliable communication, and non-identical local conditions. I work on algorithms that remain effective under these realities.

Representative topics include:
- federated learning on heterogeneous clients;
- decentralized and infrastructure-less learning;
- personalized federated learning;
- on-device model adaptation;
- edge AI and Internet of Things applications.

This thread of work has led to projects on WiFi sensing, mobile systems, edge intelligence, and learning on constrained hardware.

### 4. Multimodal AI for Health, Agriculture, and Sensing
I collaborate widely on AI methods that integrate images, language, event streams, physiological signals, and other sensor data. These applications give rise to important algorithmic questions about robustness, interpretability, multimodal fusion, and efficient deployment.

Representative applications include:
- multimodal medical time-series analysis;
- physiological signal interpretation and supportive small models;
- contactless BMI and blood pressure monitoring;
- smart-home activity recognition;
- poultry monitoring and precision agriculture;
- AI-assisted breeding and other domain-specific scientific workflows.

A common principle in these collaborations is that useful AI systems should be interpretable, resource-aware, and robust enough for real operational settings.

### Selected Recent Publications
- Roots Beneath the Cut: Uncovering the Risk of Concept Recovery in Pruning-Based Unlearning for Diffusion Models, CVPR 2026
- MITS: Enhanced Tree Search Reasoning for LLMs via Pointwise Mutual Information, PAKDD 2026
- ADLGen: Synthesizing Symbolic, Event-Triggered Sensor Sequences, SenSys 2026
- CARE: Contrastive Alignment for ADL Recognition from Event-Triggered Sensor Streams, PerCom 2026
- LOCAL: Latent Orthonormal Contrastive Learning for Paired Image Classification, ICCV 2025
- HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-Tuning LLM with Zeroth-Order Optimization, EMNLP 2025
- Harmony in Divergence: Towards Fast, Accurate, and Memory-Efficient Zeroth-Order LLM Fine-Tuning, NeurIPS 2025
- Proximal Federated Learning for Body Mass Index Monitoring Using Commodity WiFi, MobiCom 2024

See the full [publications list](/papers/) for more.

### Funding and Collaborations
My research has been supported through collaborations and internal awards, including the NIH-supported CARE-TRAC project and University of Georgia awards related to LLM inference in IoT, Neuro-AI integration, and AI-assisted breeding. I collaborate with researchers across computing, engineering, medicine, agriculture, and environmental science.

### Talks and Visibility
I regularly present this work in conference venues, invited seminars, and university research events. Recent presentations include talks connected to ICCV, EMNLP, NeurIPS, ICCAD, GLSVLSI, MobiCom, and UGA's AI Research Spotlight.

### Learn More
- [Papers](/papers/)
- [Teaching](/teaching/)
- [Group](/group/)
- [Daily arXiv Digest](/arxiv/)
