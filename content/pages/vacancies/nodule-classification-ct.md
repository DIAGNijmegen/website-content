title: Deep learning for fully automated classification of pulmonary nodules
groups: diag
closed: true
type: student
picture: vacancies/nodule-classification.png
template: vacancy-single
people: Kiran Vaidhya Venkadesh, Ward Hendrix, Colin Jacobs
description: Development of deep learning algorithms for nodule classification in CT.
bibkeys: Ciom17a

## Clinical problem
Lung cancer is the leading cause of cancer death among both men and women, accounting for nearly 25% of all cancer deaths. While lung cancer typically shows up as pulmonary nodules on CT examinations, most nodules are benign and do not require further clinical workup. However, radiologist workload is expected to drastically increase soon with the widespread implementation of lung cancer screening programs. Therefore, accurate detection and characterization of pulmonary nodules are crucial for optimizing screening. 

The [Diagnostic Image Analysis Group (DIAG)](https://www.diagnijmegen.nl/) at Radboudumc has brought [Veolity](https://www.veolity.com/) to the market with MeVis Medical Solutions (Bremen, Germany). Veolity is a dedicated software solution for efficient reading of chest CT examinations in lung cancer screening programs. This product is actively used by several sites in North America, Europe, Asia, and Australia. The software includes algorithms to detect, classify, and segment pulmonary nodules.

In previous publications, we have analyzed the performance of a deep learning system for nodule classification on two screening datasets from Italy and Denmark ([paper](https://www.nature.com/articles/srep46479)). It is at present unclear how this deep-learning based classification system performs on heterogeneous CT data collected from routine clinical practice.

## Solution
You have two main tasks within this project:

* Train and improve deep learning algorithm(s) to automatically classify pulmonary nodules.
* Validate performance on an extensive set of clinical CT scans.

You will begin by taking the previously published [nodule type classifier](https://www.nature.com/articles/srep46479) and retrain the system with more modern convolutional neural networks, preferably starting with the ResNet50 and I3D based nodule malignancy classifier described [here](https://pubs.rsna.org/doi/full/10.1148/radiol.2021204433). Then, you will perform external validation with unseen datasets once the development is frozen. Finally, you will analyze the weak points of the trained system and explore techniques how to improve performance.

## Data
DIAG has a scientific archive of over 100,000 chest CT examinations including data from several lung cancer screening trials. For this project, we have curated images and labels for:

* 1,352 nodules from [MILD](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6637372/)
* 453 nodules from [DLCST](https://pubmed.ncbi.nlm.nih.gov/26485620/)
* A clinical set of nodules from 100 CT scans at Radboudumc and 100 CT scans from JBZ, extensively annotated by 5 thoracic radiologists
* ~1200 nodules from [LIDC/IDRI](https://pubmed.ncbi.nlm.nih.gov/21452728/), extensively annotated by 4 radiologists
	
## Results
The algorithm(s) that come out of this project will be made publicly available for research use as Docker containers through the [grand-challenge.org](https://grand-challenge.org/algorithms/) platform, and may be integrated with [CIRRUS Lung Screening](https://www.diagnijmegen.nl/software/cirruslungs/) (the research prototype version of Veolity). You are encouraged to write a scientific publication describing your results.

## Embedding
You will be embedded in the Diagnostic Image Analysis Group and will be supervised by a research member whose research is dedicated to [AI for lung cancer](https://www.diagnijmegen.nl/research/lung-cancer-image-analysis/). We have a strong collaboration with both clinical and radiological experts. You will also have access to a Deep Learning GPU Cluster ([SOL](https://www.diagnijmegen.nl/software/sol/)) to run deep learning experiments.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics, Biomedical Engineering or similar in the final stages of their Master education. 
- You should be proficient in Python programming and have a theoretical understanding of deep learning architectures.
- Experience with medical images is beneficial.

## Information 
- Project duration: 3, 6 or 9 months 
- Location: Radboud University Medical Center 
- For more information or to apply for this project, please contact [Colin Jacobs](https://www.diagnijmegen.nl/people/colin-jacobs/)
