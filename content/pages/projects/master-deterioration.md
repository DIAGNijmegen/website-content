title: Predicting Clinical Deterioration Events
finished: false
type: student
template: project-single
picture: projects/clinical_deterioration.jpg
groups: ai-for-health
people: Maarten Vos, Tom Heskes, Bas Bredie, Mats Koeneman
description: Predicting clinical deterioration events in hospitalized patients by using novel machine learning techniques.

**Background**<br>
The deterioration of patients on the non-ICU wards of a hospital is a serious issue. Although there is  a low incidence, the effects are large, leading to prolonged length-of-stay, transfers to the ICU ward or even death. To counter this, the Radboudumc and many other hospitals in the world use an early warning system. Currently, the Radboudumc uses MEWS, or Modified Early Warning Score, which requires a nurse to measure five vital signs of a patient, after which the system will output a number of alarm points that indicate the risk of said patient. The MEWS uses bins that are based on expert opinion and the output value is based on the bins in which each of the vital signs fall.  Due to the labor intensive measurements and the large amount of beds on a ward, these vital signs are usually only measured three times a day, providing the clinicians with limited and often out-of-date information to make decisions upon.  

One of the problems with this MEWS score is that it does not discriminate between patients. The normal value for the one patient is a critical value for another and a critical value for the one patient, can be a relatively normal value for the other.  It also does not take into account the vital sign history of a patient, which is assumed to be highly indicative of deterioration. Also, the thresholds for each bins are chosen arbitrarily, based on the values of a large amount of patients and not adapted to fit each individual. These arbitrary cut-offs cause a patient that for example has a temperature of 38.1 to be in a higher bin and thus to have a larger risk than a patient with a temperature of 38.0 degrees Celsius. 

As MEWS just uses the sum of the bins for each vital sign rather than some sort of weighing, all vital signs are considered to be equally important in predicting patient risk, while this is an assumption that is not at all supported by the existing literature. These reasons also cause the MEWS to wield a large amount of false alarms for healthy patients, which will cause ‘alarm fatigue’ in the nurses as they have to constantly recheck each patient that raises an alarm. This causes the nurses to ignore alarms for patients that look healthy, using their intuition rather than the implemented system, rendering such a system with a large amount of false alarms effectively useless.

All of the aforementioned reasons helped us decide that we should find a system that is better than MEWS in detecting patient deterioration, as the current system is incapable of detecting deterioration accurately and at an early stage. 

**Research question**: "How feasible is it to create a system that accurately predicts early clinical deterioration in patients in real-time while limiting the number of false alarms and does this in an explainable manner by providing information about the features that contribute to this prediction and the features that can be left out".

**Tasks**<br>
For my Master thesis, I am currently developing an array of ML models that use the vital signs of the patients and their vital sign history, measured once per minute, along with patient characteristics and admission data (e.g. age, bmi, initial diagnosis and the admission ward) to predict whether that patient is likely to deteriorate in the next couple of hours. Whether the patient is deteriorating or not is determined by looking, amongst other things, at the medication they received during their stay, MET/CPR calls during their stay and whether they eventually died or were transferred to the ICU ward. Several studies have shown that for example cardiac arrests and unplanned ICU transfers are preceded by changes in vital sign values that can be detected a couple of hours before the actual event. Detecting these events at an early stage leaves sufficient time for the clinical staff to prevent such an event, which could severely reduce patient morbidity and mortality. 

A more specific alarming system would limit the number of false alarms, which helps the nurses to be able to respond more accurately to any alarm that they do receive. This would also reduce workload in general.

Another goal of this research is to determine which features are important in predicting patient deterioration, both reducing the cost of measuring all vital signs and giving the clinicians an idea of why the model outputs a higher deterioration risk. This required level of interpretability, along with the complete but rather small data set that is available, severely limits the choice for a model. 

The trained models are being compared to the MEWS that is currently being used in the Radboudumc and other hospitals in the world and we hope to find an increase in accuracy, albeit a small one, as even a small increase in model performance could have large benefits for costs and patient mortality.
