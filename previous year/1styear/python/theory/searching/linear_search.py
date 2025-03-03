def linear_search(v, b):
	j = len(b) - 1
	print(j)
	while j > -1 and b[j] != v:
		j -= 1
		print(j, '4')
	if j == -1:
		return -1
	return j

print(linear_search('a', 'sonaaaal'))

# def linear_search(v,b):
#  """Returns: first occurrence of v in b (-1 if not found)
# Precond: b a list of number, v a number
#  """
#  # Loop variable
# 	i = 0
# 	while i < len(b) and b[i] != v:
# 		i = i + 1
# 	if i == len(b): # not found
# 		return -1
# 	return i

# print(linear_search(5, [1,5,2,3,7,8,9,4,1,5]))