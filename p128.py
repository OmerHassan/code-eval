import sys

for line in open(sys.argv[1]):
	output = []

	for number in line.rstrip().split(' '):
		if not output or output[-1] != number:
			output.extend([1, number])
		else:
			output[-2] += 1

	print(' '.join(map(str, output)))