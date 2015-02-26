import sys, string

DISPLACEMENT_PERMUTATIONS = (
	(-1, -2),
	(1, -2),
	(-2, -1),
	(2, -1),
	(-2, 1),
	(2, 1),
	(-1, 2),
	(1, 2)
)

def getPGNPosition(row, col):
	return string.ascii_lowercase[col] + str(row + 1)

for line in open(sys.argv[1]):
	row = int(line[1]) - 1
	col = string.ascii_lowercase.find(line[0])
	output = ''

	for displacement in DISPLACEMENT_PERMUTATIONS:
		targetRow = row + displacement[0]
		targetCol = col + displacement[1]
		
		if 0 <= targetRow <= 7 and 0 <= targetCol <= 7:
			output += getPGNPosition(targetRow, targetCol) + ' '

	print(output.rstrip())