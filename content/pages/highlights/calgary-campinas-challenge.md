title: MIDL 2020 MRI Reconstruction Challenge
date: 2020-07-16
picture: news/calgary-campinas-challenge.png
description: Together with colleagues from the NCI and the AMC, DIAG's Jonas Teuwen and Nikita Moriakov won an international competition where MRI-scans can be accelerated using deep learning.
groups: diag, aiimnijmegen

Researchers [member/jonas-teuwen] and [member/nikita-moriakov] of the Diagnostic Image Analysis Group of the Radboud University Medical Center together with colleagues 
from the <a href="https://nki.nl">Netherlands Cancer Institute</a> and the <a href="https://amsterdamumc.nl/">Amsterdam Medical Center</a> won an international competition where MRI-scans can be accelerated using deep learning algorithms. Their deep learning algorithm won the competition resulting in images of high quality within 2 minutes of scanning.

The <a href="https://sites.google.com/view/calgary-campinas-dataset/mr-reconstruction-challenge">competition which was part of MIDL 2020</a> was organized by universities in Canada and Brazil who have provided more than 100 brain MRI scans
to train the algorithm. The team won both tracks of the challenge, where in the first track the goal was to reconstruct data similar to the
training data with 5 and 10 times acceleration, and the second track where the algorithms had to reconstruct out-of-distribution 
data of a different scanner with different coil configurations. The reconstruction framework is published under an open source license on 
<a href="https://github.com/directgroup/direct">GitHub</a>, including the winning algorithm.

The methods developed in the challenge have tight connections to our current research lines in MRI-guided radiotherapy where the patient anatomy can be visualized during radiation treatment using the builtin MRI scanner. 
Fast reconstruction algorithms such as the ones in the challenge open opportunities to track second-by-second patient motion.
