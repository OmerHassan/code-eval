import sys

class Stack:
	def __init__(self):
		self.elements = []

	def push(self, element):
		self.elements.append(element)

	def pop(self):
		return self.elements.pop()

	def size(self):
		return len(self.elements)

for line in open(sys.argv[1]):
	stack = Stack()

	for element in line.split():
		stack.push(element)

	printNext = True
	output = []

	for i in range(stack.size() - 1, -1, -1):
		poppedElement = stack.pop()

		if printNext:
			output.append(poppedElement)

		printNext = not printNext

	print(' '.join(output))