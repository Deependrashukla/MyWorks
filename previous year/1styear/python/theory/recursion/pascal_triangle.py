lst = [1]
def pascal_triangle(n) :
	if n == 1 :
		return [1]

	for i in range(1,n) :
		lst1 = lst + [i]
		lst.append(lst1)

pascal_triangle(3)
print(lst)

