title: Grand-challenge.org
title_long: Grand Challenges in Biomedical Image Analysis
finished: false
picture: software/grand-challenge.png
template: project-single
groups: rse, diag, rtc
people: James Meakin, Sjoerd Kerkstra, Paul Konstantin Gerke, Harm van Zeeland, Karel Gerbrands, Bram van Ginneken
description: The home of challenges in biomedical imaging.

bibkeys:
github: https://github.com/comic/grand-challenge.org


We develop and maintain [grand-challenge.org](https://grand-challenge.org), a Django site for hosting challenges in biomedical imaging, annotating data and making deep learning models accessible to clinicians. This text is adapted from our abstract at the [Challenges in Machine Learning workshop at NeurIPS 2018](https://nips.cc/Conferences/2018/Schedule?showEvent=10909).

## Introduction

An increasing reliance on imaging for clinical decision making and an ageing population has resulted in an unprecedented demand for trained personnel to interpret medical images. As this demand is unable to be met there is consequently an increased workload for physicians, increasing the likelihood of interpretation errors. Computer-aided detection and diagnosis systems have been developed to assist in reducing this workload and to enable more reliable clinical decisions. Challenges in biomedical image analysis have proven successful in driving innovation in creating algorithms that form components of these systems. However, for the algorithm developer, there exists a validation gap between performing well on the curated challenge data to transitioning to the clinic where imaging devices, scanning protocols and populations can vary significantly, and integration with heterogeneous clinical systems and clinicians' workflows is non-trivial.

Since 2012, as part of the Consortium for Open Medical Image Computing, we have developed and maintained an open source framework for hosting challenges in biomedical imaging, and support an instance of this at [grand-challenge.org](https://grand-challenge.org). Here, we have hosted successful challenges across various medical domains, such as LUNA16 for lung nodule detection, CAMELYON16/17 in digital pathology and The Medical Imaging Decathlon for 10 segmentation tasks in CT and MRI. The platform is now integral to our groups work, from private challenges used in educational courses to reproducibility of scientific output and archiving of developed algorithms. The platform has recently been extended to assist the algorithm developer in clinical validation by allowing clinicians to execute algorithms on their own data via a web interface.

The grand-challenge.org project is developed on GitHub and consists of 3 main components:

-   [the grand-challenge.org framework](https://github.com/comic/grand-challenge.org), a re-usable platform for hosting challenges.
-   [Evalutils](https://github.com/comic/evalutils), a pip installable python package that assists challenge administrators in creating Docker containers for evaluating submissions from challenge participants.
-   [CIRRUS](/software/cirrus/), a platform for developing medical imaging workstations that integrates with clinicians' workflows.

Whilst grand-challenge and evalutils are open source and licensed under Apache 2.0 and MIT respectively, CIRRUS is currently closed source but alternative viewers that integrate with the grand-challenge API could also be used, such as AMI or Cornerstone.

## The Grand-Challenge.org Framework

The platform is a web application that uses Django 2.1, backed by a PostgreSQL database and a Celery task queue with a Redis message broker. The application is distributed as a set of Docker containers, which are automatically published to Docker Hub after all tests have passed in Travis-CI. A Docker Compose file allows site administrators to quickly launch another instance of the framework on their own infrastructure, or for developers to replicate the entire stack on their machine.

We maintain an instance of the framework at [grand-challenge.org](https://grand-challenge.org). Here, anyone can join the site and become a challenge administrator by creating their own challenge. Other users are also able to join the site, sign up as participants in particular challenges and collaborate on solutions as teams. Currently, there are 24,000+ users, participating in 160+ public and private challenges hosted on the site. We also index challenges in medical imaging hosted on other sites, providing a valuable resource to the community in searching for datasets and benchmarks relevant to their tasks.

A challenge in the framework consists of a set of pages that describe the challenge, datasets for training and testing, the ground truth annotations for those datasets, and a method to evaluate submissions. Challenge participants submit their predictions as CSV files or ITK images. Each submission will be evaluated using that challenges evaluation method, which is provided by the challenge administrator as a Docker image. An instance of the evaluation image will be launched with the current submission attached as a Docker volume, and the container must produce a JSON file containing the score for this submission, which is then aggregated in the database. Instances of these images will be scheduled by Celery on an available Docker host, which for security reasons could be inside an isolated virtual machine.

Whilst challenge administrators are free to implement the evaluation in any language they choose, we have developed [Evalutils](https://github.com/comic/evalutils), a Python 3.6+ package that assists the creation of evaluation containers. The package uses CookieCutter to generate project templates for Classification, Segmentation and Detection challenges, provides methods to validate submissions and give feedback to the participants, and to score evaluations using a statistics library designed for medical imaging tasks.

## Reproducible Science

Researchers are now able to use the framework as a platform for reproducible science and algorithm archival. If the data can be shared publicly they are separately archived to [Zenodo](https://zenodo.org/) where they receive a DOI or distributed via [Academic Torrents](http://academictorrents.com/) if the data are large. Those developing algorithms set their problem up as a challenge on grand-challenge.org and are expected to produce three containers:

-   a training container that trains the model and produces all the figures in the paper,
-   a model container that executes the model on new data and produce a prediction,
-   an evaluation container that will score predictions.

Whilst the training container is archived and executed on our HPC systems, researchers are able to upload model containers to Grand Challenge in the same manner as for evaluation containers.

## Integration into Annotation Workflows and Clinical Use

For clinical validation, these models need to be executed on diverse data from heterogeneous sources. Authorised algorithm users are now able to upload their own data and generate predictions from any the archived model containers available to them. Instances of these model containers are scheduled in a similar manner to the evaluation containers, only that the Nvidia Docker runtime is used and a GPU is attached to the container instance if required.

The predictions generated then need to be assessed in an environment the clinician is familiar with. Our group has previously developed CIRRUS for creating workstations, which is built on MeVisLab and has been used as part of commercial CE and FDA certified products for Chest-CT screening. We have now extended the platform to make it accessible via a web browser so that clinicians are able to launch viewer instances wherever they are located, access algorithms and load any image and prediction available to them on Grand Challenge via a REST API. A clinician can then provide feedback on algorithm performance, generating more ground truth data by correcting the predictions, helping the algorithm developer close the validation gap.
