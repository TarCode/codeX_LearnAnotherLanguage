import csv

list = []

def readFile(file):
        with open(file, 'rU') as csvfile:
                readData = csv.reader(csvfile, delimiter = ';', quotechar='|')
                for row in readData:
                        list.append(row)
           	return list[1:]