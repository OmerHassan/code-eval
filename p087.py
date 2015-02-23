import sys

def query(lineIndex, numElements, statements, isColumn):
	'''
	Algorithm:
		Disregard any SetCol statements which don't affect column at
		`lineIndex`.
		This leaves us with at most one SetCol statement and any number of
		SetRow statements.
		Also disregard any SetRow statements that occur before SetCol.

		columnSum = (numElements - len(setRowStatementsFollowingSetCol)) *
			columnValue + sum(setRowStatementsFollowingSetCol)

	Parameters
	----------
	lineIndex:int
		Index of line (row or column) whose sum is required
	numElements:int
		Number of elements in the line (row or column)
	statements:list
		Preceding SetCol and SetRow statements. Each element of the list is a
		list with three elements [command, index, value] where `command` can be
		either "SetRow" or "SetCol".
	isColumn:boolean
		Whether to sum column values

	Returns
	-------
	int
		Sum of all elements in column at index `lineIndex`
	'''
	PARALLEL_COMMAND = 'SetCol' if isColumn else 'SetRow'
	PERPENDICULAR_COMMAND = 'SetRow' if isColumn else 'SetCol'

	# index of SetCol statement. Only the SetRow statements occurring after this
	# index take effect
	setColIndex = -1
	columnValue = 0

	for (index, statement) in enumerate(statements):
		if statement[0] == PARALLEL_COMMAND and statement[1] == lineIndex:
			columnValue = statement[2]
			setColIndex = index

	rowIndexToValueMap = {}

	for (index, statement) in enumerate(statements):
		if index > setColIndex and statement[0] == PERPENDICULAR_COMMAND:
			rowIndexToValueMap[str(statement[1])] = statement[2]

	setRowStatementValues = rowIndexToValueMap.values()

	return (numElements - len(setRowStatementValues)) * columnValue + sum(setRowStatementValues)

SIZE = 256
statements = []

for (command, *args) in [line.rstrip().split(' ') for line in open(sys.argv[1])]:
	args = [int(arg) for arg in args]

	if command == 'SetCol' or command == 'SetRow':
		statements.append([command] + args)
	else:
		print(query(args[0], SIZE, statements, command == 'QueryCol'))