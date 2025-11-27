title: Muscle ultrasound classification
finished: false
type: general
description: For the Neurophysiology department we have developed an algorithm for the identification of abnormal muscle tissue in ultrasound images of the tibialis anterior.
template: project-single
groups: rtc
picture: projects/muscle-us.png
people: Juerd Wijntjes, Jonne Doorduin, Ajay Patel, Bram van Ginneken
bibkeys: 

Ultrasound is a non-invasive imaging technique that is increasingly used to diagnose patients with suspected neuro-muscular disorders through imaging of superficial structures. Recent studies have shown benefits of neuro-muscular ultrasound for screening and diagnostic purposes. The clinical neurophysiology department of the Radboudumc uses ultrasound of the muscles for the assessment of neuro-muscular conditions. The ultrasound probe is placed at specific locations on the body to visualize the superficial muscular tissue. At each location the probe is used to create three images by repeatedly placing the probe in the same location. 
<br>

Currently, a manual ROI is drawn in each image by a technician and the mean pixel value in the ROI averaged over the three images is used to obtain a 'Z-score'. The Z-score is compared to a curve that shows the average Z-score of a healthy subject for a given age. If the Z-score is two standard deviations or more above the curve it is considered abnormal. The creation of such curves is time-consuming and expensive. Automatic analysis of the entire images could possibly be used to distinguish between abnormal and healthy subjects, negating the use of manual interaction and standard curves.
<br>

The RTC AI has developed an algorithm for the binary classification of ultrasound images of the tibialis anterior muscle. Research on this topic has been continued in an [AI for Health MSc project](https://www.ai-for-health.nl/projects/muscle_us/) to develop a new device-independent method that can discriminate between muscle ultrasound images from healthy subjects and patients with a neuromuscular disease..
