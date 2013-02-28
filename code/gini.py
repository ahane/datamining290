#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
from collections import Counter, defaultdict
(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variables
# TODO: declare datastructures
zipcodes = defaultdict(Counter)
candidates = Counter()
############### Read through files
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        ###
        # TODO: replace line below with steps to save information to calculate
        # Gini Index

        zipcodes[row[contbr_zip]][row[cand_nm]] += 1 
        candidates[row[cand_nm]] += 1
##/

###
# TODO: calculate the values below:
total = sum(candidates.values())
gini = 1 - sum(((float(count)/total)**2 for count in candidates.values()))   # current Gini Index using candidate name as the class

split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/
for zipcode in zipcodes.keys():
    zip_total = sum(zipcodes[zipcode].values())
    zip_gini = 1 - sum(((float(count)/zip_total)**2 for count in zipcodes[zipcode].values()))
    split_gini += (float(zip_total)/total)*zip_gini

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
