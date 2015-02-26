import sys

for line in open(sys.argv[1]):
	output = ''
	lastCharacter = None

	for character in line.rstrip():
		if character != lastCharacter:
			output += character

		lastCharacter = character

	print(output)