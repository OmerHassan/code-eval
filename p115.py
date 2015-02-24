import sys

for line in open(sys.argv[1]):
	words = []
	numbers = []

	for string in line.rstrip().split(','):
		firstCharacter = string[0]

		if firstCharacter >= '0' and firstCharacter <= '9':
			numbers.append(string)
		else:
			words.append(string)

	print(','.join(words) + ('|' if words and numbers else '') + ','.join(numbers))