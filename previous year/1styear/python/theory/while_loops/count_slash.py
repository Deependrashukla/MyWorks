def count_slash(s) :

	total = 0
	# for i in s :
	# 	if i == '/' :
	# 		total += 1

	# return total

	# for i in range(len(s)) :
	# 	if s[i] == '/' :
	# 		total += 1

	# return total

	i = 0
	while  i < len(s) :
		if s[i] == '/' :
			total += 1

		i += 1
	return total

print(count_slash('///a/'))
