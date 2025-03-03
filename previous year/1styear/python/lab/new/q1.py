num1 = int(input('enter your first number :- ')) #number given by user.
num2 = int(input('enter your second number :- ')) #number given by user.
def number(num1,num2):
	'''
	Return true if either a,b equal to 6 or if sum or difference is equal to 6.
	otherwise False
	'''
	return num1 == 6 or num2 == 6 or (num1 + num2) == 6 or abs(num1 - num2) == 6
print(number(num1,num2))