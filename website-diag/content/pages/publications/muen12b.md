title: DIRBoost: An algorithm for boosting deformable image registration
authors: S.E.A. Muenzing, B. van Ginneken and J.P. W. Pluim
has_pdf: True
template: publication
bibkey: muen12b
published_in: IEEE International Symposium on Biomedical Imaging
pub_details: in: <i>IEEE International Symposium on Biomedical Imaging</i>, 2012, pages 1339-1342
doi: https://doi.org/10.1109/ISBI.2012.6235813
We introduce a novel boosting algorithm to boost - i.e. improve on - existing methods for deformable image registration. The proposed DIRBoost algorithm is inspired by the theory on hypothesis boosting, well-known in the field of machine learning. DIRBoost involves a classifier for landmark-based Registration Error Detection (RED). Based on these RED predictions a Voronoi tessellation is generated to obtain a dense estimate of local image registration quality. All areas predicted as erroneous registration are subjected to boosting, i.e. undergo iterative registrations by employing boosting masks on both the fixed and moving image. We evaluated the DIRBoost algorithm on five CT pulmonary breathhold inspiration and expiration scan pairs, employing the NiftyReg registration algorithm. DIRBoost could boost about 50% of the wrongly registered areas which in turn also improved the average landmark registration error by 24%.

