title: Learning from sparsely annotated data for semantic segmentation in histopathology images
template: presentation-single
picture: posters/JMB_MIDL_2019_poster.JPG 
arxiv: http://proceedings.mlr.press/v102/bokhorst19a.html
author_list: John-Melle Bokhorst, Hans Pinckaers, Peter van Zwam, Iris Nagtegaal, Jeroen van der Laak, Francesco Ciompi
groups: pathology

We investigate the problem of building convolutional networks for semantic segmentation in histopathology images when weak supervision in the form of sparse manual annotations is provided in the training set. We propose to address this problem by modifying the loss function in order to balance the contribution of each pixel of the input data. We introduce and compare two approaches of loss balancing when sparse annotations are provided, namely (1) instance based balancing and (2) mini-batch based balancing. We also consider a scenario of full supervision in the form of dense annotations, and compare the performance of using either sparse or dense annotations with the proposed balancing schemes. Finally, we show that using a bulk of sparse annotations and a small fraction of dense annotations allows to achieve performance comparable to full supervision.
