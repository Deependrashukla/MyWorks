"""
This function returning the sum of all elements in list including sum of sub lists also.

Author :Kirtan Khichi
Date :28 January,2023
"""

lst = [1, 2, [1, 2], [4, 5, 6], [7, 8, 9], 10]

def sum_recursion_list(lst) :
	"""
	Return :The sum of elements in list including the elements of sub-list.
	"""
	total = 0    # Accumalator

	for i in lst :

		if type(i) == list :

			# Recursive case
			
			total = total + sum_recursion_list(i)

		else :
			total = total + i 

	return total

print(sum_recursion_list(lst))