title: Automatic classification of retinal vessels into arteries and veins
authors: M. Niemeijer, B. van Ginneken and M.D. Abràmoff
has_pdf: True
template: publication
bibkey: niem09c
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 7260 of SPIE, 2009, pages 72601F1-72601F8
doi: https://doi.org/10.1117/12.813826
Separating the retinal vascular tree into arteries and veins is important for quantifying vessel changes that preferentially affect either the veins or the arteries. For example the ratio of arterial to venous diameter, the retinal a/v ratio, is well established to be predictive of stroke and other cardiovascular events in adults, as well as the staging of retinopathy of prematurity in premature infants. This work presents a supervised, automatic method that can determine whether a vessel is an artery or a vein based on intensity and derivative information. After thinning of the vessel segmentation, vessel crossing and bifurcation points are removed leaving a set of vessel segments containing centerline pixels. A set of features is extracted from each centerline pixel and using these each is assigned a soft label indicating the likelihood that it is part of a vein. As all centerline pixels in a connected segment should be the same type we average the soft labels and assign this average label to each centerline pixel in the segment. We train and test the algorithm using the data (40 color fundus photographs) from the DRIVE database1 with an enhanced reference standard. In the enhanced reference standard a fellowship trained retinal specialist (MDA) labeled all vessels for which it was possible to visually determine whether it was a vein or an artery. After applying the proposed method to the 20 images of the DRIVE test set we obtained an area under the receiver operator characteristic (ROC) curve of 0.88 for correctly assigning centerline pixels to either the vein or artery classes.

