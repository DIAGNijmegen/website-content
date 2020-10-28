title: Detecting Fractures in the Radius, Ulna, and Metacarpal Bones on Conventional Radiographs
groups: ai-for-health
finished: false
type: student
picture: vacancies/fracture_detection_radius_ulna_metacarpals_msc_project.jpg
template: project-single
people: Jeroen Verboom, Nils Hendrix, Matthieu Rutten, Bram van Ginneken
description: Development of a deep learning algorithm and web application for automated detection of fractures in the radius, ulna, and metacarpal bones on conventional radiographs. 

**Start date: 25-01-2021** <br>
**End date: 26-07-2021**

## Clinical problem
Hand and wrist injuries are one of the most common and costly injury types encountered at the emergency department. [Research](https://www.injuryjournal.com/article/S0020-1383(16)30147-4/fulltext) has shown that the total costs of these injuries amount to 410 million dollar per year in the Netherlands, of which 75% are related to lost productivity in the working population. Among hand and wrist injuries, bone fractures are most frequently diagnosed: a text analysis of radiology reports at the Jeroen Bosch Hospital and Radboud University Medical Center shows that approximately 56% of all radiographic studies of the hand and wrist concern a fracture. In particular, the incidence of fractures in the radius, ulna, and metacarpal bones is remarkably high, accounting for half of the fractures. Radiography is the standard imaging technique of choice for fracture detection after trauma, but wrist fractures can be [overlooked](https://link.springer.com/article/10.1007%2Fs10140-014-1278-1) on this modality. Missed diagnoses may have severe clinical consequences for the patient, such as non-union, osteoarthritis, surgical intervention, and ultimately functional loss. Given these risks and the high productivity costs they would incur, it is essential to not overlook a fracture and start adequate treatment as soon as possible.   

## Solution 
We would like to improve the diagnostic performance on conventional radiographs for fracture detection by means of an artificial intelligence (AI) system. Recent studies in the field of AI show that convolutional neural networks (CNNs) are a promising solution for automated fracture detection on radiographs. By teaming them up with the radiologist, they have great potential to improve the diagnostic performance, possibly preventing missed diagnoses and allowing for earlier treatment. In this project, we will focus on the most common fractures, which occur in the radius, ulna, and metacarpal bones. 

## Data
We have access to over one hundred thousand hand and wrist radiography studies from Radboudumc and Jeroen Bosch Ziekenhuis and the corresponding radiology reports that can be used to develop the AI system.

## Approach
Jeroen will be supervised by a [DIAG](https://www.diagnijmegen.nl/) research member whose research is dedicated to bone fracture detection with machine learning techniques. Depending on the project progression, he will be guided to set up a state-of-the-art CNN-based system for detecting fractures in one or more of the bones of interest (radius, ulna, metacarpals). The final deliverable will be a publicly available algorithm on the platform [Grand Challenge](https://grand-challenge.org/algorithms/). Students get access to the high-performance deep learning cluster of DIAG, named [SOL](https://rtc.diagnijmegen.nl/software/sol/), for running machine learning experiments.  
