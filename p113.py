import sys

for line in open(sys.argv[1]):
	numberGroups = [x.split(' ') for x in line.rstrip().split(' | ')]
	group0 = numberGroups[0]
	group1 = numberGroups[1]
	numElements = len(group0)
	products = []

	for i in range(numElements):
		group0[i] = str(int(group0[i]) * int(group1[i]))

	print(' '.join(group0))