title: CHIMERA
picture: projects/chimera.png
finished: false
type: general
description: The CHIMERA Challenge benchmarks multimodal AI, integrating transcriptomics, pathology, and radiology to improve cancer recurrence prediction.
template: project-single
groups: diag, pathology
default_group: pathology
people: Catherine Chia, Robert Spaans, Tongjie Wang, Farbod Khoraminia, Khrystyna Faryna, Maryam Mohammadlou, Tahlita Zuiverloon, Jean-Paul van Basten, Sita Vermeulen, Geert Litjens, Nadieh Khalili, Adam Kowalewski, Parandzem Khachatryan, Alberto Nakauma-González, Domingos Oliveira

## Background
The CHIMERA Challenge aims to advance precision medicine in cancer care by addressing the critical need for multimodal data integration. Despite significant progress in AI, integrating transcriptomics, pathology, and radiology across clinical departments remains a complex challenge. Clinicians are faced with large, heterogeneous datasets that are difficult to analyze effectively. AI has the potential to unify multimodal data, but several technical barriers remain, such as defining appropriate fusion stages and handling missing modalities.

## Aim
Unlike previous challenges focusing on single modalities, CHIMERA introduces a benchmark for multimodal AI models that integrates transcriptomics, histopathology, and radiology. CHIMERA includes prostate cancer and non-invasive bladder cancer (NIBC) datasets to improve recurrence prediction and optimize treatment strategies across three distinct tasks.

### Prostate Cancer Recurrence Prediction (Task 1):
Current assessments rely on PSA levels, a controversial biomarker with limited reliability in predicting biochemical recurrence. CHIMERA integrates multiparametric MRI and H&E-stained histopathology slides, routinely used in clinical practice, to enhance recurrence prediction. Deep learning has shown that morphological features in histopathology provide significant prognostic value.

### Non-Invasive Bladder Cancer (NMIBC) Response Predictions (Task 2 and 3):
50% of NIBC patients fail to respond to BCG treatment, a globally scarce resource. Molecular RNA analysis has been linked to high-risk treatment response and can aid in early treatment decision-making. Integrating transcriptomics, pathology, and imaging can improve prognostic accuracy and patient management.
