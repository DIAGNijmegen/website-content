title: AI-assisted detection of endometrium (pre)malignancies in endometrium pipelle biopsies. 
groups: ai-for-health
finished: false 
type: student 
picture: projects/endoaid.png 
template: project-single 
people: Thijs Gelton, Sanne Vermorgen, Francesco Ciompi 
description: The development of model to detect (pre)malignancies in highly fragmented pipelle sampled biopsies.

**Start date: 01-02-2022** <br>
**End date: 31-07-2022**

## Clinical problem

Endometrial cancer is one of the more frequent malignancies in women. Each year, 2000 women are diagnosed with
endometrial cancer (EC) in the Netherlands, the majority of which are postmenopausal women with a mean age of 65 year at
the time of diagnosis. An increased thickness of the endometrium and abnormal vaginal blood loss are often the first
signs of the development of endometrium cancer. Sometimes, precancerous tissue (premalignancy) can be detected, and
early treatment of this premalignancy can prevent the ultimate development of cancer, thus preventing the morbidity and
mortality related to endometrial cancer. The histopathologic diagnosis of the pipelle sampled endometrium tissue guides
further management of the patient. Pipelle sampling is a non-invasive method for biopsy, which is, therefore, often
preferred in clinical screenings. The extracted cell tissue is, however, highly fragmented and pathologically less
informative than, for example, a surgical resection. Additionally, a high percentage (90 - 95%) of the screenings yield
benign tissue. A correct evaluation of the biopsy specimen, with 100% sensitivity, is therefore of paramount importance
in reducing the workload of pathologists.

## Data

In this project, we will include all Radboudumc archival endometrial pipelle biopsies processed between October 2013 and
April 2021, resulting in a total 3230 cases (using a PALGA search to find cases). From this set, we will select
representative examples of the four main clinically relevant categories that will be addressed in this project, namely

1. Normal endometrium
2. Endometrial hyperplasia without atypia
3. Endometrial hyperplasia with atypia
4. Endometrial carcinoma.

On this set, pathologists will make manual annotations of relevant regions, which will be used for training and
validation of AI algorithms. For training purposes, about 100 cases will be annotated with manual dense annotations of
tissue types, while the rest of cases will be annotated with weak annotations extracted from the pathology reports.
Eventually, the validation of developed algorithms will be performed on > 3,000 cases.

## Solution

We will develop a segmentation model, trained using our novel Stratified Hard Negative Mining (SHNM) approach, where the
most severe category will be used for slide-level diagnosis. This means that if malignant (the highest clinical
importance) tissue is predicted to be present in the WSI, then this will determine the diagnosis. SHNM is a novel
addition to Hard Negative Mining (HNM). Regular HNM will select false positives (FP) solely on a likelihood. This
neglects the morphological value certain categories display. With SHNM the FP are first collected, including metadata
(coordinates, low dimensional embedding, etc.). In the second stage, these FPs are clustered based on their encoded
embeddings, which represent the morphologies of the cell tissue. This should aid the model in fine-tuning its ability to
discriminate the difficult morphologies which are located on the boundaries between two categories.

## Results

The final algorithm will be made publicly available as a Docker container on https://grand-challenge.org/. This will
allow pathologists and other interested parties to easily test against their own Whole-Slide images.
