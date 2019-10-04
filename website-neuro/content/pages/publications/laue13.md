title: Automated Artery and Vein Detection in Dynamic CT data with an Unsupervised Classification Algorithm of the Time Intensity Curves
authors: H.O. A. Laue, M.T. H. Oei, L. Chen, I.N. Kompan, H.K. Hahn, M. Prokop and R. Manniesing
has_pdf: True
template: publication
bibkey: laue13
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, 2013
doi: https://doi.org/10.1117/12.2008116
In this work a fully automated detection method for artery input function (AIF) and venous output function (VOF) in 4D-computer tomography (4D-CT) data is presented based on unsupervised classification of the time intensity curves (TIC) as input data. Bone and air voxels are first masked out using thresholding of the baseline measurement. The TICs for each remaining voxel are converted to time-concentration-curves (TCC) by subtracting the baseline value from the TIC. Then, an unsupervised K-means classifier is applied to each TCC with an area under the curve (AUC) larger than 95% of the maximum AUC of all TCCs. The results are three clusters, which yield average TCCs for vein and artery voxels in the brain, respectively. A third cluster generally represents a vessel outside the brain. The algorithm was applied to five 4D-CT patient data who were scanned on the suspicion of ischemic stroke. For all _ve patients, the algorithm yields reasonable classification of arteries and veins as well as reasonable and reproducible AIFs and VOF. To our knowledge, this is the first application of an unsupervised classification method to automatically identify arteries and veins in 4D-CT data. Preliminary results show the feasibility of using K-means clustering for the purpose of artery-vein detection in 4D-CT patient data.

