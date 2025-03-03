# # def binary_search(v, b):
# # 	y = 0
# # 	x = len(b) // 2
# # 	# guess = (x + y) // 2
# # 	if len(b) == 1:
# # 		return x 

	
# # 	elif v > b[x]: 
# # 		binary_search(v, b[x:len(b)]) 
# # 		# print(binary_search(v, b[x:len(b)]))

# # 	else:
# # 		binary_search(v, b[0:x])
# # 		# print(binary_search(v, b[0:x]))
# # print(binary_search(5, [1,2,3,4,5]))


# # lst = [1,2,3,4,5]
# # print(lst[2:5])
# # lst = lst[2:5]
# # print(lst)
# # lst = lst[1:3]
# # print(lst)


# # def binary_search(v, b):
# # 	x = len(b) // 2
# # 	if b[x] == v :
# # 		return v 

# # 	while b[x] > v : 



# def binary_search(v, b):
# 	x = 0
# 	y = len(b)
# 	guess = (x + y) // 2
# 	while v != b[guess] :
# 		if b[guess] < v:
# 			# print(guess)
# 			# print(b[guess])
# 			b = b[guess:len(b)]
# 			print(b, 'qwerty')
# 			guess = (b[guess] + len(b)) // 2
# 			# continue
# 			# print(b)
# 			# continue

# 		else:
# 			# print(b)
# 			b = b[0:guess]
# 			print(b, 'ytrewq')
# 			guess = (x[guess] + len(b)) // 2
# 			# continue

# 		if len(b) == 1:
# 			return guess

# 		return -1 

# print(binary_search(5, [1,2,3])) 


# # def binary_search(v, b):
# # 	x = 0
# # 	y = len(b)
# # 	guess = (0 + len(b)) // 2

# # 	if len(b) == 1 and v == guess:
# # 		return guess

# # 	if len(b) == 0:
# # 		return -1

# # 	if v == b[guess]:
# # 		return guess

# # 	elif v > b[guess]:
# # 		# guess += guess
# # 		return binary_search(v, b[guess: len(b)])

# # 	else:
# # 		# guess += guess
# # 		return binary_search(v, b[0:guess])

# # print(binary_search(5, [1,2,3,4,5]))






def binary_search(v, b):
	low = 0
	high = len(b)
	guess = (low + high) // 2

	if len(b) == 1:
		return guess

	if len(b) == 0:
		return -1

	if v == b[guess]:
		return guess

	elif v > b[guess]:
		# guess += guess
		low = len(b) // 2
		high = len(b)
		return binary_search(v, b[len(b)//2:len(b)])

	# guess += guess
	return binary_search(v, b[0:len(b)//2])

print(binary_search(0, [1,2,3,4,5,6,7,8]))




# def binary_search(v, b):
# 	x = 0
# 	y = len(b)
# 	mid = (x + y) // 2

# 	while x < y:
# 		if b[mid] < v:
# 			x = mid + 1

# 		else:
# 			y = mid

# 		mid = (x + y) // 2

# 		if x < len(b) and b[x] == v:
# 			return x

# print(binary_search(3, [0,1,2,3,4,5,6,7,8,9]))
