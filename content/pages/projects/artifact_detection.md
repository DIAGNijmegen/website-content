title: Artifact detection in digitized histopathology images
groups: pathology, diag, ai-for-health
finished: false
type: student
picture: vacancies/pathology_artifact_detection_msc.png
template: project-single
people: Gijs Smit, Caner Mercan, Francesco Ciompi
description: Development of a deep learning algorithm that can classify the different types of artifacts in whole slide images.

**Start date: 15-08-2020** <br>
**End date: 15-02-2021**

## Clinical problem
Whole slide imaging technology allowed the digitization of conventional glass slides, which led to several new opportunities in the Pathology field, such as the integration of computational systems, most notably artificial intelligence (AI). However, the digitization process also brought along new challenges for the automated analysis of digitized images. One of the most important challenges arises from the presence of image artifacts. The image below shows examples of common types of artifacts found in whole slide images; (a) out-of-focus, (b) tissue folds, (c) ink, (d) dust, (e) pen mark, and (f) air bubbles.

![Artifact Types]({{ IMGURL }}/images/projects/pathology_artifact_detection_artifacts.png)

Depending on the severity of artifacts that are present, tissue regions that are important for diagnosis could be unclear, unusable, or even be completely missing. As a result, an AI system can fail to make a correct diagnosis in those regions. A quality control mechanism is needed to ensure that whole slide images are of good enough quality to be further analyzed by pathologists. Additionally, the quality system could provide recommendations, such as rescanning the whole slide image or leaving out defect regions of the slide when making diagnoses. Here is an example image with artifacts causing an AI algorithm to make false predictions;

![AI making false prediction]({{ IMGURL }}/images/projects/pathology_artifact_detection_falsepreds.png)

In the Pathology department of Radboudumc, every scanned whole slide image is manually inspected on its quality by technicians. Approximately 1.68% of scanned slides are rescanned due to having too poor quality. The high volume of the slides and the sheer size of the scanned images (reaching up to 100,000 x 200,000 pixels) make manual control and supervision a highly time-consuming task for technicians. 

## Solution
We propose a solution to this problem in the form of an AI system that detects and highlights regions containing artifacts in whole slide images using deep learning methods. The goals of this AI system are to speed up the process of digitization of slides and to make other AI algorithms more robust against artifacts.

Initially, the AI system will be trained to detect out-of-focus, tissue folds, ink, dust, pen mark, and air bubbles, as shown in Fig. 1. To our knowledge, these are the most common types of artifacts observed in whole slide images. We will consider other less common artifacts in the later stages of the project. The unique characteristics of some artifacts, in combination with the wide range of tissue types and staining techniques, make artifact detection a challenging task that requires sophisticated solutions. Therefore, an important goal of this project is to develop a generalizable AI solution that can accurately detect different types of artifacts in a wide range of tissue and staining types.

To train deep learning models, we will use multiple data sources. These include an in-house data set of over 300 whole slide images from several organ types and staining. There will be additional data sets provided from partners (out-house data sets).

The desired outcome of the project is to deploy the AI-driven algorithm as part of the quality control (QC) systems in a clinical setting. An additional but important impact will be on the existing and upcoming AI algorithms by assisting them in making robust predictions in the presence of artifacts in whole slide images. A secondary project outcome will be in the form of a publication describing the AI system, deep learning methodology, used datasets, and obtained results within the scope of the project.

## Tasks
- Collect and label artifacts in whole-slide histopathology images.
- Development of AI for segmentation of regions with artifacts present.
- Development of a demonstrator to show the developed system in action.
- Writing of manuscript following publication guidelines.

## Innovation
The developed tool will be tested in the Department of Pathology of the Radboudumc. A major milestone of the project is to demonstrate that the tool can help pathologists to speed up the process of digitization of slides, as well as making other AI algorithms more robust against artifacts.


