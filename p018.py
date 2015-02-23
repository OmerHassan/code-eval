import sys

for line in open(sys.argv[1]).read().splitlines():
	(x, n) = [int(x) for x in line.split(',')]

	multipleOfN = n

	while multipleOfN < x:
		multipleOfN += n

	print(multipleOfN)