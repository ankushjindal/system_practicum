# for part f
from pprint import pprint

gHist = {}
iHist = {}

with open('L4_1000.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		tempScore = float(temp[5])
		if (int(temp[4])==1):
			#genuine
			if tempScore in gHist.keys():
				gHist[tempScore]+=1
			else:
				gHist[tempScore]=1
		else:
			#imposter
			if tempScore in iHist.keys():
				iHist[tempScore]+=1
			else:
				iHist[tempScore]=1
pprint(gHist)

# pprint([(x,iHist[x]) for x in iHist if iHist[x]>2])