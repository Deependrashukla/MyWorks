call = 0
def is_sorted(lst) :
	global call
	"""
	Return :True if list element in increaisng order, otherwise gives False.

	Test-Cases :-
	>>> is_sorted([1, 2, 3, 4])
	True
	>>> is_sorted([3, 2, 1])
	False
	"""

	# Base Case
	if len(lst) == 1 :
		return True

	left = lst[0] <= lst [1]

	# Recursive case
	call += 1
	
	right = is_sorted(lst[1:])

	return left and right 

print(is_sorted([1, 2, 3, 5, 7]))
print(call)