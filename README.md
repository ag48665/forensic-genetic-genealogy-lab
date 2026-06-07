\# Forensic Genetic Genealogy Lab



Educational forensic genomics project for simulating SNP-based relatedness estimation and forensic genetic genealogy workflows.



\## Overview



Forensic genetic genealogy combines genomics, population genetics, and genealogical analysis to identify unknown individuals through biological relatives.



This project explores computational approaches for estimating genetic relatedness using simulated SNP profiles and Monte Carlo experiments.



The framework demonstrates how genetic similarity can distinguish close relatives from unrelated individuals.



\---



\## Scientific Motivation



Forensic genetic genealogy has become an important tool in:



\- Missing persons investigations

\- Human remains identification

\- Disaster victim identification

\- Cold case investigations

\- Relationship inference

\- Genealogical research



This project provides an educational introduction to SNP-based relatedness analysis and identity-by-descent concepts.



\---



\## SNP Relatedness Experiment



Evaluates genetic similarity between biological parents and their children using simulated SNP profiles.



!\[IBD](reports/ibd\_experiment.png)



Example results:



| Relationship | Average Similarity |

|-------------|-------------------|

| Parent-Child | 0.500 |

| Unrelated | 0.334 |



Results show substantially higher SNP similarity between biological relatives than between unrelated individuals.



\---



\## Sibling Relatedness Experiment



Evaluates SNP similarity between biological siblings.



!\[Sibling IBD](reports/sibling\_ibd\_experiment.png)



Example results:



| Relationship | Average Similarity |

|-------------|-------------------|

| Siblings | 0.708 |

| Unrelated | 0.334 |



Biological siblings share considerably more genetic information than unrelated individuals, demonstrating the usefulness of SNP-based relationship inference.



\---



\## Identity-by-Descent (IBD)



Identity-by-Descent refers to genomic regions inherited from a common ancestor.



In forensic genetic genealogy, IBD sharing is commonly used to:



\- Estimate biological relationships

\- Prioritize potential relatives

\- Support missing person identification

\- Assist human remains identification



The experiments in this project provide simplified educational demonstrations of these concepts.



\---



\## Research Questions



1\. How can SNP profiles be simulated computationally?

2\. How can biological relatives be distinguished from unrelated individuals?

3\. How does genetic similarity vary across different relationships?

4\. How can forensic genetic genealogy support human identification?



\---



\## Methods



\- SNP profile simulation

\- Mendelian inheritance modeling

\- Parent-child relatedness estimation

\- Sibling relatedness estimation

\- Monte Carlo simulation

\- Data visualization using Python



\---



\## Project Structure



```text

forensic-genetic-genealogy-lab/

│

├── reports/

│   ├── ibd\_experiment.png

│   ├── sibling\_ibd\_experiment.png

│   ├── ibd\_results.csv

│   └── sibling\_ibd\_results.csv

│

├── src/

│   ├── snp\_simulator.py

│   ├── relatedness.py

│   ├── ibd\_experiment.py

│   ├── sibling\_ibd\_experiment.py

│   ├── plot\_ibd\_results.py

│   └── plot\_sibling\_ibd\_results.py

│

├── data/

├── notebooks/

├── tests/

│

├── requirements.txt

└── README.md

```



\---



\## Reproducibility



Install dependencies:



```bash

pip install -r requirements.txt

```



Run experiments:



```bash

python src/ibd\_experiment.py

python src/sibling\_ibd\_experiment.py

```



Generate plots:



```bash

python src/plot\_ibd\_results.py

python src/plot\_sibling\_ibd\_results.py

```



\---



\## Future Work



\- First cousin simulation

\- Identity-by-Descent segment simulation

\- Shared centimorgan (cM) estimation

\- Population structure modeling

\- SNP frequency-based relatedness estimation

\- Missing persons identification workflows

\- Advanced forensic genetic genealogy methods



\---



\## Disclaimer



This project is intended for educational and research-training purposes only.



It is not validated for forensic casework and must not be used in real investigations.



\---



\## Author



Agata Gabara

