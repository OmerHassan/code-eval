import sys

for line in open(sys.argv[1]).read().splitlines():
	(string, substring) = line.rsplit(',', 1)
	print(string.rfind(substring))