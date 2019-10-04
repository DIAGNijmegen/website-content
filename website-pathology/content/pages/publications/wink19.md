title: Out-of-distribution detection for computational pathology with multi-head ensembles
authors: J. Winkens
has_pdf: True
template: publication
bibkey: wink19
Distribution shift is a common phenomenon in real-life safety-critical situations that is detrimental to the performance of current deep learning models. Constructing a principled method to detect such a shift is critical to building safe and predictable automated image analysis pipelines for medical imaging. In this work, we interpret the problem of out-of-distribution detection for computational pathology in an epistemic uncertainty estimation setting. Given the diﬃculty of obtaining a suﬃciently multi-modal predictive distribution for uncertainty estimation, we present a multiple heads topology in CNNs as a highly diverse ensembling method. We empirically prove that the method exhibits greater representational diversity than various popular ensembling methods, such as MC dropout and Deep Ensembles. The fast gradient sign method is repurposed and we show that it separates the softmax scores of in-distribution samples and out-of-distribution samples. We identify the challenges for this task in the domain of computational pathology and extensively demonstrate the eﬀectiveness of the proposed method on two clinically relevant tasks in this ﬁeld.

