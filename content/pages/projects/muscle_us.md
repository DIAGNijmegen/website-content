title: Automatic screening for neuromuscular disorders
groups: ai-for-health
finished: true
type: student
picture: vacancies/muscle_us.png
template: project-single
people: Klaus Lux, Jonne Doorduin, Juerd Wijntjes, Nens van Alfen, Twan van Laarhoven, Ajay Patel
description: Development of a deep learning algorithm for the automatic classification of muscle ultrasound images.

**Start date: 01-03-2020** <br>
**End date: 31-08-2020**

## Clinical problem
Muscle ultrasound is a useful and patient friendly tool in the diagnostic evaluation of patients with suspected neuromuscular diseases. These diseases can affect the muscles and the nerves that connect them and an early and reliable screening method can help to allow for target patient care. Generally, they cause structural changes such as fibrosis and fatty infiltration that increases muscle echogenicity (i.e. how bright the muscle appears in an ultrasound image). 
A quantitative method developed at RadboudUMC extracts the echogenicity of the muscle tissue from ultrasound images and uses it to screen for neuromuscular disease. This method has been proven to be more reliable and more sensitive in detecting neuromuscular diseases than visual evaluation, with a sensitivity of 92%. Although it offers advantages over visual assessments, widespread implementation of the method is currently out of reach: The same muscle imaged on two ultrasound devices of different types will not show the same echogenicity. This is due to differences in beam-forming, post-processing of the raw radio frequency signals and physical characteristics of the acoustic array. Furthermore, the post-processing is machine specific, affecting the echogenicity even more. As a consequence, the reference echogenicity values that need to obtained in a time-consuming and expensive manner by sampling healthy volunteers do not transfer between different devices. Consequently, the sampling process is required for each new device type that is to be used. This fact is a major impediment to wider adoption of neuromuscular ultrasound by other hospitals.

## Solution
The goal of this project was to develop a new device-independent method that can discriminate between muscle ultrasound images from healthy subjects and patients with a neuromuscular disease.

## Tasks
To date, the only parameter clinically validated to discriminate between healthy and diseased muscle ultrasound images is its echogenicity (gray value). Probably, other features than echogenicity can be extracted from the muscle ultrasound images that discriminate between healthy and diseased muscle. The AI challenge in this project is to develop an algorithm that can extract these features from muscle ultrasound images that is independent from the ultrasound machine. Specifically, the task for this project is to develop an AI algorithm that 1) can discriminate between healthy and diseased muscle, and 2) can classify patients with a neuromuscular disease based on a set of muscle ultrasound images, and 3) can perform this classification on ultrasound images from different ultrasound machines and setups.

## Innovation
Since 2002, the clinical neurophysiology laboratory of the department of Neurology at the Radboudumc performs research on the frontier of neuromuscular ultrasound. The technique of quantitative muscle ultrasound based on echogenicity has been developed in our lab and is part of our routine daily clinical practice. However, a new method to screen for neuromuscular diseases based on ultrasound images that is device independent is much needed to able to continue this routine care when our current ultrasound machine is eventually phased out. Thus, if a reliable AI algorithm can be developed to screen for neuromuscular disorders this will be implemented in our clinical practice immediately. Furthermore, this innovation will facilitate widespread clinical implementation of muscle ultrasound. 

## Methods
We leverage pre-trained convolutional neural networks for ultrasound image classification. Specifically, we investigate the use of various forms of multi-instance learning to be able to integrate information from multiple images of multiple muscles that characterized each patient record. Various forms of unsupervised domain adaptation are investigated to ensure that a model trained on images from one ultrasound machine also works reliably on images from another machine. As these methods are unsupervised, the adoption of new devices can be eased in the future: A number of images need to be recorded, but there is no need for collecting separate labels or annotations. 

## Results


## Conclusion
