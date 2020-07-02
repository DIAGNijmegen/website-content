title: Quantitative facial phenotyping of patients with intellectual disability
groups: ai-for-health
finished: false
type: student
picture: vacancies/facial-phenotyping.jpg
template: project-single
people:  Fien Ockers, Lex Dingemans, Bert de Vries, Marcel van Gerven
description: Development of a deep learning algorithm for learning face representations.

## Clinical problem
lntellectual disability (lD), affecting 2% of the general population, is frequently part of a syndrome with specific facial characteristics, so-called dysmorphism. The majority of lD cases are caused by rare sporadic genetic mutations, making it difficult to accurately diagnose. For clinical geneticists, craniofacial characteristics are highly informative when diagnosing genetic diseases. We propose to automate the extraction of patient-specific facial phenotypic information from image data. To this end, we will develop new machine learning algorithms for the analysis of facial expressions that are able to capture the relevant features for accurate matching of facial characteristics. This analysis will be supported by whole exome sequencing to assess the presence of a mutation in the patient. The main challenges in this study come from the novelty of the application area, the clinical conditions, and the rarity of some of the genetic disorders.

## Solution
Successful completion of the study will result in a technically and clinically validated technology that provides quick, automated, quantitative, and objective phenotyping of patients. The foreseen technology will reduce the burden on both the medical system and patient families by providing a quick non-invasive strategy able to increase the number of positive diagnoses of patients with lD.

## Research question
To be able to execute the task of quantitative phenotyping of facial features there are roughly two tasks that need to be solved: 1) A rich face representation needs to be extracted from faces. 2) A model should be found that can classify these face representations into their correct syndrome category. 
Initially, this classification problem has been seen as a binary classification problem. A patient either belongs to a specific syndrome group or to the control group (patients with an undefined form of ID, so no healthy patients, as that would be too easy). Later on in the project, also a syndrome vs. syndrome approach has been taken to better understand the capabilities of various representations and models.

## Methods

There are several ways to get a face representation. In general there are two different kinds of approaches. The first approach is model based, i.e. letting a neural network (DeepFace and FaceNet are two well-performing examples) determine a face representation, based on the pixel image input, which is acquired by using these face representations in a task of face recognition or face verification. However, this leads to not a lot of insight into which numbers in the face representation correspond to which parts of the face.
The second approach is more local based, i.e. locating keypoints on an image (corner of the eyes, mouth etc.) and using these, their pairwise distances or surrounding textures as face representation to feed as input to the classifier. This would of course give a better clue about which features are distinctive to certain syndromes, but these methods perform in general a bit worse. 

Currently, the face representations that are/have been experimented with are:
- A publicly available implementation of DeepFace, a neural network made originally by Facebook which has a face representation of 4096 features
- The pairwise distances of the 68 automatically detected facial keypoints by the python library dlib
¬- The 510 3D facial keypoints, found by the algorithm made by the company VicarVision which they have made available for this research project.
- The hybrid model representation, which is a combination of the model-based publicly available implementation of FaceNet, OpenFace, and the local-based method which combines pair-wise distances with surrounding textures CFPS. This hybrid model is a result of previous research done into this topic.

For most face representations, several simple classifiers (SVM, k-NN, RandomForest) are tried, in combination with a Leave One Out cross validation method to ensure that as much data as possible can be used.  For the 3D point-representation the pointnet model is currently used for some experiments.

## Results
Below are some preliminary results of classifying patients in the binary way described above, and using the DeepFace representation and a GradientBoostClassifier with 10 trees.

| --- | Area under the ROC curve | Specificity | Sensitivity |
| --- | --- | --- | --- |
| ADNP (N=33)	| 0.7622	| 0.6970	| 0.8182 |
| ANKRD11 (N=25) | 0.6976	| 0.7200	| 0.8000 |
| CDK13 (N=30)	| 0.7967	| 0.8667	| 0.8000 |
| DEAF1 (N=19)	| 0.7064	| 0.6316	| 0.6316 |
| DYRK1A (N=16)	| 0.5391	| 0.5625	| 0.6250 |
| EHMT1 (N=39)	| 0.6285	| 0.6923	| 0.6410 |
| FBXO11 (N=17)	| 0.5121	| 0.4706	| 0.6471 |
| KDVS (N=75)	| 0.7717	| 0.6667	| 0.7333 |
| SON (N=18)	| 0.9228	| 0.8333	| 0.8889 |
| WAC (N=12)	| 0.6667	| 0.6667	| 1.0000 |
| YY1 (N=10)	| 0.9300	| 0.8000	| 0.7000 |


## Innovation
This project represents a unique combination of state-of-the-art genomic analysis, with significant developments in the phenotyping of patients with rare and difficult to diagnose developmental disorders via facial image analysis. This innovation comes through combining the two major research fields of genetics and machine learning, and requires a multidisciplinary team of clinicians, bioinformaticians and informaticians.

The developed tool for quantitative facial phenotyping will be tested and subsequently implemented in the Dept. of Human Genetics, Radboudumc. Further dissemination will follow both at national as well as international level.

