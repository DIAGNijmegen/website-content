title: Deep placental vessel segmentation and registration for fetal laser surgery
groups: ai-for-health
closed: true
type: student
picture: vacancies/placental-vessel-segmentation.png
template: vacancy-single
people: Anouk van der Schot, Guido de Jong
description: Development of a model for deep placental vessel segmentation and registration for fetal laser surgery

**This is an AI for Health MSc project. Students are elgible to receive a monthly reimbursement of €500,- for a period of six months. For more information please read the requirements.**

## Clinical Problem
Twin-to-twin transfusion syndrome (TTTS) is a severe and progressive disorder where there are imbalanced blood vessel connections in the shared placenta of monochorionic twins. Untreated, this syndrome is associated with a 90% mortality rate of the twins.
Laser surgery has become the treatment of choice for TTTS[1]. During this procedure, a small diameter endoscope (fetoscope) is used to visualize the placental surface in the uterus. The surgeon scans the placenta to localize and coagulate blood vessel connections to dissolve the blood flow.[2]
However, even in the most experienced fetal therapy centers, survival rates remain below 90%. The stagnation of survival rates is due to, on the one hand, the limited field of view and poor visibility in the uterus. This limited view, together with the complexity of the surgical task of recognizing the vessels at the placental surface, midst the very variable topography of vessels, can result in incomplete surgery, leading to recurring or reversal of the TTTS.[3]
A computer-assisted guidance system can help overcome these challenges by providing better visualization of the vessel map and artificially expanding the surgical field of view, guiding the surgeons in quick and precise detection of the placental blood vessel connections.[4]

[1] M.-V. Senat, J. Deprest, M. Boulvain, A. Paupe, N. Winer, and Y. Ville, "Endoscopic laser surgery versus serial amnioreduction for severe twin-to-twin transfusion syndrome," N. Engl. J. Med., vol. 351, no. 2, pp. 136–144, 2004.

[2] S. H. P. Peeters et al., "Identification of essential steps in laser procedure for twin-twin transfusion syndrome using the Delphi methodology: SILICONE study," Ultrasound Obstet. Gynecol., vol. 45, no. 4, pp. 439–446, Apr. 2015, doi: 10.1002/uog.14761.

[3] E. Lopriore, J. M. Middeldorp, D. Oepkes, F. J. Klumper, F. J. Walther, and F. P.H.A. Vandenbussche. Residual Anastomoses After Fetoscopic Laser Surgery in Twin-to-Twin Transfusion Syndrome: Frequency, Associated Risks and Outcome. Placenta, vol. 28 no. 2, pp. 204–208, 2007

[4] Rosalind Pratt, Jan Deprest, Tom Vercauteren, Sebastien Ourselin, and Anna L. David. Computer-assisted surgical planning and intraoperative guidance in fetal surgery: A systematic review, 2015.

## Solution
Technical solutions to artificially extend the visual field of view of the surgeon are of major interest in the field. However, translation to clinical practice is still limited. Two main tasks are formulated to foster research in this field and catalyze a fast clinical implementation:

1.	Placental vessel segmentation
Intra-operative fetoscopic vessel segmentation can guide the surgeon during fetal surgery. In addition, the segmentation can be used to perform fetoscopic video mosaicking. 
The first task aims to segment four classes in the fetoscopic images, namely, background, vessels, tool, surgical instrument, and fetus. 

2.	Fetoscopic video mosaicking
Promising results have been achieved for mosaicking from short fetoscopic video sequences. However, these solutions are not yet clinically applicable since long-term mapping remains an open challenge. The second task aims to perform fetoscopic registration of consecutive frames to create a drift-free mosaic of the fetoscopic environment.
These tasks are also part of the FetReg 2021 challenge1.

## Data
There are three databases available for the segmentation task. The image appearance and quality varies in each video, due to the variation in intra-operative environment among different cases and lightning conditions. Also, the videos present different resolutions as the videos are captured at different centres with different facilities, resulting in an increased variability in the data.

1.	The first dataset is a public set that contains 483 frames with ground-truth vessel segmentation annotation from six different fetoscopic procedure videos. This dataset is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

2.	Another online dataset contains 2060 frames with ground-truth vessel, tool, and fetus segmentation annotations from 18 different fetoscopic procedure videos. The videos
contained in this dataset are collected from three fetal surgery centres across Europe.
Note: this database cannot be used for publication.

3.	An intern database containing ~1200 frames with ground-truth vessel, tool, and fetus segmentation annotations from 8 different fetoscopic procedure videos is being prepared.  
For the second task, two databases are available:

1.	An online database is containing unannotated video clips of 18 fetoscopic procedures. The clips exist of representative frames every 2 seconds. These videos contained in this dataset are collected from three fetal surgery centres across Europe
Note: this database cannot be used for publication.

2.	An internal database is available that contains unannotated video clips of 8 fetoscopic procedures. Also, these clips exist of representative frames every 2 seconds.

## Embedding
You will be embedded in the Department Obstetrics & Gynaecology at Radboudumc, and collaborate closely with 3D Lab Radboudumc. We provide access to CPU and GPU clusters, direct supervision by PhD students and regular meetings with the supervisors of this project.

## Requirements
-	Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics in the final stages of their Master education.
-	You should be proficient in python programming and have a theoretical understanding of deep learning architectures.
-	Basic biological / biomedical knowledge is preferred, but not necessary.


## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- More information can be obtained from [Anouk van der Schot](mailto:anouk.vanderschot@radboudumc.nl)
