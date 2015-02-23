import sys

for numbers in [map(float, line.rstrip().split(' ')) for line in open(sys.argv[1])]:
	numbers = list(numbers)
	numbers.sort()

	print(('{:.3f} ' * len(numbers)).format(*numbers)[:-1])