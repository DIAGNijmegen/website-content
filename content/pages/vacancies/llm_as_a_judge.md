title: LLM-as-a-Judge as a validation framework for clinical Generative AI tools
groups: rtc
closed: false
type: student
picture: vacancies/ehr_llm.jpeg
template: vacancy-single
people: Julie Swillens, Tim Frenzel, Arjen de Vries
description: Designing an LLM-as-a-Judge framework to validate clinical generative AI tools integrated in the EHR at Radboudumc


## Background

Generative AI (GenAI) applications are increasingly being integrated into clinical workflows to reduce the workload of healthcare professionals and improve efficiency [1]. At Radboudumc, several GenAI tools are currently being evaluated in pilot settings within the electronic health record (EHR) system Epic. These include “ART”, a tool that drafts responses to patient messages, and “OP & IP Insights”, which automatically summarize recent medical notes.

To ensure safe and responsible deployment in clinical practice, these tools require thorough validation, not only during initial deployment but also whenever the underlying large language models (LLMs) or prompts are updated. Traditional human validation is resource-intensive and does not scale well. Recently, the concept of *LLM-as-a-Judge* has been proposed, where an LLM is used to automatically evaluate the output of another LLM on dimensions such as correctness, completeness, relevance, and potential harm [2]. This project explores whether such an approach can serve as a reliable and efficient validation framework for clinical GenAI tools within the EHR.

## Approach

In this project, the student will design and implement an LLM-as-a-Judge framework tailored to the Radboudumc context. The framework will be applied to evaluate outputs from existing Epic-integrated GenAI tools.

Depending on the student’s interests, the project may focus on:

- Comparing LLM-based evaluations with human annotations
- Studying the robustness and bias of LLM-as-a-Judge scores
- Experimenting with different judge models, prompts, and evaluation rubrics

The work will contribute to the development of a scalable technical validation pipeline for clinical GenAI, supporting future implementation and updates of these tools in routine care.

## Data

The project will use extracted data from real clinical EHR workflows at Radboudumc. Available data include:

- Drafted and final clinician-approved responses to patient messages (ART)
- Original clinical notes and their automatically generated summaries (OP & IP Insights)

Where available, clinician outputs will serve as a reference standard.

## References

[1] Hu, D., Guo, Y., Zhou, Y., Flores, L., & Zheng, K. (2025). A systematic review of early evidence on generative AI for drafting responses to patient messages. *npj Health Systems*, 2(1), 27.  
[2] Croxford, E., Gao, Y., First, E., Pellegrino, N., Schnier, M., Caskey, J., ... & Afshar, M. (2025). Evaluating clinical AI summaries with large language models as judges. *npj Digital Medicine*, 8(1), 640.

## Requirements

Students in the final phase of a Master’s program in Artificial Intelligence, Computer Science, Biomedical Engineering, Data Science, or a related field are invited to apply.

**Required skills:**

- Experience with Python programming
- Familiarity with machine learning or NLP concepts

Affinity with clinical AI validation, LLMs, or healthcare data is a strong plus.

## Information

**Project duration:** Approximately 6 months (flexible, depending on student interests)  
**Location:** Radboud University Medical Center

The student will be embedded in the Implementation, (De-)Implementation and Behavioural Change group of the IQ Health department and collaborate closely with clinical, AI, and IT stakeholders. Access to GPU resources will be arranged through existing institutional infrastructures.

For more information, please contact Julie Swillens (Julie.Swillens@radboudumc.nl).

