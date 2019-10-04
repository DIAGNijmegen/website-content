title: Automated detection of nodules attached to the pleural and mediastinal surface in low-dose CT scans
authors: B. van Ginneken, A. Tan, K. Murphy, B.J. de Hoop and M. Prokop
has_pdf: True
template: publication
bibkey: ginn08b
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 6915 of SPIE, 2008, pages 69150X1-69150X10
doi: https://doi.org/10.1117/12.772298
This paper presents a new computer-aided detection scheme for lung nodules attached to the pleural or mediastinal surface in low dose CT scans. First the lungs are automatically segmented and smoothed. Any connected set of voxels attached to the wall - with each voxel above minus 500 HU and the total object within a specified volume range - was considered a candidate finding. For each candidate, a refined segmentation was computed using morphological operators to remove attached structures. For each candidate, 35 features were defined, based on their position in the lung and relative to other structures, and the shape and density within and around each candidate. In a training procedure an optimal set of 15 features was determined with a k-nearest-neighbor classifier and sequential floating forward feature selection. The algorithm was trained with a data set of 708 scans from a lung cancer screening study containing 224 pleural nodules and tested on an independent test set of 226 scans from the same program with 58 pleural nodules. The algorithm achieved a sensitivity of 52% with an average of 0.76 false positives per scan. At 2.5 false positive marks per scan, the sensitivity increased to 80%.

