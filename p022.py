import sys

def fibonacci(n):
	if n <= 1:
		return n

	return fibonacci(n - 1) + fibonacci(n - 2)

for line in open(sys.argv[1]).read().splitlines():
	print(fibonacci(int(line)))