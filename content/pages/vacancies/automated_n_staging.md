title: Automatic nodal staging in lung cancer patients with PET/CT imaging
groups: diag
closed: true
type: student
picture: vacancies/NodalStaging.png
template: vacancy-single
people: Lars Leijten, Colin Jacobs
description: Development of an automatic nodal staging algorithm in lung cancer patients with PET/CT imaging

## Clinical Problem

Lung cancer is the leading cause of cancer-related death worldwide. Accurate staging is critical for treatment decisions and prognosis and is performed using the TNM classification system. TNM systematically describes the extent of cancer and categorizes each malignancy by the status of the primary tumor (T), nodal involvement (N) and metastatic disease (M). This project focuses on the assessment of the nodal involvement, the N-stage. FDG-PET/CT imaging is an important imaging procedure for N-staging, combining anatomical and metabolic information. 

Accurate assignment of the correct N-stage can be challenging for physicians, as it can be difficult to distinguish metastatic from non—metastatic lymph nodes. Recent AI algorithms based on deep learning show promise in improving staging accuracy. Yet, most models lack external validation, clinical interpretability, or public availability. This project aims to develop and evaluate an interpretable AI tool for lung cancer N-staging, addressing key limitations of current clinical and AI approaches.

## Objectives / Aims / Goals

The development of an AI algorithm based on a lung cancer segmentation tool and an anatomical region detection that can accurately predict the N-staging of lung cancer patients using FDG-PET/CT scans. 

## Study design

During this internship, the student will apply existing PET/CT lung cancer segmentation algorithms on a dataset of biopsy confirmed lung cancer cases from Radboudumc. Anatomical regions will be identified using TotalSegmentator – an existing algorithm for anatomy segmentation. The student will develop a system that automatically predicts the nodal staging in these patients. The predictions can be compared with the original FDG-PET/CT staging (clinical TNM stage) and the post-surgery staging (pathological TNM stage) as a ground truth.  

## Available data

The student will have access to an existing database with pseudononymized CT and FDG-PET/CT imaging of lung cancer patients in Radboudumc. For these patients, the clinical staging and the pathological staging is available as comparator and reference respectively. 

## Profile

We are looking for a Master student with a technical and scientific background (e.g. Data Science, AI, Biomedical Engineering, Physics, etc.).
The student should ideally bring:

1.	Proficiency in Python programming
2.	Experience working with the command line (e.g. Bash) and basic scripting
3.	Experience handling and preprocessing data files
4.	Prior experience with deep learning frameworks, specifically PyTorch
5.	Interest in medical imaging, clinical data, or AI applications in healthcare
6.	Ability to work independently and communicate results clearly 

## Learning outcomes

By the end of this internship the student will be able to:
1.	Apply and adapt models AI models for medical image analysis in a clinical research setting
2.	Work with real-world imaging data and clinical annotations
3.	Evaluate model performance using clinical ground truth and established standards of care
4.	Communicate findings in a scientific report and presentation

The results of this internship may contribute to a scientific publication, with the student considered for co-authorship based on the level of contribution.

## Timeline 

The estimated workload of this project is 6 months (30 EC). We prefer a student that is available to start in September 2025. Changes to the timeline can be considered based on the individual preferences and study requirements of the student. 

| Activity                                     | Timeline (weeks) |
|----------------------------------------------|------------------|
| Review of existing literature                | 1 – 4            |
| Getting familiar with department systems     | 1 – 4            |
| Implementing lung cancer segmentation algorithm | 5 – 10         |
| Implementing anatomical segmentation algorithm | 5 – 10         |
| Developing nodal staging system              | 10 – 14          |
| Predicting N-stage in Radboudumc cohort      | 14 – 16          |
| Analyzing results                            | 14 – 18          |
| Writing report and presenting results        | 18 – 20          |

## Response
If you are interested in this intership or want more information, please contact [member/Lars-Leijten] at [lars.leijten@radboudumc.nl](mailto:lars.leijten@radboudumc.nl).

## About DIAG
The Diagnostic Image Analysis Group (DIAG) at Radboudumc Nijmegen develops advanced, clinically driven AI tools to interpret medical images across multiple specialties—including radiology, pathology, cardiology, neurology, and oncology. 

Currently, over 70 PhD candidates and postdoctoral researchers are working at DIAG, developing and validating an assortment of AI algorithms used for medical image analysis. As a research group, DIAG offers access to a range of curated datasets, a self-hosted high-performance compute cluster and a range of experienced an motivated colleagues. Joining this team for you internship offers hands-on experience in clinical AI research, collaboration across disciplines and exposure to scientific innovation with clinical impact.

Visit our [website](https://www.diagnijmegen.nl/) for more information. 

