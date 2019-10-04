title: Active shape model segmentation with optimal features
authors: B. van Ginneken, A.F. Frangi, J.J. Staal, B.M. ter Haar Romeny and M.A. Viergever
has_pdf: True
template: publication
bibkey: ginn02
published_in: IEEE Transactions on Medical Imaging
pub_details: <i>IEEE Transactions on Medical Imaging</i> 2002;21:924-933
doi: https://doi.org/10.1109/TMI.2002.803121
pmid: http://www.ncbi.nlm.nih.gov/pubmed/12472265
An active shape model segmentation scheme is presented that is steered by optimal local features, contrary to normalized first order derivative profiles, as in the original formulation [Cootes and Taylor, 1995, 1999, and 2001]. A nonlinear kNN-classifier is used, instead of the linear Mahalanobis distance, to find optimal displacements for landmarks. For each of the landmarks that describe the shape, at each resolution level taken into account during the segmentation optimization procedure, a distinct set of optimal features is determined. The selection of features is automatic, using the training images and sequential feature forward and backward selection. The new approach is tested on synthetic data and in four medical segmentation tasks: segmenting the right and left lung fields in a database of 230 chest radiographs, and segmenting the cerebellum and corpus callosum in a database of 90 slices from MRI brain images. In all cases, the new method produces significantly better results in terms of an overlap error measure (p < 0.001 using a paired T-test) than the original active shape model scheme.

