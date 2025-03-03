lst = [1, 2, [1, 2], [4, 5, 6], [7, 8, 9], 10]
# for i in lst :
# 	print(i)


# for i in range(len(lst[0])) :
# 	for j in lst :
# 		print(j[i] ,j[i+1], j[i+2])

# for i in lst :
# 	for j in i :
# 		print(j)

# for i in range(len(lst[0])):
# 	for j in lst :
# 		print(j[i])

# for i in range(len(lst)) :
# 	for j in range(len(lst[i])) :
# 		print(lst[j][i])

# for i in range(len(lst[0])) :
# 	for j in range(len(lst)) :
# 		print(lst[j][i])
l = []

for i in lst :

	if type(i) == list :
		for j in range(len(i)):
			l.append(i[j])

	else:
		for j in range(len(lst)):
			l.append(i)
			break
print(l)