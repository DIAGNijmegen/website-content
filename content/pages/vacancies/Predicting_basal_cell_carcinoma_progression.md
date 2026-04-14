title: Predicting Basal Cell Carcinoma Progression from Histopathology Using Artificial Intelligence
groups: diag, pathology
closed: false
type: student
picture: vacancies/basal_cell_carcinoma_microscopic.png
template: vacancy-single
people: Ivan Slootweg, Geert Litjens 
description: Predicting basal cell carcinoma progression from histopathology using Artificial Intelligence
date: 2026-04-15

**Department**: Dermatology & Pathology, Radboud University Medical Center, Nijmegen

## Background

Basal cell carcinoma (BCC) is the most common cancer worldwide, with 4.0 million cases diagnosed globally in 2019. In the Netherlands, 1 in 5 people will develop at least one BCC during their lifetime, and 1 in 3 patients develops multiple tumors over time. BCC mainly affects older adults, with a median age at diagnosis of 70 years. Given the aging population and UV-exposure habits, the number of cases is expected to keep rising, putting unprecedented pressure on healthcare systems.

![Incidence Basal cell carcinoma]({{ IMGURL }}/images/vacancies/Incidence_basal_cell_carcinoma.png)

**Fig. 1:**  Incidence trends for the most common type of tumors per organ. (left) Basal cell carcinoma cases are registered since 2017. (right) In 2025, basal cell carcinoma was responsible for 1 third of all tumors overall and for 70% of all tumors of the skin. Source: IKNL

## Problem

The good news is that BCC grows very slowly. The median annual increase in tumor diameter is only 1 to 4 mm, metastasis is extremely rare, and spontaneous regression has been described in 10 to 20% of cases. Most BCCs cause no complaints, and when they do, symptoms are usually mild. On the other hand, 15% of BCCs turn out to progress into more severe tumors. Current guidelines offer limited guidance on whether active treatment is truly needed or whether active surveillance, meaning close monitoring without immediate treatment, is the more appropriate strategy. This is especially relevant for older patients who may not live long enough to develop bothersome symptoms, while treatment itself can cause a significant burden.

A recent observational cohort study at our center followed patients with BCC under active surveillance. We observed substantial heterogeneity in tumor behavior, and the factors driving this variability remain largely unexplained. Being able to predict which tumors will progress and which will remain stable would directly support prioritizing treatment for high-risk patients, especially given that waiting times for specialized care can be as long as six months.

![Basal cell carcinoma]({{ IMGURL }}/images/vacancies/basal_cell_carcinoma_microscopic.png)

**Fig. 2:**  A microscopic image of basal cell carcinoma with the epidermis at the bottom. The heatmap overlay are detected cancer regions of a developed model.

## Project aim

Scientific literature proposes many biomarkers associated with BCC aggressiveness and progression. Many of these markers are traditionally assessed by immunohistochemistry (IHC), but a substantial number have morphological correlates that are visible or potentially detectable on H&E. On top of that, clinical variables such as tumor location, tumor size, patient age, sex, recurrent versus primary status, and the presence of ulceration can be combined with the imaging features.

The aim of this project is to develop and evaluate an AI model that predicts BCC tumor progression using routinely available data: H&E-stained histopathology images from diagnostic punch biopsies, combined with clinical and demographic variables. The central question is whether morphological features visible on standard H&E slides, without the need for additional IHC staining, contain enough prognostic information to distinguish progressive from stable BCC.

## Approach

The project will use data from an existing observational cohort of patients with BCC managed by active surveillance at the Radboud University Medical Center.

As a student you will:

**Prepare and curate the dataset.** This involves working with digitized baseline H&E-stained punch biopsies and translating patient variables into meaningful inputs for a computational model. You may even use AI models to extract more image-derived features.

**Develop an AI prediction model.** You will train and evaluate weakly-supervised learning models on whole slide images to predict tumor progression. This may involve patch-level feature extraction, and integration of clinical variables.

**Analyze which morphological features drive the prediction.** Using explainability methods you will identify which tissue regions and morphological patterns the model relies on and relate these back to the known biomarker evidence. For example, does the model attend to basement membrane regions or stromal patterns?

**Evaluate the added value of IHC.** You will compare model performance using H&E images alone versus H&E combined with biomarkers selected by a pathologist.

## What we are looking for

A motivated master student in Artificial Intelligence, Data Science, Biomedical Engineering, Computer Science, or related field. You should have experience or strong interest in deep learning and image analysis, programming skills in Python, and an interest in medical or clinical applications.

## Information

- You will be supervised by an interdisciplinary team covering dermatology, pathology, and computational pathology.

- The work you do has direct clinical relevance: it contributes to improving shared decision making in skin cancer management.

- We provide access to a unique and well characterized cohort of BCC patients under active surveillance with longitudinal tumor measurements. You will learn to work with digitized histopathology slides that are gigapixel in size.

- There are existing AI frameworks developed in our group that you can build on.

- Duration: 6 to 9 months

- Start: Flexible

- For more information please contact Ivan Slootweg

## People

Supervisors: Ivan Slootweg (Computational Pathology), Satish Lubeek (Dermatology), Avital Amir (Pathology), Geert Litjens (Computational Pathology).
