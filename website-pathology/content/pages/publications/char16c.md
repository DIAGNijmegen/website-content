title: Improving Airway Segmentation in Computed Tomography using Leak Detection with Convolutional Networks
authors: J.P. Charbonnier, E.M. van Rikxoort, A.A.A. Setio, C. Schaefer-Prokop, B. van Ginneken and F. Ciompi
has_pdf: True
template: publication
bibkey: char16c
published_in: Medical Image Analysis
pub_details: <i>Medical Image Analysis</i> 2017;36:52-60
doi: https://doi.org/10.1016/j.media.2016.11.001
urlweb: http://dx.doi.org/10.1016/j.media.2016.11.001
pmid: http://www.ncbi.nlm.nih.gov/pubmed/27842236
We propose a novel method to improve airway segmentation in thoracic computed tomography (CT) by detecting and removing leaks. Leak detection is formulated as a classification problem, in which a convolutional network (ConvNet) is trained in a supervised fashion to perform the classification task. In order to increase the segmented airway tree length, we take advantage of the fact that multiple segmentations can be extracted from a given airway segmentation algorithm by varying the parameters that influence the tree length and the amount of leaks. We propose a strategy in which the combination of these segmentations after removing leaks can increase the airway tree length while limiting the amount of leaks. This strategy therefore largely circumvents the need for parameter fine-tuning of a given airway segmentation algorithm.  The ConvNet was trained and evaluated using a subset of inspiratory thoracic CT scans taken from the COPDGene study. Our method was validated on a separate independent set of the EXACT?09 challenge. We show that our method significantly improves the quality of a given leaky airway segmentation, achieving a higher sensitivity at a low false-positive rate compared to all the state-of-the-art methods that entered in EXACT09, and approaching the performance of the combination of all of them.

