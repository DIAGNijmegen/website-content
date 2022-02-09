title: Machine Learning in Acute Care: Liver
groups: ai-for-health, diag 
finishe: false
type: student 
picture: vacancies/trauma-ai-liver.jpg
template: project-single
people: Laura Álvarez, Vincent Stirler, Erik Hermans, Monique Brink, Stan Buckens, Matthieu Rutten, Bram van Ginneken, Ajay Patel, Silvan Quax, Amin Mohseni, Ashley Remi, Rozemarie van den Bergh
description: Will deep learning-based algorithms become the new members of the trauma team?  

**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).**

## Clinical Problem 

Initial trauma assessment of severely injured patients is a fast-paced and challenging activity that is unlike most other clinical activities. A multidisciplinary team of varying composition is responsible for primary survey and resuscitation.[1] It performs multiple evaluations and procedures simultaneously and will focus on teamwork and effective communication day and night. The timely diagnosis of injuries is mandatory to initiate appropriate treatments and to prevent further harm at a later point in time.

Many critical decisions are made in during the initial trauma assessment. Fitzgerald et al reported that a critical decision linked to a lifesaving intervention was made every 72 seconds in the first 30 minutes of the primary survey.[2] However, diagnostic errors are more likely to occur in the emergency department than anywhere else.[3] It is reported that "3.2 errors were made per patient in the first 30 minutes of the primary survey and resuscitation."[2] Besides cognitive bias of the team members, typical circumstances are relevant that mitigate diagnostic performance.[4,5] Relevant clinical information is incomplete or absent at presentation. Mental and physical performance impacted by fatigue from working during duty hours. Excessive workloads shorten the time spent on examinations and may lead to hasty assessments. Distractions, such as telephone calls, are repeatedly present and require one to toggle with medical tasks. It is easy to imagine that the initial trauma assessment is prone to error.

In this project we focus on traumatic injuries to the liver. 

1. Advanced Trauma Life Support (ATLS): The Ninth Edition. J Trauma Acute Care Surg. 2013;74(5)
2. Fitzgerald et al. Trauma resuscitation errors and computer-assisted decision support. Arch Surg. 2011;146(2):218-225.
3. Sevdalis et al. Diagnostic error in a national incident reporting system in the UK. J Eval Clin Pract. 2010;16(6):1276-1281
4. Leape. Error in Medicine. JAMA J Am Med Assoc. 1994;272(23):1851
5. Waite et al. Interpretive error in radiology. Am J Roentgenol. 2017;208(4):739-749

## Solution 

A deep learning-based model should be developed for the automatic segmentation of anatomy and pathology on abdominal CT images. Furthermore, the model should be able to classify the type of injury and its features, and predict the probability of rebleeding within the first couple of days following trauma.

## Data 

A database has been compiled with data from 677 patients (177 positive cases and 500 negative cases) who underwent an abdominal CT-scan during the initial trauma assessment. The database requires curation. The images require annotation.

## Embedding 

The student will work in a team together with a medical master student and radiology technician in training. The team will be supervised by a member of the [Diagnostic Image Analysis Group](https://www.diagnijmegen.nl/) with experience in image processing using deep learning approaches as well as team members form the AI in Traumasurgery team. We provide access to a [large GPU computation cluster](https://rtc.diagnijmegen.nl/software/sol/).  

The final deliverable is a code repository on GitHub, a publicly available algorithm on the platform [Grand Challenge](https://grand-challenge.org), a report and validation study and preferably a scientific publication. 


## Requirements 

- Students with a major in data science, computer science, or artificial intelligence in the final stage of master level studies are invited to apply. 

- Interest in natural language processing and machine learning. Affinity with image processing is also welcome. 

- Affinity with programming in Python and with deep learning packages is required. 


## Information 

- Project duration: 6 months 

- Location: Radboud University Medical Center 

- For more information, please contact [Vincent Stirler](mailto:vincent.stirler@radboudumc.nl) 
