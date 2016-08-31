import operator

d = dict()
total = 0

with open('a1.cipher', 'r') as file:
	content = file.read()
	for char in content: 
		if char == ' ' or char == '\n':
			continue;
		elif char in d:
			d[char] += 1
		else:
			d[char] = 1
		total += 1

for key, item, in d.items():
	d[key] = 100 * float(item)/float(total)

sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

with open('sampleFrequencies.dat', 'w') as file:
	for k, i in sorted_d:
		file.write(k + " " + "{0:.2f}".format(i) + "\n")
