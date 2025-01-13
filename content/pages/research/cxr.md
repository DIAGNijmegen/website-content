title: Chest x-ray analysis
title_long: Chest x-ray analysis
finished: false
type: general
picture: projects/cxr.jpg
template: project-single
groups: diag
people: Bram van Ginneken, Keelin Murphy
description: Chest radiography is ubiquitous in radiology. We develop tools to interpret these exams automatically.
bibkeys: Murp20a, Habi20, Maho20, Murp20, Ginn18, Phil19a, Mele18, Koes18, Mele17, Mele16a, Stei15, Phil15b, Muyo14, Madu13c, Breu14, Hoge17, Mele16, Madu16, Phil15, Hoge15, Mele14a, Madu14, Hoge13, Hoge13, Hoge12, Hoge10a, Arzh09, Arzh07, Ginn06b, Ginn02a, Phil19, Madu15a, Mele15, Hoge13b, Ginn01a

![CAD4TB]({{ IMGURL }}/images/projects/cxr.jpg)

Chest radiography is the most common radiological exam in the world. In many hospitals 40% of all exams made in the radiology department are chest x-rays. The advent of deep learning has increased the interest for chest x-ray analysis. At DIAG, we have pioneered tuberculosis detection with chest x-ray, but we also have research projects aimed at detecting other diseases from chest radiographs.

## Tuberculosis screening and chest radiography
Tuberculosis (TB) is a highly infectious disease that still kills 1.5 million people every year, despite the fact that a cheap cocktail of antibiotics can cure almost every TB patient. Finding TB before patients infect others and putting people on treatment is crucial. 

Chest radiography has always been widely used to find TB. Digital chest radiography has made x-ray cheaper and easier to use. No films, chemicals and water are needed to produce a digital radiograph, automatic exposure control ensures high image quality, and images are instantly available. The cost per exam, once a digital unit is operational, is near zero. Digital chest radiography, therefore, has a large potential to be used in TB case finding and prevalence surveys, as an adjunct test, next to molecular testing. Molecular diagnostics for TB, such as the [GeneXpert](http://www.nejm.org/doi/pdf/10.1056/NEJMoa0907847) test have become a standard for TB diagnosis, because they can make a definitive diagnosis of TB in two hours. However, these tests are still much more expensive and time-consuming than radiography. Radiography can act as a filter: TB suspects undergo symptom screening and chest radiography, and those with symptoms and/or abnormalities in the chest radiograph undergo further testing. 

One issue remains: the lack of human expert readers in countries with a high burden of TB. CAD4TB eliminates this problem by automating the reading process. 

## The CAD4TB project
Our work in developing software to detect signs of tuberculosis started in 1996 when digital x-ray machines were first entering the market. We work with [Delft Imaging](https://www.delft.care), famous as the inventor of the Odelca camera from the 1960s, one of the most widely used systems in x-ray TB screening in the world. Our project resulted in a [prototype computer-aided detection system for TB in 2001](/publications/ginn02a/). At that time, however, digital x-ray was not yet widely adopted for TB case finding. 

In 2007, we attracted a research grant and established the CAD4TB project with partners in South Africa, the [University of Cape Town Lung Institute](http://lunginstitute.co.za), and in Zambia, the NGO [Zambart](http://www.zambart.org/).

## The CAD4TB software
The first CAD4TB beta prototype (CAD4TB v0.01) was field-tested in 2010. In 2011, the first official prototype version was released (CAD4TB v1.08), notably improved by training the system with a much larger number of images. A string of new versions of the software has been released: in 2012 v2.09, in 2013 v3.07, and in 2014 v4.10. Version v4.10 was the first version to receive a CE label. In 2016, version 5 saw the light and in 2019 version 6 was released, based on deep learning. Algorithm development behind CAD4TB is now carried out at [Thirona](https://www.thirona.eu), a spin-off company from the Diagnostic Image Analysis Group.

CAD4TB is commercially available via [Delft Imaging](https://www.delft.care) and has hundreds of installations in over 40 countries worldwide. 

This BBC report shows CAD4TB in action in Ghana:

[youtube: -YVozBT5HaA]

## New research
Our current research focuses on extending the capabilities of the software to do more than outputting a single number related to the probability the subject has TB. We have developed a system for automatically measuring the cardiothoracic ratio, for childhood pneumonia detection, and we are working on detection of COVID-19 on the chest radiograph. In collaboration with Thirona, the Fondation Botnar, the Swiss Tropical and Public Health Institute and NGO SolidarMed, we will field test a combined TB and COVID-19 screening in district hospitals in Lesotho with a new  AI system that uses a combination of chest x-ray and blood markers.

## Funding
* [Delft Imaging](http://www.delft.care/)
* [Deep Learning in Medical Image Analysis](http://dlmedia.eu/)
* [ImageREPORT](https://www.eurostars-eureka.eu/project/id/11470)
* [TBTriage+](https://tbtriage.com/)
* [MistraL](https://www.fondationbotnar.org/)
