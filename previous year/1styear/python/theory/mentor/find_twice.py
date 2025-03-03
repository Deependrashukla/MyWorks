"""
This function tells that any number is twice or not in a list.

Author :Kirtan Khichi.
"""
#Here i am creating a list which taking input from user.
numbers = [float(input('Enter the first number: ')), float(input('Enter the first number: ')), float(input('Enter the first number: ')),float(input('Enter the first number: ')), float(input('Enter the first number: '))]

def find_twice_one(lst) :
	'''
	Returns: The number which is appears twice in given five numbers. 
	Float and Integer vlues will be considered same i.e 6.0 equal to 6 numbers with diffrent sign will be considered different. 

	Parameters lst : This one is list containing all five numbers.
	Precondition : This must be list type.

	'''
	lst.sort() 
	for x in range(len(lst) - 1 ) :
		if lst[x] == lst[x + 1] :
			return lst[x]
	return 'No double value is present'

print(find_twice_one(numbers))
