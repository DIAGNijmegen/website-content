title: Early prediction of multi-drug resistant Klebsiella species using machine learning
groups: rtc
closed: false
type: student
picture: vacancies/mosquito-biting.png
template: vacancy-single
people: Michael Rodgers, Evert den Drijver
description: Machine learning on antibiotic susceptibility testing data to predict MDR Klebsiella (ESBL/CPE) one day earlier than current laboratory workflows


## Background

When a patient is suspected of having a bacterial infection, clinical samples such as blood or urine are cultured in the medical microbiology laboratory. After identification of the bacterial species, automated antibiotic susceptibility testing is performed. This testing yields minimum inhibitory concentrations (MICs) for a broad range of antibiotics, which are used to classify bacteria as susceptible or resistant.

Some bacteria, however, are classified as multi-drug resistant (MDR). Two clinically important examples are *Klebsiella pneumoniae* and *Klebsiella oxytoca*. MDR strains, particularly those producing extended-spectrum beta-lactamases (ESBL) or carbapenemases (CPE), pose a major threat to patient safety and infection control. Patients carrying MDR bacteria must be placed in isolation to prevent hospital transmission. The prevalence of MDR *Klebsiella* species has increased steadily in recent years in the Netherlands, as reported in national surveillance programs such as NethMap [1].

Current laboratory workflows use simple rule-based criteria derived from automated susceptibility testing to raise suspicion of ESBL or CPE production. Definitive confirmation requires additional laboratory tests, which involve overnight incubation and delay results by at least one day. As a result, isolation measures may be implemented later than optimal.

The automated susceptibility testing systems generate far more information than is currently used in these rule-based approaches. MIC values are continuous, multiple antibiotics are tested simultaneously, and complex patterns of resistance may indicate MDR status. Machine learning methods are well suited to exploit such multidimensional data and have previously been shown to improve diagnostic screening for antimicrobial resistance in other bacterial species [2]. Earlier prediction of MDR *Klebsiella* could enable faster infection control measures and reduce hospital transmission.

## Approach

The aim of this project is to develop a machine learning model that predicts whether *Klebsiella pneumoniae* and *Klebsiella oxytoca* isolates are MDR (ESBL and/or CPE producers) using only the results of automated susceptibility testing.

The model will integrate MIC values across multiple antibiotics and learn patterns that are not captured by current rule-based systems.

The student will explore and compare different classification approaches, such as tree-based models and other supervised learning techniques. Model outputs may be binary (MDR vs. non-MDR) or probabilistic, providing a confidence estimate for MDR status. Performance will be evaluated against the current laboratory reference standard.

The ultimate goal is to enable reliable MDR prediction one day earlier than is currently possible.

## Data

The project will use routinely collected laboratory data from February 2019 onwards, including thousands of *Klebsiella pneumoniae* and *Klebsiella oxytoca* isolates. Approximately 10–20% of these isolates are classified as MDR, predominantly ESBL producers with a smaller proportion of CPE.

The reference standard consists of the results of confirmatory MDR tests currently performed in the laboratory, yielding binary outcomes (ESBL yes/no, CPE yes/no).

For a subset of isolates, whole-genome sequencing data are available, which represent the gold standard for identifying resistance mechanisms and may be incorporated into the analysis.

Data can be extracted from the laboratory information system into structured formats (e.g. CSV). All data are anonymized at the bacterial isolate level; no patient-identifiable information is required for this project.

## References

[1] NethMap 2024. Consumption of antimicrobial agents and antimicrobial resistance among medically important bacteria in the Netherlands.  
[2] Coolen JPM et al. Machine learning for improved diagnostic screening of antimicrobial resistance in *Escherichia coli*. *J Antimicrob Chemother.* 2019.

## Requirements

Students in the final phase of a Master’s program in Artificial Intelligence, Data Science, Biomedical Sciences, Computer Science, or a related field are invited to apply.

**Required skills:**

- Experience with Python programming
- Basic knowledge of machine learning and data analysis

Affinity with microbiology, infectious diseases, or antimicrobial resistance is an advantage.

## Information

**Project duration:** 6 months  
**Location:** Radboud University Medical Center

The student will be embedded within the Department of Medical Microbiology. A secure Digital Research Environment (DRE) and standard computing facilities are available for data analysis.

For more information, please contact Michael Rodgers (michael.rodgers@radboudumc.nl).

## People

**Michael Rodgers**  
Medical Microbiologist  
Department of Medical Microbiology, Radboudumc

**Evert den Drijver**  
Medical Microbiologist  
Department of Medical Microbiology, Radboudumc
