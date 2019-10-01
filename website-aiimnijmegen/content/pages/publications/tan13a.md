title: Computer-aided Detection of Cancer in Automated 3D Breast Ultrasound
authors: T. Tan, B. Platel, R. Mus, L. Tabar, R. Mann and N. Karssemeijer
has_pdf: True
template: publication
bibkey: tan13a
published_in: IEEE Transactions on Medical Imaging
pub_details: <i>IEEE Transactions on Medical Imaging</i> 2013;32:1698-1706
doi: https://doi.org/10.1109/TMI.2013.2263389
pmid: http://www.ncbi.nlm.nih.gov/pubmed/23693128
Automated 3D breast ultrasound (ABUS) has gained a lot of interest and may become widely used in screening of dense breasts, where sensitivity of mammography is poor. However, reading ABUS images is time consuming, and subtle abnormalities may be missed. Therefore, we are developing a computer aided detection (CAD) system to help reduce reading time and prevent errors. In the multi-stage system we propose, segmentations of the breast, the nipple and the chestwall are performed, providing landmarks for the detection algorithm. Subsequently, voxel features characterizing coronal spiculation patterns, blobness, contrast, and depth are extracted. Using an ensemble of neuralnetwork classifiers, a likelihood map indicating potential abnormality is computed. Local maxima in the likelihood map are determined and form a set of candidates in each image. These candidates are further processed in a second detection stage, which includes region segmentation, feature extraction and a final classification. On region level, classification experiments were performed using different classifiers including an ensemble of neural networks, a support vector machine, a k-nearest neighbors, a linear discriminant, and a gentle boost classifier. Performance was determined using a dataset of 238 patients with 348 images (views), including 169 malignant and 154 benign lesions. Using free response receiver operating characteristic (FROC) analysis, the system obtains a view-based sensitivity of 64\% at 1 false positives per image using an ensemble of neuralnetwork classifiers.

