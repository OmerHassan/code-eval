import sys

'''
for each line
	if this line has a checkpoint && |checkpointIndex - previousLineMarkIndex| <= 1
		mark it
	else
		mark gate
'''

CHECKPOINT = 'C'
GATE = '_'
WAYPOINT_CHARACTERS = ['/', '|', '\\']

lastWaypointIndex = -1

for line in open(sys.argv[1]):
	line = line.rstrip()
	checkpointIndex = line.find(CHECKPOINT)

	if checkpointIndex > -1 and (lastWaypointIndex == -1 or abs(checkpointIndex - lastWaypointIndex) <= 1):
		waypointIndex = checkpointIndex
	else:
		waypointIndex = line.find(GATE)

	waypointIndexDifference = waypointIndex - lastWaypointIndex

	if lastWaypointIndex == -1 or waypointIndexDifference == 0:
		waypointCharacter = WAYPOINT_CHARACTERS[1]
	elif waypointIndexDifference < 0:
		waypointCharacter = WAYPOINT_CHARACTERS[0]
	else:
		waypointCharacter = WAYPOINT_CHARACTERS[2]

	print(line[:waypointIndex] + waypointCharacter + line[waypointIndex + 1:])

	lastWaypointIndex = waypointIndex