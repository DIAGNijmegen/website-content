title: Explainability through Reasoning Segmentation
groups: diag, pathology
closed: false
type: student
picture: vacancies/reasoning_segmentation.jpg
template: vacancy-single
people: Sebastiaan Ram, Geert Litjens
description: Advancing clinical explainability of vision-language models through reasoning segmentation

## Clinical Problem
Reasoning segmentation is an emerging technique in vision-language models (VLMs), in which the model is tasked with generating a segmentation mask in response to an implicit query formulated in natural language<sup>[1]</sup>. Unlike traditional segmentation, where the target class is explicitly defined (for example segmenting a 'yellow bag'), reasoning segmentation requires the model to interpret clinical language (for instance: "show me the region most likely to influence tumour staging"), infer what structure or pattern is being described, and then localize it in the image. Given that pathological diagnosis is fundamentally grounded in visual observations, reasoning-based segmentation could offer a powerful new form of explainability. By enabling models to visually locate structures and patterns described in clinical language, this technique could serve not only as a diagnostic aid, but also as a training tool for pathologists.

While this approach has shown early promise in general computer vision, it has not yet been extensively explored in digital pathology. Additionally, it remains unclear which architectural strategy is most effective for this task in pathology. Currently, two methodologies have been proposed: 1) End-to-end pipelines, where VLMs jointly learn reasoning and segmentation<sup>[2, 3]</sup>, and 2) modular pipelines that first extract and reason about visual concepts and then apply segmentation through a dedicated agent<sup>[4, 5, 6]</sup>. This presents a unique opportunity to explore and introduce reasoning segmentation into the clinical workflow. As part of the [ANTONI project](https://www.computationalpathologygroup.eu/projects/antoni/), we are developing a virtual assistant capable of supporting pathologists in their clinical diagnosis across multiple tissue types and diseases. Therefore, the results of this project will be of great value to continue the development of explainable and reliable systems.

## Approach
This project aims to investigate and compare the different reasoning segmentation approaches currently applied to digital pathology and general computer vision. Specifically, we aim to understand where the performance gains in pathology-specific reasoning segmentation originate, and what the impact of concept-only (agent-based) reasoning segmentation is compared to end-to-end approaches. You will benchmark and analyze a variety of state-of-the-art models on large datasets, spanning throughout the domain of digital pathology.

## Data
The evaluation will be conducted using a combination of publicly available pathology datasets and in-house annotated data from Radboudumc. 

## References
[1] Shen, Yiqing, et al. "Reasoning segmentation for images and videos: A survey." arXiv preprint arXiv:2505.18816 (2025). <br>
[2] Lai, Xin, et al. "LISA: Reasoning segmentation via large language model." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pp. 9579-9589. <br>
[3] Liu, Zelin, et al. "PathChat-SegR1: Reasoning segmentation in pathology via SO-GRPO." International Conference on Learning Representations (ICLR), 2026. <br>
[4] Carion, Nicolas, et al. "SAM 3: Segment anything with concepts." arXiv preprint arXiv:2511.16719 (2025). <br>
[5] Liu, Anglin, et al. "MedSAM3: Delving into segment anything with medical concepts." arXiv preprint arXiv:2511.19046 (2025). <br>
[6] Jiang, Chongcong, et al. "Medical SAM3: A foundation model for universal prompt-driven medical image segmentation." arXiv preprint arXiv:2601.10880 (2026). <br>

## Requirements 
- Students in computer science, biomedical engineering, artificial intelligence, physics, or a related area in the final stage of bachelor/master level studies are invited to apply.
- Interest in image analysis, machine learning and vision-language models.
- Affinity with programming in Python, specifically in the PyTorch framework.

## Information 
- Project duration: 3-6 months
- Location: Radboud University Medical Center
- You will be part of the Diagnostic Image Analysis Group (DIAG) and Computational Pathology Group, whose research focus is the analysis of histopathological slides with deep learning techniques.
- You will have access to and work with a large GPU cluster.
- For more information, please contact [member/sebastiaan-ram]
