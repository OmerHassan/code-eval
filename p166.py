import sys

def formatSeconds(numberOfSeconds):
	'''
	Parameters
	----------
		numberOfSeconds:int

	Returns
	-------
		str
			String of the format HH:MM:SS
	'''
	hours = int(numberOfSeconds / 3600)
	minutes = int(numberOfSeconds / 60) % 60
	seconds = numberOfSeconds % 60

	return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

for line in open(sys.argv[1]):
	time1, time2 = [[int(x) for x in time.split(':')] for time in line.rstrip().split(' ')]
	seconds = (time1[0] - time2[0]) * 3600 + (time1[1] - time2[1]) * 60 + time1[2] - time2[2]

	print(formatSeconds(abs(seconds)))