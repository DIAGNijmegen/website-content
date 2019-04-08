title: SOL
title_long: SOL - Deep Learning GPU Cluster
finished: false
picture: sol-logo.png
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

## Architecture

SOL uses offers consists of a compute cluster of 80 GPUs (mainly NVIDIA GTX1080Ti
and RTX2080Ti cards), a dedicated 500 TB storage server for serving data to
deep learning compute nodes via 20 GBit networking, and a Prometheus/Grafana
based monitoring solution to monitor the activity and health of the cluster. 

![sol-cluster-architecture]({filename}/images/projects/sol-architecture.png "SOL's architecture overview")

The cluster uses Slurm as job scheduler and docker to encapsulate experiments and
isolate the software stacks of different experiments from each other.