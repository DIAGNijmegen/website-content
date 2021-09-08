title: Detecting and characterizing vertebral fractures in CT scans
groups: ai-for-health
finished: false
type: student
picture: vacancies/msc-vertebral-fractures.jpg
template: project-single
people: Michel Botros, Nikolas Lessmann, Stan Buckens, Matthieu Rutten, Bram van Ginneken
description: Developing image analysis algorithms that automatically detect osteoporotic vertebral fractures.

**Start date: 01-02-2021** <br>
**End date: 31-07-2021**

## Clinical problem

Osteoporosis is a silent age-related disease that slowly decreases the stability of the bones, which eventually leads to bones starting to fracture and collapse. Vertebral fractures are one of the most common skeletal fractures and are mostly caused by osteoporosis, making them especially useful for diagnosing osteoporosis. Osteoporotic vertebral fractures are associated with an increased mortality, morbidity, a decrease in quality of life and are strong predictors of future osteoporotic fractures. Many guidelines on management of osteoporosis recommendpharmacological intervention when vertebral fractures are present. However, they remain largely underdiagnosed, due to frequently occurring asymptomatic and often being not reported by clinicians when present in computed tomography (CT) scans. Every year, millions of CT scans of the thorax and abdomen are made worldwide, for reasons other than osteoporosis and vertebral fractures, providing the opportunity to detect vertebral fractures. In this project we explored the use of AI systems to assist clinicians with detection and assessment of vertebral fractures based on CT images, thereby enabling preventive treatment and improving the outcome for osteoporosis patients.


## Solutions
During this project two algorithms were developed: 

### (1) Genant Classification 
The proposed method for performing automated VFA according to Genant’s method consists of two stages. In the first stage every visible vertebra in the input CT image is segmented and labeled. In the second stage each individual (relevant) vertebra is assessed according to Genant’s method by a 3D CNN.
<p align="center">
  <img src="https://user-images.githubusercontent.com/4972463/132573897-6a520a75-f130-49a1-bd9d-b20c96d458ae.png" width="750" height="475">
</p>

#### Results
The performance of fracture assessment by three different networks is listed below. Out of three networks, the CBR-5 proved to be best equipped to learn the task of VFA, performing slightly better than the deeper networks. CBR-5 correctly graded 89% <img src="https://render.githubusercontent.com/render/math?math=\left( \frac{103}{116} \right)"> of the vertebrae in the test set with <img src="https://render.githubusercontent.com/render/math?math=\kappa=0.92">.

<p align="center">
  <img src="https://user-images.githubusercontent.com/4972463/132573681-c70a4274-1e4f-43d1-9f7a-652c5a4de511.png" width="750" height="405">
</p>
 
**Examples of automated Genant Classification**
<p align="center">
  <img src="https://user-images.githubusercontent.com/4972463/132577646-a74154ec-6d29-41d4-becc-3395c812ec02.png" width="750" height="500">
</p>


### (2) Vertebral Abnormality Scoring
To detect abnormalities in the vertebral body we trained a deep learning model to predict the shape of a healthy vertebra, given the shape of neighboring vertebrae. Afterwards the original shape of the vertebra is compared with the generated shape and their differences are measured to assess whether it is an abnormal vertebra.

<p align="center">
  <img src="https://user-images.githubusercontent.com/4972463/132570535-2518ecd0-556b-40e2-bcf2-515b2fa1c781.png" width="750" height="500">
</p>

#### Results
Correspondence between the abnormality score and the Genant grades for is shown below.  To obtain a grade from the score we fitted a logistic regression classifier on the training set. The resulting thresholds are shown as the dashed lines. Grading was then performed by using the threshold values. 84% <img src="https://render.githubusercontent.com/render/math?math=\left( \frac{97}{116} \right)"> of the vertebrae were correctly graded using the score, with <img src="https://render.githubusercontent.com/render/math?math=\kappa=0.85">.

<p align="center">
  <img src="https://user-images.githubusercontent.com/4972463/132580706-0b32f2fb-ed8e-45d8-872c-3d5f0cc97fe9.png" width="750" height="431">
</p>

**Examples of our proposed scoring system**
<!-- TO-DO: Add a colorbar and add maybe one examples with more fractures (one of the examples from the Genant classification, to show the difference) -->
In the examples below the color indicates the abnormality score computed by the algorithm. The black arrow indicates disagreement between the algorithm and radiogists. This case was graded as a mild fracture by radiologists.

<p align="center">
  <img src="https://user-images.githubusercontent.com/4972463/132582040-4301cdd1-4bfd-4604-9e50-12743c314fdf.png" width="750" height="800">
</p>


## Conclusion
Two algorithms were developed and both were made available on Grand-challenge!

<a href="https://grand-challenge.org/algorithms/vertebral-fracture-assessment/" class="btn btn-primary btn-lg my-3">Try out Genant Classification</a>

<a href="https://grand-challenge.org/algorithms/vertebral-abnormality-scoring/" class="btn btn-primary btn-lg my-3">Try out Vertebral Abnormality Scoring</a>

Both need CT images as input and vertebral body segmentations, which can be obtained here:

<a href="https://grand-challenge.org/algorithms/vertebral-body-segmentation/" class="btn btn-primary btn-lg my-3">Get Vertebral Body Segmentation</a>

The code for this project can be found in this [GitHub repository](https://github.com/DIAGNijmegen/msk-compression-fracture-detection).
