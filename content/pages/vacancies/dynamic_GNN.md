title:  Dynamic graph network simulator for peptide-MHC-I structures 
groups: ai-for-health
closed: True
type: student 
picture: vacancies/dynamic_GNN.png
template: vacancy-single
people: Li Xue, Jolanda de Vries
description: Developping a  dynamic graph network simulator for peptide-MHC-I structures 


**This is an AI for Health MSc project. Students are
elgible to receive a monthly reimbursement of €500,- for
a period of six months. For more information please read the
[requirements](https://www.ai-for-health.nl/requirements/).** 

## Clinical Problem 
Deeper  understanding  of  the  immune  system’s  intricacies  has  led  to  clinical  breakthroughs  of  personalized  cancer  vaccines  in  eliminating  tumors  in  advanced-stage  cancer  patients  1-4  .  Formulated  with  fragments  from  a  patient’s  tumor  DNA,  cancer  vaccines  train  a  patient’s  own  immune  system  to  recognize  a  patient’s  mutated  cancer  proteins  as  ‘foreign’  and  wage  a  lethal  attack  against  tumors  (see  key  concepts  in  Box  1).  The  major  puzzle  in  this  field  is:  which  of  a  patient’s  hundreds  of  tumor  mutations  can  trigger  the  immune  system  to  attack  tumors  ?  Complementary  to  costly  and  time-consuming  wet-lab  screenings  (e.g.,  Sipuleucel-T  was  priced  at  $93,000  5  ),  predictive  algorithms  that  can  quickly  pinpoint  neoantigens  from  a  patient’s  tumor  DNA  are  urgently  needed,  if  personalized  cancer  vaccines are to be applied on a large scale. 
We aim to predict 3D peptide:MHC structures using a neural network simulator in this  project. 3D peptide:MHC structures bear crucial information for predicting effective cancer vaccine candidates, the major challenge of this field. Our overall aim is to improve the  efficacy, safety and development time of existing T cell based cancer vaccine approaches. 

## Solution 
General-purpose  AI  algorithms  predicting  3D  structures  of  proteins, l ike  AlphaFold2,  are  computationally  expensive  and  do  not  perform  well  on  proteins  without  MSA  (multiple  sequence  alignment),  an i mportant  source  of  evolutionary i nformation.  Here,  we  will  explore  using  a  dynamic  graph  neural  network  (GNN,  https://arxiv.org/abs/2102.09844)  for  modelling  3D  peptide:MHC  complexes  (peptides  do  not  have  MSA).  Protein  complexes  have  different  shapes  and  sizes  presenting  unique  challenges  to  conventional  machine l earning  algorithms,  which  take  fixed-size i nput.  Graphs  are  natural  representations  of  protein  complexes.  We  will  further i ntegrate  domain  knowledge  (e.g.,  where  are  protein i nterfaces,  experimentally  measured  distance  restraints,  and  so  on) i nto  the  GNN  model  to  restrain  the  structure  predictions  thus  speeding  up  the  computation.  This  project  pioneers i ntegrating  domain  knowledge  to  guide  AI-based  modelling,  and  thus  has  a  wide  range  of  applications  on  antibody:antigen, TCR:pMHC, and general protein-peptide interactions. 

Training  such  GNN  requires  at l east  hundreds  of  thousands  of  3D  structures,  which i s  a  big  data  challenge.  This  project i s  built  upon  DeepRank,  our  deep l earning  framework  for  data  mining  very l arge  sets  (up  to  millions)  of  protein i nterfaces.  The  resulting  software  will  be i ntegrated i nto  our  DeepRank  platform,  distributed  on  GitHub,  and  disseminated  through  user-community  workshops.  The  software  will  be  designed  generally  applicable  to  structural  biology, chemistry, human genetics and beyond.
 We specifically define the following tasks:  
 
 Task 1  : Train a GNN on a single well-studied peptide:MHC complex. The goal here is to find a  suitable architecture and the correct hyperparameters before proceeding to the bigger task of  making a general peptide:MHC complex predictor. For the test complex, we plan to use: PDB  ID: 3MGT, a crystal structure of a H5-specific CTL epitope variant derived from H5N1 influenza  virus in complex with HLA-A*0201. We will use the PANDORA software to generate 50,000  models, which will serve as training and validation datasets for the GNN.  
 
 Task 2  : Train the GNN from task 1 (but with more parameter capacity) on a bigger dataset  containing a great variety of peptides and MHC alleles. This is to accomplish our final desired  goal of predicting peptide conformations for any peptide:MHC complex. Here again we will use  the Pandora software package to generate/simulate the “true” models as labels for training 
 (dataset 3 below). For testing, we will use the experimentally derived peptide conformations  from dataset 1, which will be excluded from the train and validation sets to test the  generalization capacity of the final GNN.  
 
 Task 3:  Test the generalization capabilities of the trained GNN from task 2 on non-peptide loop  predictions. The GNN will, by design, iteratively update the peptide loop conformation until  convergence. Since the updates are based on local interactions, which should be general for  all loop formations, we will test whether or not the trained GNN can generalize to also model  TCR-CDR3 loops. We will test on a set of bound and unbound TCR:peptide:MHC structures.  We will take unbound CDR3 loops as the starting point of GNN and ask GNN to model the  bound conformation of CDR3 loops. We will also compare the final results with HADDOCK  simulation results, a flagship physics-based docking software for flexible modeling 
 protein-protein complexes. 

## Data 
We will use our PANDORA software to generate 3D peptide:MHC models and their energy  values. We have shown that PANDORA is able to reproduce near-native peptide:MHC  structures and other plausible conformations. 

 Dataset 1: X-ray pMHC-I structures and their energy values. 
 We have downloaded 841 X-ray pMHC-I structures from the IMGT database. 
  Dataset 2: 3D models for dataset 1 and their energy values. 
 For each entry in dataset 1, we will use PANDORA to generate N (100, to be optimized)  models. PANDORA also outputs the energy values for each model. 
 Dataset 3: 3D models for 147,326 strong MHC-I binders from biochemistry assays and their  energy values. 
 We collected 147,326  strong MHC-I binders from the MHCflurry paper, which are biochemistry  binding affinity data and mass spectrometry (MS) eluted data. For each entry, we will generate  100 PANDORA models along with their energies. 

## Embedding 
You will be embedded in the Center for Molecular and Biomolecular Informatics at Radboudumc. We provide access to CPU and GPU clusters, direct supervision by PhD students and regular meetings with the PIs of this project.

## Requirements 
- Students Artificial Intelligence, Data Science, Computer Science, Bioinformatics in the final stages of their Master education. 
- You should be proficient in python programming and have a theoretical understanding of deep learning architectures. 
- Basic biological / biomedical knowledge is preferred.

## Information 
- Project duration: 6 months 
- Location: Radboud University Medical Center 
- More information can be obtained from Li Xue (mailto: li.xue@radboudumc.nl)
