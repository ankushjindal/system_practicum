import sys

print('Genuine rejected (FRR)')
with open('L4.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		if(int(temp[4])==1):
			if (float(temp[5][:-1])>sys.argv[1]):
				print(lineNo, end='')
