title: Assessing the Skeletal Age From a Hand Radiograph: Automating the Tanner-Whitehouse Method
authors: M. Niemeijer, B. van Ginneken, C. Maas, F.J. A. Beek and M.A. Viergever
has_pdf: True
template: publication
bibkey: niem03a
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 5032 of SPIE, 2003, pages 1197-1205
doi: https://doi.org/10.1117/12.480163
The skeletal maturity of children is usually assessed from a standard radiograph of the left hand and wrist. An established clinical method to determine the skeletal maturity is the Tanner-Whitehouse (TW2) method. This method divides the skeletal development into several stages (labelled A, B, ...,I). We are developing an automated system based on this method. In this work we focus on assigning a stage to one region of interest (ROI), the middle phalanx of the third finger. We classify each ROI as follows. A number of ROIs which have been assigned a certain stage by a radiologist are used to construct a mean image for that stage. For a new input ROI, landmarks are detected by using an Active Shape Model. These are used to align the mean images with the input image. Subsequently the correlation between each transformed mean stage image and the input is calculated. The input ROI can be assigned to the stage with the highest correlation directly, or the values can be used as features in a classifier. The method was tested on 71 cases ranging from stage E to I. The ROI was staged correctly in 73.2% of all cases and in 97.2% of all incorrectly staged cases the error was not more than one stage.

