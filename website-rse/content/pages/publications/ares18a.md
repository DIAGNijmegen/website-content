title: Towards an automatic lung cancer screening system in low dose computed tomography
authors: G. Aresta, T. Araújo, C. Jacobs, B. van Ginneken, A. Cunha, I. Ramos and A. Campilho
has_pdf: True
template: publication
bibkey: ares18a
published_in: MICCAI Workshop: Thoracic Image Analysis
pub_details: in: <i>MICCAI Workshop: Thoracic Image Analysis</i>, volume 11040 of LNCS, 2018
doi: https://doi.org/10.1007/978-3-030-00946-5
We propose a deep learning-based pipeline that, given a low-dose computed tomography of a patient chest, recommends if a patient should be submitted to further medical analysis. The algorithm is composed of a nodule detection block that uses the object detection framework YOLOv2, followed by a U-Net based segmentation. The found structures of interest are then characterized in terms of diameter and texture to produce a final referral recommendation according to the National Lung Screen Trial (NLST) criteria. Our method is trained using the public LUNA16 and LIDC-IDRI datasets and tested on an independent dataset composed of 500 scans from the Kaggle DSB 2017 challenge. The proposed system achieves a patient-wise recall of 89% while providing an explanation to the referral decision and thus may serve as a second opinion tool to speed-up and improve lung cancer screening.

