title: Self-supervised pretraining for digital pathology
groups: ai-for-health
finished: false 
type: student
picture: projects/self-supervision.png
template: project-single
people: Sofía León, Marina D'Amato, Francesco Ciompi
description: Development of self-supervised pretraining for digital pathology.


** Start date: {15-01-2023} ** <br>
** End date: {15-07-2023} **


## Clinical problem
When training deep learning algorithms for medical image analysis, learning a good representation of the data is a key step needed for most downstream tasks, such as image classification, segmentation or object detection. 

In recent years, the field of self-supervised learning has grown rapidly in computer vision and is being adopted as a technique for model pre-training in medical imaging as well, producing a domain-specific feature extractor without the need for manually annotated images, which considerably reduces the burdens of pathologists. 

The goal of this project is to push the boundaries of self-supervised training in digital pathology by increasing the training set size by a factor ten compared with the state of the art, using both digital archival material from the Radboudumc, as well as a broad collection of publicly available data from grand challenges available via the grand-challenge.org platform. 

Furthermore, we will investigate the benefits of learning a general-purpose representation of pathology images beyond H&E, also including immunohistochemical staining. The goal is to build some form of general-purpose pan-cancer histopathology encoder that can be used as a backbone to improve downstream tasks such as image classification, detection or segmentation. This project is intended to be a cross-application project and the resulting model will be tested on different clinical tasks.

## Solution

Recent approaches like SimCLR<sup>[1]</sup>, DINO<sup>[2]</sup>, BYOL<sup>[3]</sup> and other similar self-supervised methods have proven their utility in learning good representations of histopathological images, where the amount of data in a single slide is very large, given the size of gigapixel images used in pathology. However, recent work in this field has solely paired self-supervised approaches with publicly available datasets such as TCGA, which contains 11,000 whole-slide images, solely stained with standard haematoxylin and eosin staining (H&E). Pushing the boundaries of the data set size might unlock the possibility of learning a very high-level representation of the data that can improve performance of state-of-the-art downstream tasks, such as image segmentation, classification, or object detection. Several AI tasks will be selected as demonstrators to test the model’s performance in different settings.

[1] Chen et al, A Simple Framework for Contrastive Learning of Visual Representations <br>
[2] Caron et al, Emerging Properties in Self-Supervised Vision Transformers <br>
[3] Grill et al, Bootstrap your own latent: A new approach to self-supervised Learning


## Data
In this project we intend to use the digital archival material from the Radboudumc, as well as a broad collections of publicly available data from grand challenges available via the grand-challerge.org platform.

## Results
A well documented algorithm or pipeline made available as a Github repository. The algorithm will be made publically available on Grand-Challenge.

