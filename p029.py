import sys

for line in open(sys.argv[1]).read().splitlines():
	elements = line.split(',')
	uniques = []

	for element in elements:
		if element not in uniques:
			uniques.append(element)

	print(','.join(uniques))