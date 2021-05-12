title: Neural Image Compression
template: project-single
picture: software/neural_image_compression.png
description: Neural image compression for gigapixel histopathology image analysis.
groups: pathology
people: David Tellez, Geert Litjens, Jeroen van der Laak, Francesco Ciompi
bibkeys: Tell19
github: https://github.com/davidtellez/neural-image-compression

<figure class="figure my-4">
  <img data-src="/images/software/nic_pipeline.png" class="figure-img img-fluid lazyload" alt="Overview of the neural image compression pipeline.">
  <figcaption class="figure-caption">Overview of the neural image compression pipeline</figcaption>
</figure>

<a href="https://github.com/davidtellez/neural-image-compression" class="btn btn-secondary"><svg class="svg-icon svg-icon-github"><use xlink:href="#icon-github"></use></svg> View on Github</a>

We propose **Neural Image Compression (NIC)**, a two-step method to build convolutional neural networks (CNNs) for gigapixel image analysis solely using weak image-level labels. First, gigapixel images are compressed using a neural network trained in an unsupervised fashion, retaining high-level information while suppressing pixel-level noise. Second, a CNN is trained on these compressed image representations to predict image-level labels, avoiding the need for fine-grained manual annotations. A full description of our method can be found in the journal paper [Neural Image Compression for Gigapixel Histopathology Image Analysis](https://doi.org/10.1109/TPAMI.2019.2936841) and Arxiv [link](https://arxiv.org/abs/1811.02840).

