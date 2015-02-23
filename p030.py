import sys

for line in open(sys.argv[1]).read().splitlines():
	(set1, set2) = [set(map(int, x.split(','))) for x in line.split(';')]
	print(','.join(map(str, sorted(set1 & set2))))