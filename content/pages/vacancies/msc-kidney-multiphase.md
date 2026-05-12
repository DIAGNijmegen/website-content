title: Multi-phase AI for kidney cancer
groups: diag
closed: false
type: student 
picture: vacancies/msc-kidney-multiphase.png
template: vacancy-single
people: Sarah de Boer, Alessa Hering
description: Develop a method that incorporates multiple CT contrast phases for kidney cancer

## Background 

Our team is developing an AI-based pipeline for segmenting and classifying renal masses (also called lesions) in computed tomography (CT) scans. For patients with suspicion of kidney  cancer, a multi-phase CT scan is commonly used to diagnose and stage the cancer. Multi-phase CT  refers to an imaging protocol where a contrast agent is given to the patient and at subsequent  timepoints a CT scan is made. The contrast agent goes through the body and depending on the time  point, different organs are enhancing. These enhancements allow radiologists to assess organs for  tumors or other findings. At the moment, the AI models we have built and are common in the  literature, only take one contrast-phase CT scan as input. We would like to investigate whether it is  beneficial for AI models to input multiple contrast phases. 

This project will be embedded in the [COMFORT project](https://comfort-ai.eu) which aims to  develop robust and trustworthy multimodal AI systems to enhance clinical outcomes for prostate  and kidney cancer patients. Our goal is to create internationally and interdisciplinarily validated  decision support systems that improve clinical prognosis, patient stratification, and individualized  therapy options. 

## Goal

Develop a method that incorporates multiple CT contrast phases for kidney cancer. 

## Method

In recent literature [1,2,3,4,5], multiple methods for leveraging multi-phase CT in AI have been proposed.  Most of the work apply their strategies to liver cancer, as open data is available, or it is applied to  kidney cancer, but the models are unfortunately not publicly available. Therefore, the first step  would involve researching these methods and picking a promising approach. Next, the chosen  method needs to be built, likely from scratch. However, for baseline methods we have code  available for single phase models, which can be used to compare the developed method to. If time  allows, proposing a new strategy for improving the existing methods is possible. 

## Student requirements 

- Experience with / interest in: AI, deep learning, medical image analysis, building AI models from  scratch in Pytorch, strong mathematical foundation of deep learning methods 
- Type of project: master thesis
- Expected time frame: 6 months

## Literature

[[1]](https://doi.org/10.1109/JBHI.2022.3219123) Uhm K-H, Jung S-W, Choi MH, Hong S-H, Ko S-J (2022). A Unified Multi-Phase CT Synthesis and Classification Framework for Kidney Cancer Diagnosis With Incomplete Data. _IEEE Journal of Biomedical and Health Informatics_. 26(12): 6093–6104.  

[[2]](https://doi.org/10.1038/s41698-021-00195-y) Uhm K-H, Jung S-W, Choi MH, Shin H-K, Yoo J-I, Oh SW, Kim JY, Kim HG, Lee YJ, Youn SY, Hong S-H, Ko S-J (2021). Deep learning for end-to-end kidney cancer diagnosis on multi-phase abdominal computed tomography. _NPJ Precision Oncology_. 5(1): 54.  

[[3]](https://doi.org/10.1148/radiol.232178) Dai C, Xiong Y, Zhu P, Yao L, Lin J, Yao J, Zhang X, Huang R, Wang R, Hou J, Wang K, Shi Z, Chen F, Guo J, Zeng M, Zhou J, Wang S (2024). Deep Learning Assessment of Small Renal Masses at Contrast-enhanced Multiphase CT. _Radiology_. 311(2): e232178.  

[[4]](https://doi.org/10.1007/s00330-021-07803-2) Kim DW, Lee G, Kim SY, Ahn G, Lee J-G, Lee SS, Kim KW, Park SH, Lee YJ, Kim N (2021). Deep learning–based algorithm to detect primary hepatic malignancy in multiphase CT of patients at high risk for HCC. _European Radiology_. 31(9): 7047–7057.  

[[5]](https://doi.org/10.48550/arXiv.2108.00911) Zhang Y, Peng C, Peng L, Huang H, Tong R, Lin L, Li J, Chen Y-W, Chen Q, Hu H, Peng Z (2021). Multi-phase Liver Tumor Segmentation with Spatial Aggregation and Uncertain Region Inpainting. _arXiv_. arXiv:2108.00911.

## Information 

For more information, see the full vacancy [here](https://www.ru.nl/en/students/news/ellis-excellence-fellowships-apply-now-for-a-project-0#13).