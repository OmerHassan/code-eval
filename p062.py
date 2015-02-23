import sys

for (n, m) in [map(int, line.split(',')) for line in open(sys.argv[1]).read().splitlines()]:
	print(n - int(n / m) * m)