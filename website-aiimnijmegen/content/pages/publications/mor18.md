title: Deep learning framework for digital breast tomosynthesis reconstruction
authors: N. Moriakov, K. Michielsen, R. Mann, J. Adler, I. Sechopolous and J. Teuwen
has_pdf: True
template: publication
bibkey: mor18
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, 2019
arxiv: https://arxiv.org/abs/1808.04640
Digital breast tomosynthesis is rapidly replacing digital mammography as the basic x-ray technique for evaluation of the breasts. However, the sparse sampling and limited angular range gives rise to dierent artifacts, which manufacturers try to solve in several ways. In this study we propose an extension of the Learned Primal-Dual algorithm for digital breast tomosynthesis. The Learned Primal-Dual algorithm is a deep neural network consisting of several `reconstruction blocks', which take in raw sinogram data as the initial input, perform a forward and a backward pass by taking projections and back-projections, and use a convolutional neural network to produce an intermediate reconstruction result which is then improved further by the successive reconstruction block. We extend the architecture by providing breast thickness measurements as a mask to the neural network and allow it to learn how to use this thickness mask. We have trained the algorithm on digital phantoms and the corresponding noise-free/noisy projections, and then tested the algorithm on digital phantoms for varying level of noise. Reconstruction performance of the algorithms was compared visually, using MSE loss and Structural Similarity Index. Results indicate that the proposed algorithm outperforms the baseline iterative reconstruction algorithm in terms of reconstruction quality for both breast edges and internal structures and is robust to noise.

