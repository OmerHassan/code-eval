import sys

def printRepetition(elements):
	numElements = len(elements)
	
	if numElements == 1:
		print(elements[0])
		return

	for repetitionLength in range(1, int(numElements / 2) + 1):
		for repetitionStartIndex in range(numElements - 2 * repetitionLength + 1):
			secondOccurrenceStartIndex = repetitionStartIndex + repetitionLength
			if elements[repetitionStartIndex:secondOccurrenceStartIndex] == elements[secondOccurrenceStartIndex:secondOccurrenceStartIndex + repetitionLength]:
				print(' '.join(elements[repetitionStartIndex:repetitionStartIndex + repetitionLength]))
				return

for line in open(sys.argv[1]):
	printRepetition(line.split())