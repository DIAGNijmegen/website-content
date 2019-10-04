title: Segmentation of the outer vessel wall of the common carotid artery in CTA
authors: D. Vukadinovic, T. van Walsum, R. Manniesing, S. Rozie, R. Hameeteman, T. T de Weert, A. van der Lugt and W. J Niessen
has_pdf: True
template: publication
bibkey: vuka10
published_in: IEEE Transactions on Medical Imaging
pub_details: <i>IEEE Transactions on Medical Imaging</i> 2010;29:65-76
doi: https://doi.org/10.1109/TMI.2009.2025702
pmid: http://www.ncbi.nlm.nih.gov/pubmed/19556191
A novel method is presented for carotid artery vessel wall segmentation in computed tomography angiography (CTA) data. First the carotid lumen is semi-automatically segmented using a level set approach initialized with three seed points. Subsequently, calcium regions located within the vessel wall are automatically detected and classified using multiple features in a GentleBoost framework. Calcium regions segmentation is used to improve localization of the outer vessel wall because it is an easier task than direct outer vessel wall segmentation. In a third step, pixels outside the lumen area are classified as vessel wall or background, using the same GentleBoost framework with a different set of image features. Finally, a 2-D ellipse shape deformable model is fitted to a cost image derived from both the calcium and vessel wall classifications. The method has been validated on a dataset of 60 CTA images. The experimental results show that the accuracy of the method is comparable to the interobserver variability.

