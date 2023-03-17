title: HealthyAI
title_long: HealhtyAI
finished: false
type: general
picture: projects/prostate.jpg
template: project-single
groups: diag
people: Henkjan Huisman, Derya Yakar
description: 
bibkeys: 

## Background

Recent breakthroughs in Artificial intelligence (AI) allow its use as an assistive technology in
healthcare. However, the adoption of AI is stalling partly because of a lack of trust by clinicians and
patients. HEALTHY-AI is about developing trustworthy, robust AI, with a primary application to prostate
cancer diagnosis with MRI. Prostate cancer strikes as many as 1 in 9 men. Recent developments in
prostate MRI make non-invasive detection feasible. This avoids biopsies and allows for earlier
detection at a more curable stage. However, the rapidly increasing workload and high level of expertise
are a huge concern. AI can exploit MRI to its full potential to maximize impact on quality of care, reduce
healthcare costs, and reallocate time for routine decision-making to human-centric care.
HEALTHY-AI brings together the clinical knowledge institutes Radboudumc, UMCG, and the University
of Twente with industrial partner Siemens Healthineers. Its mission is to explore novel AI technology
and ethical challenges to achieve trustworthy AI.
![HealthyAI]({{ IMGURL }}/images/projects/prostate.jpg)

## Aim

Project 1. AI methods in medical imaging and analysis often require large training data sets and accurate labels.
While the availability of large datasets continues to improve, annotation remains time-consuming, expensive, and
challenging to keep cohesive. The scientific challenge is to develop AI methods for prostate MRI analysis that are
repeatable, reproducible, and safe by requiring less training data and using problem-specific model-driven
knowledge inside. This project will develop repeatable, reproducible, and safe physics-informed graph neural
networks by including model-driven data symmetries and manifold-based graph embeddings. Graph neural networks (GNNs) are a powerful tool to model interactions and relations between heterogeneous data and understand them in both a global and local manner. By developing generative adversarial networks (GANs) on such manifold embeddings will boost data synthesis in uncertain training data regimes hence increasing data
safety inside our developed AI methods.

Project 2. We will experiment with Reinforcement Learning (RL) that will be unique in that it will follow in its design,
training, and evaluation of a structured “ethical AI” roadmap. The ultimate aim is to render RL suitable for use in
clinical routine. To achieve this goal, we will seek to explore AI algorithms that are transparent and explainable.
Furthermore, the sequences of (potentially off-policy) clinical decisions for individual patients should improve long-
term health outcomes. As a clinical use case for this work, we will focus on prostate cancer treatment. Appropriate
clinical data is already available in an open-source database of pathway data such as the MIMIC IV database and
existing clinical pathway data available at RUMC.

Project 3. Merely applying a retrospectively trained algorithm on prospective cases will not allow it to improve its
diagnostic accuracy, in other words, it will not be able to learn from its encounters or mistakes. For AI to resemble
human intelligence it needs to be dynamic or “living”. The hypothesis is that AI can be embedded in a continuous
feedback framework with scientific oversight that strives to improve performance and trust. The research questions
are:
* What are the legal consequences? This new framework will deviate from the conventional CE/FDA certification process that regulates validity for clinical use. Can it be seen as an extreme form of post-
marketing surveillance?
* How to set up such a framework? This involves novel techniques for the continuous collection of new
cases, AI predictions, and outcome data. Moreover, it involves a scientific board that compares and
interprets AI deficiencies.
* What constitutes an AI deficiency? Similar to aviation, it makes sense to not just look at collisions only,
but also include near misses.
* What does AI need to report to help identify deficiencies and build trust? Novel technological AI
developments include the prediction of uncertainty, calibrated probability, image quality, and the rarity of a
case. These novel AI outcome features can help build trust by providing direct clinical feedback about AI
validity, but impose novel challenges as to the use for detecting deficiencies and even to the assessment
of the validity of these new outcomes.

Project 4. In prostate MRI, assessing follow-up imaging is still new. A trustworthy AI for imaging follow-up has a
double goal of helping mature a novel clinical application and assisting its current use. AI needs to provide robust
biomarkers for the appearance of new lesions, progression of existing lesions. AI needs to tell its confidence level.
If for reasons including those above, AI indicates uncertainty, then it should warn the user, which can then carefully
inspect the cause of uncertainty.

Project 5. Prostate, breast, and liver MRI is the fastest-growing use case of MRI in oncology. Upscaling services
from a few specialized centers to widespread clinical adoption increases the need for reliability, robustness, and
reproducibility of image acquisition and radiological evaluation. The radiographer has a critical role in image
acquisition, and robustness and reproducibility are highly dependent on their individual skills. AI has vast potential
to assist the MRI operator in making timely decisions for better results, e.g., by automatically detecting a patient's
breath-hold capability, implant status, the presence or absence of motion, and providing the operator with
recommendations patient-tailored strategies.

## Funding
* Part of the ROBUST ICAI lab funded by NWO and RVO: https://icai.ai/icai-labs/healthyai/
