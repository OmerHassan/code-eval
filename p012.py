import sys

def printFirstNonRepeatingCharacter(string):
	checkedCharacters = {}

	for characterIndex in range(len(string)):
		character = string[characterIndex]

		if character in checkedCharacters:
			continue

		if string.find(character, characterIndex + 1) < 0:
			print(character)
			return

		checkedCharacters[character] = None

for line in open(sys.argv[1]):
	printFirstNonRepeatingCharacter(line)