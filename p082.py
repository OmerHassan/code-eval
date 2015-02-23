import sys

for n in [line.rstrip() for line in open(sys.argv[1])]:
	digitSum = 0
	numDigits = len(n)

	for i in n:
		digitSum += int(i) ** numDigits

	print(str(digitSum) == n)