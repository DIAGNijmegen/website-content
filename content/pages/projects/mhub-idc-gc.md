title: MHub/IDC/Grand Challenge algorithm exchange
finished: false
type: general
description: A collaboration between Radboudumc, MHub, and Imaging Data Commons (IDC), aimed at exchanging algorithms and investigating interoperability regarding exchange of data and algorithms.  
template: project-single
groups: rtc
picture: projects/mhub.png
people: Leonard Nürnberg, Dennis Bontempi, Bram van Ginneken, Andrey Fedorov, Hugo Aerts, Henkjan Huisman, Ajay Patel, Sil van de Leemput, Miriam Groeneveld, Keyvan Farahani, Linmin Pei, Ulrike Wagner, Granger Sutton
bibkeys: 

The MHub/IDC/Grand Challenge algorithm exchange project is a collaboration between [Radboudumc](https://www.radboudumc.nl/en/research), [MHub](https://mhub.ai/), and [Imaging Data Commons (IDC)](https://datacommons.cancer.gov/repository/imaging-data-commons), aimed at porting ten deep learning algorithms available at Grand Challenge[Grand Challenge](https://grand-challenge.org/) platform to the open-source [MHub platform](https://mhub.ai/) and is part of a larger project investigating data and algorithm exchange between the three involved parties. The project was financed by the National Institute of Health (NIH) through the Leidos Biomedical Research Inc as subcontract through the Brigham and Women’s hospital.

MHub is a comprehensive repository of self-contained deep learning models designed for a wide range of applications in the medical and medical imaging domains, with a strong focus on cutting-edge advancements and reproducible science. Each MHub model is packaged as an MHub container, which is bundled inside a Docker container, complete with all necessary system dependencies and model weights. This setup allows you to run any model with a single docker run command.

One of the major advantages of MHub containers is their standardized yet flexible input and output interface, enabling you to prepare your data once and use it across any MHub model. Additionally, the repository offers extensive documentation for each algorithm, making it easier to understand the model’s design, expected inputs and outputs, potential caveats, and more.

Grand Challenge is a platform dedicated to the end-to-end development of machine learning solutions in biomedical imaging. A core component of Grand Challenge is the concept of an Algorithm, which encapsulates all the necessary code, models, and dependencies for running a deep learning algorithm. These Algorithms are implemented as Docker containers with predefined input and output interfaces, allowing users to implement deep learning pipelines in any framework and run them on any image available through Grand Challenge.

In this project, ten algorithms from Grand Challenge have been successfully ported to the MHub repository. Each model has been re-implemented as a self-contained Docker file within the MHub framework and is thoroughly annotated for ease of understanding and use. A detailed list of the implemented models in the MHub repository can be found below:

* [Pulmonary Lobes Segmentation (RTSU-Net)](https://mhub.ai/models/gc_lunglobes)
* [Second place in AutoPET challenge: False Positive Reduction Network](https://mhub.ai/models/gc_autopet_fpr)
* [CT Lung cancer risk prediction](https://mhub.ai/models/gc_grt123_lung_cancer)
* [TIGER challenge winner: Team VUNO](https://mhub.ai/models/gc_tiger_lb2)
* [SPIDER challenge baseline: Spine Segmentation](https://mhub.ai/models/gc_spider_baseline)
* [Pancreatic Ductal Adenocarcinoma Detection in CT](https://mhub.ai/models/gc_nnunet_pancreas)
* [STOIC2021 challenge baseline](https://mhub.ai/models/gc_stoic_baseline)
* [NODE21 challenge baseline: Chest Radiograph Nodule Locator](https://mhub.ai/models/gc_node21_baseline)
* [PI-CAI challenge baseline](https://mhub.ai/models/gc_picai_baseline)
* [Tissue-Background segmentation in histopathological whole-slide images](https://mhub.ai/models/gc_wsi_bgseg)
