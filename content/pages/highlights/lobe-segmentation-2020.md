title: Contextual two-stage U-net for pulmonary lobe segmentation in COVID-19 and COPD patients.
date: 2020-04-27
description: Pulmonary lobe segmentation in computed tomography scans is essential for regional assessment of pulmonary diseases. Our algorithm for automatic segmentation of pulmonary lobes on CT scans for patients with COPD or COVID-19 is now available on Grand Challenge.
picture: lobe_segmentation_I.png
groups: diag

Automated pulmonary lobe segmentation in computed tomography scans is still an open problem, especially for scans with substantial abnormalities, such as in COVID-19 infection. Recent works used Convolutional Neural Networks for automatic pulmonary lobe segmentation. Convolution kernels in these networks only respond to local information within the scope of their effective receptive field, and this may be insufficient to capture all necessary contextual information. 

[member/xie-weiyi] and colleagues argue that contextual information is critically important for accurate delineation of pulmonary lobes, especially when the lungs are severely affected by diseases such as COVID-19 or COPD. They propose a contextual two-stage U-net (CTSU-Net) that leverages global context by introducing a first stage in which the receptive field encompasses the entire scan and by using a novel non-local neural network module. 

With a limited amount of training data available from COVID-19 subjects, [member/xie-weiyi] et al initially train and validate CTSU-Net on a cohort of 5000 subjects from the COPDGene study (4000 for training and 1000 for evaluation). Using the models pretrained on COPDGene,  transfer learning  was applied to retrain and evaluate CTSU-Net on 204 COVID-19 subjects (104 for retraining and 100 for evaluation). Experimental results show that CTSU-Net outperforms state-of-the-art baselines and performs robustly on cases with incomplete fissures and severe lung infection due to COVID-19. The algorithm is now available on <a href="https://grand-challenge.org/algorithms/">Grand Challenge</a>, where users are free to use the algorithm on their own data sets.

![Results automated pulmonary lobe segmentation in COVID-19 patients]({static}/images/news/lobe_segmentation_II.png)

The image above displays a qualitative comparison of the proposed CTSU-Net segmentation (middle row) and ground truth (bottom row) in CT scans of COVID-19 patients. Blue: right upper lobe, light blue: right lower lobe, red: left upper lobe, green: left lower lobe. 

Read more about the CTSU-Net in the <a href="https://arxiv.org/abs/2004.07443">ArXiv paper</a>.
