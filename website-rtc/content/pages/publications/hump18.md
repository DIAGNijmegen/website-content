title: Efficient organ localization using multi-label convolutional neural networks in thorax-abdomen CT scans
authors: G.E. Humpire Mamani, A. Setio, B. van Ginneken and C. Jacobs
has_pdf: True
template: publication
bibkey: hump18
published_in: Physics in Medicine and Biology
pub_details: <i>Physics in Medicine and Biology</i> 2018;63(8):085003
doi: https://doi.org/10.1088/1361-6560/aab4b3
urlweb: http://iopscience.iop.org/article/10.1088/1361-6560/aab4b3
pmid: http://www.ncbi.nlm.nih.gov/pubmed/29512516
Automatic localization of organs and other structures in medical images is an important preprocessing step that can improve and speed up other algorithms such as organ segmentation, lesion detection, and registration. This work presents an efficient method for simultaneous localization of multiple structures in 3D thorax-abdomen CT scans. Our approach predicts the location of multiple structures using a single multi-label convolutional neural network for each orthogonal view. Each network takes extra slices around the current slice as input to provide extra context. A sigmoid layer is used to perform multi-label classification. The output of the three networks is subsequently combined to compute a 3D bounding box for each structure. We used our approach to locate 11 structures of interest. The neural network was trained and evaluated on a large set of 1884 thorax-abdomen CT scans from patients undergoing oncological workup. Reference bounding boxes were annotated by human observers. The performance of our method was evaluated by computing the wall distance to the reference bounding boxes. The bounding boxes annotated by the first human observer were used as the reference standard for the test set. Using the best configuration, we obtained an average wall distance of 3.20±7.33mm in the test set. The second human observer achieved 1.23±3.39mm. For all structures, the results were better than those reported in previously published studies. In conclusion, we proposed an efficient method for the accurate localization of multiple organs. Our method uses multiple slices as input to provide more context around the slice under analysis, and we have shown that this improves performance. This method can easily be adapted to handle more organs.

