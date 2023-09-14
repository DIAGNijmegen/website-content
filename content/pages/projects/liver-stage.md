title: Spying on parasites: using deep learning to quantify the interactions between malaria parasites and human liver cells
groups: ai-for-health
finished: false
type: student
picture: projects/liverStage.jpg
template: project-single
people: Anton Ligterink, Annie Yang, Felix Hol
description: Quantifying interactions between malaria parasites and human liver cells 

**Start date: 15-02-2023** <br>
**End date: 14-08-2023**

## Clinical Problem
Malaria remains a significant mosquito-transmitted disease with approximately 250 million cases and 0.6 million deaths annually. The disease begins with the injection of parasites by an infected mosquito into the human host. These parasites travel to the liver and begin a week long development where they quietly undergo impressive replication (where one infected liver cell can generate up to 10.000 daughter blood-infective parasites). The subsequent rupture of the infected liver cells releases tens of thousands of daughter parasites that infect the circulating red blood cells, wrecking havoc on the body, resulting in the symptoms of fever, anaemia etc associated with malaria.

Given the serious impact of malaria on the world population, extensive efforts to understand the complex nature of the causative parasites’ life-cycle have been made to great results. However, the initial development of parasites in the liver remains a black-hole compared to the other life-stages due to in vitro difficulties in obtaining enough samples for research. 

Given the importance of the liver stage in establishing malaria in the human host and its potential in therapeutic interventions (the only WHO approved vaccine candidate is against this stage of the life-cycle), this ambitious project aims to take fluorescence microscopy images generated over a 5 year period across different parasite strains, treatment conditions etc to understand important biological questions regarding liver stage infection. 

References:
1. Cutler, Kevin J., et al. "Omnipose: a high-precision morphology-independent solution for bacterial cell segmentation." Nature methods 19.11 (2022): 1438-1448.

## Solution
Microbial infections of nucleated cells cause large problems of morbidity and mortality around the world. Using malaria parasite as a proof of concept, this project will provide guidance with regards to the analysis of existing and yet-to-be characterized microbial-host interactions. The generated software will be used by the department of Medical Microbiology in ongoing projects that aim to characterize the liver stage of malaria and in research lines that aim to identify novel malaria drugs. 

The tasks in this project are:
1)	Generate a deep learning based algorithm that will segment parasite and host cells present in multi-channel fluorescent images, and measure an informative set of parasite/host parameters from individual cells. A comprehensive set of annotated images is available. 
2)	Apply the developed computational pipeline to answer biological questions concerning:
a.	The different growth rates of different parasite strains
b.	The  amount of daughter parasites generated per parasite strain during development
c.	The presence and spatial arrangement of different parasite markers during development
d.	The spatio-temporal relationship between parasites and host
3)	Create a computational pipeline to sieve through existing drug treated parasite forms to create a (hopefully unique) phenotype-based profile associated with distinct compound treatment. 

## Data
An initial set of 1000 annotated images is available to train a segmentation algorithm. To answer a variety of clinical and biological questions in the second phase of the project (obtaining measurements of useful parameters to understand biology and predict possible unique phenotypes associated with particular treatments), there are at least 70.000 images available. 
