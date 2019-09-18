title: Full Volumetric Brain Tissue Segmentation in Non-contrast CT using Memory Efficient Convolutional LSTMs
authors: S. C. van de Leemput, A. Patel and R. Manniesing
has_pdf: True
template: publication
bibkey: leem18c
published_in: Medical Imaging meets NeurIPS
pub_details: in: <i>Medical Imaging meets NeurIPS</i>, 2018
urlweb: https://openreview.net/pdf?id=rJxlLGBElN
There is a demand for deep learning approaches able to process high resolution 3D volumes in an accurate and fast way. However, training of these models is often limited by the available GPU memory, which often results in reduced model depth, receptive field, and input size, limiting the expressiveness of the model. In this work we present a memory efficient modified convolutional-LSTM, which integrates a context-rich 2D U-Net as an input in a slice based manner and subsequently integrates the acquired slices using LSTM to create the full 3D context. Memory savings achieved by checkpointing on one or more steps within the LSTM allow for direct training on a single full non-contrast CT volume of: 512 x 512 x 320 on a NVIDIA Titan X with 12 GB of VRAM. We demonstrate the effectiveness of our method by training and segmenting the cranial cavity including soft-brain tissue and CSF in the non-contrast CT end-to-end on the full image data, without any stitching, while preserving a large receptive field and high expressiveness.

