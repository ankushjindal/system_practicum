# for part c,d

eer = 0.5000 #enter err here
imposter_total = 0
genuine_total = 0

with open('L4_1000.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		if(int(temp[4])==0):
			#imposter
			imposter_total += 1
			if (float(temp[5][:-1])<eer):
				#far
		else:
			#genuine
			genuine_total += 1
			if (float(temp[5][:-1])>eer):
				#frr
