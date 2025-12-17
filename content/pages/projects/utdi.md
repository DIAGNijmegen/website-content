title: Unstructured Textual Data Integration for Radiology Image Analysis (UTDI)
title_long: Unstructured Textual Data Integration for Radiology Image Analysis (UTDI)
finished: false
type: general
picture: projects/UTDI.jpg
template: project-single
groups: diag
people: Luc Builtjes, Alessa Hering
description: Integrating unstructured radiology reports with image analysis using large language models
bibkeys: Buil25, Buil24

## Background

Radiology reports are critical components of clinical workflows, providing detailed narratives that complement imaging studies. These reports are typically unstructured, written in free-text formats, and contain a mix of observations, impressions, and recommendations. While rich in information, this lack of structure poses significant challenges for automated processing and integration into data-driven healthcare systems. 

The increasing adoption of advanced radiology image analysis tools highlights the need for complementary text-processing solutions. For example, automated impression generation can help streamline report summaries for downstream use, while accurate information extraction supports clinical decision-making and research. Moreover, robust anonymization methods are crucial to ensure that sensitive patient information is protected during data sharing and analysis. 

This project explores the use of large language models (LLMs) to address these challenges by processing and integrating textual data in radiology. LLMs are applied to tasks such as summarizing detailed reports, extracting structured data from narrative content, and anonymizing sensitive information. By combining these textual insights with image analysis, the research aims to create tools that support radiologists, enhance efficiency, and unlock new opportunities for leveraging radiology data in clinical practice and research. 

As part of this project, the Python package [**llm_extractinator**](https://github.com/DIAGNijmegen/llm_extractinator) was developed to support structured information extraction from unstructured radiology reports using large language models. The package provides configurable pipelines for mapping free-text reports to structured outputs based on user-defined schemas and prompts. It is intended to facilitate tasks such as report summarization, information extraction, and de-identification, and to support downstream analysis and integration with imaging-derived data.

