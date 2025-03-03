def sum_fraction(n) :
	total = 0
	# for i in range(1, n + 1):
	# 	total += 1/i 

	# return total 
	i = 1
	while i <= n :
		total += 1/i
		i += 1
	return total

print(sum_fraction(1))