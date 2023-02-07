title: Unraveling mechanisms of vascular function and regulation with causal discovery
finished: false 
type: general 
picture: vacancies/vascular-function.jpg 
people: Mirthe van Diepen, Gabriel Bucur, Jurgen Claassen, Tom Claassen, Tom Heskes
description: The aim of this project is to design a pipeline for applying causal structure discovery algorithms on healthcare data.
template: project-single 
groups: ai-for-health

## Project Description

Unraveling causal mechanisms behind variables in healthcare can be extremely helpful to get a better insight into the underlying model. The healthcare system can benefit from this knowledge by improving clinical prognosis based on the discovered causal relationships which can lead to the slowing down decline in cognition in Alzheimer's disease and prevention of adverse neurological outcomes in complex vascular surgery. Traditional study designs use random controlled trials (RCTs) to infer pairwise causal relationships. Unfortunately, it is not always possible to intervene on (proxy) variables, for instance, due to ethical reasons or disability. Recently, increasing attention goes to causal structure discovery which is designed to unravel causal mechanisms from observed data sets. In this project, we will use these techniques, to get a better understanding of the causal structure behind the short-term outcomes (mortality, ICU stay, delirium, stroke) and long-term outcomes (neurological function, cognition, vascular events) in thoracic aortic surgery.

Currently, in medical journals, the methods to analyze data usually do not cover causal structure discovery methods. The reason is that the assumptions made for causal structure discovery are difficult to test for, and the required definitions are seen as non-intuitive. The main goal of this project is to bridge the gap between the theory behind causal structure discovery and its applications in healthcare. The result of this project will be a pipeline for applying causal structure discovery algorithms on healthcare data (see below the sketch of the pipeline). 

Challenges of a healthcare data set can be (1) small sample size, (2) consisting of a complex combination of very different variables, both discrete and continuous, (3) unknown causal structure (there might be unknown confounders or cycles in the causal structure), (4) context variables and time-dependent variables (variables from the different phases in the perioperative period), and (5) missing values or censoring data. In the pipeline, we will cover these challenges: will show what to consider when choosing a causal discovery method and the impact of different choices for the hyperparameters for it. Moreover, we suggest how one can combine the outputs of causal discovery methods to make the outcome more robust for small data sets, how to deal with context variables, and how to deal with mixed data. 

Causal structure discovery techniques that are used in the pipeline are FCI, BCCD, GPS, DCD, JCI, LiNGAM, and CCD. We proposed an extension to FCI to obtain a more informative causal structure as for this technique more edges are oriented after running the FCI algorithm. Another goal is to combine causal structures obtained from a smaller data set with more variables, and a bigger data set with fewer variables containing the former, so that we can benefit from both many variables and more reliable information.


![Sketch of the pipeline for applying causal structure discovery on healthcare data.](https://user-images.githubusercontent.com/31853762/217268070-268f52db-ee20-461c-b122-92fe620ec33f.png)
