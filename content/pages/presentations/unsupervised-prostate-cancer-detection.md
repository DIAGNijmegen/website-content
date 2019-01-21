title: Unsupervised Prostate Cancer Detection on H&E using Convolutional Adversarial Autoencoders
template: presentation-single
picture_overview: posters/unsupervised_pca.png
picture_large: posters/unsupervised_pca_large.png
arxiv: https://arxiv.org/abs/1804.07098
author_list: Wouter Bulten, Geert Litjens

We propose an unsupervised method using self-clustering convolutional adversarial autoencoders to classify prostate tissue as tumor or non-tumor without any labeled training data. The clustering method is integrated into the training of the autoencoder and requires only little post-processing. Our network trains on hematoxylin and eosin (H&E) input patches and we tested two different reconstruction targets, H&E and immunohistochemistry (IHC). We show that antibody-driven feature learning using IHC helps the network to learn relevant features for the clustering task. Our network achieves a F1 score of 0.62 using only a small set of validation labels to assign classes to clusters.
