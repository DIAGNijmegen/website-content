title: Adipose and muscular tissue segmentation
finished: false
type: general
description: For the department of Health Evidence we are developing an application for the segmentation and quantification of adipose and muscular tissue in non-contrast abdominal CT.
template: project-single
groups: rtc
picture: projects/body-composition.jpg
people: Alina Vrieling, Scott Maurits, Nikolas Lessmann, Ajay Patel, Bram van Ginneken
bibkeys: 

There is an increasing amount of evidence that body composition measured on CT scans, in particular muscle mass and quality, is associated with perioperative outcomes, toxicity of therapy and survival in cancer patients. As a result, there is increasing clinical interest in how body composition can be used to improve cancer treatment and care. A requirement for this, however, is that the determination of body composition can be integrated into the clinical workflow. However, the segmentation of body composition on CT scans is now largely done manually. This process consists of manual selection of the L3 vertebra on the abdominal CT scan, rough segmentation based on thresholding and manual correction. This requires expertise, takes a relatively long time, and is expensive and therefore not directly applicable in the clinic. There are now a few initiatives to automate this process. 
<br>

The RTC AI has developed a web-based application for the automatic selection of the L3 vertebra and segmentation and quantification of visceral adipose tissue (VAT), intramuscular adipose tissue (IMAT), skeletal muscle tissue (SM) and subcutaneous adipose tissue (SAT) in abdominal CT scans. The algorithm can be used on the [Grand Challenge](https://grand-challenge.org/) platform. All processing is performed on the platform; there is no specialized hardware required to try out the algorithm. Running the algorithm requires an account for Grand Challenge. If you don't have an account yet, you can register on the [website](https://grand-challenge.org/accounts/signin/); alternatively, you can log in using a Google account. After registering for a new account, or logging in to an existing Grand Challenge account, you can request access to the algorithm.

<a href="https://grand-challenge.org/algorithms/abdominal-ct-segmentation/" class="btn btn-primary btn-lg my-3">Try out the algorithm</a>
