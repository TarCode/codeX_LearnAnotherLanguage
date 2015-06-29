prodMap = {}

def makeProdMap(prodList):
	for x in prodList:
		if prodMap.has_key(x[2]) == False:
			prodMap.update({x[2]:int(x[3])})
		else:
			for key in prodMap:
				if key == x[2]:
					if x[3].isdigit():
						prodMap[key] += int(x[3])

	return prodMap

        