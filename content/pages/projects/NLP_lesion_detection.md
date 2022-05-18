title: Natural language processing of radiology reports for lesion detection 
groups: ai-for-health, diag 
finished: false 
type: student 
picture: vacancies/NLP_lesion_detection.png
template: project-single
people: Manuela Bergau, Thomas van den Broek, Koen Dercksen, Max de Grauw, Bram van Ginneken
description: Develop a method to automatically find statements in radiology reports on the presence, size and type of lesions in CT scans. 

Manuela Bergau <br>
 **Start date: 10-01-2022** <br>
 **End date: 10-07-2022**
 
Thomas van den Broek <br>
 **Start date: 11-10-2021** <br>
 **End date: 11-04-2022**

## Clinical Problem 
The work of a radiologist is to describe relevant findings that can be seen in
an imaging study in the form of a free text report. Although radiologists learn
to report their findings in specific ways, following a certain writing style
and vocabulary, and sometimes even start from templates that relate to the
clinical question and the type of scan acquired, the text is to a large extent
unstructured. If we want to use the images and their reports for research, this
is a big limitation. It is also an interesting challenge for natural language
processing (NLP) researchers.

Converting radiology reports into structured information would have many
possible applications. In this project, we focus on lesions that are visible in
CT scans. Radiology reports list the presence of such lesions, and often
contain numbers from measurements of the size of the lesion and provide the
type of lesion and mention where the lesion is located. For example, the report
may say *“Nodus in de linker bovenkwab, 7 mm, binnen marge van meetfout
ongewijzigd vergeleken met vorig onderzoek, is afgenomen vergeleken met <DATE>
(zie ima 83 serie 4).”* We are looking for an accurate automatic method to
extract this information from radiology reports.

There are two direct use cases for this method related to two ongoing PhD
research projects at Radboudumc and Radboud University. The first is to use
text-processing to efficiently collect more training and validation data to
improve a universal lesion segmentation algorithm that has been developed by
[Max de Grauw]( https://www.diagnijmegen.nl/people/max-de-grauw/). The second
is to prepare parts of an annotated radiology report that is more
understandable to a patient, the task addressed in the project of [Koen
Dercksen]( https://www.diagnijmegen.nl/projects/mihracle/).

## Data
A database of 250,000 Dutch radiology reports from CT studies where the thorax,
abdomen or both were imaged are available. Protected health information has
been removed from these reports using in-house developed tools. All studies
were done at Radboudumc between 2000 and 2021.

## Methods
We propose a solution to this problem in the form of an algorithm that
determines which words are possible lesion words and which other words in the
report pertain to a particular lesion, known as relation extraction. This is
done by employing a multi-task learning algorithm that uses BERTje (BERT for
dutch texts) as its shared layers between the described main task and several
auxiliary tasks. The auxiliary tasks used are part of speech tagging, lesion
detection in the reports, and SNOMED mention detection; SNOMED is a medical
vocabulary database. A second objective is to perform coreference resolution to
offer a complete overview of the information that is present for each lesion.

## Results
We trained the multi-task learning model on 78 different reports which yielded
297 different data points. These reports were selected based on several
criteria aimed at maximizing the relevant information per report. The algorithm
managed to obtain an F1 score of 0.91 on the relation extraction task. However,
the coreference task proved to be too challenging for the current setup and
relatively small amount of available labelled data points and only managed to
obtain an F1 of 0.51. Regardless, the main purpose of the algorithm, i.e.,
relation extraction was quite successful.

![nlp-radiology-reports]({{ IMGURL }}/images/projects/NLP_lesion_detection_RE.png)
 
The examples above serve to illustrate the functioning of the algorithm. The
words in red show which word was used as a target for the prediction, the words
in yellow are the words that the algorithm predicted belong to said target
word.
