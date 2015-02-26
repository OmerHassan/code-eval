import sys

for line in open(sys.argv[1]):
	numLower = 0
	numUpper = 0

	for character in line:
		if character.islower():
			numLower += 1
		elif character.isupper():
			numUpper += 1

	percentLower = numLower / (numLower + numUpper) * 100
	percentUpper = 100 - percentLower

	print('lowercase: {:.2f} uppercase: {:.2f}'.format(percentLower, percentUpper))