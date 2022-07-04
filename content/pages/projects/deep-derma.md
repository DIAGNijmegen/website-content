title: Deep Derma
title_long: Deep Derma
finished: false
picture: projects/deep-derma-logo.png
template: project-single
groups: pathology, diag 
default_group: pathology
people: Daan Geijs,	Avital Amir, Geert Litjens
description: The aim of this project is to apply artificial intelligence to detect basal cell carcinoma. 
bibkeys: 
type: normal

With the threefold increase in skin cancer incidence in the past two decades, more skin biopsies and resections are being performed than ever before. This has led to a huge increase in the workload for pathologists who perform the microscopic diagnosis of skin samples. In particular, the increase in basal cell carcinomas (BCCs) is increasing rapidly. 
This form of skin cancer is not diagnostically challenging for a pathologist. However, because almost 40% of all cancer diagnostics is solely BCC, this puts a heavy burden on microscopic diagnostics. 

| ![Trend of three main groups of skin cancer]({{ IMGURL }}/images/projects/deep-derma-1.png) |
|:--:|
| <b>Fig. 1: </b> Trend of three main groups of skin cancer: Basal cell carcinoma (BCC), squamous cell carcinoma (PCC) and melanoma.|

| ![Distribution of most common tumors]({{ IMGURL }}/images/projects/deep-derma-2.png) |
|:--:|
| <b>Fig. 2: </b> Distribution of most common tumors. Of the most diagnosed cancers in 2017 is by far the largest part of skin cancer (including BCC).|

The rise of artificial intelligence offers solace by automating multiple diagnostic steps. Automation can free up more time for more complex diagnostics and reduce waiting times for patients.
There are multiple clinical tasks that can be automated for a pathologist. The more of these tasks that are automated, the less the pressure on microscopic diagnostics. As a result, this project examines which tasks qualify for this.
An example of a task is shown in the figure below. Here, the pathologist must determine whether there is no tumor at the cutting edges (the part where there is no epidermis at the border) after the operation. 

| ![Distribution of most common tumors]({{ IMGURL }}/images/projects/deep-derma-3.png) |
|:--:|
| <b>Fig. 3: </b> Top: A microscopic image of skin cancer with the epidermis (outer layer of the skin) at the top. All basal cell carcinoma has been circled by a pathologist. Below: Prediction of a developed model where the epidermis is located (yellow) and where skin cancer is located (black). The model learned this by analyzing thousands of labeled examples.|

Within this project we are trying to explore as many of these tasks as possible and hopefully upon completion of this project we will have the world's first evaluated AI assisted pathologist workflow, in addition this project will provide a valuable expert labeled dataset of skin specimens on; both excellent goals for valorisation. Finally, it will extend the time of pathologists for complex diagnostics and reduce the waiting time for patients.

Goals:

- Collection of a paraffin embedded retrospective set of digitized BCC and non-BCC images.
- Collection of a frozen sections retrospective set of digitized BCC and non-BCC images.
- Development of an end-to-end model for predicting presence and subtype of BCC.
- Development of segmentation model for segmenting and determining BCC free margins in excisions. 
- Evaluation of reader performance for subtyping BCC compared to developed end-to-end model. 
- Integration of the developed algorithms in the pathologist workflow.
- Integration of the developed algorithms in the dermatologist MOHS surgery workflow.
- Prospective evaluation of the algorithm in clinical practice.

# Funding

[RIHS Junior Researcher 2020](https://www.radboudumc.nl/en/news/2019/call-rihs-junior-researcher-2020)
