title: Detecting and characterizing vertebral fractures in CT scans
groups: ai-for-health, diag
closed: false
type: student
picture: vacancies/msc-vertebral-fractures.jpg
template: vacancy-single
people: Nikolas Lessmann, Stan Buckens, Bram van Ginneken
description: Develop image analysis algorithms to detect osteoporotic fractures in the spine.

## Background
Osteoporosis is a silent age-related disease that slowly decreases the stability of the bones, which eventually leads to
bones starting to fracture and collapse. These kind of fractures are referred to as compression fractures. Every year,
millions of CT scans of the thorax and abdomen are made worldwide, for reasons other than osteoporosis and compression
fractures, but providing the opportunity to detect these kind of fractures in the spine.

## Research question and tasks
We have robust methods for automatically finding the spine in CT images and for delineating the individual vertebrae
that form the spine. The goal of this project is to develop a system that automatically determines for each vertebra
whether it is normal or whether it is starting to collapse. For abnormal vertebrae, the system needs to quantify the
degree to which the bone has collapsed in order to distinguish between early stage fractures and advanced fractures.

We have access to a set of CT scans in which fractures have been labeled by a radiologist. We also have access to a much
larger set of CT scans in which the vertebrae have been manually delineated, but in which fractures have not yet been
labeled. We furthermore have access to a very large amount of CT scans without any labels. While an initial completely
labeled dataset is therefore available, part of the project will be to configure a workstation that can be used by
radiologists to label additional data.

The resulting automatic fracture detection system will be a first step toward automatically reading all thorax CT scans
in the background to detect fractures that would otherwise be missed. The goal of the project is to make the developed
algorithm available on the [grand-challenge.org](https://grand-challenge.org) platform.

## Requirements
- Student in the final year of a Master study in biomedical engineering, artificial intelligence, data science or similar
- Interest in medical applications and medical image analysis
- Good programming skills are important (Python)
- A solid theoretical understanding of deep learning is crucial, experience with deep learning frameworks (PyTorch)
  is beneficial

## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- For more information, please contact [member/nikolas-lessmann]. To apply for this project, please include your CV and
  a short summary of your background and your interest in this project in your email.
