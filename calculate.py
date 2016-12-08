# Calculates K for k means clustering where number of unique labels is unknown in pre-processed log files
import sys
log = sys.argv[1]
# with open(log,'r') as gt:
    # data = [line.strip() for line in gt.read]
    #data = [int (i) for i in gt.readlines()] #readlines gives one line at a time.

data = [line.strip() for line in open(log, 'r')]
# print (data) #prints list
print (set(data)) #prints set of list having unique elements
print('{} Total entries. k = {}'.format(len(data), len(set(data))))
