import sys

output = ''

for line in open(sys.argv[1]).read().splitlines():
	(x, y, n) = [int(x) for x in line.split(' ')]
	outputLine = ''

	for i in range(1, n + 1):
		isMultipleOfX = i % x == 0
		isMultipleOfY = i % y == 0

		if isMultipleOfX and isMultipleOfY:
			outputLine += 'FB '
		elif isMultipleOfX:
			outputLine += 'F '
		elif isMultipleOfY:
			outputLine += 'B '
		else:
			outputLine += str(i) + ' '

	output += outputLine[:-1] + '\n'

print(output[:-1])