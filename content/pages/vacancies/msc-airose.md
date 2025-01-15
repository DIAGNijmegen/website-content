title: Automation of cytology-to-diagnosis using a smartphone
groups: diag, pathology
closed: false
type: student 
picture: vacancies/msc-airose.png
template: vacancy-single
people: Francesco Ciompi, Siem de Jong, Roel Verhoeven, Erik van der Heijden
description: Efficient artificial intelligence for rapid on-site evaluation during navigation bronchoscopy 

## Background
Every day, lung cancer is diagnosed on the base of lung biopsies, tiny samples of lung tissue that needs to be examined under the microscope. In most cases, lung biopsies are acquired in the operating room (OR) via a navigational bronchoscopy and endobronchial ultrasound (EBUS) procedure. The biopsied tissue is then inspected onsite via cytology, a procedure consisting of smearing the sample on a glass slide during the procedure, staining it with chemical components to make cells visible, and inspecting it under the microscope, commonly placed in or next to the OR. Such a procedure is called Rapid On-Site Evaluation (ROSE), and it usually takes 1-2 minutes from sample smearing to final diagnosis.
While being an essential part of the lung cancer diagnostic chain, ROSE has several problems. First, the availability of cytopathologists is scarce, a current reality that is expected to get worse in the future [1], limiting the possibility to perform ROSE in most medical centers. Second, when available, the cytopathologist must be present next to the OR during the entire operation. Since samples during EBUS are acquired and diagnosed sequentially, until a representative sample is found, the cytopathologist mostly remains “in idle” while waiting for the next sample to come. Third, ROSE is subject to inter-observer variability, especially when cytopathologists with various levels of experience are involved. Fourth, ROSE is still an analog procedure, performed by inspecting the glass slide under the microscope. Digital cytology would facilitate opportunities to automate ROSE diagnosis and make it possible also in settings when no cytopathologist is available, also via tele-cyto-pathology [2]. 

## Approach
In this project, we address all these problems by developing an efficient AI model to detect and diagnose lung cancer by processing digital cytology images acquired during ROSE. For this, we will rely on a smartphone, a technology that is increasingly being used for research and development in medicine [3-6], connect to an analog microscope via an adapter, and use it to acquire high-quality images of cytology ROSE samples.
We will train the AI model using images acquired using a smartphone camera attached to a microscope, a low-cost and easily adoptable approach to a) enable digital cytology for everyone, and b) allow data collection from multiple centers. We will first test different commercially available smartphone adapters [7] for microscopes and then select the most suitable one to acquire data for this project. We will train models using weakly supervised learning approaches, using slide-level labels obtained via cytological analysis, with particular focus on lightweight yet effective models that can run on a mobile (or cloud-based) platform. 

## Data 
We will use >1,000 cytology samples collected in the navigation bronchoscopy registry from the archive of Radboud University Medical Center, for which the final diagnosis is known. We will digitize each case using the selected adapter and a smartphone and use images for training and validation of the AI developed in this project.

## References
* [1] https://www.sciencedirect.com/science/article/pii/S2213294521000521
* [2] https://pmc.ncbi.nlm.nih.gov/articles/PMC5846691/
* [3] https://www.nature.com/articles/s41746-024-01159-9
* [4] https://www.nature.com/articles/s41467-023-38104-5
* [5] https://www.medrxiv.org/content/10.1101/2024.09.19.24313954v1.full.pdf
* [6] https://link.springer.com/article/10.1007/s00216-023-04978-z
* [7] https://skopedmicro.com

## Requirements 
Students with a major in computer science, biomedical engineering, artificial intelligence, or a related area in the final stage of master level studies are invited to apply. Knowledge of the Python programming language is needed. Experience with development in iOS (Swift) or Android is a plus.

## Information 
- Project duration: 6-9 months 
- Location: Radboud University Medical Center 
- You will be part of the Diagnostic Image Analysis Group (DIAG) and Computational Pathology Group, whose research focus is the analysis of histopathological slides with deep learning techniques. 
- You will have access to and work with a large GPU cluster.
- For more information, please contact [member/francesco-ciompi] and Roel Verhoeven (roel.lj.verhoeven@radboudumc.nl)
