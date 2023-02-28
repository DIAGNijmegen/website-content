title: Extending a prostate cancer grading algorithm to other surgical entities
groups: ai-for-health
finished: false
type: student 
picture: vacancies/prostate_pathology.png
template: project-single
people: Michelle Stegeman, Khrystyna Faryna, Geert Litjens
description: Develop a method to extend a prostate cancer grading algorithm to other surgical entities

**Start date: 23-02-2022** <br>
**End date: 23-11-2022** <br>

## Clinical Problem 
In prostate disease, biopsies, small tissue specimens, play a prominent role in the early detection and staging of cancer. Radical prostatectomy, complete surgical removal of the prostate, is typically performed as a curative treatment following a biopsy positive for prostate cancer. Radical prostatectomies result in enormous amounts of tissue for the pathologist to analyse.

Prostatectomy specimens need to be fully graded to allow determination of an adequate follow-up strategy for the patient. For example, a small high-grade component of cancer might be present that alters the treatment strategy and was missed on initial biopsy. Our group has developed a prostate cancer grading algorithm for biopsy samples. Next, we plan to extend this algorithm to prostatectomy data. From an algorithmic perspective, analysis of prostatectomy specimens is challenging due to the presence of a wide variation of tissue, some of which only appear in a fraction of cases. Examples include the seminal vesicles, surrounding fat, nerves, muscle, and large blood vessels, among others. These tissue types are also rarely sampled in biopsies, such that our biopsy-trained algorithm fails on those cases.



## Methods 
We will use active learning to iteratively enrich the training dataset with normal tissue from various locations, depending on which of them throws off the algorithm the most. In order to ensure training data contains adequate tissue variability, we will use ‘spatial hard-negative mining’ to monitor misclassifications in normal tissue during training time in a location-aware manner and sample data accordingly.

In this project we plan to combine data from public datasets PANDA (~11.000 annotated slides) and PESO, and inhouse dataset of prostatectomy data (slides from ~40 patients with detailed annotations + ~4000 slides with only slide level labels).

## Results
The algorithm will be made publically available as a Docker container on https://grand-challenge.org/.

## Conclusion
Overall the evaluation of several strategies to extend a biopsy Gleason grading algorithm
to radical prostatectomy slides revealed that the models are prone to fit on confounding
features such as staining, leading to decreased performance compared to the baseline.
To overcome this issue proper stain normalization is needed, and combined with the use
of biopsy slides during training and the selection of regions that caused false positives
in the baseline model this can help to improve the performance. The future work on
this project can include improvements such as cycleGAN normalization and pixel level
Gleason masks for prostatectomy samples. The results of the preliminary results indicate
that fine-tuning a pre-trained biopsy algorithm can effectively reduce amount of false
positive Gleason predictions while preserving good performance on accurately grading
biopsy slides and tumor regions in prostatectomy slides. This will potentially lead to an
overall improvement in the accurate grading of radical prostatectomy slides.
