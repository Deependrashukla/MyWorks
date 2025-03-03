lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
def dic_return(lst) :
	d = {}
	for i in lst:
		d[i[0]] = []
	return d 

# print(dic_return(lst))

def dic(d):
	# d = {'yellow' : [] , 'blue' : [], 'red' : []}
	# lst1=[]
	# d = {}
	for i in lst:
		# lst1.append(i[1])
		# d[i[0]] = [i[1]]

		# if i[0] == 'yellow' :
		# 	d['yellow'].append(i[1])

		# elif i[0] == 'blue' :
		# 	d['blue'].append(i[1])

		# elif i[0] == 'red' :
		# 	d['red'].append(i[1])

		for j in d:
			(d[j].append(i[1]))
			


	return d 
print(dic(dic_return(lst)))