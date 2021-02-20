title: Brachial plexus segmentation on ultrasound imaging with a deep learning model
picture: projects/brachial-plexus.png
groups: anes-ai
finished: false
type: student
template: project-single
people: Michel Botros
description: Developing image analysis algorithms that automatically detect osteoporotic vertebral fractures.


## Background
Regional nerve block is a common anaesthesia technique used for surgery on the extremities. A successful block requires excellent anaesthesia experience including the ability to identify the appropriate nerves and surrounding tissues on ultrasound and good skills with a needle.

Previous studies have primarily focussed on the usage of ultrasound which has shown that ultrasound increases the success rate of regional nerve blocks. Some studies, however, have found that even with ultrasound assistance, a relatively high failure rate persists. This failure rate has largely been attributed to operators with limited experience and insufficient ultrasound skills.

A failed nerve block not only results in a bad experience for the patient, it might even lead to damage to the patients’ health and in some cases complications could even threaten life.

It’s essential to recognise ultrasound anatomy when performing nerve blocks, however this may sometimes be hampered by patients’ habitus. 


## Aim
In this study we will attempt to create a dataset of ultrasound images depicting the brachial plexus and use this dataset to train an U-net model in order to identify the region of interest in these images, which may potentially be used in clinical practise.

Primary Objective
 - Construct a dataset of ultrasound images depicting the brachial plexus with manual image segmentation

Secondary Objective(s)
 - Train an U-net deep learning model using the dataset and teach it to properly identify the brachial plexus
