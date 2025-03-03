# a=[x*x  for x in range(5) if x*x>3]
# print(a)
lst = [1,2,3,4,5]
#print([x+1 for x in lst])
def add_one(lst):
	for i in lst:
		yield i+1

# a=add_one(lst)
# print(next(a))
# print(list(lst))


# def even(lst):
# 	for i in lst:
# 		if i%2==0:
# 			yield i
# a=even(lst)
# print(next(a))
# print(next(a))
# print(next(a))
# a=[i for i in lst if i %2==0]
# print(a)
def average(lst):
	num=1
	sum_=0
	for i in lst:
		sum_=sum_+i
		yield sum_/num
		num=num+1
a=average(lst)
print(next(a))
print(next(a))
print(next(a))

sum_=0
num=1
a=[sum_/num for i in lst]

lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def transpose(lst):
	result=[]
	num_rows=len(lst)
	for i in range(len(lst[1])):
		res=[]
		for j in range(num_rows):
			res.append(lst[j][i])
		result.append(res)
	return result
print(transpose(lst))

