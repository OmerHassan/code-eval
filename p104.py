import sys

NUMBER_NAME_TO_VALUE_MAP = {
	'zero': '0',
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9'
}

def mapNumberNameToValue(numberName):
	return NUMBER_NAME_TO_VALUE_MAP[numberName]

for line in open(sys.argv[1]):
	names = line.rstrip().split(';')
	values = map(mapNumberNameToValue, names)

	print(''.join(values))