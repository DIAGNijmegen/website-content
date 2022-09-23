title: Few-shot learning for medical image segmentation
groups: ai-for-health, diag
finished: false
type: student
picture: vacancies/segmentation.jpg
template: project-single
people: Niels van Hoeffelen, Bob Sanders, Bram van Ginneken, Silvan Quax
description: Develop a 3D segmentation method that can learn a task from only a few segmented 2D slices.

**Niels van Hoeffelen**<br>
**Start: **<br>
**End: **

**Bob Sanders**<br>
**Start: Nov 14, 2022**<br>
**End: May 14, 2023**

## Clinical problem
Segmentation of anatomical structures and lesions in 3D scans is important for many AI radiology applications. Convolutional neural networks such as the [U-net](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/), an encoder-decoder architecture with skip connections, generally produce good results when trained with a few hundred scans in which the structures to be segmented have been manually outlined. But annotating a few hundred scans is very time consuming. Moreover, a trained segmentation network may fail if it is applied to new cases that are somewhat different from the data is was trained on, for example because the new case contains abnormalities that were not well represented in the training data.

## Solution 
Recently it has been demonstrated that large language models such as [GPT-3](https://arxiv.org/abs/2005.14165) that have been trained a huge corpora of text in a self-supervised manner, can be quickly adapted to solve new tasks by providing them with only a few examples of the desired input and output (this is called few-shot learning). In this project, the goal is to investigate if it is possible to develop 2D segmentation methods that can learn a new tasks from only one or a few example slices with segmented output. Such a method could be used in an interactive setting to massively speed-up annotation of 3D scans; a user would segment one or a few slices and the few-shot 2D segmentation engine produces a 3D output by simply iterating over all slices.

Based on recent deep learning literature, we envision several strategies that could be explored to build a good few-shot 2D segmentation method. A small literature search is also part of the project before you embark on building a system. 

## Data 
We have many thousands of 3D scans available, consisting of hundreds of thousands 2D slices, in which a large number of objects have been manually segmented. These data sets can be used to develop the few-shot segmentation model. We will focus on applications in computed tomography (CT) and optical coherence tomography (OCT) scans. 

## Results
The project should result in a reusable method to speed-up the annotation of new 3D scans, possibly scans for which existing segmentation models produce poor results, so that those methods can be improved by retraining them with additional interactively corrected cases. We intend to make the model available on [grand-challenge.org](https://grand-challenge.org) and possibly write a publication.

## Embedding 
You will be embedded in the Department Of Medical Imaging at Radboudumc. We provide access to Sol, our large GPU cluster, and the cloud-based compute infrastructure of grand-challenge.org, powered by Amazon Web Services. 

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics, or Biomedical Sciences in the final stages of their Master education.
- You should be proficient in Python programming and have a theoretical understanding of deep learning
- Basic biological / biomedical knowledge is preferred.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- For more information or to apply for this project, please contact bram.vanginneken@radboudumc.nl.
