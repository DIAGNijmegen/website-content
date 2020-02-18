title: Muscle and fat segmentation in 3D CT images for body composition assessment
groups: diag, ai-for-health
finished: false
type: student
picture: vacancies/body-composition.jpg
template: project-single
people: Thijs van den Hout, Nikolas Lessmann, Alina Vrieling, Matthieu Rutten
description: Develop deep learning algorithms for segmentation of muscles and fat tissue in 3D CT images.

## Clinical problem
Body composition is an important biomarker in the treatment of cancer. In particular, low muscle mass has been associated with
higher chemotherapy toxicity, shorter time to tumor progression, poorer surgical outcomes, impaired functional status, and
shorter survival. However, because CT-based body composition assessment requires outlining the different tissues in the image,
which is time-consuming, its practical value is currently limited. The different tissue types are often outlined manually and
only in a single slice of a CT scan at the level of the third vertebra (L3). This is based on the observed linear relation
between cross-sectional areas and total body volume of muscle and fat. However, 2D estimates are still less accurate than
3D measurements. For use in both routine care and in research studies, automatic segmentation of the different tissue types is
desirable, especially if that would enable quantification of various tissue types in the whole 3D scan rather than a single slice.

## Innovation
The goal is to develop a deep learning algorithm that automatically outlines different muscles and fat in 3D CT scans. An important
aspect of this project is also the implementation as an easy to use web-app so that the software can be used by clinical researchers.
