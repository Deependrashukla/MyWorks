"""
This function return two number from list whose sum is equal to sum value given by user.
"""

list_input = int(input('Enter your input that how much element you want to insert in list: '))
lst = []
for i in range(list_input) :
	list_element = int(input('Enter your element for in list: '))
	lst.append(list_element)

sum_element = int(input('Enter your sum of two elements: '))

def two_sum(sum_element) :
	"""
	Return two number from list whose sum is equal to sum value given by user.Otherwise None.

	Parameter sum_element: sum value given by user.
	Precondition : Value must be integer. 
	"""
	for i in lst :
		for j in lst :
			if i + j == sum_element :
				return (i, j)

print(two_sum(sum_element))
