def linear_search(v, b):
	i = len(b) - 1
	# b = b[::-1]
	while i < len(b) and b[i] != v :
		i = i - 1

	# if i == len(b):
		# return -1
	return i

	# for i in range(len(b)) :
	# 	if v == b[i]:
	# 		return i 

	
	# return -1

print(linear_search(5, [1,2,3,4,5,6, '4']))