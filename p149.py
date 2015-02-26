import sys

for line in open(sys.argv[1]):
	lineParts = line.rstrip().split(' ')
	binaryNumber = ''

	for i in range(0, len(lineParts) - 1, 2):
		if lineParts[i] == '0':
			binaryNumber += lineParts[i + 1]
		else:
			binaryNumber += '1' * len(lineParts[i + 1])

	print(int(binaryNumber, 2))