import sys

TOP_NODE_VALUE = '30'

node30 = {'value': TOP_NODE_VALUE, 'parent': None}
node8 = {'value': '8', 'parent': node30}
node52 = {'value': '52', 'parent': node30}
node3 = {'value': '3', 'parent': node8}
node20 = {'value': '20', 'parent': node8}
node10 = {'value': '10', 'parent': node20}
node29 = {'value': '29', 'parent': node20}

TREE = (
	(node30),
	(node8, node52),
	(node3, node20),
	(node10, node29)
)

NODE_VALUE_TO_LEVEL_MAP = {
	TOP_NODE_VALUE: 0,
	'8': 1,
	'52': 1,
	'3': 2,
	'20': 2,
	'10': 3,
	'29': 3
}

del node30, node8, node52, node3, node20, node10, node29

for line in open(sys.argv[1]):
	node1Value, node2Value = line.split()
	level1, level2 = NODE_VALUE_TO_LEVEL_MAP[node1Value], NODE_VALUE_TO_LEVEL_MAP[node2Value]

	if node1Value == TOP_NODE_VALUE or node2Value == TOP_NODE_VALUE:
		print(TOP_NODE_VALUE)
		continue

	if level1 == level2:
		node1IndexInLevel = 0
	else:
		# make sure node1 is at a higher level than node2
		if level1 > level2:
			node1Value, node2Value = node2Value, node1Value
			level1, level2 = level2, level1

		node1IndexInLevel = 0 if TREE[level1][0]['value'] == node1Value else 1

	print(TREE[level1][node1IndexInLevel]['parent']['value'])