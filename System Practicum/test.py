
res = 1000000

cnt = 0

with open('L4_1.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		print(temp)
		line = (float(temp[5][:-1]), int(temp[4]))
		# print(lineNo)
		cnt += 1

print(cnt)

