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

## Methods 
We propose an artificial intelligence (AI) system that can automatically detect distal radius and ulna fractures on conventional radiographs of the hand and wrist in any direction. The main goal of this system is to aid radiologists with identifying radius and ulna fractures by acting as a second reader. The fracture detection is conducted in three steps. Firstly, patches of the radius and ulna are extracted from a radiograph with a YOLOv5 bounding box detection network. This way, irrelevant image regions can be excluded from the analysis. Secondly, each extracted patch is passed to one of four InceptionV3 classification networks depending on detected body part (radius or ulna) and direction (frontal or lateral) for fracture analysis. For each patch a probability is returned whether it contains a fracture or not. Finally, image regions that were most influential to the AI predictions are visualized as heat maps using the ScoreCAM method for fracture localization. 

## Results
We trained the AI system per body part (radius or ulna) and direction (frontal or lateral) on 5184 radiographs (1135 patients) from the Radboud University Medical Center. Next, we evaluated the system on an external dataset of 472 radiographs (114 patients) from the Jeroen Bosch Hospital. The binary labels (fracture present/absent) of this dataset were based on a follow-up CT scan within four weeks (ground-truth). On the frontal and lateral radius fracture detection task, it achieved an AUC of 0.93 and 0.78 respectively (332 frontal radiographs [166 fractured], 140 lateral radiographs [70 fractured]). On the frontal and lateral ulna fracture detection task, it achieved an AUC of 0.94 and 0.90 respectively (254 frontal radiographs [127 fractured], 118 lateral radiographs [59 fractured]). A qualitative analysis of the corresponding ScoreCAM heat maps revealed that the highlighted image regions correlated with the fracture location.    

![radius-ulna-fracture-detection]({{ IMGURL }}/images/projects/example_outputs_radius_ulna_fracture_detector.png)
_Examples of heat maps produced by the AI system highlighting visual evidence that a fracture is present._

## Conclusion
We developed an AI system that can automatically detect distal radius and ulna fractures on conventional radiographs with state-of-the-art performance. Furthermore, we demonstrated that fractures can be successfully located using the ScoreCAM method. By teaming the AI system up with the radiologist, it may have great potential to improve the diagnostic performance, possibly preventing missed diagnoses and allowing for earlier treatment. In future research, an observer study could be conducted to investigate this hypothesis. 

The master thesis can be found [here](https://github.com/RadboudAIforHealth/master-theses/blob/main/Master_thesis_Jeroen_Verboom.pdf).

The code for this project can be found in this [GitHub repository](https://github.com/DIAGNijmegen/DIAG_Jeroen_Verboom_radius-ulna_fracture_detection).

The algorithm will be made publicly available on the platform Grand Challenge soon.

