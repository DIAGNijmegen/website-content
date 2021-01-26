title: MRI-based decision support tool for patients with chronic lower back pain
groups: diag, ai-for-health 
finished: false
type: general
picture: projects/msk_lbp.jpg
people: Jasper van der Graaf, Nikolas Lessmann, Miranda van Hooff, Bram van Ginneken, Marinus de Kleuver 
template: project-single
description: We develop AI-based MRI analysis software for treatment decision support in patients with chronic degenerative low back pain.

Low back pain (LBP) is worldwide responsible for more years lived with disability than any other health condition. In the Netherlands, approximately 44% of the population experiences at least one episode of LBP in their lifetime, with one in five reporting persistent back pain lasting longer than three months (chronic low back pain, CLBP). CLBP often results in substantial limitations in functional activities and is responsible for high healthcare and socioeconomic costs. In the vast majority of patients with CLBP (85-90%), the aetiology is unknown and for medical specialists it is challenging to identify patients who would benefit from surgical or non-surgical interventions.

The Nijmegen Decision Tool for CLBP (NDT-CLBP) is a pre-diagnostic decision support tool that matches patients based on a questionnaires to the treatment that they are most likely to benefit from. Patients are referred to either spinal surgeon consultation or non-surgical consultation. In this project the NDT-CLBP will be further developed into a two-phased decision support tool following the patient journey: phase 1 decision support for consultation (currently in use) and phase 2 decision support for referral to a specific treatment based on the clinical diagnostic phase (NDT-CLBP 2.0). In the diagnostic phase, many patients with CLBP receive a lumbar spine MRI scan to detect degenerative changes of the spine. The goal of this project is to develop an AI-based image analysis algorithms that enable detailed quantitative routine analysis of these MRI scans.

The first step in creating such an algorithm is getting an automatic segmentation of the spine. In our first project we aim to create a convolutional neural network that automatically segments vertebrae and inter-vertebral discs on MRI scans. Anonymized clinical MRI scan from the RadboudUMC are manually annotated which will be used to train the network. Eventually we also aim to organize a segmentation challenge using this dataset. 

To identify which MR image features are related to CLBP a narrative review is being written. In this review an overview of all possible image features is presented in five different catagories: discogenic, neurogenic, osseous, facetogenic and paraspinal. Per catagory an overview of all relevant literature is given. The result of this review will be a list of image features that have a high predictive value for CLBP which eventually will be used in the decision support tool. 

## Funding
* [AI for Health](https://www.ai-for-health.nl/)
