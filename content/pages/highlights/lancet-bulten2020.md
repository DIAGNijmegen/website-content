title: CPG's work on Automated Gleason Grading using Deep Learning published in The Lancet Oncology 
date: 2020-01-08
description: The Gleason score suffers from significant inter-observer variability. This problem could be solved by the fully automated deep learning system developed by Wouter Bulten and his colleagues. Their work appeared online today in The Lancet Oncology. 
picture: news/lancet_I.png
groups: diag, pathology

With 1.2 million new prostate cancer cases each year, a high incidence-to-mortality ratio, and risk of overdiagnosis and overtreatment, there is a strong need for accurate assessment of patient prognosis. Currently, the Gleason score, assigned by a pathologist after microscopic examination of cancer morphology, is the most powerful prognostic marker for prostate cancer patients. However, it suffers from significant inter- and intra-observer variability, limiting its usefulness for individual patients.

As an alternative, [member/wouter-bulten] et al developed a fully-automated cancer detection and Gleason grading system for entire prostate biopsies. The system was developed using 5759 biopsies from 1243 patients. A semi-automatic labeling technique was used to circumvent the need for manual pixel-level annotations. The study was focussed on the full range of Gleason grades, and evaluated on a large cohort of patients with an expert consensus reference standard and an external tissue microarray test set. Their work was accepted for publication by <a href="https://www.thelancet.com/journals/lanonc/home">The Lancet Oncology</a> and appeared <a href="https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30739-9/fulltext">online</a> today. 

![Deep learning system Gleason grading]({static}/images/news/Lancet_II.png)

The figure above depicts the development of the deep learning system. The authors employed a semi-automated method of labelling the training data (top row), removing the need for manual annotations by pathologists. The final system can assign Gleason growth patterns on a cell-level.

The developed system achieved a high agreement with the reference standard (quadratic kappa 0.918). In a separate observer experiment, the deep learning system outperformed 10 out of 15 pathologists in agreement with the reference standard. The system was validated on an external test set where it achieved an AUC of 0.977 on distinguishing between benign and malignant biopsies and an AUC of 0.871 using grade group 2 as a cut-off.


Click <a href="https://www.computationalpathologygroup.eu/software/automated-gleason-grading/">here</a> to try Wouter's algorithm on your own data and learn more about the project on automated Gleason grading.




