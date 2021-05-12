title: Development and validation of a deep-learning system for wisdom tooth removal
finished: false 
type: general 
picture: vacancies/wisdomteeth.jpg 
people: Shankeeth Vinayahalingam, Thomas Maal, Tong Xi, Guido de Jong, Hossein Ghaeminia, Bram van Ginneken, Stefaan Bergé
description: The aim of this project is to develop a deep-learning system that can predict, on the basis of clinical information, panoramic radiographs, and possibly cone-beam CT, if wisdom tooth removal is recommended.
template: project-single 
groups: diag, ai-for-health

## Project Description

Unnecessary removal of wisdom teeth is an enormous health and economic problem worldwide. For example, costs associated with wisdom teeth removal exceed $3 billion in the USA every year. Moreover, wisdom teeth surgery causes approximately 11 million patient days of "standard discomfort or disability" in the States. Surprisingly, research studies have shown that more than half of these extractions are unnecessary. Nowadays, the decision flowchart for wisdom tooth removal is based on the experience of the surgeon as well as on considerations of a wide range of risk versus benefit factors, including the anatomy-, general health-, age-, dental status, drug history, other specific patient-, surgeon- and financial related factors. Taking the numerous interactions between all those factors into account, it is very challenging to make the correct decision during an average
presurgical consultation.

The goal of this project is to create an AI-driven decision flowchart (AIFC). In a first step, the AIFC will generate a categorial output based upon a 2D panoramic radiograph (OPG) and clinical signs, resulting in
1) advice to remove a wisdom tooth; 2) advice to not remove a wisdom tooth; or 3) recommend additional 3D imaging with a cone-beam CT (CBCT) scan. If the CBCT scan is available, the system will recommend whether or not to remove a wisdom tooth.

The system will be developed, validated, prospectively tested and implemented in close collaboration with AI experts of Radboud AI for Health and clinical experts at Radboudumc.

## Results

### Automated detection of third molars and mandibular nerve by deep learning

The approximity of the inferior alveolar nerve (IAN) to the roots of lower third molars (M3) is a risk factor for the occurrence of nerve damage and subsequent sensory disturbances of the lower lip and chin following the removal of third molars. To assess this risk, the identification of M3 and IAN on dental panoramic radiographs (OPG) is mandatory. In this study, we developed and validated an automated approach, based on deep-learning, to detect and segment the M3 and IAN on OPGs. As a reference, M3s and IAN were segmented manually on 81 OPGs. 

A deep-learning approach based on U-net was applied on the reference data to train the convolutional neural network (CNN) in the detection and segmentation of the M3 and IAN. Subsequently, the trained U-net was applied onto the original OPGs to detect and segment both structures. Dice-coefficients were calculated to quantify the degree of similarity between the manually and automatically segmented M3s and IAN. The mean dice-coefficients for M3s and IAN were 0.947 ± 0.033 and 0.847 ± 0.099, respectively. Deep-learning is an encouraging approach to segment anatomical structures and later on in clinical decision making, though further enhancement of the algorithm is advised to improve the accuracy.

Publication:
https://doi.org/10.1038/s41598-019-45487-3

## Funding
* [Radboud AI for Health](https://www.ai-for-health.nl/)
