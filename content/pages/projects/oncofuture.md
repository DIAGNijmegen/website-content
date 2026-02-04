title: OncoFuture
title_long: OncoFuture: improving tumor follow-up assessment
finished: false
type: general
picture: projects/oncology.jpg
template: project-single
groups: diag
people: Niels Rocholl, Jan Tagscherer, Rianne Weber, Alessa Hering, Mathias Prokop
description: Improving tumor follow-up assessment
bibkeys: 

## General overview
The aim of OncoFuture is to improve the efficiency of tumor follow-up assessment in whole body CT imaging. This is done through the creation of cutting-edge AI algorithms capable of combining data from multiple timepoints that can both detect and segment tumor metastases. This project is divided into multiple subprojects, which are explained in more detail below. All these subprojects are supervised by [member/alessa-hering] and Ewoud Smit. 

## Detection
This research is conducted by [member/jan-tagscherer]. Finding abnormalities such as primary tumors and metastases as well as other lesions in CT images is a common radiological task that can guide treatment decisions and can be used for treatment evaluation in oncology. However, it is time-consuming for human readers to find lesions in these scans, and radiologists might miss lesions. This study aims to help with this task by detecting lesions automatically. 
Its main focus will be the development of an AI-based model for automatic detection of lesions and metastasis in CT images. The model will use multi-modal information, integrating diverse data sources. The study will also analyse how to include data such as foundational medical knowledge, radiological reports, primary tumour locations, and other clinical patient information like age and tumour markers. 

## Segmentation
This research is conducted by [member/niels-rocholl]. This study focuses on three core pillars: longitudinal imaging, robustness, and uncertainty quantification. While longitudinal imaging is a common practice in a patient lifecycle, leveraging its temporal information to improve segmentation remains under-explored. Current models typically analyse scans in isolation, ignoring prior scans. This study aims to improve segmentation performance by exploiting the temporal dimension, designing novel methods that can efficiently and elegantly integrate information from prior scans. 
The second pillar tackles robustness, ensuring segmentation consistency across variable conditions. A key challenge is sensitivity to user inputs: slight changes in click-point location can produce drastically different segmentation results. This work aims to stabilize predictions against such variability. 
Finally, uncertainty quantification will equip models with the ability to communicate confidence, enabling radiologists to prioritize ambiguous regions and refine outputs a collaborative feedback loop with the model. 

## Clinical validation
This research is conducted by [member/rianne-weber]. While technical validation of AI models is crucial, clinical validation of these models is equally important to determine the effect of the use of such models in a real-life setting. This project focuses on clinically validating the algorithms developed within the OncoFuture project. This is done through reader studies, where radiologists from within and outside the Radboudumc are asked to interact with the algorithms. These studies will allow us to determine what impact the models have on multiple clinically relevant factors, such as time spent on evaluating the scans, quality of the diagnosis, and inter-reader variability.

