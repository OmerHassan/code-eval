import sys

for line in open(sys.argv[1]).read().splitlines():
	n = int(line)
	reducedN = n
	digitSum = 0

	while reducedN > 0:
		digitSum += reducedN % 10
		reducedN = int(reducedN / 10)

	print(digitSum)