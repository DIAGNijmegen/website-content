title: Modelling long-term progression of Parkinson’s disease
groups: diag, ai-for-health
finished: false
type: student
picture: projects/decision_support.jpg
template: project-single
people:  Luc Evers, Marjan Meinders, Lieneke van den Heuvel, Bas Bloem, Tom Heskes
description: Development of a model to support treatment decisions regarding cardiovascular risk management in patients with Parkinson’s disease (PD).

## Clinical problem
Parkinson’s disease (PD) is a neurodegenerative disorder with a long disease trajectory where the rate of disease progression strongly varies between patients. One factor that may partly explain this variation – and is a suitable target for treatment – is a patient’s cardiovascular risk profile. Previous cross-sectional studies have indeed shown an association between high cardiovascular risk and impaired cognition and balance in patients with PD. However, it remains unclear whether there is a causal effect, and whether clinicians should consider cardiovascular interventions in individual PD patients (e.g. statins, anti-hypertensive medication) to slow down the disease progression. 

In this project, we use a unique database consisting of 13 longitudinal PD studies, curated by the Critical Path for Parkinson’s Consortium (CPP). This database currently includes 8105 subjects, mostly early PD patients. In addition, the first data from the ongoing Personalized Parkinson Project at the Radboudumc are available. These datasets contain detailed follow-up measurements from multiple domains, including measures for disease progression (e.g. PD symptom scales, cognitive assessments, quality of life), cardiovascular risk factors (e.g. cholesterol levels, blood sugar levels, blood pressure, BMI, smoking history), and cardiovascular treatments (e.g. statins, anti-hypertensive medication).

## Solution
The aim of this project is to develop a decision support system that offers predictions of the causal effect of cardiovascular risk management (prescribing statins and/or anti-hypertensive medication) on long-term progression of Parkinson’s disease symptoms. Predictions will be tailored to a number of clinically recognizable profiles.

In order to use longitudinal observational data to build the underlying model, standard statistical methods are insufficient to address potential confounding. Instead, we will use various advanced causal methods to correct for time-varying confounding. These methods will exploit random variation in the decision to start treatment with statins or anti-hypertensive medication.

## Tasks
-	Build a model for the effect of cardiovascular risk management on the progression of PD symptoms, that takes into account time-varying confounding (using causal methods such as inverse probability of treatment weighting, g-formula, and/or causal forests). 
-	Work together with clinical experts to make sure relevant confounders are included, and that the different types of measurements are appropriately processed.
-	Combine data from multiple datasets using transfer learning techniques, e.g. deal with comparable but not identical outcome measures, differences in the length of follow-up, timing of study visits, etc. 
-	Build a tool to visualize the model’s predictions in a way that is interpretable for clinicians.


## Innovation
This project will result in a decision support tool that offers personalized predictions of the effect of cardiovascular risk management on the progression of PD symptoms, based on representative observational data. If clinically relevant effect are found, this tool may be used by neurologists as complimentary source of evidence in the treatment of patients with PD. In addition, it may contribute to the scientific basis for conducting more expensive randomized controlled trials. 


