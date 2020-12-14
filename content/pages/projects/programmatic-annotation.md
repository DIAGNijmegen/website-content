title: Programmatically Generating Annotations for Clinical Data 
groups: ai-for-health
finished: false 
type: student
picture: {projects/<image>.png}
template: project-single
people: Ismail Guclu, Djoerd Hiemstra, Koen Dercksen 
description: {A SHORT DESCRIPTION OF +/- 135 CHARACTERS} (This will appear on the card shown on the projects home page)


** Start date: 30-09-2020 ** <br>
** End date: 01-04-2021 **


## Clinical problem

In a supervised learning setting, we need labeled data in order to train a machine learning model.
The acquisition of labeled training data is a time consuming and costly task - if done manually. 
An alternative to hand-labeling training data is to create training data programmatically. 
Weak supervision is an approach to label training data programmatically, where the user defines multiple labeling functions (LF). 
The LFs can differ in type, for example, regular expressions and external knowledge bases. 
The user defined LFs are then aggregated to output a probabilistic label to the training data. 

In our project, we have clinical notes that may contain protected health information (PHI). 
It is important to annotate and replace PHI in unstructured medical records, before being able to share the data for other research purposes due to privacy legistation. 
The process of replacing protected health information is also known as de-identification. 

There are different approaches to de-identifying clinical data: rule-based, feature based and deep neural methods. 
Trienes et al. (2019) made a comparison between the three aforementioned approaches and concluded that: the rule-based approach does not generalize well to data from other domains, the neural approach to de-identifying data shows the best performance, and a decrease in performance is to be expected when applying to new domains of data. 
Although the three methods differ, they all need annotated data to train and/or evaluate the performance.

## Solution

The RUMC Radiology department already employs a rule-based approach, which comprises a complex set of rules to do the de-identification on the radiology reports. 
Our project contributes to the Radboud Routine Care in two ways:
1. First, as there are already hand-labeled training data, we want to experiment with a different approach other than the implemented rule-based method. 
We want to investigate whether there is any improvement in predictive performance. 
2. Second, a significant amount of the radiology report still needs to be annotated. 
More data often leads to better predictive performance, especially in deep neural methods. 
Therefore, we also want to apply weak supervision to programmatically label the radiology reports to investigate the effect of programmatically generated labels on de-identification of radiology reports.

## Data

In this project, we will use the clinical notes from the RUMC Radiology department, which are in Dutch. 
This dataset comprises over 1600 hand annotated documents. 
Eight different PHI tags are defined, but the distribution of the tag count differs. 
The distribution of the tag counts are as follow: (Persoon, 129), (Datum, 1833), (Tijd, 82), (Telefoonnumer, 18), (Patientnummer, 0), (Znummer, 0), (Leeftijd, 2) and (Plaats, 5) which puts the total on 2069 tags.   
## Approach

Our approach for this project will be as follow:
1. As for the first solution, we take the rule-based implementation as baseline and want to experiment with a feature-based method and a deep neural method. 
Then, evaluate and interpret the results.
2. As for the second solution, we want to experiment with weak supervision for de-identification. 
We have to define LFs, for example, datum can be best expressed by rules as they have a certain structure, and we can use an external knowledge base for persoon. 
Subsequently, we can evaluate the accuracies of our LFs as we have access to annotated data. 

## Results

[WIP] 
