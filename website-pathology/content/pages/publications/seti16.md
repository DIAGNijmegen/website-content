title: Pulmonary nodule detection in CT images: false positive reduction using multi-view convolutional networks
authors: A.A. A. Setio, F. Ciompi, G. Litjens, P. Gerke, C. Jacobs, S. van Riel, M. Winkler Wille, M. Naqibullah, C.I. Sánchez and B. van Ginneken
has_pdf: True
template: publication
bibkey: seti16
published_in: IEEE Transactions on Medical Imaging
pub_details: <i>IEEE Transactions on Medical Imaging</i> 2016;35(5):1160-1169
doi: https://doi.org/10.1109/TMI.2016.2536809
pmid: http://www.ncbi.nlm.nih.gov/pubmed/26955024
We propose a novel Computer-Aided Detection (CAD) system for pulmonary nodules using multi-view convolutional networks (ConvNets), for which discriminative features are automatically learnt from the training data. The network is fed with nodule candidates obtained by combining three candidate detectors specifically designed for solid, subsolid, and large nodules. For each candidate, a set of 2-D patches from differently oriented planes is extracted. The proposed architecture comprises multiple streams of 2-D ConvNets, for which the outputs are combined using a dedicated fusion method to get the final classification. Data augmentation and dropout are applied to avoid overfitting. On 888 scans of the publicly available LIDCIDRI dataset, our method reaches high detection sensitivities of 85.4% and 90.1% at 1 and 4 false positives per scan, respectively. An additional evaluation on independent datasets from the ANODE09 challenge and DLCST is performed. We showed that the proposed multi-view ConvNets is highly suited to be used for false positive reduction of a CAD system.

