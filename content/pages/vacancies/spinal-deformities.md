title: Automatic segmentation and identification of the vertebrae in CT scans of patients with spinal deformities
groups: ai-for-health
closed: true 
type: student 
picture: vacancies/scoliosis_modeling.jpg
template: vacancy-single
people: Nikolas Lessmann, Dennis Janssen, Max Bakker, Sebastiaan van de Groes
description: Develop a method to automatically segment and identify the vertebrae in CT scans of patients with spinal deformities

**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical Problem 
Segmentation and anatomical labeling of the vertebrae is an essential step in computerized analysis of the spine using CT and MR images. The goal of this analysis can be, for instance, detection of osteoporotic compression fractures of the vertebrae, quantification of spinal abnormalities related to chronic low back pain, or planning of surgical correction of idiopathic scoliosis. However, existing training data for automatic vertebra segmentation is limited to relatively normal spine shapes. In clinical practice, spinal deformities present therefore a serious challenge. The goal of this project is to improve the robustness to spinal deformities and thus bring automatic spinal analysis one step closer to clinical practice.

## Solution 
The project aims to model spinal deformities and develop a simulation framework for generating abnormal but realistic spine shapes. These synthetic deformities should be used to deform CT and MR images of normal spines and the corresponding existing segmentations. This data augmentation can then be integrated into a learning-based segmentation method to increase the robustness to spinal deformities. An existing spine segmentation method can be extended so that the project can focus on the simulation/modelling aspect.

## Data 
Public and private datasets with more than 400 CT scans and around 100 MR scans are available, together with reference segmentations and anatomical labels of the vertebrae. Additionally, at least 20 scans of patients with scoliotic spines are available and more will be collected from our PACS as part of the project.

## Results
The main result will be a model of spinal deformities, which can be used both to generate synthetic images with deformities but which can also be used in other spinal analysis projects to simulate different spine shapes. Practically, the project will also lead to an improved segmentation algorithm, in particular for scans of patients with scoliosis. Here, this algorithm can help plan surgical interventions and design patient-specific drilling templates. The final deliverable is a code repository on GitHub and a publicly available algorithm on the platform Grand Challenge.

## Embedding 
The student will be supervised by a research scientist from the Diagnostic Image Analysis Group, with expertise in deep learning and in particular spine segmentation and analysis in medical images, and by a research scientist from the Department of Orthopedics, with expertise in musculoskeletal modeling. An orthopedic surgeon will provide clinical expertise. For model development, we provide access to a large GPU computation cluster and an existing database of spine scans and reference annotations.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics in the final stages of their Master education. 
- You should be proficient in python programming and have a theoretical understanding of deep learning architectures. 
- Basic biological / biomedical knowledge is preferred.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- More information can be obtained from Nikolas Lessmann (mailto: nikolas.lessmann@radboudumc.nl)
