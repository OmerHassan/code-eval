import sys, math

for line in open(sys.argv[1]):
	original = line.rstrip().replace(' ', '')
	nSquared = len(original)
	n = int(math.sqrt(nSquared))
	output = ''

	for i in range(nSquared):
		index = n * (n - 1 - i % n) + int(i / n)
		output += original[index] + ' '

	print(output.rstrip())