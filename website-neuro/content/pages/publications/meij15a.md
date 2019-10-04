title: The evaluation of multi-structure, multi-atlas pelvic anatomy features in a prostate MR Lymphography CAD system
authors: M. Meijs, O.A. Debats and H.J. Huisman
has_pdf: True
template: publication
bibkey: meij15a
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 9414 of SPIE, 2015, pages 94140T
doi: https://doi.org/10.1117/12.2082708
In prostate cancer, the detection of metastatic lymph nodes indicates progression from localized disease to metastasized cancer. The detection of positive lymph nodes is, however, a complex and time consuming task for experienced radiologists. Assistance of a two-stage Computer-Aided Detection (CAD) system in MR Lymphography (MRL) is not yet feasible due to the large number of false positives in the first stage of the system. By introducing a multi-structure, multi-atlas segmentation, using an affine transformation followed by a B-spline transformation for registration, the organ location is given by a mean density probability map. The atlas segmentation is semi-automatically drawn with ITK-SNAP, using Active Contour Segmentation. Each anatomic structure is identified by a label number. Registration is performed using Elastix, using Mutual Information and an Adaptive Stochastic Gradient optimization. The dataset consists of the MRL scans of ten patients, with lymph nodes manually annotated in consensus by two expert readers. The feature map of the CAD system consists of the Multi-Atlas and various other features (e.g. Normalized Intensity and multi-scale Blobness). The voxel-based Gentleboost classifier is evaluated using ROC analysis with cross validation. We show in a set of 10 studies that adding multi-structure, multi-atlas anatomical structure likelihood features improves the quality of the lymph node voxel likelihood map. Multiple structure anatomy maps may thus make MRL CAD more feasible.

