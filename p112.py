import sys

for line in open(sys.argv[1]):
	colonIndex = line.find(':')
	numbers = line[:colonIndex - 1].split(' ')
	positions = line[colonIndex + 2:].rstrip().split(', ')

	for position in positions:
		dashIndex = position.find('-')
		p1 = int(position[:dashIndex])
		p2 = int(position[dashIndex + 1:])

		n1 = numbers[p1]
		numbers[p1] = numbers[p2]
		numbers[p2] = n1

	print(' '.join(numbers))