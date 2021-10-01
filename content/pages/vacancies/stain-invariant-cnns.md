title: Towards stain invariant CNNs for computational pathology
groups: ai-for-health
closed: true 
type: student 
picture: vacancies/scoliosis_modeling.jpg
template: vacancy-single
people: Khrystyna Faryna, Geert Litjens
description: Develop stain invariant CNNs for computational pathology

**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical Problem 
In medical imaging, data acquisition conditions differ among institutions, which leads to variations in image properties, known as  domain shift. Convolutional neural networks (CNN) are sensitive to domain shifts, which can result in poor generalization. Stain variation in histopathological slides is a prominent example.
A number of methods have been proposed to tackle domain shift: stain normalization, domain augmentation, domain adversarial training, classical data augmentation and domain adaptation. Each of the aforementioned methods improves CNNs performance on data from external centers to a certain extent. At the same time, none of these methods guarantees stain invariance.

## Solution 
Group Convolutional Neural Networks (GCNN) have been applied to introduce rotation and translation invariance in histopathology. In M. Lafarge et. al, (2021) models learn feature representations with a discretized orientation dimension that guarantees that their outputs are invariant under a discrete set of rotations. In this project we plan to use GCNNs to guarantee stain invariance. We first plan to define a symmetry group in one of the color spaces. Secondly, we will define functions that transform images from lab 1 to images of lab 2 or lab 3. Thirdly, we 
will discretize the color space accordingly. Subsequently, we will use GCNNs along with a predefined set of transforms to develop a stain invariant solution for histopathology tissue classification. 

## Data 
In this project we plan to use public, multi-institutional datasets such as Camelyon17, MIDOG or PANDA.

## Results

## Embedding 


## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics in the final stages of their Master education. 
- You should be proficient in python programming and have a theoretical understanding of deep learning architectures. 
- Basic biological / biomedical knowledge is preferred.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- More information can be obtained from Khrystyna Faryna (mailto: khrystyna.faryna@radboudumc.nl)
