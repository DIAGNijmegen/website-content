title: Segmentation of malignant lesions in 3D breast ultrasound using a depth-dependent model
authors: T. Tan, A. Gubern-Mérida, C. Borelli, R. Manniesing, J. van Zelst, L. Wang, W. Zhang, B. Platel, R.M. Mann and N. Karssemeijer
has_pdf: True
template: publication
bibkey: tan16
published_in: Medical Physics
pub_details: <i>Medical Physics</i> 2016;43(7):4074-4084
doi: https://doi.org/http://dx.doi.org/10.1118/1.4953206
urlweb: http://scitation.aip.org/content/aapm/journal/medphys/43/7/10.1118/1.4953206
pmid: http://www.ncbi.nlm.nih.gov/pubmed/27370126
Purpose Automated 3D breast ultrasound (ABUS) has been proposed as a complementary screening modality to mammography for early detection of breast cancers. To facilitate the interpretation of ABUS images, automated diagnosis and detection techniques are being developed, in which malignant lesion segmentation plays an important role. However, automated segmentation of cancer in ABUS is challenging since lesion edges might not be well defined. In this study, the authors aim at developing an automated segmentation method for malignant lesions in ABUS that is robust to ill-defined cancer edges and posterior shadowing.  Methods: A segmentation method using depth-guided dynamic programming based on spiral scanning is proposed. The method automatically adjusts aggressiveness of the segmentation according to the position of the voxels relative to the lesion center. Segmentation is more aggressive in the upper part of the lesion (close to the transducer) than at the bottom (far away from the transducer), where posterior shadowing is usually visible. The authors used Dice similarity coefficient (Dice) for evaluation. The proposed method is compared to existing state of the art approaches such as graph cut, level set, and smart opening and an existing dynamic programming method without depth dependence.  Results: In a dataset of 78 cancers, our proposed segmentation method achieved a mean Dice of 0.73+-0.14. The method outperforms an existing dynamic programming method (0.70+-0.16) on this task (p = 0.03) and it is also significantly (p < 0.001) better than graph cut (0.66+-0.18), level set based approach (0.63+-0.20) and smart opening (0.65+-0.12).  Conclusions: The proposed depth-guided dynamic programming method achieves accurate breast malignant lesion segmentation results in automated breast ultrasound.

