import statistics as st

res = 1000000

gen, imp = 0, 0
genuine = [0]*(res+1)
imposter = [0]*(res+1)
genuine_score = []
imposter_score = []

infile = open('L4.txt')
for lineNo in infile:
	temp = lineNo.split('\t')
	line = (float(temp[5][:-1]), int(temp[4]))

	if line[1] == 1:
		gen += 1
		genuine[int(line[0]*res)] += 1
		genuine_score.append(line[0])
	else:
		imp += 1
		imposter[int(line[0]*res)] += 1
		imposter_score.append(line[0])

print(len(genuine_score), st.mean(genuine_score), st.stdev(genuine_score))
print(len(imposter_score), st.mean(imposter_score), st.stdev(imposter_score))

for i in range(len(genuine)):
	if genuine[i]:
		print(i, genuine[i])

for i in range(len(imposter)):
	if imposter[i]:
		print(i, imposter[i])		

for i in range(1, res+1):
	genuine[res-i] += genuine[res-i+1]
	imposter[i] += imposter[i-1]

for i in range(len(genuine)):
	genuine[i] /= gen
	imposter[i] /= imp

for i in range(len(genuine)):
	print(i/res, '\t', genuine[i]*100, '\t', imposter[i]*100)

final = []
for i in range(res+1):
	final.append(abs(genuine[i]-imposter[i]))

threshold = final.index(min(final))
errG = genuine[threshold]
errI = imposter[threshold]
diff = final[threshold]

print(threshold, errG, errI, diff)

