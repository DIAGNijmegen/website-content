title: Automatic segmentation of prostate zones
authors: G. Mooij, I. Bagulho and H. Huisman
has_pdf: False
template: publication
bibkey: mooi18
published_in: arXiv:1806.07146
pub_details: <i>arXiv:1806.07146</i> 2018
arxiv: https://arxiv.org/abs/1806.07146
Convolutional networks have become state-of-the-art techniques for automatic medical image analysis, with the U-net architecture being the most popular at this moment. In this article we report the application of a 3D version of U-net to the automatic segmentation of prostate peripheral and transition zones in 3D MRI images. Our results are slightly better than recent studies that used 2D U-net and handcrafted feature approaches. In addition, we test ideas for improving the 3D U-net setup, by 1) letting the network segment surrounding tissues, making use of the fixed anatomy, and 2) adjusting the network architecture to reflect the anisotropy in the dimensions of the MRI image volumes. While the latter adjustment gave a marginal improvement, the former adjustment showed a significant deterioration of the network performance. We were able to explain this deterioration by inspecting feature map activations in all layers of the network. We show that to segment more tissues the network replaces feature maps that were dedicated to detecting prostate peripheral zones, by feature maps detecting the surrounding tissues.

