title: Automatic classification and segmentation of subsolid pulmonary nodules using deep learning
groups: ai-for-health, diag
finished: false
type: student
picture: vacancies/subsolid-nodule-segmentation-ai4h-21.png
template: project-single
people: Kiran Vaidhya Venkadesh, Bram van Ginneken, Colin Jacobs
description: We want to develop deep learning algorithms for classification and segmentation of subsolid pulmonary nodules from CT.

## Clinical problem
Lung cancer is the leading cause of cancer death among both men and women, accounting for nearly 25% of all cancer deaths. While lung cancer typically shows up as pulmonary nodules on CT examinations, most nodules are benign and do not require further clinical workup. However, radiologist workload is expected to drastically increase soon with the widespread implementation of lung cancer screening programs. Therefore, accurate detection and characterization of pulmonary nodules are crucial for optimizing screening. 

Among the different types of nodules, subsolid pulmonary nodules are routinely encountered in screening and carry a higher malignancy risk. [Clinical reporting guidelines](https://www.acr.org/Clinical-Resources/Reporting-and-Data-Systems/Lung-Rads) recommend different management strategies based on the radiological appearance and biological behaviour of nodules. For subsolid nodules, the management decisions are dependent on accurate volumetric measurements and tracking the evolution of the solid cores of these nodules. 

The [Diagnostic Image Analysis Group (DIAG)](https://www.diagnijmegen.nl/) at Radboudumc has brought [Veolity](https://www.veolity.com/) to the market with MeVis Medical Solutions (Bremen, Germany). Veolity is a dedicated software solution for efficient reading of chest CT examinations in lung cancer screening programs. This product is actively used by several sites in North America, Europe, Asia, and Australia. The software includes algorithms to detect, classify, and segment pulmonary nodules. However, the algorithms behind nodule type classification and segmentation are either outdated or are based on traditional image processing methods. Hence, there is a need to upgrade them into modern deep learning algorithms, which are becoming [increasingly prevalent](https://www.sciencedirect.com/science/article/pii/S1361841517301135?via%3Dihub) in medical image analysis.

![Segmentation example]({{ IMGURL }}/vacancies/subsolid-nodule-segmentation-ai4h-21.png)

## Solution
You have two main tasks within this project:
- Develop deep learning algorithm(s) to automatically classify and segment subsolid nodules.
- Ensure the algorithm(s) are fast enough to process a single nodule within 0.5 seconds.

You will begin by taking the previously published [nodule type classifier](https://www.nature.com/articles/srep46479) and retrain the system with more modern convolutional neural networks, preferably starting with the ResNet50 and I3D based nodule malignancy classifier described [here](https://pubs.rsna.org/doi/full/10.1148/radiol.2021204433). Then you will start with the [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z) framework as the baseline for segmenting sub-solid nodules. You must perform external validation with unseen datasets once the development is frozen. If time permits, you may experiment with a unified framework that can classify and segment a nodule in a single shot. Finally, overall care must be taken to minimize computational overhead and ensure that all processing happens within 0.5 seconds. This will enable smooth integration with [CIRRUS Lung Screening](https://www.diagnijmegen.nl/software/cirruslungs/) (the research prototype version of Veolity).

## Data
DIAG has a scientific archive of over 100,000 chest CT examinations including data from several lung cancer screening trials. For this project, we have curated images and labels for:
- Nodule type classifier: 1,352 nodules from [MILD](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6637372/) for training and 453 nodules from [DLCST](https://pubmed.ncbi.nlm.nih.gov/26485620/) for externally validation, as previously described in a publication. 
- Subsolid nodule segmentation: 200 screen-detected malignant nodules from [NLST](https://www.nature.com/articles/srep46479) with voxel-level labels for the solid-core and the subsolid regions for training, and 170 screen-detected nodules from the MILD trial for external validation. In addition, we have voxel-level labels for ~20,000 nodules from the NLST which may be used to increase the robustness of the segmentation algorithm.

Related publications:
- Charbonnier, JP., Chung, K., Scholten, E.T. et al. Automatic segmentation of the solid core and enclosed vessels in subsolid pulmonary nodules. Sci Rep 8, 646 (2018). https://doi.org/10.1038/s41598-017-19101-3
- Scholten, E.T., Jacobs, C., van Ginneken, B. et al. Detection and quantification of the solid component in pulmonary subsolid nodules by semiautomatic segmentation. Eur Radiol 25, 488–496 (2015). https://doi.org/10.1007/s00330-014-3427-z
- Ciompi, F., Chung, K., van Riel, S. et al. Towards automatic pulmonary nodule management in lung cancer screening with deep learning. Sci Rep 7, 46479 (2017). https://doi.org/10.1038/srep46479
	
## Results
The algorithm(s) that come out of this project will be made publicly available for research use as Docker containers through the [grand-challenge.org](https://grand-challenge.org/algorithms/) platform, and be integrated with [CIRRUS Lung Screening](https://www.diagnijmegen.nl/software/cirruslungs/) (the research prototype version of Veolity). You are encouraged to write a scientific publication describing your results.

## Embedding
You will be embedded in the Diagnostic Image Analysis Group and will be supervised by a research member whose research is dedicated to [AI for lung cancer screening](https://www.diagnijmegen.nl/projects/lung-cancer-screening/). We have a strong collaboration with both clinical and radiological experts in lung cancer screening. You will also have access to a Deep Learning GPU Cluster ([SOL](https://www.diagnijmegen.nl/software/sol/)) to run deep learning experiments.
