import sys

ASCII_A = ord('a')

for line in open(sys.argv[1]):
	digits = ''

	for character in line.rstrip():
		if character >= 'a' and character <= 'j':
			digits += str(ord(character) - ASCII_A)
		elif character >= '0' and character <= '9':
			digits += character

	print(digits if digits else 'NONE')