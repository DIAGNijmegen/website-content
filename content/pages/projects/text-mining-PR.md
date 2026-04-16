title: Text mining to extract lifestyle classifications for prevention-related research
title_long: Diving into the tangle of unstructured clinical notes: Text mining to extract lifestyle classifications for prevention-related research
finished: false
type: general
picture: projects/text-mining-PR.jpg
template: project-single
groups: diag, rtc
people: Anushka Ashish Kore, Silvan Quax, Esmée Bakker, Alina Vrieling, Sander Beekhuis
description: Extracting lifestyle information for prevention-related research from clinical notes using text mining and NLP techniques
bibkeys:

## Problem description
Data on lifestyle is key for prevention-related research. For example, data could be used to 1) identify individuals with an unhealthy lifestyle at high risk of developing (chronic) disease or disease progression, and 2) examine the long-term effectiveness of lifestyle prescription or programs. However, lifestyle data is often recorded as free (unstructured) text in clinical notes. Extraction and interpretation of these data is challenging due to heterogeneity in note-taking among clinicians. Furthermore, privacy and feasibility issues prohibit researchers to go through individual patient records. This complicates extracting this data at a large scale. Recently, Bi-directional Encoder Representations from Transformers (BERT) based models have been developed by researchers in LUMC to classify smoking, alcohol, and drugs use based on Dutch free text from clinical notes from HagaZiekenhuis [(Muizelaar et al., 2024)](https://link.springer.com/article/10.1186/s12911-024-02557-5). These state-of-the-art NLP models processing allow efficient and valid extraction of lifestyle classifications on a large scale without violating patients’ privacy. More recently, large language models (LLMs) have been shown to outperform or match BERT-based models on several tasks for clinical information extraction [(Builtjes et al., 2025)](https://academic.oup.com/jamiaopen/article/8/5/ooaf109/8270821). However, they have not been used and validated for lifestyle data extraction yet.

## Aim
This collaborative project between [RTC AI](https://rtc.diagnijmegen.nl/) and the Prevention Hub, aims to-
1) validate, optimize and evaluate the performance of LLMs for smoking, alcohol, and drugs use classification using clinical notes from Radboudumc and the RTC Health data General Practitioners (GP) database, and
2) explore extension of these models to classification of BMI, physical activity, and diet.

This project will also provide insight into the availability and usability of lifestyle data in clinical notes and how registration of lifestyle data could be improved.

## Funding
This research project is funded by the [Sectorplan](https://www.radboudumc.nl/en/projects/sector-plan-medische-en-gezondheidswetenschappen) and falls under the themes of "Data-driven innovation" and "Data-driven & AI". 
