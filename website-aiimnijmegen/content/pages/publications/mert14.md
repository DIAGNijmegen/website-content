title: MRI to X-ray mammography intensity-based registration with simultaneous optimisation of pose and biomechanical transformation parameters
authors: T. Mertzanidou, J. Hipwell, S. Johnsen, L. Han, B. Eiben, Z. Taylor, S. Ourselin, H. Huisman, R. Mann, U. Bick, N. Karssemeijer and D. Hawkes
has_pdf: True
template: publication
bibkey: mert14
published_in: Medical Image Analysis
pub_details: <i>Medical Image Analysis</i> 2014;18:674-683
doi: https://doi.org/10.1016/j.media.2014.03.003
pmid: http://www.ncbi.nlm.nih.gov/pubmed/24727358
Determining corresponding regions between an MRI and an X-ray mammogram is a clinically useful task that is challenging for radiologists due to the large deformation that the breast undergoes between the two image acquisitions. In this work we propose an intensity-based image registration framework, where the biomechanical transformation model parameters and the rigid-body transformation parameters are optimised simultaneously. Patient-specific biomechanical modelling of the breast derived from diagnostic, prone MRI has been previously used for this task. However, the high computational time associated with breast compression simulation using commercial packages, did not allow the optimisation of both pose and FEM parameters in the same framework. We use a fast explicit Finite Element (FE) solver that runs on a graphics card, enabling the FEM-based transformation model to be fully integrated into the optimisation scheme. The transformation model has seven degrees of freedom, which include parameters for both the initial rigid-body pose of the breast prior to mammographic compression, and those of the biomechanical model. The framework was tested on ten clinical cases and the results were compared against an affine transformation model, previously proposed for the same task. The mean registration error was 11.6Ã‚Â±3.8mm for the CC and 11Ã‚Â±5.4mm for the MLO view registrations, indicating that this could be a useful clinical tool.

