title: Natural language processing of radiology reports for lesion detection 
groups: ai-for-health, diag 
finished: false 
type: student 
picture: vacancies/NLP_lesion_detection.png
template: project-single
people: Koen Dercksen, Max de Grauw, Bram van Ginneken
description: Develop a method to automatically find statements in radiology reports on presence, size and type of lesions in CT scans. 

Manuela Bergau
 **Start date: 10-01-2022** <br>
 **End date: 10-07-2022**
 
Thomas van den Broek
 **Start date: 11-10-2021** <br>
 **End date: 11-04-2022**

## Clinical Problem 

The work of a radiologist is to describe relevant findings that can be seen on an imaging study in the form of a free text report. Although radiologists learn to report their findings in specific ways, following a certain writing style and vocabulary, and sometimes even start from templates that relate to the clinical question and the type of scan acquired, the text is to a large extent unstructured. If we want to use the images and their reports for research, this is a big limitation. It is also an interesting challenge for natural language processing (NLP) researchers.  

Converting radiology reports into structured information would have many possible applications. In this project, we focus on lesions that are visible in CT scans. Radiology reports list the presence of such lesions, and often contain numbers from measurements of the size of the lesion and provide the type of lesion and mention where the lesion is located. For example, the report may say *“Nodus in de linker bovenkwab, 7 mm, binnen marge van meetfout ongewijzigd vergeleken met vorig onderzoek, is afgenomen vergeleken met <DATE> (zie ima 83 serie 4).”* We are looking for an accurate automatic method to extract this information from radiology reports.  

There are two direct use cases for this method related to two ongoing PhD research projects at Radboudumc and Radboud University. The first is to use the text processing to efficiently collect more training and validation data to improve a universal lesion segmentation algorithm that has been developed by [Max de Grauw]( https://www.diagnijmegen.nl/people/max-de-grauw/). The second is to prepare parts of an annotated radiology report that is more understandable to a patient, the task addressed in the project of [Koen Dercksen]( https://www.diagnijmegen.nl/projects/mihracle/).   

 

## Solution 

A method should be developed that parses a radiology report and produces a list of findings with for each finding 1) the sentence or part of the report that describes the finding; 2) the type of lesion (for example *nodule*, *mass*, *metastasis*; 3) the slice number at which the lesion appears (usually specified in the report); 4) the size of the lesion in mm (often specified in the report); 5) the organ or structure in which the lesion is located (for example *liver*); 6) the location or position of the lesion (for example *left* or *posterior*); 7) characteristics of the lesion (for example *hypodense*, *spiculated*, or *sclerotic*). For output 2, 5, 6 and 7 a list will be compiled with all possible outputs.  

As a secondary objective, the lesion should be detected in the slice in which it occurs, using a standard 2D bounding box detector, such as [Yolov5]( https://github.com/ultralytics/yolov5) or [Detectron2]( https://github.com/facebookresearch/detectron2).  

 

## Data 

A database of 250,000 Dutch radiology reports from CT studies where the thorax, abdomen or both were imaged are available. Protected health information has been removed from these reports using in-house developed tools. All studies were done at Radboudumc between 2000 and 2021. The CT scans are also available. The reports have not been annotated yet, but simple tools are available to find potential mentions of lesions in the reports and efficiently label a subset of the reports. This data preparation process is part of the assignment.  

 
