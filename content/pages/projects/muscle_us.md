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
Muscle ultrasound is a useful and patient friendly tool in the diagnostic evaluation of patients with suspected neuromuscular diseases. Neuromuscular diseases cause structural changes such as fibrosis and fatty infiltration that increases muscle echogenicity (gray value of the muscle). With quantitative muscle ultrasound the echogenicity of the muscle is calculated and used to distinguish normal from diseased muscle. Quantitative muscle ultrasound has proven to be more reliable and more sensitive in detecting neuromuscular diseases than visual evaluation, with a sensitivity of 92%. Although quantitative muscle ultrasound offers advantages over visual assessments, widespread implementation of quantitative muscle ultrasound in the clinical setting is limited by an inability to replicate reference values, and therefore results, between different ultrasound devices. Echogenicity of different devices cannot be compared, because beam-forming and post-processing of raw RF signals is different between ultrasound devices, as well as physical characteristics of the acoustic array such as frequency, element size and pitch, acoustical lens, and the beam profile. Furthermore, the post-processing is also machine specific affecting the echogenicity even more. Consequently, a set of new normal values is required for each device, which is time-consuming and expensive.

## Solution
The goal of this project is to develop a new device-independent method that can discriminate between muscle ultrasound images from healthy subjects and patients with a neuromuscular disease.

## Tasks
To date, the only parameter clinically validated to discriminate between healthy and diseased muscle ultrasound images is its echogenicity (gray value). Probably, other features than echogenicity can be extracted from the muscle ultrasound images that discriminate between healthy and diseased muscle. The AI challenge in this project is to develop an algorithm that can extract these features from muscle ultrasound images that is independent from the ultrasound machine. Specifically, the task for this project is to develop an AI algorithm that 1) can discriminate between healthy and diseased muscle, and 2) can classify patients with a neuromuscular disease based on a set of muscle ultrasound images, and 3) can perform this classification on ultrasound images from different ultrasound machines and setups.

## Innovation
Since 2002, the clinical neurophysiology laboratory of the department of Neurology at the Radboudumc performs research on the frontier of neuromuscular ultrasound. The technique of quantitative muscle ultrasound based on echogenicity is developed in our lab and is part of our routine daily clinical practice. However, a new method to screen for neuromuscular diseases based on ultrasound images that is device independent is much needed to able to continue this routine care when our current US machine is out of service. Thus, if a reliable AI algorithm can be developed to screen for neuromuscular disorders this will be implemented in our clinical practice immediately. Furthermore, this innovation will facilitate widespread clinical implementation of muscle ultrasound. 

## Methods
We leverage pre-trained convolutional neural networks for ultrasound image classification. Specifically, we investigate the use of various forms of multi-instance learning to be able to integrate information from multiple images of multiple muscles that characterized each patient record. Various forms of unsupervised domain adaptation are investigated to ensure that a model trained on images from one ultrasound machine also works reliably on images from another machine. As these methods are unsupervised, the adoption of new devices can be eased in the future: A number of images need to be recorded, but there is no need for collecting separate labels or annotations. 
