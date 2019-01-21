title: CAMELYON17
finished: false
picture: camelyon17_logo.png
template: project-single
people: Peter Bandi, Oscar Geessink, Geert Litjens, Jeroen van der Laak
description: ISBI 2017 challenge to evaluate algorithms for automated detection and classification of breast cancer metastases in whole-slide images of histological lymph node sections.
bibkeys: Ehte17, Litj18
disable_gradient: true

## Overview

Built on the success of its predecessor, CAMELYON17 is the second grand challenge in pathology organised by the Diagnostic Image Analysis Group (DIAG) and Department of Pathology of the Radboud University Medical Center (Radboudumc) in Nijmegen, The Netherlands.

The goal of this challenge is to evaluate new and existing algorithms for automated detection and classification of breast cancer metastases in whole-slide images of histological lymph node sections. This task has high clinical relevance and would normally require extensive microscopic assessment by pathologists. The presence of metastases in lymph nodes has therapeutic implications for breast cancer patients. Therefore, an automated solution would hold great promise to reduce the workload of pathologists while at the same time reduce the subjectivity in diagnosis.

## Task

The TNM system is an internationally accepted means to classify the extent of cancer spread in patients with a solid tumour. It is one of the most important tools for clinicians to help them select a suitable treatment option and to obtain an indication of prognosis. Since the histological assessment of lymph node metastases is an essential part of TNM classification, CAMELYON17 will focus on the pathologic N-stage, in short: pN-stage.

In clinical practice several lymph nodes are surgically removed after which these nodes are processed in the pathology laboratory. In this challenge we forged **artificial patients**, with 5 slides provided for each patient where each slide corresponds to exactly one lymph node.

The task in this challenge is to **determine a pN-stage for every patient in the test dataset**. To compose a pN-stage, the number of positive lymph nodes (i.e. nodes with a metastasis) are counted. For the evaluation of the results we use five class quadratic weighted kappa where the classes are the pN-stages.

## Website

Further information, registration, and the results are available on the [challenge website](https://camelyon17.grand-challenge.org).
