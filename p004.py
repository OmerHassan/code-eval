def isPrime(n):
	for i in range(2, int(n / 2) + 1):
		if n % i == 0:
			return False

	return True

n = 0
sumN = 0
i = 2

while (n < 1000):
	if isPrime(i):
		n += 1
		sumN += i

	i += 1 if i == 2 else 2

print(sumN)