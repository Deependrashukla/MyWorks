import sys
# sys.setrecursionlimit(100000000)
def factorial(n):
	if n == 0 :
		return 1


	try:
		assert n >= 0 ,str(n) + 'is not a positive integer.' 
		# return n * factorial(n - 1)
	except:
		# return (n + 1) * factorial(n - 1)
		return ('you putted wrong number.')
	return n * factorial(n - 1)

print(factorial(8))