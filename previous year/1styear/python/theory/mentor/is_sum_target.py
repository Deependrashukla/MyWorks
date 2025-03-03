"""
This function return True if sum of any two numbers of three is equal to target number otherwise false.

Author :Kirtan Khichi
"""
# Creating list of input from user
numbers = [float(input("Enter first number: ")), float(input("Enter second number: ")), float(input("Enter third number: "))]
target_num = float(input("Enter your target number: "))

def is_sum_equal_target(numbers, target_num) :
	'''
	Returns: True if sum of any two numbers of three is equal to target number otherwise false

	Sum is calculated of absolute values of numbers.Sum will be equated with absolute value of target numbers

	paramteres numbers:It is list of all three numbers to check sum
	precondition:It is list type having only numerical datatype.

	parameters target_num: It is numbers to with which sum to be equated
	precondition:It is number

	'''
	num1 = abs(numbers[0])
	num2 = abs(numbers[1])
	num3 = abs(numbers[2])
	t_num= abs(target_num)
	
	return num1 + num2 == t_num or num1 + num3 == t_num or num2 + num3 == t_num

print(is_sum_equal_target(numbers, target_num))