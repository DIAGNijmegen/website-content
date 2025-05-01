title: Retrospective Evaluation of AI Stability for Lung Cancer Detection
groups: diag
closed: false
type: student
picture: vacancies/ai-lung-tumor-detection.png
template: vacancy-single
people: Dré Peeters, Merel Huisman, Colin Jacobs
description: Retrospective Evaluation of AI Stability for Lung Cancer Detection in real-world clinical setting

## Clinical Problem

Artificial intelligence (AI) algorithms are increasingly achieving performance comparable to human experts in many medical imaging tasks, however, their performance may degrade over time once deployed due to a variety of external factors. Therefore, there is a growing need to assess their robustness, stability and clinical applicability in real-world clinical settings. This necessity extends beyond the external testing and is termed post-market surveillance (PMS), which is the systematic monitoring of AI behavior following its deployment. PMS is closely aligned with emerging regulatory frameworks, such as the European AI Act, which requires continuous monitoring of AI systems in healthcare. 

While AI algorithms often demonstrate strong performance in controlled research environments, translating these results into routine clinical practice presents significant challenges. There are several factors that can impact AI performance in clinical practice, which include but are not limited to: <br>
- Scanner variability: differences in imaging hardware (vendors, models) and acquisition settings<br>
- Population shifts: variations in patients or disease prevalence<br>
- Dataset drift: gradual changes<br>

Such factors can lead to unexpected changes in model outputs, potentially affecting patient safety and clinical trust if left unmonitored.  

In this project, we aim to retrospectively evaluate the longitudinal performance and stability of our in-house AI algorithms for lung nodule detection and malignancy risk estimation, and identify some of the conditions under which their performance becomes unstable

## Objectives / Aims / Goals

**Primary Objective**:
Evaluate the performance and stability of our in-house AI algorithms for lung nodule detection and malignancy risk estimation over multiple years, and identify scenarios that may affect the output of the algorithms. 

**Further goals** (depending on project scope, student interests, literature findings, and initial conclusions):<br>
- Simulate a post-market surveillance scenario to systematically assess the AI performance<br>
- Investigate how a nodule detection and malignancy risk estimation pipeline would perform in a real-world clinical scenario<br>
- Perform clinical and technical subgroup analyses to assess which conditions are resulting in unexpected changes in for example nodule detection rates, and number of malignant cases<br>


## Requirements

- Master students with a major in technical medicine, computer science, mathematics, biomedical engineering/sciences, artificial intelligence, or a related area in the final stage of master’s studies are invited to apply<br>
- Experience with programming in Python<br>
- Experience or interest in deep learning, medical imaging, and/or medical image analysis<br>

## Practical Information

- **Project Duration**: 6 months (Optionally: MSc Thesis)
- **Location**: Department of Medical Imaging, Radboud University Medical Center, Nijmegen
- For more information, please contact [member/dre-peeters].

## Suggested Reading

- W. Hendrix, N. Hendrix, E. Scholten, M. Mourits, J. Trap-de Jong, S. Schalekamp, M. Korst, M. van Leuken, B. van Ginneken, M. Prokop, M. Rutten and C. Jacobs, "Deep learning for the detection of benign and malignant pulmonary nodules in non-screening chest CT scans", Communications Medicine, 2023;3(1):156. doi: [10.1038/s43856-023-00388-5](https://doi.org/10.1038/s43856-023-00388-5)
- K. Venkadesh, A. Setio, A. Schreuder, E. Scholten, K. Chung, M. W Wille, Z. Saghir, B. van Ginneken, M. Prokop and C. Jacobs, "Deep Learning for Malignancy Risk Estimation of Pulmonary Nodules Detected at Low-Dose Screening CT.", Radiology, 2021;300(2):438-447. doi: [10.1148/radiol.2021204433](https://doi.org/10.1148/radiol.2021204433)
