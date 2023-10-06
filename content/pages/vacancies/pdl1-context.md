title: Improving PD-L1 digital pathology image analysis
groups: pathology, diag
closed: false
type: student
picture: vacancies/pdl1-project.png
template: vacancy-single
people: Francesco Ciompi, Leander van Eekelen
description: Development of deep learning methods to characterize PD-L1 positive cells in lung cancer immunohistochemistry for automatic biomarker extraction

## Clinical Problem
Immunotherapy is increasingly becoming the standard of care for late-stage non-small cell lung cancer (NSCLC) patients, utilizing an approach that harnesses the body’s own immune system to combat cancer. However, not all NSCLC patients have an equal response to immunotherapy; only approximately 30-40 percent of patients derive clinical benefit. The current patient selection criterion in the clinic is based on the quantification of the expression of PD-L1, a protein targeted by most immunotherapy drugs. This expression is quantified by pathologists in immunohistochemistry (IHC) of histology slides, who have to estimate the proportion of PD-L1 positive tumor cells over all tumor cells (so-called “tumor proportion score”, TPS). Studies have shown that the TPS has only a modest predictive value (AUC=0.65, Lu et al., 10.1001/jamaoncol.2019.1549), but still, it is the only one that is available in the clinic and used every day to select patient for immunotherapy treatment. Because of this, the scientific community is in constant search for improved predictive biomarkers. 

## Solution
Despite the modest predictive value of TPS, positivity of tumor cells to PD-L1 has been shown to play a role in the tumor-immune reaction mechanism. Furthermore, studies have shown that spatial arrangement of the tumor microenvironment has superior predictive power over TPS alone (Ghiringhelli et al., 10.1016/j.ebiom.2023.104633). Therefore, automatic analysis at single-cell level in PD-L1 staining via detection or segmentation technique is a necessary building block for the design of improved biomarkers based on spatial analysis. 

## Approach
In this project, we will develop AI techniques for multi-class cell detection and segmentation in PD-L1 stained histopathology slides. The Computational Pathology Group has done preliminary work on this topic using the popular YOLOv5 framework (https://github.com/ultralytics/yolov5). However, this work has highlighted two shortcomings: i) the model struggles significantly with cell types that can only be distinguished by considering them in relation to other cells, suggesting the need for a contextual information injected into the cell detection framework; ii) the model does not generalize well to data originating from clinical centers outside of the training set. In this project, the YOLOv5-based approach will serve as a baseline, and we will investigate novel frameworks for PD-L1 analysis where contextual information can be exploited.  

## Data
The student working on this project will have access to an existing dataset of over 500.000 individually annotated cells within approximately 150 PD-L1 stained IHC digital pathology images of NSCLC. This dataset will be used to train and validate their algorithms. Experiments will be run on a large GPU cluster managed by the Diagnostic Image Analysis Group. Supervision will be performed by Leander van Eekelen (PhD candidate) and Francesco Ciompi, members of the Computational Pathology group of the Radboudumc.


## Requirements
-	Students with a major in computer science, biomedical engineering, artificial intelligence, physics, or a related area in the final stage of master level studies are invited to apply.
-	Affinity with programming in Python, specifically in the PyTorch framework.
-	Interest in deep learning and medical image analysis.

## Information
-	Project duration: 6 months
-	Location: Radboud University Medical Center
-	For more information, please contact [Leander van Eekelen](mailto:leander.vaneekelen@radboudumc.nl)
