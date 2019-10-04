title: Iterative fully convolutional neural networks for automatic vertebra segmentation
authors: N. Lessmann, B. van Ginneken, P.A. de Jong and I. Išgum
has_pdf: False
template: publication
bibkey: less18a
published_in: Medical Imaging with Deep Learning
pub_details: in: <i>Medical Imaging with Deep Learning</i>, 2018
arxiv: https://arxiv.org/abs/1804.04383
Precise segmentation of the vertebrae is often required for automatic detection of vertebral abnormalities. This especially enables incidental detection of abnormalities such as compression fractures in images that were acquired for other diagnostic purposes. While many CT and MR scans of the chest and abdomen cover a section of the spine, they often do not cover the entire spine. Additionally, the first and last visible vertebrae are likely only partially included in such scans. In this paper, we therefore approach vertebra segmentation as an instance segmentation problem. A fully convolutional neural network is combined with an instance memory that retains information about already segmented vertebrae. This network iteratively analyzes image patches, using the instance memory to search for and segment the first not yet segmented vertebra. At the same time, each vertebra is classified as completely or partially visible, so that partially visible vertebrae can be excluded from further analyses. We evaluated this method on spine CT scans from a vertebra segmentation challenge and on low-dose chest CT scans. The method achieved an average Dice score of 95.8% and 92.1%, respectively, and a mean absolute surface distance of 0.194 mm and 0.344 mm.

