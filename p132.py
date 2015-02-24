import sys

for line in open(sys.argv[1]):
	elements = line.rstrip().split(',')
	halfNumElements = len(elements) / 2
	checkedElements = []

	for element in elements:
		if element not in checkedElements and elements.count(element) > halfNumElements:
			print(element)
			break

		checkedElements.append(element)
	else:
		print('None')