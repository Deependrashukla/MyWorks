# call = 0
# def gcd(a, b) :
# 	"""
# 	Return :The greatest common factor between two numbers.


# 	"""
# 	global call
	
# 	# Base case.
# 	if a == 0 :
# 		return b

# 	elif b == 0 :
# 		return a
	   
# 	r = a % b    # Remainder of the numbers. 

# 	call += 1    # Here we are calculating call frames.

# 	# Recursive case.

# 	return gcd(b, r)
# print(gcd(5,50))
# print(call)


# i = 1
# def fact_gcd(x) :

# 	global i

# 	# if x % i == 0 :
# 	# 	return x

# 	i += 1

# 	return x / i

# def gcd(a, b) :

# 	r = a % b

# 	if a == 0 :
# 		return b

# 	elif b == 0 :
# 		return a

# 	elif fact_gcd(a // 2) == fact_gcd(b // 2 ):
# 		return fact_gcd(a)

# 	return 1

# print(gcd(48, 2))