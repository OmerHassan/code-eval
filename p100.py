import sys

for line in open(sys.argv[1]):
	print(1 if int(line.rstrip()) % 2 == 0 else 0)