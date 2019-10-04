title: Shape Constrained Vessel Centerline Extraction by Integrating Surface Evolution and Topology Analysis
authors: R. Manniesing and W.J. Niessen
has_pdf: True
template: publication
bibkey: mann06
published_in: IEEE International Symposium on Biomedical Imaging
pub_details: in: <i>IEEE International Symposium on Biomedical Imaging</i>, 2006, pages 165-168
doi: https://doi.org/10.1109/ISBI.2006.1624878
A novel approach for vessel axis tracking is presented based on surface evolution in 3D. The main idea is to guide the evolution by analyzing the topology of intermediate segmentation results, and in particular, to impose shape constraints on the topology. For example, the topology can be constrained to represent a bifurcation, which can be imposed by extracting three different connected paths with maximum length from the skeleton of intermediate segmentation results. The evolving surface is then re-initialized with the newly found topology. Re-initialization is a crucial step since it creates probing behavior of the evolving front and prevents the surface from leaking into the background. The method was evaluated in two CTA applications (i) extracting the internal carotid arteries including the region in which they traverse through the skull base, which is challenging due to the close proximity of bone structures and overlap in intensity values, and (ii) extracting the carotid bifurcation, some of them severely stenosed and most of them containing calcifications. Using only the image gradient as the image force in the surface evolution and a single seed point as initialization, the method was successful in 80% of ten internal carotids in five patients, and 80% of ten carotid bifurcations in five patients, respectively

