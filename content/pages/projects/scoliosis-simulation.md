title: Scoliosis simulation for improving a segmentation and labelling algorithm
groups: ai-for-health, diag
finished: false
type: student
picture: projects/scoliosis_modeling.jpg
template: project-single
people: Lars Leijten, Nikolas Lessmann, Dennis Janssen, Max Bakker, Sebastiaan van de Groes
description: Modeling of deformities in adolescent idiopathic scoliosis to improve segmentation

**Start date: 01-02-2021** <br>
**End date: 01-07-2022**

## Clinical problem
Artificial intelligence in medical imaging, is a rapidly innovating field which promises the opportunity of fast and objective analysis of medical images. Automatic processing and analysis of these scans could greatly reduce the costs and required man power in the field of Radiology. In orthopedic surgery, CT scans are often used in surgical planning and navigation, where its use results in increases surgical accuracy and reproducibility. Computerized analysis of these scans could increase the options within and the extent to which imaging is applied in orthopedic surgery of the spine. Automatic segmentation and anatomic labeling of the vertebrae is an important aspect of this analysis and it can help in the detection of osteoporosis, compression fractures, scoliosis or spinal abnormalities related to chronic back pain. Additionally, segmented spinal images can be used in planning and virtual practicing of the surgery, creating 3D-printed drilling guides that exactly fit the spine of the patient and aid the surgeon in accurate screw placement. 

Automatic segmentation and labeling can be performed using convolutional neural networks. These offer the ability to sequentially segment and label vertebrae in different images. These convolutional neural networks are trained in an iterative process where the algorithm is corrected based one a pre-labeled database. To increase the accuracy of the network while avoiding overfitting, a large training set is needed. Existing training data mostly exists of relatively normal spine curvatures, limiting the accuracy of the image analysis algorithm. To increase the robustness of the network, the training data should be extended with a large number of images from deformed spines. A suitable database of labeled and segmented deformed spines is not available and manual labeling and segmentation is enormously time consuming. A possible solution is to generate this data by adapting images of regular spines. 

<!--![scoliosis-simulation]({{ IMGURL }}/images/projects/scoliosis_simulation_clinical_problem.png)-->

## Methods
CT scans were transformed according to a scan-specific 3D spinal model that was deformed to resemble a scoliosis curve. For an individual CT scan, a 3-dimensional model was created, which was deformed according to a 2-dimensional model, representing a clinical scoliosis curve. After the deformation of the 3-dimensional model and interpolation of the displacement vectors per voxel, the entire image and segmentation mask were deformed into a simulated scoliosis.

<!--![scoliosis-simulation]({{ IMGURL }}/images/projects/scoliosis_simulation_method.png)-->

With the described method, 54 simulated scoliosis cases were created, which were split 42:12 between a training set and a test set. The 42 cases were used to retrain a segmentation and labelling algorithm. The results of this retrained algorithm were quantitatively compared against the results of the original algorithm on the 12 test cases. A reader study qualitatively evaluated both algorithms on 30 cases of clinical scoliosis.

<!--![scoliosis-simulation]({{ IMGURL }}/images/projects/scoliosis_simulation_method_2.png)-->

## Results
In the simulated test cases of scoliosis, segmentation performance increased from a Dice coefficient of 61.5% to 93.6% (p<0.001), and labelling accuracy increased from 71.8% to 100% (p<0.001 ) after retraining of the model. Qualitative evaluation of clinical cases showed a significant reduction of vertebrae with small segmentation errors (from 14.3% to 7.6%, p = 0.02) and vertebrae with severe segmentation errors (from 12.7% to 3.3%, p<0.001). Segmentation and labelling performance in normal cases was similar for both algorithms. As the example in the image below demonstrates, the retrained algorithm performed more accurately and robustly on clinical scoliosis cases. 

<!--![scoliosis-simulation]({{ IMGURL }}/images/projects/scoliosis_simulation_results.png)-->

## Conclusion
Scoliosis simulation proved to be an effective method for smart data augmentation to improve the robustness of the segmentation and labelling algorithm in scoliosis cases. Our improved model can be used to automatically generate additional training cases or could aid in corrective surgical planning and execution. 

A demo of the retrained algorithm is accessible via [Grand-Challenge](https://grand-challenge.org/algorithms/vertebra-segmentation/):

The report of this project can be found [here](https://drive.google.com/file/d/1GUXhtXsTOu9n1nwQmMxxOuUiJspaDq5k/view?usp=sharing).

