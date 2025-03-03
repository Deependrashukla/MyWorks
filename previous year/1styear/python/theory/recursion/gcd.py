call = 0
def gcd(a, b) :
	"""
	Return :The greatest common factor between two numbers.

	Here we have two number and we are calculating gratest common factor.l

	Parameter a :

	Test cases :
	>>> gcd(5, 2)
	1
	>>> gcd(10, 0)
	5
	>>> gcd(0, 0)
	0
	>>> gcd(5, 5)
	5
	>>> gcd(10, 5)
	5
	"""
	global call
	
	# Base case.
	if a == 0 :
		return b

	elif b == 0 :
		return a
	   
	# r = a % b    # Remainder of the numbers. 

	a, b = b % a, a    # Here we are using Euclidian algorithms. 

	call += 1    # Here we are calculating call frames.

	# Recursive case.

	# return gcd(b, r)
	return gcd(a, b)
print(gcd(5, 2))
print(call)