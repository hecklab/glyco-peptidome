# glyco-peptidome

These scripts where used in the data analysis of the described paper below. These scripts combined all search output data from Byonic and then profiled the phosphorylation and O-glycosylation PSMs along the protein back bone of β-casein. Please see the published paper for links to the data uploaded to MassIVE. 

**Monitoring β-casein phosphorylation and O-glycosylation over lactation reveals distinct differences between the proteome and endogenous peptidome**

*Kelly A. Dingess<sup>1,2</sup>, Inge Gazi<sup>1,2</sup>, Henk van den Toorn<sup>1,2</sup>, Marko Mank<sup>3</sup>, Bernd Stahl<sup>3,4</sup>, Karli R. Reiding<sup>1,2\*</sup>, Albert J.R. Heck<sup>1,2\*</sup>*
	
1. Biomolecular Mass Spectrometry and Proteomics, Bijvoet Center for Biomolecular Research and Utrecht Institute for Pharmaceutical Sciences, University of Utrecht, Padualaan 8, Utrecht 3584 CH, The Netherlands
2. Netherlands Proteomics Center, Padualaan 8, Utrecht 3584 CH, The Netherlands
3. Danone Nutricia Research, Uppsalalaan 12, 3584 CT Utrecht, The Netherlands
4. Chemical Biology & Drug Discovery, Utrecht Institute for Pharmaceutical Sciences, University of Utrecht, Universiteitsweg 99, 3584 CG Utrecht, The Netherlands


\*Corresponding authors: Karli R. Reiding, E-mail: k.r.reiding@uu.nl; Albert J. R. Heck, E-mail: a.j.r.heck@uu.nl

Keywords: Human milk, Mass Spectrometry, O-Glycosylation, Peptidomics, Antimicrobial peptides 

------

# Instructions for use

First, the Byonic output files from the article must be downloaded and combined using the python script. The script will read all \*.xlsx files from the current directory, and outputs a file called "Combined.xlsx".
The script uses the **pandas** package.

Second you can run the jupyter notebook to go through the analysis done in the article, reading in the Combined.xlsx file. This notebook uses the R kernel, and it requires the tidyverse, cowplot, scales, readxl packages.
