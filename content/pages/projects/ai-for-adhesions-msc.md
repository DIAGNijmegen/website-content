title: Artificial intelligence-assisted detection of adhesions on cine MRI
groups: ai-for-health
finished: false
type: student
picture: projects/ai4adhesion.jpg
template: project-single
people: Evgenia Martynova, Bram de Wilde, Henkjan Huisman
description: Development of an AI-assisted algorithm for automatic detection of adhesions on cine MRI

**Start date: 25-01-2021** <br>
**End date: 26-07-2021**

## Clinical problem 

This project aims to improve outcomes in the
30,000 patients per year in the Netherlands that develop chronic pain
after abdominal surgery. This pain is often caused by adhesions,
tough bands of tissue that form between structures and organs in
the abdomen. Medical consumption in these patients is high, 70%
is under treatment of a gastroenterologist and one in three is
permanently taking pain suppressing medication. Adhesions can be
detected both invasively and non-invasively. Invasive diagnosis
(i.e. surgery) is controversial, because it can cause the formation
of new adhesions. Non-invasively, adhesions are detected with either
ultrasound or cine MRI. Ultrasound works well, but can only detect
adhesions attached to the front abdominal wall. Cine MRI, on the
other hand, can detect adhesions in the entire abdomen.  This type
of imaging is used in the Radboudumc to make treatment decisions
for patients with chronic abdominal pain. It helps doctors decide
whether a patient should be treated conservatively with medication,
or more progressively with surgery. Cine MRI is not widely used in
other hospitals yet, because radiological reading is time-consuming
and expertise-dependent.

Automatic detection algorithms for adhesion detection can reduce
the learning curve for new readers and reduce variability among
radiologists.  By helping radiologists interpret the images, the
algorithm may reduce the number of false positives and negatives. False
positives can result in unnecessary surgery, whereas false negatives
can block surgery for patients who may actually be helped by it.

The gif below gives an impression of the type of data used in this
project.

![Adhesion example]({{ IMGURL }}/images/projects/ai4adhesion-example.gif)

## Solution 

We want to develop an automated system for adhesion
detection, using deep learning segmentation and classification. We take
an existing, semi-automated method as a starting point.  This existing
method need a segmentation map of the abdominal cavity, to perform a
masked image registration. This allows quantification of the amount
and direction of movement of the abdomen and its contents.  The local
difference in movement between the abdominal wall and its contents,
called visceral slide, is indicative for adhesions. Little or no
visceral slide indicates that an adhesion is present. This method
can be fully automated using deep learning-based segmentation of the
abdominal cavity and deep learning-based classification or detection
on the registration results.

## Data 

We have access to 60 cine MRI studies
with binary labels (adhesions or no adhesions) extracted from radiology
reports and abdominal cavity segmentations. In 10 of these studies,
adhesions are annotated with bounding boxes. Soon, this database
will be extended to more than 500 cine MRI studies with labels from
another hospital.

## Method


{DESCRIBE THE APPROACH USED TO SOLVE THE CLINICAL PROBLEM}

## Results

The algorithm is published on the Grand Challenge platform. 

<a href="https://grand-challenge.org/algorithms/visceral-slide-on-abdominal-cine-mri/" class="btn btn-primary btn-lg my-3">Try out the algorithm</a>

The code for this project can be found in this [GitHub repository](https://github.com/DIAGNijmegen/abdomenmrus-cinemri-cavity-segmentation).

TODO: note that private DIAG code is used in these repo. Can registration repo be made public?

