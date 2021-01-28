title: Fetal heart rate detection in twin pregnancies
groups: ai-for-health
closed: false
type: student
picture: vacancies/fhr_twin_pregnancies.png
template: vacancy-single
people: Rik Vullings, Joris van Drongelen, Wieteke Heidema, Tom Heskes
description: Development of a model to determine the individual fetal heart rates in twin pregnancies.


## Clinical Problem
The tendency of parents in Western countries to postpone parenthood is associated with increased needs of assisted reproductive technology (e.g. IVF) and resulting increased incidence rate of twin pregnancies.  Twin pregnancies have an elevated risk of complications that require monitoring of the fetal health during pregnancy and labor. Such pregnancy monitoring is typically done through the cardiotocogram (CTG), the simultaneous registration of fetal heart rate (FHR) and uterine activity. Before and during labor, the FHR is obtained by means of Doppler ultrasound technology. Here, a beam of ultrasound is transmitted into the body from the maternal abdominal surface. The Doppler shift in the ultrasound that is reflected from the heart rate is subsequently used to calculate the FHR. For twin pregnancies, this means that two ultrasound transducers are required. When the mother moves, or when the fetuses move, the ultrasound beams of these transducers might no longer be directed towards the fetal hearts, leading to loss of signal or worse, mix-up of the two fetal hearts. In the latter case, the two FHR patterns get confused leading to complicated, if not impossible, assessment of the fetal condition and consequently potentially dangerous situations.

## Solution
In this project, we build on existing technology for non-invasive, multi-channel, electrophysiological monitoring of the FHR in singleton pregnancies. For twin pregnancies, further signal processing and/or machine learning needs to be developed to separate the data from both twins and determine their individual FHRs.

The aim is to develop machine learning methods that exploit the multi-channel aspect of the electrophysiological recordings to separate the signals from both fetal hearts in twin pregnancies and determine the individual FHR of both fetuses.

Standard source separation methods like principal or independent component analysis are insufficient to separate the signals due the dimensionality of the recorded data, with only 4-6 channels of data. Instead, we will develop advanced source separation methods such as combinations of model-driven and data-driven machine learning to separate the signals. These methods will exploit differences in the morphology of the fetal ECG signals for both fetuses across the electrodes.

## Data
We have access to >1200 cases of simulated twin pregnancy recordings, by combining two recordings from singleton pregnancies. These recordings have ground truth data obtained from the existing method for processing singleton pregnancy data. In addition, 11 real twin pregnancy recordings exist (without ground truth data) and during the project we expect to collect another 10-20 recordings from twin pregnancies with Doppler ultrasound as ground truth reference.

## Approach
Students will be supervised by a research member whose research is dedicated to biomedical signal processing and machine learning, with specialization in pregnancy as application domain. We furthermore have a group of experts on machine learning and pregnancy for additional supervision. The student will get familiarized with the electrophysiological data and an approach for the separation of twin signals will be chosen together with the supervision team. Depending on the chosen approach a combination of convolutional neural networks (CNNs) and/or feed-forward neural networks can be used with or without a combination with more conventional signal processing algorithms. The goal is to create a novel method for monitoring twin pregnancies, based on electrophysiology, validated against a large dataset of simulated data and a small set of real-life twin measurements. The final deliverable might be implemented on existing monitoring technology and results published in an academic journal.

## Requirements
- Students with a major in data science, computer science, or artificial intelligence in the final stage of master level studies are invited to apply.
- Interest in (medical) signal analysis and machine learning.
- Affinity with programming in Python and with deep learning packages (e.g. PyTorch or Keras) is required.

## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- For more information, please contact [Rik Vullings](mailto:R.Vullings@tue.nl) 
