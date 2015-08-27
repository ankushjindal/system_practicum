
res = 1000000

genuine = [0]*(res+1)
imposter = [0]*(res+1)

with open('L4.txt') as infile:
	for lineNo in infile:
		temp = lineNo.split('\t')
		line = (float(temp[5][:-1]), int(temp[4]))

		if line[1] == 1:
			genuine[int(line[0]*res)] += 1
		else:
			imposter[int(line[0]*res)] += 1

for i in range(1, res+1):
	genuine[res-i] += genuine[res-i+1]
	# genuine[i] += genuine[i-1]
	imposter[i] += imposter[i-1]

for i in range(len(genuine)):
	print(i/res, genuine[i]/res, imposter[i]/res)

final = []
for i in range(res+1):
	final.append(abs(genuine[i]-imposter[i]))
print(final.index(min(final)))

