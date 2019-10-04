title: Training convolutional neural networks with megapixel images
authors: H. Pinckaers and G. Litjens
has_pdf: True
template: publication
bibkey: pinc18
published_in: Medical Imaging with Deep Learning
pub_details: in: <i>Medical Imaging with Deep Learning</i>, 2018
arxiv: https://arxiv.org/abs/1804.05712
To train deep convolutional neural networks, the input data and the intermediate activations need to be kept in memory to calculate the gradient descent step. Given the limited memory available in the current generation accelerator cards, this limits the maximum dimensions of the input data. We demonstrate a method to train convolutional neural networks holding only parts of the image in memory while giving equivalent results. We quantitatively compare this new way of training convolutional neural networks with conventional training. In addition, as a proof of concept, we train a convolutional neural network with 64 megapixel images, which requires 97% less memory than the conventional approach.

