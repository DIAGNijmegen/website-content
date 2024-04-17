title: ULS23
title_long: Universal Lesion Segmentation
finished: false
type: general
picture: projects/uls23.png
template: project-single
groups: diag
people: Max de Grauw, Bram van Ginneken, Alessa Hering
description: Building and Evaluating Universal Lesion Segmentation Models for Computed Tomography
bibkeys: 

## Background

In recent years, the number of CT exams conducted annually has continued to increase, resulting in higher workloads for radiologists. With a predicted rise of 47% in global cancer burden in 2040 compared to 2020 oncological radiology can be expected to be a major contributor to future workload increase, especially since patients with cancer often have multiple imaging exams over an extended period of time to track disease progression.

The quantification of disease progression and treatment response in longitudinal CT scans often relies on manual long or short-axis measurements of lesions. Typically, these measurements are interpreted using the Response Evaluation Criteria In Solid Tumors (RECIST) guidelines, which were developed to standardize and speed up this process. The guidelines limit the number of lesions that need to be measured to a maximum of five "target lesions", across multiple organs or structures, using which the overall response is estimated.

To reduce the time burden of annotating lesions in oncological scans, automatic segmentation models can extract information with limited guidance from a radiologist. Guidance can consist of a single-click inside the lesion by a radiologist or by using a bounding box prediction of a detection model. Segmenting the lesion volume in 3D provides additional information that can be leveraged to calculate more informative lesion volumes or lesion characteristics. Registration algorithms can also be used to propagate segmented lesions, enabling significant time savings during follow-up exams.

Significant advancements have been made in AI-based automatic segmentation models for tumours. Medical challenges focusing on e.g. liver, kidney, or lung tumours have resulted in large performance improvements for segmenting these types of lesions. However, in clinical practice there is a need for versatile and robust models capable of quickly segmenting the many possible lesions types in the thorax-abdomen area. 

For these reasons we hosted [the ULS23 challenge](https://uls23.grand-challenge.org/) in which we evaluated the state-of-the-art in ULS. 
