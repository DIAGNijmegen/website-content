title: Generic out-of-distribution detection for radiology AI systems
groups: ai-for-health
finished: false
type: student
picture: projects/ood.jpg
template: project-single
people: Ruben Geurtjens, Dré Peeters, Colin Jacobs, Bram van Ginneken
description: Develop a method for out-of-distribution detection to make AI more reliable and robust.


**Start date: 01-10-2022** <br>
**End date: 30-03-2023**


## Clinical problem
In recent years, over 200 AI products for radiology have come on the market. These products are CE certified, meaning they are approved for clinical use in hospitals. Almost all these products analyze a specific type of radiological image, for example a frontal chest radiograph, and produce a specific output, for example locations of possible pulmonary nodules. Almost all products have been developed using supervised deep learning. A general problem for such products is that they tend to produce nonsense or poor output when an image is input that was not represented in the data that the product was trained on. For example, the chest x-ray nodule detector was very likely not trained with radiographs from children. It won’t work at all, of course, on a hand radiograph. It may work poorly on bedside chest x-rays. It could well have been trained only on images from hospitals in Western countries and therefore the product will perform less well on x-rays of middle-age Asian women, a group known to have an increased risk for developing lung cancer. We refer to all this kind of data as [out-of-distribution](https://medium.com/analytics-vidhya/out-of-distribution-detection-in-deep-neural-networks-450da9ed7044). At the moment, there are no legal requirements for AI products in radiology to systematically perform out-of-distribution detection. We believe legislation enforcing this will be implemented in the next decade and proper out-of-distribution detection will become a requirement for any product so that AI in healthcare will be more robust and reliable.

## Approach 
The computer vision literature reports many different methods for out-of- distribution detection. We recently tested several approaches and found several to perform poorly on chest radiographs, but one method achieved very promising results: the approach by [Dan Hendricks et al.](https://arxiv.org/abs/1906.12340) that employs self-supervision, a popular recent trend in deep learning. In this project we would like to use this method, and possibly extend it or compare it to other methods, on a variety of radiological image classification and detection tasks. Our hypothesis is that a generic approach to out-of-distribution detection, trained with self-supervision, will be able to enhance a wide variety of products for AI in radiology.

## Data 
We have different sets of data available from previous projects in the analysis of x-rays, ultrasound images and color fundus images. In all cases out-of-distribution datasets can be defined as well.

[comment]: <> (## Results)

[comment]: <> (The project should result in a reusable method to enhance any AI system analyzing 2D images with out-of-distribution detection capabilities. Organizing a multi-task challenge on [grand-challenge.org](https://grand-challenge.org) for this problem would be a nice outcome that could be continued in subsequent projects.)

