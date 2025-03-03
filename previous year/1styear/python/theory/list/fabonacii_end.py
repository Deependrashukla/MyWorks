def fabonacii(n):
	'''
	Return:List of fabonnacii series.

	input-output example:-
	1.) fabonacii(0) gives '0'
	2.) fabonacii(1) gives '0'
	3.) fabonacii(2) gives '1'
	4.) fabonacii(3) gives '1'
	5.) fabonacii(4) gives '2'

	Parameter n:user input of fabonacii series.
	Precondition:user must input positive interger.
	'''
	lst=[0, 1]
	if n == 0:
		return 'error'
	elif n == 1 :
		lst =[0]
	elif n == 2 :
		lst=[0, 1]
	else:
		for i in range(n - 2):
			lst.append(lst[i] + lst[i + 1])
	lst=lst[::-1]
	return lst[0]
print(fabonacii(3))