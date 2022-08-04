title: AI-assisted detection of endometrium (pre)malignancies in endometrium pipelle biopsies groups: ai-for-health
finished: false type: student picture: projects/endoaid.png template: project-single people: Thijs Gelton, Sanne
Vermorgen, Francesco Ciompi description: The development of model to detect (pre)malignancies in highly fragmented
pipelle sampled biopsies.

**Start date: 01-02-2022** <br>
**End date: 31-07-2022**

- Uitleggen readerstudy en verandering problem statement
- Solution beschrijven
- Toelichten uitbreidingen in methods (hoe zijn we tot de solution gekomen)
- Resultaten toelichten
- Conlusie van het project (itereer nog een keer over problemen data)

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
benign or non-informative tissue. A correct evaluation of the biopsy specimen, with 100% sensitivity, is therefore of
paramount importance in reducing the workload of pathologists.

## Data

A total of 3002 pipelle biopsies performed between October 2013 and April 2021 were retrieved from the pathology archive
of the Radboudumc. To retain a real-life situation, no preselection of cases was performed. H&E-stained slides were
scanned using a 3DHistech P1000 scanner at 0,25 µm/pixel. Images were pseudonymized. A total of 91 whole slide images (
WSI), randomly chosen with a predefined category-weighted key, were immediately set aside to be used in the
interobserver variability study and to be used for evaluation of the algorithm. The remaining 2911 cases were used to
train the algorithm.

From the 2911 cases, 100 WSI (25 “normal”, 25 “hyperplasia without atypia”, 25 “hyperplasia with atypia”, 25
“malignant”) were selected for manual annotation of pixels. An average of five regions of interest (ROI) of 500*500 µm
were identified on each of the 100 WSI and dense annotations were made, labelling each pixel inside the ROI in 6 tissue
classes: “epithelium benign” (normal glands), “epithelium hyperplasia” (hyperplastic glands without atypia), “epithelium
atypia” (hyperplastic glands with atypia), “epithelium malignant” (malignant glands or cell groups), “stroma” (including
stromal structures such as blood vessels) and “rest” (blood, mucus, luminal space inside the glands,…). The remaining
2811 WSI were not annotated and only labeled with a category code, as described above. The use of strong- and weakly
labeled samples allowed us to apply different modelling techniques.

## Solution

An AI-system, based on the multiple instance learning algorithm CLAM[CITE], that learns to correlate visual patterns on
patch-level to binary slide-level diagnosis, based on a single category per WSI. Figure ? illustrates the model taking a
WSI as input, dividing this into patches (W: 512, H: 512, MMP: 0.5) based on a tissue mask and then encoding each patch
into a vector of length 2048. The CNN used for encoding is a ResNet50 architecture pre-trained using 900.000
histopathology images[CITE]. The vectors are weighted using an attention module and this attention score is used as a
pseudo-label. High attention scores should correlate to positive samples and vice versa. These pseudo-labels are used in
a clustering model, which could be a seen as a form of self-supervised learning and meant to improve the feature
representation produced by the attention module. The same attention scores are eventually pooled into a slide-level
diagnosis and simultaneously used in an interpretable heatmap visualisation. The final output of the modul is thus the
likelihood that endometrium (pre)malignancy is present and what patches in the image attribute to this.

## Results

The final algorithm will be made publicly available as a Docker container on https://grand-challenge.org/. This will
allow pathologists and other interested parties to easily test against their own Whole-Slide images.
