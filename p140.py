import sys

for line in open(sys.argv[1]):
	words, targetPositions = [part.split(' ') for part in line.rstrip().rsplit(';', 1)]
	orderedWords = [None] * len(words)

	for i, targetPosition in enumerate(targetPositions):
		orderedWords[int(targetPosition) - 1] = words[i]

	orderedWords[orderedWords.index(None)] = words[-1]

	print(' '.join(orderedWords))