import operator
import makeCat
import readCSV
import makeProdMap

prodList = readCSV.readFile("salesHistory.csv")
prodMap = makeProdMap.makeProdMap(prodList)
productList = []
for key, value in sorted(prodMap.iteritems(), key=operator.itemgetter(1)):
	productList.append({key:value}) 

print "Most popular product: " + str(productList[-1:])
print "Least popular product: " + str(productList[0:1])

print makeCat.makeCat(productList)
