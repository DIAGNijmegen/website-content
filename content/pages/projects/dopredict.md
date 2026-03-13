title: DoPredict: Dynamic 3D Biopsy Based Response to Treatment Prediction
picture: projects/dopredict.png
finished: false
type: general
description: AI-based analysis of the effect of drugs on cultured biopsies of patients with lung cancer or fibrotic lung disease using 3D+T label-free HHG microscopy.
template: project-single
groups: diag, pathology
default_group: pathology
people: Evgenia Martynova, Francesco Ciompi, Naomi Duits, Marloes Groot, Jan Willem Duitman, Annemiek Dijkhuis
bibkeys:

## Background
Despite recent advances in personalized medicine, selecting the optimal treatment for a patient can be challenging. Response rates to cancer therapies remain highly variable and often low, especially in lung cancer. For its most common type, non-small cell lung cancer (NSCLC), response rates range from 9 to 74% depending on the therapy and patient population [1]. This problem is not limited to cancer and is also highly relevant for fibrotic interstitial lung disease (fILD), where standard immunosuppressive therapy fails in a substantial part of the population [2,3].  This underscores the urgent need for approaches that can reliably predict an individual patient’s response to available treatments for lung cancer and fILD.  

Several predictive biomarkers have been developed for NSCLC and are now routinely used in clinical practice to select patients for specific treatments. Biomarkers for targeted therapies have demonstrated good predictive performance: in biomarker-positive patient populations, response rates to targeted therapies are often approximately two-fold higher than those observed with standard chemotherapy. In contrast, for immunotherapy, only a modest increase in response rate has been achieved. Yet both types of treatment often yield only modest improvements in overall survival, typically up to a few months, while being associated with high costs and considerable side effects for patients [1]. 

One likely explanation for the limited predictive power of current biomarkers is that they do not sufficiently integrate the information about the tumor-immune microenvironment (TIME). Most existing biomarkers rely on static molecular measurements and therefore fail to reflect the dynamic interactions between tumor and immune cells. Meanwhile, spatio-temporal dynamics of the TIME, such as survival of tumor and immune cells, cell division metrics, and cell-cell interactions, can be essential determinants of therapy success. Therefore, new biomarkers derived from TIME dynamics may be promising for improving patient stratification. 

## Aims
DoPredict aims to develop a compact personalized testbed that allows prediction of the optimal treatment for a patient by testing the effects of multiple drugs applied to fresh, unprocessed patient biopsies. Acute biopsies containing intact tissue architecture and exposed to different treatments will be kept viable for 5-7 days and imaged during culturing in 3D with higher harmonic generation (HHG) microscopy, generating 3D+T data for each sample. Such live imaging is possible since HHG microscopy is label-free, requires no tissue preparation, and does not damage tissue. This approach allows us to capture the spatio-temporal dynamics of the tumor–immune microenvironment (TIME) in patient tissue biopsies. 

Using these rich data, we will: 

- Develop AI methods for advanced analysis of 3D+T HHG images, including such tasks as tissue segmentation, detection and classification of cells, and tracking them over time. 

- Derive the metrics characterizing TIME dynamics using the output of these AI algorithms, such as tumor reduction rate, change in relative frequencies of tumor and immune cells, immune cell motility, and changes in collagen content. 

- Investigate and validate the predictive power of the derived TIME-based characteristics by correlating them with patient responses to treatment in a set of test control samples. 

Potentially, this platform will provide clinicians with the prediction of optimal treatment for a patient within 5-7 days. 

## Funding
This project is supported by [NWO Open Technology Program](https://www.nwo.nl/en/projects/20863).

## References

1. D. R. Camidge, R. C. Doebele, K. M. Kerr, Comparing and contrasting predictive biomarkers for immunotherapy and targeted therapy of NSCLC. Nature Reviews Clinical Oncology 16, 341-355 (2019).

2. C. Hyldgaard, S. Torrisi, S. Kronborg Brix-White, T. S. Prior, C. Ganter, E. Bendstrup, M. Kreuter, Immunomodulatory treatment in unclassifiable interstitial lung disease: A retrospective study of treatment response. Respirology 28, 373-379 (2023).

3. H. Barnes, K. A. Johannson, Management of Fibrotic Hypersensitivity Pneumonitis. Clin Chest Med 42, 311-319 (2021).
