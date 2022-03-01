title: Automatic classification and segmentation of subsolid pulmonary nodules using deep learning
groups: ai-for-health
closed: false
type: student
picture: vacancies/subsolid-nodule-segmentation-ai4h-21.png
template: vacancy-single
people: Kiran Vaidhya Venkadesh, Bram van Ginneken, Colin Jacobs
description: Development of deep learning algorithms for subsolid nodule analysis in CT.
bibkeys: Char18, Ciom17a, Scho14d

**This is an AI for Health MSc project. Students are
eligible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical problem
Lung cancer is the leading cause of cancer death among both men and women, accounting for nearly 25% of all cancer deaths. While lung cancer typically shows up as pulmonary nodules on CT examinations, most nodules are benign and do not require further clinical workup. However, radiologist workload is expected to drastically increase soon with the widespread implementation of lung cancer screening programs. Therefore, accurate detection and characterization of pulmonary nodules are crucial for optimizing screening. 

Among the different types of nodules, subsolid pulmonary nodules are routinely encountered in screening and carry a higher malignancy risk. [Clinical reporting guidelines](https://www.acr.org/Clinical-Resources/Reporting-and-Data-Systems/Lung-Rads) recommend different management strategies based on the radiological appearance and biological behaviour of nodules. For subsolid nodules, the management decisions are dependent on accurate volumetric measurements and tracking the evolution of the solid cores of these nodules. 

![Segmentation example]({{ IMGURL }}/images/projects/subsolid-nodule-segmentation-ai4h-21.png)

The [Diagnostic Image Analysis Group (DIAG)](https://www.diagnijmegen.nl/) at Radboudumc has brought [Veolity](https://www.veolity.com/) to the market with MeVis Medical Solutions (Bremen, Germany). Veolity is a dedicated software solution for efficient reading of chest CT examinations in lung cancer screening programs. This product is actively used by several sites in North America, Europe, Asia, and Australia. The software includes algorithms to detect, classify, and segment pulmonary nodules. However, the algorithms behind nodule type classification and segmentation are either outdated or are based on traditional image processing methods. Hence, there is a need to upgrade them into modern deep learning algorithms, which are becoming [increasingly prevalent](https://www.sciencedirect.com/science/article/pii/S1361841517301135?via%3Dihub) in medical image analysis.

## Solution
You have two main tasks within this project:

* Develop deep learning algorithm(s) to automatically classify and segment subsolid nodules.
* Ensure the algorithm(s) are fast enough to process a single nodule within 0.5 seconds.

You will begin by taking the previously published [nodule type classifier](https://www.nature.com/articles/srep46479) and retrain the system with more modern convolutional neural networks, preferably starting with the ResNet50 and I3D based nodule malignancy classifier described [here](https://pubs.rsna.org/doi/full/10.1148/radiol.2021204433). Then you will start with the [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z) framework as the baseline for segmenting sub-solid nodules. You must perform external validation with unseen datasets once the development is frozen. If time permits, you may experiment with a unified framework that can classify and segment a nodule in a single shot. Finally, overall care must be taken to minimize computational overhead and ensure that all processing happens within 0.5 seconds. This will enable smooth integration with [CIRRUS Lung Screening](https://www.diagnijmegen.nl/software/cirruslungs/) (the research prototype version of Veolity).

## Data
DIAG has a scientific archive of over 100,000 chest CT examinations including data from several lung cancer screening trials. For this project, we have curated images and labels for:

* Nodule type classifier: 1,352 nodules from [MILD](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6637372/) for development and 453 nodules from [DLCST](https://pubmed.ncbi.nlm.nih.gov/26485620/) for external validation, as previously described in a [publication](https://www.nature.com/articles/srep46479). 
* Subsolid nodule segmentation: 200 screen-detected malignant nodules from [NLST](https://www.nejm.org/doi/full/10.1056/nejmoa1102873) with voxel-level labels for the solid-core and the subsolid regions for development, and 170 screen-detected nodules from the MILD trial for external validation. In addition, we have voxel-level labels for ~20,000 nodules from the NLST which may be used to increase the robustness of the segmentation algorithm.
	
## Results
The algorithm(s) that come out of this project will be made publicly available for research use as Docker containers through the [grand-challenge.org](https://grand-challenge.org/algorithms/) platform, and be integrated with [CIRRUS Lung Screening](https://www.diagnijmegen.nl/software/cirruslungs/) (the research prototype version of Veolity). You are encouraged to write a scientific publication describing your results.

## Embedding
You will be embedded in the Diagnostic Image Analysis Group and will be supervised by a research member whose research is dedicated to [AI for lung cancer screening](https://www.diagnijmegen.nl/projects/lung-cancer-screening/). We have a strong collaboration with both clinical and radiological experts in lung cancer screening. You will also have access to a Deep Learning GPU Cluster ([SOL](https://www.diagnijmegen.nl/software/sol/)) to run deep learning experiments.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics, Biomedical Engineering or similar in the final stages of their Master education. 
- You should be proficient in Python programming and have a theoretical understanding of deep learning architectures.
- Experience with medical images is beneficial.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- For more information or to apply for this project, please contact KiranVaidhya.Venkadesh@radboudumc.nl.
