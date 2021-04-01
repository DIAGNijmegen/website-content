title: Using big data to improve diagnosis in general practice
groups: ai-for-health
finished: false
type: student
picture: vacancies/gp_diagnoses.png
template: project-single
people: Richard Li, Noud Emonts, Kees van Boven, Michael Ricking, Hans Peters, Tim Olde Hartman, Hilde Luijks, Annemarie Uijen, Henk Schers
description: Development of a model to determine probable diagnoses for common reasons to visit a General Practitioner.

** Start date: 22-03-2021 ** <br>
** End date: 22-09-2021 **

## Clinical Problem 
General practitioners (GPs) work with probabilities of diagnoses to head their diagnostic and therapeutic decisions. To a large extent, this is an implicit process, controlled by prior knowledge and so-called pattern recognition. Less is known about the concreteness and preciseness of the used probabilities. Uncertainty may lead to an overestimation of the probability of a rare disease, and thus lead to overuse of diagnostic facilities, unnecessary costs, and ultimately patient harm. Underestimating probabilities may lead to late diagnoses and detrimental consequences. The process of coming to a diagnosis starts when the patient tells his first complaint. This first utterance of a complaint during the consultation is called reason for encounter (RFE; for example cough, back pain, headache). The RFE itself is related to probabilities of diagnoses. 

For common reasons to visit a doctor, context variables influence probabilities of diagnoses. Deepening of our understanding of how diversity, context, multimorbidity and symptoms influence probabilities of final diagnoses will help doctors to work more secure and evidence based. It will lead to the development of a diagnostic support tool to use in everyday practice. 

## Solution
We aim to analyze how GPs can be supported in early diagnosis through AI support. For all patients with new episodes (2010-2020) we want to define the predictive value of the RFE for diagnoses. More specifically we want to study which data influence predictive values. This knowledge is crucial to build ICT tools to support the GP.

The AI challenge is to use machine learning (eg Bayesian network approach and other methods) to calculate probabilities of diagnoses based on the reason for encounter, modified for other personal and context variables, based on the data in our database. For 10 common reasons to visit the GP, we want to develop an algorithm that is able to show a physician realtime for any unique patient the probabilities of diagnoses.

## Data
We will use data from the research network FaMeNet (www.famenet.nl) covering over 300.000 patient years, and over 1 million patient contacts. Structured data on contextual factors are available for more than 50% of the adult population. Contextual factors include chronic comorbidity, sex, age, ethnicity, educational level, and all symptoms and diagnoses in the two years preceding the diagnosis.

The data are stored in a data warehouse at the department of Primary and Community care of the Radboud University Nijmegen Medical Center (Radboud Technology Center Health Data). 
