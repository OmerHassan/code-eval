import sys

POSITION_TO_ROMAN_DIGITS_MAP = [
	['I', 'V', 'X'],
	['X', 'L', 'C'],
	['C', 'D', 'M'],
	['M']
]

DIGIT_TO_ROMAN_DIGIT_INDICES_MAP = {
	'1': [0],
	'2': [0, 0],
	'3': [0, 0, 0],
	'4': [0, 1],
	'5': [1],
	'6': [1, 0],
	'7': [1, 0, 0],
	'8': [1, 0, 0, 0],
	'9': [0, 2]
}

def toRoman(n):
	romanNumber = ''
	numDigits = len(n)

	for index, digit in enumerate(n):
		if digit != '0':
			romanNumber += getRomanDigit(digit, numDigits - index - 1)

	return romanNumber

def getRomanDigit(digit, position):
	'''
	Returns Roman number equivalent to `digit` at `position`.

	Parameters
	----------
		digit:int
		position:int
			`0` for units, `1` for tens, `2` for hundreds, and so on

	Returns
	-------
		str
	'''
	romanDigitsAtPosition = POSITION_TO_ROMAN_DIGITS_MAP[position]
	romanDigitIndices = DIGIT_TO_ROMAN_DIGIT_INDICES_MAP[digit]
	romanDigit = ''

	for index in romanDigitIndices:
		romanDigit += romanDigitsAtPosition[index]

	return romanDigit

for line in open(sys.argv[1]):
	print(toRoman(line.rstrip()))