#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv
import collections
total = 0
values = []
candidates = set()
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        total += float(row[9])
        values.append(float(row[9]))
        candidates.add(row[2])
n = len(values)
values.sort()
minimum = min(values)
maximum = max(values)
mean = total/n
print mean

def calc_median(list_of_values):
    n = len(list_of_values)
    if (n % 2) == 1:
        median = values[n/2]
    else:
        a = values[n/2 - 1]
        b = values[n/2]
        median = (a+b)/2
    return median
median = calc_median(values)
variance = sum(((x - mean)**2 for x in values))/n
stdev = variance**0.5


##### Print out the stats
print "Total: %s" % total
print "Minimum: %s" % minimum
print "Maximum: %s" % maximum
print "Mean: %s" % mean
print "Median: %s" % median
# square root can be calculated with N**0.5
print "Standard Deviation: %s" % stdev

##### Comma separated list of unique candidate names
#Used semicolon instead of comma, as names already carry commas in them
print "Candidates: %s" % '; '.join(candidates)

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    if value > maximum or value < minimum:
        raise ValueError("Value is not in range of original dataset")
    
    norm = (value - minimum)/(maximum -  minimum)
    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

