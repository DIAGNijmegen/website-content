title: CIRRUS Lung Screening
title_long: CIRRUS Lung Screening
finished: false
picture: software/cirruslungs_workstation.png
template: project-single
groups: rse, diag
people: Haimasree Bhattacharya, Paul Konstantin Gerke, Joep Kamps, Colin Jacobs, Mathias Prokop, Bram van Ginneken
description: This workstation is a highly optimized reading platform that allows fast and standardized reading of lung screening CT scans.
disable_gradient: true
bibkeys:

## Aim
This software is aimed to facilitate research collaborations between a
network of clinical and technical partners that is needed to address
the challenge of cost effective and efficient lung CT screening. A
radiologist can quickly and accurately report chest CT scans and
produce a standardized report with CIRRUS Lung Screening according to
Lung-RADS guidelines. AI algorithms developed within DIAG are integrated
 into the workstation to allow for more accurate and faster
 interpretation of CT scans and extraction of a rich set of biomarkers.
In addition to screen for lung cancer, the workstation is also aimed to
screen for two other conditions for which heavy smokers are at risk:
chronic obstructive pulmonary disease (COPD) and cardiovascular
diseases.

## Software
This software includes computer-aided detection and volumetric
measurements for both solid and subsolid nodules. The workflow can be
categorized into three steps - processing, reading and reporting.
During the processing stage, input DICOM data is validated first. Then,
lung, airway and vessel, lobe and segments are segmented. Various CAD
systems are run to detect nodules, which is then followed by a
dedicated lung CT registration algorithm to register a new scan with
prior scans. All nodules from the prior scans are propagated
automatically to the new scan. Finally, the prior findings and the CAD
marks are merged. This software also provides a functionality to
propagate a newly found nodule retroactively through the previous scans.
![Workstation]({filename}/images/software/cirruslungs_workstation.png)
*CIRRUSLungS workstation*

After a user has finished reading, a structured report is automatically
generated. The report provides general patient information, gives a
quick overview of the annotated findings and their characteristics and
optionally provides follow-up recommendations according to the
BTS/Fleischner/LungRADS guidelines. The suggested follow up and other
case comments can be added to the report. Finally, the user signs off
the case and proceeds with the next one.
![Workstation]({filename}/images/software/cirruslungs_report.png)
*CIRRUSLungS report*

## Usage
There are two different versions of our software. The research version
 runs the processing pipeline on our in-house clusters and contains
 experimental features. The commercial version,
 <a href="https://www.veolity.com/">Veolity</a>, uses a client-server
 architecture, has communication with PACS systems integrated, can use
 PACS as a storage database, divides worklists over multiple clients,
 and is CE and FDA certified. Both versions are in active use at sites
 in North America, Europe, Asia and Australia.
