title: Improving efficiency and accuracy of skin cancer diagnostics through implementation of ‘deep learning’-based tissue analysis
groups: ai-for-health
closed: true 
type: student 
picture: vacancies/skin-cancer-diagnostics.jpg
template: vacancy-single
people: Daan Geijs, Geert Litjens, Avital Amir, Lisa Hillen
description: Develop a method to improve the efficiency and accuracy of skin cancer diagnostics through implementation of ‘deep learning’-based tissue analysis

**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical Problem 
Due to the tripling of skin cancer incidence over the past two decades, more skin biopsies and resections are performed than ever before. This has led to an enormous increase in workload for pathologists, who perform the microscopic diagnostics of skin samples.
Both the biopsy and the resection need to be inspected by a pathologist, each typically consisting of multiple glass slides. Due to the increased incidence of skin cancer and the number of patients undergoing skin biopsies, the amount of work for pathologists has risen to unprecedented levels. At the Radboudumc at least 25% of all diagnostic tissue samples are now skin neoplasia, of which most are non-melanoma skin cancers. Of these, the number of basal cell carcinomas increased tenfold in the last twenty years. The increased workload is even worse in peripheral pathology labs that directly receive diagnostic material from GPs and primary care dermatologists. With the expected further increase in the incidence of skin cancer, this will become even more problematic in the future.
Most of the microscopic skin analysis is not professionally challenging, but it is time-consuming and can lead to reduced time for more complex diagnostics and increased wait time for patients. Machine learning and specifically deep learning offers a path to automating the diagnoses of skin samples, which would reduce the pressure on pathologists and the cost of diagnosis, both in time and money. 

## Solution 
This project focuses on integrating AI in the clinical workflow of the clinician. We are currently working on multiple applications that are suitable for pathologists and dermatologists . A dataset with single labels can be used to train and predict end-to-end BCC presence. This allows filtering out negative cases from the clinical workflow. For this, a deep learning algorithm needs to be deployed that can communicate with a medical image database. It will be implemented as a research component in the Sectra image management system (IMS) and viewer using the existing application program interface (API). Both pathologists at the RUMC and the UMCU use this system for daily diagnostics and have received training on how to use these systems. The student can work with Jesper Molin of Sectra Medical, who has a strong track record and a Ph.D. in user interface design for digital pathology. 
Another way of putting AI in the hands of a medical specialist is by using smartphone applications. A collaborative project with MUMC+ is to validate the use of automatic tumor segmentation during the microscopical examination of Mohs surgery. Normally this is done by a dermatologist, who has less experience than a derma pathologist. By attaching a smartphone to the ocular of a microscope, a video stream can be captured and segmented in real-time, adding expert pathologist predictions. 
Last, as in any diagnostic setting, sometimes very rare findings are present, for example, lymphoma in a resection specimen. As it is impossible to acquire enough data to train algorithms to find every single rare event, we will solve this using out-of-distribution detection algorithms. One algorithm which we have explored previously is Monte Carlo Dropout, where a network is asked to give multiple predictions for the same sample where randomly parts of the network are deactivated. It has been shown that if the network outputs become unstable, the sample is out-of-distribution and should be flagged for further inspection.

## Data 
We have a dataset of more than 4000 skin biopsies with multiclass labels, 300 fully annotated skin BCC resections. Next to that, we have more than 1500 frozen skin sections pooled from multiple centers. If the student's approach warrants it, the latter can be used for domain-adaptation techniques or cycle-consistent generative adversarial networks (cycleGANs), to combine it with the skin biopsies.

## Results
The project will be made publicly available as a Docker container on https://grand-challenge.org/. 
Next to this, the student is encouraged and supervised by writing and submitting an academic paper or abstract. 

## Embedding 
The student will be supervised by a research member of the Diagnostic Image Analysis Group whose research is dedicated to skin cancer diagnostics with deep learning techniques. 
We have a strong collaboration with both dermatology and pathology experts in the field of skin cancer, across multiple centers. The student will have access to a large GPU computation cluster. 
Next to that, the student will be part of a large group of Ph.D. students and Post-docs that have experience in deep learning techniques in the field of pathology. 

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics in the final stages of their Master education. 
- You should be proficient in python programming and have a theoretical understanding of deep learning architectures. 
- Basic biological / biomedical knowledge is preferred.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- More information can be obtained from Daan Geijs (mailto: daan.geijs@radboudumc.nl)
