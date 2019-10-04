title: Ridge Based Vessel Segmentation in Color Images of the Retina
authors: J. J. Staal, M. D. Abràmoff, M. Niemeijer, M. A. Viergever and B. van Ginneken
has_pdf: True
template: publication
bibkey: staa04a
published_in: IEEE Transactions on Medical Imaging
pub_details: <i>IEEE Transactions on Medical Imaging</i> 2004;23(4):501-509
doi: https://doi.org/10.1109/TMI.2004.825627
pmid: http://www.ncbi.nlm.nih.gov/pubmed/15084075
A method is presented for automated segmentation of vessels in two-dimensional color images of the retina. This method can be used in computer analyses of retinal images, e.g., in automated screening for diabetic retinopathy. The system is based on extraction of image ridges, which coincide approximately with vessel centerlines. The ridges are used to compose primitives in the form of line elements. With the line elements an image is partitioned into patches by assigning each image pixel to the closest line element. Every line element constitutes a local coordinate frame for its corresponding patch. For every pixel, feature vectors are computed that make use of properties of the patches and the line elements. The feature vectors are classified using a kappaNN-classifier and sequential forward feature selection. The algorithm was tested on a database consisting of 40 manually labeled images. The method achieves an area under the receiver operating characteristic curve of 0.952. The method is compared with two recently published rule-based methods of Hoover et al. and Jiang et al. The results show that our method is significantly better than the two rule-based methods (p < 0.01). The accuracy of our method is 0.944 versus 0.947 for a second observer.

