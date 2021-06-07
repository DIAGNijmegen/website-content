title: Diagnosis Prediction in General Practice: The Importance of Temporality in EPRs
groups: ai-for-health
finished: false
type: student
picture: vacancies/gp_diagnoses.png
template: project-single
people: Richard Li, Noud Emonts, Kees van Boven, Michael Ricking, Henk Schers, Hans Peters, Tim Olde Hartman, Hilde Luijks, Annemarie Uijen, Tom Heskes
description: Development of a model to determine probable diagnoses for common reasons to visit a General Practitioner.

**Start date: 22-03-2021** <br>
**End date: 22-09-2021**

## Clinical Problem 
General practitioners (GPs) work with probabilities of diagnoses to head their diagnostic and therapeutic decisions. To a large extent, this is an implicit process, controlled by prior knowledge and so-called pattern recognition. Less is known about the concreteness and preciseness of the used probabilities. Uncertainty may lead to an overestimation of the probability of a rare disease, and thus lead to overuse of diagnostic facilities, unnecessary costs, and ultimately patient harm. Underestimating probabilities may lead to late diagnoses and detrimental consequences. The process of coming to a diagnosis starts when the patient tells his first complaint. This first utterance of a complaint during the consultation is called reason for encounter (RFE; for example cough, back pain, headache). The RFE itself is related to probabilities of diagnoses. 

For common reasons to visit a doctor, context variables influence probabilities of diagnoses. Deepening of our understanding of how diversity, context, multimorbidity and symptoms influence probabilities of final diagnoses will help doctors to work more secure and evidence based. It will lead to the development of a diagnostic support tool to use in everyday practice. 

## Solution
We aim to analyze how GPs can be supported in early diagnosis through AI support. For all patients with new episodes (2010-2020) we want to define the predictive value of the RFE for diagnoses. More specifically we want to study which data influence predictive values. This knowledge is crucial to build ICT tools to support the GP.

We will use machine learning to calculate probabilities of diagnoses based on the reason for encounter, modified for other personal and context variables, based on the data in our database. For 15 common reasons to visit the GP, we want to develop an algorithm that is able to show a physician realtime for any unique patient the probabilities of diagnoses.

## Data
We will use data from the research network FaMeNet (www.famenet.nl) covering over 300.000 patient years, and over 1 million patient contacts. Structured data on contextual factors are available for more than 50% of the adult population. Contextual factors include chronic comorbidity, sex, age, ethnicity, educational level, and all symptoms and diagnoses in the two years preceding the diagnosis.

The data are stored in a data warehouse at the department of Primary and Community care of the Radboud University Nijmegen Medical Center (Radboud Technology Center Health Data). 

We will only consider patients that have had at least one episode starting with one of the top 15 RFEs. Our dataset consists of data points that describe the first contact in an episode (with a top 15 RFE). Each data point has the following information: RFE, age, sex, start date, and diagnosis. Importantly, we will augment each data point in the dataset with information from the patient's medical history up to the start date of the current episode to predict. In this way, we take into account the contextual factors, and in a sense can provide personalized care. Note that patients can appear multiple times in our dataset with different episodes, and because episodes usually start on different dates, the patient history can vary for the same patient although the histories of course partially overlap.

## Approach
The patient history will be a sequence of episodes, where each episode consists of a set of associated ICPC codes. We will learn a latent representation of the patient history through sequence learning with a recurrent neural network (RNN). An RNN is well-suited for sequence learning, and has already been extensively used on similar tasks with Electronic Health Records (EHRs). The model will have an encoder-decoder architecture, where the encoder will be an RNN and the decoder a multilayer perceptron (MLP). The patient history goes into the encoder and the encoder will output a latent patient representation. The latent patient representation together with the RFE, age, and sex will then go into the decoder, which will output the probabilities of diagnoses.

![Model architecture]({{ IMGURL }}/images/projects/gp_diagnoses_rl_model.png)

Additionally, we will investigate the importance of modelling time in the input and/or model. Of particular interest is irregular time, RNNs expect constant time or equally-spaced gaps between points in a sequence, however this does not hold in our patient history. Episodes happen irregularly in time, where some episodes happen only shortly after one another or otherwise can have long periods between them. We will experiment with four conditions based on varying levels of time assumptions:

1. **None**: patient history is represented without retaining the order of episodes and the time between them.
2. **Weak**: patient history is represented as an ordered sequence of episodes, but the time between them is unspecified.
3. **Moderate**: patient history is represented as an ordered sequence of episodes, and each episode is provided with a time interval feature, which indicates the time since the previous episode.
4. **Strong**: patient history is represented as an ordered sequence of episodes, and each episode is provided with a time interval feature, which indicates the time since the previous episode, and the encoder specifically handles irregular time in the sequence.





