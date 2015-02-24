import sys

for line in open(sys.argv[1]):
	line = line.rstrip()
	lineLength = len(line)
	firstCharacter = line[0]
	firstCharacterRepetitionIndex = 0

	while True:
		firstCharacterRepetitionIndex = line.find(firstCharacter, firstCharacterRepetitionIndex + 1)

		if firstCharacterRepetitionIndex < 0:
			print(lineLength)
			break

		repetition = line[:firstCharacterRepetitionIndex]
		repetitionLength = len(repetition)

		if lineLength % repetitionLength == 0 and repetition * int(lineLength / repetitionLength) == line:
			print(repetitionLength)
			break