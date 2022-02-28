title: Domain Generalization for Prostate Cancer Detection in MRI
groups: ai-for-health
finished: false 
type: student 
picture: 
template: project-single
people: Sheikh Adinila, Anindo Saha, Henkjan Huisman
description: Develop a method for domain generalization for prostate cancer detection in MRI

**Start date: 01-02-2021** <br>
**End date: 01-07-2022**

## Clinical Problem 
One million men receive a prostate cancer diagnosis and 300,000 die from prostate cancer, each
year, worldwide. There are currently no blood/urine-based biomarkers that can reliably detect clinically significant
prostate cancer (csPCa). Magnetic resonance imaging (MRI) represents a breakthrough, facilitating the early
detection of csPCa, non-invasively. However, current guidelines for reading prostate MRI (i.e. PI-RADS v2) follow
a semi-quantitative assessment, leading to overdiagnosis and low inter-reader agreement among radiologists
(<50%). At the same time, csPCa can manifest as multifocal lesions of different shapes and sizes, bearing a strong
resemblance to numerous non-malignant conditions. Modern deep learning (DL) algorithms have paved the way
for powerful computer-aided detection/diagnosis (CAD) models that can improve diagnostic accuracy in prostate
MRI. However, unlike human readers, DL-CAD systems are highly sensitive to domain shifts (i.e. testing data
acquired from a different distribution, than the training data). Domain shifts can occur due to many factors (e.g.
different MRI scanners, patient cohorts, imaging protocols, etc.). When left unaccounted for, they can cause severe
degradation in DL-CAD performance, limiting their viability for clinical usage.

## Solution 
The goal of this project is to systematically investigate state-of-the-art classical and DL algorithms proposed
in recent literature for domain generalization, specifically for csPCa detection in prostate MRI. Possible solutions
are not limited to methods solely based on image transformations (e.g. histogram matching, domain adaptation
via CycleGANs), but can also include methods that improve generalization via training (e.g. domain adversarial
training, domain adaptation via data augmentation, etc.). All viable methods investigated in this study will be
benchmarked on our downstream task (i.e. DL-CAD performance on unseen multi-scanner data before and after
domain generalization is applied).

## Data 
The Diagnostic Image Analysis Group (DIAG) at Radboud University Medical Center has a scientific archive
of nearly 10,000 anonymized prostate biparametric MRI (bpMRI) scans. Over 3,000 scans have voxel-level labels
of radiologically-estimated csPCa lesions, and nearly 1,000 scans also include histologically-confirmed groundtruth
labels. For this project, an external multi-center, multi-scanner dataset of nearly 1,000 scans with biopsyconfirmed
csPCa labels, will also be made available for validation and testing

## Results
Any algorithm(s) conceived over the span of this project will be made available as a Docker container on
https://grand-challenge.org/. In turn, they can be applied by hospitals/researchers that use the grand-challenge
infrastructure. Significant results/breakthroughs will also yield a publication.
