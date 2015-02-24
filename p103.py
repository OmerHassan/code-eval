import sys

for line in open(sys.argv[1]):
	numbers = [int(i) for i in line.rstrip().split(' ')]
	countedNumbers = []
	lowestUniqueNumber = 10
	lowestUniqueNumberIndex = -1

	for (index, number) in enumerate(numbers):
		if number not in countedNumbers and number < lowestUniqueNumber:
			count = numbers.count(number)
			countedNumbers.append(number)

			if count == 1:
				lowestUniqueNumber = number
				lowestUniqueNumberIndex = index

	print(lowestUniqueNumberIndex + 1)