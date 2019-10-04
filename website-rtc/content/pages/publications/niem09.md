title: Fast detection of the optic disc and fovea in color fundus photographs
authors: M. Niemeijer, M.D. Abràmoff and B. van Ginneken
has_pdf: True
template: publication
bibkey: niem09
published_in: Medical Image Analysis
pub_details: <i>Medical Image Analysis</i> 2009;13(6):859-870
doi: https://doi.org/10.1016/j.media.2009.08.003
pmid: http://www.ncbi.nlm.nih.gov/pubmed/19782633
A fully automated, fast method to detect the fovea and the optic disc in digital color photographs of the retina is presented. The method makes few assumptions about the location of both structures in the image. We define the problem of localizing structures in a retinal image as a regression problem. A kNN regressor is utilized to predict the distance in pixels in the image to the object of interest at any given location in the image based on a set of features measured at that location. The method combines cues measured directly in the image with cues derived from a segmentation of the retinal vasculature. A distance prediction is made for a limited number of image locations and the point with the lowest predicted distance to the optic disc is selected as the optic disc center. Based on this location the search area for the fovea is defined. The location with the lowest predicted distance to the fovea within the foveal search area is selected as the fovea location. The method is trained with 500 images for which the optic disc and fovea locations are known. An extensive evaluation was done on 500 images from a diabetic retinopathy screening program and 100 specially selected images containing gross abnormalities. The method found the optic disc in 99.4\% and the fovea in 96.8\% of regular screening images and for the images with abnormalities these numbers were 93.0\% and 89.0\% respectively.

