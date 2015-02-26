import sys

for line in open(sys.argv[1]):
	# find the shortest distance between the right-most X and the left-most Y
	shortestDistance = -1

	for row in line.split(','):
		distance = row.find('Y') - row.rfind('X') - 1

		if shortestDistance == -1 or distance < shortestDistance:
			shortestDistance = distance

		if shortestDistance == 0:
			break

	print(shortestDistance)