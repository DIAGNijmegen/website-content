title: Universal lesion tracking in whole-body longitudinal CT imaging
groups: diag
closed: false
type: student
picture: vacancies/lesion_tracking.png
template: vacancy-single
people: Xuan Loc Pham, Alessa Hering
description: Evaluation of multi-organ CT registration models for lesion tracking across timepoints

## Clinical Motivation
Image registration is the process of aligning two or more images to achieve pointwise spatial correspondence. By establishing spatial correspondences between multiple images, it aligns anatomical structures and facilitates the automatic quantification of findings in subsequent imaging examinations. This saves radiologists a significant amount of time while ensuring accurate and efficient patient care. 

This project will explore the application of image registration for universal lesion tracking in whole-body longitudinal CT scans acquired at different time points. Conventional registration methods perform consistently across various anatomical structures but are often limited in clinical practice due to their runtime. Meanwhile, existing learning methodologies are predominantly tailored to a specific organ of interest and often exhibit lower performance on other organs, thus limiting their generalizability and applicability.

## Objectives / Aims / Goals
**Primary objective**:
- Evaluate the performance of recent open-source algorithms for universal image registration, together with unsupervised learning single-organ registration models, and compare them to our in-house multi-organ registration model
- Apply on a longitudinal whole-body CT dataset for universal lesions tracking

**Further goals** (depending on project scope, student interests, literature findings, and initial conclusions):
- Integrate the tracking results into our in-house universal lesions segmentation pipeline
- Develop an improved version of the in-house registration model, focusing more on the diffeomorphism 

## Dataset
- This study is based on two large-scale longitudinal whole-body CT datasets
- The internal dataset includes 591 pairs for training and 104 pairs for evaluation. The test set already contains labels for 14 anatomical structures verified by medical experts 
- The public dataset can be downloaded from the AutoPET challenge, which includes keypoints for multiple lesions at different time points 

## Requirements
- Master students with a major in computer science, artificial intelligence, mathematics, biomedical engineering, technical medicine, physics, or a related area in the final stage of master's studies
- Experience with programming in Python
- Experience in deep learning, medical imaging, and/or medical image analysis

## Practical Information
**Project Duration**: 6 or 12 months, starting September 2025.

**Location**: Department of Medical Imaging, Radboud University Medical Center, Nijmegen

**For more information**, please contact Loc Pham or Alessa Hering.

**Application**: Please send your CV, grade list and motivation letter (maximum of 1 A4 page) to xuanloc.pham@radboudumc.nl or Alessa.Hering@radboudumc.nl .

## Suggested Reading

1.	Pham, X.L., Prokop, M., van Ginneken, B., Hering, A., 2025. Divide to conquer: A field decomposition approach for multi-organ whole-body ct image registration, in: SPIE Medical Imaging: Image Processing 2025 (SPIE MI25). https://doi.org/10.1117/12.3046235
2.	Tian, L., Greer, H., Kwitt, R., Vialard, F.X., San Jose Estepar, R., Bouix, S., Rushmore, R., Niethammer, M., 2024. unigradicon: A foundation model for medical image registration, in: Medical Image Computing and Computer Assisted Intervention (MICCAI 2024), Cham. pp. 749–760. https://doi.org/10.1007/978-3-031-72069-7_70