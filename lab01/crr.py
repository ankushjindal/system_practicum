# for part g

current_point = (1,1)
min = 1.0
max = 0.0

with open('L4_1000.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		if(current_point==(int(temp[0]),int(temp[1]))):
			if(float(temp[5])<min):
				min = float(temp[5])
			if(float(temp[5])>max):
				max = float(max[5])
