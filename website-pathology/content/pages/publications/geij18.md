title: Automatic color unmixing of IHC stained whole slide images
authors: D.J. Geijs, M. Intezar, J.A.W.M. van der Laak and G.J.S. Litjens
has_pdf: True
template: publication
bibkey: geij18
published_in: Medical Imaging
pub_details: in: <i>Medical Imaging</i>, volume 10581 of SPIE, 2018
doi: https://doi.org/10.1117/12.2293734
Assessment of immunohistochemically stained slides is often a crucial diagnostic step in clinical practice. However, as this assessment is generally performed visually by pathologists it can suﬀer from signiﬁcant inter-observer variability. The introduction of whole slide scanners facilitates automated analysis of immunohistochemical slides. Color deconvolution (CD) is one of the most popular ﬁrst steps in quantifying stain density in histopathological images. However, color deconvolution requires stain color vectors for accurate unmixing. Often it is assumed that these stain vectors are static. In practice, however, they are inﬂuenced by many factors. This can cause inferior CD unmixing and thus typically results in poor quantiﬁcation. Some automated methods exist for color stain vector estimation, but most depend on a signiﬁcant amount of each stain to be present in the whole slide images. In this paper we propose a method for automatically ﬁnding stain color vectors and unmixing IHC stained whole slide images, even when some stains are sparsely expressed. We collected 16 tonsil slides and stained them for diﬀerent periods of time with hematoxylin and a DAB-colored proliferation marker Ki67. RGB pixels of WSI images were converted to the hue saturation density (HSD) color domain and subsequently K-means clustering was used to separate stains and calculate the stain color vectors for each slide. Our results show that staining time aﬀects the stain vectors and that calculating a unique stain vector for each slide results in better unmixing results than using a standard stain vector.

