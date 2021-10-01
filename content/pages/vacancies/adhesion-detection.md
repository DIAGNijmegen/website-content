title: Artificial intelligence-assisted detection of adhesions on cine-MRI
groups: ai-for-health
closed: true 
type: student 
picture: vacancies/MD_drug_repurposing.png
template: vacancy-single
people: Bram de Wilde
description: Develop a method to detect adhesions on cine-MRI

**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical Problem 
This project aims to improve outcomes in the 30,000 patients per year in the Netherlands alone that develop chronic pain after abdominal surgery.[1] This pain is often caused by adhesions, tough bands of tissue that stick between structures and organs in the abdomen. Medical consumption in these patients is high, 70% is under treatment of a gastroenterologist and one in three is permanently taking pain suppressing medication.[2] Adhesions can be detected both invasively and non-invasively. Invasive diagnosis (i.e. surgery) is controversial, because it can cause the formation of new adhesions. Non-invasively, adhesions are detected with either ultrasound or cine-MRI. Non-invasive imaging using videos can depict where tissues are connected by adhesions. Ultrasound can only detect adhesions near the abdominal wall. Cine-MRI, on the other hand, can detect adhesions in the entire abdomen.[3] This type of special video MRI is used in the Radboudumc to make treatment decisions for patients with chronic abdominal pain. It helps doctors decide whether a patient should be treated conservatively with medication, or more progressively with surgery. Cine-MRI is not widely used in other hospitals yet, because radiological reading is time-consuming and expertise-dependent.
 
Automatic detection algorithms for adhesion detection can reduce the learning curve for new readers and reduce variability among radiologists. In addition, by helping radiologists interpret the images, the algorithm may reduce the number of false positives and negatives. False positives can result in unnecessary surgery, whereas false negatives can block surgery for patients who may actually be helped by it.
 
## Solution 
The goal of this project is to explore and develop a deep learning algorithm for automatic detection of abdominal adhesions on cine-MRI. We are currently working on an approach based on temporal image registration and deep learning segmentation.[4][5] Additionally, we are actively exploring recurrent neural networks and temporal deep learning algorithms.[6] Other possible research directions are: using data more effectively through self-supervised techniques for video ([7]) or improving the interpretability of our methods for the clinic with e.g. saliency map models.[8] There are many possible approaches and the student is encouraged to come up with original solutions to this novel problem in medical imaging.

## Data 
We have a dataset of more than 500 cine-MRI studies with binary labels (adhesions or no adhesions), extracted from radiology reports. Each study has on average 6 sagittal cine-MRI slices (2D + time), giving a total of more than 3000 cine-MRI slices. 200 cine-MRI slices have detailed bounding box annotations, provided by an expert radiologist. If the student's approach warrants it, we also have access to thousands of unlabeled regular abdominal MRI studies for transfer learning of anatomic information.

## Results
The algorithm will be made publically available as a Docker container on https://grand-challenge.org/.

## Embedding 
The student will be supervised by a research member of the Diagnostic Image Analysis Group whose research is dedicated to adhesion detection with deep learning techniques. We have a strong collaboration with both clinical and radiological experts in the field of abdominal adhesions. The student will have access to a large GPU computation cluster.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics in the final stages of their Master education. 
- You should be proficient in python programming and have a theoretical understanding of deep learning architectures. 
- Basic biological / biomedical knowledge is preferred.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- More information can be obtained from Bram de Wilde (mailto: bram.dewilde@radboudumc.nl)
