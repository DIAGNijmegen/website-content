title: Iterative convolutional neural networks for automatic vertebra identification and segmentation in CT images
authors: N. Lessmann, B. van Ginneken and I. Išgum
has_pdf: True
template: publication
bibkey: less18
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 10574 of SPIE, 2018
doi: https://doi.org/10.1117/12.2292731
Segmentation and labeling of the vertebrae in CT images are important steps for automatic analysis of the spine. This paper presents an automatic method based on iterative convolutional neural networks. These utilize the inherent order of the vertebral column to simplify the detection problem, so that the network can be trained with as little as ten manual reference segmentations. Vertebrae are identified and segmented individually in sequential order, first in low-resolution images that enable the analysis of context information, and afterwards in the original high-resolution images to obtain a fine segmentation. The method was trained and evaluated with 15 spine CT scans from the MICCAI CSI 2014 workshop challenge. These scans cover the whole thoracic and lumbar part of the spine of healthy young adults. In contrast to a non-iterative convolutional neural network, the proposed method correctly identified all vertebrae. Our method achieved a mean Dice coefficient of 0.948 and a mean surface distance of 0.29 mm and thus outperforms the best method that participated in the original challenge.

