title: On Combining Algorithms for Deformable Image Registration
authors: S.E. A. Muenzing, B. van Ginneken and J.P. W. Pluim
has_pdf: True
template: publication
bibkey: muen12
published_in: Biomedical Image Registration
pub_details: in: <i>Biomedical Image Registration</i>, 2012, pages 256-265
doi: https://doi.org/10.1007/978-3-642-31340-0_27
We propose a meta-algorithm for registration improvement by combining deformable image registrations (MetaReg). It is inspired by a well-established method from machine learning, the combination of classifiers. MetaReg consists of two main components: (1) A strategy for composing an improved registration by combining deformation fields from different registration algorithms. (2) A method for regularization of deformation fields post registration (UnfoldReg). In order to compare and combine different registrations, MetaReg utilizes a landmark-based classifier for assessment of local registration quality. We present preliminary results of MetaReg, evaluated on five CT pulmonary breathhold inspiration and expiration scan pairs, employing a set of three registration algorithms (NiftyReg, Demons, Elastix). MetaReg generated for each scan pair a registration that is better than any registration obtained by each registration algorithm separately. On average, 10% improvement is achieved, with a reduction of 30% of regions with misalignments larger than 5mm, compared to the best single registration algorithm.

