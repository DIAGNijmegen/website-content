title: Body composition assessment in 3D CT and MR images
groups: ai-for-health, diag
finished: false
type: student
picture: projects/body-composition.jpg
template: project-single
people: Lena Philipp, Nikolas Lessmann, Matthieu Rutten, Bram van Ginneken
description: Automatic quantification of muscle and fat tissue in 3D CT and MR images

## Clinical problem
The composition of the body in terms of muscle and fat mass is a precise measure of the physical state of the patient. This information has many practical applications in clinical routine care, such as monitoring treatment response to chemotherapy and immunotherapy in patients with cancer, or predicting clinical outcomes in other patients. While every hospital routinely acquires hundreds of cross-sectional imaging studies (CT and MRI scans) every day that would be suitable for deriving precise body composition measurements, this potential currently remains unused. Measuring fat and muscle mass would require manually delineating tissues depicted in the scan, which is labor-intensive and time-consuming.

## Aim of the project
The project aims to develop deep learning algorithms for automatic delineation (segmentation) of fat and muscle compartments in 3D CT and MRI scans. These segmentations will then be used to allow radiologists to routinely include fat and muscle mass into their reports. Next to semantic segmentation in medical images, the project also involves finding solutions for various practical challenges, such as efficient data annotation, automatic recognition of suitable scans, and extrapolation in scans with incompletely depicted body parts.
