title: Automated Detection of Developmental Hip Dysplasia
groups: ai-for-health, diag
finished: false
type: student
picture: projects/developmental-hip-dysplasia.png
template: project-single
people: Hermen van Westen, Thomas van den Heuvel, Chris de Korte, Bram van Ginneken
description: Develop a deep learning algorithms for automated detection developmental hip dysplasia. The algorithms should run on a phone with a  low-cost portable ultrasound probe attached.

**Start date: 13-02-2023** <br>
**End date: 12-08-2023**

## Clinical problem
Developmental Hip Dysplasia (DDH) is the most common congenital defect in newborns which is a leading cause of early arthritis leading to total hip replacement. 3% of all newborns, until the age of 6 months, will develop DDH. Unfortunately, youth health clinicians are not able to use ultrasound, since it requires months of training. Instead, they perform an inaccurate physical examination and a questionnaire to decide which newborn needs to be referred for an ultrasound. As a consequence, 22.000 newborns are unnecessarily referred to the hospital every year in the Netherlands alone. 

Ultrasound devices have recently become cheaper and portable. These portable devices can be connected to laptops, tablets and even smartphones, making them accessible for a wide range of users, including physicians in the first line. 

## Solution 
In this project we will develop a deep learning algorithm for automated detection of the alfa and beta angle according to the method of Graf using ultrasound images. The deep learning algorithms will be deployed in a smartphone application and evaluated at child health centers.

## Data 
There is a dataset available of 1400 newborns which had an ultrasound examination of their hips at the Radboudumc between 2016 and 2021. During each examination, the right and left hip are imaged, so the dataset contains 2800 2D ultrasound images. The ground truth of each image is the alfa and beta angle measured according to Graf’s method.

## Results
When the algorithms have sufficient sensitivity and specificity, and are able to run on a smartphone, they will be integrated in the current prototype and evaluated in practice.

## Embedding 
The student will be supervised by a research scientist from the Department of Medical Imaging, with expertise in deep learning and point-of-care ultrasound and by a pediatric radiologist with expertise in developmental hip dysplasia. For model development, we provide access to a large GPU computation cluster and an existing database of ultasound scans and reference annotations.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics, Biomedical Engineering or similar in the final stages of their Master education. 
- You should be proficient in Python programming and have a theoretical understanding of deep learning architectures.
- Experience with medical images is beneficial.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- For more information or to apply for this project, please contact [member/thomas-van-den-heuvel].
