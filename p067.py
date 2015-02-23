import sys, string

for n in [x.rstrip() for x in open(sys.argv[1])]:
	decimal = 0

	for i in range(len(n)):
		decimal += string.hexdigits.find(n[-1 - i]) * 16 ** i

	print(decimal)