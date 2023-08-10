---
layout: skeleton
---
[site]: https://www.cis.upenn.edu/~exwong/debugml/

# [7000-005: Debugging Data & Models (Fall 2022)][site]

Do you trust your model? Despite their widespread adoption and impressive performance, modern machine learning models have a crucial flaw: it is extremely difficult to discern when and how models fail. This pitfall has given rise to a field of research known as *trustworthy machine learning*, in order to make these systems safe, responsible, and understandable. 

This course will explore the tools and methods for analyzing the machine learning pipeline and assessing their trustworthiness (or lack thereof), from the datasets, models, and predictions perspective. A [tentative schedule](#tentative-schedule-and-topics) of these topics can be found at the bottom of this page. 

**Instructor**: [Eric Wong](https://www.cis.upenn.edu/~exwong) ([exwong@cis](mailto:exwong@cis.upenn.edu))

**Class**: Tues 1:45-3:15pm Eastern, DRLB 4C6 / Thurs 1:45-3:15pm Eastern, CHEM 514

**Website**: [https://www.cis.upenn.edu/~exwong/debugml/][site]

**Ed discussion**: [Self sign-up link](https://edstem.org/us/join/dKcj6G)

**Mask policy**: Masks are required.  

Students from all majors and degree levels are welcome. There are no specific course requirements, but a background in machine learning at an introductory course level is expected, as well as basic programming experience for the course project.  

Grading will be based off of 80% course project (15% proposal + 20% progress report + 25% final report + 20% presentation) and 20% participation (5% readings + 15% discussion). There will be no homeworks or exams. 

This class will combine lectures and discussions. The lectures will typically cover the core groundwork, followed by a student-led in-depth discussion based on assigned readings. Readings and lecture materials will be posted on the schedule. 

#### Project
As part of this course, students will inspect and debug machine learning problems for deficiencies in settings of their choice. All parts of the pipeline are fair game, including data collection, training algorithms, models and architectures, the resulting predictions, and even the debugging tools themselves. This can take the form of an audit (identifying the shortcomings of a fixed pipeline) or a patch/update (changing the pipeline to fix a problem). Example projects at various stages in the pipeline include the following: 

+ Datasets: 
    + Are there biases, spurious correlations, or underrepresented subpopulations? For example, does US census data have any blind spots or misleading correlations? 
    + Where do these problems stem from, and how does this impact downstream predictions? 
    + Can we fix the data or collection procedure to mitigate these issues? 
+ Methods and architectures: 
    + Do ML algorithms (i.e. fairness / privacy / adversarial robustness / security) for fixing models via training actually achieve their goal? 
    + Can you pinpoint or characterize the failures of modern architectures (such as large language models)? 
    + Can you construct counterexamples / subpopulations that exemplify the failure modes of these models and algorithms, or guarantee that such failure modes don't exist? 
+ Interpretability and predictions: 
	+ How faithful are explainability methods to the actual model predictions? 
	+ Are the type of explanations we can generate aligned with what practitioners need? 
	+ For example, do analysis tools for diagnosing health conditions tell doctors useful and meaningful information? 

#### Tentative schedule and topics 
The schedule and topics can change based on students' interests and as time permits. If you don't see something you'd like to learn about, send me an email. 

| Date | Topic | Notes |
|---|---|---|
| August 30 | Overview | [Slides](https://www.cis.upenn.edu/~exwong/assets/debugml/overview_slides.pdf)<br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/overview.pdf)<br>[Notebook](https://www.cis.upenn.edu/~exwong/assets/debugml/linear.ipynb)<br>Supplementary reading - [Problems in health care](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8443295/) |
|  |  |  |
| *Failure modes* |||
| September 1 | Bias | Types of Bias<br>[Slides](https://www.cis.upenn.edu/~exwong/assets/debugml/bias_slides.pdf)<br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/bias.pdf)<br>[Notebook](https://www.cis.upenn.edu/~exwong/assets/debugml/bias.ipynb)<br>[The trouble with Bias - NeurIPS 2017 Keynote by Kate Crawford](https://www.youtube.com/watch?v=fMym_BKWQzk)<br>[Supplementary reading - Suresh & Guttag, 2019](https://arxiv.org/abs/1901.10002) |
| September 6 | Bias | [Assigned reading - Bolukbasi et al. 2016](https://arxiv.org/abs/1607.06520)<br>[Supplementary reading - Arteaga et al. 2019](https://arxiv.org/abs/1901.09451)|
| September 8 | Out of distribution | Covariate, label & concept shifts<br>[Slides](https://www.cis.upenn.edu/~exwong/assets/debugml/distribution_shift_slides.pdf)<br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/distribution_shift.pdf)<br>[Assigned reading - Rabanser et al. 2019](https://arxiv.org/abs/1810.11953)|
| September 13 | Out of distribution | Measuring distribution shift <br>[Assigned reading - Riegar et al. 2019](https://arxiv.org/abs/1909.13584) |
| September 15 | Adversarial | Adversarial attacks <br>[Slides](https://www.cis.upenn.edu/~exwong/assets/debugml/adversarial_slides.pdf)<br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/adversarial.pdf)<br>[Assigned reading - Beery et al. 2018](https://arxiv.org/abs/1807.04975) |
| September 20 | No class |  |
| September 22 | Adversarial | Data poisoning, backdoors, Byzantine faults <br>[Assigned reading - Li et al. 2020](https://arxiv.org/abs/2004.09984)<br>[Supplementary reading - Rice et al. 2021](https://proceedings.neurips.cc/paper/2021/hash/ea4c796cccfc3899b5f9ae2874237c20-Abstract.html)<br>[Supplementary reading - Robey et al. 2022](https://arxiv.org/abs/2202.01136) |
| September 27 | Adversarial | Model stealing & membership inference <br> [Assigned reading - Nguyen et al. 2014](https://arxiv.org/abs/1412.1897)<br> [Assigned reading - Sinha et al. 2017](https://arxiv.org/abs/1710.10571)<br> [Supplementary reading - Tramer et al. 2016](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/tramer) <br>[Supplementary reading - Jagielski et al. 2020](https://arxiv.org/abs/1909.01838) |
| September 29 | Explainability | Data visualization, feature visualization, & interpretable models<br> [Slides](https://www.cis.upenn.edu/~exwong/assets/debugml/explainability_slides.pdf)<br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/explainability.pdf)<br>[Assigned reading - Javanmard et al. 2020](https://arxiv.org/abs/2002.10477) <br>[Assigned reading - Shamir et al. 2021](https://arxiv.org/abs/2106.10151)<br>[Assigned reading - Rudin 2019](https://arxiv.org/abs/1811.10154)|
|  |  |  |
| *Debugging models* |||
| October 4 | Explainability | Local & global explanations <br>*Project proposal due* <a href="https://www.cis.upenn.edu/~exwong/assets/debugml/proposal.pdf">Proposal guidelines</a><br>[Assigned reading - Wei et al. 2022](https://arxiv.org/abs/2201.11903) <br>[Assigned reading - Hassani et al. 2022](https://arxiv.org/abs/2201.05149)<br>  [Assigned reading - Dombrowski et al. 2019](https://arxiv.org/abs/1906.07983)<br>[Supplementary reading - Woods et al. 2019](https://arxiv.org/abs/1906.02896)|
| October 6 | Fall term break |  |
| October 11 | Explainability | Example-based & model visualizations  <br>[Assigned reading - Nguyen et al. 2016](https://arxiv.org/abs/1602.03616)<br>[Assigned reading - Slack et al. 2020](https://dl.acm.org/doi/abs/10.1145/3375627.3375830)<br>[Assigned reading - Ye & Durrett 2022](https://arxiv.org/abs/2205.03401)<br>[Supplementary reading - Jeanneret et al. 2022](https://arxiv.org/abs/2203.15636)|
| October 13 | Verification | Complete & incomplete <br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/verification.pdf)<br>[Assigned reading - Reddi et al. 2014](https://www.cs.cmu.edu/~sjakkamr/papers/doublyrobust.pdf)<br>[Assigned reading - Elazar et al. 2020](https://arxiv.org/abs/2006.00995)<br>[Assigned reading - Jacovi et al. 2021](https://arxiv.org/abs/2103.01378)|
| October 18 | Verification | Specifications and properties<br>[Assigned reading - Swayamdipta et al. 2020](https://arxiv.org/abs/2009.10795)<br>[Assigned reading - Ruan et al. 2022](https://arxiv.org/abs/2201.00057)<br>[Assigned reading - Zhang et al. 2021](https://arxiv.org/abs/2111.04986v1)<br>[Supplementary reading - Gowel et al. 2019](https://arxiv.org/abs/1810.12715)|
| October 20 | Scientific discovery |  Finding correlations<br>[Slides](https://www.cis.upenn.edu/~exwong/assets/debugml/scientific_discovery_slides.pdf)<br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/scientific_discovery.pdf)<br>[Assigned reading - Liu et al. 2018]( https://arxiv.org/abs/1811.00196)<br>[Assigned reading - Nori et al. 2019](https://arxiv.org/abs/1909.09223)<br>[Assigned reading - Kleinberg et al. 2018](https://www.cs.cornell.edu/home/kleinber/aer18-fairness.pdf)|
| October 25 | Scientific discovery | [Influence functions](https://arxiv.org/abs/1703.04730) & [data models](https://arxiv.org/abs/2207.05739)<br>[Assigned reading - Singla et al. 2021](https://arxiv.org/abs/2012.01750)<br>[Assigned reading - Xiao et al. 2020](https://arxiv.org/abs/2006.09994)<br>[Li et al. 2015](https://arxiv.org/abs/1506.01066)<br>[Supplementary reading - Yang et al. 2022](https://arxiv.org/abs/2202.05189) |
|  |  |  |
| *ML repair* |||
| October 27 | Robust learning | Robust training & overfitting, provable defenses (bound propagation & smoothing)<br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/robust_learning.pdf) <br>[Assigned reading - Chhabra et al. 2022](https://arxiv.org/abs/2210.01953) <br>[Assigned reading - Guo et al. 2022](https://www.nature.com/articles/s41598-022-06484-1)<br>[Assigned reading - Ye & Durrett 2022](https://arxiv.org/abs/2205.03401a)<br>[Supplementary reading - Carlini et al. 2022](https://arxiv.org/abs/2206.10550)<br>[Supplementary reading - Salman et al. 2021](https://arxiv.org/abs/2110.07719) |
| November 1 | Robust learning | Distributional robustness ([Domain generalization](https://arxiv.org/abs/2007.01434), [Group DRO](https://arxiv.org/abs/1911.08731), [IRM](https://arxiv.org/abs/1907.02893), [JTT](https://arxiv.org/abs/2107.09044))<br>[Assigned reading - Liang & Zou 2022](https://arxiv.org/abs/2202.06523)<br>[Assigned reading - Carter et al. 2020](https://arxiv.org/abs/2003.08907)<br>[Supplementary reading - Sagawa et al. 2019](https://arxiv.org/abs/1911.08731) |
| November 3 | Data interventions | Data balancing, [source selection](https://proceedings.mlr.press/v139/hashimoto21a.html), pruning hard examples <br>*Checkpoint due* <a href="https://www.cis.upenn.edu/~exwong/assets/debugml/checkpoint.pdf">Checkpoint guidelines</a><br>[Assigned reading - Recht et al. 2019](https://arxiv.org/abs/1902.10811)<br>[Supplementary reading - Idrissi et al. 2021](https://arxiv.org/abs/2110.14503)<br>[Assigned reading - Mariani et al. 2018](https://arxiv.org/abs/1803.09655)<br>[Assigned reading - Ribeiro et al. 2022](https://aclanthology.org/2022.acl-long.230/)<br>[Supplementary reading - Mariani et al. 2018](https://arxiv.org/abs/1803.09655)| 
| November 8 | Election day | Reading group only<br>[Assigned reading - Muller et al. 2021](https://arxiv.org/abs/2103.10158)<br>[Assigned reading - Lipton et al. 2018](https://arxiv.org/abs/1802.03916)<br>[Assigned reading - Baek et al. 2022](https://arxiv.org/abs/2206.13089 ) |
| November 10 | Data interventions | Data augmentations (classical, [subgroups](https://arxiv.org/abs/2008.06775) & generative) <br>[Slides](https://www.cis.upenn.edu/~exwong/assets/debugml/interventions_slides.pdf)<br>[Lecture notes](https://www.cis.upenn.edu/~exwong/assets/debugml/interventions.pdf)<br>[Assigned reading - Meng et al. 2022](https://arxiv.org/abs/2202.05262 )<br>[Assigned reading - Schwartz et al. 2022](https://arxiv.org/abs/2204.12708)<br>[Supplementary reading - Sorscher et al. 2022](https://arxiv.org/abs/2206.14486)|
| November 15 | Model adjustments | Model [edit](https://arxiv.org/abs/2110.11309)[ing](https://arxiv.org/abs/2112.01008) and [fine-tuning](https://arxiv.org/abs/2207.02842)<br>[Assigned reading - Muller et al. 2021](https://arxiv.org/abs/2211.00241) <br>[Assigned reading - Jiang et al. 2021](https://arxiv.org/abs/2106.13799)<br>[Supplementary reading - Muller et al. 2021](https://arxiv.org/abs/2203.07320)|
| November 17 | Model adjustments | Model [patching](https://arxiv.org/abs/2008.06775) & [repair](https://arxiv.org/abs/2005.09912) <br>[Supplementary reading - Barratt et al. 2020](https://arxiv.org/abs/2001.11010)<br>[Supplementary reading - Sotoudeh et al. 2021](https://arxiv.org/abs/2104.04413)<br>[Supplementary reading - Liu et al. 2022](https://arxiv.org/abs/1912.03817)|
| November 22 | Ethics & Implications |  |
| November 24 | Thanksgiving |  |
| November 29 | NeurIPS |  |
| December 1 | NeurIPS |  |
| December 6 | Presentations | <a href="https://www.cis.upenn.edu/~exwong/assets/debugml/final_presentation.pdf">Presentation guidelines</a> |
| December 8 | Presentations |  |
| December 13 | Reading period |  |
| December 15 | Final examinations | |
| December 22 | Term ends | *Final report due* <a href="https://www.cis.upenn.edu/~exwong/assets/debugml/final_report.pdf">Final report guidelines</a> |

There is no official textbook for this course, but you may find the following references to be useful: 
+ [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/) by Christoph Molnar
+ [Trustworthy Machine Learning](http://www.trustworthymachinelearning.com/) by Kush R. Varshney
<!-- There are no specific course requirements. The course assumes a background in machine learning, such as an introductory course. , and have some basic programming experience for the course project. -->

<!-- (healthcare, autonomous driving, agriculture, logistics, energy, etc.)  -->