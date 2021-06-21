title: Study on Adversarial Attack Vulnerability of Medical Image Analysis Systems published in Medical Image Analysis
date: 2021-06-21
description: Cristina González Gonzalo (Radboudumc), Gerda Bortsova (Erasmus MC) and Suzanne Wetstein (TU Eindhoven) study previously unexplored factors affecting adversarial attack vulnerability of deep learning medical image analysis systems in three medical domains: ophthalmology, radiology, and pathology.
picture: news/media-adversarial.png
groups: diag

Our paper **‘Adversarial Attack Vulnerability of Medical Image Analysis Systems: Unexplored Factors’**, by Bortsova, González-Gonzalo, Wetstein et al. is now available online in Medical Image Analysis. In this paper, [member/cristina-gonzalez-gonzalo] (Diagnostic Image Analysis Group, Radboudumc / Eye Lab, qurAI Group, UvA) worked in collaboration with Gerda Bortsova (Biomedical Imaging Group Rotterdam, Erasmus MC) and Suzanne Wetstein (Medical Image Analysis Group, TU Eindhoven) to study previously unexplored factors affecting adversarial attack vulnerability of deep learning medical image analysis (MedIA) systems in three medical domains: ophthalmology, radiology, and pathology.

We focus on **adversarial black-box settings**, in which the attacker does not have full access to the target model and usually uses another model, commonly referred to as surrogate model, to craft adversarial examples that are then transferred to the target model. We consider this to be the most realistic scenario for MedIA systems. 

Our experiments show that **pre-training on ImageNet** may dramatically increase the transferability of adversarial examples, even when the target and surrogate’s architectures are different: the larger the performance gain using pre-training, the larger the transferability. **Differences in the development data** between target and surrogate models considerably decrease the performance of the attack; this decrease is further amplified by difference in the model architecture. We believe these factors should be considered when developing **security-critical** MedIA systems planned to be **deployed in clinical practice**.

You can find the paper [here](https://doi.org/10.1016/j.media.2021.102141).
