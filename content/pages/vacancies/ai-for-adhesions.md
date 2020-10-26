title: Artificial intelligence-assisted detection of adhesions on cine MRI
groups: ai-for-health, diag
closed: false
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
suppressing medication. A recently
developed imaging technique, cine MRI, can detect and localize
these adhesions. This type of imaging can be used to make treatment
decisions. Cine MRI is not widely used yet, because radiological
reading is time-consuming and expertise-dependent.

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
The student will have access to a database of more than 300 cine MRI
scans with labels extracted from radiology reports. A subset of these
scans is annotated with segmentations of relevant anatomy and adhesion 
locations.

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
