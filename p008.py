import sys

for line in open(sys.argv[1]).read().splitlines():
	words = line.split(' ')
	words.reverse()
	print(' '.join(words))