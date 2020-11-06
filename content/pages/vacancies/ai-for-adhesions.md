title: Artificial intelligence-assisted detection of adhesions on cine MRI
groups: ai-for-health, diag
closed: true
type: student
picture: projects/ai4adhesion.jpg
template: vacancy-single
people: Bram de Wilde, Henkjan Huisman
description: Development of an AI-assisted algorithm for automatic detection of adhesions on cine MRI

**This is an AI for Health MSc project. Students are elgible to receive 
a monthly reimbursement of €500,- for a period of six months. For more 
information please read the 
[requirements](https://www.ai-for-health.nl/requirements/).**

## Clinical problem
This project aims to improve outcomes in the 30,000 patients per
year in the Netherlands that develop chronic pain after abdominal
surgery. This pain is often caused by adhesions, tough bands of tissue
that form between structures and organs in the abdomen. Medical
consumption in these patients is high, 70% is under treatment of a
gastroenterologist and one in three is permanently taking pain 
suppressing medication. Adhesions can be detected both invasively and
non-invasively. Invasive diagnosis is controversial, because it can 
cause the formation of new adhesions. Non-invasively, adhesions are
detected with either ultrasound or cine MRI. Ultrasound works well, but
can only detect adhesions attached to the front abdominal wall. Cine MRI,
on the other hand, can detect adhesions in the entire abdomen. 
This type of imaging is used in the Radboudumc to make treatment
decisions for patients with chronic abdominal pain. It helps doctors
decide whether a patient should be treated conservatively with medication,
or more progressively with surgery. Cine MRI is not 
widely used in other hospitals yet, because radiological reading is 
time-consuming and expertise-dependent.

Automatic detection algorithms for adhesion detection can reduce the
learning curve for new readers and reduce variability among radiologists. 
By helping
radiologists interpret the images, the algorithm may reduce the number
of false positives and negatives. False positives can result in 
unnecessary surgery, whereas false negatives can block surgery for
patients who may actually be helped by it.

The gif below gives an impression of the type of data the student will
be working with.

![Adhesion example]({{ IMGURL }}/images/projects/ai4adhesion-example.gif)

## Solution
We want to develop an automated system for adhesion detection, using
deep learning segmentation and classification. We take existing, 
semi-automated, methods as a starting point.
Existing methods need a segmentation map of the abdominal cavity, to 
perform a masked image registration. This allows quantification of the amount 
and direction of movement of the abdomen and its contents. The local
difference in movement between the abdominal wall and its contents, 
called visceral slide, is indicative for adhesions. Little or no visceral slide indicates that
an adhesion is present. This method can be fully automated using 
deep learning-based segmentation of the abdominal cavity and deep
learning-based classification or detection on the registration
results. This task is new and unexplored territory in AI research and
leaves a lot of room for creative and challenging approaches!

## Data
The student will have immediate access to 60 cine MRI studies with
binary labels (adhesions or no adhesions) extracted from radiology
reports. 10 of these studies are annotated with bounding boxes. Soon,
this database will be extended to more than 300 cine MRI studies with
labels from another hospital.

## Approach
Students will be supervised by a [DIAG](https://www.diagnijmegen.nl/) 
research member whose research is dedicated to adhesion detection 
with machine learning techniques. Depending on the project progression, 
they will be guided to set up an automatic CNN-based system for 
detecting adhesions to the abdominal wall, in the lesser pelvis and 
between bowel loops. The final deliverable will be a publicly available 
algorithm on the platform 
[Grand Challenge](https://grand-challenge.org/algorithms/). Students get 
access to the high-performance deep learning cluster of DIAG, named 
[SOL](https://rtc.diagnijmegen.nl/software/sol/), for running machine 
learning experiments.

## Requirements
- Student with a major in data science, computer science, or artificial 
    intelligence in the final stage of master level studies
- Interest in (medical) image analysis and machine learning
- Affinity with programming in Python and with deep learning packages 
    (e.g. PyTorch) is required
 
## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- For more information, please contact [member/bram-de-wilde]
