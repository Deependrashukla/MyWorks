lst = [1, 2, [1, 2], [4, 5, [1, 2], 6], [7, [5, 5, 5], 8, 9], 10]

l = []
def flatern(lst):
	"""
	Return :Flatten a list of lists.

	Parameter lst :It is a list.
	Precondition :It must be a list. 
	"""
	for i in lst :

		if type(i) == list :
			# for j in range(len(i)):
				# l.append(i[j])
			flatern(i)

		#Base Case
		else:
			# for j in range(len(lst)):
			l.append(i)
				# break

				
flatern(lst)
print(l)




# s = 0
# k = []
# def flatern_recursion(lst) :
# 	global s

# 	if type(s) == int :
# 		k.append(lst[s])
# 		s += 1
# 	elif type(lst[s]) == list :
		
# 		k.append(s[s])
# 		s += 1
# 		flatern_recursion(lst[s])
# 	else:
		
# 		k.append(lst[s])
# 		s += 1
# 		flatern_recursion(lst)

# 	# s += 1

# flatern_recursion(lst)
# print(k)
# print()




# k = []
# def flatern(lst):
# 	for i in lst :

# 		if type(i) == list :
# 			for j in range(len(i)):
# 				l.append(i[j])
# 				flatern(i)

# 		else:
# 			# for j in range(len(lst)):
# 			k.append(i)

# 				# break