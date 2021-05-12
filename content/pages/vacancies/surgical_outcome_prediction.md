title: Three dimensional oral and maxillofacial surgical outcome prediction
groups: ai-for-health
closed: true
type: student
picture: vacancies/soft_tissue.png
template: vacancy-single
people: Guido de Jong, Shankeeth Vinayahalingam, Tom Loonen, Tong Xi, Thomas Maal
description: Development of a model for accurate facial profile outcome prediction following oral and maxillofacial surgery.

## Clinical Problem
Oral and maxillofacial (O&M) surgery is the type of surgery that is focussed on the face, mouth and neck area. This involves surgery for the treatment of facial deformities, jaw malocclusion, pathologies, trauma, adjacent orthodontic treatment and others. Since the facial profile and appearance is often associated with self-identity it is important that the esthetical outcome is also taken in consideration besides the treatment itself. Most of the O&M surgeries affect the facial profile at least to some degree. During the surgical planning for these O&M surgery patients predictions of the facial profile are made for the informed decision making and, where possible, tweaking for different functional and esthetical outcomes. For the prediction a combination of (conebeam) CT-scans and 3D Photos are used. This is most often done by simulating the soft-tissue profile under the influence of changes to the bony tissue using mass tensor models (MTM). However there is a certain degree of inaccuracy in these MTM models that could lead to false predictions of the actual post-surgical facial profile. Accurate predictions are key in the informed decision making and the possibility of tweaking the surgical parameters for optimal treatment. We therefor have a great need for more accurate facial profile outcome prediction models in Oral and maxillofacial surgery.

## Solution
In order to overcome this issue we had a pilot study (under review) for one type of surgery using deep learning (DL) based models in the prediction of the facial profile which showed to be more accurate in most cases as compared to the MTM model. However, this was limited to only one type of surgery and still showed flaws in specific cases. Still, based upon our initial results we strongly believe that DL models can eventually achieve more accurate facial profile outcome prediction models for various types of O&M surgeries. We want to focus on three common O&M surgical forms with well-defined degrees of freedom for the DL prediction models. These are the Bilateral Sagittal Split Osteotomy (BSSO), the LeFort 1, and the BiMax.

## Data
We have access to 120 cases for BSSO, 30 for the LeFort 1 and 200 for the BiMax. Of these cases we have the (conebeam) CT-scan, a pre-surgical 3D Photo and a post-surgical 3D Photo. Furthermore we have the bony tissue surgical parameters of each case.

## Approach
Students will be supervised by a 3D Lab research member whose research is dedicated to 3D technology and machine learning techniques. We furthermore have a group of experts within 3D technology for additional supervision. The student will get familiarized with the 3D data and an approach of choice in the prediction will be chosen. Depending on the chosen approach a combination of convolutional neural networks (CNNs) and/or feed-forward neural networks can be used with or without a combination with more conventional 3D processing algorithms. The goal is to create accurate facial profile outcome prediction models in Oral and maxillofacial surgery for BSSO, LeFort1 and BiMax surgeries. The final deliverable will be implemented within the 3D-Lab software suite called 3DMedX. Furthermore, this final deliverable will also be a publicly available algorithm on the platform Grand Challenge.

## Requirements
- Students with a major in data science, computer science, or artificial intelligence in the final stage of master level studies are invited to apply.
- Interest in (medical) image analysis and machine learning.
- Affinity with programming in Python and with deep learning packages (e.g. PyTorch or Keras) is required.

## Information
- Project duration: 6 months
- Location: Radboud University Medical Center
- For more information, please contact [Guido de Jong](mailto:Guido.deJong@radboudumc.nl)
