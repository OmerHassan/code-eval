import sys

for line in open(sys.argv[1]):
	number = float(line.rstrip())
	integer = int(number)
	minutes = (number - integer) * 60
	seconds = (minutes - int(minutes)) * 60

	print('{:d}.{:02d}\'{:02d}"'.format(integer, int(minutes), int(seconds)))