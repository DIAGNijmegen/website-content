title: Image Level Training and Prediction: Intracranial Hemorrhage Identification in 3D Non-Contrast CT
authors: A. Patel, S.C. van de Leemput, M. Prokop, B. van Ginneken and R. Manniesing
has_pdf: True
template: publication
bibkey: pate19
published_in: IEEE Access
pub_details: <i> IEEE Access </i> 2019;7:92355-92364
doi: https://doi.org/10.1109/ACCESS.2019.2927792
urlweb: https://ieeexplore.ieee.org/document/8758429
Current hardware restrictions pose limitations on the use of convolutional neural networks for medical image analysis. There is a large trade-off between network architecture and input image size. For this reason, identification and classification tasks are commonly approached with patch or region based methods often utilizing only local contextual information during training and at inference. Here, a method is presented for the identification of intracranial hemorrhage (ICH) in three-dimensional (3D) non-contrast computed tomography (CT). The method combines a convolutional neural network and recurrent neural network in the form of bidirectional long short-term memory (LSTM) for ICH identification at image level. A convolutional neural network is trained for the identification of ICH in axial slices. LSTM is used to analyze the sequential information obtained from slice level classifications. The method is trained end-to-end using full high-resolution 3D non-contrast CTs. At inference it produces a binary classification with respect to the presence of ICH. A total of 1554 cranial CTs were used to train and validate the method and a separate dataset of 386 images was used for testing. Quantitative analysis showed an area under receiver operating characteristic curve of 0.96. The average time to classification was approximately 0.5 seconds. classification of whole 3D images is therefore possible without the need for pre-processing.

