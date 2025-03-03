def fabonacii(n):
	'''
	Return:List of fabonnacii series.

	input-output example:-
	1.) fabonacii(0) gives 'error'
	2.) fabonacii(1) gives '[0]'
	3.) fabonacii(2) gives '[0,1]'
	4.) fabonacii(3) gives '[0,1,1]'

	Parameter n:user input of fabonacii series.
	Precondition:user must input positive interger.
	'''
	lst=[0, 1]
	if n == 0:
		return 'error'
	elif n == 1 :
		return [0]
	elif n == 2 :
		return [0, 1]
	else:
		for i in range(2, n):
			lst.append(lst[i - 2] + lst[i - 1])
			# lst[i]=lst[i]+i
		return (lst)
print(fabonacii(3))