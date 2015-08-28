# for part d

eer = 0.5000 #enter err here

print('Genuine rejected (FRR)')
with open('L4_1000.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		if(int(temp[4])==1):
			#imposter
			if (float(temp[5][:-1])>eer):
				#frr
				print lineNo
