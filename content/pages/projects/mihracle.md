title: Building multi-modal interactive health records
finished: false
type: general
picture: projects/mihracle.jpg
people: Koen Dercksen, Arjen de Vries, Faegheh Hasibi, Liesbeth Langenhuysen, Monique Brink, Ritse Mann, Bram van Ginneken 
description: The aim of this project is to build a system that can automatically create annotated radiology reports that a patient can understand.
template: project-single
groups: diag, ai-for-health

## Project Description

Can we use multi-modal analysis of medical health records to inter-link the textual and image information and present the data in an intuitively clear manner?

Today, patients access their medical information using the [mijnRadboud portal](https://www.radboudumc.nl/en/patient-care/mijnradboud). Medical records are however not written with the patient in mind - the vocabulary gap between language that the patient would understand and the actual contents of their electronic health records is huge. Online health records will also include medical images, where even experts with extensive medical training rely on the support of radiologists to interpret that information. 

The proposed project explores (semi-)automatic methods to transform electronic health records (EHRs) into an interactive online version that is easily explored and understood by the patient. To reduce the vocabulary gap, we will transform the textual information in the health record and/or link it to medical knowledge graphs. The scientific question is whether textual and image information reinforce each other to improve effectiveness of these methods. A specific problem to overcome is limited availability of resources for processing Dutch medical health records. Developing word embeddings, entity tagging and knowledge graph extraction from Dutch medical records will have sustainable impact on health innovation at RadboudUMC.

## Results
Initially, we are working on linking EHR text to medical knowledge bases. These links can then be used to provide additional information to patients on certain medical terms like diseases, body locations and other findings.

In the paper [*First Steps Towards Patient-Friendly Presentation of Dutch Radiology Reports*](http://ceur-ws.org/Vol-2619/paper1.pdf) (ECIR2020), we present preliminary work on preparing Dutch radiology reports for entity linking to provide additional information to patients. It provides an overview of existing resources and touches on subjects like data anonymisation and annotation, as well as potential word embedding techniques and models.

Alongside these ongoing efforts, we are also closely involved in the development of [Radboud Entity Linker (REL)](https://github.com/informagi/REL), a state-of-the-art open source entity linking package that we are now enhancing for medical entity linking. A paper on REL was [published at SIGIR2020](http://hasibi.com/files/sigir2020-REL.pdf), demonstrating state-of-the-art performance on classical entity linking datasets. We hope to eventually use REL (amongst other systems) for linking entities in Dutch EHRs.
