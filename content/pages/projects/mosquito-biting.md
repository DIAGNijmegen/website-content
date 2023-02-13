title: Deep behavioral phenotyping of mosquito biting behavior
groups: ai-for-health
finished: false
type: student
picture: vacancies/mosquito-biting.png
template: project-single
people: Felix Hol
description: Development of a deep learning algorithm for phenotyping of mosquito biting behavior in video

## Reimbursement
This is an AI for Health MSc project. Students are eligible to receive a monthly reimbursement of €500,- for a period of six months. For more information please read the [requirements](https://www.ai-for-health.nl/requirements).

## Clinical Problem
Mosquitoes transmit an array of pathogens, making them one of the world’s most deadly animals. A mosquito's thirst for blood is central to understanding mosquito-borne pathogen transmission. Yet despite the strong relevance for pathogen transmission, we lack a thorough understanding of the internal and external drivers of blood feeding behavior. It is for instance unclear how pathogen infections affect biting behavior, nor is it known how contact-dependent sensing of the composition of the skin shapes biting dynamics. To explore these questions, we recently developed the  biteOscope - an open-source platform that attracts mosquitoes to a host mimic which they bite to obtain an artificial blood meal. The host mimic is transparent, allowing high-resolution imaging of the feeding mosquito. Coupling this imaging platform to a computational pipeline enables the automated extraction of detailed behavioral characteristics allowing the dissection of the micro-behaviors that together lead to the successful completion of a blood meal, and create the possibility for pathogen transmission.

Using the biteOscope we have obtained a large dataset of Aedes aegypti mosquitoes (the principle vector of dengue virus) biting the transparent host mimic under various experimental conditions. By applying a range of deep learning tools to this video dataset we aim to investigate how pathogen infections change the biting behavior of mosquitoes. Accurate estimates of changes in e.g. the mosquito's attraction to humans, or its biting frequency will allow us to predict how pathogen-induced behavioral changes affect the pathogen's transmission in the real world.  

References

1. Hol, Felix JH, Louis Lambrechts, and Manu Prakash. "BiteOscope, an open platform to study mosquito biting behavior." Elife 9 (2020): e56829.

2. Lauer, Jessy, et al. "Multi-animal pose estimation, identification and tracking with DeepLabCut." Nature Methods 19.4 (2022): 496-504.

3. Luxem, Kevin, et al. "Identifying behavioral structure from deep variational embeddings of animal motion." BioRxiv (2022): 2020-05.

4. Berman, Gordon J., et al. "Mapping the stereotyped behaviour of freely moving fruit flies." Journal of The Royal Society Interface 11.99 (2014): 20140672.

## Solution
Advances in computer vision are currently pushing the observation of animal behavioral into the realm of big data: An animal's interactions with its environment can be recorded at high spatiotemporal resolution, and machine learning tools are enabling detailed analysis from video data. A significant challenge currently lies in the efficient, automated, and accurate extraction of meaningful behavioral statistics from video data.  

In this project, we will use deep learning for the tracking and pose estimation of freely behaving mosquitoes. We have established a convolutional neural network (trained using the DeepLabCut framework) to track the movement of 34 locations on the mosquito body (e.g. head, mouthparts, all leg joints) of multiple animals present in the same image. Together, these locations can be used to describe the pose of a mosquito's body (i.e. the relative position of all body parts). The behavioral dynamics of the mosquito can then be reduced to multiple time series of body parts. We will now build upon this and develop unsupervised machine learning methods based on dimension reduction (e.g. UMAP  or variational autoencoders) to embed the high-dimensional data obtained using body-part tracking in two dimensions. This will result in 2D 'maps' in which specific areas correspond to behaviors (e.g. walking, biting, drinking). Behaving mosquitoes navigate this landscape, and their behavioral trajectories can be represented as ethograms. We will develop statistical tools to compare key behaviors (e.g. biting frequency) among cohorts. Building ethograms furthermore allows the identification of distinct behavioral motifs, and we will explore data-driven Markov models and other numerical methods to better understand the structure, order, and transitions between behavioral subroutines.

## Data
We currently have a large database of videos of mosquitoes exhibiting blood feeding behavior obtained using the biteOscope. A training set of several hundred mosquitoes with labelled body parts has been established. This data set can be used for CNN training and subsequently inference on the entire video database to establish the body part coordinate data set to be used for behavioral clustering. 


