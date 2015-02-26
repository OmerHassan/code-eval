import sys

for line in open(sys.argv[1]):
	line = line.rstrip()

	if len(line) <= 55:
		print(line)
	else:
		lastSpaceIndex = line.rfind(' ', 0, 40)
		print(line[:lastSpaceIndex if lastSpaceIndex > -1 else 40].rstrip() + '... <Read More>')