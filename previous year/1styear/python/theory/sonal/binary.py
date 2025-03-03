def binary_search(v, b):
	i = 0
	j = len(b)
	guess = (i + j) // 2

	while b[guess] != v :
		print(b[guess],i,j)
		if b[guess] > v:
			j = guess

		else:
			i = guess + 1


		if i == len(b) or j <= 0:
			return -1

		guess = (i + j) // 2


	return guess


print(binary_search(0, [1,2,3,4,5,6]))