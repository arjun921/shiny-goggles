# shiny-goggles

k-means calculator for log files

##Usage

run command - python calculate.py filteredLog

For testing purposes I've used a filtered log from apache log-dump

Number of unique elements will be returned which can be used for k means clustering.

##IMPORTANT

Log files should be pre-processed and should be devoid of date, time and ip Adresses. Only core
log messages should be present in the file.
