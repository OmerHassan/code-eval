import sys

for line in open(sys.argv[1]):
	words = [word[0].upper() + word[1:] for word in line.rstrip().split(' ')]
	print(' '.join(words))