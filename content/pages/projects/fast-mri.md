title: Interventional reconstruction AI for real-time needle tracking in MRI
groups: ai-for-health
finished: true
type: student
picture: vacancies/fast-mri.png
template: project-single
people: Stan Noordman
description: Development of an interventional reconstruction algorithm for real-time needle tracking in MRI


## Clinical Problem
The primary bottleneck for interventional MRI is accurately positioning instruments in the correct position relative to the lesion. The instruments, operated by hand or robots, move unpredictably and currently require a careful and iterative process of move - scan - move - scan until the position is satisfactory. Conversely, the lesion moves much less and can generally be assumed to stay within a region.

Guiding a percutaneous needle towards the region of interest in a prostate biopsy may take several minutes per biopsy. Cryoablation interventions, for example, use several needles and may take hours to position correctly. MRI-guided interventions can be made faster and more accurate by developing solutions allowing for real-time acquisitions, greatly improving current time-consuming processes.


## Solution
Based on previous work showing dynamic deep-learning algorithms capable of reconstructing highly undersampled acquisitions, we modified a CRNN-MRI algorithm to reconstruct the sagittal and transverse images of a pelvis containing a biopsy needle in a dynamic fashion. In this project, we will integrate an existing segmentation AI into our reconstruction algorithm, employ various experiments to improve its performance, and subsequently integrate a trained model into simulation to show its performance in a simulated environment.

The student is invited to come up with other experiments that show improvement over the base model, exceptional students may propose using a different base algorithm if they think it would be better.


## Data
The dataset consists of 142 patients and 144 cases. These are biopsies, with each case containing at least 5 sagittal or transverse pairs of shape 256x256x5. The total number of files is 1820.

## Approach
For model development, we provide access to our deep learning GPU cluster, SOL.
