title: Automatic Pulmonary Artery-Vein Separation and Classification in Computed Tomography Using Tree Partitioning and Peripheral Vessel Matching.
authors: J. Charbonnier, M. Brink, F. Ciompi, E. Scholten, C. Schaefer-Prokop and E. van Rikxoort
has_pdf: True
template: publication
bibkey: char15
published_in: IEEE Transactions on Medical Imaging
pub_details: <i>IEEE Transactions on Medical Imaging</i> 2016;882-92
doi: https://doi.org/10.1109/TMI.2015.2500279
urlweb: http://dx.doi.org/10.1109/TMI.2015.2500279
pmid: http://www.ncbi.nlm.nih.gov/pubmed/26584489
We present a method for automatic separation and classification of pulmonary arteries and veins in computed tomography. Our method takes advantage of local information to separate segmented vessels, and global information to perform the artery-vein classification. Given a vessel segmentation, a geometric graph is constructed that represents both the topology and the spatial distribution of the vessels. All nodes in the geometric graph where arteries and veins are potentially merged are identified based on graph pruning and individual branching patterns. At the identified nodes, the graph is split into subgraphs that each contain only arteries or veins. Based on the anatomical information that arteries and veins approach a common alveolar sag, an arterial subgraph is expected to be intertwined with a venous subgraph in the periphery of the lung. This relationship is quantified using periphery matching and is used to group subgraphs of the same artery-vein class. Artery-vein classification is performed on these grouped subgraphs based on the volumetric difference between arteries and veins. A quantitative evaluation was performed on 55 publicly available non-contrast CT scans. In all scans, two observers manually annotated randomly selected vessels as artery or vein. Our method was able to separate and classify arteries and veins with a median accuracy of 89\%, closely approximating the inter-observer agreement. All CT scans used in this study, including all results of our system and all manual annotations, are publicly available at http://arteryvein.grand-challenge.org.

