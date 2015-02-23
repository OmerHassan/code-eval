import sys

for line in open(sys.argv[1]):
	if not line.strip():
		continue

	separatorIndex = line.find('|')
	characters = line[:separatorIndex]
	numbers = line[separatorIndex + 1:].strip().split(' ')
	name = ''
	
	for number in numbers:
		name += characters[int(number) - 1]

	print(name)