---
title: Multi-scale phenotyping of mosquito host-seeking behavior using machine learning and computer vision
groups: rtc
closed: false
type: student
picture: vacancies/mosquito-biting.png
template: vacancy-single
people: Felix Hol, Théo Maire
description: Machine learning and computer vision for multi-scale analysis of host-seeking behavior in malaria-transmitting mosquitoes using long-term video data from the BuzzWatch platform
---

## Background

Mosquitoes transmit some of the world’s deadliest pathogens, including the malaria parasite, causing hundreds of thousands of deaths each year. One of the most effective malaria control measures has been the widespread deployment of insecticide-treated bed nets (ITNs), which protect people during sleeping hours when malaria-transmitting mosquitoes are most active [1]. However, recent field studies have shown that mosquitoes increasingly bite earlier in the evening, before people are protected by bed nets [2]. This phenomenon, known as behavioral resistance, threatens the long-term effectiveness of existing malaria control strategies and increases the risk of disease transmission [3].

Despite its importance, the biological basis of altered mosquito host-seeking behavior remains poorly understood. Addressing this knowledge gap requires detailed, long-term, and high-resolution behavioral monitoring under semi-natural conditions. To this end, the BuzzWatch platform was developed: an open-source, AI-enabled behavioral monitoring system that continuously tracks mosquito flight, resting, sugar feeding, and host-seeking behavior over extended periods [4]. The platform combines high-frame-rate video acquisition, environmental sensing, automated delivery of host cues, and light cycle control, all embedded on a Raspberry Pi-based system.

BuzzWatch has recently been deployed in a malaria-endemic region in northern Uganda, generating a large dataset of wild *Anopheles gambiae* and *Anopheles funestus* mosquitoes, the two most important malaria vectors in Africa. By applying machine learning and computer vision techniques to this dataset, this project aims to generate a data-driven, multi-scale characterization of mosquito host-seeking rhythms. These insights are essential for informing future vector control strategies and mitigating residual malaria transmission.

## Approach

The central challenge of this project is to extract meaningful and interpretable behavioral representations from large-scale, heterogeneous video data collected across multiple temporal scales. The dataset includes continuous low-resolution video for population-level monitoring of flight and resting behavior, as well as high-resolution video for targeted analysis of sugar feeding and host-seeking behavior.

The project will focus on three main objectives:

1. Develop supervised learning methods to improve tracking accuracy and generate detailed ethograms (time-resolved behavioral sequences) from both global and local video streams, potentially using modern deep learning architectures such as transformer-based models tailored to different video modalities.
2. Explore unsupervised learning techniques to uncover latent temporal structure in mosquito behavior by embedding ethograms into a shared low-dimensional latent space for comparison across species, conditions, and locations.
3. Optimize and standardize the computational pipeline for deployment directly on the BuzzWatch platform, enabling real-time behavioral monitoring by non-expert users in the field.

## Data

The project will use data from seven field experiments conducted in Uganda. Each experiment consisted of six BuzzWatch stations operating continuously for one week. Each station recorded more than 7,000 hours of low-resolution video capturing flight and sugar-feeding behavior at 1 frame per second.

For flight behavior, corresponding motion-detection data are available at 25 frames per second, including 2D coordinates and tracking information based on Kalman filtering. In addition, high-frame-rate (25 FPS) videos of host-seeking behavior were collected during three experiments, comprising approximately 400 videos (around 200 hours).

For both sugar-feeding and host-seeking videos, YOLO-based object detection results and basic tracking outputs are available, providing a strong foundation for supervised and unsupervised learning approaches.

## References

[1] Bhatt S. et al. The effect of malaria control on *Plasmodium falciparum* in Africa between 2000 and 2015. *Nature*. 2015;526:207–211.  
[2] Sougoufara S. et al. Biting by *Anopheles funestus* in broad daylight after use of insecticidal nets. *Malar J.* 2014;13:125.  
[3] Sherrard-Smith E. et al. Mosquito feeding behavior and residual malaria transmission across Africa. *Proc Natl Acad Sci USA*. 2019;116:15086–15095.  
[4] Maire T., Wan Z., Lambrechts L., Hol F.J.H. BuzzWatch: uncovering multi-scale temporal patterns in mosquito behavior through continuous long-term monitoring. *eLife*. 2015;14:RP107916.

## Requirements

Students in the final phase of a Master’s program in Artificial Intelligence, Computer Science, Biomedical Engineering, Computational Biology, or a related field are invited to apply.

**Required skills:**

- Experience with Python programming
- Familiarity with machine learning and/or computer vision

Affinity with behavioral analysis, ecology, or biological data analysis is considered a strong advantage.

## Information

**Project duration:** 6 months  
**Location:** Radboud University Medical Center

The student will be embedded within the Medical Microbiology department, vector biology research group. Two GPU-equipped workstations are available for model development and experimentation.

For more information, please contact Felix Hol (felix.hol@radboudumc.nl).

