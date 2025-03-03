def insertion(b):
	i = 0
	j = len(b)
	while i < j:
		push_down(i, b)

		i += 1


def push_down(i, b):

	while i > 0:
		if b[i] < b[i - 1]:
			b[i - 1], b[i] = b[i], b[i - 1]

		else:
			break

		i -= 1

lst = [1,2,3,4,5,6,7,8,9]
print(insertion(lst))
print(lst)