title: Lung Lobe Segmentation in CT imaging
groups: diag
closed: false
type: student
picture: vacancies/LungLobeSegmentation.PNGs
template: vacancy-single
people: Lisa Klok, Colin Jacobs
description: Evaluation of Lung Lobe Segmentation models in Thoracic CT scans

## Clinical Problem

The computational detection of pulmonary lobes from CT images is a challenging segmentation problem in Radiology & Nuclear Medicine with significant respiratory healthcare applications, including surgical planning and regional image analysis. Variability in anatomical structures, the presence of disease-related structural changes, and imaging artifacts complicate automated segmentation. Given the increasing integration of AI into medical imaging, it is essential to benchmark the effectiveness of existing solutions to determine their reliability.

Our in-house algorithm is currently used as an important pre-processing step before further evaluations, such as emphysema quantification and classification. However, recent advancements in AI-based segmentation—such as CNNs (mainly U-Nets)—have resulted in several different models specifically developed for lung lobe segmentation, as well as broader models designed to segment multiple organs and tissues from CT scans. Currently, the comparative performance of these models remains unclear due to variations in dataset availability, annotation standards, and evaluation methodologies.

This project will provide valuable insights into the effectiveness of state-of-the-art lung lobe segmentation models while ensuring that our in-house methodologies remain competitive and clinically applicable. Depending on the student’s interests, duration, and initial findings, the project can be adapted to focus more on model development/improvement, dataset enhancement, or clinical impact assessment.

## Objectives / Aims / Goals

**Primary Objective**:  
Evaluate the performance of recent open-source algorithms for lung lobe segmentation (e.g., TotalSegmentator, dedicated narrow AIs) and compare them to our in-house lobe segmentation algorithm.

**Further goals** (depending on project scope, student interests, literature findings, and initial conclusions):
- Develop a dataset for evaluation of the models
- Develop an improved lung lobe segmentation algorithm
- (Re)train models on diverse and/or more challenging datasets
- Analyze the impact of pathologies (e.g., emphysema, ILD) and structural changes (e.g., lobectomy) on segmentation performance
- Conduct subgroup analyses to assess segmentation performance across different patient populations
- Ensure all model outputs can be integrated into our AI pipelines
- Evaluate the impact of segmentation quality on downstream AI applications (e.g., emphysema quantification, lung functioning on lobe level (Luuk Boulogne), lung nodule localization, and other lung AI tasks)

## Tasks

- Evaluate recent open-source algorithms for lobe segmentation (i.e., TotalSegmentator) and our in-house lobe segmentation algorithm

## Requirements

- Master students with a major in computer science, mathematics, biomedical engineering, artificial intelligence, physics, or a related area in the final stage of master's studies are invited to apply
- Experience with programming in Python
- Experience in deep learning, medical imaging, and/or medical image analysis

## Practical Information

- **Project Duration**: 6 months (MSc Thesis)
- **Location**: Department of Medical Imaging, Radboud University Medical Center, Nijmegen
- For more information, please contact [member/Lisa-Klok] or [member/colin-jacobs].

## Suggested Reading

- W. Xie, C. Jacobs, J.-P. Charbonnier and B. van Ginneken, "Relational Modeling for Robust and Efficient Pulmonary Lobe Segmentation in CT Scans," *IEEE Transactions on Medical Imaging*, vol. 39, no. 8, pp. 2664–2675, Aug. 2020. doi: [10.1109/TMI.2020.2995108](https://doi.org/10.1109/TMI.2020.2995108)

- Doel, T., Gavaghan, D. J., & Grau, V. (2015). Review of automatic pulmonary lobe segmentation methods from CT. *Computerized Medical Imaging and Graphics*, 40, 13–29. https://doi.org/10.1016/j.compmedimag.2014.10.008
