title: Handling label noise through model confidence and uncertainty: application to chest radiograph classification
authors: E. Calli, E. Sogancioglu, E. Th. Scholten, K. Murphy and B. van Ginneken
has_pdf: True
template: publication
bibkey: call19
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, 2019
doi: https://doi.org/10.1117/12.2514290
In this work we analyze the eect of label noise in training and test data when performing classication experi- ments on chest radiographs (CXRs) with modern deep learning architectures. We use ChestXRay14, the largest publicly available CXR dataset. We simulate situs inversus by horizontal ipping of the CXRs, allowing us to precisely control the amount of label noise. We also perform experiments in classifying emphysema using the ChestXRay14 provided labels that are known to be noisy. Our situs inversus experiments conrm results from the computer vision literature that deep learning architectures are relatively robust but not completely insensi- tive to label noise in the training data: without or with very low noise, classication results are near perfect; 16% and 32% training label noise only lead to a 1.5% and 4.6% drop in accuracy. We investigate two metrics that could be used to identify test samples that have an incorrect label: model condence and model uncertainty. We show, in an observer study with an experienced chest radiologist, that both measures are eective in identifying samples in ChestXRay14 that are erroneously labeled for the presence of emphysema.

