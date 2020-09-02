title: Streaming CNNs for Multi-Megapixel Images 
date: 2020-08-26
description: Due to memory constraints on current hardware, most convolutional neural networks (CNN) are trained on sub-megapixel images. A novel method for end-to-end training of CNNs on multi-megapixel images was proposed by Hans Pinckaers and his colleagues. Their work appeared online in IEEE Transactions on Pattern Analysis and Machine Intelligence. 
picture: news/StreamingCNN.png
groups: diag, pathology

Due to memory constraints on current hardware, most convolutional neural networks (CNN) are trained on sub-megapixel images. Computer memory becomes a limiting factor because the conventional backpropagation algorithm for optimizing deep neural networks requires the storage of intermediate activations. Since the size of these intermediate activations in a convolutional neural network increases proportionally to the input size of the network, memory quickly fills up with images of multiple megapixels. Hence, most popular datasets in computer vision contain images much less than a megapixel in size. However, in some domains such as medical imaging, multi-megapixel images are needed to identify the presence of disease accurately.

[member/hans-pinckaers] et al. developed a novel method to directly train state-of-the-art convolutional neural networks using any input image size in an end-to-end manner. This method exploits the locality of most operations in modern CNNs by performing the forward and backward pass on smaller tiles of the image. Their work was accepted for publication by [IEEE Transactions on Pattern Analysis and Machine Intelligence](https://ieeexplore.ieee.org/document/9178453). In this work, they showed a proof of concept using images of up to 66-megapixels (`8192x8192`), saving approximately 50GB of memory per image.

Memory demand is typically highest in the first few layers of state-of-the-art CNNs before several pooling layers are applied because the intermediate activation maps are large. These activation maps require much less memory in subsequent layers. They proposed to construct these later activations by _streaming_ the input image through the CNN in a tiled fashion, changing the memory requirement of the CNN to be based on the size of the tile and not the input image. This method allows the processing of input images of any size.

![Streaming CNN Full]({{ IMGURL }}/images/news/StreamingCNN_full.png)

The figure above depicts the schematic overview of streaming in a one-dimensional case, using a 1x3 kernel. A detailed explanation of the algorithm can be found in their [paper](https://ieeexplore.ieee.org/document/9178453).

They improved the AUC from 0.580 on 4-megapixel images to 0.706 on 66-megapixel images for metastasis detection in breast cancer on the [CAMELYON17](https://camelyon17.grand-challenge.org/Data/) dataset.

![Streaming CNN CAMELYON17]({{ IMGURL }}/images/news/StreamingCNN_CAMELYON17.png)
The figure above shows the saliency maps for images of the tuning set of the CAMELYON17 experiment. The highest resolution model, trained on image-level labels shows highlights corresponding to the ground truth pixel-level annotation of a breast cancer metastasis. The lower resolution models have lower probability for the ground truth class and show little correspondence to the location of the metastases.

They also obtained a Spearman correlation metric approaching state-of-the-art performance on the [TUPAC16](http://tupac.tue-image.nl/node/3) dataset, from 0.485 on 1-megapixel images to 0.570 on 16-megapixel images.

![Streaming CNN TUPAC16]({{ IMGURL }}/images/news/StreamingCNN_TUPAC16.png)
The figure above shows the saliency maps for test set images of the TUPAC16 experiment using the best performing models. The TUPAC16 network shows highlights in cell-dense and cancerous regions. There is a trend in which the higher the input solution of the model, the less it focuses on healthy tissue. Also, higher resolution models focus on more locations of the tissue.

The code to reproduce a subset of the experiments is publicly available [here](https://github.com/DIAGNijmegen/StreamingCNN).
