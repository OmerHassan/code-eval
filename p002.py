import sys

inputFile = open(sys.argv[1])
numRequiredLines = int(inputFile.readline())
lines = []
lengthIndexPairs = []
i = 0

while True:
	line = inputFile.readline().rstrip()

	if not line:
		break

	lines.append(line)
	lengthIndexPairs.append((len(line), i))
	i += 1

for lengthIndexPair in sorted(lengthIndexPairs, reverse = True)[:numRequiredLines]:
	print(lines[lengthIndexPair[1]])