title: AI predicts lung cancer risk
date: 2021-05-26
description: Kiran Vaidhya Venkadesh and team developed an AI algorithm for predicting the malignancy risk of lung nodules. This work appeared in Radiology.
picture: news/lung-nodule-malignancy-risk-cnn.png
groups: diag

Lung cancer is the leading cause of cancer death worldwide, with an estimated 1.8 million deaths in 2020, according to the World Health Organization. Screening for lung cancer using low-dose chest CT scans in people at a high risk of lung cancer, such as longtime smokers, has been shown to significantly reduce lung cancer mortality, primarily by helping to detect cancers at an early stage when they are easier to treat. 

While lung cancer typically shows up as lung nodules on CT images, most nodules are benign and do not require further clinical workup. Accurately distinguishing between benign and malignant nodules is therefore crucial to optimize nodule management in lung cancer screening.

[member/kiran-vaidhya-venkadesh] and colleagues from Radboudumc and the Danish Lung Cancer Screening Trial team built an AI algorithm that accurately predicts the risk that lung nodules detected on screening CT will become cancerous.

For this study, they trained a deep learning (DL) algorithm with 16,077 nodules (1,249 cancers) from the National Lung Screening Trial. They externally validated the algorithm with 883 nodules (65 cancers) from the Danish Lung Cancer Screening Trial. 

The deep learning algorithm delivered excellent results, outperforming the established Pan-Canadian Early Detection of Lung Cancer model ([PanCan model](https://www.nejm.org/doi/full/10.1056/nejmoa1214726)). It performed comparably to 11 clinicians, including four thoracic radiologists, five radiology residents, and two pulmonologists.

The study was published in [Radiology](https://pubs.rsna.org/doi/10.1148/radiol.2021204433) on 18th May 2021. A press release can be found [here](https://www.rsna.org/news/2021/may/AI%20Predicts%20Lung%20Cancer%20Risk). The AI system is freely available on [grand-challenge.org](https://grand-challenge.org/algorithms/pulmonary-nodule-malignancy-prediction/). You can upload a chest CT scan along with the coordinates of the lung nodules, and inspect the outputs of the algorithm in a web browser. 

The team at Radboudumc, led by [member/colin-jacobs], plans to continue improving the algorithm by incorporating clinical parameters like age, sex, and smoking history.
They are also working on a deep learning algorithm that takes multiple CT examinations as input. The current algorithm is highly suitable for analyzing nodules at the initial, or baseline, screening, but for nodules detected at subsequent screenings, growth and appearance in comparison to the previous CT are important. The team has also developed other algorithms to reliably extract imaging features from the chest CT related to chronic obstructive pulmonary diseases and cardiovascular diseases. They will be investigating how to effectively integrate these imaging features into the current algorithm.
For more information about this research line, please visit [this page](https://www.diagnijmegen.nl/research/lung-cancer-image-analysis/).
