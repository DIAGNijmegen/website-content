title: Automatic detection of spiculation of pulmonary nodules in Computed Tomography images
authors: F. Ciompi, C. Jacobs, E. Th Scholten, S. van Riel, M.M. W. Wille, M. Prokop and B. van Ginneken
has_pdf: True
template: publication
bibkey: ciom15
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 9414 of SPIE, 2015
doi: https://doi.org/10.1117/12.2081426
We present a fully automatic method for the assessment of spiculation of pulmonary nodules in low-dose Com- puted Tomography (CT) images. Spiculation is considered as one of the indicators of nodule malignancy and an important feature to assess in order to decide on a patient-tailored follow-up procedure. For this reason, lung cancer screening scenario would bene t from the presence of a fully automatic system for the assessment of spiculation. The presented framework relies on the fact that spiculated nodules mainly di er from non-spiculated ones in their morphology. In order to discriminate the two categories, information on morphology is captured by sampling intensity pro les along circular patterns on spherical surfaces centred on the nodule, in a multi-scale fashion. Each intensity pro le is interpreted as a periodic signal, where the Fourier transform is applied, obtain- ing a spectrum. A library of spectra is created by clustering data via unsupervised learning. The centroids of the clusters are used to label back each spectrum in the sampling pattern. A compact descriptor encoding the nodule morphology is obtained as the histogram of labels along all the spherical surfaces and used to classify spiculated nodules via supervised learning. We tested our approach on a set of nodules from the Danish Lung Cancer Screening Trial (DLCST) dataset. Our results show that the proposed method outperforms other 3-D descriptors of morphology in the automatic assessment of spiculation.

