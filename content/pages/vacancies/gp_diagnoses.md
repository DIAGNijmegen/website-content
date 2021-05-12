title: Using big data to improve diagnosis in general practice
groups: ai-for-health
closed: true
type: student
picture: vacancies/gp_diagnoses.png
template: vacancy-single
people: Kees van Boven, Michael Ricking, Hans Peters, Tim Olde Hartman, Hilde Luijks, Annemarie Uijen, Henk Schers
description: Development of a model to determine probable diagnoses for common reasons to visit a General Practitioner.

## Clinical Problem 
General practitioners (GPs) work with probabilities of diagnoses to head their diagnostic and therapeutic decisions. To a large extent, this is an implicit process, controlled by prior knowledge and so-called pattern recognition. Less is known about the concreteness and preciseness of the used probabilities. Uncertainty may lead to an overestimation of the probability of a rare disease, and thus lead to overuse of diagnostic facilities, unnecessary costs, and ultimately patient harm. Underestimating probabilities may lead to late diagnoses and detrimental consequences. The process of coming to a diagnosis starts when the patient tells his first complaint. This first utterance of a complaint during the consultation is called reason for encounter (RFE; for example cough, back pain, headache). The RFE itself is related to probabilities of diagnoses. 

For common reasons to visit a doctor, context variables influence probabilities of diagnoses. Deepening of our understanding of how diversity, context, multimorbidity and symptoms influence probabilities of final diagnoses will help doctors to work more secure and evidence based. It will lead to the development of a diagnostic support tool to use in everyday practice. 

## Solution
We aim to analyze how GPs can be supported in early diagnosis through AI support. For all patients with new episodes (2010-2020) we want to define the predictive value of the RFE for diagnoses. More specifically we want to study which data influence predictive values. This knowledge is crucial to build ICT tools to support the GP.

The AI challenge is to use machine learning (eg Bayesian network approach and other methods) to calculate probabilities of diagnoses based on the reason for encounter, modified for other personal and context variables, based on the data in our database. For 10 common reasons to visit the GP, we want to develop an algorithm that is able to show a physician realtime for any unique patient the probabilities of diagnoses.

## Data
We will use data from the research network FaMeNet (www.famenet.nl) covering over 300.000 patient years, and over 1 million patient contacts. Structured data on contextual factors are available for more than 50% of the adult population. Contextual factors include chronic comorbidity, sex, age, ethnicity, educational level, and all symptoms and diagnoses in the two years preceding the diagnosis.

The data are stored in a data warehouse at the department of Primary and Community care of the Radboud University Nijmegen Medical Center (Radboud Technology Center Health Data). 

## Approach
Students will be supervised by a group of GP-researchers and data managers from the Radboud Technology Center Health data. The student will get familiarized with the data structure of the datawarehouse. Depending on discussions with the group, a machine learning method will be used to analyse the data. The goal is to create prediction models for diagnoses in general practice. The deliverable will be used in a consultation tool for GPs in everyday practice.

## Requirements
- Students with a major in data science, computer science, or artificial intelligence in the final stage of master level studies are invited to apply.
- Interest in machine learning and clinical data.

## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- For more information, please contact [Kees van Boven](mailto:Kees.vanBoven@radboudumc.nl)
