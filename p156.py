import sys

for line in open(sys.argv[1]):
	characters = list(line.rstrip())
	wasLastUpper = False

	for i, character in enumerate(characters):
		if character.isalpha():
			characters[i] = character.lower() if wasLastUpper else character.upper()
			wasLastUpper = not wasLastUpper

	print(''.join(characters))