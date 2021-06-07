title: {Segmentation of tumor-infiltrating Lymphocytes}
groups: ai-for-health
finished: false 
type: student
picture: {projects/perspectief.jpg} (This picture appears on the the card shown on the project home page and is collected from website-content/content/images/. Image should be landscape, ratio 2:1, minimum width 480 px)
template: project-single
people: {Cyril de Kock, Francesco Ciompi, Tom Heskes, Mart Rijthoven, Witali Aswolinskiy}
description: {Developing an algorithmn that can automatically detect and segment tumor-infiltrating lymphocytes in breast cancer.} (This will appear on the card shown on the projects home page)

** Start date: {01-05-2021} ** <br>
** End date: {17-12-2021} **

## Clinical problem

{Recent studies have developed our knowledge regarding the tumor microenvironment to exploit tumor immunity in fighting breast cancer (BC). An important part of the immune system response to invase tumors is formed by tumor infiltrating lymphocytes (TILs), which are immune cells that infiltrate tumor tissue. Multiple studies have established a positive relationship between higher levels of TILs and survival outcomes in Triple Negative Breast Cancer and human epidermal growth factor receptor 2 positive. The amount of TILs can be quantified by estimating a TIL score, which is the percentage of the stromal area around the tumor that is covered TILs.

A patient's TIL score is assessed by estimating the proportion of TILs present in the tumor stroma.  As per the guidelines of the International TILs working group , the TIL score is assigned by the following procedure:
1. Define the tumor area in which TILs are to be evaluated
2.Segment the stromal areas.
3. Only evaluate mono-nuclear TILs
4. Asses the percentage of TILs as the fraction of stromal tissue covered by them
    
Scoring the percentage of TILs in a slide typically requires a trained pathologist to perform the evaluation. As such, manual TIL evaluation from slides is a slow process that can only be performed by a limited set of people. Automatically calculating the TIL score as well as producing detection and segmentation maps of stromal areas and their respective lymphocytes could be of great benefit to TIL research as well as facilitate the implementation of TIL scoring in clinical practice. This thesis aims to develop a system which segments the stromal area, detects and segments the TILs present within this area and subsequently uses this map to calculate a TIL score per slide.}

## Solution

{The purpose of this project is to produce an automated pipeline that can reproduce all of the steps involved in TIL scoring. First, the tumor including the invasive edge will be segmented, within this segmentation the stromal area will be marked as the proposed region in which to locate and count the TILs. After this step the individual TILs will be detected and segmented. Lastly we will automatically generate a TIL score per slide. The automatic calculation of the TIL score should considerably reduce pathologist efforts in diagnostics while the segmentation map is a tangible output that provides interpretability and allows for convenient checking of the TIL score.}

## Data

{The [NuCLS](https://sites.google.com/view/nucls/home?authuser=0) dataset will be used as the primary source of annotated slide data. The dataset aims at providing a high resolution mapping of cells and tissue for the purposes of segmentation, detection and classification. It contains just over 220,000 cell nuclei annotations spread over thirteen different classes. Other datasets may be added later in the process if the additional data can be made consistent and is found to facilitate increased performance in any of the sub-tasks. Note that the data in NuCLS does not come with a TIL score per slide. Scoring the slides will require additional data or information for proper evaluation.}

## Approach

{Cyril will be supervised by Francesco, Mart, and Witali whom all have previously worked on research related to TIL detection, segmentation and scoring. To create a system that can perform stroma segmentation, TIL detection and automated TIL scoring the state of the art convolutional neural approaches will be reviewed and adapted to the problem at hand. The Students get access to the high-performance deep learning cluster of DIAG, named SOL, for running machine learning experiments.}

## Results

{T.B.A} 