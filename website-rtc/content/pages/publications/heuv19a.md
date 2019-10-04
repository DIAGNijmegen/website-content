title: Automated Fetal Head Detection and Circumference Estimation from Free-Hand Ultrasound Sweeps Using Deep Learning in Resource-Limited Countries
authors: T.L.A. van den Heuvel, H. Petros, S. Santini, C.L. de Korte and B. van Ginneken
has_pdf: True
template: publication
bibkey: heuv19a
published_in: Ultrasound in Medicine and Biology
pub_details: <i>Ultrasound in Medicine and Biology</i> 2019;45(3):773-785
doi: https://doi.org/10.1016/j.ultrasmedbio.2018.09.015
pmid: http://www.ncbi.nlm.nih.gov/pubmed/30573305
Ultrasound imaging remains out of reach for most pregnant women in developing countries because it requires a trained sonographer to acquire and interpret the images. We address this problem by presenting a system that can automatically estimate the fetal head circumference (HC) from data obtained with use of the obstetric sweep protocol (OSP). The OSP consists of multiple pre-defined sweeps with the ultrasound transducer over the abdomen of the pregnant woman. The OSP can be taught within a day to any health care worker without prior knowledge of ultrasound. An experienced sonographer acquired both the standard plane-to obtain the reference HC-and the OSP from 183 pregnant women in St. Luke's Hospital, Wolisso, Ethiopia. The OSP data, which will most likely not contain the standard plane, was used to automatically estimate HC using two fully convolutional neural networks. First, a VGG-Net-inspired network was trained to automatically detect the frames that contained the fetal head. Second, a U-net-inspired network was trained to automatically measure the HC for all frames in which the first network detected a fetal head. The HC was estimated from these frame measurements, and the curve of Hadlock was used to determine gestational age (GA). The results indicated that most automatically estimated GAs fell within the P2.5-P97.5 interval of the Hadlock curve compared with the GAs obtained from the reference HC, so it is possible to automatically estimate GA from OSP data. Our method therefore has potential application for providing maternal care in resource-constrained countries.

