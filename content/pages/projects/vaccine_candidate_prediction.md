title: 3D Convolutional Network based cancer vaccine candidate predictions
groups: ai-for-health 
finished: true 
type: student 
picture: projects/vaccine_candidate_prediction.png 
template: project-single 
people: Daniil Lepikhov, Dario Marzella, Daniel Rademaker, Li Xue 
description: Develop an AI method to identify cancer vaccine candidates using 3D Convolutional Networks  - a proof of concept
 
**Start date: 01-02-2022** 
**End date: 31-07-2022**
 
## Clinical Problem

Deeper understanding of the immune system’s intricacies has led to clinical
breakthroughs of personalized cancer vaccines in eliminating tumors in advanced-stage
cancer patients. Formulated with fragments from a patient’s tumor DNA, cancer
vaccines train a patient’s own immune system to recognize a patient’s mutated cancer
proteins as ‘foreign’ and wage a lethal attack against tumors. The major puzzle in this field is: which of a patient’s hundreds of tumor mutations can trigger the immune system to attack tumors? Complementary to costly and time consuming wet-lab screenings (e.g., Sipuleucel-T was priced at $93,0005), predictive algorithms that can quickly pinpoint neoantigens from a patient’s tumor-specific proteins are
urgently needed, if personalized cancer vaccines are to be applied on a large scale.
We aim to predict cancer vaccine candidates in this project. Our overall aim is to
improve the efficacy, safety and development time of existing T cell based cancer
vaccine approaches
 
## Solution

To serve as good cancer vaccine candidates, the tumor-specific peptides (i.e., short segments of tumor proteins) have to bind to the patient’s MHC (Major histocompatibility complex) molecule and form peptide:MHC protein complexes. The MHC molecule then ships the tumor peptides to the cell surface to be visible to the immune T cells to trigger immune attacks.  [please add a newline here  in the md file]
 
![Peptide:MHC TCR interaction]({{ IMGURL }}/images/projects/TCR-MHC.png)

Today, state of the art predictive algorithms predict MHC-binding peptides based on the 1D sequences of MHC and peptides.  Common residue patterns in the peptides’ sequence are elucidated by going over big datasets of experimental binding affinity values of peptide:MHC complexes, by using different computational approaches (e.g., fully connected neural networks, recurrent neural networks, hidden Markov models, etc). However, the existing methods have limited performance. This may be caused by several factors. First, the binding affinity depends on atomic features such as the hydrophobicity, Van der Waals interaction, solvent accessibility and other parameters. Sequence-based approaches can only indirectly capture the physico-chemical parameters that really determine the binding affinity of a similar complex.  Second, the existing methods are data-driven ML methods. They rely heavily on the training data. This makes the existing methods to have limited accuracy on rare peptides that are not well-represented in the training data, for example, tumor frameshift mutations. Also they will not perform well on MHC alleles without enough training data. MHC alleles are highly polymorphic on sequences. 

To tackle these problems, in this project we explored the 3D structure-based prediction approach and its generality to rare peptides. We want to train 3D-CNN on 3D structures of pMHC models to learn interaction patterns in the space of energies, shapes and sequences. 

Energy patterns at the atom level should be universally applicable to data that are not seen in the training set. MHC structures are highly conserved (i.e., different alleles have almost the same structures). So MHC structures should be able to drastically reduce the need for training data. Our 3D structure based approach can also naturally deal with peptides with different lengths, a challenge for typical machine learning algorithms that take fixed-length input.


This will be done by using a 3D convolutional neural network algorithm (our DeepRank software https://www.nature.com/articles/s41467-021-27396-0) trained on
3D models for peptide:MHC complexes generated with high-accuracy package (our PANDORA software https://www.frontiersin.org/articles/10.3389/fimmu.2022.878762/full). The solution provided allows to address the issue of predicting binding affinity between peptide and MHC with a new approach paving the way for further investigation concerning a structure based prediction on unseen data.

## Data

The data used for this work comes from binding affinity assays. Several types of
experiments are available to quantitatively assess how strongly one peptide can bind to
the MHC groove. Experiments include measurements of half maximal inhibitory
concentration (IC50), half maximal effective concentration (EC50), binding constant (Kd)
which all allows us to assess the binding affinity. Some of these rely on the competitiveness of
the peptide compared to a fluorescent/radioactive strong binder (EC50, IC50). Binding
affinity assays are conducted in a completely artificial setup where one HLA allele is fixed
on the support and the tested peptide is being added at varying concentration, in presence
of a competitor. Resulting measurement is only viable if the conditions of the experiments
are as close as possible to physiological chemical conditions (temperature, pH, electrolyte
concentration). Binding affinity values below 500nM indicates a binder (100nM and lower
being strong binders), values above this threshold are not considered as binders.

7,726 Binding affinity values were extracted from the MHCflurry 2.0 paper dataset. It represents 3512 binding peptides and 4214 non binding peptides with a threshold of 500nM.

To check the generability of our approach to unseen peptides, we clustered the peptides into 10 clusters . 
 
## Approach
As a proof of principle study, peptides with the most frequent length of 9 residues
with known binding affinity to one MHC-I allele (HLA-A*02:01) are investigated. With these
criteria, a total of 7,726 p:MHC-I binding affinity values were retrieved. For every binding
affinity value, related p:MHC-I structure was generated using the p:MHC integrative
modelling tool PANDORA. Using our DeepRank feature generator, each atomic-level and
residue-level feature is mapped on the grid. Those features are learned by the 3D
convolutional neural network (3D CNN) and the results will be compared with structure-
based approach. For a fair comparison, a fully connected neural network will be trained on
the same dataset using one-hot encoded sequence of peptides. To demonstrate predictive
performances of the 3D CNN, clusters of peptides used for training have very distant
sequences from the clusters used for evaluation of the model.
 
![Grid at the interface of the p:MHC complex]({{ IMGURL }}/images/projects/pMHC_grid.png)
 
## Results
![Final results]({{ IMGURL }}/images/projects/3dVacFinalResult.png)
 
Metrics used to evaluate performances are 1)- sensitivity or true positive rate, which
is the amount of positives in the validation dataset (true positives) divided by the number of
predicted positives. 2)- Specificity or true negative rate, calculated by dividing the number
of true negatives by the total number of predicted negatives. 3)- Area under the receiver
operating characteristic curve AUC. For a value between 0-0.5, false positive rate is higher
than true positive rate. The closer the value is to 1 the better the model is able to predict
positive values while keeping the false positive rate low. The closer the value is to 0.5, the
higher false positive rate gets. If the AUC is equal to 0.5, the amount of false positive is
50%. 4)- Mathew correlation coefficient MCC ranges between -1 and 1. Compared to AUC,
it is a single-value classification metric incorporating sensitivity and specificity in the
scoring process. A high score depends on a good sensitivity and specificity, together with
false positive and negative rate being low. A score of 0 means random predictions, a score
of 1 means perfect predictions and -1 opposite predictions.
 
The results indicate that CNN (structure-based approach) has more similar predictive performances on shuffled and clustered datasets compared to sequence based approach. Indeed, sensitivity, accuracy and
MCC score remains high, even if overall there is more variability for the predictor trained
on a clustered model. MLP (sequence-based approach) metrics are consistently lower for
the clustered and shuffled compared to CNN at the exception of AUC (capacity to predict
positives) and specificity (true negative rate). This gives the intuition that a structure-based
approach is able to perform better on unseen sequence motifs compared to a sequence-
based approach, thus generalizing better to unseen data. 

Note that we worked on a set of fixed-length peptides and on a single MHC allele. This is to the advantage of sequence-based approaches. The advantages of our structure-based CNN are expected to be further visible when we train and test on peptides with variable lengths and with diverse MHC alleles in a much bigger dataset. 

