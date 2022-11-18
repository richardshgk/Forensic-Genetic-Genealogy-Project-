# Forensic Genetic Genealogy Analysis 

As a true crime enthisust with a special interst in the science of solving these crimes I was very excited to come across Tracey Dowdeswell's ['Forensice Genetic Geneaology Project v. 2021'](https://data.mendeley.com/datasets/2jvgmbrjgm) dataset. The public frequently hears anecdotes from investigators and criminal prosecutors about how quickly or seemingly miraculously Forensic Genetic Genealogy (FGG) is helping solve cold cases. From idenitifying the Golden State Killer (April 2018) to finally giving Ruth Marie Taylor, Massachusettes' Lady in the Dunes and oldest unidentifed Doe, her name back (October 2022) FGG is certainly in the headlines. But how many cases is this new technique actually solving and is it actually moving as quickly as anecdotes say? 

Forensic Genetic Genealogy is the combination of DNA analysis and geneteic techniques used to identify individuals involved in a crime or criminal investigation. This technique uses a STR profile 

## My Analysis 
* Please note:  For this analysis I chose to use the data from only criminal cases (homicides, kidnappings, etc). Data from human remains investigations, living Does, and disaster victim investigations were not included in my analysis, even if circumstances surrounding the death suggest foul play. *

When comparing the two charts it is immediately apparent that after FGG is begun on a case, the time it takes to clear the case is drastically reduced. While the majority of these cases took 20-45 years to be cleared, Very few cases took more then 3 years to be cleared, with the majority of cases being cleared after  year. However it should be noted that comparitively few cases took less then 15 years to be cleared. This is, to me, an indication that investigators are seeing and using FGG to clear cold cases, not as a technique to solve active cases. 


### A note about the data: 
All of the data used in this project comes from the ['Forensic Genetic Genealody Project v. 2021' by Tracey Dowdeswell.](https://data.mendeley.com/datasets/2jvgmbrjgm) As stated in the project description, all data was collected from publically available sources, not directly from investigators or the investigating agency. For this reason there are understandable gaps in the data, especially in the dates materials were turned over to FGG. 
For more details on how the data was collected, what criteria were used, and the project's User Manual please visit the project's [Mendeley Data page](https://data.mendeley.com/datasets/2jvgmbrjgm).



## Required Modules:  
pip install pandas
pip install matplotlib
pip install numpy
pip install datetime
pip install xlrd 

## Code Kentucky
-------------------------------------------------------------------------------------------------------------------------
This project was done for a final grade a Code Kentucky. 

- Data was read in from an xlsx file using the pandas and xlrd modules.
- Data was cleaned using built in functions from the pandas and numpy modules. 
- General pandas calculations were used to learn more about the data and do calculations over the dataframe for plotting. 
- Two histogram plots were created using the pyplot feature in matplotlib.
- Please see paragraph four above for my interpretation of the data. 