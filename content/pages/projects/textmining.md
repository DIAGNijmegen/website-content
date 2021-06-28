title: Text mining pathology reports
groups: ai-for-health
finished: true
type: student
picture: projects/textmining.jpg
template: project-single
people:  Josien Visschedijk, Jan van den Brand, Wynand Alkema, Jack Wetzels, Djoerd Hiemstra
description: Development of a text mining system to accurately make a diagnosis from nephrology pathology reports.

## Clinical problem
Within the department nephrology, a biopsy is taken from patients for further research. This biopsy can be analyzed with three different methods:

* Light microscopy
* Immunofluorescence
* Electron microscopy

The analysis and the final diagnosis of the biopsy are documented in a pathology report. However, there is a suspicion that only light microscopy and immunofluorescence are required in making a diagnosis. In some cases, electron microscopy adds nothing to the process of making a diagnosis. There is demand for a decision supporting algorithm, which state a diagnosis, based on the text. Furthermore, this explainable algorithm makes the process of concluding such a diagnosis clear. In this way, certain characteristics of the kidneys can be extracted, which have led to a particular diagnosis. It can also show abnormalities in the decision making, in which human beings would decide otherwise.

## Innovation
The goal of this project is to design a text mining algorithm, which makes (with a fairly high accuracy) the same diagnosis as a nephrologist would when analyzing pathology reports.

## Results
To support nephrologists in their decision making process, this project studies if it is possible to automatically diagnose for 32 glomerular diseases given the text of a pathology report,  The project results are the following:

With two classifiers and an alteration of several parameters, 63 separate classifiers are designed. Of these models, 49 models used a decision tree classifier, and 24 models used a neural network classifier. Examples of the alteration of parameters is the use of binary- or multilabel classification, or the use of different feature selection methods. The performance was measured using the F1 score. The mean F1 score of the top five models using a decision tree classifier is ±0.3. The mean F1 score for the neural network classifier is ±0.4. There is a relation between the occurrence of a specific glomerular disease and the F1 score.

Predominant diseases have an F1 score of ±0.8, whereas rare diseases have an F1 score of ±0.1. The best mean F1 scores are achieved with a 3-layered neural network, using multilabel classification and a tensor flow implementation.

## Conclusion 
With an overall mean F1 score of ±0.4, the classifiers are not sufficient in supporting nephrologists in their decision making process when classifying pathology reports. However, for predominant glomerular diseases, the classifiers could serve as a supporting factor. It is recommended to conduct further research into setting up a categorization system with pre-defined values for better results in classifying pathology reports. At the moment, we are extending the categorization system, with all the characteristics on which a pathology report is scored in order to determine one or more glomerular disease(s). With this new information, we are capable 
to extract which features are important in order to determine the diagnosis of pathology reports.
