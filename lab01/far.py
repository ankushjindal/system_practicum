# for part c

eer = 0.5000 #enter err here

print('Imposter passed (FAR)')
with open('L4_1000.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		if(int(temp[4])==0):
			#imposter
			if (float(temp[5][:-1])<eer):
				#far
				print lineNo
