# Logistic-model-and-Python-GIS-methods

This project is a set of replications of a model used by Markus Gehersitz and Martin Ungerer in their paper Jobs, Crime and Votes: A Short-run Evaluation of the Refugee Crisis in Germany. 
doi:10.1111/ecca.12420


The main folder consists of the following folders:

- ArcGIS
- data
- R code

ArcGIS folder includes Python code and shape files of a map of Germany. The shape file is openly accessible on a website of https://gadm.org/.
The Python code applies ArcGIS methods to get a list of neighbour counties of TOP 5% GDP per capita producing German counties according to 2016.
Please unzip ArcGIS folder and use Python code in the code subfolder to run GIS methods on to the shape file.

Data folder includes various type open sourced data, which can be reached via a website of https://www.inkar.de/.

R code folder contains R code, which runs code to clean the data, to run a regression and to plot a graph of logistic model.
R code also runs logistic model using the available data.


There is only one dataset which is not available openly, that is each county's reception centers capacity (Erstaufnahmeeinrichtungen, EAEs) in years 2014 and 2015. As a proxy to this, the aggregate data mentioned in the paper is used by cleaning, averaging and estimating per 100.000 using population data of the year in question. 
