title: AMI
finished: true
type: general
picture: projects/AMI.png
template: project-single
groups: pathology, retina, diag
default_group: diag
people: Péter Bándi, Bart Liefers, Gabriel Humpire Mamani, Marcory van Dijk, Geert Litjens, Jeroen van der Laak, Clarisa Sánchez, Colin Jacobs, Bram van Ginneken
description: Automation in Medical Imaging - a joint project between DIAG and Fraunhofer MEVIS aimed at the development of a generic platform for automatic medical image analysis.


## Background
Innovative procedures based on digital imaging are changing healthcare: clinical decision making becomes increasingly dependent on images, and images permeate all aspects of medicine from detection and diagnosis to interventions and treatment monitoring. The number of images consequently increases, increasing healthcare costs for their acquisition, but importantly also for image interpretation and communication. Automation as proposed in this project can help: firstly, by detecting the abnormal cases, and  secondly by extracting relevant and characteristic parameters of the abnormal cases, relating them to known cases, and presenting them in an intuitive and interactive workflow.

Within this project, we focus on three application areas: oncology, 
opthalmology, and pathology.

Radiological imaging is a crucial component of the oncological disease pathway. Cancer patients undergo imaging for detection, diagnosis, and treatment monitoring. CT imaging of the thorax and abdomen is a large portion of the oncological workload of a radiology department and therefore, we focus on automating the interpretation of these scans.

Retinal diseases, such as age-related macular degeneration (AMD) or diabetic retinopathy (DR), are compromising the vision of more and more patients and causing blindness in an alarmingly large percentage of world population. Multimodal retinal imaging has become an indispensable diagnostic tool in Ophthalmology to early detect, treat and monitor these diseases and automated retina image analysis has the potential to improve the diagnostic process and make treatment monitoring more effective. However, efficiently leveraging information contained in multimodal imaging is a complex task and many traditional automated solutions do not suffice to accurately extract the required information.  Specially, the manual assessment of quantitative temporal change for treatment decision of AMD suffers from observer dependence, and the joint assessment of different imaging techniques for one patient leave ambiguities in terms of spatial correspondence.

![Geographic atrophy segmentation in CFI]({{ IMGURL }}/images/projects/ami_cf.jpg)
<br>
<i>Automatic segmentation of geographic atrophy in color fundus images.</i>

For the pathology application, the focus is on breast cancer. Breast cancer is the most common cancer among women. Within their lifetime, 12% of women are diagnosed with breast cancer. The prognosis of breast cancer patients is mainly determined by whether the cancer is organ-confined or has spread to other parts of the body. An internationally accepted means to classify the extent of cancer is the TNM staging system. In breast cancer, TNM staging takes into account the size of the tumor (T-stage), whether the cancer has spread to the lymph nodes (N-stage), and whether the tumor has metastasized to other parts of the body (M-stage). The axillary lymph nodes are typically the first location breast cancer metastasizes to. Currently, the status of these lymph nodes is almost always assessed by applying the sentinel lymph node procedure. This procedure identifies the nearest lymph nodes to which the tumor drains, which are then excised for pathologic examination. Glass slides are prepared from the tissue speciments and stained with hematoxylin and eosin (H&E) to highlight the cell nuclei and the general structural features of the tissue. Through microscopic assessment the pathologist screens the slides for tumor presence. If tumor cells are found, the pathologist measures their extent in order to determine the pathologic N stage (pNstage) of the tumor. In case of unclear diagnosis on H&E, immunohistochemical (IHC) staining for cytokeratin can be used for clarification and is standard diagnostic practice in the Netherlands.

## Aim
The oncology applications aims to develop novel diagnostic algorithms for many different oncological situations and to validate them using an annotated database. The application will focus on temporal follow-up in screening and therapy, supported by automated abnormality linkage and change quantification. Technically, the focus within this application lies in designing the workflows both for general oncology, and for more specialized oncologic workflows.

The opthalmology application aims to develop solutions for the automated analysis of multimodal retinal imaging examinations in order to assess treatment response in patients with advanced wet AMD and provide treatment decision support to clinicians. For that, as an alternative to traditional techniques, deep learning algorithms will be developed that can accurately analyze and quantify changes in follow-up optical coherence tomography scans and multimodal retinal images. In this project, we will also integrate these algorithms in a platform tailored to provide an advanced visualization of these changes and the joint review of multimodal retinal images.

The pathology application aims to develop deep neural networks that can automatically detect and outline the tumor areas on the digitized version of the glass slides. With these outlines we would like to help steering the attention of the pathologist during assessment for faster, and more accurate evaluation. Furthermore, in current practice, the IHC staining is only made when the pathologist cannot find tumor lesions in the lymph node tissue and needs clarification. With the developed algorithm, we automated this process by pre-screening the scanned slides. If the algorithm could not find cancer in the screened whole-slide images, the system would order the IHC stained clarification slides automatically. The practicing pathologist would be presented with whole-slide images where the algorithm already outlined the identified tumor areas or an attached IHC clarification, in case of cancer free slides further accelerating the evaluation process. Finally, in this project we also developed web based whole-slide image viewers that can be accessed via a web browser for client independent viewing and assessment.

## Funding
AMI is a collaborative project of the [Fraunhofer Gesellschaft](https://www.fraunhofer.de/) and the [Radboud University and University Medical Center](https://www.radboudumc.nl/en/research).

## Media
- Best Demo Award from Live Demonstrations Workshop at SPIE Medical Imaging 2017 : “A Multimodal Workstation for Analysis of Retinal Images”
