import sys

FONT = [
	'-**----*--***--***---*---****--**--****--**---**--',
	'*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-',
	'*--*---*---**---**--****-***--***----*---**---***-',
	'*--*---*--*-------*----*----*-*--*--*---*--*----*-',
	'-**---***-****-***-----*-***---**---*----**---**--',
	'--------------------------------------------------'
]
WIDTH = 5
HEIGHT = 6

for line in open(sys.argv[1]):
	outputLines = [''] * HEIGHT

	for character in line.rstrip():
		if character.isdecimal():
			integer = int(character)
			firstCharacterIndex = integer * WIDTH

			for i in range(HEIGHT):
				outputLines[i] += FONT[i][firstCharacterIndex:firstCharacterIndex + WIDTH]

	print('\n'.join(outputLines))