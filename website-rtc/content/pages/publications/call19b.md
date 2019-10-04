title: FRODO: Free rejection of out-of-distribution samples: application to chest x-ray analysis
authors: E. Calli, K. Murphy, E. Sogancioglu and B. van Ginneken
has_pdf: True
template: publication
bibkey: call19b
published_in: Medical Imaging with Deep Learning
pub_details: in: <i>Medical Imaging with Deep Learning</i>, 2019
urlweb: https://openreview.net/forum?id=H1e7kWD794
In this work, we propose a method to reject out-of-distribution samples which can be adapted to any network architecture and requires no additional training data. Publicly available chest x-ray data (38,353 images) is used to train a standard ResNet-50 model to detect emphysema. Feature activations of intermediate layers are used as descriptors defining the training data distribution. A novel metric, FRODO, is measured by using the Mahalanobis distance of a new test sample to the training data distribution. The method is tested using a held-out test dataset of 21,176 chest x-rays (in-distribution) and a set of 14,821 out-of-distribution x-ray images of incorrect orientation or anatomy. In classifying test samples as in or out-of distribution, our method achieves an AUC score of 0.99.

