title: Dealing with Label Scarcity in Computational Pathology: A Use Case in Prostate Cancer Classification
template: presentation-single
picture: posters/midl_2019_poster_dercksen19.png
arxiv: https://arxiv.org/abs/1905.06820
author_list: Koen Dercksen, Wouter Bulten, Geert Litjens
groups: pathology

Large amounts of unlabelled data are commonplace for many applications in computational pathology, whereas labelled data is often expensive, both in time and cost, to acquire. We investigate the performance of unsupervised and supervised deep learning methods when few labelled data are available. Three methods are compared: clustering autoencoder latent vectors (unsupervised), a single layer classifier combined with a pre-trained autoencoder (semi-supervised), and a supervised CNN. We apply these methods on hematoxylin and eosin (H&E) stained prostatectomy images to classify tumour versus non-tumour tissue. Results show that semi-/unsupervised methods have an advantage over supervised learning when few labels are available. Additionally, we show that incorporating immunohistochemistry (IHC) stained data provides an increase in performance over only using H&E.
