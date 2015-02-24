import sys, json

for line in open(sys.argv[1]):
	if not line.strip():
		continue

	idSum = 0

	for item in json.loads(line)['menu']['items']:
		if item and 'label' in item and 'id' in item:
			idSum += item['id']

	print(idSum)