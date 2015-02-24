import sys

for line in open(sys.argv[1]):
	spaceIndex = line.find(' ')
	number = line[:spaceIndex]
	operatorIndex = line.find('+')
	operatorIndex = operatorIndex if operatorIndex > -1 else line.find('-')
	numDigitsInOperand1 = len(line[spaceIndex + 1:operatorIndex])
	operand1 = int(number[:numDigitsInOperand1])
	operand2 = int(number[numDigitsInOperand1:])
	operator = line[operatorIndex]

	if operator == '+':
		print(operand1 + operand2)
	else:
		print(operand1 - operand2)