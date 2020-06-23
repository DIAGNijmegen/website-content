title: A machine learning model to identify neurogenic and infectious fever in ICU patients with acute brain injury
groups: ai-for-health
finished: false
type: student
picture: projects/intensive_care.jpg
template: project-single
people:  Lisette Boeijenk, Ruud van Kaam, Astrid Hoedemaekers, Tim Frenzel, Luca Ambrogioni
description: Development of a model that can identify whether a febrile ICU patient with acute brain injury has a neurogenic fever or an infectious fever.

## Clinical problem
Fever is a common symptom in critically ill neurologic patients, presenting in up to 70% of patients at some point during their stay in the ICU. Though fever is common among patients in the ICU, multiple studies show that fever impacts the population of patients with acute brain injury (ABI) differently and is associated with increased mortality, increased ICU and hospital length-of-stay (LOS) and worse outcome. Given this costly impact of fever on ABI patients it is important to promptly and accurately identify the underlying cause of the fever and start adequate treatment. Only half of the fevers among neurologic ICU patients are caused by an infection, other etiologies for fever among neurologic ICU patients are drug reactions, post-surgical, venous thromboembolism, paroxysmal sympathetic hyperactivity and neurogenic. The latter, neurogenic fever (NF), also known as central fever and centrally mediated fever, can be caused by a complex disturbance of the thermoregulatory center and is thought to be induced by injury to the hypothalamus. Another common cause of NF is the body’s inflammatory response to the cleanup of damaged tissue (e.g. damage due to trauma to the brain or other parts of the body, such as a hematoma), leading to fever. 

Differentiating NF from infectious fever is a critical diagnostic decision that clinicians face with ABI patients, for the treatments differ significantly. If the cause of the fever is an infection, then body fluids (blood, urine, sputum, etc) should be cultured and antibiotics should be given rapidly. If the fever is neurogenic, taking cultures are needless, expensive and labour intensive and applying antibiotics when there is no infection increases the risk of resistance and eventually renders certain antibiotics powerless. The dilemma for clinical experts is consequently to choose a treatment as quick as possible that is the most effective. Yet, currently there is no specific marker for NF, so NF can only be diagnosed by exclusion of infectious processes and ruling out other etiologies, requiring expensive and invasive tests that burden the patient and take time to process, thus antibiotics are often prescribed preventively.

Any additional information, such as a classification model, to aid the clinician in promptly identifying the cause of the fever (neurogenic or infectious) would therefore be a valuable aid in clinical decision making.

## Solution
The aim of this project is to build a model that can identify whether a febrile ICU patient with ABI has a neurogenic fever or an infectious fever, allowing the experts to make faster and better informed decisions based on more data than they can take into account themselves. 

To develop a model, we first need data to train the model on. For this project we have access to historical patient data from the Electronic Medical Record (EMR), which includes personal data, decursus (i.e. textual notes from medical professionals about the patient), laboratory results and medical imaging data, along with an SQL database containing all vital parameters of the patients (e.g. blood pressure, temperature, saturation) sampled 5 times a minute for their entire length of ICU stay. In consultation with clinical experts we will collect the relevant data and patients from these records to create a dataset for this project. We will use this dataset to develop a model which can identify the type of fever: neurogenic or infectious. Though outside the scope of this project, the goal of this model is to be implemented in the ICU of the RadboudUMC to support clinicians in deciding the most adequate treatment for ABI patients who are presenting fever.

## Tasks
 - Decide on which variables in the EMR to include.
 - Decide on which patients to include.
 - Collect the dataset from the available databases.
 - Pre-process the data.
 - Develop and iterate on a model for neurogenic and infectious fever identification.

## Innovation
This project will be part of a broader research focusing on implementation of AI at the ICU at RadboudUMC to improve patient care and assist clinical decision making. This project will consequently not only advance the ICU with a predictive model, but as one of the first AI projects at the ICU department of RadboudUMC this project will also lay the foundation of AI applied to the ICU on which future projects can build and learn from. The task of discriminating neurogenic fever from infectious fever is very complex even for a clinical expert. Building a model for this discrimination will prove quite the challenge and the findings in this project can therefore be an inspiration for identification modelling tasks of similar complexity, specifically in the field of applying AI for health.
Additionally, no study (that we could find) yet exists where a machine learning model is applied to identify the etiology of a fever, neither in general on the ICU nor related to infections, indicating a clear research gap.
