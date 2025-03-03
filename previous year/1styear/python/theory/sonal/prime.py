def is_prime(n):
	x = True
	for i in range(1, n):
		# print(i)
		if i % n != 0:
			return True

	return False


def prime_number(n):
	x = []
	for i in range(2, n):
		if is_prime(i):
			x.append(i)

	return x


print(prime_number(5))