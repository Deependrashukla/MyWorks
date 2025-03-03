def triangle_recursion(n) :
	"""
	Prints the triangle 
	"""
	if n <= 0 :
		return ''

	print(n * '*')
	triangle_recursion(n - 1)

triangle_recursion(5)