title: Algorithms

## CARA Lab algorithms

At CARA Lab, we focus on developing advanced AI-driven methods for the analysis of intracoronary imaging. Our research aims to improve segmentation, plaque characterization and vulnerability assessment, artifact detection, and the identification of key pathological structures such as thrombus, plaque rupture and layered plaque. Additionally, we work on models for stent detection and characterization.

## Segmentation

Our segmentation model [OCT-AID](https://academic.oup.com/ehjdh/advance-article/doi/10.1093/ehjdh/ztaf021/8078941), now also available for [real time](https://academic.oup.com/ehjdh/article/7/8/ztag138/8779935) analysis, is led by [member/ruben-van-der-waerden] and is designed to precisely delineate key structures within intracoronary OCT images, aiding in the identification of vessel boundaries, plaque types, and other relevant features. By leveraging deep learning techniques, our model enhances automated interpretation and assists clinicians in decision-making. The latest version of OCT-AID now also includes [layered plaque](https://www.sciencedirect.com/science/article/pii/S2352906726001594?via%3Dihub) as an additional pixel-wise class.

![Multiclass segmentation model]({{ IMGURL }}/images/projects/cara_lab_model_segmentation.png) 

We demonstrated previously, in the PECTUS-AI study led by [member/rick-volleberg] and [member/thijs-luttikholt], that OCT-AID can automatically detect high-risk plaques and predict adverse clinical outcomes more accurately than manual core lab assessment. These findings highlight the potential of AI to transform intracoronary imaging into a powerful, clinically actionable tool for risk stratification.

![PECTUS-AI]({{ IMGURL }}/images/news/cara_pectus_ai.png) 

## Artifact Detection

Our [artifact detection algorithm](https://arxiv.org/abs/2503.05322), led by [member/pierandrea-cancian] focuses on identifying attenuation artifacts within OCT recordings. It employs an A-line-based approach to distinguish between valid imaging data and regions affected by signal loss due to blood and gas bubbles, ensuring more accurate assessments of vessel structures and pathology. Our latest version also incorporates detection of nonuniform rotational distortion (NURD) and tangential signal dropout (TSDO) artifacts.

![Artifact detection model]({{ IMGURL }}/images/projects/cara_lab_model_artifact.png) 

## Model uncertainty in relation to expert variability
For AI-assisted image analysis to be clinically useful, it is essential to know when the output of a model can be trusted. To investigate how model uncertainty relates to the variability between expert readers, [member/joske-van-der-zande] and [member/leah-heil] performed a preliminary [study](https://ieeexplore.ieee.org/document/11516044) in which multiple expert analysts independently annotated the same intravascular OCT frames, revealing where expert readers agree and where they diverge. When compared with these manual annotations, OCT-AID exhibited the highest uncertainty in precisely those regions where experts disagreed, and its uncertain predictions were also the least accurate. These findings indicate that model uncertainty estimates are a meaningful confidence measure that can identify frames requiring expert review, thereby enhancing the transparency and trustworthiness of AI-assisted OCT analysis.

![Artifact detection model]({{ IMGURL }}/images/projects/cara_uncertainty.png) 

Stay tuned for updates on our ongoing developments in thrombus and plaque rupture detection, assessment of inflammatory characteristics, and stent modeling!
