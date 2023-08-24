title: Extending a prostate cancer grading algorithm to other surgical entities
groups: ai-for-health
finished: true
type: student 
picture: vacancies/prostate_pathology.png
template: project-single
people: Michelle Stegeman, Khrystyna Faryna, Geert Litjens
description: Develop a method to extend a prostate cancer grading algorithm to other surgical entities

**Start date: 01-06-2022** <br>
**End date: 23-02-2022** <br>

## Clinical Problem 
In prostate disease, biopsies, small tissue specimens, play a prominent role in the early detection and staging of cancer. Radical prostatectomy, complete surgical removal of the prostate, is typically performed as a curative treatment following a biopsy positive for prostate cancer. Radical prostatectomies result in enormous amounts of tissue for the pathologist to analyse.

Prostatectomy specimens need to be fully graded to allow determination of an adequate follow-up strategy for the patient. For example, a small high-grade component of cancer might be present that alters the treatment strategy and was missed on initial biopsy. Our group has developed a prostate cancer grading algorithm for biopsy samples. Next, we plan to extend this algorithm to prostatectomy data. From an algorithmic perspective, analysis of prostatectomy specimens is challenging due to the presence of a wide variation of tissue, some of which only appear in a fraction of cases. Examples include the seminal vesicles, surrounding fat, nerves, muscle, and large blood vessels, among others. These tissue types are also rarely sampled in biopsies, such that our biopsy-trained algorithm fails on those cases.

## Methods 
We will use fine-tuning to extend the existing model with normal tissue from various locations, depending on the Gleason grade that was falsly predicted. In order to ensure training data contains adequate tissue variability, we will use the false positives predicted by the biopsy model to monitor misclassifications in normal tissue during training time in a location-aware manner and sample data accordingly.

In this project we combined data from public datasets PANDA (~6.000 annotated biopsies), PESO (~40 prostatecomy slides from the test set), and 32 inhouse prostatectomy slides (slides from ~28 patients with coarse annotations).

![Screenshot from 2023-03-06 13-41-21](https://user-images.githubusercontent.com/22368424/223113608-a483e6ba-c282-449b-84f7-472a61efc623.png)

## Results
For an interactive demo we advise to use the baseline algorithm avaiable via Grand-Challenge: <a href="https://grand-challenge.org/algorithms/gleason-grading-of-prostate-biopsies/" class="btn btn-primary btn-lg my-3">Try out the algorithm</a>

## Conclusion
Overall the evaluation of several strategies to extend a biopsy Gleason grading algorithm to radical prostatectomy slides revealed that the models are prone to fit on confounding features such as staining, leading to decreased performance compared to the baseline. To overcome this issue proper stain normalization is needed, and combined with the use of biopsy slides during training and the selection of regions that caused false positives in the baseline model this can help to improve the performance. The future work on this project can include improvements such as cycleGAN normalization and pixel level Gleason masks for prostatectomy samples. The results of the preliminary results indicate that fine-tuning a pre-trained biopsy algorithm can effectively reduce amount of false positive Gleason predictions while preserving good performance on accurately grading biopsy slides and tumor regions in prostatectomy slides. This will potentially lead to an overall improvement in the accurate grading of radical prostatectomy slides.
