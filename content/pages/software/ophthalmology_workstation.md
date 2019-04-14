title: Ophthalmology workstation
title_long: Ophthalmology workstation 
finished: false
picture: software/ophthalmology_workstation_small.jpg
template: project-single
groups: retina, rse, diag
people: Harm van Zeeland, James Meakin, Clarisa Sánchez, Caroline Klaver
description: The goal of this project is to develop a software solution that assists researchers and specialists to view and annotate retinal images. 
bibkeys: 

## Aim

Researchers and specialists in the field of ophthalmology currently rely on suboptimal vendor-specific software solutions for viewing and annotating retinal images. Our goal is to develop a fully-featured vendor-independent application that allows researchers and specialists to visualize multi-modal retinal images, perform spatial alignment and annotations, and review outputs of artificial intelligence (AI) algorithms.

## Software

The application consists of a web-based front-end that allows users to analyze baseline and follow-up images in a multi-modal viewer. It communicates with a back-end API for grader authentication, loading and storing of images and annotation data. Several types of annotation techniques are available, ranging from image-level classification to point-based and region-based lesion-level annotations.

![Workstation]({filename}/images/software/ophthalmology_workstation.jpg)
*Screenshot showing a multi-modal hanging protocol with annotated lesions.*

The user can select color fundus (CF) images, optical coherence tomography (OCT) volumes, infrared (IR) and autofluorescence (AF) images to be shown simultaneously in the viewer. Spatial alignment of the different modalities can be performed using an integrated affine registration method by clicking on corresponding landmarks, after which a synchronized cursor will appear. After several graders have annotated lesions, the application can be used to compare these and create a consensus grading.

![Workstation consensus]({filename}/images/software/ophthalmology_workstation_consensus.jpg)
*Screenshot showing the view for a consensus grading.*

## Usage

The application has been used by graders and researchers in the EyeNED research group. Region based annotations of geographic atrophy were made for 313 studies containing 488 CF images and 68 OCT images; and of drusen in 100 OCT b-scans. Semi-automatic annotation of the area of central retinal atrophy in Stargardt disease was performed for 67 AF images. Point-based annotation was carried out on lesions in 50 CF images of diabetic retinopathy patients. The multimodal viewing and localisation of lesions was perceived as particularly helpful in the grading of lesions and consensus discussions.

