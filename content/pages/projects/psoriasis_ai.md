title: Automated clinical scoring in psoriasis
groups: ai-for-health
finished: false
type: student
picture: vacancies/psoriasis_AI.jpg
template: project-single
people: Nolan Cardozo, Mirjam Schaap, Marieke Seyger, Ajay Patel, Bram van Ginneken, Elena Marchiori
description: Development of automatic classification algorithm for psoriasis in photographs of the body.

**Start date: 07-09-2020** <br>
**End date: 27-05-2021**

## Clinical problem

Psoriasis is a common chronic inflammatory skin disease, with a prevalence of 2-3% of the Western population. The skin disease is characterized by raised, red, scaling lesions, which can be present all over the body. These lesions are often a burden to patients since they can be  visible, itchy or painful. Due to its chronic nature, psoriasis causes a remarkable decrease in the quality of life of patients. In daily clinical practice and clinical research, psoriasis severity is often measured by the Psoriasis Area Severity Index ([PASI](https://en.wikipedia.org/wiki/Psoriasis_Area_and_Severity_Index)) score. This is a subjective score that determines the severity of the psoriasis in four anatomical regions, which consist of the head, trunk, arms and legs. For each anatomical region, four separate  subscores are determined: a) redness of the lesions, b) amount of scaling (called desquamation), and c) the thickness are assessed on a 5 point scale (0-4). Additionally, the affected body surface area is assessed on a 7 point scale (0-6). These scores are combined in an equation to result in the PASI score (0-72). The PASI score is used to determine treatment efficacy and is also used for treatment decisions. In addition, it is used in international randomized controlled pharmaceutical trials as one of the main efficacy outcome measures. Unfortunately, the PASI score is a subjective and time-consuming severity score. Development of an automated and objective PASI scoring device is therefore of utmost importance for patients, physicians and pharmaceutical industries. 

## Solution

It would highly benefit patients, physicians and the pharmaceutical industry if the PASI score would be objectively and automatically performed. Therefore, the University of Twente ([RAM](https://www.ram.eemcs.utwente.nl/)/[BMPI group](https://www.utwente.nl/en/tnw/bmpi/bmpimembers/)) and the Radboudumc (Department of Dermatology), aim to develop a deep learning algorithm which is able to objectively determine the clinical scores in psoriasis patients. Apart from the benefit of collecting an objective score, implementing automated severity scoring in daily clinical practice and research would be time saving.

## Dataset

At the outpatient clinic of the Department of Dermatology, Radboudumc, the PASI scores of patients are assessed by PASI-trained treating physicians follwed by photgraphs taken by a medical photographer, resulting in a total of 10 images for the trunk, arms and legs regions. In this study, 5844 anonymized images and PASI subscores of patients that visited the outpatient clinic between October 2011 and September 2020 were retrieved from the database. The head region was excluded to maintain anonymity. Since PASI scores were collected as part of daily practice, subscore distributions for erythema, desquamation, induration and area were imbalanced with low scores being more common than high scores. The subscore ‘4’ for erythema, desquamation and induration, and ‘6’ for area were excluded since there were not enough images available to accurately train CNNs. This resulted in a final dataset of 576 collective images of the trunk region, 614 images of the arms region and 541 images of the legs region.    

## Methods
Two proprietary image enhancement algorithms were developed to automatically improve the quality of the images. Seperate CNNs were trained for three anatomical regions: trunk, arms and legs region, and four subscores: erythema, desquamation, induration and area, resulting in a deep learning system consisting of 12 CNNs. Additonally, six different variants of CNNs were explored for PASI severity scoring. The first variant was trained using the commonly used categorical cross-entropy loss function( 1. CNN<sub>XE</sub>). However, the categorical cross-entropy loss, does not account for the ordinal relationship between the subscores. Therefore, three alternative loss functions that model the ordinal relationship between subscores were explored: Mean squared error (2. CNN<sub>MSE</sub>), Huber loss (3. CNN<sub>Huber</sub>) and Squared earth movers distance (4. CNN<sub>EMD</sub>). In addition, two CNN variants in which the final convolutional layer was split into binary tasks : Ordinal regression based CNN (5. CNN<sub>OR</sub>) and Consistent rank logits (6. CNN<sub>CORAL</sub>) were developed to account for the ordinal relationship in the subscores. The ResNet18 network pre-trained with the ImageNet weights was used for all the six CNN variants. In addition, a reader study was conducted wherein the images of the test set of the trunk region were assessed by five PASI-trained clinicians. The accuracy, mean absolute error (MAE) and intraclass correlation coefficient (ICC) with 95% confidence intervals were used to the evaluate the performance of both the deep learning system and the PASI trained physicians.


## Results
The CNN<sub>CORAL</sub> was the best performing CNN variant on all subscores: erythema, desquamation, induration and area, and for all anatomical regions: trunk, arms and legs regions. The subscores predicted by the CNN<sub>CORAL</sub> were in moderate agreement with real-life assessments made by treating physicians for erythema, desquamation and induration subscores, while the agreement between the real-life assessments and the predictions by the CNN<sub>CORAL</sub> for the area subscore was good. Additionally, majority of the misclassifications made by the CNN<sub>CORAL</sub> , were in the adjacent score classes, indicating that the predictions were robust.

The PASI-trained physicians performing image-based PASI scoring were in good agreement with eachother, but the agreement with the treating physicians performing PASI scoring in real-life was moderate. This indicates that physicians find it diffcult to perform PASI scoring from images, compared to in real-life. The CNN<sub>CORAL</sub> performed similarly to PASI-trained clinicians performing image-based PASI scoring for the erythema, desquamation and induration subscores, but outperformed the physicians on the area subscore.

Detailed results are currently withheld since the study is being published.

## Conclusion
Deep learning based CNNs have the potential to automatically and objectively perform image-based PASI scoring. The CNN<sub>CORAL</sub> outperformed PASI-trained physicians on image-based PASI scoring for the area subscore, while having similar performance on the erythema, desquamation and induration subscores. Automated PASI scoring could potentially enable objective and efficient PASI scoring in clinical practice and clinical research.

An interactive demo is accessible via Grand-Challenge:
<a href="https://grand-challenge.org/algorithms/psoriaisis-severity-grading-from-skin-images/"><img src="https://grand-challenge-public.s3.amazonaws.com/logos/algorithm/b13631d6-579e-419f-bf1a-f7e5cc2a0918/Logo.x20.jpeg" alt="GC" style="width:150px;height:150px;"></a>

[Image-based PASI scoring using deep learning](https://grand-challenge.org/algorithms/psoriaisis-severity-grading-from-skin-images/)

The code for this project can be found in this [GitHub repository](https://github.com/nolancardozo13/pasi_scoring_using_deep_learning)
