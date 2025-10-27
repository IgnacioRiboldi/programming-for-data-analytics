# Lab.04.5


import re
#regex = "\d{1,3}\.\d{1,3} " # this will find other numbers apart from ips
regex = r"(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}" # we make a group at the beginning to keep
replacementText = r"\1XXX.XXX " # note the space at the end to match above
filename = "/Users/nacho/Desktop/University/tutorialdata/www3/access.log"
outputFileName = "anonymisedIPs.txt"
with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
# for debugging
#foundText = re.search(regex, line).group()
#print(foundText)
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)