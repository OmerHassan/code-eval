import sys

for n in open(sys.argv[1]).read().splitlines():
	for i in range(len(n)):
		if int(n[i]) != n.count(str(i)):
			print(0)
			break
	else:
		print(1)