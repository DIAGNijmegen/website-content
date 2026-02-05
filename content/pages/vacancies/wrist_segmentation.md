title: AI-enhanced segmentation and registration of wrist bones in fractured and implant-containing wrists
groups: rtc
closed: false
type: student
picture: vacancies/mosquito-biting.png
template: vacancy-single
people: Erin Teule, Brigitte van der Heijden
description: Deep learning for robust segmentation and registration of wrist bones in pathological 3D and 4D CT scans with fractures and metal implants


## Background

Wrist fractures are among the most common injuries of the upper extremity, with distal radius and scaphoid fractures occurring most frequently. Although many fractures heal without complications, distal radius malunions and scaphoid non-unions are common and can severely disrupt carpal alignment and wrist biomechanics [1]. If left untreated or insufficiently corrected, these conditions may lead to chronic pain, instability, and ultimately post-traumatic osteoarthritis. Surgical treatment often involves corrective osteotomies and fixation using metal implants such as plates and screws to restore anatomy and preserve wrist function [2,3]. Despite surgical intervention, it remains unclear to what extent normal wrist kinematics can be restored, making objective evaluation of functional outcomes challenging.

Dynamic computed tomography (4D-CT) offers a unique opportunity to address this challenge by capturing wrist motion in real time. A single acquisition produces 50–100 three-dimensional CT volumes within approximately 10 seconds, enabling detailed quantification of bone motion and carpal kinematics [4,5]. However, the resulting data volume is large, and manual analysis is labor-intensive and impractical for routine clinical use.

Previous work within our research group has demonstrated that deep learning approaches, such as nnU-Net, can accurately segment and label wrist bones in dynamic CT scans of uninjured wrists [6]. However, current algorithms struggle when applied to fractured wrists or wrists containing surgical implants due to anatomical irregularities and metal-induced imaging artifacts. Overcoming these limitations is essential for enabling robust, automated analysis of dynamic CT scans in clinically relevant scenarios.

## Approach

The goal of this project is to advance existing AI-based segmentation and registration methods to handle complex wrist pathology, including fractures, non-unions, and implanted hardware.

The first objective is to improve deep learning-based segmentation models so that they can reliably identify and label all wrist bones in the presence of fractures and metal implants. This will involve retraining and validating models on datasets that include a wide range of pathological cases and artifact patterns.

In addition to segmentation, the project will address registration of dynamic CT sequences. Currently, wrist bone motion is analyzed using classical registration methods such as Coherent Point Drift (CPD), which align bone surfaces across time frames but are computationally intensive and sensitive to irregular geometries. A second objective is therefore to explore AI-based registration approaches and investigate whether segmentation and registration can be integrated into a single deep learning pipeline. Such an approach could significantly improve robustness and speed, facilitating clinical adoption of dynamic CT-based wrist kinematic analysis.

## Data

A large database of anonymized wrist CT data is available through the Departments of Plastic Surgery and Radiology. This includes:

- Dynamic CT scans of healthy volunteers (n=30)
- Dynamic CT scans of patients with ligamentous wrist injuries not affecting bone morphology (n=75)

For these datasets, ground-truth segmentations and a baseline segmentation network are available.

Additional datasets include CT scans of wrists with scaphoid fractures, scaphoid non-unions, distal radius malunions, and wrists containing metal implants. These comprise:

- Standard 3D CT scans (JBZ dataset, n=174, unilateral)
- Dynamic 4D-CT scans acquired at Radboudumc (n=20, bilateral)

All data are fully anonymized and stored on secured institutional servers.

The expected outcome is accurate segmentation of both affected and unaffected wrist bones in pathological scans, as well as reliable registration matrices describing bone motion across time frames.

## References

[1] Shahabpour M, Abid W, Van Overstraeten L, De Maeseneer M. Wrist Trauma: More Than Bones. *J Belg Soc Radiol.* 2021;105(1):90.  
[2] Mulders MA, d'Ailly PN, Cleffken BI, Schep NW. Corrective osteotomy for distal radius malunions. *Injury.* 2017;48(3):731–737.  
[3] Steinmann SP, Adams JE. Scaphoid fractures and nonunions: diagnosis and treatment. *J Orthop Sci.* 2006;11(4):424–431.  
[4] van der Heijden BEPA et al. Dynamic wrist imaging and kinematic assessment. *J Hand Surg Eur Vol.* 2025;50(6):752–761.  
[5] White J, Couzens G, Jeffery C. The use of 4D-CT in assessing wrist kinematics. *Bone Joint J.* 2019;101-B(11):1325–1330.  
[6] Teule EHS et al. Automatic segmentation and labelling of wrist bones in 4D-CT via deep learning. *J Hand Surg Eur Vol.* 2024;49(4):507–509.

## Requirements

Students in the final phase of a Master’s program in Artificial Intelligence, Biomedical Engineering, Computer Science, or a related field are invited to apply.

**Required skills:**

- Experience with Python programming
- Familiarity with machine learning and deep learning frameworks

Affinity with medical imaging, image segmentation, and clinical translation is strongly preferred.

## Information

**Project duration:** 6 months  
**Location:** Radboud University Medical Center

The student will be embedded within the Department of Plastic Surgery and the Advanced X-ray Tomography and Imaging (AXTI) lab of the Department of Radiology. The project is part of a larger, ongoing research program with multiple PhD students and senior clinical and technical supervisors. High-performance GPU workstations are available.

For more information, please contact Erin Teule (erin.teule@radboudumc.nl).

## People

**Erin Teule**  
Researcher  
Department of Plastic Surgery, Radboudumc

**Brigitte van der Heijden**  
Professor, Hand and Wrist Surgery  
Department of Plastic Surgery, Radboudumc
