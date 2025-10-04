# Lab.01.3c
# This program read a csv from a file and calculates the age average of floating numbers
# By Ignacio Riboldi

import csv

filename = "data.csv" # FIle name
datadir = "../../Sources/" # File Location

with open(datadir + filename, "rt") as fp: # Open the file located where we told
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC) # Delimiter adds a comma between values # Quoting makes sure that values that are not in "" are read as numbers
    linecount = 0
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        # print(line)
        count += 1
    print(f"average is {total/(count)}")