title: Cross-modality deep learning on stain concentration maps to improve quantification of immunohistochemistry and immunofluorescence digital pathology data
groups: ai-for-health
finished: false 
type: student
picture: projects/pdl1_immunohistochemistry.jpg
template: project-single
people: Carlijn Lems, Leander van Eekelen, Francesco Ciompi 
description: Applying models trained with immunohistochemistry data on immunofluorescence.


** Start date: {30-01-2023} ** <br>
** End date: {30-07-2023} **


## Clinical problem
Every day, hundreds to thousands of histopathology slides are made in our medical center. Most of them are stained with hematoxylin and eosin (H&E) to visualize tissue morphology, producing the typical “pink-purple-blue pathology slides”. In some cases, specific subtypes of cells are targeted with immunohistochemistry (IHC), where specific proteins can be stained using the specificity of antibodies. In this case, cell nuclei are usually stained in blue, and targeted cells are stained in brown, although other chromagens can be used.

Both H&E- and IHC-stained slides are standardly produced at large scale in pathology laboratories all around the world, usually scanned via bright-field microscopy. In recent years, a large corpus of deep learning algorithms has been proposed to automate quantification on H&E and IHC stained images, usually trained based on large-scale datasets with manual annotations created by several research groups, including ours. 

At the same time, it is possible to target multiple types of cells on the same tissue sample using more advanced techniques such as multiplexing immunofluorescence (mIF), a more expensive, time consuming and not largely available, yet powerful research technique that is increasingly used for biomarker analysis and discovery. Despite some recent developments in the field, to date the analysis of mIF data is mostly based on traditional image analysis models and still does not benefit of the availability of large-scale curated datasets produced for AI development in brightfield microscopy.

## Solution

In this project, we will develop AI models that can be used for automated quantification in digital pathology across two domains: standard immunohistochemistry in brightfield microscopy, and multiple immunofluoresce.

## Approach

The core idea is to replace the RGB input typically used to train deep learning algorithms with a combination of relevant density channels extracted from the image itself, such as the intensity of nuclei and the intensity of the chromagen attached to the targeted protein in IHC; examples are CD8-positive T-cells or PD-L1 positive tumor cells. This approach will be based on initial work developed in our group (Geijs et al. 2018, 10.1117/12.2293734).

Once the input of deep learning model is no longer an RGB image but instead pure density channels, the same algorithm can be de-facto applied to other imaging modalities such as mIF, by taking combinations of intensity channels like DAPI for nuclei specific antibody channels for targeted cells e.g., CD8).

Without the need for collecting, curating and annotating new training data for deep learning in mIF, this approach will allow to reuse large-scale digitalized archival material and corresponding annotation to bring deep learning-based quantification to the field of spatial biology and biomarker discovery in mIF.

## Data

We will reuse existing data generated via brightfield microscopy and annotated in past and ongoing projects. In particular, we will initially use the dataset used in (Swiderska-Chadaj, 2019, 10.1016/j.media.2019.101547), consisting of n=83 images from three different organs (breast, colon, prostate) and >170,000 manually annotated cells, and the dataset used in the ongoing project on PD-L1 quantification, with a cohort of 60 whole-slide images of non-small cell lung cancer stained with PD-L1, with >300,000 annotated cells.

For application to immunofluorescence data, we will use two datasets, one containing n=40 cases where 7 different markers were used to stain 7 different types of cells on the same tissue slides, and where consecutive slides were cut and also stained with H&E and PD-L1, which gives a unique opportunity for validation of the PD-L1 algorithm; another dataset with n=18 cases where 6 different mIF markers were used, and serial sections were stained with PD-L1 and CD8 staining in brightfield microscopy.

## Results
A well documented algorithm or pipeline made available as a Github repository. The algorithm will be made publically available on Grand-Challenge.

