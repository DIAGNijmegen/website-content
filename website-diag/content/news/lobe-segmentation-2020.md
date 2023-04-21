title: Pulmonary lobe segmentation for CT-scans COVID-19 and COPD patients.
date: 2020-06-17
description: Pulmonary lobe segmentation in computed tomography scans is essential for regional assessment of pulmonary diseases. Our algorithm for automatic segmentation of pulmonary lobes on CT scans for patients with COPD or COVID-19 is now available on Grand Challenge.
picture: news/lobe_segmentation_I.png
groups: diag

Automated pulmonary lobe segmentation in computed tomography scans is still an open problem, especially for scans with substantial abnormalities, such as in COVID-19 infection. Recent works used Convolutional Neural Networks for automatic pulmonary lobe segmentation. Convolution kernels in these networks only respond to local information within the scope of their effective receptive field, and this may be insufficient to capture all necessary contextual information. 

[member/weiyi-xie] and colleagues argue that contextual information is critically important for accurate delineation of pulmonary lobes, especially when the lungs are severely affected by diseases such as COVID-19 or COPD. They propose a propose a relational approach (RTSU-Net) that leverages global context by introducing a first stage in which the receptive field encompasses the entire scan and by using a novel non-local neural network module. 

With a limited amount of training data available from COVID-19 subjects, [member/weiyi-xie] et al initially train and validate RTSU-Net on a cohort of 5000 subjects from the COPDGene study (4000 for training and 1000 for evaluation). Using the models pretrained on COPDGene,  transfer learning  was applied to retrain and evaluate RTSU-Net on 470 COVID-19 subjects (370 for retraining and 100 for evaluation). Experimental results show that RTSU-Net outperforms state-of-the-art baselines and performs robustly on cases with incomplete fissures and severe lung infection due to COVID-19. The algorithm is available on <a href="https://grand-challenge.org/algorithms/">Grand Challenge</a>, where users are free to use the algorithm on their own data sets. Read more about the RTSU-Net in the <a href="https://ieeexplore.ieee.org/document/9094216">TMI paper</a>, published online on the 15th of May.

![Results automated pulmonary lobe segmentation in COVID-19 patients]({{ IMGURL }}/images/news/lobe_segmentation_II.png)

The image above displays a qualitative comparison of the proposed CTSU-Net segmentation (middle row) and ground truth (bottom row) in CT scans of COVID-19 patients. Blue: right upper lobe, light blue: right lower lobe, red: left upper lobe, green: left lower lobe. 


