title: 2D Plane Detection in 3D prenatal ultrasound
groups: ai-for-health, diag
closed: false
type: student
picture: vacancies/aifh_msc_prenatalultrasound2.png
template: vacancy-single
people: Keelin Murphy, Bram van Ginneken
description: Detection and analysis of 2D planes of interest in 3D ultrasound images

** Start date: 01-03-2023 ** <br>
** End date: 31-08-2023 **

**This is an AI for Health MSc project. Students are eligible to receive a monthly reimbursement of €500,- for a period of six months. For more information please read the [requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical problem
Prenatal ultrasound images are acquired by an expert sonographer who moves and tilts the ultrasound probe, correcting its positioning until a specific 2D plane of interest is found, stored and analysed by the sonographer. Many such 2D planes need to be visualised to perform all necessary measurements and checks.  A full ultrasound examination therefore takes an average of approximately 20 minutes.  Increasing numbers of ultrasound images are being acquired, particularly in the Netherlands since the introduction of the [IMITAS](https://13wekenecho.org/ik-ben-zorgverlener/over-de-imitas-studie/) study whereby all pregnant women now receive an extra scan at 13 weeks gestation.  There is, hence, increasing pressure on the limited number of sonographers and a need to increase the efficiency of the ultrasound imaging process.

## Solution
Modern ultrasound equipment is capable of acquiring 3D volumetric images in an instant and at 13 weeks gestation such an image can include the entire fetus.  However, these images are not used in current clinical practice and navigating through them to identify and analyse the 2D planes of interest is difficult and time-consuming for the human reader.  In this project we will develop an AI system to identify and analyse 2 important planes of interest in 3D ultrasound volumes - a transverse plane of the fetal head where head circumference can be measured and a transverse plane of the fetal abdomen where abdominal circumference can be measured.  Both these measurements are used as biomarkers for healthy growth of the fetus. 

## Data
All data is acquired from patients at 13-14 weeks gestation of pregnancy. For pre-training we will use images from 757 patients acquired by sonographers during conventional 2D imaging examinations. For each patient the relevant planes to acquire head and abdomen circumferences are present but also many other planes (an average of ~57 planes per patient).  A network trained and validated on this 2D dataset will then be applied to 3D ultrasound images (from ~150 patients) where we will identify the best planes for measurement of head and abdominal circumferences.

## Results
The result will be an AI system that can identify the correct planes for measurement of head circumference and abdominal circumference in a 3D volumetric ultrasound image of a fetus at 13-14 weeks gestation. 

## Requirements
- Students with a major in computer science, biomedical engineering, artificial intelligence, physics, or a related area in the final stage of master level studies are invited to apply
- Experience with programming in Python and its deep learning frameworks 
- Theoretical understanding of deep learning architectures

## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- For more information, please contact [Keelin Murphy](mailto:keelin.murphy@radboudumc.nl)



