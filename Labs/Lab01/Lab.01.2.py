# Lab.01.2
# This program read a csv from a file and adding a line under the header
# By Ignacio Riboldi

import csv

filename = "data.csv" # FIle name
datadir = "../../Sources/" # File Location

with open(datadir + filename, "rt") as fp: # Open the file located where we told
    reader = csv.reader(fp, delimiter=",") # Delimiter adds a comma between values
    linecount = 0 # Line counter
    for line in reader:
        if not linecount: # First row is header row
            print (f"{line}\n---------------------------------")
        else: #all subsequent rows
            print(line)
        linecount += 1