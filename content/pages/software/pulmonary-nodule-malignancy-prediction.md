title: Pulmonary Nodule Malignancy Prediction
title_long: Pulmonary Nodule Malignancy Risk Estimation
finished: false
picture: software/pulmonary-nodule-malignancy-risk-estimation-logo.png
template: project-single
groups: diag
people: Kiran Vaidhya Venkadesh, Bram van Ginneken, Mathias Prokop, Colin Jacobs
description: Deep learning for malignancy risk estimation of pulmonary nodules detected at low-dose screening CT
bibkeys: Venk21

<figure class="figure my-4">
  <img data-src="{{ IMGURL }}/images/news/lung-nodule-malignancy-risk-cnn.png" class="figure-img img-fluid lazyload rounded" alt="Overview of the pipeline.">
  <figcaption class="figure-caption">Overview of a deep learning algorithm that estimates malignancy risk of pulmonary nodules from low-dose chest CT.</figcaption>
</figure>

<a name="terms"></a>

# Introduction

Lung cancer is the leading cause of cancer death among both men and women, accounting for nearly 25% of all cancer deaths. While lung cancer typically shows up as pulmonary nodules on CT images, most nodules are benign and do not require further clinical workup.Accurately distinguishing between benign and malignant nodules is therefore crucial to catch lung cancers early. In our new paper published in Radiology, we developed and externally validated a deep learning algorithm for estimating the malignancy risk of lung nodules in low-dose CT scans.

We developed the algorithm with 16,077 nodules (1,249 cancers) from the National Lung Screening Trial. We further externally validated the algorithm with 883 nodules (65 cancers) from the Danish Lung Cancer Screening Trial. In the external validation dataset, our algorithm achieved an AUC of 0.93. It significantly outperformed the clinically established PanCan model. We compared the algorithm with a group of 11 clinicians in cancer-enriched subsets. This group included 4 thoracic radiologists, 5 radiology residents, and 2 pulmonologists. The algorithm performed comparably with thoracic radiologists.

We have made the algorithm freely accessible to the public for research purposes at [grand-challenge.org](https://grand-challenge.org/algorithms/pulmonary-nodule-malignancy-prediction/). 

<a href="https://grand-challenge.org/algorithms/pulmonary-nodule-malignancy-prediction/" class="btn btn-primary btn-lg my-3">Try out the algorithm</a>

Some caveats: the algorithm is highly suitable for nodules seen at baseline screening. But for nodules seen at subsequent screenings, the growth and appearance in comparison to the previous CT images are important. We did not calibrate the risk scores in this study. Therefore, the algorithm tends to be over-confident with its predictions - a known problem with deep learning algorithms. We are working on calibrating the output risk scores. 

[UPDATE] Since July 2021, a calibrator has been added to the algorithm and the method behind the calibration is explained [here](https://www.diagnijmegen.nl/software/nodule-malignancy-risk-calibration/).
