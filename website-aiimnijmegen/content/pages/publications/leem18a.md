title: MemCNN: a Framework for Developing Memory Efficient Deep Invertible Networks
authors: S. C. van de Leemput, J. Teuwen and R. Manniesing
has_pdf: True
template: publication
bibkey: leem18a
published_in: International Conference on Learning Representations
pub_details: in: <i>International Conference on Learning Representations</i>, 2018
urlweb: https://openreview.net/forum?id=r1KzqK1wz
Reversible operations have recently been successfully applied to classification problems to reduce memory requirements during neural network training. This feature is accomplished by removing the need to store the input activation for computing the gradients at the backward pass and instead reconstruct them on demand. However, current approaches rely on custom implementations of backpropagation, which limits applicability and extendibility. We present MemCNN, a novel PyTorch framework which simplifies the application of reversible functions by removing the need for a customized backpropagation. The framework contains a set of practical generalized tools, which can wrap common operations like convolutions and batch normalization and which take care of the memory management. We validate the presented framework by reproducing state-of-the-art experiments comparing classification accuracy and training time on Cifar-10 and Cifar-100 with the existing state-of-the-art, achieving similar classification accuracy and faster training times.

