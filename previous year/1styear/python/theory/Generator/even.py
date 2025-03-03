# # # def even(input):
# # # 	for i in input:
# # # 		if i % 2 == 0:
# # # 			yield i 

# # # print(even([1, 2, 3, 4]))


# def avgRun(input):
# 	sum1 = 0
# 	count = 0
# 	for i in input:
# 		sum1 += i
# 		count += 1
# 		yield sum1 / count

# # x = avgRun([1, 2, 3, 4])
# # print(list(x))

# def map(f, data):
# 	for item in data:
# 		yield f(item)

# a = (map(avgRun, [1, 2, 3, 4]))
# # print(next(a))
# # print(list(a))



# def isEven(x):
# 	return x % 2 == 0

# def isPos(x):
# 	return x > 0

# def filter(f, data):
# 	for i in data:
# 		if f(i) :
# 			yield i 

# x = (filter(isEven, [1,2,3,4]))
# # print(next(x))
# # print(next(x))
# # print(next(x))
# print(list(x))


x = 0 
lst = [1,2,4,5]
# lst.sort()
for i in data:
	if not 1 in data:
		print(1)
		break

	elif i + 1 in data:
		