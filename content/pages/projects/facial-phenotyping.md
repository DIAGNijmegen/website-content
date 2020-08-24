title: Quantitative facial phenotyping of patients with intellectual disability
groups: ai-for-health
finished: false
type: student
picture: vacancies/facial-phenotyping.jpg
template: project-single
people:  Fien Ockers, Lex Dingemans, Bert de Vries, Marcel van Gerven
description: Development of a deep learning algorithm for learning face representations.

## Clinical problem
Approximately 2% of the general population is affected by Intellectual Disability (ID), a neurodevelopmental disorder.  Intellectual Disability is defined by the incomplete development of the mind during the developing stages of childhood, leading to impairment of several skills that contribute to the general level of intelligence, e.g. cognition, language, motor or social abilities.

In about 30-40% of the cases, ID is caused by a genetic syndrome. However, extracted genetic data is not always decisive with regards to a diagnosis. In those cases, doctors can take a look at the facial characteristics of a patient and compare them with previously diagnosed patients. This is a subjective process and therefore doctors would benefit from an objective model that would support their decisions in diagnosing patients. 

## Solution
Successful completion of the study will result in a technically and clinically validated technology that provides quick, automated, quantitative, and objective phenotyping of patients. The foreseen technology will reduce the burden on both the medical system and patient families by providing a quick non-invasive strategy able to increase the number of positive diagnoses of patients with lD.

## Research question
Can a model be found that performs better than the existing Hybrid model, regarding syndrome vs. control face classification for a specific syndrome, by trying different combinations of a face representation and classification model?

## Methods

### Data
The available data for this project is either extracted from published papers or created in the Radboudumc. In total, the data of 12 syndromes was taken into account for this project.

The control data set was mainly made in the Radboudumc itself and consisted of patients with an unknown form of ID. It was decided to use these images as a control set, as this mimics the real-world application of this classification problem the best. 

A control set was created for each of the 12 syndromes. Per syndrome, one control patient was selected for each syndromic patient, such that there was an even distribution of both labels. These control patients were selected based on gender, age and ethnicity, as was done in the development of the Hybrid model. 

### Models
Model 1: Deepface model
The Deepface model is developed by Facebook and is a convolutional neural network that uses deep learning to perform the task of face verification. The Deepface model is used to obtain a face representation and as a classifier a k-NN is chosen with k set to 3.

Model 2:  FaceReader PointNet model
For this project, the university was able to use and test the capabilities of the model called FaceReader, developed by the company VicarVision. This model detects a 3D face representation of 510 landmarks. These landmarks are processed by the PointNet model to result into a prediction. 

Model 3: FaceReader distance model
This model uses the pairwise distances of the 3D landmark face representations in combination with a Random Forest classifier. 

Model 4: Ensemble  model
The previously described 3 models are combined into an ensemble model to see whether they perform better together.

Model 5: Hybrid model
This model has been developed previously in the Radboudumc for mainly face clustering. This model combines the CFPS and Openface face representation, which are both models that put a face representation into an Euclidean space. This combined face representation is again classified with a k-NN with k set to 3. 

### Experiments
A Leave One Out Cross validation was performed for each model for each syndrome. The Area under the ROC curve (aroc), the specificity (spec) and sensitivity (sens) were used as evaluation metrics. Here only the aroc scores are displayed.

## Results
### Area under the ROC curve
| | Model 1 | Model 2 | Model 3 | Model 4 | Model 5 |
| --- | --- | --- | --- | --- | --- | 
| ADNP (N=33)	| 0.612 |	0.668 |	0.420 |	0.609 |	0.734 |
| ANKRD11 (N=25) | 0.809 |	0.589 |	0.716	| 0.854	| 0.835 |
| CDK13 (N=30)	| 0.559	| 0.780 |	0.722 |	0.786	| 0.870 |
| DEAF1 (N=19)	| 0.499	| 0.743	| 0.448	| 0.728	| 0.666 |
| DYRK1A (N=16)	| 0.694	| 0.508	| 0.525	| 0.520	| 0.750 |
| EHMT1 (N=39)	| 0.843	| 0.704	| 0.849	| 0.901	| 0.882 |
| FBXO11 (N=17)	| 0.580	| 0.473	| 0.444	| 0.492	| 0.593 |
| KDVS (N=75)	| 0.740	| 0.494	| 0.463	| 0.628	| 0.748 |
| SON (N=18)	| 0.698	| 0.755	| 0.610	| 0.857	| 0.634 |
| WAC (N=12)	| 0.418	| 0.665	| 0.828	| 0.722	| 0.790 |
| YY1 (N=10)	| 0.683	| 0.748	| 0.883	| 0.801	| 0.545 |
| 22q11 | 0.756	| 0.759	| 0.603	| 0.793	| 0.622 |

## Conclusion
This project has tried to come up with a model that performs better than the existing Hybrid model. However, no such model has been found, as the Hybrid model has the best performance in the syndrome vs. control classification task for most syndromes. It has been seen that the performance of all models fluctuates over the different syndromes. Hence, it will be quite challenging and possibly even too ambitious to come up with one model that performs well for all the different syndromes. This research has used multiple different models, as well as face representations to explore what the possibilities are, and therefore adds value to the current body of research regarding this topic. Hopefully, this project can guide new research in the right direction of a model that performs well for all syndromes in a syndrome vs. control classification task. 

The code for this project can be found in this [GitHub repository](https://github.com/spatiebalk/face-classification).

The final report for this project can be found [here](https://drive.google.com/file/d/1Q-9a34h_ewoLSLf3jg66xojaUNCPliNg/view?usp=sharing).
