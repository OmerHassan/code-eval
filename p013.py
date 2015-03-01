import sys, re

for line in open(sys.argv[1]):
	string, pattern = line.rstrip().split(', ')
	pattern = re.compile('[' + pattern + ']')
	print(pattern.sub('', string))