title: Developing deep learning algorithm for de novo variants detection in Pacbio long-read sequencing data
groups: ai-for-health
finished: true
type: student
picture: vacancies/de-novo-variant-detection.jpeg
template: project-single
people: Ole ten Hove, Gelana Khazeeva, Christian Gilissen
description: Developing deep learning algorithm for de novo variants detection in Pacbio long-read sequencing data.

**Start date: 05-09-2022** <br>
**End date: 05-03-2023**

## Clinical Problem
Many developmental disorders, such as intellectual disability, autism spectrum disorder and multiple congenital anomalies are known to be caused by de novo mutations (DNMs). The reliable identification of DNMs is, therefore, of paramount importance both for genetic testing as well as research studies. Because of the genetic heterogeneity that exists for disorders where DNMs play a major role, the identification of DNMs is typically performed based on whole exome (WES) or whole-genome sequencing (WGS) data. In our recent study, we developed DeNovoCNN, a deep-learning-based tool that identifies de novo variants in WES and WGS short-read data more accurately than existing tools. However, the short-read sequencing approaches pose a limitation for the identification of variants in difficult regions. These limitations may significantly contribute to the diagnostic gap in patients who have undergone standard WES and WGS. The emerging long-read sequencing (LRS) technologies offer improvements in the characterization of genetic variation and regions that are difficult to assess. Therefore, this is considered the genetics technology of the future. Further development of the DeNovoCNN tool is necessary to use the advantages of the LRS technologies. 

## Solution
Based on the previous work we showed that deep-learning algorithms can be efficient in the identification of de novo variants in short-read sequencing data (WES and WGS). In this project, we worked on further improvements of DeNovoCNN to detect de novo variants in long-read sequencing data. Two new models were developed, which were, together with the original DeNovoCNN model, evaluated on long-read sequencing data. The first model was a retrained DeNovoCNN, using long-read sequencing data, with the second model utilizing a purpose-built encoding for long-read sequencing.

## Data
We have a set of 33 child-parent trios in-house, 8 of them are with 80 fully validated de novo events per trio. These 8 trios were used as a test set for the evaluation of each model. Of the remaining data, 21 trios were manually annotated for de novo mutations. This had to be done by filtering all genetic variants, then generating screenshots of each remaining variant including the sequencing data of each member of the trio. These screenshots were consequently used to identify 850 mutations, only including substitutions, however, as too little data was available to train on other types of variants.

## Results and Discussion
Long read sequencing is expected to replace SRS within the next 10 years, necessitating the adaptation of all genome analysis tools. The performance of the original DeNovoCNN dropped significantly when predicting on LRS data, where the precision, recall and F1-score were 0.32, 0.87 and 0.47, respectively. These results show the need for adaptation to maintain a high performance on the new data. The manually created training dataset, mentioned before, was then used to retrain the original DeNovoCNN model.
Evaluating the retrained model on the test set, it achieved a precision of 0.0082 and recall of 1.0. The reduced performance is likely explained by losing some nuance for difficult cases from the original, due to the training dataset not including enough rare noisy regions. Another issue was the model not encoding data necessary to deduce whether some cases are mutations or simply have information missing. To solve this issue, a new encoding was developed, and a new model using this encoding was created.

This model using the LRS encoding was pretrained on old SRS data and retrained on the LRS training dataset. This model achieved a precision and recall of 0.027 and 0.99, respectively. Improving significantly compared to the retrained model, using the original encoding, while both were trained using the same dataset.

Looking at the predictions of the new models, the main mistakes made were calling noisy regions as de novo mutations, explaining the low precision. In the future, including such cases in the training should resolve the issue. Because de novo mutations are incredibly rare, any data the model struggles with is far more common than true mutations, therefore the precision is prone to drop quickly. Anyhow, repeating the methodology of this research using the new encoding, but with a dataset that is more representative of the sequencing artifacts, will likely result in a high-performance classification model.

## Embedding
The embedding was in the department of Human Genetics at Radboudumc. Who provided access to a GPU machine and research cluster. 
