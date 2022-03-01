title: Quantification of immunohistochemical markers for improved prostage cancer prognostics
groups: ai-for-health
finished: false
type: student
picture: projects/ih-prostate_diagnostics.png
template: project-single
people: Sasha Peerdeman, Jolique van Ipenburg, Geert Litjens
description: Development of a model for the quantification of immunohistochemical markers for improved prostage cancer prognostics

**Start date: 10-01-2021** <br>
**End date: 10-07-2022**

## Clinical Problem
In prostate cancer, patient treatment for a major part is determined by the subjective morphological assessment of removed tissue, the Gleason Grade. However, we know that other biomarkers have prognostic potential, such as cell division markers as a surrogate for tumor growth (Ki-67 staining) or the presence and composition of immune infiltrates (CD3 / CD8 staining). However, these markers are not used in practice because it is impossible to quantify them accurately across large swathes of tissues by human experts. We propose to develop AI system which automatically quantify these biomarkers and combines that with existing models for tumor segmentation and grading. This will allow us not just to quantify the markers within digitized microscopy images, but also identify their spatial arrangement.

## Solution
The student will need to adapt and improve existing methods to work across a variety of different immohistochemical stains. Currently our group has both detection (YOLO) and segmentation (U-net) based models for a single immunohistochemical stain (CD3) Improving these methods includes better handling of overlapping and connecting cells and improving generalization to different counterstains (e.g. brown, red, green).

## Data
We have multi-center data with 4 immunohistochemical stains (CD3, CD8, PD-L1, Ki67) from around 400 patients. Data is source from Radboudumc, Rijnstate Hospital and Erasmus Medical Center. Each patient has between 4 – 12 distinct whole-slide images for each stain. For each patient we have follow-up data for at least 5 years (biochemical recurrence yes/no) with which we can correlate the obtained cell counts.

## Innovation
The main innovation will be an IHC quantification algorithm that can generalize to a variety of IHC stains with different staining profiles and counterstains. Such an algorithm would be valuable for many clinical applications, although it would have to be further validated for different organs.
