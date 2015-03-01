import sys

for line in open(sys.argv[1]):
	lastSpaceIndex = line.rfind(' ')
	m = int(line[lastSpaceIndex:])
	index = lastSpaceIndex + 1 - m * 2

	if index > -1:
		print(line[index])