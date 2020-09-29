title: Automated scoring in psoriasis based on RGB images
groups: ai-for-health
finished: false
type: student
picture: vacancies/psoriasis_AI.jpg
template: project-single
people: Nolan Cardozo, Mirjam Schaap, Marieke Seyger, Ajay Patel, Bram van Ginneken
description: Development of automatic classification algorithm for psoriasis in photographs of the body.

**Start date: 07-09-2020** <br>
**End date: 07-03-2021**

## Clinical problem

Psoriasis is a common chronic inflammatory skin disease, with a prevalence of 2-3% of the Western population. The skin disease is characterized by raised, red, scaling lesions, which can be present all over the body. These lesions are often a burden to patients since they can be  visible, itchy or painful. Due to its chronic nature, psoriasis causes a remarkable decrease in the quality of life of patients. In daily clinical practice and clinical research, psoriasis severity is often measured by the Psoriasis Area Severity Index ([PASI](https://en.wikipedia.org/wiki/Psoriasis_Area_and_Severity_Index)) score. This is a subjective score that determines the severity of the psoriasis in four anatomical regions, which consist of the head, trunk, arms and legs. For each anatomical region, four separate  subscores are determined: a) redness of the lesions, b) amount of scaling (called desquamation), and c) the thickness are assessed on a 5 point scale (0-4). Additionally, the affected body surface area is assessed on a 7 point scale (0-6). These scores are combined in an equation to result in the PASI score (0-72). The PASI score is used to determine treatment efficacy and is also used for treatment decisions. In addition, it is used in international randomized controlled pharmaceutical trials as one of the main efficacy outcome measures. Unfortunately, the PASI score is a subjective and time-consuming severity score. Development of an automated (time saving of 3-5 minutes on a total patient contact of 10-15 minutes) and objective PASI scoring device is therefore of utmost importance for patients, physicians and pharmaceutical industries. 

## Solution

It would highly benefit patients, physicians and the pharmaceutical industry if the PASI score would be objectively and automatically performed. Therefore, the University of Twente ([RAM](https://www.ram.eemcs.utwente.nl/)/[BMPI group](https://www.utwente.nl/en/tnw/bmpi/bmpimembers/)) and the Radboudumc (Department of Dermatology), aim to develop a deep learning algorithm which is able to objectively determine the clinical scores in psoriasis patients. Apart from the benefit of collecting an objective score, implementing automated severity scoring in daily clinical practice and research would be time saving.

## Tasks

At our outpatient clinic, patients are frequently photographed by the medical photographer. In each patient, the complete skin is photographed in separate regions in a set of approximately 8 pictures. We built an anonymous dataset of the photographs of the arms, legs and trunk with corresponding PASI sub scores (redness, thickness, scaling, area). For each anatomical region, roughly 600 examples are present in the database (full sets of arms, legs and trunk). The PASI (sub score) labels in the dataset are not equally distributed, with low scores being more common. This is a reflectance of daily clinical practice. During this internship you will develop multiple deep learning algorithms to automatically perform these PASI sub scores. Also, you will be involved in identifying improvements in the image acquisition for deep learning purposes at our department. The ultimate goal of this internship is to perform one, or multiple, reader studies for PASI sub scores of anatomical regions. During this reader study we will compare the performance of dermatologists to the deep learning algorithm. The results will be written down in a manuscript in accordance with publication guidelines. We highly appreciate your input in how to solve the clinical problem described. If desired, we also will give you the opportunity to gain more insight into the clinical problem by introducing you to performing PASI scores in daily clinical practice.  

## Innovation
The developed algorithms(s) will be compared to the performance of dermatologists on PASI assessment based on RGB images by performing a reader study. This work will be used in the development of a device that can automatically perform the PASI score in daily clinical practice and research.
