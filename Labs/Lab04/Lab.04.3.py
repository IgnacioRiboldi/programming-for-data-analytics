# Lab 04.3

import re

regex = r"\[.*\]"
filename = "/Users/nacho/Desktop/University/tutorialdata/www3/access.log"

with open(filename) as input_file:
    for line in input_file:
        foundTextList = re.findall(regex, line)
        if(len(foundTextList) != 0):
            # Print foundlist
            foundText = foundTextList[0]
            print(foundText)