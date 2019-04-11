title: SOL
title_long: SOL - Deep Learning GPU Cluster
finished: false
picture: sol-logo.jpg
template: project-single
groups: rse, diag
people: Paul Konstantin Gerke, Sil van de Leemput, Thomas de Bel, Erdi Calli, Matin Hosseinzadeh, Xie Weiyi, Patrick Brand
description: DIAG's deep learning cluster for training and applying automated image analysis tools.
bibkeys: 

## Background

The Diagnostic Image Analysis Group's goal is to improve image analysis tools
for clinicians. Since 2015, deep learning has become an essential tool for 
artificial intelligence, substatially improving the acurracy and generalizability 
on classical image classification techniques. In order to create high quality 
deep learning based algorithms for clinical practice, DIAG's AI researchers 
need to make use of high-power general purpose graphic processing units (GPGPUs).

SOL is DIAG's deep learning infrastructure. It offers researches access to 
a centralized pool of GPGPUs. It is used to create state-of-the-art tools
for detecting and classifying illnesses and quantify extent, and possible
treatment options.

## Capacity/Activity

| Resource               | Value                         |
| ---------------------- | ----------------------------- |
| Compute nodes          | 30                            |
| GPUs                   | 80                            |
| CPUs                   | 788                           |
| Total memory           | 3.5TB                         |
| Active users/month     | 40                            |
| Jobs run/month         | 7000                          |

## Architecture

SOL uses offers consists of a compute cluster of 80 GPUs (mainly NVIDIA GTX1080Ti
and RTX2080Ti cards), a dedicated 500 TB storage server for serving data to
deep learning compute nodes via 20 GBit networking, and a Prometheus/Grafana
based monitoring solution to monitor the activity and health of the cluster. 

![sol-cluster-architecture]({filename}/images/projects/sol-architecture.png "SOL's architecture overview")

Users log in to job nodes directly to either schedule an experiment or to
interactively interact with a scheduled experiment. We use slurm as an automated
job queue. Experiments are encapsialted in docker containers to isolate their 
software stacks from the system software stack. This allows researchers to try
out new libraries and software without the need to install new software on the
base systems.

## Future

The SOL compute cluster runs reliably for 1.5 years now. The cluster was 
steadily growing over that period and it will reach its maximum design capacity
of 100 GPUs this year. After this, we will consolidate and upgrade old hardware
and to remove non-stardard components and compute nodes from the cluster.

In addition to this, the compute cluster will be rolled out as a service to 
other departments of the hospital and we will start offering compute capabilites
built around SOL to other departments of Radboud University in 2019.

