title: Fast Convolutional Neural Network Training Using Selective Data Sampling: Application to Hemorrhage Detection in Color Fundus Images
authors: M.J. J. P. van Grinsven, B. van Ginneken, C.B. Hoyng, T. Theelen and C.I. Sánchez.
has_pdf: True
template: publication
bibkey: grin16b
published_in: IEEE Transactions on Medical Imaging
pub_details: <i>IEEE Transactions on Medical Imaging</i> 2016;35(5):1273-1284
doi: https://doi.org/10.1109/TMI.2016.2526689
pmid: http://www.ncbi.nlm.nih.gov/pubmed/26886969
Convolutional neural networks (CNNs) are deep learning network architectures that have pushed forward the state-of-the-art in a range of computer vision applications and are increasingly popular in medical image analysis. However, training of CNNs is time-consuming and challenging. In medical image analysis tasks, the majority of training examples are easy to classify and therefore contribute little to the CNN learning process. In this paper, we propose a method to improve and speed-up the CNN training for medical image analysis tasks by dynamically selecting misclassified negative samples during training. Training samples are heuristically sampled based on classification by the current status of the CNN. Weights are assigned to the training samples and informative samples are more likely to be included in the next CNN training iteration. We evaluated and compared our proposed method by training a CNN with (SeS) and without (NSeS) the selective sampling method. We focus on the detection of hemorrhages in color fundus images. A decreased training time from 170 epochs to 60 epochs with an increased performance Ã¢â‚¬â€œ on par with two human experts Ã¢â‚¬â€œ was achieved with areas under the receiver operating characteristics curve of 0.894 and 0.972 on two data sets. The SeS CNN statistically outperformed the NSeS CNN on an independent test set.

