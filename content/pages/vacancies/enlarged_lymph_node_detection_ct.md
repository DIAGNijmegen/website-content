title: Deep learning for fully automated detection of enlarged lymph nodes in thoracic CT
groups: diag
closed: false
type: student
picture: vacancies/lymph-node-staging1.png
template: vacancy-single
people: Colin Jacobs, Roel Verhoeven, Erik van der Heijden
description: Development of deep learning algorithms for detection of enlarged lymph nodes in CT.
bibkeys: 

(Image courtesy of Radiology Assistant - radiologyassistant.nl )

## Clinical problem
Lung cancer is still the deadliest cancer in the Netherlands. The advanced stage at diagnosis is to blame for the high mortality of the disease. We are therefore awaiting the initiation of the lung cancer screening in The Netherlands, which will result in a significant stage shift from advanced to early stage lung cancer upon diagnosis. Accurate lymph node staging is essential for adequate treatment planning and patient outcome. Undertreatment should be prevented at all cost. Current international guidelines require CT and FDG-PET imaging prior to treatment. And when suspicion of nodal involvement is present, endobronchial ultrasound guided fine needle aspirations (EBUS-TBNA) should be performed to obtain cytological proof of presence or absence of malignant disease. But even when these procedures are followed, reports from the national lung surgery database (DICA) show a ~20% upstaging after surgery compared to the pre-operative clinical staging.

Lymph nodal staging in lung cancer is under influence of different imaging modalities and (subjective) expertise of multiple physicians. Each of these modalities have their limitations and detection limits. And while all imaging is performed in (internationally) protocolized fashion, no standard way of interpreting results is available. We suggest to utilize AI in our need of unifying report outcome and enabling a more reproducible and accurate risk stratification of mediastinal lymph node involvement. We propose a multimodal approach in which all imaging is combined to develop an AI model that reliably provides a malignancy estimation.

## Solution
You will initially have one main task in this project:

* Train and improve deep learning algorithm(s) to automatically detect enlarged lymph nodes on thoracic CT imaging. We will start with enlarged mediastinal lymph nodes on CT. If things progress quickly, we will explore other areas, such as axillary lymph nodes.

Several baseline algorithms are available at DIAG for detection and classification of pulmonary nodules, see e.g. our system based on ResNet50 and I3D for nodule malignancy estimation described [here](https://pubs.rsna.org/doi/full/10.1148/radiol.2021204433).

## Data
DIAG has a scientific archive of over 100,000 chest CT examinations. For this project, we have a large retrospective dataset of lung cancer cases from Radboudumc available from 2007-2018, which is already being collected as part of several ongoing projects (N=~1250 patients). Parts of this datasets have already been annotated.
	
## Results
The algorithm(s) that come out of this project will be made publicly available for research use as Docker containers through the [grand-challenge.org](https://grand-challenge.org/algorithms/) platform. You are encouraged to write a scientific publication describing your results.

## Embedding
You will be embedded in the Diagnostic Image Analysis Group and will be supervised by a research member whose research is dedicated to [AI for lung cancer](https://www.diagnijmegen.nl/research/lung-cancer-image-analysis/). We have a strong collaboration with both clinical and radiological experts. You will also have access to a Deep Learning GPU Cluster ([SOL](https://www.diagnijmegen.nl/software/sol/)) to run deep learning experiments.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics, Biomedical Engineering or similar in the final stages of their Master education. 
- You should be proficient in Python programming and have a theoretical understanding of deep learning architectures.
- Experience with medical images is beneficial.

## Information 
- Project duration: 6 or 9 months 
- Location: Radboud University Medical Center 
- For more information or to apply for this project, please contact [Colin Jacobs](https://www.diagnijmegen.nl/people/colin-jacobs/)
