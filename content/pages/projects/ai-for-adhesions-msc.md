title: Artificial intelligence-assisted detection of adhesions on cine MRI
groups: ai-for-health
finished: false
type: student
picture: projects/ai4adhesion.jpg
template: project-single
people: Evgenia Martynova, Bram de Wilde, Henkjan Huisman
description: Development of an AI-assisted algorithm for automatic detection of adhesions on cine MRI

**Start date: 08-02-2021** <br>
**End date: 06-08-2021**

## Clinical problem 

This project aims to improve outcomes in the 30,000 patients per year in the Netherlands that develop chronic pain after abdominal surgery. This pain is often caused by adhesions, tough bands of tissue that form between structures and organs in the abdomen. Medical consumption in these patients is high, 70% is under treatment of a gastroenterologist and one in three is permanently taking pain suppressing medication. 

Currently, accurate diagnosis of adhesions requires invasive tools such as diagnostic laparoscopy owing to a lack of effective noninvasive tests. These methods are controversial because they can lead to the formation of new adhesions. This is especially undesirable for the patients whose complaints are not due to adhesions.  Non-invasively adhesions can be diagnosed with either ultrasound or cine-MRI. Cine-MRI is more powerful than ultrasound because it can detect adhesions in the entire abdomen, whilst ultrasound can detect only adhesions attached to the front abdominal wall due to its limited depth penetration. Cine-MRI is a type of MRI in which a set of consecutive images of the area of interest is acquired at a fixed time interval. The captured images can be merged into a video in which the movements of a certain tissue over time are visible. This imaging modality can be used to visualise the abdominal motion during respiration and by interpreting the recorded motion patterns, radiologists can diagnose adhesions. The gif below shows the data and annotations available in the project. Adhesions are annotated with bounding boxes by an experienced radiologist.  

![Adhesion example]({{ IMGURL }}/images/projects/ai4adhesion-example.gif)

Cine-MRI is used in the Radboudumc to make treatment decisions for patients with chronic abdominal pain. It helps doctors decide whether a patient should be treated conservatively with medication, or more progressively with surgery. Cine MRI is not widely used in other hospitals yet, because radiological reading is time-consuming and expertise-dependent.

Automatic algorithms for adhesion detection can reduce the learning curve for new readers and reduce variability among radiologists.  By helping radiologists interpret the images, the algorithm may reduce the number of false positives and negatives. False positives can result in unnecessary surgery, whereas false negatives can block surgery for patients who may actually be helped by it.

## Solution 

The objective of the project is to design a fully-automated CAD method for adhesion detection. As a starting point we take the semi-automated method proposed by David Randall in his PhD thesis [1]. The method exploits the discontinuity of the abdominal motion during respiration. In healthy subjects, abdominal contents slide smoothly against the surroundings of the abdominal cavity (abdominal wall, back muscles, etc.). Simultaneously, the abdominal wall exhibits a different, anteroposterior mode of motion. This process is called _visceral slide_. The scheme of this motion pattern is given below.

![Visceral slide scheme]({{ IMGURL }}/images/projects/ai4adhesion_vs_scheme.png)

Reduction in visceral slide is a clinical criterion of underlying adhesions. The key idea of the method is that it is possible to quantify the degree of visceral slide captured on a cine-MRI scan. To do this, the method needs a segmentation map of the abdominal cavity, to perform masked image registration. The output of masked image registration is a deformation field that describes the amount and direction of movement of the abdomen and its contents. The deformation field and abdominal cavity segmentation can be used to quantify visceral slide along the abdominal cavity contour.

One of the limitations of the method is the lack of segmentation automation. For the first cine-MRI frame a segmentation map has to be drawn by a medical specialist and then it is transferred to the subsequent frames. But manual correction is still required for each frame. Also, the method assumes the manual interpretation of the computed visceral slide by a radiologist. This method can be fully automated using deep learning-based segmentation of the abdominal cavity and an algorithm that predicts adhesions based on the low visceral slide value.

## Data 

The entire dataset available for the project contains 563 cine-MRI scans for 526 patients. Each scan is provided with a report containing a radiologist’s diagnosis based on the assessment of a cine-MRI scan. From the conclusions in the report, binary study-level annotations were extracted. This dataset was used to sample training and test sets balanced by patient adhesion status as well as a healthy control group to calculate visceral slide statistics. To acquire bounding box annotations of adhesions, two reader studies were organised separately for training and test sets. The resulting training set consists of 59 cine-MRI scans with 83 adhesions annotations and 59 negative scans. The held-out test set contains 38 scans with 56 adhesions annotations and 47 negative scans. Finally, 36 negative scans are sampled for the healthy control group.

## Method

We propose the first fully-automated multi-stage CAD method for adhesion detection on cine-MRI designed based on Randall's semi-automated method. The automation comprises deep learning-based segmentation of the abdominal cavity and the region growing algorithm designed to predict adhesions using the value of quantified visceral slide as an input. In addition, multiple normalization options that account for motion difference between patients and in different areas of abdominal cavity contour were carefully designed and integrated. This enables the same interpretation of a particular visceral slide value regardless of the amplitude of motion that occurs on a cine-MRI slice and the position at which it is observed. Also, two  different  approaches  to  visceral  slide  quantification  were  explored. In the first one, only the two most dissimilar frames of a cine-MRI scan are used to sharpen the differences between regions of lower and higher motion and the second method exploits all time points in a cine-MRI slice to obtain a full picture of motion.

The full scheme of the method is visualised below:

![Visceral slide scheme]({{ IMGURL }}/images/projects/ai4adhesion_method.png)

The main components of the methods are:

### Abdominal cavity segmentation

Implemented using nnU-Net [2], a state of the art model for medical image segmentation.

### Visceral slide computation

A predicted segmentation mask of abdominal cavity is used to obtain a masked deformation field and compute visceral slide along the abdominal cavity contour based on the difference of deformation inside and outside the abdominal cavity. We used ANTS toolkit [3] to obtain a deformation field. The first method to quantify visceral slide uses only two most dissimilar frames, that correspond to the opposite phases of resiratory cycle, to approximate visceral slide that occurs on a scan. The picture below visualises the algorithm:

![Visceral slide scheme]({{ IMGURL }}/images/projects/ai4adhesion_vs_pair.png)

Another method we explored extracts cumulative visceral slide from a cine-MRI scan by adding visceral slide maps computed between each subsequent pair of frames with a specially designed summation procedure. We assumed that the latter method captures the complete motion recorded in a cine-MRI scan more accurately.

### Visceral slide normalisation 



### Adhesion detection with region growing algorithm 

## Results

The algorithm is published on the Grand Challenge platform. 

<a href="https://grand-challenge.org/algorithms/visceral-slide-on-abdominal-cine-mri/" class="btn btn-primary btn-lg my-3">Try out the algorithm</a>

The code for this project can be found in this [GitHub repository](https://github.com/DIAGNijmegen/abdomenmrus-cinemri-cavity-segmentation).

TODO: note that private DIAG code is used in these repo. Can registration repo be made public?

[1] Randall, David. "Towards a non-invasive diagnostic aid for abdominal adhesions using dynamic MRI and image processing." PhD diss., University of Sheffield, 2017.

[2] Isensee, F., Jaeger, P.F., Kohl, S.A., Petersen, J. and Maier-Hein, K.H., 2021. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature Methods, 18(2), pp.203-211.

[3]Avants, B.B., Tustison, N.J., Song, G. and Gee, J.C., 2009. Ants: Open-source tools for normalization and neuroanatomy. HeanetIe, 10, pp.1-11.
