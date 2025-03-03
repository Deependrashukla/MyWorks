# # x=[1,2,3]
# # print(id(x))
# # x.count(2)
# # print(id(x))
# # x.append(4)
# # print(id(x))
# # x.insert(0,0)
# # print(id(x))
# # x+[5]
# # print(id(x))
# # word=input('enter : ')
# # def print_each(text):
# # 	'''
# # 	Prints each char of text 
# # 	'''
# # 	for x in text:
# # 		print(x)
# # 		# return x
# # 	# print(x)
# # print_each(word)
# # lst=[0,1,2,3]
# # lst=[]
# # ls=int(input('Enter'))
# # lst.append(ls)
# # print(lst)
# # def sum(lst):
# # 	"""
# # 	Returns:the sum of all elements in lst.

# # 	Parameter lst:
# # 	"""
# # 	x=0
# # 	for i in lst:
# # 		x+=i
# # 	return x
# # print(sum(lst))


# # lst=[5, 4, 6, 2.0, 0, 'k']
# # def num_ints(lst):
# # 	"""
# # 	Return the number of ints in lst.

# # 	Parameter lst:Given list
# # 	Precondition:lst is a list of any mix types
# # 	"""
# # 	count=0
# # 	for i in lst:
# # 		if type (i) == int :
# # 			count += 1
# # 	return count
# # print(num_ints(lst))








# # def despace(s):
# # 	'''
# # 	Return:s but with its spaces removed.

# 	# Parameter s:it is string.
# 	# precondition:
# # 	'''
# # 	str1 = ''
# # 	for i in s:
# # 		if i == ' ':
# # 			i = i.strip()
# # 		str1+=i
# # 	return str1
# # print(despace('a b c'))





# # def reverse(s):
# # 	'''
# # 	Return
# # 	'''
# # 	s=s[::-1]
# # 	rever=''
# # 	for i in s :
# # 		rever+=i

# # 	return rever
# # print(reverse('abc efg'))



# # def reverse(s):
# # 	result=''
# # 	for x in s[::-1]:
# # 		if not(x==' '):
# # 			result=result+x
# # 	return result
# # print(reverse('la nos'))






# # def reverse(s):
# # 	result = ''
# # 	for x in s:
# # 		result = x + result
# # 	return result
# # print(reverse('la nos'))




# # lst=[5,2,6]

# # def copy_add_one(lst):
# # 	"""
# # 	Return:copy with 1 added to every element.

# # 	Paramater lst:List given by user.
# # 	Precondition:lst is a list of all numbers(either float or ints)
# # 	"""
# # 	result = []   # Here we are creating empty list(accumulator).

# # 	for x in lst :
# # 		x = x + 1   #Here we are incriminating the every value of list.
# # 		print(id(result))
# # 		# result = result + [x] 
# # 		result.append(x)
# # 		print(id(result))   
# # 	return result

# # lst1 = (copy_add_one(lst))
# # # print(id(lst))
# # print(lst1)






# # def hello(n):
# # 	str1=['hello world']*n
# # 	for i in str1:
# # 		print(i)

# # hello(5)



# # def hello(n):
# # 	for i in range(n):
# # 		print('Hello World!')
 
# # hello(5)






# # def sum_square(n):
# # 	x = 0
# # 	for i in range(-10,-11):
# # 		i = i ** 2
# # 		x = i + x
# # 	return x

# # print(sum_square(0))




# # def partition(s):
# # 	'''
# # 	Return:
# # 	'''
# # 	word=''
# # 	word1=''
# # 	for i in range(len(s)):
# # 		# word= i + word
# # 		if i % 2 == 0:
# # 			word =  word + s[i]
# # 		if i % 2 !=0:    # we can also use else here.
# # 			word1 = word1 + s[i]
			

# # 	return [word,word1]

# # print(partition('abcd'))
# # print(partition('abcdefrtjgn'))









# # lst=[1,2,3,4]
# # def add_one(lst):
# # 	for i in range(len(lst)):
# # 		lst[i]=lst[i]+1
# # 	print (lst)
# # add_one(lst)






# # def fabonacii(n):
# # 	'''
# # 	Return:List of fabonnacii series.

# # 	input-output example:-
# # 	1.) fabonacii(0) gives 'error'
# # 	2.) fabonacii(1) gives '[0]'
# # 	3.) fabonacii(2) gives '[0,1]'
# # 	4.) fabonacii(3) gives '[0,1,1]'

# # 	Parameter n:user input of fabonacii series.
# # 	Precondition:user must input positive interger.
# # 	'''
# # 	lst=[0,1]
# # 	if n == 0:
# # 		return 'error'
# # 	elif n == 1 :
# # 		return [0]
# # 	elif n == 2 :
# # 		return [0,1]
# # 	else:
# # 		for i in range(2,n):
# # 			lst.append(lst[i-2]+lst[i-1])
# # 			# lst[i]=lst[i]+i
# # 		return (lst)
# # print(fabonacii(3))




# def fabonacii(n):
# 	'''
# 	Return:List of fabonnacii series.

# 	input-output example:-
# 	1.) fabonacii(0) gives '0'
# 	2.) fabonacii(1) gives '0'
# 	3.) fabonacii(2) gives '1'
# 	4.) fabonacii(3) gives '1'
# 	5.) fabonacii(4) gives '2'

# 	Parameter n:user input of fabonacii series.
# 	Precondition:user must input positive interger.
# 	'''
# 	lst=[0,1]
# 	if n == 0:
# 		return 'error'
# 	elif n == 1 :
# 		lst =[0]
# 	elif n == 2 :
# 		lst=[0,1]
# 	else:
# 		for i in range(n-2):
# 			lst.append(lst[i]+lst[i+1])
# 	lst=lst[::-1]
# 	return lst[0]
# print(fabonacii(4))







def is_even_odd(x):
	if x % 2 == 0:
		print('even')

	else:
		# return 'odd'
		print('odd')


# print(is_even_odd(5))

x = is_even_odd(7)
print(x)

for 
