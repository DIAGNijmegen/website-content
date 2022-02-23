title: Automated AAA detection
groups: ai-for-health 
finished: true
type: student
picture: projects/aaa-detection.png
template: project-single
people: Douwe van Erp, Thomas van den Heuvel, Chris de Korte, Bram van Ginneken, Tom Heskes
description: Project aimed at development of deep learning algorithms for automated detection of AAA.

**Start date: 08-03-2021** <br>
**End date: 17-12-2021**

## Clinical problem
An abdominal aortic aneurysm (AAA) is a local enlargement of the abdominal artery. Patients with a AAA have an increased risk of rupture, often leading to death. It is therefore vital to early detect and closely monitor these patients. Detection and surveillance of AAA are currently performed by a specialist in the hospital, who measures the diameter of the AAA using ultrasound. 

Ultrasound devices have recently become cheaper and portable. These portable devices can be connected to laptops, tablets and even smartphones, making them accessible for a wide range of users, including physicians in the first line. 

## Methods
We present a method based on deep learning to automatically detect the abdominal aorta from ultrasound (US) imaging and to automatically measure the aortic diameter. The US acquisition can be made with a portable US device connected to a smartphone. Our algorithm runs on the smartphone, and perform automated detection of the abdominal aorta in real-time.

The system consists of two parts. First, a segmentation model will detect the abdominal aorta and give a segmentation mask as output. Second, connected component labeling is used to select the segmented volume of the abdominal aorta. A direct least-squares ellipse fit is used to automatically extract the aortic diameter. 
![image]({{ IMGURL }}/images/projects/AAA_example_segmentation.png)
## Results

The segmentation network was trained on 549 annotated US frames. The segmentation network achieved a median Dice score of 0.88 for the best achieving model, and a median Dice score of 0.83 for the model that could run on the smartphone. Additionally, the difference between the maximum CT and US diameters was computed. The CT-US maximum diameter differences had a median of 6.0 mm. 73.8% of these differences fell within the clinically acceptable limits of agreement of ±5 mm.
![image]({{ IMGURL }}/images/projects/AAA_2D_result_figure_example_client.png)

## Conclusion
We developed a deep-learning method to automatically detect and measure the abdominal aortic diameter from US imaging. This algorithm can be used for real-time detection on the smartphone. A limitation that emerged from this work was the difficulty for a layman to obtain US scans of sufficient quality. This approach shows promising results for automated aortic diameter measurement for laymen.

