import sys

print(sum([int(x) for x in open(sys.argv[1]).read().splitlines()]))