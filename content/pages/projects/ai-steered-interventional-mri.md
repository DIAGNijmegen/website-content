title: AI steered interventional MRI
groups: diag, ai-for-health
finished: false
type: student
picture: projects/mri_intervention.jpg
template: project-single
people: Tristan de Boer, Henkjan Huisman, Patrick Brand, Elena Marchiori
description: Develop Artificial Intelligence (AI) to track tumor targets in interventional MRI.

## Clinical problem
The field of minimally invasive image guided interventions (MIIGI) is emerging. MIIGI, for example using an MRI, allows minimally invasive treatment of cancer and other diseases. Currently, connecting MIIGI to real-time Artificial Intelligence is unexplored. In this research, we assess the feasibility of deep learning based tracking for real-time MIIGI, by developing a deep learning based pipeline for automated guidewire tracking.

Using MRI, we can accurately reveal a tumor within an organ or at difficult to reach locations. Using real-time MRI visualization, special needles can be inserted such that the tip of the needle is within the tumor, which then can be used for treatment. One such treatment is cryoablation, where the tumor tip is frozen. Using this treatment the tissue surrounding the tip is frozen and tissue cells in that region are killed and subsequently broken down by the body. Cryoablation has several advantages, as the minimally invasive procedure is less disruptive for surrounding tissues and thus allows for faster recovery of the patient. Furthermore, the real-time feedback on the effect of intervention ensures excellent coverage of the tumor region, ensuring that the entire tumor has been destroyed.

The accuracy of MIIGI is unfortunately limited because during needle intervention, the body deforms and structures disappear from the imaging display. The MRI needs to be manually adjusted to acquire images in a new imaging plane that shows the structure in relation to the needle. This repeated MRI adjustment takes considerable time and leads to suboptimal needle placement.

## Solution
The goal of this project is to develop Artificial Intelligence (AI) to improve MRI guided interventions by automatically tracking tumors and automatically steering MRI acquisitions, using an MRI scanner that can be digitally steered. Deep learning techniques can be used such that it can track an object from a series of MRI images. The output can be used to steer the MRI, which can be used for improved visualization, making interventions more accurate while reducing the duration of an intervention.

## Tasks
In this pilot project, the focus is on simulated interventional MRI. The tasks are as follows:

- Develop an MRI simulation module. Synthetic MRI image series should show moving tumor targets with an adjustable motion to simulate varying levels of difficulty.
- Develop an AI tracking module that predicts the tumor target location from a series of MRI images.
- Develop a demonstrator that compares conventional versus AI-driven interventional MRI 

## Methods
We trained a network using previously acquired images as the method is not directly online trainable. Before we could test the implementation using a real MRI, we had to train the network with annotated data. We semi-automatically generated bounding-box annotations of guidewires, which were then used to train a neural network for object detection.

Using the trained network and an API, we created a deep learning based pipeline for automated guidewire tracking and steering an MRI scanner. The pipeline receives data from the MRI detects and tracks the guidewire tip in an obtained coronal plane image stream in real-time, and autonomously controls the MRI scanner to update the spatial position of an imaging scan plane to keep track of the moving guidewire.

Finally, we evaluated the method by measuring the actual distance between the actual and the predicted position.

![Pipeline]({{ IMGURL }}/images/projects/interventional_mri_pipeline.png)

## Results
We first trained a network on previously acquired images, which then is inserted into a pipline shown in the figure above. We then conducted a slice repositioning experiment on an phantom of an anthropomorphic blood vessel. We can see the movement in the video below. In this video, we see guidewire markers, which then are detected and indicated with green bounding boxes. Using these predictions, we move the sagittal plane, as indicated with the red line. The sagittal plane is creating artefacts. Using these artefacts, we can see that the sagittal plane is following the red line. 

![Detection video]({{ IMGURL }}/images/projects/interventional_mri_video.gif)

We showed tracking of a guidewire displacement of 140mm in real-time (121ms) within, on average, a 7mm margin (σ = 4). 

A setup of the system can be seen below, where we can see the physician moving the guidewire in combination with the laptop running the pipeline.

![Hardware setup]({{ IMGURL }}/images/projects/interventional_mri_setup.png)

## Conclusion
Deep learning assisted image guided interventions is feasible, though not yet ready for clinical practice. We show a mean displacement error of 7 mm (σ = 4). 

Further research on model robustness and uncertainty is therefore encouraged in order to push deep learning assisted image guided interventions towards clinical practice. Incorporating spatio-temporal information may help solve the lagging and allow 3D movement tracking.

We have submitted these conclusions as short paper to [MIDL](https://midl.io). The paper is currently under review.
