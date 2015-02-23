import sys

for line in open(sys.argv[1]).read().splitlines():
	(n, p1, p2) = [int(x) for x in line.split(',')]
	(b1, b2) = [(n >> (p - 1)) & 1 for p in (p1, p2)]
	print('true' if b1 == b2 else 'false')