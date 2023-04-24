title: Automated AAA detection on CT scans
groups: ai-for-health, diag
finished: true
type: student
picture: vacancies/aaa21.jpg
template: project-single
people: Anwai Archit, Bram van Ginneken, Silvan Quax
description: We want to develop a robust deep learning algorithm for automated detection of abdominal aorta aneurysms in CT scans.

**Start date: 01-02-2022** <br>
**End date: 31-07-2022**

## Clinical problem
An abdominal aortic aneurysm (AAA) is a local enlargement of the abdominal aorta. AAAs cause 1 to 3% of all deaths among men aged 65–85 years in the Western world. People with an AAA usually have no symptoms until the catastrophic event of rupture. The mortality rate for patients with a ruptured abdominal aortic aneurysm is around 75% and about half of deaths attributed to rupture occur before the patient reaches the hospital for acute surgery. Large aneurysms can be repaired by open surgery or placing a stent in an endovascular procedure.

The size of the aorta can be accurately measured on a CT scan. Hospitals make thousands of CT scans of the abdomen every year. Automated assessment of the aorta and measurement of abnormal enlargement would be a useful tool for routine clinical practice, but such a system is not yet available. 

## Solution
In this project we will develop and validate a deep learning algorithm for segmentation and automated measurement of the abdominal aorta.

## Approach
Our group already has developed several algorithms for the segmentation of aorta in CT scans and neighboring structures that can help to determine where an enlargement is located. However, we have noticed that this aorta segmentation method fails to work correctly when the aorta is enlarged because it has not been trained with sufficient examples of enlarged aortas. This is visible in the figure below where you see in an axial (left) and coronal view (right) that the thrombus in the enlarged aorta (yellow arrow) has not been included in the aorta segmentation (green area).

![Segmentation example]({{ IMGURL }}/images/projects/aaa-overview.jpg) 

Using our large research database of CT scans acquired in Radboudumc, it is possible to improve the existing algorithm to accurately segment and measure the aorta also in abnormal CTs and develop a robust solution to this problem. We also observe that a computer algorithm can detect small changes over time because many patients get multiple CT scans and it is known that aortas can become enlarged with time at a mean rate that is initially slow and then suddenly starts to increase rapidly. Radiologist now do not routinely measure the aortic diameter at corresponding places and may miss such growth patterns. 

## Data
In our group we have a database of over 200,000 CT studies. Using the radiology reports and natural language processing, we expect to be able to retrieve a large number of AAA cases. This exercise is part of the project.

## Results
The algorithm we are developing will be made available as a Docker container on [https://grand-challenge.org/](https://grand-challenge.org/algorithms/abdominal-aortic-aneurysm-detection-in-ct-scans/). It can then be applied to CT scans from hospitals that use the grand-challenge infrastructure. We are currently working to write a scientific publication on the results of the project.

The thesis can be downloaded [here](http://eia.udg.edu/~aoliver/maiaDocs/bookMaia5th_small2.pdf#page=65).
