title: Predicting changes in quality of life of ICU survivors
groups: ai-for-health
finished: true
type: student
picture: projects/predicting-icu-survival.png
template: project-single
people:  Manon de Jonge, Marieke Zegers, Mark van den Boogaard, Ruud van Kaam, Luca Ambrogioni
description: Development of a model for prediction of quality of life.

**Start date: 01-02-2020** <br>
**End date: 01-10-2020**

## Clinical problem
Annually, over 85,000 patients are admitted to Dutch Intensive Care Units (ICUs), often in life-threatening circumstances. Due to advances in critical care medicine, more patients survive their critical illness. However, the survival of a serious illness does only rarely pass without consequences. It is estimated that 25% to 75% of ICU survivors experience physical problems (e.g. pain, shortness of breath, reduced muscle strength), psychological complaints (e.g.  anxiety/depression), cognitive problems (e.g. memory-related) and/or problems related to daily functioning. These issues often negatively influence the quality of life (QoL) and the financial and social situation of former ICU patients.

Where the emphasis of ICU healthcare professionals initially was laid on the prevention of a patient's death, the challenge now also lies in studying what the survival of a serious illness means for patients in the long term, and including these adverse consequences in the decision-making process about treatment in the ICU. At the moment, medical decisions about ICU treatment and predictions concerning the post-ICU period and QoL are often made based on the experience and intuition of physicians. 

## Solution
In 2016, the MONITOR-IC study (www.monitor-ic.nl) was set up with the aim of including patient-reported outcome measures in clinical decisions. The study should give insight into the long-term outcomes on the QoL of ICU survivors by monitoring them during a five-year follow-up period. At the moment, the study’s prediction model after a one-year follow-up period has shown that an explained variance of 0.55 can be reached by using traditional statistical analysis methods.

Using the patient-reported outcomes from the one-year follow-up of the MONITOR-IC project in addition to data from the Electronic Health Records (EHR), this research project will focus on the development of a prediction model for changes in QoL using machine learning methods. The hypothesis is that including EHR data and using AI techniques will improve upon the current model’s performance.

## Tasks
 - Deciding on which parameters in the EHR data to include and doing the pre-processing.
 - Developing and evaluating a prediction model for QoL using machines learning techniques. 
 - Conducting analyses of the important factors influencing the QoL.

## Innovation
This project is part of the extension of an ongoing study focused on the integration of patient-reported outcomes in the clinical decision-making process. Worldwide, using patient-reported outcomes during ICU treatment is new in Intensive Care Medicine. In 2020, the use of prediction models in daily clinical practice will be pilot tested in the ICU of the Radboudumc and in 2021 this will be extended to the regional hospitals participating in the MONITOR-IC study. The findings of this project will be used to optimize the traditional prediction models that have been/will be tested before and during this project. This project, therefore, participates in supporting ICU employees with data-driven information in order for them to make substantiated decisions and provide better counseling based on these decisions. Patients and family profit from this technological advance by gaining an understanding of possible consequences following ICU admission and treatment.

_________________________________________________________________________________
## Project results
The addition this project has made to the original statistical approach is twofold. Firstly, several variables (e.g. medication types, pathology tests) were selected from the vast EHR database in consultation with physicians. This expert-augmented approach to variable selection was used to reduce time- and memory-related issues whilst keeping allegedly influential data available based on domain-knowledge. The selection process resulted in the inclusion of seventy-one EHR variables. 

Secondly, several regression-based machine learning models were tested. A regular linear regression model using the original statistical model’s five most important features as predictors was used as a baseline for comparison. Among the ten models that were compared during this study were linear models as well as non-linear models. For each model, either built-in regularization or recursive feature elimination (RFE) was used to select the most influential EHR variables to use for target prediction. The prediction results were evaluated using the adjusted R^2, mean squared error (MSE), and mean absolute error (MAE). 

Results showed that, while some models outperform others slightly, the differences for the five-feature baseline were minimal. The addition of EHR features resulted in an increase in predictive performance for all tested models. However, the effects were, again, minimal. 

Due to the way the Dutch measurement of QoL used in this study (EQ-5D-5L) is defined, changes in QoL scores can theoretically range from -1.45 to +1.45. The baseline model had a MAE of 0.129. Out of all predicted values, 48% differed less than 0.1 from their actual score and 82% differed less than 0.2. The best-performing extended model had a MAE of 0.125. Out of all of its predictions, 53% differed less than 0.1 and 84% differed less than 0.2 from the actual value. These are increases of 5% and 2% respectively. 

Each of the extended models used fifteen features or less for generating predictions. Several of the EHR features included in this project were repeatedly selected by the models. This suggests that these features are of influence to one-year post-ICU QoL. The baseline EQ-5D-5L score (QoL before ICU admission) stayed the most important predictor by far, followed by the prevalence of a cerebrovascular accident (CVA) that was also included in the original study. New features that were considered influential in this study are high body temperature, low BMI, and prevalence of delirium. The full results can be found in this [final report](https://drive.google.com/file/d/1RskDzNP-hgDEAEUz3JxDNwg-zW8vgjtv/view?usp=sharing).


|                        | **Five-feature baseline** |       |       | **Baseline + EHR data** |          |       |       |
|------------------------|-----------------------|-------|-------|---------------------|----------|-------|-------|
| **Model**                 | **adj. R^2**              | **MSE**   | **MAE**   | **Nr. of features**     | **adj. R^2** | **MSE**   | **MAE**   |
| Ordinary Least Squares | 0.52                  | 0.032 | 0.129 | 9                   | 0.54     | 0.031 | 0.127 |
| Random Forest          | 0.51                  | 0.033 | 0.130 | 7                   | 0.51     | 0.032 | 0.129 |
| MLP Regressor          | 0.46                  | 0.035 | 0.136 | 11                  | 0.51     | 0.032 | 0.127 |
| LassoCV                | 0.52                  | 0.032 | 0.129 | 8                   | 0.53     | 0.031 | 0.128 |
| Lars                   | 0.52                  | 0.032 | 0.129 | 13                  | 0.54     | 0.030 | 0.127 |
| ElasticNet             | 0.52                  | 0.032 | 0.129 | 13                  | 0.54     | 0.030 | 0.127 |
| Huber Regressor        | 0.52                  | 0.032 | 0.126 | 7                   | 0.52     | 0.032 | 0.125 |
| Ridge                  | 0.52                  | 0.032 | 0.129 | 13                  | 0.54     | 0.030 | 0.127 |
| ARD Regression         | 0.52                  | 0.032 | 0.129 | 15                  | 0.53     | 0.031 | 0.127 |
| SVR                    | 0.52                  | 0.032 | 0.127 | 13                  | 0.53     | 0.031 | 0.125 |

## Conclusion
Due to the increased survival rate of ICU patients, the long term outcomes of the survival of a serious condition  become  progressively  more  important.  With  predictive modeling, the consequences of the ICU stay in terms of QoL can be estimated. Statistical models using  mostly  patient-reported  data  have  proven  to  provide a substantial prediction method for changes in a patient’s  QoL  within  one  year  after  ICU  admission. The results of this study show a slight increase in predictive performance by machine learning models using additional EHR data on top of patient-reported data. However, the increased effort by physicians needed for putting these findings into practice outweighs the slight improvement in prediction quality. It can, therefore, be concluded that the examined EHR variables in combination with the regression models that were tested do not provide sufficient added value to the already existing statistical model.

The results of this study did, however, unveil some EHR variables that influence a patient's QoL one year after admission. High temperatures, low BMI, and delirium prevalence are some of the variables of which their importance was ranked highly by the models. More research is needed to evaluate the effects of these and other EHR variables on patients' QoL changes after ICU admission in detail.

