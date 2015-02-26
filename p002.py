import sys

inputFile = open(sys.argv[1])
numRequiredLines = int(inputFile.readline())
lengthLinePairs = []

while True:
	line = inputFile.readline().rstrip()

	if not line:
		break

	lengthLinePairs.append((len(line), line))

i = 0
lengthLinePairs = sorted(lengthLinePairs, reverse = True)

for i in range(numRequiredLines):
	print(lengthLinePairs[i][1])