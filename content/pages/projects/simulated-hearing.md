
title: Simulated Prosthetic Hearing in deaf subjects
groups: diag, ai-for-health
finished: false
type: student
picture: vacancies/simulated_hearing.png
template: project-single
people:  Alex Tichter, Jan-Willem Wasmann, Marc van Wanrooij, Yağmur Güçlütürk, Umut Güçlü
description: Development of a neural network based model that improves speech perception in cochlear implant recipients, by optimizing the vocoder strategy in order to restore binaural hearing in deaf subjects.


## Background
Hearing loss is the second most prevalent (>440 million people affected) health impairment worldwide, with adequate diagnosis and treatment lacking for many. In case of severe or profound hearing impairment, rehabilitation can be provided by a cochlear implant (CI) that directly stimulates the auditory nerve via acoustically modulated electrical current pulses. The CI provides auditory sensations, and in the most successful cases leads to near-normal speech perception in low-noise listening conditions. However, not all CI recipients experience such a successful outcome; the variability in speech perception outcome among CI recipients is large. Moreover, under noisy listening conditions, CI performance is poor for all recipients.

Binaural hearing, which is essential for speech reception in noisy conditions, is currently missing in CI recipients. Only one implant is reimbursed for adults, effectively leading to only monaural restoration. Evidence however suggests that two ears are necessarily better. Still, recipients with two CI devices (bilateral CI recipients) have poor sound localization abilities. In practice, even bilateral CIs are fitted per side and do not account for potential bilateral effects of the implant.

When the performance of the CI recipient is sub-optimal, it is often not clear whether improvements are possible. Due to the vast parameter space that controls the cochlear implant, finding the optimal settings for the CI recipient is time-consuming for both patient and clinic, vary with local expertise, and can only include a small subset of parameters during the limited testing time.

Previous research showed that machine learning models can localize sound based on binaural data under normal or distorted listening conditions. We will unify earlier efforts to design a neural network that can adjust the parameter space of the vocoder in the distorted listening condition. The goal is to find the set of parameters that has the closest localization performance to the normal listening condition in an emulated CI recipient system.

## Hypothesis
An improved emulated strategy can provide valuable improvements and innovations for actual CI recipients to achieve binaural hearing, and thereby improved speech perception even under noisy listening conditions.

## Tasks
–	Simulating normal-hearing and CI recipient auditory systems of spatial hearing with DNNs.
–	Improve cochlear implant settings based on the network’s prediction
–	Validate the improved parameter set by comparing the localization performance of normal-hearing listeners between the original and optimized vocoder strategy

## Innovation
The aim of this project is to build a simulation of impaired directional hearing, which is able to predict the optimal settings for the CI recipient, while needing minimal time of patients and the clinic.
