title: Three dimensional oral and maxillofacial surgical outcome prediction
groups: ai-for-health
finished: true
type: student
picture: vacancies/soft_tissue.png
template: project-single
people: Niels van Nistelrooij, Guido de Jong, Shankeeth Vinayahalingam, Tom Loonen, Tong Xi, Thomas Maal
description: Development of a deep learning method that can generate 3D facial profiles of a patient after orthognathic surgery provided the planned surgical parameters.

**Start date: 25-01-2021** <br>
**End date: 24-08-2021**

## Clinical problem
Orthognathic surgery cuts and reshapes the bones comprising the jaws. These jaw displacements are mainly performed for functional improvements, such as alleviating malocclusion or asymmetries. A virtual planning of the surgery is routinely used that pre-operatively separates and positions the jaw bones by manipulating hard tissue 3D models. These virtual plannings are shown to the patient to inform them of the procedure and to show the expected result.
// They are also used to print molds that increase the precision of the actual surgery compared to the planned surgery.

![omf-prediction]({{ IMGURL }}/images/projects/omf_prediction_planning.png)

The jaw displacements often lead to significant changes to the patient's facial profile. If the virtual planning would additionally take these changes into account, the surgery is more likely to provide aesthetical improvements as well. Furthermore, presenting the expected facial profile during pre-operative doctor-patient communication can alleviate anxiety in the patient and provides a more pragmatic account of the changes after the surgery. The goal of the project was thus to predict a patient's facial profile after orthognathic surgery given their pre-operative facial profile and the surgical parameters from the virtual planning.

![omf-prediction]({{ IMGURL }}/images/projects/omf_prediction_example.png)

## Methods
A facial profile was represented as a mesh: a set of points in 3D space connected with triangles. A novel method discretized a mesh into a sparse grid where each grid cell contains features that characterize the triangles within the grid cell, so-called quadric error metrics (QEMs). Such a discretization could be transformed back to a mesh with a limited loss of quality.

![omf-prediction]({{ IMGURL }}/images/projects/omf_prediction_qems.png)

The AI method then introduced a neural network that encodes a discretized facial profile to a fixed number of features. The surgical parameters from the virtual planning were then appended to these features and the concatenation was decoded to produce the output sparse grid with QEMs. This predicted discretization was subsequently transformed back to a mesh to produce the final result.

![omf-prediction]({{ IMGURL }}/images/projects/omf_prediction_model.png)

## Results
A database comprising 1190 control facial profiles and 256 pairs of pre- and post-operative patient facial profiles was availalble for training. To show how the model applies the jaw displacements, a facial profile with no jaw displacements and a post-operative facial profile with the planned jaw displacements were predicted. Clear jaw displacements between the outputs are visible, showing that the model outputs can be controlled by providing different surgical parameters. However, the identity of the patient is not well represented as the eyebrows and eyelids are missing. Quantitatively, the predicted facial profiles differed on average by 1.77 mm compared to the post-operative facial profiles, which is less effective than the state of the art.

![omf-prediction]({{ IMGURL }}/images/projects/omf_prediction_results.png)

## Conclusion
An AI model has been developed that predicts a patient's facial profile after orthognathic surgery. The model's predictions can be controlled by specifying surgical parameters. Too few patient examples were available to fully utilize the novel method, so an alternative method is proposed that translates the points of the pre-operative mesh instead of generating the post-operative mesh from scratch.

The developed method is one of a few recent accounts of directly using unstructured mesh data to solve clinical problems using deep learning. This trend will likely continue to attract attention and evolve clinical 3D deep learning as the application domain that enjoys the methodological innovations in AI first.

Final report can be retrieved from here: [thesis](https://drive.google.com/file/d/1Vw_rxBvem9RVQPaJiujnsKZU67bLXLU_/view?usp=sharing).

The code for this project will be available in this [GitHub repository](https://github.com/nnistelrooij/OMPrediction) latest February 2022.
