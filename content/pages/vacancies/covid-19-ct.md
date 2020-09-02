title: Improving detection of COVID-19 classification with CT scans
groups: ai-for-health, diag
closed: false
type: student
picture: vacancies/corads-ai.jpg
template: vacancy-single
people: Luuk Boulogne, Colin Jacobs, Bram van Ginneken
description: Development of deep learning algorithms and a web application for automated classification of COVID-19. **This is an AI for Health MSc project.**

**This is an AI for Health MSc project. Students are elgible to receive a monthly reimbursement of €500,- for a period of six months. For more information please visit the [AI for Health website](https://www.ai-for-health.nl/student_projects/).**

## Clinical problem
Early this year, during the first peak of the COVID-19 pandemic, hospitals in hard-hit regions were overflowing with patients presenting at the emergency unit with respiratory complaints. To diagnose COVID-19, a positive RT-PCR test would be needed. But there was a huge shortage of tests and when swabs were made for RT-PCR, the result of the test was often only received after several days. This was a problem, since a physician would like to decide in a few minutes whether to send a patient home for self-isolation or hospitalize him or her, and if so, send him or her to a COVID-19 ward or a regular ward. 

To quickly obtain a working diagnosis, many hospitals decided to make chest CT scans of all COVID-19 suspects arriving at their emergency room. 

Several Dutch hospitals collaborated and produced a standardized system for reporting these CT scans called CO-RADS. Radboudumc validated CO-RADS and showed in a [Radiology publication](https://pubs.rsna.org/doi/10.1148/radiol.2020201473) that in this high prevalence situation predicting whether patients had COVID-19 on the basis of the CT scan alone could be done with high accuracy (area under the ROC curve of 0.95).  

Subsequently, researchers from the Diagnostic Image Analysis Group together with colleagues from Amsterdam and Bremen, developed an AI system to perform this diagnosis and they showed in another [Radiology publication](https://pubs.rsna.org/doi/10.1148/radiol.2020202439) that the AI system, called CORADS-AI and publicly available on [https://grand-challenge.org/algorithms/corads-ai/](https://grand-challenge.org/algorithms/corads-ai/), was nearly as accurate as radiologists in making this assessment.
However, during the first peak of the pandemic, the population of COVID-19 suspects suffered from few other diseases that mimic the appearance of COVID-19, for example other pneumonias (during the COVID-19 peak, the yearly influenza peak had already passed) and other interstitial lung diseases. As CORADS-AI was trained with only scans from Radboudumc obtained during the peak of the pandemic in 2020, we expect that CORADS-AI may perform a lot worse during the upcoming winter season.

Meanwhile, it has become evident that certain laboratory tests from blood are also quite predictive for COVID-19. These blood tests can also provide results within minutes. It is clear that an optimal test would analyze both the CT scan, clinical parameters and blood test results.

## Solution 
We want to improve CORADS-AI by training it to differentiate between COVID-19 and other lung diseases and by combining the CT scan analysis with routinely acquired blood parameters. This improved CORADS-AI system can then be used during the upcoming winter season and maybe it could even do a background screening of any patient who undergoes a chest CT scan in the hospital, flagging suspect cases to the technician who acquires the scan while the patient is still in the room. Patients with a suspicious scan could then receive an RT-PCR test immediately.  

## Data
We have access to several public and proprietary data sets of CT scans, clinical information and blood test results. In total, scans and clinical features of thousands of COVID-19 suspects and people without COVID-19 who were examined in the pre-COVID-19 era, are available. 

## Approach
You will be supervised by [DIAG](http://www.diagnijmegen.nl) researchers who contributed to CORADS-AI. You will have access to [Sol](https://rtc.diagnijmegen.nl/software/sol/), a high-performance deep learning cluster. There are several machine learning approaches you could explore to differentiate between COVID-19 and other lung diseases with overlapping patterns and to combine CT scans with clinical features and blood values. We are looking for two students: one to focus on CT analysis, the other one on combining image analysis with clinical features.

## Requirements
- Students with a major in data science, computer science, or artificial intelligence in the final stage of master level studies are invited to apply.
- Interest in (medical) image analysis and machine learning.
- Affinity with programming in Python and with deep learning packages (e.g. PyTorch) is required.

## Information
-	Project duration: 6 months
-	Location: Radboud University Medical Center
-	For more information, please contact [member/luuk-boulogne]. 

