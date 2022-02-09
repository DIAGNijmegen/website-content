title: Identification of drug repurposing candidates for myotonic dystrophy by Graph Convolutional Networks
groups: ai-for-health
finished: false 
type: student 
picture: vacancies/MD_drug_repurposing.png
template: project-single
people: Djesse Dirckx, Lotte Willems, Peter-Bram t Hoen, Tom Heskes
description: Develop a method to identify of drug repurposing candidates for myotonic dystrophy by Graph Convolutional Networks

**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical Problem 
Myotonic dystrophy type 1 (DM1) is a rare, inherited, progressive and multisystemic disorder. It is the most common adult form of muscular dystrophy, with an estimated prevalence of 1:8000. Typical signs and symptoms of the disease include progressive muscle weakness and wasting from distal to proximal, ptosis, weakness of facial, jaw and anterior neck muscles, myotonia, daytime sleepiness, fatigue and cataracts. DM1 is one of the most variable human diseases, has complex, multisystemic and progressively worsening clinical manifestations and leads to severe physical impairment, restricted social participation and premature death. DM1 is a neglected disease on various levels. No curative treatment exists, and treatment by gene or genetic therapies lies still far in the future. Since patients would benefit enormously from treatment of debilitating symptoms like muscle weakness, fatigue and aberrant sleeping behaviour, we propose a drug repurposing strategy that should speed up the clinical development of drugs for DM1, using drugs that have already been (FDA) approved for treatment of other disorders and have known safety and pharmacokinetic profiles. Metformin is an example of a repurposed drug with positive effects on DM1 clinical symptoms in a small clinical trial. To identify more of these drug repurposing candidates, we need to make optimal use of the existing knowledge of the clinical overlap between diseases, the molecular targets of FDA-approved drugs and the genes / proteins relevant for the disease. This knowledge can be represented by a drug repurposing knowledge graph. Advanced deep learning methods that use graphs as input (graph neural networks) can be exploited to learn about new relationships between drugs and diseases worth following up in preclinical and clinical research.

## Solution 
In your project you, and in collaboration with biomedical and bioinformatics students, you will extract and extend a drug repurposing knowledge graph based on public resources. This will be a multimodal network with genes/proteins, diseases and drugs as nodes. Edges within the different layers represent functional similarity between genes, overlap in clinical symptoms between diseases and overlap in activity profiles between drugs. Edges between the different layers include known gene-disease, drug-gene/protein target and drug-disease relationships. You will then use and optimize an emerging AI framework called Graph Convolutional Networks to learn the local embedding of the nodes in the multimodal network. You will implement a previously [published](https://arxiv.org/abs/2007.10261) [GCN framework](https://github.com/gnn4dr/DRKG/) and study the effect of introducing a more extensive drug repurposing knowledge graph. You will then identify drug repurposing candidates by training on the node and edge properties of successful / published drug repurposing candidates. Finally, you will study the effect by updating the network on the genes most relevant to DM1, using gene expression profiling data gathered in-house and by collaborators. The top ranked drug repurposing candidates will be evaluated based on known druggable pathways in DM1. New candidates will later be tested in relevant cell and animal models, and eventually clinical trials.

## Data 
You will create a data repurposing knowledge graph based on public resources like [OpenTargets](https://www.opentargets.org) and [DisGeNet](https://www.disgenet.org). Lists of successfully repurposed drugs will be extracted from the [ReDo database](https://www.anticancerfund.org/en/redo-db) and published literature reviews. DM1 expression profiles have been processed and analysed in-house. 

## Embedding 
You will be embedded in the Center for Molecular and Biomolecular Informatics at Radboudumc, and collaborate closely with the Data Science department of the Institute for Computing and Information Systems. We provide access to CPU and GPU clusters, direct supervision by PhD students and regular meetings with the PIs of this project. 
