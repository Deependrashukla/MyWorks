import sys
sys.setrecursionlimit(100000000)
def factorial(n):
	# if n == 0 :
	# 	return 1
	assert type(n) == int, str(n) + 'is not an integer'
	assert n > 0 , str(n) + 'is negative'
	return n * factorial(n - 1)

# print(factorial(-1))