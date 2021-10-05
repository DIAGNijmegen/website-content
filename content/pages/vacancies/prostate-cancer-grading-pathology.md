title: Extending a prostate cancer grading algorithm to other surgical entities
groups: ai-for-health
closed: true 
type: student 
picture: vacancies/scoliosis_modeling.jpg
template: vacancy-single
people: Khrystyna Faryna, Geert Litjens
description: Develop a method to extend a prostate cancer grading algorithm to other surgical entities

**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical Problem 
In prostate disease, biopsies, small tissue specimens, play a prominent role in the early detection and staging of cancer. Radical prostatectomy, complete surgical removal of the prostate, is typically performed as a curative treatment following a biopsy positive for prostate cancer. Radical prostatectomies result in enormous amounts of tissue for the pathologist to analyse.

Prostatectomy specimens need to be fully graded to allow determination of an adequate follow-up strategy for the patient. For example, a small high-grade component of cancer might be present that alters the treatment strategy and was missed on initial biopsy. Our group has developed a prostate cancer grading algorithm for biopsy samples [1]. Next, we plan to extend this algorithm to prostatectomy data. From an algorithmic perspective, analysis of prostatectomy specimens is challenging due to the presence of a wide variation of tissue, some of which only appear in a fraction of cases. Examples include the seminal vesicles, surrounding fat, nerves, muscle, and large blood vessels, among others. These tissue types are also rarely sampled in biopsies, such that our biopsy-trained algorithm fails on those cases.

## Solution 
A variety of approaches can be used to tackle this problem. Transfer learning from prostate biopsy grading algorithm can be used to initialize the weights of a prostatectomy grading algorithm. Subsequently, we can use active learning to iteratively enrich the training dataset with various tissue types, depending on which of them throws off the algorithm the most. Alternatively, we can use a continual learning to train a network to grade prostatectomies without losing its performance on biopsy grading task. In order to ensure training data contains adequate tissue variability, we will use ‘spatial hard-negative mining’ to monitor misclassifications in normal tissue during training time in a location-aware manner and sample data accordingly.

## Data 
In this project we plan to combine data from a public dataset PANDA and inhouse dataset of prostatectomy slides.

## Results
The algorithm will be made publically available as a Docker container on https://grand-challenge.org/.

## Embedding 
The student will be supervised by a research member of the Diagnostic Image Analysis Group and Computational Pathology Group whose research is dedicated to analyses of histopathological slides with deep learning techniques. We have a strong collaboration with pathology experts in the field of cancer grading. The student will have access to a large GPU cluster.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics in the final stages of their Master education. 
- You should be proficient in python programming and have a theoretical understanding of deep learning architectures. 
- Basic biological / biomedical knowledge is preferred.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- More information can be obtained from Khrystyna Faryna (mailto: khrystyna.faryna@radboudumc.nl)
