title: AI-Designed 3D prothesis for 3D Printing in third world countries
groups: ai-for-health
closed: false
type: student
picture: vacancies/prosthesis.jpg
template: vacancy-single
people: Merel van der Stelt, Guido de Jong
description: Development of a deep learning algorithm for automatically designing prosthetics based on 3D scans

## Reimbursement
This is an AI for Health MSc project. Students are eligible to receive a monthly reimbursement of €500,- for a period of six months. For more information please read the [requirements](https://www.ai-for-health.nl/requirements).

## Clinical Problem
The WHO estimates that 0.5% of the world's population needs prostheses, and 95% do not have access to them. Materials are not available and the workflows are highly dependent on the skills of the prosthetist, which implies difficulty in quality assurance, standardization, and scalability.
Current prostheses in low- and middle-income countries (LMICs) are of bad quality and fitting vary greatly. Plaster casts are used, which is a time-consuming method. Furthermore, the prostheses are highly dependent on the experience of the local prosthetist.

A joint venture between the 3D laboratory at the Radboud University Medical Centre and the foundation 3D printing in developing countries, started a pilot non-profit 3D lab in 2018 in the Masanga Hospital in Sierra Leone to produce prostheses for people in need. In recent years, we have conducted several [scientific studies](www.3dsierraleone.com/publications/) to investigate the added value of 3D technology in a rural hospital.
We apply computer-aided design (CAD) and computer-aided manufacturing (CAM) to produce low-cost prostheses. Using CAD-CAM techniques, the production process is consistent and faster. The entire process can be automated by following a standardized design workflow including Artificial Intelligence (AI) algorithms for patient-specific socket prediction. Socket fitting becomes less dependent on the individual prosthetist’s skills and experience, thus increasing successful prosthetic fitting rates. We believe that 3D technology can contribute to improve the quality and scalability of prosthetics in LMICs.

A difficult, but very important step in the design process of the prosthesis is building the socket that fits the stump. Deformation of the socket prevents pressure spots. The prosthetic socket designs of especially below-knee sockets are the most challenging. Therefore, an AI-algorithm was made for this socket design last year using machine learning with input from previously obtained scan data of an orthopedic company. The AI socket prediction has been incorporated into an automated design workflow.

The purpose of this proposal is to improve the AI Algorithm to empower people with limited knowledge of both prosthetics and IT to independently produce prostheses. In this way, the rate and amount of successful prosthetic fitting will increase in Low-, middle- and high-income

## Solution
Using a 3D scan (or plaster cast) of an amputee’s stump it is possible to design a prothesis (negative mold). This design involved a combination of standard- and patient- (stump) specific alterations of the 3D scan to provide the best support for a patient. With the AI workflow we aim for automatically designing the prosthesis based upon manipulation of the 3D scan. Therefore, the AI challenge is predictive in nature. The tasks at hand consist of
* A (scoping) literature study for relevant techniques for 3D mesh manipulation with AI
*  Choosing a relevant sampling/ data preprocessing method for your AI solution
*  Statistical analysis for a sanity check and (if relevant) standard adjustments
*  Training the chosen AI to apply the custom manipulations
*  Build the mesh of the 3D negative mold
*  Compare results with our pilot AI solution

As mentioned, we have a pilot AI solution which will be used in comparison to the solution provided in the Master project. Optionally the pilot AI solution can be used as inspiration for this project as well.

## Data
The dataset consists of (at the moment of writing) 116 carefully curated and matched 3D scans of lower leg stumps and the negative mold of the prosthesis as created by professional orthopedic instrument maker. This set is expected to increase over time, but these scans are currently available. Besides the raw (original) 3D scans we also have the sampled 3D meshes of either raycasted or morphable models. The student is free to also apply any custom sampling technique if desired.

## Approach
The main result will be an AI algorithm that can utilize a 3D scan of a lower leg stump to create a 3D model of an adjusted negative mold similar to those made by an orthopedic instrument maker. In the future these negative molds can be used to create 3D printed prosthesis. Considering the manual process of creating such a negative mold can easily take 2-3 hours and is subjective to several iterations we expect the AI designed molds to save time and ideally create one-hit fits for the patients saving a lengthy process of re-adjusting. The Radboudumc orthopedic instrument maker is involved in this process and can, in collaboration with the 3D-Lab, facilitate the construction and fitting of these prosthesis. This project will both affect patients in Sierra Leone as well as in Radboudumc.

The student will be embedded in the Radboudumc 3D-Lab and the [3D Sierra Leone group](https://www.3dsierraleone.com/). 

## Requirements
The candidate should have
* a major in computer science, biomedical engineering, artificial intelligence, physics, or a related area in the final stage of master level studies are invited to apply; 
* affinity with programming in Python; 
* interest in deep learning.
 
It is preferred, but not required, to have experience with manipulation of 3D Meshes. Additionally, knowledge of point-cloud / mesh / graph based AI is also preferred but not required. Having knowledge in these domains can kick-start your master-project.

## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- For more information, please contact [Merel van der Stelt ](mailto:Merel.vanderstelt@radboudumc.nl)

