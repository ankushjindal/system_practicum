# python 2.7
# for part g

current_point = (1,11)
minS = 1.0
minLine = []
maxS = 0.0
maxLine = []

cnt = 0
rank = 0
with open('L4.txt') as infile:
	for lineNo in infile:
		temp = lineNo[:-1].split('\t')
		if(current_point==(int(temp[0]),int(temp[1]))):
			if(float(temp[5])<minS):
				minS = float(temp[5])
				minLine = temp
			if(float(temp[5])>maxS):
				maxS = float(temp[5])
				maxLine = temp
		else:
			crr = float(minLine[5])/float(maxLine[5])
			if int(current_point[0])==int(minLine[2]):
				rank1 = 1
				rank += 1
			else:
				rank1 = 0
				cnt += 1
			print"{} {} \t [({},{}),{}] \t [({},{}),{}] \t {} \t {}".format(current_point[0],current_point[1],minLine[2],minLine[3],minLine[5],maxLine[2],maxLine[3],maxLine[5],crr,rank1)
			current_point = (int(temp[0]),int(temp[1]))
			minS = 1.0
			minLine = []
			maxS = 0.0
			maxLine = []
	#for the last current_point value
	crr = float(minLine[5])/float(maxLine[5])
	if int(current_point[0])==int(minLine[2]):
		rank1 = 1
		rank += 1
	else:
		rank1 = 0
		cnt += 1
	print"{} {} \t [({},{}),{}] \t [({},{}),{}] \t {} \t {}".format(current_point[0],current_point[1],minLine[2],minLine[3],minLine[5],maxLine[2],maxLine[3],maxLine[5],crr,rank1)

print(rank/(float)(rank+cnt))

