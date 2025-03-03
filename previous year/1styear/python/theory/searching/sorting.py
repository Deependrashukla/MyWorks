comparision = 0
swap_i = 0
def sorting(lst):
	i = 1
	# global k
	j = len(lst)
	while i < j:
		# k += 1
		# print(i)
		push_down(i, lst)
		# print(f'output {i}')
		i += 1
	return lst

def push_down(i, lst):
	j = i
	global comparision, swap_i
	while j > 0 and lst[j-1] > lst[j]:
		# print(f'inner {j}')
		# print(k)
		# k += 1
		# i += 1
		# # if lst[i-1] > lst[i]:
		# if lst[j-1] > lst[j]:
		# 	k += 1
		comparision += 1
		lst[j - 1], lst[j] = lst[j], lst[j - 1]
		swap_i += 1	
		j -= 1

		# else:
			# lst[i - 1], lst[i] = lst[i - 1], lst[i]
			# j -= 1
			# break

# # # k = 0
print(sorting([3,2,65,7,698,4,76,86,2,6,5,87,4,90,76,36,0,56,3,2,66,76,3,87,31,84,96,34,65,2,5,98,5,5,43,2,2,34,4,5,5,5,66,6,5,4,22,344,5,5,6,6,6]))
print(comparision)

# 306
# 674
# # # # print(k)
# # # # k = 0
# # # # print(sorting([2,1,5,4,8]))
# # # # print(k)
# # # # k = 0
# # # # print(sorting([2,1,3,4,6,8]))
# # # # print(k)
# # # # k =0
# # # # print(sorting([2,1,3,4,8]))
# # # # print(k)
# # # # k = 0
# # # # print(sorting([26,5,8,4]))
# # # # print(k)
# # # # k = 0
# # # # print(sorting([2,1,4,8]))
# # # # print(k)
# comparision = 0
# def sorting(lst):
# 	i = 0
# 	while i < len(lst):
# 		j = find_place(lst[i], lst)
# 		temp = lst[i]
# 		push(i, lst)
# 		lst[j] = temp
# 		i += 1
# 	return lst

# def find_place(x, lst):
# 	for i in range(len(lst)):
# 		if lst[i] < x :
# 			continue

# 		else:
# 			return i 

# def push(i, lst):
# 	k = 0
# 	while k != i :
# 		print(lst[i], lst[i - 1])
# 		lst[i] = lst[i - 1]
# 		k += 1

# print(sorting([2,-1,5,4,30,90]))

# def inser_sort(lst):
# 	for i in range(len(lst)):
# 		temp = lst[i]

# 		while (i - 1) > 0 and temp < 