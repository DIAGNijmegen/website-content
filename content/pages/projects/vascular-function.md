title: Unraveling mechanisms of vascular function and regulation with causal discovery
finished: false 
type: general 
picture: vacancies/vascular-function.jpg 
people: Mirthe van Diepen, Gabriel Bucur, Jurgen Claassen, Tom Claassen, Tom Heskes
description: The aim of this project is to design a pipeline for applying causal structure discovery algorithms on healthcare data.
template: project-single 
groups: ai-for-health

## Project Description

Unraveling causal mechanisms behind variables in healthcare can be extremely helpful to get a better insight into the underlying model. The healthcare system can benefit from this knowledge by improving clinical prognosis based on the discovered causal relationships which can lead to the slowing down decline in cognition in Alzheimer's disease and prevention of adverse neurological outcomes in complex vascular surgery. Traditional study designs use random controlled trials (RCTs) to infer pairwise causal relationships. Unfortunately, it is not always possible to intervene on variables, for instance, due to ethical reasons or disability. Recently, increasing attention has gone to causal structure discovery which is designed to unravel causal mechanisms from observed data sets. In this project, we will use these techniques, to get a better understanding of the causal structure behind the short-term outcomes (mortality, ICU stay, delirium, stroke) and long-term outcomes (neurological function, cognition, vascular events) in thoracic aortic surgery.

Currently, in medical journals, the methods to analyze data usually do not cover causal structure discovery methods. The reason is that the assumptions made for causal structure discovery are difficult to test for, and the required definitions are seen as non-intuitive. In this project, we will bridge the gap between the theory behind causal structure discovery and its applications in healthcare. The first result of this project will be a protocol for applying causal structure discovery algorithms on healthcare data (see below the sketch of the protocol). 

Challenges of a healthcare data set can be (1) small sample size, (2) consisting of a complex combination of very different variables, both discrete and continuous, (3) unknown causal structure (there might be unknown confounders or cycles in the causal structure), (4) context variables and time-dependent variables (variables from the different phases in the perioperative period), and (5) missing values or censoring data. In the protocol, we will cover these challenges: we will show what to consider when choosing a causal discovery method and the impact of different choices for its hyperparameters. Moreover, we suggest how one can combine the outputs of causal discovery methods to make the outcome more robust for small data sets, how to deal with context variables, and how to deal with mixed data. 

Causal structure discovery techniques that are used in the protocol are FCI, BCCD, GPS, and JCI. We proposed an extension to FCI to obtain a more informative causal structure as for this technique more edges are oriented after running the FCI algorithm [1]. After having applied this protocol to the variables in the thoracic aortic surgery data set, we select direct risk factors based on the obtained causal structure. The second result of this project will be a prediction model that exploits causal knowledge to predict the probabilities of adverse outcomes of vascular surgery. Currently, the main risk factor is age, therefore, such a prediction model can have a meaningful impact on healthcare. 

![Sketch of the protocol for applying causal structure discovery on healthcare data.](https://github.com/DIAGNijmegen/website-content/assets/31853762/95e0aa8c-8bcf-4d07-9443-7b4d845a9365)

[1] Van Diepen, M. M., Bucur, I. G., Heskes, T., & Claassen, T. (2023). Beyond the Markov Equivalence Class: Extending Causal Discovery under Latent Confounding. In 2nd Conference on Causal Learning and Reasoning.
