title: Vessel Enhancing Diffusion
authors: R. Manniesing, M.A. Viergever and W.J. Niessen
has_pdf: True
template: publication
bibkey: mann09
urlweb: http://www.insight-journal.org/browse/publication/314
Recently, an implementation of the Vessel Enhancing Diffusion (VED) algorithm [3] using the Insight Toolkit (ITK) framework [2] has been proposed by Enquobahrie et al.[1]. In this paper we present an alternative implementation, for two reasons. First, in this implementation all the main functionality of the algorithm, including eigensystem, vesselness, tensor calculation and PDE discretization using a forward Euler scheme are now grouped together in one single class. Although this may come at the cost of code-reusability, it improves readibility and enables application specific code optimization. The second reason is the criterion of reproducibility. Source code, test environment and example data of the paper [3] are provided.

