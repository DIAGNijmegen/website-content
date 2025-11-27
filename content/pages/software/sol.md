title: SOL
title_long: SOL - Deep Learning GPU Cluster
finished: false
picture: software/sol-logo.jpg
template: project-single
groups: rse, diag, rtc
people: Rita Bijlsma, Paul Konstantin Gerke, Sil van de Leemput, Thomas de Bel, Matin Hosseinzadeh, Xie Weiyi, Patrick Brand
description: RTC AI's cluster for training and applying automated image analysis tools.
bibkeys: 

The Diagnostic Image Analysis Group's goal is to improve image analysis tools
for clinicians. Since 2015, deep learning has become an essential tool for 
artificial intelligence, substantially improving the accuracy and generalizability 
on developed image classification techniques. In order to create high quality 
deep-learning based algorithms for clinical practice, AI researchers 
require the use of high-power general-purpose graphic processing units (GPGPUs).

SOL is the RTC AI's infrastructure. It offers researchers access to 
a centralized pool of GPGPUs. It is used to create state-of-the-art tools
for detecting and classifying illnesses and quantify extent and identify possible
treatment options for diseases.

## Capacity/Activity

| Resource               | Value                         |
| ---------------------- | ----------------------------- |
| Compute nodes          | 40                            |
| GPUs                   | 100                           |
| CPUs                   | 788                           |
| Total memory           | 3.5TB                         |
| Active users/month     | 40                            |
| Jobs run/month         | 7000                          |

## Architecture

SOL is a compute cluster which consists of 40 compute nodes that give access
to a pool of 100 GPUs (mainly NVIDIA GTX1080Ti
and RTX2080Ti cards), a dedicated 500 TB storage server for serving data to
deep learning compute nodes using 20 Gbit networking, and a 
[Prometheus](https://prometheus.io/)+[Grafana](https://grafana.com/)
based monitoring solution to monitor the activity and health of the cluster. 

![sol-cluster-architecture]({{ IMGURL }}/images/software/sol-architecture.png "SOL's architecture overview")

Users log in to job nodes directly to either schedule an experiment or to
interact with a running experiment using 
[Jupyter Notebooks](https://jupyter.org/). We use 
[Slurm](https://slurm.schedmd.com/overview.html) as an automated
job queue. Experiments are encapsulated in 
[docker containers](https://www.docker.com/) to isolate their 
software stacks from the base systems of our compute nodes. This allows 
researchers maximum flexibility when it comes to trying out new, experimental 
libraries and software without us needing to install it on the base systems
ourselves.

## Future

The SOL compute cluster now runs reliably since mid-2017. The cluster is planned
to steadily grow until the end of 2019 when it will reach its maximum design capacity
of 100 GPUs. After this point, plans are to consolidate and upgrade old hardware
and to remove non-stardard components and compute nodes from the cluster.

In addition to this, the compute cluster will be rolled out as a service to 
other departments of the hospital and we will start offering compute capabilites
built around SOL to other departments of Radboud University in 2021.

