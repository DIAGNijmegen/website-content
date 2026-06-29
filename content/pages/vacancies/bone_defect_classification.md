title: Supervised and unsupervised classification of bone defects in revision total knee arthroplasty
groups: rtc, diag
closed: true
type: student
picture: vacancies/tka.jpeg
template: vacancy-single
people: Aiik Biermans, Petra Heesterbeek
description: Using AI to classify bone defects in revision total knee arthroplasty

## Background

Knee osteoarthritis (OA) is a degenerative disease of the knee joint characterized by a decrease in cartilage thickness, which often leads to pain and reduced range of motion. In advanced stages, the joint may be replaced with a total knee arthroplasty (TKA). While TKA is generally successful, it is not always a permanent solution; when an implant fails, a revision total knee arthroplasty (rTKA) becomes necessary.

rTKA is technically demanding and costly, with outcomes often inferior to primary TKA. Surgeons must navigate complex bone defects resulting from the failure and extraction of the primary implant, which complicates the fixation of the revision implant. Currently, the Anderson Orthopaedic Research Institute (AORI) classification system is the clinical standard for describing these defects. However, this system suffers from low inter-observer reliability and provides little predictive value for complex three-dimensional (3D) bone defects due to its subjective nature [1]. There is a critical need for an automated, objective, and reproducible 3D-based classification system that accounts for defect volume and shape to support clinical decision-making and surgical planning.  

## Approach

The objective of this project is to develop supervised and/or unsupervised 3D-based classification systems using AI techniques to overcome the limitations of traditional systems [2].

The student will focus on processing unstructured 3D data, such as meshes or point clouds of tibial defects, and extracting meaningful features for classification. Key activities include:

- Applying techniques such as Graph Neural Networks (GNNs) or Statistical Shape Models (SSMs) to learn shape-related features like volume and topology. 
- Utilizing clustering algorithms to group defects into categories that allow for the automatic allocation of new clinical cases.  
- Integrating augmentation strategies (e.g., stems, cones, sleeves) into the model to enhance predictive classification.  
- Applying Explainable AI (XAI) methods to highlight the anatomical features determining classification, ensuring clinical transparency.  
- Validating the clinical relevance of these clusters through collaboration with experienced surgeons and comparing the results against the AORI gold standard.  

## Data

The dataset includes 3D manifold surface meshes of tibial bone defects derived from anonymized CT imaging. Approximately 100 tibial defect shapes are currently available, with the potential to generate up to 500 models using automated processing. Additionally, the project has access to paired surgery reports containing intra-operative AORI classifications, implant types, and the augmentations used, which can be utilized for supervised training and validation.  

## References

[1] Khan, Y., Arora, S., Kashyap, A. et al. Bone defect classifications in revision total knee arthroplasty, their reliability and utility: a systematic review. Arch Orthop Trauma Surg 143, 453-468 (2023).

[2] Brenneis, M., Flevas, D.A., Braun, S., Sculco, P.K. & Boettner, F. Imaging in revision total knee arthroplasty: a novel 3D classification system for tibial bone defects. Knee Surgery, Sports Traumatology, Arthroscopy, 32, 323-333 (2024).

## Requirements

Students in the final phase of a Master’s program in Artificial Intelligence, Computer Science, Biomedical Engineering, or a related field are invited to apply.

**Required skills:**

-	Experience with Python programming
-	Interest or experience in machine learning and/or statistical shape analysis techniques 
-	Familiarity with 3D data processing
-	Ability to work in a multidisciplinary environment involving clinical collaboration

## Information

**Project duration:** 6 months
**Location:** Radboud University Medical Center / Sint Maartenskliniek

The student will be officially embedded in the Orthopaedic Research Lab at Radboudumc, working in close collaboration with the Sint Maartenskliniek. A high-performance workstation is available for the project. 

If you are interested in applying for this Master student project, please send an email to: rtcai@radboudumc.nl.  
