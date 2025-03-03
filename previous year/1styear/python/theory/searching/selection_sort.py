# def sort(lst):
# 	i = 0
# 	while i < len(lst):
# 		# j = i
# 		# m = lst[j]
# 		k = find_minimum(i,lst)
# 		# k = find_minimum(lst)
# 		lst[i], lst[k] = lst[k], lst[i]
# 		i += 1
# 	return lst

# def find_minimum(i,lst):
# 	j = i  # loop variable.
# 	t = 0  # Index Containing variable of minimum variable.
# 	k = lst[t]
# 	# minimum = lst[i]
# 	# k = lst[i]
# 	while j < len(lst):
# 	# while minimum < lst[j]:
# 		# t = 0
# 		# i += 1
# 		if k > lst[j]:
# 			k = lst[j]
# 			t = j
# 			# print(t,'h')
# 			# i += 1
# 		j += 1
# 		# i += 1
# 	# i += 1
# 	# print(i,'k')
# 	return t

# # print(minimum1([5,4,6,8,2]))
# print(sort([1,2,3,10]))
# # print(sorting([20,14,12,12,10]))



# 	# while lst[i - 1] > lst[i]:
# 			# lst[i - 1], lst[i] = lst[i], lst[i - 1]
# 			# i += 1
# 		# temp = lst[i]
# 		# print(k,lst[k - 1])
# 		# temp = lst[i]
# 		# lst[i] = lst[minimum1(lst[i:])]
# 		# lst[minimum1(lst[i:])] = temp
# 		# i += 1
# 		# lst[i - 1] = temp
# 		# i += 1
# 		# lst[i - 1], lst[i] = lst[i - k], lst[i - 1]
# 		# i += 1
# 		# print(lst, k)
# 		# lst[i - 1], lst[i] = lst[i], lst[i - 1]
# 		# if i == 0:
# 			# i += 1

# 		# else:
# 			# lst[i - 1], lst[i] = lst[i], lst[i - 1]
# 			# i += 1
swap_i = 0
comparision = 0
def selection_sort(lst):
	global swap_i
	i = 0
	l = len(lst)
	while i < l:
		# print(i)
		a = min_pos(lst, i)
		# print(a)
		temp = lst[i]
		lst[i] = lst[a]
		lst[a] = temp
		swap_i += 1
		i += 1
	return lst


def min_pos(lst, i):
	'''
	returns pos of min number in lst after ith position.
	'''
	global comparision
	result = lst[i]
	for x in range(i, len(lst)):
		# print(x, result)
		comparision += 1
		if lst[x] <= result:
			
			result = lst[x]
			pos = x
			
	return pos


print(min_pos([1,5,2,3,4,5,5,6], 5))


seq = [3,2,65,7,698,4,76,86,2,6,5,87,4,90,76,36,0,56,3,2,66,76,3,87,31,84,96,34,65,2,5,98,5,5,43,2,2,34,4,5,5,5,66,6,5,4,22,344,5,5,6,6,6]
b = selection_sort(seq)
# print(b)
print(comparision, swap_i)