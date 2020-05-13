title: PANDA Challenge
finished: false
type: general
picture: projects/panda_logo_notext.png
template: project-single
groups: pathology
description: Challenge on prostate cancer grading of biopsies using the Gleason grading system.
people: Wouter Bulten, Peter Ström, Kimmo Kartasalo, Hans Pinckaers, Martin Eklund, Geert Litjens 
bibkeys: Bult20

<img alt="PANDA Challenge logo" class="img-fluid" src="https://www.computationalpathologygroup.eu/images/projects/panda_logo_square.png" style="max-width: 300px; float: right; padding-left: 1em;">


With 1.1 million new diagnoses every year, **prostate cancer (PCa) is the most common cancer** in men in developed countries. The biopsy Gleason grading system is the most important prognostic marker for prostate cancer but suffers from significant inter-observer variability, limiting its usefulness for individual patients. The Gleason grade is determined by pathologists on hematoxylin and eosin (H&E) stained tissue specimens based on the architectural growth patterns of the tumor.

Automated deep learning systems have shown promise in accurately grading prostate cancer. Several studies have shown that these systems can achieve pathologist-level performance. A large multi-center evaluation on diagnostic data is still missing. In this challenge, we strive to improve on these works by publishing the most **extensive multi-center dataset on Gleason grading** as of yet. The training set consists of up to 11.000 whole-slide images of digitized H&E-stained biopsies originating from two centers. This is the largest public whole-slide image dataset available, roughly eight times the size of the CAMELYON17 challenge. Furthermore, in contrast to previous challenges, we do not use small tissue micro-arrays, but full diagnostic biopsy images. Using a sizeable multicenter test set, graded by expert uropathologists, we will evaluate challenge submissions on their applicability to a clinically relevant task.

## Task

The task of the challenge is to design a system that can automatically detect prostate cancer, and if there is cancer present, assign a grade group. The biopsy-level grade should follow the ISUP grade group system.

## Participate in the challenge

The challenge is hosted on Kaggle. Please signup at the [Kaggle webite](https://www.kaggle.com/c/prostate-cancer-grade-assessment/overview).

## Organizers

The PANDA challenge is organized in collaboration with researchers from the Karolinska Institute (Sweden).

