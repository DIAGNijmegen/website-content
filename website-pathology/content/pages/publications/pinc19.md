title: High resolution whole prostate biopsy classification using streaming stochastic gradient descent
authors: H. Pinckaers, W. Bulten and G. Litjens
has_pdf: True
template: publication
bibkey: pinc19
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, 2019
doi: https://doi.org/10.1117/12.2512817
Prostate cancer is the most common cancer for men in Western countries, counting 1.1 million new diagnoses every year. The incidence is expected to increase further, due to the growing elderly population. This is leading to a significantly increased workload for pathologists. The burden of this time-consuming and repetitive workload has the potential to be decreased by computational pathology, e.g., by automatically screening prostate biopsies. The current state-of-the-art in many computational pathology tasks use patch-based convolutional neural networks. Developing such algorithms require detailed annotations of the task-specific classes on whole-slide images, which are challenging to create due to low availability of the pathologists. Therefore, it would be beneficial to be able to train using labels the pathologist already provides for regular clinical practice in the form of a report. However, these reports correspond to whole-slide images which are of such a high resolution that current accelerator cards cannot process them at once due to memory constraints. We developed a method, streaming stochastic gradient descent, to train a convolutional neural network end-to-end with entire high resolution images and slide-level labels extracted from pathology reports. Here we trained a neural network on 2812 whole prostate biopsies, at a input size of 8000x8000 pixels, equivalent to 50x total magnification, for a binary classification, cancerous or benign. We achieved an accuracy of 84%. These results show that we may not need expensive annotations to train classification networks in this domain.

