def sqrt(c) :
	x = c/2
	while abs(x**2 - c) > 1e-13 :
		x = x/2 + c/(2*x)
		print(x)

	return x

print(sqrt(4))
import math 
print(math.sqrt(4))
