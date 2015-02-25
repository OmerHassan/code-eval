import sys

MONTH_NAME_TO_NUMBER_MAP = {
	'Jan': '01',
	'Feb': '02',
	'Mar': '03',
	'Apr': '04',
	'May': '05',
	'Jun': '06',
	'Jul': '07',
	'Aug': '08',
	'Sep': '09',
	'Oct': '10',
	'Nov': '11',
	'Dec': '12'
}

def dateDiff(date1String, date2String):
	'''
	Parameters
	----------
		date1String:str
			Date in format "YYYY-MM"
		date2String:str
			Date in format "YYYY-MM"

	Returns
	-------
		int
			The difference date1String - date2String in months
	'''
	date1 = parseDateString(date1String)
	date2 = parseDateString(date2String)

	return (date1[0] - date2[0]) * 12 + date1[1] - date2[1] + 1

def parseDateString(dateString):
	'''
	Parameters
	----------
		dateString:str
			Date in format "YYYY-MM"

	Returns
	-------
		list
			List containing two integers [year, month]
	'''
	return [int(x) for x in dateString.split('-')]

for line in open(sys.argv[1]):
	intervals = []

	for intervalString in line.rstrip().split('; '):
		boundaries = [boundary.split(' ') for boundary in intervalString.split('-')]
		startDateString = boundaries[0]
		endDateString = boundaries[1]
		intervals.append({
			'startDate': startDateString[1] + '-' + MONTH_NAME_TO_NUMBER_MAP[startDateString[0]],
			'endDate': endDateString[1] + '-' + MONTH_NAME_TO_NUMBER_MAP[endDateString[0]]
		})

	experience = 0
	skippedIntervalIndices = []
	i = 0
	numIntervals = len(intervals)

	while i < numIntervals:
		interval = intervals[i]
		overlapDetected = False

		# if this interval has already been included in other intervals, skip it
		if i not in skippedIntervalIndices:
			# if this interval overlaps with any other, include the other
			# interval in this one
			for j in range(i + 1, numIntervals):
				# don't check intervals[i] against itself or against skipped
				# intervals
				if j in skippedIntervalIndices:
					continue

				# if there's an overlap
				possiblyOverlappingInterval = intervals[j]

				if interval['endDate'] >= possiblyOverlappingInterval['startDate'] and possiblyOverlappingInterval['endDate'] >= interval['startDate']:
					# extend interval to include possiblyOverlappingInterval
					interval['startDate'] = min(interval['startDate'], possiblyOverlappingInterval['startDate'])
					interval['endDate'] = max(interval['endDate'], possiblyOverlappingInterval['endDate'])

					# skip the interval
					skippedIntervalIndices.append(j)

					# now that the interval has changed its size, we need to
					# check if its new size overlaps with any intervals
					overlapDetected = True

		# if this interval doesn't overlap with any other
		if not overlapDetected:
			# add this interval's length to total experience
			if i not in skippedIntervalIndices:
				experience += dateDiff(interval['endDate'], interval['startDate'])
			
			# check the next interval
			i += 1

	print(int(experience / 12))