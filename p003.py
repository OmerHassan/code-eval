def isPrime(n):
	for i in range(2, int(n / 2) + 1):
		if n % i == 0:
			return False

	return True

def isPalindrome(string):
	for i in range(int(len(string) / 2)):
		if string[i] != string[-1 - i]:
			return False

	return True

for i in range(997, 3, -2):
	if isPrime(i) and isPalindrome(str(i)):
		print(i)
		break