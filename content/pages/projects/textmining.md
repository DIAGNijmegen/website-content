title: Text mining pathology reports
groups: diag, ai-for-health
finished: false
type: student
picture: vacancies/textmining.jpg
template: project-single
people:  Josien Visschedijk, Jan van den Brand, Wynand Alkema, Jack Wetzels, Djoerd Hiemstra
description: Development of a text mining system to accurately make a diagnosis from nephrology pathology reports.

## Background
Within the department nephrology, a biopsy is taken from patients for further research. This biopsy can be analyzed with three different methods:
* Light microscopy
* Immunofluorescence
* Electron microscopy

The analysis and the final diagnosis of the biopsy are documented in a pathology report. However, there is a suspicion that only light microscopy and immunofluorescence are required in making a diagnosis. In some cases, electron microscopy adds nothing to the process of making a diagnosis. There is demand for a decision supporting algorithm, which state a diagnosis, based on the text. Furthermore, this explainable algorithm makes the process of concluding such a diagnosis clear. In this way, certain characteristics of the kidneys can be extracted, which have led to a particular diagnosis. It can also show abnormalities in the decision making, in which human beings would decide otherwise.

## Research question and tasks
The main research question is: “Is it possible for a predictive algorithm to get to the same diagnosis as a human being when analyzing nephrology pathology reports?”

### Tasks
* Design a text mining algorithm which states a diagnosis based on text
* Compare the text mining algorithm with the performance of nephrologists
* Exclude some medical details (e.g. electron microscopy) to see whether the algorithm still performs the same

## Innovation
The goal of this project is to design a text mining algorithm, which makes (with a fairly high accuracy) the same diagnosis as a nephrologist would when analyzing pathology reports.
