import sys

for line in open(sys.argv[1]):
	maxLength = 0

	for word in line.rstrip().split(' '):
		wordLength = len(word)

		if wordLength > maxLength:
			maxLength = wordLength
			longestWord = word

	print(longestWord)