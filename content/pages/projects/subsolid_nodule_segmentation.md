title: Automatic classification and segmentation of subsolid pulmonary nodules using deep learning
groups: ai-for-health
finished: false 
type: student
picture: vacancies/subsolid-nodule-segmentation-ai4h-21.png
template: project-single
people: Sanyog Vyawahare, Kiran Vaidhya Venkadesh, Colin Jacobs, Bram van Ginneken  
description: Development of deep learning algorithms for subsolid nodule analysis in CT.


**Start date: 01-08-2022** <br>
**End date: 28-02-2023**


## Clinical problem

Lung cancer is the leading cause of cancer death among both men and women, accounting for nearly 25% of all cancer deaths. While lung cancer typically shows up as pulmonary nodules on CT examinations, most nodules are benign and do not require further clinical workup. However, radiologist workload is expected to drastically increase soon with the widespread implementation of lung cancer screening programs. 
Therefore, accurate detection and characterization of pulmonary nodules are crucial for optimizing screening. 

Among the different types of nodules, subsolid pulmonary nodules are routinely encountered in screening and carry a higher malignancy risk. [Clinical reporting guidelines](https://www.acr.org/Clinical-Resources/Reporting-and-Data-Systems/Lung-Rads) recommend different management strategies based on the radiological appearance and biological behaviour of nodules. 
For subsolid nodules, the management decisions are dependent on accurate volumetric measurements and tracking the evolution of the solid cores of these nodules. 

![Segmentation example]({{ IMGURL }}/images/projects/subsolid-nodule-segmentation-ai4h-21.png)

The [Diagnostic Image Analysis Group (DIAG)](https://www.diagnijmegen.nl/) at Radboudumc has brought [Veolity](https://www.veolity.com/) to the market with MeVis Medical Solutions (Bremen, Germany). 
Veolity is a dedicated software solution for efficient reading of chest CT examinations in lung cancer screening programs. 
This product is actively used by several sites in North America, Europe, Asia, and Australia.
The software includes algorithms to detect, classify, and segment pulmonary nodules. However, the algorithms behind nodule type classification and segmentation are either outdated or are based on traditional image processing methods. 
Hence, there is a need to upgrade them into modern deep learning algorithms, which are becoming [increasingly prevalent](https://www.sciencedirect.com/science/article/pii/S1361841517301135?via%3Dihub) in medical image analysis.


[comment]: <> (## Solution)

[comment]: <> ({DESCRIBE THE MAIN RESULT OR INNOVATION OF THE PROJECT AND HOW IT WILL BE INTEGRATED IN RADBOUDUMC ROUTINE CARE})

## Data

DIAG has a scientific archive of over 100,000 chest CT examinations including data from several lung cancer screening trials. For this project, we have curated images and labels for:

* Nodule type classifier: 1,352 nodules from [MILD](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6637372/) for development and 453 nodules from [DLCST](https://pubmed.ncbi.nlm.nih.gov/26485620/) for external validation, as previously described in a [publication](https://www.nature.com/articles/srep46479). 
* Subsolid nodule segmentation: 200 screen-detected malignant nodules from [NLST](https://www.nejm.org/doi/full/10.1056/nejmoa1102873) with voxel-level labels for the solid-core and the subsolid regions for development, and 170 screen-detected nodules from the MILD trial for external validation. In addition, we have voxel-level labels for ~20,000 nodules from the NLST which may be used to increase the robustness of the segmentation algorithm.


## Approach

The two main tasks within this project:

* Develop deep learning algorithm(s) to automatically classify and segment subsolid nodules.
* Ensure the algorithm(s) are fast enough to process a single nodule within 0.5 seconds.

Using the previously published [nodule type classifier](https://www.nature.com/articles/srep46479) and retraining the system with more modern convolutional neural networks, preferably starting with the ResNet50 and I3D based nodule malignancy classifier described [here](https://pubs.rsna.org/doi/full/10.1148/radiol.2021204433). 
Then working with [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z) framework as the baseline for segmenting sub-solid nodules. External validation with unseen datasets will be performed once the development is frozen. 
If time permits, experiments with a unified framework that can classify and segment a nodule in a single shot will be undertaken. Finally, overall care must be taken to minimize computational overhead and ensure that all processing happens within 0.5 seconds. 
This will enable smooth integration with [CIRRUS Lung Screening](https://www.diagnijmegen.nl/software/cirruslungs/) (the research prototype version of Veolity).

[comment]: <> (## Results)

[comment]: <> ({DESCRIBE THE RESULTS OF THE PROJECT})