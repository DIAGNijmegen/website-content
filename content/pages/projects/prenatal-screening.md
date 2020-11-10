title: Automated prenatal ultrasound screening
groups: ai-for-health 
finished: true
type: student
picture: vacancies/prenatal-screening.jpg
template: project-single
people: Martijn Schilpzand, Thomas van den Heuvel, Jeroen van Dillen, Chris de Korte, Bram van Ginneken, Tom Heskes
description: Project aimed at development of deep learning algorithms for automated detection of twin pregnancies and placenta localization.

**Start date: 03-02-2020** <br>
**End date: 03-08-2020**

## Clinical problem
Ultrasound imaging is widely used for prenatal screening. Unfortunately, it is barely performed in resource-limited settings. This is mainly caused by a severe shortage of well-trained personnel that is able to acquire and interpret ultrasound images. In this project, we are therefore combining Artificial Intelligence with a predefined ultrasound acquisition protocol. This acquisition protocol can be taught to a midwife within two hours. 

With the predefined acquisition protocol, data was acquired from 390 pregnant women in Ethiopia. This data was to develop a new deep learning algorithms that automatically determines the location of the placenta. When the location of the placenta is known, it is possible to detect women that are at risk of placenta previa (which is a placenta that partly or completely covers the birth channel). Women with placenta previa have a two-fold increased risk of postpartum hemorrhage and even a ten-fold increased risk of antepartum hemorrhage.

## Solution
Combining the predefined acquisition protocol with deep learning algorithms has the potential to obviate the need of a trained sonographer in resource-limited settings. 

## Research question and tasks
Development of a deep learning algorithm that automatically determines the location of the placenta using a predefined ultrasound acquisition protocol.

## Innovation
When the algorithm has sufficient sensitivity and accuracy, and are able to run on a smartphone, it will be integrated in the current prototype which we are planning to evaluate in resource-limited settings.

## Methods
The placenta localization algorithm was split in two parts:

- Placenta segmentation 
- Placenta classification

The acquisition protocol consists of six predefined sweeps and results in approximately 600 2D ultrasound images per pregnant woman. A deep learning model (U-Net) is trained to segment the placenta in these 2D ultrasound images.
The resulting segmentation data is used to classify the placenta of a pregnant woman as either normal or low-lying. The low-lying class includes placenta previa as well as cases where the placenta is located within a range of 2 centimeters from the birth channel. 
The classifier uses a analytical approach which is based on the center of mass of the placenta. 

## Results
The segmentation model achieves a median test Dice of 0.838. To give an indication of the performance the figure below contains an 3D visualization for a case with a median Dice of 0.855. In the figure the segmentation performance of the model is compared to the placenta annotations made by an expert. The six background blocks represent the six sweeps of the acquisition protocol. 
The yellow surfaces in the top image represent placenta annotations made by an expert. The expert annotated one if every five images which is why there is space between the surfaces. The red surfaces in the bottom image represent the placenta segmentation made by the model. 

![Segmentation example]({{ IMGURL }}/images/projects/prenatal_screening_segmentation_example.png) 

The placenta classifier achieves a AUC of 0.90. Selecting the threshold to attain the highest accuracy (86%) results in a sensitivity of 85% and a specificity of 86%.

## Conclusion
The placenta locatization algorithm shows promising results. 
Combined with the predefined acquisition protocol it could help to identify at-risk pregnancies in resource-limited settings and refer these cases to a hospital for further examination by a trained sonographer. This gives pregnant women the possibility to travel to a health care facility before delivery, so they can receive care when required. 


The code for this project can be found in this [GitHub repository](https://github.com/DIAGNijmegen/babychecker-placenta-localization).

The final report for this project can be found [here](https://drive.google.com/file/d/1-K95brXPDVxYkkO7uDxbrBUNN64motRL/view?usp=sharing).
