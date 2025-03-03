# # def itrator(n):
	
# # 	for i in range(n):
# # 		yield i**3

# # a=itrator(5)
# # print(list(a))
# # print(next(a))
# table = [[1,2],[3,4],[5,6]]
# x = [[i for i in j] for j in table]
# print(x)
# grade = {'1':5, '2':10}
# # d = {i : grade[i] / 2 for i in grade}
# # print(d)
# student=['1']
# d = {i :( grade[i] + 10 if i in student else grade[i]) for i in grade}
# print(d)

# for i in range(1,5,0.8):
# 	print(i)


a = (iter([1,23,3,4,5,5]))
# print(id(a))
# b= iter(a)
# print(id(b))
# print(list(b),list(a))
# for i in a:
# 	print(i*2)
# print(next(a))

# a="SON"
# b=iter (a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



# def poer(w):
# 	for i in range(w):
# 		yield i ** (1/5)
# 		print("uuuuu")
# 	return (77)

	
# a = poer(5)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


def add_one(n):
	c =[]
	for i in n:
		c.append(i+1)
	return c	
		
a= add_one([1,2,3,4])
#print(a)

def even(lst):
	#c=[]
	for i in lst:
		if i%2==0:
			yield (i)
	
# a=(even([1,2,3,4,45,6]))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def average(lst):
	pos=1
	result=0
	#c=[]
	for i in lst:
		result=result+i
		yield (result/pos)
		pos=pos+1
	
# a=(average([1,2,3,4]))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def map(f, data):
	# c = []
	# for i in data:
	# 	c.append(f(data))
	return f(data)
def odd(lst):
	c=[]
	for i in lst:
		if i%2 != 0:
			lst=lst
			c.append(i)
	return c 
#print(map(odd,[1,2,3,4]))

def filter(f,data):
	c=[]
	for i in data:
		if f(i):
			c.append(i)
	return c
def iseven(i):
	if i%2==0:
		return True
	return False
def add1(data):
	return [x**2  if x %2 != 0 else x  for x in data]
#print(add1([1,2,3,4]))


def transpose(lst):
	c=[]
	for i in lst:
		cum=[]
		for j in range(len(i)):
			cum.append(i[i][j])
			
	return c
print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
			



