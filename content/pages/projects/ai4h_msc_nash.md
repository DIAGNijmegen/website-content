title: AI-based quantification of non-alcoholic steatohepatitis
groups: ai-for-health, diag
finished: true
type: student
picture: vacancies/msc_nash.jpg
template: project-single
people: Thijs Schoppema, Geert Litjens
description: Develop a method to quantify non-alcoholic steatohepatitis in histopathology images

**Start date: 06-02-2023** <br>
**End date: 05-08-2023**

## Clinical problem
Non-alcoholic fatty liver disease (NAFLD) is an enormous global burden with an estimated prevalence of 20-30% worldwide. NAFLD, defined as excessive hepatic lipid accumulation in absence of alcohol use, can progress into non-alcoholic steatohepatitis (NASH), a disease characterized by hepatic inflammation and fibrosis (‘scarring’). Although only recently acknowledged, NASH can have severe consequences, such as a twofold increased risk of cardiovascular diseases, the development of liver cirrhosis with liver failure, and liver cancer.
To date, the gold standard to diagnose and stage severity of NAFLD-NASH is a liver biopsy. A liver pathologist evaluates the histopathological slide and determines the severity of the disease by assessment of the amount of fat (or: ‘steatosis’), inflammation, hepatocyte ballooning and fibrosis. Unfortunately, there are still major issues in the histopathological assessment of NAFLD-NASH. 
The first major problem is an enormous interobserver variability. The severity that two independent pathologists ascribe to a histopathological slide differs in more than 50% of cases. As one can imagine, this severely influences a patient’s health, treatment and prognosis. In addition, the lack of consistency also seriously influences the research in NAFLD-NASH, where improvements due to novel therapies can be masked by interobserver variability.
Second, a major problem and practical inevitability in the assessment of NASH histopathology by humans, is the categorical nature of severity score systems. When a histopathological slide contains 32% steatosis it is appraised one point, but when it is estimated to be 34%, the biopsy gets appraised two severity points. Therefore, this categorical nature implies a certain inaccurateness in the determination of the severity of the disease, and thereby has major consequences for both patients and the research field. 

## Solution
The goal of this project was to investigate how Artificial Intelligence can be used to support the pathologist in the histopathological assessment of NASH. For this, a segmentation pipeline and end-to-end classification method have been deployed. 

The segmentation pipeline consists of two U-net segmentation models with EfficientNet-B4 backbones. The first segmentation model detects steatosis and inflammation in a H&E stained whole slide image (WSI), on a spacing of 0,5. The second model detects the portal regions in the WSI, on a spacing of 4,0. The portal regions are on a low level similar to inflammation, but are more easily distinguishable with more context. By predicting the portal regions we are able to combine the masks and remove wrongly detected inflammation spots near these regions. Afterwards, the background of the prediction mask will be corrected and a final post-processing containing several morphological operations will be done in order to remove small errors.

The Clustering-constrained Attention Multiple Instance Learning (CLAM) pipeline has been used for the end-to-end classification. A total of 3 models have been made with the CLAM pipeline. The first model predicts the steatosis score of a WSI. However, steatosis 0 has been excluded due to a lack of samples. The second model predicts the absence and presence of ballooning. The final model predicts the presence of NASH based on the interpreted NAFLD activity score (NAS). Meaning that a score of 0 is not diagnostic of NASH, a score of 2 is diagnostic of NASH and a score of 1 is equally divided between not diagnostic, borderline and diagnostic of NASH.

## Data
For this project, a total of 48 WSI in H&E and PSR staining were available with the histopathological scores. Of the 48 WSIs a total of 10 have been manually annotated for steatosis, inflammation, and portal regions. For the segmentation and end-to-end classification models, a train-validation-test split of 6-2-2 has been used.

## Results
### Segmentation
To evaluate the segmentation models the DICE and IOU scores have been used. The table below shows the performance of both models after post-processing. The results for each relevant feature has been shown with the overall score. The metrics have been calculated on 2 different annotated WSIs.

| | Steatosis | Inflammation | Portal Area's | Liver tissue | Overall |
|-----|-----|-----|-----|-----|-----|
| Dice | 0,808 | 0,790 | 0,768 | 0,918 | 0,883 |
| IOU | 0,677 | 0,653 | 0,623 | 0,849 | 0,790 |

### end-to-end classification
To evaluate the end-to-end classification models a 4-fold cross-validation with 10 samples in each fold has been used. The used metrics for evaluation are the F1 score, Precision, Recall, and Accuracy.

| Steatosis | 1 | 2 | 3 | Average |
|-----|-----|-----|-----|-----|
| Precision | 0,750 (0,000) | 0,754 (0,152) | 0,875 (0,217) | 0,793 (0,031) |
| Recall | 0,750 (0,000) | 0,667 (0,102) | 0,917 (0,144) | 0,778 (0,044) |
| F1 | 0,750 (0,000) | 0,688 (0,036) | 0,867 (0,141) | 0,785 (0,036) |
| Accuracy | | | | 0,751 (0,040) | 

| Ballooning | 0 | 1 | Average |
|-----|-----|-----|-----|
| Precision | 0,875 (0,072) | 0,929 (0,124) | 0,902 (0,026) |
| Recall | 0,900 (0,173) | 0,850 (0,087) | 0,875 (0,043) |
| F1 | 0,869 (0,069) | 0,875 (0,024) | 0,888 (0,035) |
| Accuracy | | | 0,875 (0,043) |

| INAS | 0 | 1 | 2 | average |
|-----|-----|-----|-----|-----|
| Precision | 0,608 (0,068) | 0,708 (0,298) | 0,750 (0,144) | 0,689 (0,153) |
| Recall | 0,813 (0,207) | 0,313 (0,108) | 1,000 (0,000) | 0,708 (0,093) |
| F1 | 0,692 (0,123) | 0,421 (0,147) | 0,850 (0,087) | 0,697 (0,124) |
| Accuracy | | | | 0,650 (0,112) |

[//]: # " Students will be supervised by a team of NAFLD-NASH experts from the Amsterdam UMC (dr. Onno Holleboom, and drs. Quinten Augustijn) and a team of experts in the field of deep learning in histopathology from the Radboud University (dr. ir. Geert Litjens and prof. dr. Jeroen van der Laak). Primarily based in Nijmegen, the student will develop a deep learning model for the assessment of NAFLD-NASH. The student will be trained by a liver pathologist in the assessment of NAFLD-NASH. Thereafter the student will build a supervised model upon the histopathological slides of 60-100 patients. When successful, the model will further be validated in larger cohorts. We expect that the thesis will results in a significant scientific publication. "
