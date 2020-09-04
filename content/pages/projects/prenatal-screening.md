title: Automated prenatal ultrasound screening
groups: ai-for-health 
finished: false
type: student
picture: vacancies/prenatal-screening.jpg
template: project-single
people: Martijn Schilpzand, Thomas van den Heuvel, Jeroen van Dillen, Chris de Korte, Bram van Ginneken, Tom Heskes
description: Project aimed at development of deep learning algorithms for automated detection of twin pregnancies and placenta localization.

**Start date: 03-02-2020** <br>
**End date: 03-08-2020**

## Clinical problem
Ultrasound imaging is widely used for prenatal screening. Unfortunately, prenatal ultrasound imaging is barely performed in resource-limited settings. This is mainly caused by a severe shortage of well-trained personnel that is able to acquire and interpret ultrasound images. In this project, we are therefore combining Artificial Intelligence with a predefined ultrasound acquisition protocol. This acquisition protocol can be taught to a midwife within two hours. 

With the acquisition protocol, data was already acquired from 390 pregnant women in Ethiopia. This data will be used to develop a new deep learning algorithms that automatically determines the location of the placenta. When the location of the placenta is known, it is possible to detect women that are at risk of placenta previa (which is a placenta that partly or completely covers the birth channel). Women with placenta previa have a two-fold increased risk of postpartum hemorrhage and even a ten-fold increased risk of antepartum hemorrhage.

## Solution
Combining this protocol with deep learning algorithms has the potential to obviate the need of a trained sonographer in resource-limited settings. 

## Research question and tasks
Development of a deep learning algorithm that automatically determines the location of the placenta using a predefined ultrasound acquisition protocol.

## Innovation
When the algorithm has sufficient sensitivity and accuracy, and are able to run on a smartphone, it will be integrated in the current prototype which we are planning to evaluate in resource-limited settings.

## Methods
The placenta localisation algorithm was split in two parts
- Placenta segmentation 
- Placenta classification

With the acquisition protocol approximately 600 2D ultrasound images are acquired per case. The placenta segmentation algorithm consists of a deep learning model (U-Net) which is trained to segment placenta on this 2D ultrasound data. 
The resulting segmentation data is used to classify the placenta of a case as either normal or low-lying. The low-lying class includes placenta previa as well as cases where the placenta is located within 2 centimeters of the birth channel. 
The classifier uses a analytical approach which is based on the center of mass of the placenta. 

## Results
The segmentation model achieves a median test Dice of 0.838. To give an indication of the performance the figure below contains an 3D visualisation for a case with a median Dice of 0.855. 
Both images represent approximately 600 ultrasound images from the same case that are acquired with the acquisition protocol. They contain six blocks since the acquisition protocol consists of six sweeps. The yellow surfaces in the top image represent placenta annotations made by an expert. The expert annotated one if every five images which is why there is space between the surfaces. The red surfaces in the bottom image represent the placenta segmentation made by the model. 

![Segmentation Example]({{ IMGURL }}/images/projects/prenatal_screening_segmentation_example.png) 

The classifier achieves a AUC of 0.90. Selecting the threshold to attain the highest accuracy (86%) results in a sensitivity of 85% and a specificity of 86%.

## Concusion
The placenta locatisation algorithm shows promising results. 
Combined with the acquisition protocol it could help to identify at-risk pregnancies in resource-limited settings and refer these cases to a hospital for further examination by a trained sonographer. Ideally, this could ensure that the low number of ultrasound examinations in resource-limited settings would be used for cases that have a high chance of being at-risk.
