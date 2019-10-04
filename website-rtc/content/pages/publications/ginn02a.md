title: Automatic detection of abnormalities in chest radiographs using local texture analysis
authors: B. van Ginneken, S. Katsuragawa, B. M. ter Haar Romeny, K. Doi and M. A. Viergever
has_pdf: True
template: publication
bibkey: ginn02a
published_in: IEEE Transactions on Medical Imaging
pub_details: <i>IEEE Transactions on Medical Imaging</i> 2002;21:139-149
doi: https://doi.org/10.1109/42.993132
pmid: http://www.ncbi.nlm.nih.gov/pubmed/11929101
A fully automatic method is presented to detect abnormalities in frontal chest radiographs which are aggregated into an overall abnormality score. The method is aimed at finding abnormal signs of a diffuse textural nature, such as they are encountered in mass chest screening against tuberculosis (TB). The scheme starts with automatic segmentation of the lung fields, using active shape models. The segmentation is used to subdivide the lung fields into overlapping regions of various sizes. Texture features are extracted from each region, using the moments of responses to a multiscale filter bank. Additional "difference features" are obtained by subtracting feature vectors from corresponding regions in the left and right lung fields. A separate training set is constructed for each region. All regions are classified by voting among the k nearest neighbors, with leave-one-out. Next, the classification results of each region are combined, using a weighted multiplier in which regions with higher classification reliability weigh more heavily. This produces an abnormality score for each image. The method is evaluated on two databases. The first database was collected from a TB mass chest screening program, from which 147 images with textural abnormalities and 241 normal images were selected. Although this database contains many subtle abnormalities, the classification has a sensitivity of 0.86 at a specificity of 0.50 and an area under the receiver operating characteristic (ROC) curve of 0.820. The second database consist of 100 normal images and 100 abnormal images with interstitial disease. For this database, the results were a sensitivity of 0.97 at a specificity of 0.90 and an area under the ROC curve of 0.986.

