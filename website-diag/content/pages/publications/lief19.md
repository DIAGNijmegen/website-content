title: Dense Segmentation in Selected Dimensions: Application to Retinal Optical Coherence Tomography
authors: B. Liefers, C. González-Gonzalo, C. Klaver, B. van Ginneken and C.I. Sánchez
has_pdf: True
template: publication
bibkey: lief19
published_in: Medical Imaging with Deep Learning
pub_details: in: <i>Medical Imaging with Deep Learning</i>, volume 102 of Proceedings of Machine Learning Research, 2019, pages 337-346
urlweb: http://proceedings.mlr.press/v102/liefers19a.html
We present a novel convolutional neural network architecture designed for dense segmentation  in  a  subset  of  the  dimensions  of  the  input  data.   The  architecture  takes  an N-dimensional image as input, and produces a label for every pixel in M output dimensions, where 0< M < N.  Large context is incorporated by an encoder-decoder structure, while funneling shortcut subnetworks provide precise localization.  We demonstrate applicability of the architecture on two problems in retinal optical coherence tomography:  segmentation of geographic atrophy and segmentation of retinal layers.  Performance is compared against two baseline methods, that leave out either the encoder-decoder structure or the shortcut subnetworks.  For segmentation of geographic atrophy, an average Dice score of 0.49±0.21 was obtained, compared to 0.46±0.22 and 0.28±0.19 for the baseline methods, respectively. For the layer-segmentation task, the proposed architecture achieved a mean absolute error of 1.305±0.547 pixels compared to 1.967±0.841 and 2.166±0.886 for the baseline methods.

