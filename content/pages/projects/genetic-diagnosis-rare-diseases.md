title: AI-driven genetic diagnosis for rare-diseases
finished: false 
type: general 
picture: vacancies/genetic-diagnosis-rare-diseases.jpg
people: Gelana Khazeeva, Christian Gilissen, Marcel van Gerven, Max Hinne, Helger Yntema
description: The aim of this project is to develop an AI system to automatically diagnose patients with genetic diseases based on their exome and whole genome sequencing data. 
template: project-single 
groups: ai-for-health

## DeNovoCNN: A deep learning approach to *de novo* variant calling in next generation sequencing data

**Motivation:** 
*De novo* mutations (DNMs) are an important cause of genetic disorders. The accurate identification of DNMs from sequencing data is therefore fundamental to rare disease research and diagnostics. Unfortunately, identifying reliable DNMs remains a major challenge due to sequence errors, uneven coverage, and mapping artifacts. 

**Goal**: Develop a deep-learning based algorithm to reliably identify DNMs from sequencing data.

**Results:** 
- We developed a deep convolutional neural network (CNN) DNM caller (DeNovoCNN), that encodes sequencing information for a child-father-mother trio as 160×164 resolution images. 
- DeNovoCNN was trained on DNMs of whole exome sequencing (WES) of 2003 trios achieving 99.2% recall and 93.8% precision. 
- DeNovoCNN has increased recall/sensitivity and precision compared to existing *de novo* calling approaches (GATK, DeNovoGear, Samtools) based on the Genome in a Bottle reference dataset. 
- Sanger validations of DNMs called in both exome and genome datasets confirm that DeNovoCNN outperforms existing methods. 
- We show, that DeNovoCNN is robust against different exome sequencing and analyses approaches, thereby allowing it to be applied on other datasets. 
- DeNovoCNN is freely available and can be run on existing alignment (BAM/CRAM) and variant calling (VCF) files from WES and WGS without a need for variant recalling.

**Paper**: https://doi.org/10.1101/2021.09.20.461072 

## AI-driven genetic diagnosis for rare-diseases

**Motivation:** Exome (WES) and whole genome sequencing (WGS) are currently implemented for genetic testing of more than 7000 patients with genetic diseases per year. In order to obtain a genetic diagnosis these data are intepreted independently by a trained technician and a laboratory specialist using a wide-variety of information of the patient phenotype, known disease genes, and the genetic profile of the patient. This is a cumbersome process that can take up to weeks. The Radboudumc Department of Genetics has exome sequencing data of more than 30,000 individuals, stored as more than 500Tb of data.

**Goal:** We aim to develop an AI-based learning algorithm, that integrates all of this information and is able to automatically diagnose patients with genetic diseases. This will reduce (1) the amount of time spent on interpretation, and thereby also (2) reduce turn-around times for these tests, and (3) will improve diagnoses by reducing the risk of human error.

**Current results:**
- We developed a method based on gradient boosted trees for a binary classification of the variant into 'causative' and 'not-causative' classes
- We take into account genetic profile of the patient and high-level phenotypic information
- We predict correctly in 72.51% of cases using top-1 prediction and in 93.17% using top-5 predicted variants for 1084 unseen samples with genetic diagnosis
