# for part g

current_point = (1,1)
minS = 1.0
minLine = ''
maxS = 0.0
maxLine = ''

with open('L4_1000.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		if(current_point==(int(temp[0]),int(temp[1]))):
			if(float(temp[5])<minS):
				minS = float(temp[5])
				minLine = temp
			if(float(temp[5])>maxS):
				maxS = float(temp[5])
				maxLine = temp
		else:
			crr = float(minLine[5])/float(maxLine[5])
			# rank1 = 
			print"{} {} \t [({},{}),{}] \t [({},{}),{}] \t {}".format(current_point[0],current_point[1],minLine[0],minLine[1],minLine[5][:-1],maxLine[0],maxLine[1],maxLine[5][:-1],crr)
			current_point = (int(temp[0]),int(temp[1]))
			minS = 1.0
			minLine = ''
			maxS = 0.0
			maxLine = ''
	#for the last current_point value
	crr = float(minLine[5])/float(maxLine[5])
	# rank1 = 
	print"{} {} \t [({},{}),{}] \t [({},{}),{}] \t {}".format(current_point[0],current_point[1],minLine[0],minLine[1],minLine[5][:-1],maxLine[0],maxLine[1],maxLine[5][:-1],crr)