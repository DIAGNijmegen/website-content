title: Skeletonization for re-initialization in level set-based vascular tree segmentation
authors: R. Manniesing, B.K. Velthuis, M. van Leeuwen and W.J. Niessen
has_pdf: True
template: publication
bibkey: mann04b
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 5370 of SPIE, 2004, pages 506-514
doi: https://doi.org/10.1117/12.533045
An extension to level set based segmentation is proposed for vascular tree delineation. The method starts with topology extraction, by a shape constrained level set evolution steered by a strictly positive, image base speed function to ensure some oversegmentation. Next, the skeleton of the resulting oversegmentation is determined, which then is used to initialise another level set steered by a speed function with both negative and positive speed forces based on image features, to obtain a most accurate segmentation. The novelty of our approach lies in the shape constraint that is imposed implicitly on the first level set evolution. We apply repeatedly re-initializations of this evolution with a topology preserving skeleton of the current zero level set. We compare this method with a plain level set evolution steered by the same full range speed function. Both are initialised by placing a single seed point at the root of the vessel tree. Pilot experiments on twelve multislice CT data sets of the Circle of Willis show that our method is capable of segmenting the smaller branches at the distal part of the vessel tree structures and has the potential to segment vessels which are distal to a severe stenosis or occlusion.

