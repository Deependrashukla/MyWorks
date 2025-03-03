lst = [1, 2, 3]
def add_one(lst):
	for x in lst:
		x += 1
print(id(lst))
add_one(lst)
print(id(lst))