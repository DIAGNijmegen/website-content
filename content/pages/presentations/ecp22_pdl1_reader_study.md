title: Inter-rater agreement of pathologists on determining PD-L1 status in non-small cell lung cancer
template: presentation-single
picture: posters/ecp22_pdl1_reader_study.jpg
arxiv:
author_list: Leander van Eekelen, Enrico Munari, Ilaria Girolami, Albino Eccher, Jeroen van der Laak, Katrien Grünberg, Monika Looijen-Salamon, Shoko Vos, Francesco Ciompi
groups: pathology, diag
date: 2022-10-03

Artificial intelligence (AI) based quantification of cell-level PD-L1 status enables spatial analysis and
allows reliable and reproducible assessment of the tumor proportion score. In this study, we assess the
cell-level inter-pathologist agreement as human benchmark for AI development and validation. Three pathologists manually annotated the centers of all nuclei within 53 regions of interest in 12 whole-
slide images (40X magnification) of NSCLC cases and classified them as PD-L1 negative/positive tumor
cells, PD-L1 positive immune cells or other cells. Agreement was quantified using F1 score analysis,
with agreement defined as annotations less than 10 um apart and of the same class. An average of 9044 nuclei (1550 negative, 2367 positive tumor cells, 1244 positive immune cells, 3881
other cells) were manually annotated by the three pathologists. The mean F1 score over pairs of
pathologists at dataset level was 0.59 (range 0.54-0.65). When split across classes, the mean per-pair
F1 scores stay approximately the same, indicating the readers perform similarly regardless of cell type.
Besides human variability in manual point annotations with respect to the center of nuclei, lack of
context contributed to disagreement: readers who reported they solely examined the ROIs tended to
disagree more with readers that reported they also looked outside the ROIs for additional
(morphological/density) information.

In conclusion, agreement on determining the PD-L1 status of individual cells is only moderate, suggesting a role for
AI. By quantifying the inter-rater agreement of pathologists, we have created a human benchmark which
may serve as an upper bound (and could be combined via majority vote) for the validation of AI at celllevel, something not done previously. Cell-level AI-based assessment of PD-L1 may supersede slide
level scoring, adding significant information on the heterogeneity and spatial distribution over the tumor.
