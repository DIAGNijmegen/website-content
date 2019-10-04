title: Automatic rib segmentation in CT data
authors: J.J. Staal, B. van Ginneken and M.A. Viergever
has_pdf: True
template: publication
bibkey: staa04b
published_in: Computer Vision Approaches to Medical Image Analysis and Mathematical Methods in Biomedical Image Analysis
pub_details: in: <i>Computer Vision Approaches to Medical Image Analysis and Mathematical Methods in Biomedical Image Analysis</i>, volume 3117 of LNCS, 2004, pages 193-204
A supervised method is presented for the detection and segmentation of ribs in computed tomography (CT) data. In a first stage primitives are extracted that represent parts of the centerlines of elongated structures. Each primitive is characterized by a number of features computed from local image structure. For a number of training cases, the primitives are labeled by a human observer into two classes (rib vs. non-rib). This data is used to train a classifier. Now, primitives obtained from any image can be labeled automatically. In a final stage the primitives classified as ribs are used to initialize a seeded region growing process to obtain the complete rib cage.

