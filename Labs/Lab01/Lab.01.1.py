# Lab.01.1
# This program read a csv from a file
# By Ignacio Riboldi

import csv

filename = "data.csv" # FIle name
datadir = "../../Sources/" # File Location

with open(datadir + filename, "rt") as fp: # Open the file located where we told
    reader = csv.reader(fp, delimiter=",") # Delimiter adds a comma between values
    for line in reader:
        print(line)