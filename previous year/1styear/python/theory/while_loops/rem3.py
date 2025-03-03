def rem3(lst):
	# for i in lst :
	# 	if i == 3 :
	i = 0
	while i < len(lst) :
		if lst[i] == 3 :
			lst.remove(lst[i])
			i = 0
		else: 
			i += 1

	print(lst)

rem3([3, 3, 3,5])  