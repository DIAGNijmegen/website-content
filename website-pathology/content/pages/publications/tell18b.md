title: Gigapixel Whole-Slide Image Classification Using Unsupervised Image Compression And Contrastive Training
authors: D. Tellez, J. van der Laak and F. Ciompi
has_pdf: True
template: publication
bibkey: tell18b
published_in: Medical Imaging with Deep Learning
pub_details: in: <i>Medical Imaging with Deep Learning</i>, 2018
urlweb: https://openreview.net/forum?id=Hk2YYqssf
We propose a novel two-step methodology for entire whole-slide image (WSI) classification. First, all tissue patches in a WSI are mapped into vector embeddings using an encoder trained in an unsupervised fashion. The spatial arrangement of these embeddings is maintained with respect to the tissue patches, forming a stack of 2D feature maps representing the WSI. Second, a convolutional neural network is trained on these compact representations to predict weak labels associated with entire WSIs. We investigated several unsupervised schemes to train the encoder model: convolutional autoencoders (CAE), variational autoencoders (VAE), and a novel approach based on contrastive training. We validated the proposed methodology by predicting the existence of tumor metastasis at WSI-level using the Camelyon16 dataset. Our experimental results showed that the proposed methodology can be used to predict weak labels from entire WSIs. Furthermore, the novel contrastive encoder proved to be superior to the CAE and VAE approaches.

