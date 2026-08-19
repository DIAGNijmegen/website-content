title: "Diagnostically Calibrated AI Image Quality Framework Applied to Prostate Cancer Detection at MRI" — in Radiology
date: 2026-08-18
description: A new diagnostically calibrated deep learning framework linking prostate MRI image quality scores to diagnostic performance is now published!
picture: news/2026-coelho-radiology.png
groups: diag

A diagnostically calibrated artificial intelligence (AI) framework for prostate MRI image quality assessment has been published in Radiology.

*"Deep learning framework–derived image quality thresholds progressively excluding low-quality MRI scans correlated with improved diagnostic performance of an artificial intelligence model and radiologist accuracy in detecting clinically significant prostate cancer."*

The study introduces a two-step deep learning (DL) framework that derives a continuous image quality score from axial T2-weighted prostate MRI and calibrates that score against real diagnostic performance. As progressively stricter quality thresholds excluded the lowest-quality scans, both an AI model and radiologists became more accurate at detecting clinically significant prostate cancer (csPCa) — directly linking image quality to diagnostic outcomes rather than to subjective visual impressions alone.

👉 Read the full publication [here](https://pubs.rsna.org/doi/10.1148/radiol.253360)!

An accompanying editorial by Dr. Tristan Barrett is also available [here](https://doi.org/10.1148/radiol.262030).

𝗦𝘁𝘂𝗱𝘆 𝗢𝘃𝗲𝗿𝘃𝗶𝗲𝘄 🧪
This single-center retrospective study analyzed 12,496 consecutive prostate multiparametric MRI examinations performed between January 2014 and December 2023 at [Radboud University Medical Center](https://www.radboudumc.nl). A DL model was first trained on the most reliable low-quality (artifact-degraded structures) and high-quality (clear delineated zones) axial T2-weighted images to produce a continuous image quality score. This score was then applied in an independent internal test set of 568 multiparametric MRI examinations and calibrated against diagnostic performance, measured as the AUC of an AI model and the accuracy of radiologists for clinically significant prostate cancer (csPCa) detection, using histopathology as the reference standard.

𝗞𝗲𝘆 𝗢𝘂𝘁𝗰𝗼𝗺𝗲𝘀 📈
The DL model achieved a mean AUC of 0.99 for distinguishing low- versus high-quality images during fivefold cross-validation. In the test set, AI model AUC for csPCa detection improved from 0.92 (95% CI: 0.89, 0.94) to 0.99 (95% CI: 0.97, 1.00) (P = .005) across image quality score thresholds, while radiologist accuracy improved from 77% (95% CI: 73, 80) to 85% (95% CI: 78, 91) (P = .01).

𝗖𝗹𝗶𝗻𝗶𝗰𝗮𝗹 𝗣𝗲𝗿𝘀𝗽𝗲𝗰𝘁𝗶𝘃𝗲 🩺
These results show that an objective, standardized image quality score can be directly linked to diagnostic performance, offering a path toward real-time quality control during MRI acquisition to support both AI systems and radiologists in csPCa detection.

Congratulations to [member/tiago-coelho], [member/joeran-bosma], [member/vilma-bozgo], [member/stan-noordman], [member/robert-grimm], Maarten de Rooij, Marnix Maas, and [member/henkjan-huisman] for their work!
