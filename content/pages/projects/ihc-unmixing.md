title: Quantifying IHC pathology stains
finished: false
type: general
description: For the Pathology department we are developing an application that can unmix different IHC stains to aid analysist in quantifying pathology scans.
template: project-single
groups: rtc
picture: projects/ihc-analysis.png
people: Esther Markus-Smeets, Daan Geijs, Erik Aarntzen, Silvan Quax, Ajay Patel, Bram van Ginneken
bibkeys: 

Immunohistochemistry staining is widely used for the analysis of pathology slices. Often, multiple of such stains are applied to identify different cell types. Quantification of the number of cells or percentage of tissue that is stained with the different stainings by pathology analysts is very time consuming. In this project we developed an AI tool that can automatically quantify the relative surface that different stainings in a scan cover. It can be applied in many different contexts and is not staining specific. By automating the quantification process, analysts can much quicker interpret pathology scans and provide greater accuracy, thereby improving the efficiency and accuracy of the work done in the Pathology department.

The RTC AI and Pathology departmeent have developed a web-based application for the automatic segmentation of immunohistochemistry staining and the subsequent quantification of the different stains. Additional tools for the selection of 'regions of interest' to perform the quantification on are available for the analysts. The algorithm can be used on the [Grand Challenge](https://grand-challenge.org/) platform. All processing is performed on the platform; there is no specialized hardware required to try out the algorithm. Running the algorithm requires an account for Grand Challenge. If you don't have an account yet, you can register on the [website](https://grand-challenge.org/accounts/signin/); alternatively, you can log in using a Google account. After registering for a new account, or logging in to an existing Grand Challenge account, you can request access to the algorithm.

<a href="https://grand-challenge.org/algorithms/ihc-analysis/" class="btn btn-primary btn-lg my-3">Try out the algorithm</a>
