def is_prime(x):
	for i in range(2, int(x ** (1/2))+1):
		if x % i == 0:.
			return False
	if x > 1:
		return True
def filt(lis):
	return list(filter(is_prime, lis))

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(filt(l))