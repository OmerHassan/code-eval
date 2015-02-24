import sys, re, math

pattern = re.compile('\((-?\d+), (-?\d+)\)')

for line in open(sys.argv[1]):
	matches = re.findall(pattern, line)
	x1, y1, x2, y2 = int(matches[0][0]), int(matches[0][1]), int(matches[1][0]), int(matches[1][1])
	print(int(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)))