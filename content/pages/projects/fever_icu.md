title: Identify fever etiology in ICU patients with acute brain injury
groups: ai-for-health
finished: true
type: student
picture: projects/intensive_care.jpg
template: project-single
people:  Lisette Boeijenk, Ruud van Kaam, Astrid Hoedemaekers, Tim Frenzel, Luca Ambrogioni
description: Development of a model that can identify whether a febrile ICU patient with acute brain injury has an infectious fever or non-infectious fever.

**Start date: 13-01-2020** <br>
**End date: 12-11-2020**

## Clinical problem
Fever is a common symptom in critically ill neurologic patients, presenting in up to 70% of patients at some point during their stay in the ICU. Though fever is common among patients in the ICU, multiple studies show that fever impacts the population of patients with acute brain injury (ABI) differently and is associated with increased mortality, increased ICU and hospital length-of-stay (LOS) and worse outcome. Given this costly impact of fever on ABI patients it is important to promptly and accurately identify the underlying cause of the fever and start adequate treatment. Only half of the fevers among neurologic ICU patients are caused by an infection, other etiologies for fever among neurologic ICU patients are drug reactions, post-surgical, venous thromboembolism, paroxysmal sympathetic hyperactivity and neurogenic. The latter, neurogenic fever (NF), also known as central fever and centrally mediated fever, can be caused by a complex disturbance of the thermoregulatory center and is thought to be induced by injury to the hypothalamus. Another common cause of NF is the body’s inflammatory response to the cleanup of damaged tissue (e.g. damage due to trauma to the brain or other parts of the body, such as a hematoma), leading to fever. 

Differentiating NF from infectious fever is a critical diagnostic decision that clinicians face with ABI patients, for the treatments differ significantly. If the cause of the fever is an infection, then body fluids (blood, urine, sputum, etc) should be cultured and antibiotics should be given rapidly. If the fever is neurogenic, taking cultures are needless, expensive and labour intensive and applying antibiotics when there is no infection increases the risk of resistance and eventually renders certain antibiotics powerless. The dilemma for clinical experts is consequently to choose a treatment as quick as possible that is the most effective. Yet, currently there is no specific marker for NF, so NF can only be diagnosed by exclusion of infectious processes and ruling out other etiologies, requiring expensive and invasive tests that burden the patient and take time to process, thus antibiotics are often prescribed preventively.

Any additional information, such as a classification model, to aid the clinician in promptly identifying the cause of the fever would therefore be a valuable aid in clinical decision making.

## Solution
The aim of this project is to build a model that can identify whether a febrile ICU patient with ABI has an infectious fever or a non-infectious fever such as neurogenic fever, allowing the experts to make faster and better informed decisions based on more data than they can take into account themselves. 

To develop a model, we first need data to train the model on. For this project we have access to historical patient data from the Electronic Medical Record (EMR), which includes personal data, decursus (i.e. textual notes from medical professionals about the patient), laboratory results and medical imaging data, along with an SQL database containing all vital parameters of the patients (e.g. blood pressure, temperature, saturation) sampled 5 times a minute for their entire length of ICU stay. In consultation with clinical experts we will collect the relevant data and patients from these records to create a dataset for this project. We will use this dataset to develop a model which can identify the type of fever: infectious or non-infectious. Though outside the scope of this project, the goal of this model is to be implemented in the ICU of the RadboudUMC to support clinicians in deciding the most adequate treatment for ABI patients who are presenting fever.

## Tasks
 - Decide on which variables in the EMR to include.
 - Decide on which patients to include.
 - Collect the dataset from the available databases.
 - Pre-process the data.
 - Develop and iterate on a model for infectious and non-infectious fever identification.

## Innovation
This project will be part of a broader research focusing on implementation of AI at the ICU at RadboudUMC to improve patient care and assist clinical decision making. This project will consequently not only advance the ICU with a predictive model, but as one of the first AI projects at the ICU department of RadboudUMC this project will also lay the foundation of AI applied to the ICU on which future projects can build and learn from. The task of discriminating infectious fever from non-infectious fever is very complex even for a clinical expert. Building a model for this discrimination will prove quite the challenge and the findings in this project can therefore be an inspiration for identification modelling tasks of similar complexity, specifically in the field of applying AI for health.
Additionally, no study (that we could find) yet exists where a machine learning model is applied to identify the etiology of a fever, neither in general on the ICU nor related to infections, indicating a clear research gap.

---

## Methods

### Dataset
Main inclusion criteria for patients were: 18 years and older, consecutively admitted for at least 48 hours to the ICU of Radboud University Medical Center (Nijmegen, the Netherlands) between Jan 1, 2015 and Dec 31, 2019 having at least one of the selected ABI admission diagnoses. The exclusion criterion was a second infectious admission diagnosis since the focus of this study is fever that develops on the ICU of which the etiology is not known at onset. 

We defined fever episodes as body temperature >38.3&deg;C recorded on at least one measurement for at least two consecutive days. We excluded the first 36 hours of temperature measurement in  post-cardiac arrest patients due to cooling interventions as well as the last 48h of deceased patients due to temperature irregularities.

We dichotomized the fever etiologies in infectious and non-infectious fever as follows: if a patient received >100 hours of consecutive antibiotics during a fever, the fever episode was labelled as infectious, in all other cases the fever episode was labelled as non-infectious. 

Selected data used for model building included (1) patient demographics; (2) admission information; (3) vital parameters; (4) test measurements; (5) fluid data; (6) lab results; and (7) medications administered. Selection of these data was based on medical physiology and pathology, literature, as well as availability of the data from the medical records at the time of building the dataset.

Literature as well as clinicians were consulted in the feature engineering process to turn the selected data into meaningful features. Features extracted from (1) patient demographics and (2) admission information only needed to be extracted once for each fever episode. For the other variables intervals and a range needed to be chosen over which to extract the features. Based on medical physiology and pathology, these features were extracted from a time window starting at 3 days before the fever episode. 
Features from time series data were extracted at intervals of 8 or 24 hours, depending on the variable used. Since group (3) vitals included continuous raw data, features could be extracted over intervals of 8 hours (one shift).

Two different approaches were taken for feature engineering.
#### Numerical approach
For the first approach, continuous numeric features were extracted from the variables, such as sum, minimum (min), maximum (max), median (med) and standard deviation (std). Categorical features were one-hot encoded. One of the issues of working with retrospective EHR data is missing values, either due to machine errors, human mistakes or simply because a patient had not yet been admitted. Due to limited resources and time it was not possible to explore advanced imputation techniques. We decided to impute missing feature values with the mean of that feature. It is important to note that this imputation was fitted (the means are calculated) on the training dataset, and this fit was applied to missing values of both the training and the test datasets.
#### Discrete approach
Since we had many different data streams and limited resources it was not possible for this study to perform preprocessing on all these data streams. Therefore no outlier detection and removal was performed and as mentioned no sophisticated approaches were taken to deal with missing data. The decision was made to also make discrete features to reduce the impact of outliers and to deal with missing data. For this second approach a clinician drafted bins for some of the continuous features. Again due to time constraints not all of the numerical features could be discretized and only one continuous feature was binned for each variable, generally the median feature. Missing feature values were dealt with by adding two extra bins to each feature: one bin for missing data because the patient was not yet admitted and another bin for missing data while the patient was already admitted. To be able to use these categorical features as input for ML models, these bins were ordinal encoded, meaning that the bins of each feature were encoded as integers 0 to nBins-1.

### Models
We chose six ML classifiers from the scikit-learn library: Naive Bayes (NB) (Categorical Naive Bayes for the discrete features, Gaussian Naive Bayes for the numerical features), k-Nearest Neighbor (kNN), Logistic Regression (LR), Support Vector Machine (SVM), Random Forest (RF) and Gradient Boosting (GB). Three different kernels were used for the SVM: the Radial Basis Function (rbf) kernel, Polynomial (poly) kernel and Sigmoid (sigmoid) kernel. These techniques were chosen because they span a wide range of approaches and complexities and have different strengths and weaknesses, allowing for a systematic comparison and exploration.

To compare these classifiers to a simple baseline, we applied a Stratified Dummy classifier from the scikit-learn library which generates predictions based on the class distribution in the training set.
Some hyperparameters of the selected classifiers were tuned using grid search over supplied parameter ranges to optimize on recall. Other default  parameters were changed based on preliminary explorations. 

To study the effect of balancing the classes before training, undersampling, oversampling as well as no sampling were applied.

The performance of the models, feature engineering approaches and sampling techniques was estimated using 10 Fold Cross Validation (CV). The datasets were divided into ten subsets; one subset was retained as test set and the remaining nine were used as training set. The training sets were used to fit mean imputation for the numerical features, apply sampling on, tune the hyperparameters and train the classifiers. The trained models were tested on the test subset. This process was repeated ten times, using each of the subsets as test set once. 
To report the performance the means and standard deviations of the recall (also known as sensitivity), specificity and Area Under the Curve (AUC) were calculated. Additionally, Receiver Operating Characteristic (ROC) curves were plotted for a more qualitative analysis and the coefficients of the LGR model as well as the feature importance of RF and GB were analysed.

## Results

### Dataset
Of 1056 selected patients, 423 (40%) experienced fever episodes with a total of 610 fever episodes, of which 120 (20%) were classified as infectious. 

During the feature engineering stage, different engineering approaches were compared with regard to the medications representation, interval window, and features with a lot of missing values. The different approaches only yielded marginal differences in performance with inconclusive overall preference.
After engineering features from the selected data, the discrete feature representation dataset contained 272 features and the numerical dataset contained 618 features. The numerical dataset suffered more missing values (38%) than the discrete dataset (25% missing). Half of the missing values in the discrete dataset are due to patients not yet being admitted. For example, if a patient develops fever on the second day after admission then no data has been recorded over the third day before the fever, since the patient was not yet on the ICU that day.

Patients with infectious fever episodes had a longer ICU and hospital length of stay compared to patients with non-infectious fever episodes. Patients with infectious fever episodes had a higher mortality than non-infectious fever patients.
Overall, fever episodes occurred four days after ICU admission, however a quarter of the fever episodes developed within 1.2 days of ICU admission. Infectious fever episodes occurred after 6.9 days after ICU admission as opposed to 3.6 days for non-infectious fever episodes. 

### Models

The models were trained and tested on both the discrete and numerical datasets with each of the different sampling methods applied.

Neither the different sampling techniques nor the different datasets had a effect on the AUC performance. 

|Model | AUC | Recall | Specificity | Sampling | Dataset |
|---|---|---|---|---|---|
|Dummy | 0.55 (±0.09) | 0.28 (±0.15) | 0.82 (±0.03) | Normal | - |
|NB | 0.63 (±0.09) | 0.48 (±0.16) | 0.69 (±0.06) | Undersampling | Numerical |
|KNN | 0.58 (±0.06) | 0.57 (±0.17) | 0.54 (±0.06) | Undersampling | Numerical |
|LGR | 0.64 (±0.08) | 0.62 (±0.13) | 0.58 (±0.11) | Normal | Discrete |
|SVMpoly | 0.62 (±0.08) | 0.34 (±0.13) | 0.82 (±0.05) | Oversampling | Discrete |
|SVMrbf | 0.64 (±0.08) | 0.42 (±0.12) | 0.74 (±0.06) | Oversampling | Discrete |
|SVMsigmoid | 0.58 (±0.10) | 0.57 (±0.23) | 0.57 (±0.17) | Normal | Discrete | 
|RF | 0.63 (±0.08) | 0.48 (±0.11) | 0.72 (±0.06) | Oversampling | Numerical |
|GB | 0.60 (±0.09) | 0.59 (±0.14) | 0.60 (±0.05) | Undersampling | Numerical |

*Mean performance (SD) of setup with highest area-under-the-curve (AUC) per model.*

The table above shows a comparison of the models with setups leading to the highest AUC performance. The LGR and SVM with rbf kernel achieved the highest AUC at 0.64, which was an improvement of 0.09 on the Dummy. 
NB, RR and the SVM with polynomial kernel are not far behind with mean AUCs of 0.63, 0.63 and 0.62 respectively. 
All models were able to outperform the Dummy with at least 0.03 on mean AUC and 0.06 on mean recall, however none could outperform it on specificity. 
The sampling methods and datasets on which the models perform best is almost evenly spread.

An inspection of the coefficients for the best performing Logistic Regression showed that the most important feature for both datasets was the length-of-stay (LOS) on the ICU at the start of the fever and is predictive of infectious etiology. Ventilator settings positive end-expiratory pressure (PEEP) and fraction of inspired oxygen (FiO2) are also predictive of infectious fever etiology. Blood transfusions on the third and second day before the fever and Glasgow Coma Scale (GCS) on the second day before the fever are predictive of non-infectious fever etiology.

For more detailed results and a discussion of these results see the [final report](https://drive.google.com/file/d/1Fo8Hd4lkJnLZiU6XSd3zdtMhKW_lvUVA/view?usp=sharing) for this project.

## Conclusion
This study shows that the combination of features and labels in the created dataset do not carry predictive value for the distinction between infectious and non-infectious fever episodes. 

Concessions made in labelling criteria, the small number of samples and the large amount of missing values probably caused this lack of performance.

To be able to draw any conclusions on the applicability of AI for the prediction of fever etiology in ABI patients on the ICU, this study would need to be repeated with an improved dataset. 

## Code and report
The data and code for this project can be found on the IC research disk of the RadboudUMC.

The final report for this project can be found [here](https://drive.google.com/file/d/1Fo8Hd4lkJnLZiU6XSd3zdtMhKW_lvUVA/view?usp=sharing).
