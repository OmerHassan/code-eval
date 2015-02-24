import sys

for line in open(sys.argv[1]):
	distances = [int(segment.split(',')[1]) for segment in line.rstrip()[:-1].split('; ')]
	distances.sort()
	distanceDifferences = []

	for index, distance in enumerate(distances):
		distanceDifferences.append(str(distance if index == 0 else distance - distances[index - 1]))

	print(','.join(distanceDifferences))