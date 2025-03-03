def list_squares(n):
	lst = []
	for i in range(int(n ** 0.5) + 1):
		print(i)
		if i < n :
			lst.append(i*i)

		# else :
			# return lst 

	return lst
	i = 0
	while i*i < n :
		lst.append(i*i)
		i += 1

	return lst



print(list_squares(0))