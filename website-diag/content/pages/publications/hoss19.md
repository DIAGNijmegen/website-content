title: Effect of Adding Probabilistic Zonal Prior in Deep Learning-based Prostate Cancer Detection
authors: M. Hosseinzadeh, P. Brand and H. Huisman
has_pdf: True
template: publication
bibkey: hoss19
published_in: Medical Imaging with Deep Learning
pub_details: in: <i>Medical Imaging with Deep Learning</i>, 2019
urlweb: https://openreview.net/forum?id=SkxAwFtEqV
We propose and evaluate a novel method for automatically detecting clinically significant prostate cancer (csPCa) in bi-parametric magnetic resonance imaging (bpMRI). Prostate zones play an important role in the assessment of prostate cancer on MRI. We hypothesize that the inclusion of zonal information can improve the performance of a deep learning based csPCa lesion detection model. However, segmentation of prostate zones is challenging and therefore deterministic models are inaccurate. Hence, we investigated probabilistic zonal segmentation. Our baseline detection model is a 2DUNet trained to produce a csPCa heatmap followed by a 3D detector. We experimented with the integration of zonal prior information by fusing the output of an anisotropic 3DUNet trained to produce either a deterministic or probabilistic map for each prostate zone. We also investigate the effect of early or late fusion on csPCa detection. All methods were trained and tested on 848 bpMRI. The results show that fusing zonal prior knowledge improves the baseline detection model with a preference for probabilistic over deterministic zonal segmentation.

