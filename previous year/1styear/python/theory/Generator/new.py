# def range2(n):
# 	for x in range(n):
# 		yield x * x

# print(list(range2(3)))
# def stepup(n):
# 	while n < 10:
# 		n += 1
# 		yield n
# for num in stepup(5):
# 	print(num, end=" ")
my_list = [11, 22, 33, 44, 55]
my_iter = iter(my_list)
print(next(my_iter))
for i in my_iter:
	if i%2 != 0:
		print(i, end=" ")