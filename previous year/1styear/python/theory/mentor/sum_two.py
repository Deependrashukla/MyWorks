lst = [1, 2, 3, 5, 5]

def sum_two(lst, target):

	for i in lst :

		if (target - i) in lst :

			return i, target - i

	return 'kuch daal bhai'

print(sum_two(lst, 10))

