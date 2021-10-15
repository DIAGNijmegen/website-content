title: Quantification of immunohistochemical markers for improved prostate cancer prognostics
groups: ai-for-health
closed: true 
type: student 
picture: vacancies/scoliosis_modeling.jpg
template: vacancy-single
people: Geert Litjens, Jolique van Ipenburg
description: Develop stain a method to quantify immunohistochemical markers for improved prostate cancer prognostics

**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical Problem 
In prostate cancer, patient treatment for a major part is determined by the subjective morphological

assessment of removed tissue, the Gleason Grade. However, we know that other biomarkers have

prognostic potential, such as cell division markers as a surrogate for tumor growth (Ki-67 staining) or

the presence and composition of immune infiltrates (CD3 / CD8 staining). However, these markers are

not used in practice because it is impossible to quantify them accurately across large swathes of tissues

by human experts. We propose to develop AI system which automatically quantify these biomarkers

and combines that with existing models for tumor segmentation and grading. This will allow us not just

to quantify the markers within digitized microscopy images, but also identify their spatial arrangement.

## Solution 
The student will need to adapt and improve existing methods to work across a variety of different

immohistochemical stains. Currently our group has both detection (YOLO) and segmentation (U-net)

based models for a single immunohistochemical stain (CD3) Improving these methods includes better

handling of overlapping and connecting cells and improving generalization to different counterstains

(e.g. brown, red, green).

## Data 
We have multi-center data with 4 immunohistochemical stains (CD3, CD8, PD-L1, Ki67) from around

400 patients. Data is source from Radboudumc, Rijnstate Hospital and Erasmus Medical Center. Each

patient has between 4 – 12 distinct whole-slide images for each stain. For each patient we have follow-

up data for at least 5 years (biochemical recurrence yes/no) with which we can correlate the obtained

cell counts.

## Results
The main innovation will be an IHC quantification algorithm that can generalize to a variety of IHC

stains with different staining profiles and counterstains. Such an algorithm would be valuable for many

clinical applications, although it would have to be further validated for different organs.

## Embedding 
The student will be supervised by a research member of the Diagnostic Image Analysis Group and Computational Pathology Group whose research is dedicated to analyses of histopathological slides with deep learning techniques. We have a strong collaboration with pathology experts in the field of cancer grading. The student will have access to a large GPU cluster.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics in the final stages of their Master education. 
- You should be proficient in python programming and have a theoretical understanding of deep learning architectures. 
- Basic biological / biomedical knowledge is preferred.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- More information can be obtained from Geert Litjens (mailto: geert.litjens@radboudumc.nl)
