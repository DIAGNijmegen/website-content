title: Fovea Detection in Optical Coherence Tomography using Convolutional Neural Networks
authors: B. Liefers, F.G. Venhuizen, T. Theelen, C. Hoyng, B. van Ginneken and C.I. Sánchez
has_pdf: True
template: publication
bibkey: lief17
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 10133 of SPIE, 2017, pages 1013302
doi: https://doi.org/10.1117/12.2254301
The fovea is an important clinical landmark that is used as a reference for assessing various quantitative measures, such as central retinal thickness or drusen count. In this paper we propose a novel method for automatic detection of the foveal center in Optical Coherence Tomography (OCT) scans. Although the clinician will generally aim to center the OCT scan on the fovea, post-acquisition image processing will give a more accurate estimate of the true location of the foveal center. A Convolutional Neural Network (CNN) was trained on a set of 781 OCT scans that classifies each pixel in the OCT B-scan with a probability of belonging to the fovea. Dilated convolutions were used to obtain a large receptive field, while maintaining pixel-level accuracy. In order to train the network more effectively, negative patches were sampled selectively after each epoch. After CNN classification of the entire OCT volume, the predicted foveal center was chosen as the voxel with maximum output probability, after applying an optimized three-dimensional Gaussian blurring. We evaluate the performance of our method on a data set of 99 OCT scans presenting different stages of Age-related Macular Degeneration (AMD). The fovea was correctly detected in 96.9% of the cases, with a mean distance error of 73 +- 112 micro meter. This result was comparable to the performance of a second human observer who obtained a mean distance error of 69 +- 94 micro meter. Experiments showed that the proposed method is accurate and robust even in retinas heavily affected by pathology.

