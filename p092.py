import sys

for line in open(sys.argv[1]):
	words = line.rstrip().split(' ')
	print(words[-2])