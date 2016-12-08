# shiny-goggles

k-means calculator for log files

##Usage

python calculate.py filteredLog
##About
This small program calculates the number of unique log error messages in files.

Number of unique elements will be returned which can be used for k means clustering.
##Appendix
filteredLog - Processed log file

DefaultLog - Default apache log dump

##IMPORTANT

Log files should be pre-processed and should be devoid of date, time and ip Adresses. Only core
log messages should be present in the file.
