title: Graph Representation of Placental Vasculature for Treatment of Twin-to-Twin Transfusion Syndrome
groups: ai-for-health
finished: true
type: student
picture: vacancies/placental-vessel-segmentation.png
template: project-single
people: Isabel Burgos, Anouk van der Schot, Guido de Jong
description: Presenting a proof of concept, where we explored the potential of representing the placental vascular structure as a graph network 

**Start date: 14-03-2022** <br>
**End date: 11-07-2023** <br>

## Clinical Problem
Twin-to-twin transfusion syndrome (TTTS) is a severe and progressive disorder where there are imbalanced blood vessel connections in the shared placenta of monochorionic twins. Untreated, this syndrome is associated with a 90% mortality rate of the twins.

Laser surgery has become the treatment of choice for TTTS[1]. During this procedure, a small diameter endoscope (fetoscope) is used to visualize the placental surface in the uterus. The surgeon scans the placenta to localize and coagulate blood vessel connections to dissolve the blood flow.[2]
However, even in the most experienced fetal therapy centers, survival rates remain below 90%. The stagnation of survival rates is due to, on the one hand, the limited field of view and poor visibility in the uterus. This limited view, together with the complexity of the surgical task of recognizing the vessels at the placental surface, midst the very variable topography of vessels, can result in incomplete surgery, leading to recurring or reversal of the TTTS.[3]

A computer-assisted guidance system can help overcome these challenges by providing better visualization of the vessel map and artificially expanding the surgical field of view, guiding the surgeons in quick and precise detection of the placental blood vessel connections.[4] This is largely done through fetoscopic video mosaicking, where the result is a mosaicked image of overlapping video frames.[5] Although there are examples of good results, these approaches remain restricted by the accumulation of errors during mosaicking, known as drift.[6]

## Solution
We believe that a graph may be more robust to drift due to it being a more flexible representation than an image. Furthermore, a graph is comparable to the map the surgeons create when obtaining the overview of the placenta. Therefore, the aim of this project was to present a proof of concept on presenting the placental vasculature network as a graph and inspire further research on this topic. Assuming that the graph representation is successful, the main aspect for future work would be to obtain a graph that presents a larger view of the placenta.

## Method
The graph was extracted from an image of vascular structure using a segmentation-based graph extraction approach. With this approach the graph is retrieved by first obtaining the skeleton of the binary vessel segmentation and then extracting the graph from the skeleton. The pipeline is presented below. The pipeline assumes that the binary vessel segmentations of the input images and the annotated target graphs are obtained prior to running the pipeline.

![Pipeline approach master thesis - copy](https://github.com/DIAGNijmegen/website-content/assets/32160020/b1be8142-c9fd-4892-99fc-3c3a8d148a20)

The Zhang-Suen thinning algorithm [7] was used to obtain the skeleton of the binary vessel segmentation. The graph was extracted from the skeleton by first defining graph nodes as any pixel on the skeleton with either 1 or >2 neighbours, and based on these locations tracing the skeleton using BFS to extract the edge connections.


## Data
The approach was evaluated on images of simulated placentas and in-vivo frames from fetoscopic procedures.

- The simulated dataset consisted of 5 drawings of structures that resemble that of the vascular structure on a human placenta. The simulated images were found online and chosen based on their similarity to real placentas. The images did not have to be exact replicas of a placenta and could be simulating a placenta of a single fetus pregnancy.

-	The in-vivo dataset was a subset of the Bano et al. [5] a public dataset that contains 483 frames with ground-truth vessel segmentation annotation from six different fetoscopic procedure videos. The chosen subset was of 20 images. The Bano et al. dataset is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

## Results
The quantitative results presented high median recall and precision scores for non-end-nodes and extremely low scores for end-nodes (only one neighbour). This was the case for both the simulated dataset and the in-vivo dataset. Qualitative analysis however determined that misplacements of nodes (largely causing these low scores) did not greatly impact how representative the graphs were of the original vessel structures. It was rather the misrepresentations of complex vessel relationships, such as vessel crossings and close proximity of vessels, that largely affected the representability of the graphs.

From the qualitative analysis the overall impression when looking at the extracted graphs was that most graphs represented their respective vessel structures, although many had some local misrepresentations. For the simulated dataset all graphs were found to be sufficiently representative. Regarding the graphs from the in-vivo images, 12 graphs were found to be sufficiently representative, 5 graphs could be recognised but were on the borderline of being representative due to multiple local misrepresentations, and 3 graphs were not sufficiently representative.

Demonstrating a sufficiently representative graph:
<img width="793" alt="Figure 4 6 - thesis" src="https://github.com/DIAGNijmegen/website-content/assets/32160020/7056fcfe-c170-4757-a268-a1e3e01334e5">

Demonstrating a moderately representative graph, due to misrepresentations of vessel crossings and close proximity of vessels:
<img width="773" alt="Figure 4 10 - thesis" src="https://github.com/DIAGNijmegen/website-content/assets/32160020/b93980e2-5498-450f-a5a9-4022c8ebbbb3">


## Conclusion
We found that there is potential in presenting placental vessels as a graph, however, multiple modifications are needed to the approach. For instance, we recommend investigating approaches that do not require high quality segmentations to extract representative graphs. Furthermore,
once the modifications are made, it is necessary to confirm that high quality graphs can be made or extracted of larger views of the placenta than one video frame. The work presented in this thesis contributes to future work on the improvement of TTTS treatment by providing a proof of concept supporting the use of a graph to represent placental vessels.

## References
[1] M.-V. Senat, J. Deprest, M. Boulvain, A. Paupe, N. Winer, and Y. Ville, "Endoscopic laser surgery versus serial amnioreduction for severe twin-to-twin transfusion syndrome," N. Engl. J. Med., vol. 351, no. 2, pp. 136–144, 2004.

[2] S. H. P. Peeters et al., "Identification of essential steps in laser procedure for twin-twin transfusion syndrome using the Delphi methodology: SILICONE study," Ultrasound Obstet. Gynecol., vol. 45, no. 4, pp. 439–446, Apr. 2015, doi: 10.1002/uog.14761.

[3] E. Lopriore, J. M. Middeldorp, D. Oepkes, F. J. Klumper, F. J. Walther, and F. P.H.A. Vandenbussche. Residual Anastomoses After Fetoscopic Laser Surgery in Twin-to-Twin Transfusion Syndrome: Frequency, Associated Risks and Outcome. Placenta, vol. 28 no. 2, pp. 204–208, 2007

[4] Rosalind Pratt, Jan Deprest, Tom Vercauteren, Sebastien Ourselin, and Anna L. David. Computer-assisted surgical planning and intraoperative guidance in fetal surgery: A systematic review, 2015.

[5] S. Bano, F. Vasconcelos, L. M. Shepherd, E. V. Poorten, T. Vercauteren, S. Ourselin, A. L. David, J. Deprest, and D. Stoyanov, “Deep placental vessel segmentation for fetoscopic mosaicking,” arXiv:2007.04349 Search..., 2020.

[6] S. Bano, F. Vasconcelos, M. Tella-Amo, G. Dwyer, C. Gruijthuijsen, E. Vander Poorten, T. Vercauteren, S. Ourselin, J. Deprest, and D. Stoyanov, “Deep learning-based fetoscopic mosaicking for field-of-view expansion,” International journal of computer assisted radiology and surgery, vol. 15, no. 11, pp. 1807–1816, 2020.

[7] T. Y. Zhang and C. Y. Suen, “A fast parallel algorithm for thinning digital patterns,” Communications of the ACM, vol. 27, no. 3, pp. 236–239, 1984.
