title: Individualised endometrial cancer risk stratification by Bayesian prediction model (ENDORISK), optimizing the model for clinical implementation
groups: ai-for-health
closed: false
type: student
picture: vacancies/ENDORISK.jpg
template: vacancy-single
people: Marike Lombaers, Hanny Pijnenborg, Peter Lucas
description: Develop a Bayesian model for individualised endometrial cancer risk stratification

## Clinical problem
ENDORISK is a powerful Bayesian network predicting LNM and disease-specific survival (DSS). It was
developed in the European Network for Individualized Treatment of Endometrial Carcinoma (ENITEC) by integrating preoperative clinical, histopathological, molecular and serum markers of EC patients (n=763). For the prediction of LNM, external validation demonstrated better diagnostic
performance of the ENDORISK model compared to current guideline-based selection, area under the
curve (AUC) of 0.828, (95%-confidence interval [CI] 0.76-0.88) and 0.646, 95%-CI 0.56-0.73
respectively, also specifically for grade 3 EC, AUC 0.742, 95%-CI 0.62-0.87). An important advantage of the ENDORISK model is that it incorporates easily accessible biomarkers. The use of ENDORISK could assist clinical decision making especially in frail elderly and patients with co-morbidities, and is supported by patient advocacy groups, and clinicians working in the field.

The dynamic aspects of Bayesian networks such as ENDORISK allow continuous improving by
machine-learning with new data, and refine the individualized prediction of adjuvant treatment as well,
that can further be improved with data of large cancer registry data. As the molecular profiling according to The Cancer Genome Atlas (TCGA) has gained increased interest in defining the adjuvant therapy, integrating these TCGA molecular subgroups into the ENDORISK network is an important step towards continuous improving the network and facilitate clinical use beyond gynecologists.

We therefore aim to train the ENDORISK model with recently acquired data of the four TCGA molecular subgroups within the original cohort. Furthermore we need to internally and externally train the Bayesian network to use the updated version for an implementation study of the ENDORISK network in clinical practice in three oncological regions in the Netherlands (GOCN, GOCZ, and GOZON). 

## Solution
The four molecular subgroups (POLE mutated, MSI mutated, copy number low and copy number high) need to be implemented into the Bayesian network in relation to lymph node metastases and in relation to outcome (i.e. survival) and adjuvant therapy (i.e. chemotherapy, radiation). 

First the Bayesian network will need to be updated with the new variables.  This will require a plan on how to update parts of the Bayesian network, keeping other parts the same. As additional datasets will also become available, a scientific plan on how to update network structure and probability distributions (e.g. using Bayesian updating using prior Dirichlet  distributions) is required. Subsequently the plan is evaluated experimentally using synthetic data and the real-world dataset on endometrial cancer. Finally, the ENDORISK Bayesian network is updated with the extra variables, the structure and probability distributions are updated following the plan developed in the previous steps. Internal and external validation is carried out to obtain insight into the performance of the updated ENDORISK Bayesian network, and results are compared to the original Bayesian network. External validation on at least two other cohorts is required.

## Data
We have a training cohort of 245 patients and internal validation set of 763 patients. For external validation, several datasets can be used.

## Results
The updated Bayesian model will be used in the clinical implementation study (KWF (Dutch Cancer Association) grant awarded) at the Radboudumc and other hospitals in the oncological region of Nijmegen (GOCN), Eindhoven (GOCZ) and Maastricht (GOZON) by the departments of Obstetrics and Gynaecology. We aim to be able to implement the ENDORISK model in actual clinical care if the implementation study shows significant improvement of care. Marike Lombaers is currently employed as a PhD-Candidate at the department of Obstetrics and Gynaecology to manage and execute the implementation study and associated studies.

## Embedding
The student will be able to work at the department of Obstetrics and Gynaecology. Supervision by an expert in computer science and Bayesian networks in the context of healthcare is available from the Software Science Department of Radboud University (Peter Lucas).

## Requirements:
-	Experience with machine learning and Bayesian networks
-	Knowledge of programming with R and python
-	Affinity with healthcare processes


## Information
-	Project duration: 6 months 
-	Location: Radboud University Medical Center 
-	For more information or to apply for this project, please contact marike.lombaers@radboudumc.nl.
