title: AMI
finished: true
type: general
picture: projects/AMI.png
template: project-single
groups: pathology
people: Péter Bándi, Marcory van Dijk, Geert Litjens, Jeroen van der Laak
description: Joint project between DIAG and Fraunhofer MEVIS aimed at the development of a generic platform for automatic medical image analysis.


## Background
Breast cancer is the most common cancer among women. Within their lifetime, 12% of women are diagnosed with breast cancer. The prognosis of breast cancer patients is mainly determined by whether the cancer is organ-confined or has spread to other parts of the body. An internationally accepted means to classify the extent of cancer is the TNM staging system. In breast cancer, TNM staging takes into account the size of the tumor (T-stage), whether the cancer has spread to the lymph nodes (N-stage), and whether the tumor has metastasized to other parts of the body (M-stage). The axillary lymph nodes are typically the first location breast cancer metastasizes to. Currently, the status of these lymph nodes is almost always assessed by applying the sentinel lymph node procedure. This procedure identifies the nearest lymph nodes to which the tumor drains, which are then excised for pathologic examination. Glass slides are prepared from the tissue speciments and stained with hematoxylin and eosin (H&E) to highlight the cell nuclei and the general structural features of the tissue. Through microscopic assessment the pathologist screens the slides for tumor presence. If tumor cells are found, the pathologist measures their extent in order to determine the pathologic N stage (pNstage) of the tumor. In case of unclear diagnosis on H&E, immunohistochemical (IHC) staining for cytokeratin can be used for clarification and is standard diagnostic practice in the Netherlands.

## Aim
We aimed to develop deep neural networks that can automatically detect and outline the tumor areas on the digitized version of the glass slides. With these outlines we would like to help steering the attention of the pathologist during assessment for faster, and more accurate evaluation. Furthermore, in current practice, the IHC staining is only made when the pathologist cannot find tumor lesions in the lymph node tissue and needs clarification. With the developed algorithm, we automated this process by pre-screening the scanned slides. If the algorithm could not find cancer in the screened whole-slide images, the system would order the IHC stained clarification slides automatically. The practicing pathologist would be presented with whole-slide images where the algorithm already outlined the identified tumor areas or an attached IHC clarification, in case of cancer free slides further accelerating the evaluation process. Finally, in this project we also developed web based whole-slide image viewers that can be accessed via a web browser for client independent viewing and assessment.

## Funding

AMI is a collaborative project of the [Fraunhofer Gesellschaft](https://www.fraunhofer.de/) and the [Radboud University and University Medical Center](https://www.radboudumc.nl/en/research).
