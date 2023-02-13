title: Predicting successful statin medication treatment 
groups: ai-for-health
closed: false
type: student
picture: vacancies/prosthesis.jpg
template: vacancy-single
people: Jeroen Vermazeren, Henk Schers, Floris van der Laar, Michael Ricking, Eline Allard
description: Development of a prediction tool for successful statin medication treatment 

## Reimbursement
This is an AI for Health MSc project. Students are eligible to receive a monthly reimbursement of €500,- for a period of six months. For more information please read the [requirements](https://www.ai-for-health.nl/requirements).

## Clinical Problem
In 2020, the second most common cause of death within the Dutch population are cardiovascular
diseases. Reducing the cholesterol level is one of the drug treatments for reducing the risk for
cardiovascular disease. According to the Dutch General Practitioner Society (DGPS) there are several
drugs (statins) available depending on the desired cholesterol level decrease. The DGPS provides
guidelines for the drug treatment based on age and other risk factors.
 Statins are a commonly used drug within the Dutch population. Between 2014 and 2021, statins are
the second most prescribed drug within the FaMeNet (www.famenet.nl) dataset. It is widely known
that statin users suffer from statin-associated muscle symptoms (SAMS). Symptoms include pain,
cramps, stiffness, heaviness, weakness and/or loss of strength or muscle fatigue. SAMS often occur
within four to six weeks of statin treatment, nevertheless, can also occur after years of treatment.
These symptoms are reversible when medication is stopped. Consequently, patients with muscle
symptoms are more likely to discontinue their drug treatment, which influences their cardiovascular
risk. 

## Solution
The goal of this research is to predict which patients benefit from a certain statin treatment in a
specific doses using artificial intelligence (AI). Successful treatment is defined as the desired cholesterol
level decrease and continued drug usage of more than 6 months. This goal can be divided in three
subgoals, namely:
1. Predicting successful statin treatment per patient using AI.
2. Predicting specific statin treatment per patient using AI.
3. Predicting specific doses of specific statin treatment using AI.
A coarser analysis can be done based on the specific drugs. Specifically, predicting a specific drug for a
specific patient. This could be a single-label or multi-label prediction. Where single label means only
one drug is predicted and multi-label means multiple drugs are predicted.
 Next to predicting which and if a statin should be prescribed to a patient, an AI challenge is
predicting the correct doses for every patient. This could reduce the selection procedure and therefore
decrease risks and medical costs.

 Within our department, previous work has been done in compressing the electronic health record
(EHR) for an AI application56. From this work, the transformer neural network can be tested and
improved for our research goal. Next to statistical methods such as regression, other machine learning
methods including random forests and gradient boosted trees could be used as baseline to a neural
network approach.


## Data
The data is extracted from the complete research network of the primary and community care
department. This includes more than 400.000 patients from General Practices within the data period of
2010 until 2022. Every episode, medication, lab results and every contact will be included for the
selected data period. A selection of variables that can be found are gender, medication, comorbidities,
lab results and number of contacts.
The data are stored in a data warehouse of the department of Primary and Community care of the
Radboud University Nijmegen Medical Centre. The group has extensive and complementary experience
in research using these longitudinally collected data. 

## Approach
The result, a prediction algorithm, of this research can be used as supportive decision tool for general
practitioners in their practice. This algorithm assists GPs with their prescription of statins to reach the
desired cholesterol level and lower the drop-out rate of drug usage of patients, which in turn will
reduce the cardiovascular risks.

## Requirements
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics, Biomedical Engineering or similar in the final stages of their Master education.
- Student should be proficient in Python programming and have a theoretical understanding of deep learning architecture and supervised machine learning.
- Experience with complicated structured dataset is beneficial.

## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- For more information, please contact Jeroen Vermazeren](mailto:jeroen.vermazeren@radboudumc.nl)

