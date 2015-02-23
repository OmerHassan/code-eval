import sys

def sumDigitSquares(n):
	reducedN = n
	squareSum = 0

	while reducedN > 0:
		squareSum += (reducedN % 10) ** 2
		reducedN = int(reducedN / 10)

	return squareSum

for n in map(int, open(sys.argv[1]).read().splitlines()):
	lastSum = n

	for i in range(50):
		lastSum = sumDigitSquares(lastSum)

		if lastSum == 1:
			print(1)
			break
	else:
		print(0)